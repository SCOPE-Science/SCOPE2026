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
# Verification of exact three-point free-\(p\) inclusion constant

The analytic argument is in `RESULT.md` and uses the publicly available finite spanning-tree norm formula (Cúth--Raunig, arXiv:2311.02920v1, Theorem 2.2) and finite-subset infimum (Fact 1.1). All quantifiers include arbitrary ambient pointed p-metric superspaces. The crucial independent calculations are: (i) tree reduction to a three-terminal weighted median; (ii) `b_i>0` by strict p-subadditivity for 0<p<1; (iii) the identity `F=1/(t-1)+(t+s^2)/(1-s^2)` and the fact that `t+1/(t-1)` decreases on `(1,2)`; (iv) the explicit shortest-path ρ-star equality at the two possible hub types.

The accompanying standard-library script `three_terminal_median_check.py` enumerates every labelled spanning tree on three through five vertices for prescribed finite metrics, signed three-point measures, and p samples. It directly compares the median minimum with the tree norm cost; it also checks sharp-star sample ratios and the symbolic rational q=3/2 identity. Run it with `python3 three_terminal_median_check.py`. Expected output: `THREE_TERMINAL_P_FREE_MEDIAN_AND_SHARP_CONSTANT_CHECK_OK`.

Finite enumeration does not certify an infinite-dimensional theorem or a continuous p-parameter range; the general proof is analytic and relies on the correctly quoted primary theorem. No independent audit or external mathematical certification has been carried out.
