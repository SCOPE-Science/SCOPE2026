# Independent mathematical audit

## correctness

PASS

Reconstructed the real Hermitian normal operator by Fourier orthogonality. With gain sqrt(t) on derivative intensities, its blocks are 5uuᵀ+3twwᵀ, two copies of [[5,5],[5,5+12t]], and two scalars 5. The diagonal block has trace 15+51t, product 390t of its nonzero eigenvalues, and kernel span(diag(3,-4,1)); the 2-by-2 blocks have trace 10+12t and determinant 60t. The kernel generator has rank three, which excludes every nonzero projector difference. Independently, put r=sqrt(985), R=(33+r)/4, d(t)=(15+51t+sqrt(225-30t+2601t²))/2 and c(t)=5+6t-sqrt(25+36t²). The full squared condition number is at least d(t)/c(t). At 40/81 these are the actual extreme positive eigenvalues and d=Rc. Their derivatives there are (51+1371/r)/2 and 6-96/r, respectively, so d−Rc has zero derivative there. The top affine-block eigenvalue d is convex and −c is strictly convex (the second derivative of sqrt(25+36t²) is positive); hence d−Rc is strictly positive elsewhere. Substitution gives the listed squared spectrum and multiplicities. For rank at most two, compress Q to the range of H and apply Cauchy–Schwarz: the compression has squared Frobenius norm at most 4²+3²=25 (the two largest eigenvalues of Q²), giving squared distance to span Q at least ||H||²_F/26. This proves the stated f/26 stability bound with f the least positive squared singular value. Read the supplied checker and transcript as recorded evidence; did not execute uploaded code.

## originality

PASS

The supported distinct claim is the exact spectrum, unique relative gain and corresponding lifted condition number, with a concrete stability bound for this specific frame. Qualitative injectivity and the general rank-two test are prior coverage, explicitly not claimed as novel. No examined primary or indexed statement supplies or specializes to the quantitative optimization.

## value

PASS

The two natural root grids capture the full value and derivative intensity Fourier coefficients with eight readings. For users of that specific nonredundant structured acquisition, the exact gain balances the least observable and most amplified Hermitian directions, without numerical weight tuning. The exact spectrum also gives a certified global inverse-stability scale for projector differences. The meaningful addition is quantitative design, not another proof of qualitative injectivity or optimality among all frames.

The dated certificate retains the supplied scientific assessment, sources and limitations.
