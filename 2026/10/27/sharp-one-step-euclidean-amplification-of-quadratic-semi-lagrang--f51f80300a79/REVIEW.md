# Independent mathematical audit

## correctness

PASS

The two-node block symbol follows directly from evaluating the three Lagrange basis functions at r and 1+r. Its squared singular values have the stated trace and squared determinant, both affine in z=(1-Re q)/2. For u>0, X(u) is at least one and lies to the right of the vertex F(z)/2; the characteristic polynomial evaluated at X(u) is strictly positive for z>0 since X(u)<(2+u)/(2(1-u)). This strictly excludes all other Fourier blocks for noninteger displacement. The derivative of X is positive, and the half-step zero block takes (1,3) to (5/2,5/2); an exact independent N=2 construction reproduced the 5/4 squared ratio and the block maximum. Translations by two nodes and reflection reduce any real shift to r in [0,1] without changing the norm or u; integer shifts are permutations. The result is in the unweighted coefficient norm, and the finite reproduction does not replace the all-mesh proof.

## originality

PASS

The strongest inspected same-operator source provides the Fourier representation and uniform power bounds, not an exact largest singular value and strict zero-frequency optimizer. The distinction survives matching the sign convention and coefficient-weight normalization. Best-of-knowledge judgment subject to the inaccessible 2007 text.

## value

PASS

The sharp mesh-independent constant answers a natural finite-step stability question about an existing scheme. A positive extremizer and the strict maximizing Fourier mode show how a 25% squared-norm increase is compatible with power stability; neither an eigenvalue bound nor a weighted-energy bound would give that diagnostic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
