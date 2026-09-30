# Independent audit — 2026-09-29 UTC

Record: `2026/09/20/growing-rankin-cohen-twisted-nonvanishing--116c1bd23a07`  
Assigned source tree: `0686e2cfdd4dd389e9ba1160aaefe3c87768b401`  
Audited current source tree: `0686e2cfdd4dd389e9ba1160aaefe3c87768b401`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `fca63eb184e7c8d2c734870949a310dd3a281bf0`  
Disposition: **passed**

## Correctness

**independently_supported**. The growing-dimension perturbation argument is internally correct given Takloo-Bighash's explicit Fourier remainder estimate. The endpoint coefficient is exactly the Dirichlet convolution of a_ell(d)=chi_D(d)d^(ell-1) with id^(2e); its Dirichlet inverse is mu(d)chi_D(d)d^(ell-1), including at ramified primes where the character vanishes. The unitriangular divisor-column transform therefore converts the endpoint matrix exactly to W=(n^(2e)). Reapplying the published error bound after this transform gives the convergent divisor factor described in the record, while a Lagrange-polynomial estimate bounds ||W^-1|| by exp(O(r log r)). With r=c sqrt(ell), every additional prefactor is exp(o(ell)) and Stirling reduces the exponential rate to log(2*pi*e*|D|*c^2); the strict stated bound on c makes it negative. Thus the Neumann criterion gives eventual invertibility. The Petersson formula then places all these independent brackets in the twisted-nonvanishing subspace, giving the count. Exact small integer tests independently reproduce the Möbius/Vandermonde transform, including a quadratic character with zeros.

## Originality

**qualified_supported_growing_r_extension**. Takloo-Bighash's September 2026 theorem explicitly fixes r while the weight grows. Kayath--Lane--Neifeld--Ni--Xue construct the relevant spanning sets and discuss the broader nonvanishing problem, but do not state this square-root growing independence. The new argument's exact Möbius preconditioning is a genuine change from a fixed-index determinant limit and is what makes the published remainder estimate usable at growing r. For D=1, Luo's 2015 theorem already gives a stronger linear-order nonvanishing count, so the counting corollary is not new there; the D=1 new content is only independence of this explicit square-root Rankin--Cohen family. Searches found no matching growing-r theorem, but the motivating preprint is days old, so concurrent work remains a material risk.

## Scientific value

**meaningful_quantitative_extension**. The result upgrades an arbitrary fixed number of independent brackets to order sqrt(weight), with an explicit constant, and produces a concrete quantitative fixed-twist nonvanishing lower bound for nontrivial D. The Möbius/Vandermonde preconditioning is reusable, while the theorem remains honestly below the conjectural linear scale.

## Independent checks

- Verified exact Möbius inversion numerically for several indices with the quadratic character modulo 5, including multiples of 5.
- Re-derived the Vandermonde inverse growth estimate and the Stirling exponent log(2*pi*e*|D|*c^2).
- Checked that the source abstract explicitly assumes fixed r and compared against the 2025 open spanning-set paper.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/20/growing-rankin-cohen-twisted-nonvanishing--116c1bd23a07
- https://arxiv.org/abs/2609.19649
- https://arxiv.org/abs/2407.00532
- https://doi.org/10.4153/S0008414X25101697
- https://arxiv.org/abs/2507.17041
- https://doi.org/10.1016/j.aim.2015.08.009

## Limitations

- D is fixed and odd; no uniformity in growing |D| is proved.
- The theorem reaches only the square-root scale, not the conjectural linear-size independence regime.
- The constant (2*pi*e*|D|)^(-1/2) is not claimed optimal.
- For D=1 the nonvanishing count is weaker than Luo's prior linear-order result.
- Very recent source chronology leaves substantial concurrent-work risk.
