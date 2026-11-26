---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Smoothness holds even in characteristic two: writing A=X^(q+1)Y, B=Y^(q+1)Z, D=Z^(q+1)X, the three partial derivatives multiplied by their variables are A+D, A+B, B+D. At a singular point their simultaneous vanishing and the curve equation force A=B=D=0, so the point is a coordinate point, where a partial derivative is nonzero. The degree-(q−1) adjoint basis has q(q+1)/2 terms. For a one-shot check let m=p^r, r≤e. Applying Cartier r times to the basis numerator is equivalent to expanding F^(m−1)x^iy^j, selecting exponent residues (m−1,m−1) modulo m, and taking the m-th roots after dividing exponents accordingly. This follows by composing coefficient extractors with F^(p^r−1)=F^(p−1)(F^(p^(r−1)−1))^p. Since q is a multiple of m, the only possible term has trinomial second and third multiplicities B=i mod m, D=j mod m, and A=m−1−B−D. The coefficient is nonzero exactly when all r low digit pairs are carry-free, by the base-p factorization of the trinomial power. Its target is (floor(i/m)+(q/m)A, floor(j/m)+(q/m)B), which stays in the basis and recovers all source digits, so distinct nonzero images are linearly independent even with semilinearity. The r low digit pairs give T^r choices and the remaining triangular index condition gives (q/m)(q/m+1)/2 choices. The rank at e−1 equals the rank at e; the nested images then coincide and stay equal under further applications. The stable rank is the p-rank. The one-step partial bijection decomposes into cycles and finite strings; a length-j string contributes max(j−r,0) to the r-th rank, giving the second differences. For e≥2 the last positive drop, from e−2 to e−1, is T^(e−2)p^2(p−1)^2/4; e=1 is ordinary with no strings. No full Ekedahl–Oort classification is inferred.

## originality

PASS

The Hurwitz first rank, standard Cartier machinery, digit-filtration methods for Hermitian curves, and a general character-permutation description that applies to this tame Fermat quotient are all prior. The distinct contribution supported by the comparison is the evaluated, uniform Hurwitz rank profile and its stabilization/string consequences—not the one-step formula, the general method, or the existence of a way to enumerate quotient characters. The general character rule gives a count for any input but does not itself evaluate the product or explain the exact cutoff; those use the Hurwitz-specific digit survival and triangular boundary.

## value

PASS

A natural infinite family now has a simple explicit full Cartier filtration: it determines the exact nonzero stable rank, the first stabilization point and all nilpotent lengths across all prime characteristics. For e≥3 it resolves intermediate ranks not fixed by the one-step or terminal information, without orbit enumeration on a larger covering curve. This is a precise invariant for studying the Jacobians' p-torsion, not an inference of their full polarized type.

The dated certificate retains the supplied scientific assessment, sources and limitations.
