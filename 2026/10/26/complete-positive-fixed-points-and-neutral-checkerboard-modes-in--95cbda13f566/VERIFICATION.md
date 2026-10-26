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

The accompanying `check.py` requires only Python 3 and its standard library. From the directory containing the embedded files, run `python3 check.py`. The observed output was exactly `EXACT_CHECKS_PASSED 982`.

The checker uses exact rational arithmetic to implement the reflected-neighbor update with \(p=4\) or \(p=6\), and tests positive parity-class states on grids ranging from \(3\times3\) to \(8\times7\) nodes for multiple positive generalized timestep ratios. It also tests exact edge-energy counts for \(N=2,\ldots,12\), randomly sampled positive arrays against the parity-class fixed-point criterion, and the quadratic update-defect scaling near stationary parity states for \(p=4\). One exact test asserts that the checkerboard edge energy at \(N=p=4\), \(a=1\), \(b=2\), is \(640\).

The independent analytical verification is the following chain: fixed-point equation \(\Longleftrightarrow\) reflecting harmonicity of \(w=u|G_hu|^{p-2}\); finite maximum principle \(\Longrightarrow\) \(w\) constant; mirrored corner gradient \(0\) \(\Longrightarrow\) \(w\equiv0\); strictly positive \(u\) \(\Longrightarrow\) every centered gradient vanishes; centered-gradient recurrences \(\Longleftrightarrow\) one arbitrary value per coordinate parity class. Differentiability of \(|z|^{p-2}\) with zero derivative at \(0\) for \(p>3\) yields \(DT=I\). The high-edge-energy formula is obtained by counting exactly \(2N(N+1)\) unequal adjacent pairs.

Finite experiments are not claimed to prove any universal statement. The proof assumes coordinatewise mirror closure and does not address other implementations of homogeneous Neumann boundary conditions, nonzero reaction, states containing zeros, singular exponents, or nonlinear stability of the neutral states.
