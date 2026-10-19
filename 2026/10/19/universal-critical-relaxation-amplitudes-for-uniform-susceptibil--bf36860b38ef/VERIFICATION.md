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

# Verification and scope

The analytical proof of the claimed limits is contained in `RESULT.md`; its key steps are the exact critical Lyapunov identity, simple-center spectral decomposition, logarithmically slow positive amplitude, and scalar reciprocal-amplitude integration. The executable `verify.py` checks representative cases with one, two and three stages using SciPy's implicit BDF solver to time \(T=200000\), compares predicted scaled limits, and checks a nontransmitting initial face. It also tests the exact Lyapunov derivative identity and critical eigenvector identities. Finite diagnostics are supplementary and do not establish the theorem for all matrices or initial conditions. The verified source text is the open article https://arxiv.org/pdf/2512.11003 and the earlier comparator https://sites.ualberta.ca/~myli/research/ps_files/multistage_2012.pdf. Independent mathematical validation has not been performed.
