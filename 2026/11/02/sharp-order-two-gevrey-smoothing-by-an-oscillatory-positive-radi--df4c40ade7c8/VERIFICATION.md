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

# Reproducibility checks and scope

The coefficient identities follow from the exact monomial norms and the integral representation of Tricomi's function. Their asymptotic error uses DLMF Eq. 13.8.11 with its leading Bessel term and the large-argument Bessel expansion. The Gevrey lower exclusion requires an infinite cosine phase subsequence and is established analytically.

The accompanying `checker.py` is self-contained apart from the `mpmath` package. Running `python checker.py` performs 45 finite assertions on exact special-function values, asymptotic envelopes, and representative phase subsequences over three fixed parameter families. It does not constitute a uniform or infinite-degree proof, and it is not independent mathematical validation.

The weight is positive only because the assumed perturbation magnitude is strictly less than one. A global order-two threshold is claimed only for nonzero perturbations, not for the unperturbed reference kernel. An independent audit has not been performed.
