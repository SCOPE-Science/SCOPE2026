---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The accompanying `verify.py` is standalone Python 3 and requires only the standard library. Run `python verify.py` in the directory containing this file. The script separately enumerates all increasing subsequences for the Rips grade, computes the longest-path recurrence, and verifies the interval certificate. On the small integer matrices it searches every integer Cho parameter vector with smaller or equal total to check exact integer optimality; the proof in `RESULT.md` establishes optimality for all nonnegative real parameters.

**Observed execution:** `PASS: 1510 directed upper-triangular dissimilarity matrices, including exhaustive integer Cho optima and journal counterexample.` It also reports the four-vertex radius-four certificate \((1,3,\sqrt6)\). The coverage comprises all upper-triangular arrays with values \(0,1,2\) through tuple length four, seeded arrays through length seven, and the direct example. An additional independent numerical test checked 1,800 tuples for exponents \(p\) including \(p<1\); that auxiliary experiment is not necessary for replaying the proof or the standalone script.

**Proof-only steps:** The recurrence's characterization of the maximum path weight, the telescope \(D_j-D_i\ge G(v_i,v_j)^p\), and the reverse inclusion from disjoint interval sums prove the universal statement. Separate boundary checks handle \(p=\infty\), extended infinite weights, degree zero and infinite filtration scale. No finite computation is presented as a proof of an infinite statement.

**Limits:** This is a review of the supplied proof and computations. It is not an independent mathematical audit and does not prove literature uniqueness. Prior metric-space certificate constructions are close and should be compared in an external novelty review.
