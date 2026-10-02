# Independent audit — 2026-10-01

**Record:** SCOPE-20260921-3d52bbf9bbcb — A sharp phase boundary in the unresolved Muirhead–identric E4 region

**Disposition:** passed

## Final claim

In the Wang–Chu–Qiu \(E_4\) region, with \(s=a+b\) and \(d=|a-b|\), the global comparison between the generalized Muirhead and identric means is governed exactly by \(C(d)=\inf_{z>0}\log\cosh(dz)/(z\coth z-1)\): \(C\) is continuous and strictly increasing, lies strictly between the algebraic E4 boundaries for \(\sqrt{2/5}<d<\log2\), equals \(d\) for \(d\ge\log2\), and separates global domination, boundary equality and mixed-sign behavior.

## C — correctness

**PASS**. The hyperbolic normalization is exact: for \(x=ge^{-z}\), \(y=ge^z\), the sign of \(\log(M/I)\) is the sign of \(R_d(z)-s\). Re-deriving the E4 inequalities gives \(d_0<d<1\) and \(L(d)<s<U(d)\). The small- and large-\(z\) expansions give endpoint values \(3d^2/2\) and \(d\); the Wang–Chu–Qiu E1 boundary yields \(C(d)>L(d)\), while the local and large-\(z\) expansions give \(C(d)<U(d)\) below \(\log2\). Pittenger's sharp power-mean bound gives \(C(d)=d\) for \(d\ge\log2\). Joint compactified continuity and pointwise strict increase in \(d\) prove continuity and strict monotonicity of \(C\). An independent rational check reproduced the displayed negative certificate \(-43568079809/14910328125000\) for the mixed-sign example.

## O — originality

**PASS**. The primary 2010 paper explicitly leaves the complementary E4 region as an open problem. Searches of the later generalized-Muirhead/identric literature and the published-record corpus did not locate a theorem implying the variational threshold \(C(d)\), its collapse at \(d=\log2\), or the complete below/on/above classification. The later sources inspected concern adjacent mean inequalities or different parameter comparisons rather than this missing E4 phase boundary.

### Source inspections

- **Some Comparison Inequalities for Generalized Muirhead and Identric Means** (DOI:10.1155/2010/295620): **OPEN_PROBLEM_SOURCE**. The final Remark says the remaining parameter case is not discussed and is left as an open problem.

## V — scientific value

**PASS**. This resolves a specifically published open comparison region with a necessary-and-sufficient phase curve, identifies the exact fully-positive tail \(d\ge\log2\), and exhibits a rigorous mixed-sign interior example. The result is a natural completion of an existing classification rather than an arbitrary parameter slice.

## Sources and residual risks

- M.-K. Wang, Y.-M. Chu, Y.-F. Qiu, Some Comparison Inequalities for Generalized Muirhead and Identric Means, J. Inequal. Appl. 2010, DOI:10.1155/2010/295620.
- A. O. Pittenger, Inequalities between arithmetic and logarithmic means, Publ. Elektrotehn. Fak. Ser. Mat. Fiz. 678–715 (1981), 15–18.
- Y.-M. Chu, M.-Y. Shi, Y.-P. Jiang, Exact inequalities involving power mean, arithmetic mean and identric mean, Rev. Anal. Numér. Théor. Approx. 40 (2011), DOI:10.33993/jnaat402-1042.
- T. Zhao, Y.-M. Chu, Comparison between the logarithmic and two-parameter generalized Muirhead means, Sci. Sin. Math. 45 (2015), DOI:10.1360/N012013-00175.
- Published-record semantic search for generalized Muirhead/identric E4 phase boundaries and equivalent parameterizations.
- Risk/limit: An equivalent resolution in unindexed or differently parameterized post-2010 literature could still exist; no such implication was found in the inspected sources.
- Risk/limit: No elementary closed form for \(C(d)\) is proved on \((\sqrt{2/5},\log2)\).
- Risk/limit: Uniqueness of the interior minimizer is not proved.
- Risk/limit: Originality remains to the best of knowledge against unindexed literature.

