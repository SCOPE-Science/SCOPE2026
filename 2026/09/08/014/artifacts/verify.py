#!/usr/bin/env python3
"""Exact integral cochain-level verification of the corrected SCOPE014 witness.

The degree-2 Magnus/Fox coefficients are used ONLY for cups of cocycles.
Triple Massey products use Dwyer's U4(Z)/center defining-system model.
Run: python verify.py --check (default), or --write to regenerate results.json.
"""
import json
import sys
from pathlib import Path

WORDS = {
    "r1": "xxyzYZyzYZ",            # x^2 [y,z]^2
    "r2": "xzXZ",                  # [x,z]
    "r3": "xyXYzyxYXZ",            # [[x,y],z]
}
LETTERS = "xyz"
TRIPLES = ("YYY", "YYZ", "YZY", "YZZ", "ZYY", "ZYZ", "ZZY", "ZZZ")


def poly_mul(a, b):
    out = {}
    for u, cu in a.items():
        for v, cv in b.items():
            w = u + v
            if len(w) <= 2:
                out[w] = out.get(w, 0) + cu * cv
    return out


def magnus(word):
    p = {"": 1}
    for c in word:
        u = c.lower()
        factor = {"": 1, u: 1} if c.islower() else {"": 1, u: -1, u + u: 1}
        p = poly_mul(p, factor)
    return p


def eye():
    return [[int(i == j) for j in range(4)] for i in range(4)]


def mat(entries):
    a = eye()
    for (i, j), v in entries.items():
        a[i - 1][j - 1] = v
    return a


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


def inv(a):
    n = [[a[i][j] - int(i == j) for j in range(4)] for i in range(4)]
    n2, n3 = mul(n, n), mul(mul(n, n), n)
    return [[int(i == j) - n[i][j] + n2[i][j] - n3[i][j] for j in range(4)] for i in range(4)]


def eval_word(word, images):
    a = eye()
    for c in word:
        g = images[c.lower()]
        a = mul(a, g if c.islower() else inv(g))
    return a


def central_only(a):
    return all(a[i][j] == int(i == j) for i in range(4) for j in range(4) if (i, j) != (0, 3))

class Polynomial:
    """Exact Z[a,b,c,d,e,f,u,v,p,q,X,Y,Z], not a finite parameter sample."""
    variables = 13

    def __init__(self, value=0):
        self.terms = ({k: v for k, v in value.items() if v} if isinstance(value, dict)
                      else ({(0,) * self.variables: value} if value else {}))

    @classmethod
    def variable(cls, i):
        exponent = tuple(int(j == i) for j in range(cls.variables))
        return cls({exponent: 1})

    def __add__(self, other):
        other = other if isinstance(other, Polynomial) else Polynomial(other)
        terms = self.terms.copy()
        for k, v in other.terms.items():
            terms[k] = terms.get(k, 0) + v
        return Polynomial(terms)

    __radd__ = __add__

    def __neg__(self):
        return Polynomial({k: -v for k, v in self.terms.items()})

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        other = other if isinstance(other, Polynomial) else Polynomial(other)
        terms = {}
        for k, v in self.terms.items():
            for kk, vv in other.terms.items():
                exponent = tuple(a + b for a, b in zip(k, kk))
                terms[exponent] = terms.get(exponent, 0) + v * vv
        return Polynomial(terms)

    __rmul__ = __mul__

    def __eq__(self, other):
        other = other if isinstance(other, Polynomial) else Polynomial(other)
        return self.terms == other.terms


