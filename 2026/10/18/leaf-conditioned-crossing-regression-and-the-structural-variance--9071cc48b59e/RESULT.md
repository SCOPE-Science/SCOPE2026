# Leaf-conditioned crossing regression and the structural variance split in random Cayley trees

## Finding

Consider a uniform labeled Cayley tree on \(n\ge4\) vertices positioned, by their labels, at the vertices of a fixed convex \(n\)-gon. Let \(X_n\) be the number of unordered crossing pairs of tree edges, and let \(L_n\) be the number of leaves. Write \(S(t,k)\) for the Stirling number of the second kind. For every integer \(2\le\ell\le n-1\),

\[
\mathbb E[X_n\mid L_n=\ell]
=\frac{\binom{n-2}{2}}3
\left(1-\frac{S(n-3,n-\ell)}{S(n-2,n-\ell)}\right).
\]

This conditional expectation is **strictly decreasing** as the prescribed leaf number \(\ell\) increases across its entire support. Its endpoint values are \(\binom{n-2}{2}/3\) for paths (two leaves) and zero for stars (\(n-1\) leaves). Furthermore,

\[
\operatorname{Cov}(X_n,L_n)
=-\frac{\binom{n-2}{2}}{3n}
\left(\frac{n-1}{n}\right)^{n-3}<0.
\]

Write \(\mathcal S_n\) for the unlabelled tree shape and \(U_n=\mathbb E[X_n\mid\mathcal S_n]\) for its shape-induced mean crossing count. Then

\[
\operatorname{Var}(U_n)
=\frac{\binom{n-2}{2}(n-1)}{9n^2},
\qquad
\operatorname{Corr}(U_n,L_n)^2
\longrightarrow\frac1{2(e-2)}\approx0.6961.
\]

The latter limit is the fraction of variation in \(U_n\) explained asymptotically by the **best linear predictor from the leaf count**; it does not assert this is the fraction explained by arbitrary nonlinear prediction. By contrast, using the known leading crossing variance \(\operatorname{Var}(X_n)\sim n^3/45\), one obtains

\[
\frac{\operatorname{Var}(U_n)}{\operatorname{Var}(X_n)}
\sim\frac{5}{2n^2},
\qquad
\operatorname{Corr}(X_n,L_n)
\sim -\frac{\sqrt5}{2\sqrt{e-2}}\frac1n.
\]

Thus leaf count provides substantial linear information about the **structural component** of mean crossings even though that component represents a vanishingly small fraction of the total crossing variance.

## Assumptions and scope

The random object is uniform over the \(n^{n-2}\) labeled, unrooted trees on the fixed label set \(\{1,\ldots,n\}\); label \(j\) is placed at polygon vertex \(j\) in circular order. Polygon geometry is otherwise immaterial because only the cyclic order determines crossings. A crossing is an intersection in the *interiors* of two edges; edges sharing an endpoint do not count. The statement holds for every integer \(n\ge4\), with exactly the leaf support \(2\le L_n\le n-1\).

Let \(m=n-2\), \(B=\binom m2\), and \(q=(n-1)/n\). A uniformly random Prüfer code is an iid uniform word \((Y_1,\ldots,Y_m)\) on \(n\) symbols. Let \(J=\sum_{1\le i<j\le m}\mathbf1\{Y_i=Y_j\}\). The number of symbols absent from the code is exactly \(L_n\). Write \(S(t,k)=0\) when \(k>t\).

## Proof

**1. Shape-to-code reduction.** For a fixed abstract tree, a uniformly random assignment of its vertices to the circular positions makes every pair of vertex-disjoint edges cross with probability exactly \(1/3\): among the three pairings of four cyclically ordered positions, exactly one crosses. The number of disjoint edge pairs of a tree is

\[
\binom{n-1}{2}-\sum_{v}\binom{\deg(v)}2.
\]

