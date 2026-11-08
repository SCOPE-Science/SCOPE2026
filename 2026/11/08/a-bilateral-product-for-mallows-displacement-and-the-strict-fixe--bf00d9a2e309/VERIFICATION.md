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

# Reproducibility and limits

Run `python verify.py` with Python 3.9 or newer; no third-party package is needed. It checks four rational parameter values against the exact finite versions of the cited displacement sum and derived product, with rigorous upper bounds on errors from truncating the double sum, Pochhammer normalization, and Euler product. Output for the four tests ends in `OK`, followed by `Exact-rational finite diagnostics passed; analytic proof required for all real q.`

The check's mathematical assumptions include the known joint-index displacement law of Gnedin–Olshanski. For the original double sum truncated at \(0\le r,\ell\le N\), both inversion-count marginals are geometric with \(\Pr(R>N)=\Pr(L>N)=q^{N+1}\), so the missing probability is at most \(2q^{N+1}\). The Pochhammer tail is at most \(q^{M+1}/(1-q)\), and the omitted logarithmic product is at most \(4q^{M+1}/((1-q)(1-q^{M+1}))\). These finite bounds justify the checks but are not a substitute for the generating-function derivation. Full infinite-parameter correctness follows from the proof in `RESULT.md`, including the q-binomial identity's analytic derivation.

The source distribution and the finite-cycle limiting identification were proved in earlier publications; they are cited rather than reverified here. Historical priority and the full text of a related dissertation chapter remain outside the verified scope. No independent audit has been conducted.
