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

Conditional on its uniform arrival time x, a tagged long edge pivots precisely if its b-1 companions have arrived and all m short paths remain incomplete. Integrating and aggregating gives the beta integral and product. For the normalized Banzhaf calculation the analogous independent-coalition factors give the short-to-long per-edge ratio (2^b-1)/(2^a-1); summing over ma short edges and b long edges gives the displayed share. The Shapley integrands differ by the strictly positive x^(a-1)(1-x^a)^(m-1)(1-x^(b-a)). With A=b/a and T=a(2^b-1)/(b(2^a-1)), the adjacent difference in (2^n-1)/n^2 has strictly positive numerator for n>=2, so T>A and R_1>1. The sign of R_(m+1)/R_m-1 is the opposite of A-T+(A-1)mT, strictly increasing in m, hence any plateau is at the peak above one. The gamma ratio yields R_m of order m^(1-A), which tends to zero; the boundary has at most one tie. Seven is minimal within the stated family after adding a short path since m>=2 and 2a+b>=7, not a claim about all simple graphs. New exact permutation and coalition enumeration verified both minimal-witness fractions and the 1/6 tie. The frozen certificate reports finite checks only; its 17040 pivotal count is the nominal total of edge/other-edge subsets, while the code skips states already winning, not 17040 separate swing evaluations. This accounting detail does not affect its fractions or the theorem.

## originality

PASS

The game class and computation of the two indices are established prior art. The supported distinct result is the aggregate physical path allocation crossing uniformly in both path lengths and the number of parallel alternatives, including its unique boundary and scoped smallest witness. Neither the inspected index algorithms nor the adjacent catalogue rankings give this parametric inequality.

## value

PASS

A sharp redundancy threshold compares two standard allocation methods on a motivated network observable. It separates aggregate path allocation from per-edge rankings, establishes a unique reversal rather than isolated counterexamples, and includes a sharp small witness and a genuine tie.

The dated certificate retains the supplied scientific assessment, sources and limitations.
