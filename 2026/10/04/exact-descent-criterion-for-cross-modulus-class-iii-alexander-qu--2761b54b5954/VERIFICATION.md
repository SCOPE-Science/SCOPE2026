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
# Verification

The theorem was checked at four interfaces.

First, representative independence was proved directly. If \(b\) and \(b+r_j\) represent the same element of \(\mathbb Z_{r_j}\), their images differ by \((1-k_i)r_j\) in \(\mathbb Z_{r_i}\). This vanishes exactly under the stated divisibility condition.

Second, after descent, right translation by an element of fiber \(j\) restricts on fiber \(i\) to an affine map with linear part multiplication by \(k_j\). It is a permutation exactly when \(\gcd(k_j,r_i)=1\).

Third, right self-distributivity was expanded symbolically. Both sides reduce to
\[
k_\ell k_j a+(1-k_i)k_\ell b+(1-k_i)c.
\]
Thus no hidden compatibility condition is omitted once all cross terms are legitimate.

Fourth, the embedded standalone checker exhaustively explores small two-fiber systems, compares the pairwise and least-common-multiple criteria, produces representative-dependence witnesses on descent failures, checks nonbijective right translations on unit failures, and verifies all quandle axioms whenever the theorem predicts success. Its output is:

`VERIFY_OK systems=484 criterion_true=160 checked_quandles=160 descent_failure_witnesses=318 example7.3=PASS example7.5_k2_k3_k4=FAIL_DESCENT`

The source examples are included as explicit regression tests: Example 7.3 passes; Example 7.5 with \(k=2,3,4\) fails canonical quotient descent.

Finite tests are not used as proof of the infinite statement. The conclusion about Example 7.5 is not a claim that its printed Cayley tables fail the quandle axioms; it concerns whether those tables arise canonically from the literal quotient-module expression without extra cross-fiber data.

The independent-audit channel has not been performed.
