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
# Reproducibility

Run `python verify_duads.py` and `python verify_symplectic.py` with standard-library Python 3. Both scripts are exact finite calculations using integer bit masks or rational weights and construct their graphs independently. The first builds 15 duads and 15 synthemes; the second builds 15 nonzero vectors and 15 isotropic two-spaces over the binary field. Both represent the unique \(\operatorname{GQ}(2,2)\) incidence graph.

The first script checks that no porous source set of size 1, 2 or 3 works, enumerates all \(\binom{30}{4}=27405\) four-source sets, finds exactly 45 porous feasible sets, and verifies the exact blocked-path weights of all 45. It compares the resulting list against all 45 geometric flags. The second independently enumerates porous four-source sets and uses blocking-aware shortest-path integer inequalities to verify all 45; it independently reconstructs the 45-state three-replacement graph. Both count the 450 one-intersection pairs, 540 disjoint pairs, degree twenty, and two-step maximum distance.

The representative blocked-weight multiset is \(\{9/8:16,21/16:8,3:2\}\); the minimum weight is \(\frac98>1\). Full content and output records are embedded, so no other-run files or external certificates are required. Finite enumeration is used only where the domain is explicitly finite; the analytic proof establishes why this exact 30-vertex census suffices for the claim. Independent external scientific audit has not been performed.
