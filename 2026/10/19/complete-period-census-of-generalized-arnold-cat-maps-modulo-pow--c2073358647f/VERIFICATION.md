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

The global period is the order of the matrix, not a single point's orbit length. For x=pq, Cayley–Hamilton gives A^2=(2+x)A−I; reduction mod 3 is respectively identity, nonidentity unipotent, a matrix squaring to −I, or the negative of a nonidentity unipotent, yielding exact base orders 1,3,4,6. Direct substitution gives A^3−I=(x+3)((x+1)A−I), A^4−I=(x+2)A(A^2−I), and A^3+I=(x+1)((x+3)A−I). Unit off-diagonal entries and, when used, invertible factors modulo 3 ensure exact rather than lower-bound depth. For r=1 the off-diagonals already exhibit the minimum. If A^r=I+3^s C with a unit entry in C and s<e, cubing increases the minimum valuation exactly by one and powers prime to three preserve it; depth e needs no lifting. For r=1 subtract consecutive squares of residue-subgroup cardinalities. In the other cases each product has 2φ(3^e) ordered factorizations with exactly one unit or φ(3^e) with both units. The valuation shells around −3, −2, −1 have 2·3^(e−s−1) residues for s<e and one at s=e. This gives the joint counts, including merged periods from r=1 and 3. The maximum 6·3^(e−1) is unique to (r,s)=(6,1); there are two maximizing pairs at e=1 and 4·3^(2e−3) otherwise. Independent direct multiplication, not the uploaded verifier, matched all pairs at e=1 and 2; for e=2 the observed histogram was 1:1, 3:20, 4:6, 6:6, 9:24, 12:12, 18:12.

## originality

PASS

The supported distinct claim is the exact joint census in the specified two-parameter slice over 3^e, including scalar reductions and the maximal-period fraction, not the order-lifting mechanism. The closest older preprint yields closely related ambient transitions; its count alone does not specialize to counts in this slice. Access limits for two precise family references remain explicit.

## value

PASS

The full parameter sample is the same natural two-parameter cat-map family studied for period distributions, and the base prime 3 is outside the stated p>3 prime-power result. The distinction between ambient lifts and restricted parameters matters in counting how often the longest global return actually occurs. The exact valuation rule and census account for period collisions and give a uniform quantitative selection statistic beyond individual period or lifting recipes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
