# Independent mathematical audit

## correctness

PASS

In barycentric coordinates the affine basis Gram matrix is \(G=|T|((d+1)(d+2))^{-1}(I+J)\), whose inverse gives the projector kernel \(K(x,y)=\frac{d+1}{|T|}((d+2)\sum_i\lambda_i(x)\lambda_i(y)-1)\). For fixed \(x\), minimizing over \(0\le f\le M\) puts mass exactly on the negative part of the kernel. With \(a_i=\lambda_i(x)\) and uniform Dirichlet barycentric coordinates \(B\), the negative mass is \(c(a)=(d+1)E[(1-(d+2)\sum_i a_iB_i)_+]\). The positive-part function is convex, so Jensen in the convex combination of coordinates gives \(c(a)\le\sum_i a_i c(e_i)=c(e_0)\), proving the sharp vertex location. The marginal \(B_0\sim\mathrm{Beta}(1,d)\) integrates to \(C_d=(d+1)((d+1)/(d+2))^d-1\). Since the kernel integrates to one, its absolute integral is \(1+2c(a)\), giving the exact \(L^\infty\) norm. The strictly-positive perturbation and the asymptotics follow directly. Exact-rational package checks through many dimensions verify the Gram inverse and integral formula, while the convexity argument proves all dimensions.

## originality

PASS

The surrounding literature establishes \(L^p\) stability of finite-element \(L^2\) projection and studies Lebesgue constants of polynomial projectors on simplices, but targeted searches for the continuous uniform-measure degree-one simplex projector found no all-dimensional closed norm or sharp positivity-defect formula. The 2024 primary paper on simplex Lebesgue constants develops rigorous numerical evaluation for interpolation, discrete weighted least squares and hyperinterpolation; it does not state the audited continuous projector constant. Duan et al. use local or almost local linear \(L^2\) projectors as a finite-element ingredient rather than solve this sharp kernel problem. Current Resultary queries returned no stronger same-object formula.

## value

PASS

Local affine \(L^2\) projection on a simplex is a standard finite-element building block. Quantifying exactly how far it can violate positivity, locating the extremizing region, and giving the exact max norm in every dimension turns a qualitative stability issue into a sharp analytic benchmark. The linear-in-dimension growth is structurally informative, not a finite recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
