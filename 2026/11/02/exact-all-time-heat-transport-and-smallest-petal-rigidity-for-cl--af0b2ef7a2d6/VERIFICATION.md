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

# Verification of the heat-transport theorem

Run `python verify.py` with a standard Python interpreter (stdlib only). The checker reconstructs each graph and its Laplacian, explicitly constructs and checks each rational eigenspace projector, and computes the heat kernel at \(t=\log 2\) and \(t=\log 3\) by the projected spectral formula. It independently maximizes \(\sum_v [H_t(x,v)-H_t(y,v)]f(v)\) over anchored integral one-Lipschitz potentials for every pair. This is exhaustive at each finite instance: graph incidence/difference constraints are totally unimodular, and fixing the hub potential to zero restricts each integer leaf value to \(-1,0,1\); each clique's potentials must have spread at most one. The checker also recomputes the actual-edge maximum to compare the asserted sharp norm.

Actual execution output: `CERTIFICATE_OK compositions= 255 exact_rational_heat_instances= 510 W1_pairwise_dual_comparisons= 14846`.

The infinitely many integer profiles and continuously many times are handled by the explicit analytic eigenspace, sign, coupling, duality and calculus arguments in `RESULT.md`. The finite checks are diagnostic replay, not an exhaustive proof of an infinite statement. Independent scientific audit has not been performed.
