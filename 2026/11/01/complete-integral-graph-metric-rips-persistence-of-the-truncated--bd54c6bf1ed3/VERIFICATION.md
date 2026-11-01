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

# Verification and reproducibility

Run `python3 verify_truncated_cube_persistence.py` with Python 3.10 or later. It uses only the standard library and makes no network requests. The run output in `verification_output.txt` ends with `TRUNCATED_CUBE_INTEGRAL_PERSISTENCE_VERIFIED`.

The verifier enumerates every Rips face through scale four, checks the simplicial free-face property before elementary collapses, and performs exact signed integral Gaussian cancellations only at unit coefficients \(\pm1\). It verifies all surviving boundary maps square to zero, and all final maps vanish. This gives rigorous integral chain equivalences; reduction counts are \(31,103,542,9719\) total pairs at scales \(1,2,3,4\) respectively. At scale four the final chain groups contain one generator in degree zero, one in degree three, and two in degree five, with zero boundary. No Smith-normal-form approximation or modular rank inference is needed for the integral result.

For the inclusion homomorphisms, the verifier reconstructs chain-homotopy inverse lifts of critical generators, confirms the lifts are integral cycles in the original face complex, embeds those cycles in the next scale, and applies the target's recorded chain projections. It computes the unimodular degree-one matrix and the zero scale-three-to-four third-homology matrix. An independent binary persistent-column algorithm reproduces all intervals through scale four, providing a separate check of the combinatorial filtration.

The scale-five statement uses a direct graph-distance argument: the twelve antipodal pairs are the **only** nonedges of the fifth power, so its clique complex is the join of twelve copies of \(S^0\). At scale six the clique complex is a full simplex.

The computation proves integral homology, inclusion maps and barcode decomposition; it does not supply or require the higher-dimensional homotopy attaching maps of the scale-four complex. The ordinary full scale-three homotopy type and the final antipodal sphere mechanism were previously known. No independent audit has been performed.
