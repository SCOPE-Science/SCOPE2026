# Independent audit — 2026-09-29

**Record:** `2026/09/18/sharp-ainfty-endpoint-power-sparse-operators--ef01896cc9bb`  
**Disposition:** **PASSED**

## Correctness

**PASS** — The finite dyadic construction is correct. For omega_N=1+2^N 1_{I_N}, dyadic nesting reduces the Fujii--Wilson characteristic to ancestors I_j. Direct shell integration gives integral_{I_j} M_D(1_{I_j} omega_N)=1+2^{-j}+(N-j)/2 and omega_N(I_j)=1+2^{-j}, hence the stated exact maximum and A_infinity growth Theta(N). Setting v_N=M_D omega_N makes the mixed A1 characteristic exactly one. With f=1, the sparse sum equals (N+1)^(1/r) on I_N, whose omega-mass is 1+2^{-N}, while ||f||_{L1(v)}=2+N/2. The resulting lower bound is therefore Theta_r(N^(1/r-1)), forcing gamma>=1/r-1.

## Originality

**PASS** — Goncalves--Lorist's current September 2026 preprint gives the upper mixed endpoint estimates and says some weak-type bounds are new even in the dyadic setting, while its public abstract highlights a different sharp weak-(2,2) Rubio de Francia consequence. Searches using the source identifier, r<1, p=1, A_infinity, sharpness, and 1/r-1 did not locate a prior lower-bound example isolating this exponent with [omega,v]_{A1}=1. Older Hytönen--Li and Nieraeth--Stockdale works cover neighboring weighted and endpoint regimes. On this evidence the specific sharpness example passes, qualified by the recency of the source theorem.

## Scientific value

**PASS** — The example decides whether the new A_infinity power in the endpoint upper bound is intrinsic or an artifact of proof, and it cleanly isolates that factor by freezing the mixed A1 characteristic at one. Because the example is finite and explicit, it is easy to reuse as a sharpness test for related sparse endpoint estimates.

## Independent checks

- Recomputed every dyadic shell contribution to the Fujii--Wilson A_infinity characteristic and checked the cases disjoint from or contained in I_N separately.
- Verified v=M_D omega gives [omega,v]_{A1}=1 pointwise and integral_0^1 v=2+N/2.
- Evaluated the weak-level set at t=N^(1/r), confirmed I_N lies strictly inside it, and divided by the exact L1(v) input norm.

## Findings

- The claimed exponent lower bound follows with no limiting or numerical step.
- The construction genuinely separates A_infinity growth from the mixed A1 factor.
- No prior source matching this exact p=1, 0<r<1 two-weight sharpness example was located in the current search.

## Literature evidence

- https://arxiv.org/abs/2609.20531 — Goncalves and Lorist (2026), current upper-bound source for mixed A_p-A_infinity sparse estimates.
- https://arxiv.org/abs/2409.08921 — Nieraeth and Stockdale, endpoint weak-type bounds beyond Calderon--Zygmund theory; neighboring endpoint problem cited by the source.
- https://arxiv.org/abs/1509.00273 — Hytonen and Li, earlier weak/strong A_p-A_infinity estimates for square functions and related operators.

## Limitations

- The conclusion is sharpness for the positive sparse model, not a lower bound for every concrete operator admitting sparse domination.
- It does not determine the best constant as a function of r or sparseness.
- The logarithmic r=1 endpoint is a separate phenomenon and is not addressed.

## Publication consequence

The audited claim may remain at its source path. This audit does not modify the research statement; it adds only the independent-audit evidence and updates the independent-audit verification channel.
