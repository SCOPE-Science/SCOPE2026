# Independent mathematical audit

## correctness

PASS

For each alpha>1, rational disk heights a_j=1/floor(j^alpha) eventually have gap a_j-a_{j+1} ~ alpha j^{-alpha-1}, so at mesh c/N they have matching packing/cover orders N^{1/(alpha+1)}. Each disk rotation frequency equals height a, giving |e^{2pi ita}-e^{2pi itb}|<=2pi t|a-b|. A height net at O(1/N) mesh and a fixed planar epsilon-net give an N-step Bowen spanning bound O(N^{1/(alpha+1)}) for X; ordered n-point products and Hausdorff factor give upper exponent n/(alpha+1). For lower bound, mark each of n points by fixed distinct radii r_i=i/(n+1) and select independently from cN^{1/(alpha+1)} heights spaced >=1/N and <=1/8. A changed ith height delta gives integer t=ceil(1/(4delta))<N with tdelta in [1/4,3/8], so same-radius chord separation >=sqrt(2)r_i, while different radii are always distance >=1/(n+1); thus (N,Delta)-separation of >=c^n N^{n/(alpha+1)} unlabeled configurations. Each configuration remains >=Delta/2 from singleton stratum; the quotient metric min(d,distA+distB) retains separation for n>=2. Full compact hyperspace contains F_n for all n, hence infinite polynomial entropy. Each finite subset is periodic (LCM of finitely many rational rotations), and bounded polynomial growth implies zero ordinary entropy. Independent exact-rational gap/phase checks at alpha=2,N=1000,10000,100000 corroborated the scale and tdelta inequalities; infinite assertions use the analytic proof, not samples.

## originality

PASS

The original 2026 Đorić–Katić–Perić rotating-disk paper provides the space, base polynomial-entropy exponent and height packing, which are credited. A Đorić symmetric-product/suspension paper has the same formal multiplier n but requires a finite chain recurrent set or wandering points; those assumptions decisively fail because every point here is periodic and the chain recurrent set is an infinite continuum, with no wandering points. Naghmouchi studies ordinary topological entropy of hyperspaces of pointwise periodic maps, not their exact polynomial entropy. The explicit radial-marker argument is the novel surviving extension by best knowledge; full texts of closest 2026 sources were not available, so uninspected statements remain priority risks.

## value

PASS

Every finite-layer polynomial-entropy exponent n/(alpha+1), its survival under singleton collapse and the full hyperspace infinite complexity together create a natural unbounded hierarchy despite all base points and finite configurations being periodic. This exactly probes the boundary of finite-recurrent-set and wandering-point hypotheses in established induced-dynamics entropy results; it is more than a mechanical n-fold product application because unlabeled configurations and quotient collapse require distinct-radius separation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
