# Independent mathematical audit

## correctness

PASS

For h>0 the resolvent is a positive weighted series of walk matrices on a connected torus, so T=2R-I has positive off-diagonals. Translation transitivity and the Fourier spectrum make the diagonal of R the stated average, strictly decreasing from 1 to 1/(mn); h=0 gives the identity. At fixed h>0 and horizontal frequency, the vertical average of 1/(a-h cos theta), a>h, retains precisely the Fourier modes divisible by n. Their geometric sum is proportional to (1+q^n)/(1-q^n), 0<q<1, which strictly decreases at every increment, not only over divisibility chains. The comparison transfers to the unique crossings. Substituting the spectrum at 3 by 3 gives 7h^2-h-2=0 and the stated positive root, less than 1. In the infinite walk, the even return coefficients are binom(2k,k)^2/16^k and the odd coefficients vanish; one way to see this is that the transformed coordinates X+Y and X-Y perform independent one-dimensional walks. The generating function is the elliptic integral with its modulus, not its parameter. Nonzero torus images require at least min(m,n) steps, and some image occurs with positive probability, so the resolvent difference is strictly positive and at most z^min(m,n). The finite diagonal derivative has magnitude at least 2/25 for h<=H_(m,n)<1 using mean eigenvalue 4 and maximum 8; applying the mean-value theorem at the infinite crossing gives the constant 25/2 at z_infty. Exact rational recomputation of the return series through k=22, with geometric tail at most z^46/((1+2h)(1-z^2)), confirms the strict endpoint signs at 588197/10^6 and 588198/10^6. This uses the dimensionless step for the degree-four combinatorial Laplacian, and concerns the end-step, not stages or other boundaries. The supplied finite checker was inspected, not run.

## originality

PASS

The general crossing criterion and the square-lattice Green function are known. The distinct claim supported here is the strict ordering for independent rectangular periods at every unit increase and the uniform rectangular finite-size enclosure for the corresponding step threshold. No inspected earlier statement establishes that claim.

## value

PASS

An exact coordinatewise mesh-period ordering is useful because a coarser nested-grid comparison would not order general rectangles. The result ties that ordering to a practical one-step nonnegativity cutoff and gives an explicit guarantee for using the limiting threshold at finite size. Its value does not depend on novelty of the general resolvent law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
