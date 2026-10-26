# Strict root-degree regression and a linear covariance law for uniform plane-tree path length

## Finding

Let \(\mathcal T_n\) be a uniformly random rooted ordered (plane) tree with \(n\ge2\) edges, among the \(C_n=\binom{2n}{n}/(n+1)\) possibilities. Let \(R_n\) be its root outdegree and \(P_n=\sum_{v\in\mathcal T_n}\operatorname{depth}(v)\) its total root-to-vertex path length. Set
\[
c_{m,r}=\frac r m\binom{2m-r-1}{m-r}\quad(1\le r\le m),
\qquad b_j=\binom{2j}{j},
\]
with \(c_{m,r}=0\) when \(r>m\).

**Exact conditional regression.** For every integer \(n\ge2\) and \(1\le r\le n\),
\[
\mathbb E[P_n\mid R_n=r]
=\frac n2+\frac1{2c_{n,r}}
\sum_{m=r}^{n}m\,b_{n-m}\,c_{m,r}.
\]
For every \(1\le r<n\), this conditional mean decreases **strictly** when \(r\) is replaced by \(r+1\). In particular, for every nonconstant nondecreasing real function \(g\) on \(\{1,\ldots,n\}\),
\[
\operatorname{Cov}(P_n,g(R_n))<0.
\]
The first-step decrease is exactly
\[
\mathbb E[P_n\mid R_n=1]-\mathbb E[P_n\mid R_n=2]=\frac n2.
\]

**Two asymptotic scales.** For every *fixed* integer \(r\ge1\), as \(n\to\infty\) through integers \(n\ge r\),
\[
\mathbb E[P_n\mid R_n=r]
=\frac{\sqrt\pi}{2}n^{3/2}+\frac{2-r}{2}n+O_r(\sqrt n).
\]
Unconditionally,
\[
\operatorname{Cov}(P_n,R_n)=-2n+O(\sqrt n).
\]
These assertions concern conditional means and covariances; no stochastic ordering of the *full conditional distributions* is claimed.

## Assumptions and scope

The tree is sampled uniformly from all **ordered rooted** trees with exactly \(n\) edges (equivalently, \(n+1\) vertices). Root outdegree takes every value \(1,\ldots,n\) with positive probability. Path length counts depth from the designated root (the root contributes zero). No vertex labels or edge weights occur. All finite statements hold for every integer \(n\ge2\); the fixed-root-degree expansion is not uniform when \(r\) grows with \(n\).

Use the usual Dyck contour, writing a step \(+1\) when traversing away from the root and \(-1\) when returning. Let \(A_n\) be the sum of the heights immediately *before* each of its \(2n\) steps. Each edge to a vertex at depth \(d\) contributes \((d-1)+d=2d-1\), hence
\[
A_n=2P_n-n.
\]
The number of returns to zero of the contour equals \(R_n\).

## Proof

Write \(C(z)=\sum_{n\ge0}C_nz^n\), \(B(z)=zC(z)\), and \(S(z)=\sqrt{1-4z}\). The Catalan equation gives
\[
C(z)=\frac1{1-B(z)},\quad B(z)=\frac{1-S(z)}2,\quad
z=B(z)(1-B(z)),\quad B'(z)=S(z)^{-1}.
\]
An irreducible nonempty Dyck path is \(+1\), followed by an arbitrary Dyck path, followed by \(-1\). Thus its size generating function is \(B(z)\). A Dyck path with exactly \(r\) returns is an ordered concatenation of \(r\) irreducibles, so it is counted by \(B(z)^r\). Lagrange inversion for \(B=z/(1-B)\) gives
\[
[z^m]B(z)^r=c_{m,r}=\frac r m\binom{2m-r-1}{m-r}.
\]

