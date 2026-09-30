# Independent audit — 2026-09-30 UTC

Record: `2026/09/21/first-repeat-law-identifies-atomic-mass-spectrum--a5416f2ce9bb`  
Assigned and audited source tree: `53a7a8167350509a53afb0664a6ba279f0f95391`  
Repository/branch: `SCOPE-Science/SCOPE2026` / `main`  
Current RESULT.md blob: `8628646719e97be4333c07230bcc9ac19785ef33`  
Disposition: **passed**

## Correctness

**independently_supported**. The factorization B(z)=e^{qz}∏(1+p_i z) follows exactly by conditioning on how many of the first n draws land on distinct atoms. Since Σp_i<∞, the genus-zero product converges uniformly on compact sets and its zero multiset is precisely {-1/p_i}, so the first-repeat law determines all positive atomic masses with multiplicity and normalization then gives the nonatomic mass. Expanding log B recovers every collision power Σp_i^r. For at most m atoms, C_2 through C_{2m+1} are the first 2m moments of ρ=Σp_i^2δ_{p_i}; a signed difference of two candidates has at most 2m support points, so the Vandermonde system forces equality and recovers multiplicities.

## Originality

**qualified_supported_with_explicit_discrete_prior_art**. Camarri–Pitman 2000 was inspected in full-text form through its exact first-repeat formulas for arbitrary countable discrete laws; it develops the forward repeat-time distribution and asymptotics, not the mixed-law inverse classification found here. Stein's 1990 report explicitly concerns Newton identities and the generalized birthday problem, so no novelty is assigned to finite-discrete Newton inversion; verified theorem-level full text of that report was not available in this run and it is not claimed as read. Current searches did not locate the complete invariant statement for an arbitrary law with both atoms and nonatomic dust or the stated finite-horizon mixed-law bound.

## Scientific value

**meaningful_structural_identification**. The theorem shows that the one-dimensional population law of a severe stopping-time compression still identifies the entire ranked atomic mass spectrum and total dust, and it gives a finite-horizon recovery guarantee under a bounded atom count. It also states exactly what repeat data cannot identify.

## Independent checks

- Re-derived the all-distinct probability and the exponential generating function factorization.
- Checked compact convergence and zero recovery for countably many atoms accumulating only at mass zero.
- Derived the logarithmic collision-power coefficients directly.
- Rechecked the finite-horizon Vandermonde argument with repeated equal atom masses combined in ρ.
- Inspected Camarri–Pitman 2000 through its exact first-repeat formulas; Stein 1990 was not available as verified full text and is not claimed as read.

## Literature and evidence checked

- https://statistics.stanford.edu/technical-reports/application-newtons-identities-generalized-birthday-problem-and-poisson-binomial
- https://doi.org/10.1214/EJP.v5-58
- https://doi.org/10.3390/e25020185
- https://doi.org/10.3390/e28080882
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/21/first-repeat-law-identifies-atomic-mass-spectrum--a5416f2ce9bb
## Limitations

- This is population-level identification, not a stable finite-sample estimator.
- Small or clustered atom masses can make numerical inversion severely ill-conditioned.
- Atom locations and the internal nonatomic distribution are unidentifiable.
- The 2m+1 horizon is sufficient, not claimed minimal.
- Stein 1990 remains a material finite-discrete priority risk because verified full text was unavailable.
