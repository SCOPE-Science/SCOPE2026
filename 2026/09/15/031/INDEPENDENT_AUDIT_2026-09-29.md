# Independent audit — 2026-09-29

Record: `2026/09/15/031`  
Audited source tree: `25370a0f2e2e60fdb7b1836b58175a04583bd979`  
Disposition: **passed**

## Correctness

The generating-function derivation is correct. Marking multiplicities gives prod_{n=1}^m (1-(1-t)u q^n)/(1-u q^n); expanding elementary and complete symmetric functions yields the shifted Gaussian-product basis, and applying the linear functional L_z(t^v)=binom(v+z-1,v) gives L_z((t-1)^i)=binom(z-1,i). An independent exact enumeration for (l,m)=(3,4) reproduced the formula at z=3, z=3/2 and z=0, including the archived z=3 coefficient vector. The stated centres (lm+i)/2 follow from the minimum and maximum degrees of each summand.

## Originality

The ingredients—finite-box partition products, Gaussian binomials and corner/distinct-part statistics—are classical. Focused searches found extensive corner enumeration literature but did not identify this exact Gamma-weighted finite-box transform. That non-detection is not used as a priority claim.

## Scientific value

The identity is a useful exact reduction of the target coefficients to staggered-centre Gaussian products and explains the z=0 and z=1 specializations. Its scope is appropriately limited: it does not solve the requested all-z unimodality problem.

## Limitations

- The full unimodality question for every l,m and real z>=1 remains open.
- The originality assessment is conservative because the identity is assembled from classical finite-box generating-function ingredients.
- The record metadata/reproducibility section names output/artifacts/verify.json, whereas the archived file is artifacts/verify.json; this packaging mismatch does not affect the proof.
- No priority claim is inferred from search non-detection.

## Sources checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/15/031
- https://arxiv.org/abs/2206.05062
- https://arxiv.org/abs/1805.08375
- https://arxiv.org/abs/1808.01596
- https://doi.org/10.1137/17M1133798
