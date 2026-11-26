---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In residue r the possible (y,z) are partitioned by y+3z=r+jm, j≥0, and each such pair gives exactly one representation iff q≥j+y+z. For a given j the costs start at j+f(r+jm) and increase by 2 through floor((r+jm)/3)+1 choices. Writing t≡b mod 3 and m=3h+a gives f(t+m)−f(t)=h+a−2 floor((a+b)/3). It is nonnegative for m≥4 and at least one for m≥5, so j=1 is the earliest wrapped cost. If r≤2, layer zero has just one choice and the first wrapped cost is the threshold for two. If r≥3 and m≥5 the wrapped cost cannot precede the second layer-zero cost f(r)+2; the same holds at the only remaining case m=4,r=3 by f(7)=3. Thus the threshold formula includes ties and all small boundaries. In the large residues the maximum H−1 is h+2, whose last attainment is m−1 for a=0,2 or m−2 for a=1 when m≥5. The small residues have H−1≤h+2 and lower r, and direct substitution at m=4 gives (3,4,3,3) and F₁=13. Since f(m)+f(m+1)+f(m+2)=m+3, summing H gives Σf+3m−3, and excluding the single zero gives the positive count; summing the blocks f(3j+b)=j+b gives the three displayed quadratic formulas. A direct enumeration of distinct coin triples on both sides of each predicted threshold reproduced the boundary behavior for 4≤m≤36.

## originality

PASS

The p-Apéry framework, largest-gap and genus identities are known. The distinct contribution is the two-piece threshold array for all m≥4 in this non-arithmetic shifted family. The closest arithmetic-progression theorem does admit p=1 but not these generators; the ordinary shifted-monoid theorem has the generators but not the two-representation condition. No inspected source gave the entire array or implied it through an existing family formula.

## value

PASS

The first nontrivial generalized Apéry layer is a natural target already studied for arithmetic triples. Here the third denomination omits the next arithmetic shift, creating a real competition between two types of second representation. The exact threshold in every residue over an unbounded family decides uniqueness at any input and yields the generalized Frobenius and gap-count invariants, including the m=4 edge case. A largest-gap formula or first-representation computation alone would not answer that question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
