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

Equal escape makes the quantum-jump hazard exactly constant; each rank-one jump relocalizes the state and flips the parity of its departure site. The weighted coherent probabilities J_r(2ht)^2 summed over even and odd displacement give the two stated Bessel kernels and their Laplace transforms. Although for real theta the ordinary Bessel component can change sign as a function of time, the even and odd sums are nonnegative, nonzero continuous kernels. The determinant of K is -C_0 C_1 g_I g_J<0 on the real domain, so the second eigenvalue is negative and cannot produce a second real solution. Every entry decreases with z; the divergence of g_I at the lower edge and decay at infinity give the unique Perron crossing. The PF conjugation of the exponentially tilted kernels gives a nonlattice finite-state renewal process with finite means and integrable final segment, and hence a positive leading prefactor for either starting parity. For cumulant differentiation near theta=0, the Laplace resolvent has an isolated simple pole: at theta=0, the continuous kernel densities strictly reduce the entrywise modulus on the imaginary axis away from zero, and the transforms tend to zero at high frequency. Exponential moments give a strip, and analytic continuation in theta isolates the same pole uniformly in a small complex neighborhood of zero. Laplace inversion gives the exponential leading term with an analytic prefactor (subtract a decaying exponential transform to make the large-frequency remainder integrable). This justifies differentiating to obtain the limiting cumulant rates. At the origin the determinant perturbation is D² sinh²(theta)g_I g_J, D=(d_0-d_1)/2, and its contribution to curvature is -2D²/(Gamma+B); the homogeneous curvature is Gamma+4h²/Gamma. The strictly increasing variance and classical penalty ratio follow. For the LDP, the PF root is differentiable for all real tilts. Row sums of K are C_a g_I, so at the crossing Lambda+Gamma>=min(C_0,C_1); strict directional positivity makes the bound exponential as theta tends to either end. This also supports the asserted steep growth by convexity. Finite real tilts give exponential tightness and the full Gartner–Ellis conclusion with a good Legendre–Fenchel rate. Read frozen VERIFICATION.md, requirements.txt and verify.py, but did not execute the frozen script. Fresh bounded reproduction: OPENBLAS_NUM_THREADS=1 python /workspace/branches/independent_staggered.py; direct 151-site sparse density matrix, rates (1.1,0.3),(0.2,1.2), h=0.8, times 12 and 24 and both initial parities. The moment slopes agreed with (-0.1,2.8974760438) to about 6e-9 and log-MGF slopes at tilts ±0.4 agreed with the root to about 4e-9. This finite-chain floating-point check is not a proof of an infinite-time, all-tilt or infinite-chain conclusion.

## originality

PASS

The supported distinct contribution is the equal-escape, unequal-directional-bias parity law: its two-kernel all-tilt equation and the explicit bias-contrast curvature, with an LDP for that SCGF. The homogeneous square-root dispersion (and its second-order coefficient), the quantum stochastic walk model, and the abstract large-deviation machinery are not new. The strongest inspected matches did not imply the unequal-bias law.

## value

PASS

An alternating bias at equal escape is the smallest spatial inhomogeneity that separates parity memory from waiting-time variability. Its measurable suppression of diffusion is exactly quantified and weakened by coherent motion without changing the drift; the full tilt equation gives non-Gaussian long-time transport information beyond that variance. This is a motivated solvable class and benchmark, restricted to rank-one directional jumps, homogeneous coherent hopping, and localized initial data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