The Prüfer degree identity \(\deg(v)=1+\#\{i:Y_i=v\}\) gives

\[
\sum_v\binom{\deg(v)}2=m+J,
\qquad
U_n=\frac{B-J}{3}.
\]

The same conditional expectation holds on conditioning on the degree multiset; in particular, \(L_n\) is measurable with respect to tree shape. Therefore \(\mathbb E[X_n\mid L_n]=\mathbb E[U_n\mid L_n]\), and \(\operatorname{Cov}(X_n,L_n)=\operatorname{Cov}(U_n,L_n)\).

**2. Conditional collision probability.** Fix \(\ell\) leaves and write \(k=n-\ell\), the number of distinct symbols used by the Prüfer code. There are \((n)_{\underline{k}}S(m,k)\) code words with exactly \(k\) used symbols, with \((n)_{\underline{k}}=n(n-1)\cdots(n-k+1)\). Requiring \(Y_i=Y_j\) is equivalent to merging the two specified word positions, leaving a word of length \(m-1\) that still uses exactly \(k\) distinct symbols. Thus

\[
\mathbb P(Y_i=Y_j\mid L_n=\ell)
=\frac{S(m-1,k)}{S(m,k)},
\quad
\mathbb E[J\mid L_n=\ell]
=B\frac{S(m-1,k)}{S(m,k)}.
\]

Substituting into \(U_n=(B-J)/3\) proves the displayed conditional regression. For strict monotonicity, the rows of Stirling numbers of the second kind are strictly log-concave on their positive interior. Equivalently, for fixed \(t\), the consecutive ratios \(S(t,k-1)/S(t,k)\) strictly increase with \(k\) where defined (at the positive boundary they increase by the elementary endpoint comparison). The recurrence

\[
\frac{S(m-1,k)}{S(m,k)}
=\frac1{k+S(m-1,k-1)/S(m-1,k)}
\]

for \(1\le k<m\) shows that this fraction strictly decreases with \(k\); the remaining case \(k=m\) has fraction zero. Hence \(\mathbb E[X_n\mid L_n=n-k]\) strictly increases with \(k\), equivalently strictly decreases with \(\ell\). In particular the boundary cases are covered without divisions by zero.

**3. Exact covariance.** For each code symbol \(v\), let \(A_v\) indicate that \(v\) is absent. For distinct positions \(i,j\), independence of other positions gives

\[
\mathbb E[\mathbf1\{Y_i=Y_j\}A_v]
=\frac{q^{m-1}}n,
\quad
\mathbb E[\mathbf1\{Y_i=Y_j\}]=\frac1n,
\quad
\mathbb E[A_v]=q^m.
\]

Therefore \(\operatorname{Cov}(\mathbf1\{Y_i=Y_j\},A_v)=q^{m-1}/n^2\). Summing over \(B\) position pairs and \(n\) vertex labels yields \(\operatorname{Cov}(J,L_n)=Bq^{m-1}/n\). Because \(U_n=(B-J)/3\), this proves the exact negative covariance.

**4. Structural variance.** Two *different* equality indicators \(\mathbf1\{Y_i=Y_j\}\) and \(\mathbf1\{Y_h=Y_k\}\) are uncorrelated, even if the respective pairs overlap in one position: in the overlapping case both equalities hold precisely when three iid symbols coincide, with probability \(1/n^2\). Thus

\[
\operatorname{Var}(J)=B\frac{n-1}{n^2},
\quad
\operatorname{Var}(U_n)=\frac{B(n-1)}{9n^2}.
\]

The leaf indicators satisfy \(\mathbb E A_v=q^m\) and \(\mathbb E A_vA_w=(1-2/n)^m\) for distinct symbols. Hence the exact leaf variance is

\[
V_{L,n}:=\operatorname{Var}(L_n)
=nq^m(1-q^m)+n(n-1)\left((1-2/n)^m-q^{2m}\right).
\]

Combining these identities yields the finite-sample linear prediction coefficient

\[
\operatorname{Corr}(U_n,L_n)^2
=\frac{Bq^{2m-2}}{(n-1)V_{L,n}}.
\]

As \(n\to\infty\), \(B\sim n^2/2\), \(q^m\to e^{-1}\), and elementary second-order expansions give \(V_{L,n}\sim n(e^{-1}-2e^{-2})\). Therefore the squared correlation converges to \(1/[2(e-2)]\).

**5. Total fluctuations.** The published variance asymptotic for convexly embedded uniform Cayley trees is \(\operatorname{Var}(X_n)\sim n^3/45\); inserting this into the exact expressions above proves the last two asymptotic relations. Since \(L_n\) is shape-measurable, the law of total variance yields \(\operatorname{Var}(X_n)\ge\operatorname{Var}(U_n)\). All variance comparisons are for the same model and same fixed circular placement of labels.

## Verification

The supplied standard-library-only `verify.py` exhaustively enumerates Prüfer words for each \(4\le n\le8\), reconstructs each labeled tree, counts actual geometric crossings by interleaving endpoints, and checks the leaf-stratified means, Stirling counts, covariance and structural moments with exact rational arithmetic. It also independently checks the strict ratio inequalities through Prüfer length 100. Execute `python3 verify.py` in the directory containing this file. Successful execution prints `VERIFY_OK 280562 exact assertions; Prüfer enumeration through 8 vertices`. The infinite statements follow from the preceding proof; finite tests are corroboration, not infinite certificates.

## Relationship to prior work

The crossing expectation of a randomly ordered **fixed** tree in terms of degree second moments was already established by Ferrer-i-Cancho (2013); it is not claimed as new here. Arizmendi, Cano and Huemer (2019) established the asymptotic mean, variance and normality of crossing counts in uniform labeled trees; Arenas-Velilla and Arizmendi (2022) gave sharper finite-sample crossing moments. Arenas-Velilla, Arizmendi and Paguyo (2023, arXiv first submission) established crossing moments in random convex embeddings of fixed graphs and Gaussian approximation results. The conditional crossing regression across **every feasible leaf count**, strict order, exact mixed covariance and quantified structural-versus-geometric variation are the subject of the present theorem, rather than the fixed-graph mean or known leaf-count distribution.

Classical Prüfer-code occupancy identities and log-concavity of Stirling numbers are employed as lemmas, not asserted as new. Comparison against broad fixed-graph moment formulas means there is an indirect derivation route from known ingredients. No claim of priority over unidentified earlier leaf-conditioned calculations is made.

## Limitations

The exact conditional identity specifies a conditional **mean**, not stochastic monotonicity or an entire conditional crossing distribution. The nearly 69.6% limit applies to the squared Pearson correlation of the **shape-induced mean** with leaf count, i.e. linear prediction, not to prediction of all crossing randomness or to conditional variance. Polygon vertices must be in strict convex position. The work does not address rooted trees, uniformly random *unlabeled* tree shapes, nonconvex vertex placements or arbitrary drawing models. The exact total-crossing variance is taken from cited prior literature; the shape mean, leaf covariance, variance and asymptotic calculations have independent proofs above. Residual possibility of implicit coverage by older enumerative arguments remains; no independent historical-priority audit has been performed.

## References

1. S. Arenas-Velilla, O. Arizmendi and J. E. Paguyo, *Central limit theorem for crossings in randomly embedded graphs*, arXiv:2308.11570, first posted 2023-08-22. https://arxiv.org/abs/2308.11570 . Primary MSC2020 60C05.
2. S. Arenas-Velilla and O. Arizmendi, *Convergence Rate for the Number of Crossings in a Random Labelled Tree*, arXiv:2209.09431, 2022. https://arxiv.org/abs/2209.09431 .
3. O. Arizmendi, P. Cano and C. Huemer, *On the number of crossings in a random labelled tree with vertices in convex position*, arXiv:1902.05223, 2019. https://arxiv.org/abs/1902.05223 .
4. R. Ferrer-i-Cancho, *Random crossings in dependency trees*, arXiv:1305.4561, 2013. https://arxiv.org/abs/1305.4561 .
5. E. H. Lieb, *Concavity properties and a generating function for Stirling numbers*, Journal of Combinatorial Theory 5 (1968), 203–206. Standard real-rootedness/log-concavity input; no result of this paper is attributed as new.
