# Independent audit — 2026-09-29 UTC

Record: `2026/09/19/universal-attractor-largest-dihedral-bisection--a18a352f8148`  
Assigned and audited source tree: `42e62720a92e6909020322f9940824395adfef92`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `5af15e851c0bda9f4919dd3e252269ae51fcf518`  
Disposition: **passed**

## Correctness

**independently_supported**. Starting from the source recurrence, the limiting map F_0(t)=1/(t+sqrt(1+t^2-2ct)) has a unique fixed point rho in [3/4,4/5], satisfying 7rho^3-12rho^2+4=0. Direct symbolic differentiation gives F_t(rho,0)=-1/2 and the b^2 forcing coefficient -s^2 rho^5/[2(1-rho^2)]; normalization by b_n^2 gives the stated A=-0.0804857780 because rho^2>1/2. The product convergence b_n/rho^n, inradius asymptotic, cut/volume fraction rho^2, and limiting dihedral double-angle identity all follow from the recurrence and source coordinate formulas. Independent symbolic evaluation reproduces rho=0.783553337513463 and A=-0.080485778020468.

## Originality

**qualified_recent_refinement**. Korotov--Michaud's September 2026 paper supplies the invariant family, selected-edge recurrence and degeneration but its public statement gives only qualitative/coarse geometric behavior. The current record was first committed at 2026-09-19T02:17:50Z; the similarly named SCOPE self-similar-rate record was committed later at 14:22:22Z, so it is not prior to this record. Current searches did not locate the universal fixed ratio, second-order coefficient, exact asymptotic rate, or limiting split law in accessible external work. Priority remains qualified because the source is days old.

## Scientific value

**meaningful_exact_dynamical_refinement**. The result converts a degenerating counterexample into a quantitatively characterized projective attractor with exact exponential rate, second-order approach, retained-volume ratio and limiting dihedral profile. This materially sharpens the mechanism while remaining confined to the source invariant family.

## Evidence and literature checked

- https://arxiv.org/abs/2609.18788
- https://arxiv.org/abs/2609.08846
- https://arxiv.org/abs/2608.23139
- https://github.com/SCOPE-Science/SCOPE2026/commit/67992dc3c3a968a6b81297ace07ffd1f8fb8fa12
## Limitations

- Only the retained branch in the c=7/8 invariant family is analyzed.
- The prefactor C depends on the initial condition and is not closed-form.
- The motivating paper is very recent, so concurrency risk is material.
