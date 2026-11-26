---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Normalized independent squared complex Gaussian components give the uniform simplex, not the real-Haar or mixed-state sampling law. For full computational-basis dephasing the spectrum consists of those populations. Global passive rearrangement pairs descending populations with ascending Hamming energies even when energies repeat. The exact ordered means are (h_d−h_{i−1})/d: independent exponential order-statistic gaps have means 1/j in descending gap order, and the population vector is independent of its unnormalized exponential sum, whose mean is d. This also checks the frozen ordered-simplex Jacobian argument. The average initial energy is nω/2. For the limit the standardized Bin(n,1/2) quantile converges in L² to the Gaussian quantile by weak and second-moment convergence, and the harmonic weight converges in L² to −log u by the bound 1−log u. Their paired integral therefore converges; Gaussian integration by parts has vanishing boundary terms (the left logarithm is O(z²) and the Gaussian density decays). This gives the stated positive finite c_*. Dephasing contracts trace distance, the pure-projector bound contributes a factor ≤2, and subtraction of the passive minimum contributes a factor ≤2, so the work is 4nω-Lipschitz in the real sphere coordinates. The mean-centered spherical estimate in arXiv:2412.19801, Eq. (14)–(15), gives exponent (2d)(εω√n)²/[25π(4nω)²]=dε²/(200πn), including n=1. E_n is positive almost surely and concentrates at nω/2 after scaling, for example by the direct Dirichlet variance nω²/[4(d+1)]. The work/energy statement follows by Slutsky. `python3 /workspace/branches/independent_examples.py 5` independently checked the grouped finite harmonic formula for n=1,…,4 and reproduced c_*=0.4515986427843126768… by mpmath quadrature; the latter checks digits numerically and is not the limit proof.

## originality

PASS

Credit the passive-ordering formula, classical broken-stick means and general ergotropy concentration as existing tools; the finite mean by itself is their direct specialization. The supported distinct finding is the sharp post-dephasing work and work-fraction asymptotic for this specific Haar-pure spin ensemble, including the Gaussian integral coefficient. The strongest inspected primary studies and the same-date indexed spin-battery result use materially different spectra, dephasing or observables, and do not yield this coefficient or scaling as a special case. This is not a priority guarantee.

## value

PASS

The exact Haar-pure benchmark distinguishes stored energy of order n from work of order √n after complete dephasing, giving an explicit positive coefficient and a typical efficiency tending to zero at a sharp rate. This answers a natural model question that generic concentration or an exact single-size mean cannot answer, and does not purport to predict a driven battery, a weaker pinching channel, or a local extraction protocol.

The dated certificate retains the supplied scientific assessment, sources and limitations.
