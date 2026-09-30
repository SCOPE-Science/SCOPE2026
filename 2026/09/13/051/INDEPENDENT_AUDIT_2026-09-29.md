# Independent audit — 2026-09-29

Record: `2026/09/13/051`  
Audited source tree: `04f3298d6bf156a54ce9e3384b6073ca86a8e80d`  
Disposition: **repaired**

## Correctness

For the stated two-chamber sum functional F_s=P_s(E1)+P_s(E2), the decisive 120-degree computation is correct. At p=(1,0) on a face of the 120-degree sector, subtracting the tangent half-plane gives a strictly positive, absolutely convergent difference integral. The cylinder reduction multiplies it by B(s)=sqrt(pi) Gamma(1+s/2)/Gamma((3+s)/2), and the inscribed-disk estimate gives a uniform 3D lower bound 0.1715... on s in [3/4,1), so a homogeneous stationary cone, whose face curvature must scale to zero, cannot have this 120-degree chamber. Two ancillary numerical statements were wrong: the beta>pi branch in the archived script used the wrong difference wedge and produced -Infinity, and its off-center tail formula broke the exact d^{-s} scaling. The repaired script uses the finite wedge pi<arg<beta and the correct r=1/u tail kernel; it reproduces finite negative curvatures for beta>pi and scaling errors at machine precision.

## Originality

Nonlocal cluster theory already studies sums of fractional perimeters of all phases and, in two dimensions for s close to 1, proves a 120-degree singular cone for that full cluster functional. The present target uses the different degenerate two-chamber sum P_s(E1)+P_s(E2), which omits the exterior phase and changes interface weights. The repaired record therefore states its conclusion explicitly for that functional. Its exact wedge curvature calculation is useful, but it should not be read as contradicting the standard full-cluster theorem.

## Scientific value

The uniform positive curvature gap sharply diagnoses why the target's two-chamber sum functional does not inherit the classical/full-cluster 120-degree law at fixed s. This is useful for preventing a functional mismatch in subsequent regularity arguments.

## Limitations

- The true stationary angle for the two-chamber sum functional is not computed.
- The conclusion is specific to F_s=P_s(E1)+P_s(E2); it is not a statement about the standard full three-phase sum of fractional perimeters.
- The numerical angle sweep is supporting evidence; the positive 120-degree gap is proved analytically.
- The repaired script corrects two ancillary numerical branches but leaves the central analytic bound unchanged.

## Sources checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/13/051
- https://arxiv.org/abs/1910.03429
- https://arxiv.org/abs/2301.10705
