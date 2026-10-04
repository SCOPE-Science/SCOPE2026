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

The proof was replayed from the exact conditional law of the dominant uniform summand. When \(t<a_1-r(a)\), every conditional central interval lies strictly inside \([-a_1,a_1]\), so its probability is exactly \(t/a_1\), independently of the residual weights. A coupling bound gives uniform convergence of the full tail ratio to the one-uniform ratio as \(r(a)\to0\), allowing the prior uniqueness of \(t_0\) to localize the global maximizer.

For the localized ratio, differentiating gives the critical equation \(a_1=t+h(t)\). The standard-normal Mills-ratio derivative yields \(h'(t)=3t h(t)-1\), hence \((t+h(t))'=3t h(t)>0\). The implicit-function and envelope derivatives then give the displayed threshold and sharp-constant expansions.

The standalone `verify.py` uses only the Python standard library. It returns `VERIFY_OK`, reproduces \(t_0=0.6429083350319993\), \(C_*=1.3451182120491867\), \(\kappa=1.2108763588856895\), and the threshold-shift coefficient \(0.7259721828638812\). It also compares the local formula with exact inclusion-exclusion CDFs for several three- and four-summand weighted-uniform laws. These computations stress-test the formulas but are not substitutes for the analytic localization proof.

The scientific comparison inspected the lead arXiv full text, the full available text of the distributional-stability article, and the full PDF of the \(\ell_p\)-section stability paper, together with targeted searches. No independent validation has been performed.