Let \(F(z)\) be the sum of contour areas of all Dyck paths and \(W(z)\) the sum of areas of irreducible paths, both marked by semilength. Area is additive across excursions; therefore \(F=W/(1-B)^2\). If an irreducible excursion has interior of semilength \(m-1\), shifting its interior one level higher adds \(2m-1\) to its contour area. Therefore
\[
W(z)=zF(z)+2zB'(z)-B(z).
\]
Substitution of \(F\), together with \(z=B(1-B)\) and \(1-2B=S\), gives
\[
W(z)=\frac{z}{S(z)^2}=\frac z{1-4z}.
\]
For precisely \(r\) excursions the area sum is
\[
Q_r(z)=rW(z)B(z)^{r-1}
=\frac z{S(z)}\frac{d}{dz}B(z)^r.
\]
Since \(S(z)^{-1}=\sum_{j\ge0}b_jz^j\), coefficient extraction yields
\[
[z^n]Q_r(z)=\sum_{m=r}^{n}m\,c_{m,r}\,b_{n-m}.
\]
Dividing by \(c_{n,r}\), then using \(P_n=(A_n+n)/2\), proves the exact conditional expectation.

For \(r=1\) and \(m\ge2\), \(c_{m,1}=c_{m,2}=C_{m-1}\). The only additional summand at \(r=1\) is \(m=1\). Since \(c_{n,1}=\binom{2n-2}{n-1}/n\),
\[
\mathbb E[A_n\mid R_n=1]-\mathbb E[A_n\mid R_n=2]=n.
\]
For \(2\le r<n\) and \(m\ge r+1\),
\[
\frac{c_{m,r+1}}{c_{m,r}}
=\frac{r+1}{r}\frac{m-r}{2m-r-1}.
\]
For fixed \(r>1\), the right-hand side is strictly increasing as a function of \(m\) (its derivative with respect to real \(m\) has the sign of \(r-1\)). Consequently for every \(r+1\le m<n\),
\[
\frac{c_{m,r+1}}{c_{n,r+1}}
<\frac{c_{m,r}}{c_{n,r}}.
\]
The term \(m=n\) in the area regression equals \(n\) for both degrees; all intermediate weighted terms decrease and the positive \(m=r\) term disappears. Strict decrease follows. For the covariance statement, put \(h(r)=\mathbb E[P_n\mid R_n=r]\). If \(R_n'\) is an independent copy,
\[
2\operatorname{Cov}(P_n,g(R_n))
=\mathbb E[(h(R_n)-h(R_n'))(g(R_n)-g(R_n'))]<0,
\]
because \(h\) decreases strictly, \(g\) is nonconstant nondecreasing, and every degree occurs with positive probability.

For asymptotics, with fixed \(r\),
\[
Q_r(z)=\frac{r}{2^{r+1}}
\left(S^{-2}-(r-1)S^{-1}+O_r(1)\right),
\quad B(z)^r=2^{-r}(1-S)^r.
\]
These are *finite Laurent/polynomial expansions in \(S\)*, so the standard binomial coefficients of \(S^j\) justify coefficient extraction, with the next nonpolynomial terms bounded by \(O_r(4^n n^{-3/2})\) in \(Q_r\) and \(O_r(4^n n^{-5/2})\) in \(B^r\). In particular,
\[
[z^n]Q_r=\frac r{2^{r+1}}\left(4^n-(r-1)\binom{2n}{n}
+O_r(4^n n^{-3/2})\right),
\]
\[
c_{n,r}=\frac{r}{2^{r+1}}\frac{4^n}{\sqrt\pi\,n^{3/2}}
(1+O_r(n^{-1})).
\]
It follows that \(\mathbb E[A_n\mid R_n=r]=\sqrt\pi n^{3/2}-(r-1)n+O_r(\sqrt n)\), and hence the stated path-length expansion.

Finally, let \(Q(z)=\sum_{r\ge1}Q_r(z)\). Summing geometrically gives the generating series of the *unconditional totals* of contour area and of its product with the number of returns:
\[
Q(z)=\frac{W(z)}{(1-B(z))^2}=\frac{1-S}{S^2(1+S)},
\quad
\sum_{r\ge1}rQ_r(z)=\frac{W(z)(1+B(z))}{(1-B(z))^3}
=\frac{(3-S)(1-S)}{S^2(1+S)^2}.
\]
Their singular terms are respectively \(S^{-2}-2S^{-1}+O(1)\) and \(3S^{-2}-10S^{-1}+O(1)\). Coefficient extraction divided by \(C_n\sim4^n/(\sqrt\pi n^{3/2})\) gives
\[
\mathbb E[A_n]=\sqrt\pi n^{3/2}-2n+O(\sqrt n),
\quad
\mathbb E[A_nR_n]=3\sqrt\pi n^{3/2}-10n+O(\sqrt n).
\]
Also \(\mathbb E[R_n]=3n/(n+2)=3-6/n+O(n^{-2})\), by extracting \([z^n]B/(1-B)^2\). Therefore
\[
\operatorname{Cov}(A_n,R_n)=-4n+O(\sqrt n),
\quad \operatorname{Cov}(P_n,R_n)=-2n+O(\sqrt n),
\]
completing the proof.

## Verification

The accompanying standalone `verify.py` enumerates all Dyck paths through semilength nine and independently compares root-degree counts and total contour areas against the derived coefficient formulas. It also checks the strict regression and boundary identity for sizes through 60, exact algebraic ratios, and negative finite covariances. Run `python3 verify.py` using the standard Python library. The script is a finite corroboration only; the unrestricted claims are proved above.

## Relationship to prior work

Janson's *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation* (arXiv:1112.0510v1, December 2, 2011) establishes uniform ordered-tree structure, root-degree asymptotics and conditioned offspring laws. Its Sections 2, 7, and 14 were consulted; the root-degree law does not itself determine the root-degree-conditioned global path length.

Blanco and Petersen's *Counting Dyck paths by area and rank* (arXiv:1206.0803v1, June 2012) develops joint Dyck-path area and noncrossing-lattice rank formulas; their rank statistic is not the number of returns. Their area is expressed in the customary diagonal-cell convention, whereas the present contour sum is \(2P_n-n\). Their first-return decomposition is consistent with, but does not directly state, the decreasing conditional path-length regression proved here.

Wagner's *Central Limit Theorems for Additive Tree Parameters with Small Toll Functions* (DOI:10.1017/S0963548314000443, first online September 8, 2014; published primary classification 60C05) concerns additive tree parameters with small toll functions. The path-length toll equals the tree's size and is outside its indicated small-toll setting. Its publisher abstract and accessible bibliographic/author-version excerpts were inspected; the complete text could not be reliably retrieved and remains a priority risk.

A published research-record search also surfaced related exact root-attachment/path-length results for *random recursive trees* and root-degree/leaf results, but those use a different probability law from the uniform Catalan plane-tree model. No covering statement for the present conditional regression and \(-2n\) covariance law was identified in the material inspected. This comparison is not a claim of exhaustive historical priority.

## Limitations

The result concerns means and covariances, not stochastic dominance between conditional path-length distributions. The \(O_r\)-bound allows its implied constant to depend on the fixed root degree. Nothing is asserted for labels, nonuniform offspring weights, or general simply generated trees. Finite verification cannot replace proof. Historical priority against inaccessible full articles and implicit coefficient specializations requires independent examination.

## References

- S. Janson, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*, arXiv:1112.0510v1 (2011-12-02), https://arxiv.org/abs/1112.0510 .
- S. A. Blanco and T. K. Petersen, *Counting Dyck Paths by Area and Rank*, arXiv:1206.0803v1 (2012-06-05), https://arxiv.org/abs/1206.0803 .
- S. Wagner, *Central Limit Theorems for Additive Tree Parameters with Small Toll Functions*, first published online 2014-09-08, DOI:10.1017/S0963548314000443, https://doi.org/10.1017/S0963548314000443 .
