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

The replay command is `python verifier.py` from the artifact directory.

The verifier reconstructs the generalized Petersen graph \(G(10,2)\), forms the complete unordered two-particle discrete configuration complex, and checks the cell counts \((190,540,375)\). It proves the rational second-boundary rank is exactly \(339\) by combining two independent bounds: the supplied \(36\) integral kernel vectors give an upper bound, and exact row reduction over \(\mathbb F_2\) gives the matching lower bound. Connectivity of the one-skeleton gives first-boundary rank \(189\), hence rational Betti numbers \((1,12,36)\).

The verifier then enumerates all \(120\) graph automorphisms, identifies the central involution and the rotational order classes, computes signed traces on all cellular chain groups, computes exact \(H_2\)-traces using the integral cycle basis, derives \(H_1\)-traces from the Lefschetz identity, and checks the decomposition into the rational \(A_5\)-characters of dimensions \(4,5,6\).

The computation verifies only the stated finite dodecahedral case. It does not verify an integral module decomposition, torsion statements, or analogous formulas for other graphs.
