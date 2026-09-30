# Independent Audit — sharpness-ultraspherical-lower-envelope--e1fc7460efef

**Audit date:** 2026-09-29 (UTC)  
**Assigned/current source tree:** `c78137e0dd9fd7d2767b8981ed54ecb671844257`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree is unchanged from the dispatcher-audited source tree; no source-path file changed between the source-check commit and the current audited commit.

## Correctness — PASS

PASS. Independent symbolic recomputation of the normalized Jacobi polynomials gives U_1(x)=x, U_2(x)=((2α+3)x^2-1)/(2(α+1)), and at ξ_1=-1/(2α+3) the exact defect U_5(ξ_1)-U_1(ξ_1)=4α(α+2)(2α+1)(2α+7)/(2α+3)^5. Its sign is negative precisely on -1/2<α<0. At α=-1/2 the Chebyshev specialization T_n gives the stated counterexample, and for -1<α<-1/2 the exact value U_{2m}(0)=(-1)^m Γ(α+1)Γ(m+1/2)/(sqrt(π)Γ(m+α+1)) has magnitude asymptotic to a positive constant times m^{-α-1/2}, hence is unbounded with alternating sign. The three regimes cover the full Jacobi domain -1<α<0 without a gap.

## Originality — PASS

PASS, NARROWLY. The September 2026 Castillo--Sadigova source proves the lower-envelope theorem only for α>=0. Targeted searches for the negative-parameter sharpness, the degree-5 defect, and the three-regime classification did not locate a prior statement. Classical Jacobi/Chebyshev formulas used in the proof are not treated as original; the original content is the sharp failure classification immediately beyond the new theorem's parameter range.

## Scientific value — PASS

PASS. The result identifies α=0 as the exact endpoint of a newly proved ultraspherical lower-envelope theorem over the full admissible symmetric-Jacobi range, with explicit low-degree and asymptotic witnesses for every failure regime. This is a compact but mathematically informative sharpness theorem rather than a numerical observation.

## Independent checks

- independently derived normalized U_1, U_2, and U_5 with symbolic algebra and factored the ξ_1 defect exactly
- checked the signs of every factor on -1/2<α<0
- checked the α=-1/2 Chebyshev specialization and first-cell location
- verified the even-degree origin formula against normalized Jacobi polynomials for several m and rederived its Gamma-ratio asymptotic
- compared the claim against the September 2026 Castillo--Sadigova theorem and targeted negative-parameter searches
- confirmed no assigned record path changed between the dispatcher source-check commit and the audited current main commit

## Limitations

- The originality claim is deliberately narrow: standard Jacobi identities, Chebyshev specialization, and Gamma asymptotics are classical.
- The motivating source theorem is very recent, so simultaneous unindexed follow-up work is a residual priority risk.

## Evidence and references

- https://arxiv.org/abs/2609.15473
- https://dlmf.nist.gov/18
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/17/sharpness-ultraspherical-lower-envelope--e1fc7460efef

This audit changes only the independent-audit channel. Lean verification and expert attestation remain unchanged.
