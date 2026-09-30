# Independent audit — 2026-09-28

Record: `2026/09/10/045`  
Audited tree: `1c5a143ba3d2af688ca0dc41ee1853b593295baa`  
Disposition: **passed**

## Correctness
The central calculation survives independent reconstruction. At `z=0`, `z^2 r(z)=z^3+z` is analytic, so the singularity is regular with exponents `0,1`. The Frobenius recursion `(n+rho)(n+rho-1)a_n=a_(n-1)+a_(n-3)` gives `a1=1/2`, `a2=1/12`, `a3=13/144` for `rho=1`, while the `rho=0`, `n=1` equation is the obstruction `0*a1=a0=1`; a logarithmic second solution is therefore required. There are no Stokes matrices at zero.

At infinity the transformed coefficient has pole order five, hence an irregular singularity of Airy type. The reducible Kovacic case is excluded because a rational Riccati solution has an integer leading exponent at infinity, but no integer exponent can make `u'+u^2` have leading term `z`. The irreducible imprimitive case is excluded by the symmetric-square equation: for `w~az^e`, the leading `z^e` coefficient is `-2a(2e+1)`, never zero for integer `e`. A finite Picard–Vessiot group is incompatible with an irregular singularity. Since the Wronskian is constant, `G` is contained in `SL2`; the remaining case is `G=SL2(C)`.

## Originality
The method is standard, but I did not locate a prior table or paper carrying out this exact `r=z+1/z` cell or recording the slope-at-zero correction. That supports originality of the specific computation only.

## Scientific value
The exact group determination is reusable and the regular-singular correction removes an impossible Stokes-at-zero requirement from subsequent work.

## Limitations
Exact Stokes multiplier values at infinity remain uncomputed.

## Sources
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/10/045
- https://arxiv.org/abs/0712.4124
- https://arxiv.org/abs/2009.07607
