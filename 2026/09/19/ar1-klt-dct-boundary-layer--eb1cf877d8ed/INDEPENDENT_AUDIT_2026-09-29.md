# Independent Audit — 2026/09/19/ar1-klt-dct-boundary-layer--eb1cf877d8ed

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `83dbdaba6aec58fb098939525e881273a4206701`
- Disposition: **PASSED**

## Correctness

**PASS** — The exact secular equation for the symmetric Perron mode rearranges to tan(x_N/2)tan(x_N/(2N))=(1-rho_N)/(1+rho_N). With x_N=N omega_N, finite kappa=N(1-rho) therefore gives x tan(x/2)=kappa, while kappa->infinity forces x->pi. The exact finite cosine-sum normalization yields the submitted overlap A(kappa) and the limit 2sqrt(2)/pi. This proves the iff threshold N(1-rho)->0 for convergence of the leading KLT vector to DCT-II DC. Independent diagonalizations at N=256 reproduce the submitted overlaps for kappa=0.1,1,5,20 to the expected finite-N error. The fixed-mode phase equation yields the stated Robin conditions after continuum interpolation, and the eigenvalue scaling agrees with the exponential-kernel eigenproblem. The DCT DC Rayleigh quotient is a direct Riemann-sum integral, and its efficiency can tend to one even when the vector angle stays nonzero. The Reznik-factorization consequence is correctly stated only as a necessary condition for full correction-matrix convergence.

## Originality

**PASS** — Jain's 1979 work places DCT and AR(1) KLT in a sinusoidal family and discusses asymptotic equivalence and finite-length differences. Clarke gives the fixed-size rho->1 DCT endpoint. Unser proves performance asymptotic equivalence for stationary processes, and Sherman gives exact AR(1) eigenstructure. Reznik's 2026 factorization likewise states correction factors tend to identity for fixed N as rho->1. These actual prior statements do not give the joint local-to-unity scaling N(1-rho), the limiting principal angle, the iff top-mode threshold, or the Robin crossover. Targeted searches for those formulas and the local-to-unity boundary layer found no covering theorem. The audited contribution is thus a new joint-limit classification built from classical exact eigenstructure, not a claim that the AR(1) secular equations themselves are new.

## Scientific value

**PASS** — The theorem resolves an important nonuniformity hidden by the standard fixed-N statement KLT->DCT as rho->1, identifies the exact 1/N boundary scale, and quantifies the persistent basis angle. The Robin continuum limit organizes all fixed modes, while the Rayleigh-efficiency formula explains why coding performance may remain DCT-like despite basis nonconvergence. This is a useful bridge between exact transform theory and growing-block asymptotics.

## Sources

- Exact fast factorizations of the AR(1) Karhunen-Loeve transform (Yuriy A. Reznik): https://arxiv.org/abs/2609.20221 — Primary 2026 motivation; states fixed-N rho->1 convergence of the correction factors to the DCT-II factorization.
- A sinusoidal family of unitary transforms (Anil K. Jain): https://doi.org/10.1109/TPAMI.1979.4766944 — Classical AR(1) KLT/DCT sinusoidal-family and asymptotic-equivalence result; does not state the audited joint local-to-unity boundary law.
- On the Approximation of the Discrete Karhunen-Loève Transform for Stationary Processes (Michael Unser): https://doi.org/10.1016/0165-1684(84)90002-1 — Classical performance-asymptotic-equivalence result for fast transforms versus the KLT.
- On the Eigenstructure of the AR(1) Covariance (Peter J. Sherman): https://doi.org/10.1109/SSP53291.2023.10208005 — Recent exact finite-N AR(1) eigenstructure background.

## Limitations

- The sharp iff theorem is for the leading eigenvector versus the DCT-II DC vector, not the whole KLT basis in operator norm.
- For Reznik's full correction factors the result proves a necessary, not sufficient, growing-size scale.
- The Robin statement is fixed-mode and does not control spectral indices growing with N.
- The result does not claim new finite-N AR(1) eigenformulas; novelty is in the joint scaling and its consequences.

## Independent checks

```json
{
  "proof_reconstructed": true,
  "N256_overlap_checks": {
    "kappa_0_1": [
      0.999972867535072,
      0.9999728759295695
    ],
    "kappa_1": [
      0.9978005199464295,
      0.9978079296337878
    ],
    "kappa_5": [
      0.9758984142075844,
      0.9761542871718069
    ],
    "kappa_20": [
      0.9340147760930002,
      0.935044953424824
    ],
    "limit_infinite_kappa": 0.9003163161571062,
    "all_ok": true
  },
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Open-access/preprint sources were checked before considering institutional retrieval.
