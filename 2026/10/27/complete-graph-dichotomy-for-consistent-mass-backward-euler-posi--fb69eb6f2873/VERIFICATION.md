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
# Reproducibility and scope

Run `python verification/check.py` in Python 3 with NumPy, SymPy and NetworkX. Reproduced observations: 995 connected unlabeled atlas graphs on two through seven vertices; 10,945 floating-point tests of entry signs and row sums at eleven normalized step sizes; 330 fully rational tests on 30 connected graphs of up to five vertices; and four symbolic complete-graph spectral identities. The checker does not certify all graph orders or a continuum of steps: those conclusions are established by the proof's inverse-Stieltjes argument. The public source manuscript arXiv:1209.5657 was read at its introduction, Theorem 3.1, selected mesh analyses and concluding discussion; arXiv:1510.02825 at its introduction, Theorems 4.1–4.3 and numerical discussion. The 2008 Thomée–Wahlbin article was only accessible as an abstract, so specialized prior overlap remains a residual uncertainty. Independent audit has not been performed.
