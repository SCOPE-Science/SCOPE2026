# A two-switch covariance law for induced graph motifs and degree frequencies

## Finding
Let \(G\sim G(n,p)\), with \(n\ge h\ge3\) and \(0<p<1\), and let \(H\) be a fixed simple graph on \(h\) vertices. Let \(X_H\) count the \(h\)-vertex subsets of \(G\) that induce a graph isomorphic to \(H\), and let \(N_k\) count vertices of degree exactly \(k\), for \(0\le k\le n-1\). For integers \(a\ge0\), write
\[
 b_{a,j}(p)=\begin{cases}\binom ajp^j(1-p)^{a-j},&0\le j\le a,\\0,&\text{otherwise}.\end{cases}
\]
Write \(d_v=\deg_H(v)\), \(e_v=h-1-d_v\), and \(A_v=\binom{n-h}{k-d_v}/\binom{n-1}{k}\), taking an out-of-range binomial coefficient as zero. The exact covariance is
\[
\boxed{\operatorname{Cov}(X_H,N_k)=\mathbb E[X_H] b_{n-1,k}(p)
\left[\sum_{v\in V(H)}\frac{A_v}{p^{d_v}(1-p)^{e_v}}-h\right].}
\tag{1}
\]
In particular, suppose \(H\) has at least one edge and at least one nonedge, and \(d_v\le k\le n-h+d_v\) for every \(v\in V(H)\), so that all \(A_v>0\). The function
\[
 R(p)=\sum_{v\in V(H)} A_vp^{-d_v}(1-p)^{-e_v}
\]
has a *strictly convex logarithm*, tends to infinity at both endpoints, and attains a unique minimum. Consequently, as \(p\) increases through \((0,1)\), the covariance has **exactly two positive-to-negative-to-positive sign reversals** when \(\min R<h\), is positive except for one tangential zero when \(\min R=h\), and is positive everywhere when \(\min R>h\). In particular, no admissible motif–degree pair in this class can undergo three sign reversals.

For a \(d\)-regular \(H\) with \(1\le d\le h-2\), put \(r=h-1\), \(e=r-d\), and \(N=n-1\). Then
\[
 A=\frac{(k)_d(N-k)_e}{(N)_r},\qquad (a)_j=a(a-1)\cdots(a-j+1),
\]
and two sign reversals occur if and only if
\[
\boxed{ A< \left(\frac d r\right)^d\left(\frac e r\right)^e.}\tag{2}
\]
Equality gives a single tangential zero; strict inequality in the other direction gives positive covariance throughout. For fixed \(H\), if \(k=k_N\) and
\[
 \frac{k_N-(d/r)N}{\sqrt N}\longrightarrow t\in\mathbb R,
\]
then, with \(A=A_N\),
\[
\boxed{N\log\left(\frac{A_N}{(d/r)^d(e/r)^e}\right)
 \longrightarrow \frac r2-\frac{r^3t^2}{2de}.}\tag{3}
\]
Thus for sufficiently large \(N\), the covariance stays positive at *all* \(p\in(0,1)\) when \(|t|<\sqrt{de}/r\), while it has exactly two sign reversals when \(|t|>\sqrt{de}/r\). No assertion is made at equality.

A sharp concrete instance is the induced four-cycle \(H=C_4\) against the number \(N_2\) of degree-two vertices:
\[
\boxed{\operatorname{Cov}(X_{C_4},N_2)
=12\binom n4p^4(1-p)^{n-2}
\left[1-\binom{n-1}{2}p^2(1-p)\right].}\tag{4}
\]
For \(n=4,5\) this covariance is strictly positive for all \(0<p<1\); for **every \(n\ge6\)** it is positive, negative, then positive, with the two transition probabilities being exactly the two roots in \((0,1)\) of
\[
 p^2(1-p)=\frac{2}{(n-1)(n-2)}.
\]
Hence six vertices are necessary and sufficient for this double reversal. In the sparse regime \(p=c/n\), with any fixed \(c>0\),
\[
\boxed{\lim_{n\to\infty}\operatorname{Cov}(X_{C_4},N_2)
=\frac{c^4e^{-c}}{2}\left(1-\frac{c^2}{2}\right),}\tag{5}
\]
whose sign changes at \(c=\sqrt 2\).

