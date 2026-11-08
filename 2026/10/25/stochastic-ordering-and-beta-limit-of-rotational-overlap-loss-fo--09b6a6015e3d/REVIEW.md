# Independent mathematical audit

## correctness

PASS

For every integer n>=3 and circumradius R>0, uniform relative rotation reduces by dihedral symmetry to a uniform folded angle alpha∈[0,k], k=pi/n. The 2n active supporting normals alternate gaps alpha and 2k−alpha (endpoints by continuity), all below pi. Circle-tangent length additivity gives overlap A_n(alpha)=nR²cos²(k)[tan(alpha/2)+tan(k−alpha/2)], strictly decreasing on (0,k). Its max deficit M_n=A(P_n)tan²(k/2)>0. With U=1−alpha/k uniform, exact quantile q_k(U)=tan((1+U)k/2)tan((1−U)k/2)/tan²(k/2), endpoints 1 and 0, decreasing strictly in U. Solving for cos(kU) establishes the CDF with correct support. For fixed U∈(0,1), derivative in k of log q equals [f((1+U)k)+f((1−U)k)−2f(k)]/k with f(z)=z/sin z; direct second derivative f´´(z)=[z(1+cos²z)−sin2z]/sin³z>0 for z∈(0,pi) proves strict Jensen inequality. Because k_n descends with n, q_{k_n}(U)>q_{k_(n+1)}(U), and monotone invertibility implies strict first-order stochastic dominance for every 0<q<1. Uniform tangent Taylor expansion yields q=1−U²+(pi²/(6n²))U²(1−U²)+O(n^-4); E U²(1−U²)=2/15 gives mean 2/3+pi²/(45n²)+O(n^-4); variance→4/45 and n²M_n/R²→pi³/4, proving geometric scaling. Exact expected overlap obtained by integrating tan alpha/2 over [0,k]. n=3, R>0, alpha=0,k, q=0,1 and all integer n boundaries checked. An entirely independent Shapely polygon-intersection implementation verified 1,872 cases n=3..50 with max absolute discrepancy 2.665e−15; SymPy expanded q through k^4 and high-precision quadrature confirmed exact mean for six n. Finite experiments corroborate, not prove, the unbounded n hierarchy.

## originality

PASS

Qualified best-of-knowledge originality for the strict all-side-count stochastic hierarchy of the normalized two-congruent-regular-polygon overlap loss, its universal Beta(1,1/2) law Q∞=1−U², and sharp n^-2 quantile correction. The fixed-n tangency area formula, CDF, and elementary mean are not asserted as novel: the package itself reports an archived unequal-order gap-law antecedent, which is not separately accessible as a complete primary document here. Primary 2012 tangent-area formulas and a published 2026 expected-area theorem supply important prior background. The latter fixes n and varies the number m of intersected copies, and does not derive pointwise stochastic order as n varies. The 2015 rotating-polygons question counts vertices. The 2014 random-rotation convex-body paper could not be read beyond its abstract (public PDF timeout; authorized Oxford VPN disconnected), so no categorical historical-priority claim is made. Three actual Resultary searches and targeted external literature searches returned no stronger explicit cross-order theorem; search absence alone is not novelty proof.

## value

PASS

For a uniformly misaligned pair of congruent regular polygons approaching a disk, normalized overlap-area loss is a natural dimensionless rotational-registration/geometric-probability invariant. The new point is a nontrivial complete stochastic comparison of the entire distribution as polygon side count changes, not a renaming of the known fixed-n area formula or a few small-n numbers. The sharp universal Beta(1,1/2) limiting law, uniform n^-2 correction and geometric unscaled n² law describe the precise transition to rotational symmetry and provide exact calibration and validation targets. This is a motivated family-wide structural inequality with independent mathematical utility; neither reproducibility nor mere novelty is treated as sufficient on its own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
