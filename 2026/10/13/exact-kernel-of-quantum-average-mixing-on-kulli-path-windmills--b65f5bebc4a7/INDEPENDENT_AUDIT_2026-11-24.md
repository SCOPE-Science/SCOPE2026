# Independent mathematical audit

## correctness

PASS

For the unweighted adjacency walk, time averaging keeps exactly the equal-eigenvalue terms. The quadratic form is the sum of squared Frobenius norms of the compressions E_lambda diag(z) E_lambda, so all compressions must vanish. The center-coupled block is a symmetric arrowhead with nonzero couplings at odd path eigenvalues, hence simple and disjoint from those poles. At an even mode lambda its reflection-symmetric path resolvent has coordinate sum (m+1)/(lambda-2), so collision would require lambda(lambda-2)=b(m+1), impossible since the left side is less than 8 and the right at least 9. Thus the even path space is unrestricted in the blade index and each odd path space has blade sum zero. Testing single blades and then blade differences forces every squared-sine moment to vanish per blade (for three or more blades each pair-sum vanishes and hence every entry vanishes). The Fourier transform of the symmetric part extended with a zero at index 0 is constant by sin^2=(1-cos(2x))/2, forcing that part to be zero. A coupled eigenvector with nonzero center enforces z_0=0, and products within each spectrally separated eigenspace are reflection-symmetric on each blade, proving the converse. Counting pairs gives the stated rank and nullity including m=2. The attached NumPy projector/rank script and recorded 40 graph cases were inspected, not run; the proof handles exact multiplicities without tolerance assumptions.

## originality

PASS

The supported distinct contribution is the evaluated infinite-family rank and full blade-by-blade kernel for m≥3 and b≥3, not the general projector criterion or the known clique-petal boundary m=2. The conjecture attribution was checked to the level of available evidence, not by independently reading its complete text.

## value

PASS

The supported infinite-family result identifies all null modes of a natural quantum-walk invariant rather than interpolating finite ranks. The blade antisymmetries and hub condition provide exact direction-level information and explain why the b≥3 spectral structure suffices; the known clique boundary is not the source of value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
