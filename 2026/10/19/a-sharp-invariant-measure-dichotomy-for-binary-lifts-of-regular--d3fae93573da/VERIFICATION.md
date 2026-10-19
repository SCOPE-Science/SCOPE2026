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
# Mathematical verification

The stated recursion has exact level incidence \(M_k=q_k^{-1}((q_k-1)I+J)\), where \(J\) interchanges the two phases. Its constant and difference eigenvalues are respectively \(1\) and \(1-2/q_k\), verified by symbolic algebra in the proof. The tower-measure inverse limit is determined by compatible probability vectors; ambiguities at all skeleton levels have zero probability because their upper frequency is bounded by one over \(p_k\).

The standalone `verify.py` was executed against the public-source recursion using Python 3, with **804 exact assertions**. It tests seven initial periods, ten period ratios, checks \(4^4\) four-stage matrix compositions via rational fractions and three sample nested recursions. The console result was `PASS 804 exact assertions; all sampled incidence matrices and symbolic blocks agree`. This finite check cannot establish the theorem for arbitrary infinite sequences, which is proved analytically.

Primary source: Kang–Jäger, arXiv:2609.01140v1. General finite-rank incidence framework: Bezuglyi–Karpel–Kwiatkowski, arXiv:1709.00055v3. No independent audit was undertaken.