def symbolic_defining_systems():
    # Six arbitrary H1 coefficients, four arbitrary second-superdiagonal
    # generator entries, and three arbitrary central lift entries.
    a, b, c, d, e, f, u, v, p, q, X, Y, Z = (
        Polynomial.variable(i) for i in range(13))
    images = {
        'x': mat({(1, 3): -(a*e-d*b), (2, 4): -(b*f-e*c), (1, 4): X}),
        'y': mat({(1, 2): -a, (2, 3): -b, (3, 4): -c,
                  (1, 3): u, (2, 4): v, (1, 4): Y}),
        'z': mat({(1, 2): -d, (2, 3): -e, (3, 4): -f,
                  (1, 3): p, (2, 4): q, (1, 4): Z}),
    }
    evaluated = [eval_word(word, images) for word in WORDS.values()]
    assert all(central_only(r) for r in evaluated)
    assert evaluated[1][0][3] == a*e*f - 2*d*b*f + d*e*c
    assert evaluated[2][0][3] == 0
    assert all(v % 2 == 0 for v in evaluated[0][0][3].terms.values())
    # Changing only the central x lift changes the first relator by 2X.
    coefficient = evaluated[0][0][3].terms.get(tuple(int(i == 10) for i in range(13)))
    assert coefficient == 2


def compute():
    mag = {name: magnus(word) for name, word in WORDS.items()}
    exponent = [[mag[name].get(i, 0) for i in LETTERS] for name in WORDS]
    second = [[[mag[name].get(i + j, 0) for j in LETTERS] for i in LETTERS] for name in WORDS]
    assert exponent == [[2, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert second == [
        [[1, 0, 0], [0, 0, 2], [0, -2, 0]],
        [[0, 0, 1], [0, 0, 0], [-1, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]
    cups = {}
    for u, v in ("YY", "YZ", "ZY", "ZZ"):
        ui, vi = LETTERS.index(u.lower()), LETTERS.index(v.lower())
        vector = [a[ui][vi] for a in second]
        assert vector[1:] == [0, 0] and vector[0] % 2 == 0
        cups[u + v] = vector
    central = {}
    middle = {}
    for triple in TRIPLES:
        a, b, c = (int(t == "Y") for t in triple)
        d, e, f = (int(t == "Z") for t in triple)
        x13, x24 = -(a * e - d * b), -(b * f - e * c)
        images = {
            "x": mat({(1, 3): x13, (2, 4): x24}),
            "y": mat({(1, 2): -a, (2, 3): -b, (3, 4): -c}),
            "z": mat({(1, 2): -d, (2, 3): -e, (3, 4): -f}),
        }
        evaluated = [eval_word(word, images) for word in WORDS.values()]
        assert all(central_only(r) for r in evaluated)
        vec = [r[0][3] for r in evaluated]
        assert vec[1] == a * e * f - 2 * d * b * f + d * e * c
        assert vec[2] == 0
        central[triple] = vec
        middle[triple] = vec[1]
    assert middle == {"YYY": 0, "YYZ": 0, "YZY": 0, "YZZ": 1,
                      "ZYY": 0, "ZYZ": -2, "ZZY": 1, "ZZZ": 0}
    return {
        "presentation": WORDS,
        "exponent_matrix": exponent,
        "second_magnus_fox_matrices": second,
        "cocycle_cups": cups,
        "coboundary_image": "(2Z,0,0)",
        "triple_central_relator_vectors": central,
        "triple_middle_coordinates": middle,
        "strict_nonzero_triples": [k for k, v in middle.items() if v],
        "method": "Dwyer U4(Z)/center defining-system obstruction; no non-cocycle Fox cup shortcut",
    }


def main():
    path = Path(__file__).with_name("results.json")
    actual = compute()
    symbolic_defining_systems()
    if len(sys.argv) == 2 and sys.argv[1] == "--write":
        path.write_text(json.dumps(actual, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    elif len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] == "--check"):
        expected = json.loads(path.read_text(encoding="utf-8"))
        assert actual == expected, "committed results.json differs from exact recomputation"
    else:
        raise SystemExit("usage: python verify.py [--check|--write]")
    print("VERIFY_OK: corrected U4 integral triple table and cocycle cups")
    print("SYMBOLIC_OK: all integer H1 coefficients and every free defining-system/lift entry")


if __name__ == "__main__":
    main()
