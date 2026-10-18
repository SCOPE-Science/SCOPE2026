# Independent mathematical audit

## correctness

PASS

Diagonal similarity C=D^-1/2 A D^-1/2 has unit diagonal, SPD and Stieltjes signs. The iteration polynomial q3(C)=3omega I-3omega^2 C+omega^3 C^2 has off-diagonal omega^2[(3-2omega)g_ij+omega sum_(l!=i,j)g_il g_lj], which is >=0 for omega<=3/2; spectral positivity q3(lambda)=omega(1+r+r^2)>0 when r=1-omega lambda in (-1,1) handles diagonal. q2 diagonal omega(2-omega)>0 and offdiagonal >=0. For omega>3/2, 2x2 C_a with a<2/omega-1 and b=e2 yields negative offdiagonal. Independently iterated exact rational omega=8/5,a=1/5 to x3=(-64/625,4312/3125) with iteration eigenvalues -23/25,-7/25; scalar case is positive for all k.

## originality

PASS

Imakura et al Theorems 3.1–3.2 optimize weighted Jacobi spectral radius; their full four-page source has the identical recurrence but no finite third-iterate sign theorem. M-matrix nonnegative splitting arguments guarantee monotonicity only in underrelaxed regime and do not deliver the overrelaxed 3/2 boundary. No exact equivalent appeared in the targeted Resultary comparison.

## value

PASS

Separates asymptotic convergence of a classical positivity-relevant iterative solver from finite-step coordinatewise sign safety, with a sharp universal weight and minimal counterexample. This boundary matters when nonnegative transient states are required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
