# A sharp heterogeneous-feedback placement transition on complete bipartite networks

## Finding

Let \(K_{p,q}\) be the simple unit-conductance complete bipartite graph with integer part sizes \(2\le p<q\). Select **two distinct vertices** to receive respectively prescribed gains \(a\ge b>0\). For its combinatorial Laplacian \(L\), minimize
\[
J(u,v)=\operatorname{tr}\left[(L+a e_u e_u^{\mathsf T}+b e_v e_v^{\mathsf T})^{-1}\right]
\]
over all ordered pairs of distinct vertices \((u,v)\). Here \(u\) receives gain \(a\) and \(v\) receives gain \(b\); the trace is twice the total steady-state variance under independent unit-intensity white disturbances.

Write \(A\) for the part of size \(p\), and \(B\) for the part of size \(q\). Define
\[
\begin{aligned}
S&=q(q^2-q-3p^2),\\
H&=(p-2)[q^2-p(p-1)]+q(p+2),\\
W&=(2p-1)q(q-1)-p^2(2p-5),\\
D&=S-bH,\\
E&=q(2p^2q+bW),\\
F&=bpq^2(q-p)(p+q-1).
\end{aligned}
\]
For the stated integers and gains, \(H,E,F>0\). **The exact optimizer classification is:**

1. If \(D\le0\), exactly the placements with **both** selected vertices in \(A\) minimize \(J\).
2. If \(D>0\), let
\[
a_* =\frac{E+\sqrt{E^2+4DF}}{2D}>b.
\]
For \(b\le a<a_*\), exactly both-in-\(A\) placements minimize \(J\); at \(a=a_*\), both-in-\(A\) and the placements putting the gain-\(a\) leader in \(A\) and the gain-\(b\) leader in \(B\) tie; for \(a>a_*\), precisely the latter split placements minimize \(J\). All claims of uniqueness are up to permutations within the two vertex parts. No placement with the stronger leader in \(B\), and no both-in-\(B\) placement, minimizes \(J\).

The split phase is possible for some positive gains **if and only if** \(q^2-q>3p^2\); for fixed weaker gain \(b\), it is possible if and only if
\[
0<b<\frac{q(q^2-q-3p^2)}{(p-2)[q^2-p(p-1)]+q(p+2)}.
\]
Among graphs with \(2\le p<q\), \(K_{2,5}\) is the unique smallest-order graph admitting any such transition. For \(K_{2,5}\) with \(b=1\), the transition is exactly
\[
\boxed{a_*=13+\sqrt{214}}.
\]
Thus \(a=27\) chooses two vertices in the two-vertex part, whereas \(a=28\) chooses one vertex from each part, with the stronger leader in the two-vertex part.

## Assumptions and scope

All edges of \(K_{p,q}\) have unit weight; \(p,q\) are integers with \(2\le p<q\). The two prescribed gains are strictly positive and finite and are attached to two *different* vertices. Gains are not redistributed or optimized, and all vertices experience the same independent disturbance intensity. The objective includes the noise response of leaders as well as followers. No conclusion is asserted for unequal edge weights, more than two leaders, gains constrained by a common budget, or other network families. If gains were initially presented in reverse order, exchange their labels to ensure \(a\ge b\).

## Proof

**1. Exact trace identity.** Put \(N=p+q\), \(G=L^+\), \(K=G^2\), and \(T=\operatorname{tr}G\). For any distinct vertices \(u,v\), set \(g_{ij}=G_{ij}\), \(k_{ij}=K_{ij}\), and \(r=g_{uu}+g_{vv}-2g_{uv}\). The matrix-tree theorem, the determinant lemma, and the Laurent expansion
\[
(L+zI)^{-1}=\frac{\mathbf1\mathbf1^{\mathsf T}}{Nz}+G-zK+O(z^2)
\]
give, on differentiating the determinant at \(z=0\),
\[
\begin{split}
J(u,v)=T+\frac{1}{a+b+abr}\bigl\{&N[1+ag_{uu}+bg_{vv}+ab(g_{uu}g_{vv}-g_{uv}^2)]\\
&-ab(k_{uu}+k_{vv}-2k_{uv})\bigr\}.
\end{split}
\tag{1}
\]
This derivation is valid because the weighted-pinned Laplacian is positive definite for \(a,b>0\) on a connected graph. Specifically, \(\det(L+zI)=zN\tau(1+zT+O(z^2))\), where \(\tau\) is any principal cofactor of \(L\). Inserting the Laurent expansion into the rank-two determinant lemma and comparing the coefficients of \(z^0,z^1\) proves (1) without any limiting-gain assumption.

**2. Bipartite spectral data.** The nonzero Laplacian eigenvalues are \(q\) on the \((p-1)\)-dimensional part-\(A\) contrast subspace, \(p\) on the \((q-1)\)-dimensional part-\(B\) contrast subspace, and \(N\) on the remaining one-dimensional nonconstant subspace. Thus \(T=(p-1)/q+(q-1)/p+1/N\). The entries required by (1), with \(x,y\) distinct vertices in the indicated parts, are
\[
\begin{array}{c|ccc}
 & x,y\in A & x,y\in B & x\in A,y\in B\\\hline
G_{xx}&(1-1/p)/q+q/(pN^2)&(1-1/q)/p+p/(qN^2)&\text{as at left/right}\\
G_{xy}&-1/(pq)+q/(pN^2)&-1/(pq)+p/(qN^2)&-1/N^2\\
K_{xx}&(1-1/p)/q^2+q/(pN^3)&(1-1/q)/p^2+p/(qN^3)&\text{as at left/right}\\
K_{xy}&-1/(pq^2)+q/(pN^3)&-1/(qp^2)+p/(qN^3)&-1/N^3.
\end{array}
\tag{2}
\]
The diagonal formulas apply separately to the appropriate part and do not depend on which other vertex is chosen.

