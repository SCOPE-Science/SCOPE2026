# Independent audit — 2026-09-29

Record: `2026/09/19/first-order-weyl-isotropy-criterion--1615b82a083d`  
Assigned and audited source tree: `91325e7ddb622b62a780330eec2e73a2c83f3dfe`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**independently_supported**. The trichotomy is correct. For d=deg A>=2, the equation rho(W)-W in k forces deg(A(P)Q)=dm+n=d+1 in the standard filtration, hence deg P=deg Q=1. Leading-form unique factorization then forces a diagonal affine automorphism; normalization of the p^(d-1) coefficient eliminates the translation, and the lower-degree term eliminates the q-translation. Coefficient comparison gives precisely the cyclic group mu_g. On k[p], ad_{a(p)q+b(p)} acts as -a(p)d/dp, so repeated images of p have degrees 1+n(d-1) when d>=2, proving non-local-finiteness. The constant and linear branches reduce to the standard q/polynomial locally nilpotent forms and the pq locally finite torus form.

## Originality

**qualified_supported**. Baltazar--Lopes--Morales currently state the isotropy criterion for nonzero locally finite derivations of A1 and explicitly leave arbitrary derivations open. Their public abstract, including the September 18 update, does not cover the non-locally-finite first-order family. Targeted searches did not locate the exact stabilizer formula for a(p)q+b(p). The automorphism-group and leading-form inputs are classical, so novelty is accepted only for this first-order partial resolution and explicit cyclic stabilizer.

## Scientific value

**meaningful_partial_resolution**. The result extends the new isotropy criterion beyond local finiteness on a natural infinite stratum and gives an exact stabilizer, including a sharp finite-vs-unbounded dichotomy. It leaves genuinely higher q-degree elements open.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/19/first-order-weyl-isotropy-criterion--1615b82a083d
- https://arxiv.org/abs/2609.19470
- https://doi.org/10.24033/bsmf.1667
- https://doi.org/10.24033/bsmf.2010

## Limitations

- Restricted to elements of q-degree at most one (and, by Fourier symmetry, the analogous p-degree-one stratum).
- Classical Weyl-automorphism structure is prior art; the new content is the stabilizer calculation and criterion on this stratum.
- Equivalent implicit coverage in older Weyl-algebra literature cannot be excluded absolutely.
