# Independent mathematical audit

## correctness

PASS

Fix n>=2 and r>0 in the stated metric. In each upper-half-plane factor cosh(d(i,x+ie^s))=cosh(s)+x^2/(2e^s). With q=d_0(o,z)^2/2, the constraint ∇u=lambda ∇q forces x_1=x_2=0, the other factors equal to i, and s_1=-s_2=±b, b=r/sqrt(2). There is no interior critical point. At the maximum lambda=1/b; the horizontal constrained Hessian entries in the orthonormal frame are -e^b/sinh(b) and -e^(-b)/sinh(b) (also obtained directly from the distance identity), and the other 2n-3 are -1/b. Its absolute determinant is b^(-(2n-3))/sinh(b)^2; interchange of factors gives the minimum. Euclidean density in hyperbolic volume is prod(y_j^2)=1 there. Divergence with ∇u/2 gives boundary amplitudes ±1/sqrt(2) times (it)^(-1). Stationary phase on the smooth (2n-1)-sphere gives the exact prefactor and phase in the Finding and remainder O(t^(-n-3/2)) for fixed r. The real multiplier consequently alternates sign along large successive cosine extrema. For a selected positive zero, affine hyperbolic isometries give exact unweighted Euclidean mean zero at every upper-half-plane center. The transfer in Ma–Zhang (33)–(35) is valid for any fixed r after the zero is known. Independently, smooth cutoffs of radius j about (i exp(-j^3),...,i exp(-j^3)) can be separated by >2r on a tail, equal 1 on the half-radius balls and have metric Lipschitz norm O(1/j). Each radius-r ball interacting with one late cutoff has mean error O(r/j)+o(1): replace the cutoff by its center value and use that the inverse Cayley volume weight is uniformly asymptotic to a positive constant on these thickened supports. Thickened early supports are compact, so this covers approaches to every face, not just the distinguished boundary. Pullback by the center dilations and dominated convergence give the product of the one-factor normalized kernel moment and its conjugate: the moment reduces to 2 int_0^infty y^(it)(1+y)^(-3)dy = Gamma(1+it)Gamma(2-it), giving the stated positive squared modulus. Weakly null normalized kernels annihilate compact contributions to the limit. Thus the symbol and bound hold for each prescribed R with r=sqrt(2(n+1))R as normalized by the cited source, not uniformly in R or with one common symbol. The uploaded stationary checker was only inspected, not used for the infinite proof.

## originality

PASS

Credit Ma–Zhang for the sufficiently-small-radius theorem, the multiplier formulation and the localization/essential-norm transfer conditional on a zero. The supported distinct results are the exact large-frequency law at every fixed positive radius and the resulting removal of the small-radius restriction. The strongest checked prior does not supply that nondegeneracy calculation or zeros at arbitrary r.

## value

PASS

An exact fixed-radius averaging detector for compactness could otherwise still work on genuine polydisc balls of larger prescribed radii. The result rules out that possibility at every radius and gives an explicit nonzero essential-norm witness. The multiplier's oscillatory coefficient and infinitely many zeros are useful beyond rechecking a single small-radius example; the required sign oscillation is not a numerical or small-ball extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