## Assumptions and scope
All graphs are finite, simple, undirected, and labeled on \([n]\), with independent Bernoulli edges of the *same* probability \(p\). An induced copy is counted once per vertex subset, regardless of automorphisms. Formula (1) holds even for an empty or complete motif and for incompatible degree classes, with the zero-binomial convention. The log-convex two-switch classification requires a nonempty, noncomplete motif and compatibility \(d_v\le k\le n-h+d_v\) for every vertex of the motif. Formula (3) requires the fixed regular motif to have positive numbers of both incident edges and incident nonedges, and the stated degree scaling. The four-cycle calculation concerns *induced* four-cycles, not noninduced four-cycle embeddings.

## Proof
**Conditional degree identity.** Fix an \(h\)-subset \(S\subset[n]\) and write \(I_S\) for its induced-\(H\) indicator. By independence of edges within \(S\) from edges incident to an outside vertex, for \(w\notin S\),
\[
 \mathbb E[I_S\mathbf1\{\deg_G(w)=k\}]=\Pr(I_S=1)b_{n-1,k}(p).
\]
Conditional on \(I_S=1\), each vertex of \(S\) occupies each vertex role of \(H\) with frequency \(1/h\). Given role \(v\), it has \(d_v\) forced neighbors within \(S\) and an independent \(\operatorname{Bin}(n-h,p)\) number of outside neighbors. Summing over \(w\in S\) gives
\[
 \mathbb E\left[I_S\sum_{w\in S}\mathbf1\{\deg_G(w)=k\}\right]
 =\Pr(I_S=1)\sum_{v\in V(H)}b_{n-h,k-d_v}(p).
\]
Summing over \(S\) and subtracting \(\mathbb E[X_H]\mathbb E[N_k]\), with \(\mathbb E[N_k]=nb_{n-1,k}(p)\), yields
\[
 \operatorname{Cov}(X_H,N_k)=\mathbb E[X_H]\left[\sum_v b_{n-h,k-d_v}(p)-h b_{n-1,k}(p)\right].
\]
Divide each nonzero conditional binomial mass by \(b_{n-1,k}(p)\) to obtain exactly \(A_vp^{-d_v}(1-p)^{-e_v}\). This proves (1).

