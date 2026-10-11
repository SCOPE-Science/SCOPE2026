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
The proof was replayed from the source hypotheses rather than from numerical experiments.

The scale calculation was checked in three exhaustive cases. With \(b_j\le a_j/s\) and \(a_{j+1}\le b_j/s\), both scale sequences decrease by at least \(s^2\). The first tail is a geometric series with ratio \(s^{-2(q-p)}\), the third tail has ratio \(s^{-2p}\), and the middle set has at most one index. If the middle set is empty and both tails occur, their adjacent boundary ratios multiply to at most \(1/s\), which forces one of them below \(s^{-1/2}\). These facts give the displayed \(G_s\) and \(G_s\to1\).

The detector recursion was checked against the actual source lemma: finite-support recovery remains valid for every sufficiently small \(b\), not merely for one chosen value, so imposing \(b_j\le a_j/s\) preserves recovery. Kalton's property allows the next \(a_j\) to be chosen arbitrarily small relative to the preceding \(b_{j-1}\). The remaining quantitative-selection inequalities are unchanged after replacing the published assembly norm by \(G_s^{1/p}\).

Limits: the argument needs \(q-p>0\), gives no endpoint result at \(q=p\), and proves no optimality statement for \(\Gamma_p\). No independent audit has been performed.
