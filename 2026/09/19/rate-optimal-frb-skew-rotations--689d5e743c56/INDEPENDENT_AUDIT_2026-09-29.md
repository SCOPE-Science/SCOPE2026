# Independent audit — 2026-09-30

Record: `2026/09/19/rate-optimal-frb-skew-rotations--689d5e743c56`  
Assigned and audited source tree: `0dcc5947a5defc925bfa178183773cc91de5dda8`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `1df9813864094c2635689deec7cb3511d498d34e`  
Disposition: **passed**

## Correctness

**independently_reproduced**. The characteristic polynomial and the complete rate phase diagram check independently. Its discriminant simplifies to 1-4(1+gamma)h^2. For gamma>-1, below coalescence the dominant squared modulus is (1+u)/(gamma+2-gamma u), increasing in u while u decreases with h; above coalescence it is 1/(gamma+2-2 sqrt(gamma+1) w), increasing with w and hence h. Thus the unique global minimum occurs at h=1/(2 sqrt(1+gamma)) with spectral radius 1/sqrt(gamma+2). The repeated companion eigenvalue is defective, so the k r^k transient qualification is correct. At gamma=-1 one root is exactly one; for gamma<-1 the same real-root formula decreases monotonically to 1/sqrt(-gamma). An independent dense numerical sweep of representative gamma values (-3,-2,-1,0,1,2,3,5) reproduced every optimum/limit. The source's stability threshold for 0<=gamma<3 agrees with the record's comparison. The isolated 'nu' versus 'u' symbol in the theorem statement is a non-substantive notation typo and does not alter any formula or proof.

## Originality

**qualified_source_specific_rate_refinement**. Shehu's September 2026 paper establishes the exact stability boundary for this skew family and the gamma=0 FRB rate benchmark is older work. Current searches did not locate the closed gamma-dependent spectral-radius minimum, its discriminant-coalescence characterization, or the gamma<-1 infinite-step rate regime as stated here. The contribution is therefore supported as a source-specific rate optimization of a very recent linear counterexample family, not as a general optimal-step theorem for FRB/RFB.

## Scientific value

**useful_exact_rate_phase_diagram**. The result cleanly separates largest stable step from fastest asymptotic step and exhibits the distinction even when all finite steps are stable. The matched-skew example gives a concrete large gap, and the defective optimum warns that finite-horizon behavior need not be optimized by the asymptotic spectral-radius minimizer.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/19/rate-optimal-frb-skew-rotations--689d5e743c56
- https://arxiv.org/abs/2609.18373
- https://arxiv.org/abs/2509.02005
## Limitations

- The theorem is confined to the exact two-dimensional linear skew family and fixed scalar steps.
- The gamma=0 optimum is prior work and is not a new claim.
- The exactly optimal repeated root has a polynomial transient, so finite-horizon optimality is not asserted.
- The motivating stability paper is extremely recent, leaving normal concurrency risk.
