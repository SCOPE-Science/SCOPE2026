# Sharp weighted \(L^2\) complete-graph maximal norm and one-third mass rigidity

## Finding
Let \(V\) be a finite set with \(|V|\ge2\) and let \(w_i>0\) be arbitrary real vertex masses. Write \(W=\sum_{i\in V}w_i\), \(\mu=W^{-1}\sum_{i\in V}w_i|f_i|\), and define the centered metric-ball maximal operator on the unit-edge complete graph by
\[
(M_w f)_i=\max\{|f_i|,\mu\},\qquad
\|f\|_{2,w}^{2}=\sum_{i\in V}w_i|f_i|^{2}.
\]
For \(0<t<1\), put
\[
\Phi(t)=\frac{2-t+\sqrt{t(4-3t)}}2,
\qquad t_S=\frac{\sum_{i\in S}w_i}{W}.
\]
The exact strong operator norm is
\[
\boxed{\displaystyle \|M_w\|_{L^2(w)\to L^2(w)}^2
=\max_{\varnothing\ne S\subsetneq V}\Phi(t_S).}
\]
Every nonzero extremizer has absolute values constant on a nonempty proper high-value set \(S\) and its complement, where \(S\) maximizes \(\Phi(t_S)\), with strictly positive low value \(b\) and high value \(a>b\) in the precise ratio
\[
\boxed{\displaystyle \frac ab=\frac{\Phi(t_S)-(1-t_S)^2}{t_S(1-t_S)}.}
\]
Conversely, each such two-level input attains the norm. Signs or complex phases may be changed pointwise without changing equality.

The universal inequality is \(\|M_w\|\le 2/\sqrt3\), **with equality if and only if** there exists a subset of vertices with mass exactly \(W/3\). In that event \(|f|=4\) on the one-third-mass subset and \(|f|=1\) on its complement is an extremizer. With strictly positive integer masses given in binary, deciding whether the exact norm equals \(2/\sqrt3\) is weakly NP-complete (in the standard many-one sense). Thus two vertices with masses \(1,2\) attain the universal constant, whereas three vertices with masses \(1,1,2\) do not.

## Assumptions and scope
The graph is complete and its edges have unit length, so a centered graph-metric ball is either a singleton or all of \(V\). Masses are positive, are used both in averages and in the Hilbert norm, and need not be rational except in the complexity statement. The operator acts on arbitrary real or complex functions; its value depends only on absolute values. The complexity problem accepts a finite binary list of strictly positive integers and asks for exact equality with the fixed constant, not floating-point approximation.

## Proof
**1. Reduction to a two-dimensional Rayleigh quotient.** Since \(M_w f=M_w|f|\), assume \(f_i\ge0\). Normalize \(W=1\) and set \(S=\{i:f_i>\mu\}\), \(T=V\setminus S\). Unless \(f\) is constant, \(S,T\) are nonempty and \(0<t:=\sum_{S}w_i<1\). Set \(A^2=\sum_Sw_i f_i^2\), \(B^2=\sum_Tw_i f_i^2\). By Cauchy–Schwarz, \(\mu\le\sqrt t\,A+\sqrt{1-t}\,B\), and therefore
\[
\|M_w f\|_{2,w}^2=A^2+(1-t)\mu^2\le
\begin{bmatrix}A&B\end{bmatrix}
\mathcal B(t)
\begin{bmatrix}A\\B\end{bmatrix},
\quad\mathcal B(t)=\begin{bmatrix}
1+t(1-t)&(1-t)\sqrt{t(1-t)}\\
(1-t)\sqrt{t(1-t)}&(1-t)^2
\end{bmatrix}.
\]
The trace and determinant are \(2-t\) and \((1-t)^2\); its discriminant is \(t(4-3t)\). The largest eigenvalue is exactly \(\Phi(t)>1\). This proves the stated upper bound for each active set. A constant input has quotient one and cannot maximize the norm because \(\Phi(t)>1\) for every nontrivial subset.

**2. Equality and exhaustive classification.** For any nonempty proper \(S\) of mass \(t\), the matrix \(\mathcal B(t)\) has positive off-diagonal entries and hence a simple top eigenvalue with a strictly positive eigenvector \((A,B)\). Choose constants \(a=A/\sqrt t\), \(b=B/\sqrt{1-t}\) on \(S,T\). The bottom row of the eigenvector equation yields
\[
\frac ab=\frac{\Phi(t)-(1-t)^2}{t(1-t)}.
\]
This ratio exceeds one: explicitly \(\Phi(t)-(1-t)^2>t(1-t)\), equivalent to \(\Phi(t)>1-t\), which holds since \(\Phi(t)>1\). Hence \(b<ta+(1-t)b<a\), and the selected high/low sets are exactly the active sets of this input. Both Cauchy–Schwarz and the Rayleigh bound attain equality, giving quotient \(\Phi(t)\). Conversely, every norm extremizer has equality in both inequalities above; Cauchy equality forces its absolute value to be constant in each of \(S,T\), and the Rayleigh equality forces the displayed ratio. This also shows that all maximizers arise exactly from optimal-mass subsets, up to scale and phases.

