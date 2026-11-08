# Independent mathematical audit

## correctness

PASS

For n>=4 the sample space is all connected labelled simple n-edge graphs on n vertices, uniformly weighted. The cycle of length ell with rooted trees attached yields N_{n,ell}=(n-1)! n^{n-ell}/(2(n-ell)!) using the *already-known* Abel–Cayley–Hurwitz rooted forest polynomial (sum_{root} x_r)(sum_{all}x_v)^{n-ell-1}. Differentiating gives total degree factorial moment 3(n-z_n), hence exact p=2/(n-1), adjacent-edge a, and disjoint-edge b. Covariance is (p-b)I+(a-b)A+(b-p^2)J; Johnson two-subset eigenvalues 2(n-2),n-4,-2 lead to 0,4A_n and 4B_n on the claimed dimensions after w_e=-2(I_e-p). For n=4, z=4/5 gives equality; for n>=5 exact sign checks give B>A>0 and B<2A, and Gaussian product/Riemann sum gives z~sqrt(2/(pi n)), B/A=2-6/n+O(n^-3/2). Independently enumerated all labelled connected unicyclic n-edge graphs for n=4,5,6 and exactly verified counts 15,222,3660 and full one/two-edge moments; finite cases corroborate the symbolic uniform proof.

## originality

PASS

Best-of-knowledge, after implication-aware prior/source comparisons: None of the forest-enumeration statements inspected gives the final covariance spectrum or asymptotic condition number without additional substantial nonstandard calculations, though earlier random graph covariance literature may contain an equivalent.

## value

PASS

The uniform connected unicyclic labelled ensemble is a classical, natural sparse random-graph model with exactly one cycle, and its centered edge Walsh Gram conditioning quantifies spectral stability of its first Fourier band. The exact full eigenvalue multiplicities and sharp uniform condition-number bound 2 address a natural sampling/frame problem; neither the known forest polynomial nor the standard Johnson decomposition alone supplies these ensemble-specific moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