**3. Reduce all placements to two candidates.** Denote by \(J_{AA},J_{BB},J_{AB},J_{BA}\) the four classes, where the first letter identifies the part of the gain-\(a\) vertex. Substituting (2) into (1) and simplifying gives
\[
J_{AB}-J_{BA}=\frac{(a-b)(p-q)(N-1)}{ab(N-1)+pq(a+b)}\le0.
\tag{3}
\]
A second difference identity is
\[
J_{AA}-J_{BB}=\frac{(p-q)\,U}{pq[2ab+p(a+b)][2ab+q(a+b)]},
\tag{4}
\]
where
\[
U=2a^2b^2(N-4)+ab(a+b)N(N-4)
+pq\{(N-1)(a-b)^2+2ab(N-2)\}>0.
\]
Since \(p<q\) and \(N\ge5\), both-in-\(B\) is strictly worse than both-in-\(A\), and putting the stronger leader in \(B\) is no better than putting it in \(A\). At equal gains the mixed orientations tie, but both-in-\(A\) is still strictly better by step 4. Hence every minimizer is either \(AA\) or \(AB\).

**4. A single quadratic threshold.** Algebraic simplification of (1) gives the exact identity
\[
J_{AB}-J_{AA}=
-\frac{b\,[Da^2-Ea-F]}{pq[2ab+q(a+b)][ab(N-1)+pq(a+b)]}.
\tag{5}
\]
The denominator is strictly positive. Also \(H>0\), because \(q^2>p(p-1)\) and \(p\ge2\); and
\[
W\ge(2p-1)p(p-1)-p^2(2p-5)=2p^2+p>0.
\]
Therefore \(E,F>0\). If \(D\le0\), the polynomial \(Da^2-Ea-F\) is negative at every \(a>0\), proving the first regime. If \(D>0\), that polynomial has exactly one positive zero, which is the displayed \(a_*\), and changes sign from negative to positive there.

To verify that this zero lies strictly **above** the permitted diagonal \(a=b\), define
\[
V=(p-1)q(q-1)-p^2(p-4)\ge p(2p+1)>0.
\]
Direct substitution gives
\[
[Da^2-Ea-F]_{a=b}
=-b\{b^2H+2bqV+2p^2q^2+pq^2(q-p)(N-1)\}<0.
\tag{6}
\]
The positive zero must therefore exceed \(b\). Equation (5) yields all strict inequalities and the exact tie case.

**5. Exact onset.** Since \(H>0\), some positive choice of \(b\) can yield \(D>0\) exactly when \(S=q(q^2-q-3p^2)>0\). This proves the claimed imbalance condition and the weaker-gain cutoff. With \(p\ge2\) and \(q>p\), no graph of fewer than seven vertices satisfies \(q^2-q>3p^2\). At seven vertices, the only qualifying pair is \((p,q)=(2,5)\). Substituting \((p,q,b)=(2,5,1)\) into the polynomial in (5) gives \(20(a^2-26a-45)\), whose unique positive root is \(13+\sqrt{214}\). This lies between \(27\) and \(28\), giving the exact witness.

## Verification

The accompanying `verify_bipartite.py` checks (3)–(6) by symbolic rational simplification, compares all four performance classes with independently inverted exact Laplacian matrices across a finite rational parameter grid, and checks the seven-vertex threshold polynomial. The script requires Python 3 and SymPy. Its successful output on the reviewed package was:

`VERIFY_OK 880 exact symbolic identities, rational matrix traces and location inequalities`

The finite tests are not used to infer an infinite statement. Arbitrary part sizes and gains follow from the spectral decomposition, rational difference identities, and explicit sign arguments in the proof.

## Relationship to prior work

Lin, Fardad and Jovanović [1] formulate the same inverse-trace leader-selection objective with general prescribed feedback strengths and obtain general relaxations, greedy schemes and rank-one update formulas; their results do not give the present complete bipartite two-leader switching classification. Fitch and Leonard [2] give a graph-theoretic two-leader theory and explicit solutions for paths and cycles, but their stated network model assumes the same gain at all leaders. Their equal-gain result does not imply the heterogeneous-gain relocation threshold. Clark, Bushnell and Poovendran [3] study leader selection under *link* noise, using supermodularity rather than this model of independent state disturbances. Previous special classifications for three and four equal-gain leaders on complete bipartite graphs concern different cardinalities; a result about optimally *allocating* a continuous gain budget is likewise not a theorem for two prescribed gains at distinct vertices.

## Limitations

The result is not an algorithmic lower bound for arbitrary graphs and gives no classification for other leader counts, weighted edges or optimized gain budgets. General convex relaxations can evaluate the objective but do not themselves supply these sharp closed-form transitions. Equivalent specialized deductions in unindexed literature remain possible, so bibliographic uniqueness is not established.

## References

[1] F. Lin, M. Fardad and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, first public arXiv posting 3 February 2013, arXiv:1302.0450, particularly Sections II–III.

[2] K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, first public arXiv posting 7 July 2014, arXiv:1407.1569, particularly Section II and Section V.

[3] A. Clark, L. Bushnell and R. Poovendran, *A Supermodular Optimization Framework for Leader Selection under Link Noise in Linear Multi-Agent Systems*, first public arXiv posting 4 August 2012, arXiv:1208.0946, particularly Sections I–II.
