# Independent mathematical audit

## correctness

PASS

For every finite metric star with m>=3 positive lengths ell_i, effective positive conductances produce barycentric weights w_i. Exact full-star Lipschitz norm is max_i sum_{j!=i} w_j(ell_i+ell_j)/ell_i, saturated by one-Lipschitz leaf data f_i=ell_i, f_j=-ell_j. Reparameterize a_i=ell_i w_i/L, sum a_i=1, L=sum ell_i w_i. The excess ratio is max_i(1-2a_i)/ell_i divided by sum a_i/ell_i. Water-fill lower bounds b_i(z)=(1-z ell_i)_+/2, feasible iff z>=z* solving sum(1-z ell_i)_+=2. Remaining mass optimally resides at shortest arm. z/D(z) fractional-affine on each active interval, so finite candidates z*,1/ell_i prove global infimum over positive conductances (possibly boundary-only). For (r,1^k) obtain 1+min{r,2(k-1)r/(k+2r+kr^2)}, transition r=(k-2)/k for k>=3, equilateral 2-2/m. Independently compared the formula to primal exact rational linear-program vertices and scipy direct LP for 30 heterogeneous 3..5 arm samples. Bounds hold for arbitrary m by analytic proof, not finite LP.

## originality

PASS

General Lipschitz linear extension existence and equal-arm factors are known; the unequal-length positive harmonic conductance infimum, finite water-filling algorithm, and nonattainment phase boundary were not stated in inspected literature. This is a specific optimization, not novelty of the general linear-programming method.

## value

PASS

The minimax conductance choice is an intrinsic graph/network design objective: optimize worst-case Lipschitz amplification of harmonic interpolation. It gives an explicit sharp algorithm and an attainability/degeneration transition for nonuniform metric stars, a meaningful structural phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