**Log-convexity and crossing count.** Under the compatibility hypotheses put
\[
 \phi_v(p)=\log A_v-d_v\log p-e_v\log(1-p).
\]
Each \(\phi_v''(p)=d_v/p^2+e_v/(1-p)^2>0\), since \(d_v+e_v=h-1>0\). If \(w_v=e^{\phi_v}/\sum_u e^{\phi_u}\), direct differentiation gives
\[
 (\log R)''=\sum_v w_v\phi_v''+\sum_vw_v(\phi_v')^2
 -\left(\sum_vw_v\phi_v'\right)^2>0.
\]
A nonempty motif has at least one \(d_v>0\), and a noncomplete motif has at least one \(e_v>0\). Because all coefficients \(A_v\) are positive, these guarantee \(R(p)\to\infty\) as \(p\downarrow0\) and as \(p\uparrow1\). Strict convexity of \(\log R\), smoothness, and endpoint divergence imply a unique minimum and at most two intersections with the level \(h\). The positive outside factor in (1) transfers this sign pattern to the covariance.

**Regular motifs and central degree window.** For a regular motif all terms of \(R\) coincide, and the single coefficient is
\[
 A=\frac{\binom{N-r}{k-d}}{\binom Nk}
 =\frac{(k)_d(N-k)_e}{(N)_r}.
\]
The maximum of \(p^d(1-p)^e\) occurs uniquely at \(p=d/r\) and equals the right side of (2); comparison of the horizontal level \(A\) with this maximum proves (2). For (3), set \(q_N=k_N/N\), \(q=d/r\). Fixed-order falling-factorial expansions give
\[
 \log A_N=d\log q_N+e\log(1-q_N)
 +\frac{r(r-1)-d(d-1)/q_N-e(e-1)/(1-q_N)}{2N}
 +O(N^{-2}).
\]
Here \(q_N\to q\) stays away from zero and one. The correction numerator at \(q\) equals \(r\), and Taylor expansion at the strict maximum of \(d\log q_N+e\log(1-q_N)\) gives quadratic coefficient \(-r^3/(2de)\). As \(q_N=q+t/\sqrt N+o(N^{-1/2})\), multiplying by \(N\) proves (3), and its strict-sign conclusions follow from (2).

**Four-cycle specialization.** For \(H=C_4\), all four vertices have \(d_v=2\) and \(e_v=1\), and precisely three of the 64 labeled simple graphs on a fixed four-set induce a four-cycle. Thus \(\mathbb E[X_{C_4}]=3\binom n4p^4(1-p)^2\). Substituting \(k=2\) into the conditional-degree identity gives (4). Since \(\max_{0\le p\le1}p^2(1-p)=4/27\), two crossings exist precisely when \(\binom{n-1}{2}>27/4\), i.e. for integer \(n\ge6\). In that case strict increase on \((0,2/3)\) and strict decrease on \((2/3,1)\) of the cubic give exactly two roots. Finally \(\binom n4\sim n^4/24\), \((1-c/n)^{n-2}\to e^{-c}\), and \(\binom{n-1}{2}(c/n)^2(1-c/n)\to c^2/2\), proving (5).

## Verification
The standalone standard-library script `verify.py` exhaustively enumerates every simple labeled graph on four, five, and six vertices at three rational edge probabilities, computes \(\operatorname{Cov}(X_{C_4},N_2)\) by direct weighted enumeration, and compares it to (1) and (4) in exact fractions. It additionally verifies the general conditional-degree formula for an induced four-vertex path with different vertex degrees. The analytic convexity and asymptotic arguments above—not the finite enumeration—prove the all-parameter statements.

## Relationship to prior work
Induced-motif counting and the interaction of network subgraph statistics with other graph observables are established subjects: Fretter, Müller-Hannemann, and Hütt (2012) analyze motif fluctuations under edge-density perturbations; Janson (1990) develops functional limit theory for subgraph counts; Bollobás (1982) studies vertex-degree statistics. The full text of Fürer and Kasiviswanathan (initially available 2008-06-13) concerns approximation of counts of *noninduced embeddings*, not these finite-sample joint covariances. The full text of Bhattacharya, Chatterjee, and Janson (arXiv:2104.07259) concerns asymptotic fluctuations of noninduced subgraph counts in graphon random graphs; its Remark 2.12 explicitly distinguishes induced counts as a separate problem not pursued there. Its four-cycle calculations concern asymptotic nondegeneracy, not cross-covariance with degree-two vertices. No inspected source states the two-switch theorem (1)–(3) or the six-vertex induced-square transition (4). General joint subgraph-count expansions could contain equivalent identities implicitly, and the full text of the especially relevant 2012 motif-fluctuation article was not accessible; these are residual originality risks.

## Limitations
The two-switch theorem does not cover degree classes for which some motif roles are incompatible; formula (1) still applies. The critical-window statement excludes the boundary \(|t|=\sqrt{de}/r\). The sparse covariance limit does not assert a joint central limit theorem. No independent scientific audit has been performed, and an unlocated equivalent result in older random-graph literature cannot be excluded. These statements concern probabilities under the specified homogeneous independent-edge model, not observational networks with dependent edges or fixed degree sequences.

## References
1. M. Fürer and S. P. Kasiviswanathan, *Approximately Counting Embeddings into Random Graphs*, arXiv:0806.2287, first version 2008-06-13, https://arxiv.org/abs/0806.2287.
2. C. Fretter, M. Müller-Hannemann, and M.-T. Hütt, *Subgraph fluctuations in random graphs*, Physical Review E **85** (2012), 056119, published 2012-05-29, https://doi.org/10.1103/PhysRevE.85.056119.
3. S. Janson, *A functional limit theorem for random graphs with applications to subgraph count statistics*, Random Structures & Algorithms **1** (1990), 15–37, https://doi.org/10.1002/rsa.3240010103.
4. B. Bollobás, *Vertices of given degree in a random graph*, Journal of Graph Theory **6** (1982), 147–155, https://doi.org/10.1002/jgt.3190060209.
5. B. B. Bhattacharya, A. Chatterjee, and S. Janson, *Fluctuations of Subgraph Counts in Graphon Based Random Graphs*, arXiv:2104.07259, first version 2021-04-15, https://arxiv.org/abs/2104.07259.
