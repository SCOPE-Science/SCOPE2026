# Independent mathematical audit

## correctness

PASS

The published simplex projection formula reduces brightness exactly to the ℓ1 norm of a Haar direction in H0. Represent U as centered iid normal vector Y/||Y||; each coordinate has known sphere-coordinate beta moment and pair Y_i,Y_j correlation −1/(m−1). The exact Gaussian absolute-product identity E|Z1Z2|=(2/π)(sqrt(1−r²)+r arcsin r), together with independence of spherical radius, yields E|UiUj|=(2/(πm))(sqrt(1−r²)+r arcsin r). Summation gives both finite moments; gamma Stirling and Taylor yield the displayed −1/(4πm) variance correction. Centering an iid Gaussian vector changes its ℓ1 norm by O_P(1) and squared radius by O_P(1), hence normalized ℓ1 by o_P(1); the established spherical cube-width CLT or the multivariate delta method gives Gaussian variance 1−3/π. Independently recomputed formula and asymptotic variance corrections at m=3,4,8,100,1000; m×[1−3/π−Var] tends toward 1/(4π). Checked the actual verification script. All-size proof is analytic, not based on simulations.

## originality

PASS

Pandis gives the exact all-direction simplex projection identity and extremizers; that is the stated input rather than a newly proved formula. Kabluchko–Litvak–Zaporozhets give the cube ℓ1 CLT used for the limiting Gaussian; this limiting law is not independently new. The remaining exact finite-dimensional zero-sum sphere brightness moments and the first finite-size variance correction are not stated in examined relevant primary material. A hidden older exact zero-sum spherical ℓ1 moment table is a plausible priority risk.

## value

PASS

Haar brightness dispersion is a natural intrinsic probabilistic invariant of regular-simplex projection geometry, not an arbitrary restriction; the exact first and second moments quantify concentration/variability at each dimension and provide a sharp finite-size correction to the nonzero asymptotic variance. It distinguishes dependent zero-sum coordinates from the familiar unrestricted spherical cube-width limit. This is a motivated, reusable exact invariant even without higher-moment theorems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
