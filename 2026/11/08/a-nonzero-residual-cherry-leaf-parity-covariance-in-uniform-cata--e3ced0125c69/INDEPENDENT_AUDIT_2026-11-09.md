# Independent mathematical audit

## correctness

PASS

For ordered full binary trees of n internal vertices, including the size-zero leaf, direct subtree-depth reversal gives F(z;u,v)=u+z(F(z;u^{-1},v)^2+(v-1)u^{-2}). Its mixed derivatives produce M=1/(2-s), B=z/s and J=-2z/(2-s)-2z^2/[s(2-s)^2], s=sqrt(1-4z). Independent Puiseux expansion gives M=1/2+s/4+s^2/8+s^3/16+... and J=-1/(32s)-9/32-11s/128+..., yielding E Delta=-1/8-9/(64n)+..., E H=n/4+3/8+..., E Delta H=-n/32+3/256+..., hence Cov=3/32+O(1/n). A second-u derivative yields Var Delta~9n/8, cherry bivariate Catalan derivative yields Var H~n/16, giving n Corr -> 1/(2sqrt2); correlation only n>=3. Singularities outside z=1/4 are subdominant. Explicit enumeration of all ordered Catalan shapes for n=3..6 reproduced 24/25,-24/49,4/7,-12/121. These finite enumerations are corroboration, not proof of the limits.

## originality

PASS

Best-of-knowledge original mixed local-cherry versus signed global leaf-parity covariance: marginal depth-residue CLTs and a full earlier cherry-versus-Sackin-depth covariance do not determine the mixed parity quantity. The precise order-one residual and inverse-n correlation were not found elsewhere, but broad historical implicit generating-function coverage remains possible.

## value

PASS

Cherries are a canonical local fringe-subtree count and leaf-depth parity is a canonical Fourier-depth statistic; proving their covariance survives at order one after cancellation of order-n terms identifies a non-obvious dependence scale, including finite sign changes. The exact natural residual constant and decorrelation rate are independently meaningful beyond a normalization identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
