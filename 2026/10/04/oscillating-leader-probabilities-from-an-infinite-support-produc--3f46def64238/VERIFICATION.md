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

The proof is analytic and has no external computational dependency.

For the peak subsequence, write \(q=T_{k-1}\), so \(T_k=q^4\), \(p_k=q-q^4\), and \(N_k=q^{-4}\). Then
\[
(1-T_k)^{N_k}=(1-1/N_k)^{N_k}\to e^{-1}.
\]
Conditional on no value above \(k\), the level-\(k\) multiplicity has mean asymptotic to \(q^{-3}=N_k^{3/4}\), while the proof only asks for \(N_k^{2/3}\) ties. Two maximizing sets that large have conditional disjointness probability at most \(e^{-N_k^{1/3}}\).

For the trough subsequence \(M_k=q^{-3/2}\), the probability of any observation above \(k\) is at most \(q^{5/2}\), the no-level-\(k\) probability is at most \(e^{-M_kp_k}\) with \(M_kp_k\sim q^{-1/2}\), and the probability of any index simultaneously equal to \(k\) in both coordinates is at most \(M_kp_k^2\sim q^{1/2}\). Every error term therefore vanishes in the asserted direction.

Finite numerical values quoted in RESULT.md are consistency checks only. They are not certificates for the infinite statement and are not used in the proof.
