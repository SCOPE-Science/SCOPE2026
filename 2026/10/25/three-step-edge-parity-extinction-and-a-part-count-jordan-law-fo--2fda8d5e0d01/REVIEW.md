# Independent mathematical audit

## correctness

PASS

For every r>=2 and even part sizes n_i>=2, take the binary unsigned vertex-edge incidence matrix B of the connected multipartite graph. The line-graph adjacency is exactly F=B^T B because a diagonal incidence inner product is 2=0 in F_2. The image of B is W={y:sum y=0}, dim N-1, and ker B^T=<1_N>, which lies in W for even N; hence rank F=N-2. BB^T=A_G on even-degree vertices. On W it sends each vertex in part i to the part sum s_i, with sum_i s_i=0; the image is (r-1)-dimensional in part-constant space and hits <1_N> exactly when r is even. Thus rank F^2=c=r-1-1_{r even}. Because every part size is even, A_G annihilates part-constant vectors: F^3=B^T A_G^2 B=0. The ranks force Jordan block counts b3=c, b2=N-2-2c, b1=E-2N+4+c, and kernel sizes give the asserted complete H_0..H_3 extinction census. The r=2 and r>=3 sharp depth boundaries are handled. Independently constructed GF2 line-graph adjacency and exact rank triples for eight even-part profiles in private scratch calculations; the actual unrestricted proof, not these finite cases, establishes all sizes.

## originality

PASS

Best-of-knowledge based on actual source-tree proof inspection, prior claim/implication comparisons and the explicit coverage boundaries. Classical binary cut-cycle code or adjacency-rank literature may already contain an equivalent part-count Jordan formula under different terminology.

## value

PASS

The line-graph edge-neighbour XOR rule is a natural finite-field dynamical system. The complete arbitrary-part-size Jordan decomposition, full initial-state extinction census and parity plateaus in the number of parts are more informative than the standard incidence identity; they provide exact worst-case convergence and proportions of exceptional depths. The treatment is sharply restricted to even-sized parts and F_2, a motivated structural boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
