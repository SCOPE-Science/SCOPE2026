# Independent mathematical audit

## correctness

PASS

For the repaired claim, a known exact per-edge cut-projection row sum is 2+f_N(u)+f_N(v) for parts of sizes u,v. At fixed t=u+v, strict concavity forces the balanced integer split. For r>=3 and N>=5, each allowed increment of the balanced score equals f_N(k+1)-f_N(k) with k=floor(t/2)<=(N-2)/2, and its numerator is at least (N-2)(N-4)/4>0. The optimal t is therefore exactly N-r+2, leaving only singleton parts. For r=2 the sum is forced and for r>=3, N<=4 each fixed count has only one multiset. Substitution gives the optimized value, and the reciprocals sum to 4/N+O_r(N^-2), giving the correction r+6. In the original, the row identities themselves check out by solving the zero-mean vertex dipole and counting absolute differences; diagonal entry R>0 gives S_Q=S_P+1-2R. But the original proof line 110 makes a false comparison with the balanced bipartite graph at the same N (at N=5, K_{2,2,1} yields 26/15 versus K_{3,2} at 5/3); the original strict universal bounds instead follow directly from a+b<=N and R>0. Also, K_{N-2,1,1} has tied cut-projection edge orbits, so an attaining edge between largest parts need not be the only type. The replacement makes no cross-count comparison or claim about uniqueness of a norming edge.

## originality

PASS

PASS is restricted to the repaired fixed-(N,r) extremum and uniqueness theorem. The frozen claim as a whole fails originality: both exact canonical row and norm formulas and cut attainment between two largest parts are already explicit in the October 18 complete-multipartite result, which the repair credits and uses solely as input. Its formulas also imply the frozen balanced-bipartite evaluations and global envelope consequences. The constrained optimization and its sharp first correction were not stated by the inspected prior results; they require a new comparison across part multisets and equality analysis.

## value

PASS

The original per-graph formulas are known and would not justify acceptance by themselves. The remainder answers a natural worst-case design question for bounded edge error at specified vertex budget and number of vertex classes. The unique extremizer concentrates non-singleton mass into two almost equal groups, rather than balancing the entire partition, and the dependence of the optimized deficit on the prescribed number of classes is explicit. The proof of strict concentration and equality across all boundary counts is substantive beyond evaluating or tabulating one known norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