**3. Universal constant and one-third mass.** Direct differentiation gives that \(\Phi\) rises strictly on \((0,1/3)\), falls strictly on \((1/3,1)\), and takes its unique maximum \(\Phi(1/3)=4/3\). To check the critical point without numerical approximation, \(\Phi'(t)=0\) implies \(2-3t=\sqrt{t(4-3t)}\), whose square reduces to \((1-t)(1-3t)=0\); only \(t=1/3\) lies in \((0,1)\). Since the finite norm is a maximum over attainable subset masses, equality with \(4/3\) holds exactly for a subset of mass \(W/3\). At \(t=1/3\) the eigenvector ratio is \(a/b=4\).

**4. Complexity.** The weighted equality-decision problem is in NP: a subset \(S\) of integer weights summing to one third of their total verifies a yes-instance by exact integer arithmetic. For NP-hardness, reduce the standard positive-integer SUBSET SUM problem. Given weights \(a_1,\ldots,a_n>0\), total \(A\), and \(0<T\le A\), take \(L=2A+1\), and form the positive-integer mass list
\[
(a_1,\ldots,a_n,\ L-T,\ 2L-A+T).
\]
Its total is \(3L\). The last mass is strictly greater than \(L\), while \(A<L\); therefore a subset of mass \(L\) exists if and only if it contains \(L-T\) together with some original masses totaling exactly \(T\). The construction has polynomial binary length. This establishes NP-completeness. As with SUBSET SUM, the reduction gives weak, not strong, NP-completeness; for integer masses a subset-sum dynamic program gives a pseudo-polynomial procedure for the exact norm.

## Verification
Run `python verify_weighted_clique_maximal.py` with Python's standard library. The checker establishes 153 exact-rational two-by-two trace/determinant/discriminant identities, reproduces the known unweighted strong-norm constants, constructs 210 two-level eigenvector extremizers, checks 12,600 random inputs against the exact bound, verifies the integer reduction in 320 exhaustive small instances, and tests the one-third-mass equality criterion. These finite tests are corroboration, not a proof of the universal theorem; the proof above is analytical and uses exact algebra and a classical NP-complete source problem.

## Relationship to prior work
Soria–Tradacete (2014, arXiv:1410.6204) initiated sharp finite-graph maximal-operator bounds, with cardinality/counting-measure normalization and, for \(p>1\), initially bounds rather than a complete graph \(L^2\) exact evaluation. González-Riquelme–Madrid (2020, arXiv:2005.03146), Theorem 4 and §3.1, **already prove** the exact complete-graph \(L^2\) formula and extremizers under *uniform counting measure*: this is recovered by restricting to subset fractions \(t=k/|V|\). Their result and its special case \(|V|\equiv0\pmod3\) are not claimed as new. The same operator can also be viewed as a two-stage nonnegative martingale maximal function for the filtration from the trivial sigma-algebra to the full atomic sigma-algebra; generic Doob bounds do not resolve the precise weighted atomic mass-spectrum or equality decision. The present statement is about arbitrary nonuniform *positive mass vectors*: its exact norm depends on the attainable mass-subset spectrum instead of cardinalities, and its universal-equality decision is NP-complete. The 2022 sequel (arXiv:2011.02630) analyzes further counting-measure graph norms and regularity; its inspected abstract and introduction do not give the nonuniform mass-subset classification. A priori a differently formulated weighted finite-space result might still cover part or all of the present statement.

## Limitations
Only finite complete graph metrics, a common positive atomic measure for averaging and the Hilbert norm, and the strong \(L^2\) operator norm are treated. No all-graph or infinite-space bound with a sharpness classification is claimed. The universal equality problem is weakly NP-complete, not proved strongly NP-complete and not a claim of hardness for approximating the norm to a specified absolute tolerance. Source searches and index comparisons do not establish publication priority or independent mathematical validation.

## References
1. J. Soria and P. Tradacete, *Best constants for the Hardy-Littlewood maximal operator on finite graphs*, first posted October 22, 2014, arXiv:1410.6204, https://arxiv.org/abs/1410.6204 .
2. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, first posted May 6, 2020, arXiv:2005.03146, Theorem 4 and §3.1, https://arxiv.org/html/2005.03146v3 .
3. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, first posted 2020, arXiv:2011.02630, https://arxiv.org/abs/2011.02630 .
4. Classical SUBSET SUM NP-completeness under binary integer encoding, used solely as a standard complexity-theoretic source problem.
