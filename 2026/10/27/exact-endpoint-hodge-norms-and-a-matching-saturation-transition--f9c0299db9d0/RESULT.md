# Exact endpoint Hodge norms and a matching-saturation transition in complete bipartite graphs

## Finding

Fix integers \(m\ge4\), \(n\ge2\) and \(0\le t\le\lfloor m/2\rfloor\). Let \(G_{m,n,t}\) be the simple unweighted graph obtained from \(K_{m,n}\) by inserting \(t\) disjoint edges between vertices of its \(m\)-vertex class. All choices of this matching yield isomorphic graphs. Write \(Q_t\) for the Euclidean-orthogonal projection of the real edge-coordinate space onto the cut space, and \(P_t=I-Q_t\) for its cycle-space complement.

Define
\[
q_0=3-\frac2m-\frac2n+\frac2{mn},\qquad
p_0=4\left(1-\frac1m\right)\left(1-\frac1n\right),
\]
and the continuous-at-the-boundary piecewise rational functions
\[
d_Q(m,n)=\begin{cases}
-\dfrac{n-2}{n(n+2)},&m\le n+2,\\[2pt]
\dfrac{mn-2n^2-2n+4}{mn(n+2)},&m\ge n+2,
\end{cases}
\]
\[
d_P(m,n)=\begin{cases}
-\dfrac{n-4}{n(n+2)},&m\le n+2,\\[2pt]
\dfrac{m-2n+2}{mn},&m\ge n+2.
\end{cases}
\]
Then the induced real endpoint norms are **exactly**
\[
\begin{array}{c|cc}
\text{matching size}&\|Q_t\|_{1\to1}=\|Q_t\|_{\infty\to\infty}&
\|P_t\|_{1\to1}=\|P_t\|_{\infty\to\infty}\\ \hline
 t=0&q_0&p_0\\
1\le t<m/2&q_0+\max\{0,d_Q(m,n)\}&p_0+\max\{0,d_P(m,n)\}\\
2t=m&q_0+d_Q(m,n)&p_0+d_P(m,n)
\end{array}
\]
(the last row is possible only when \(m\) is even). Thus **once the first matching edge is inserted, adding further disjoint edges leaves *both* norms completely unchanged until, potentially, the final edge saturates the entire \(m\)-vertex class**.

More sharply, if \(m\ge4\) is even and \(n\ge5\), compare the graphs immediately before and after saturation, at \(t=m/2-1\) and \(t=m/2\):

* If \(m\le2n-4\), both norms strictly decrease on adding the last edge.
* If \(m=2n-2\) or \(m=2n\), only the cut-projection norm strictly decreases.
* If \(m\ge2n+2\), neither norm changes.

For instance, for \(m=4\), \(n=7\), the norms at matching sizes \(t=0,1\) are respectively \(16/7\) and \(18/7\); after the second matching edge they become \(139/63\) and \(53/21\). Hence adding an edge can simultaneously reduce the two canonical complementary projection norms, but no prior addition within that disjoint matching changed either one.

## Assumptions and scope

All graphs are finite, simple, connected and unit-conductance. Let \(D\) be any oriented vertex-edge incidence matrix and \(L=DD^{\mathsf T}\). The projections are \(Q_t=D^{\mathsf T}L^+D\) and \(P_t=I-Q_t\); edge-orientation changes only conjugate these matrices by a diagonal sign matrix. The stated norms are the real induced \(\ell_1\) and \(\ell_\infty\) norms, not minimum norms over arbitrary projections.

For an edge \(e=\{u,v\}\), let \(\phi\) solve \(L\phi=\mathbf1_u-\mathbf1_v\), up to an additive constant. The absolute \(e\)-column sum of \(Q_t\) is \(\sum_{xy\in E}|\phi_x-\phi_y|\), while the absolute \(e\)-column sum of \(P_t\) is this sum plus \(1-2(\phi_u-\phi_v)\), because \(0<\phi_u-\phi_v<1\). The final strict inequality holds here since all edges belong to cycles. Symmetry of both projections implies equality of their induced \(\ell_1\) and \(\ell_\infty\) norms.

## Proof

Write \(A\) for the \(m\)-vertex class and \(B\) for the \(n\)-vertex class. The Laplacian block matrix has diagonal blocks \(nI+L_M\) and \(mI\), with off-diagonal blocks \(-J\), where \(L_M\) is the Laplacian of the added matching on \(A\). The constant, zero-sum matched-pair-symmetric, matched-pair-antisymmetric, and right-zero-sum spaces diagonalize the relevant operator. In particular, a pair-antisymmetric vector has eigenvalue \(n+2\), while every other left zero-sum vector constant on each matched pair has eigenvalue \(n\).

There are exactly three edge types when unmatched vertices are present: a cross edge from an unmatched \(A\)-vertex, a cross edge from a matched \(A\)-vertex, and an inserted matching edge. At perfect saturation the first type is absent. We evaluate their *entire* electrical-current columns.

**Unmatched cross edge.** Let \(a\in A\) be unmatched and \(w\in B\). Set \(c_A=1/[m(m+n)]\) and \(c_B=-1/[n(m+n)]\). For \(L\phi=\mathbf1_a-\mathbf1_w\), take
\[
\phi_a=c_A+\frac{1-1/m}{n},\quad
\phi_{x}=c_A-\frac1{mn}\ (x\in A\setminus\{a\}),\quad
\phi_w=c_B-\frac{1-1/n}{m},\quad
\phi_y=c_B+\frac1{mn}\ (y\in B\setminus\{w\}).
\]
Every inserted matching edge carries zero current. The four cross-edge current magnitudes, for \(a w\), \(a(B\setminus w)\), \((A\setminus a)w\), and \((A\setminus a)(B\setminus w)\), respectively, are
\[
\frac{m+n-1}{mn},\quad\frac{m-1}{mn},\quad
\frac{n-1}{mn},\quad\frac1{mn}.
\]
Summing with multiplicities \(1,n-1,m-1,(m-1)(n-1)\) gives \(q_0\). Subtracting twice the diagonal current from \(1+q_0\) gives \(p_0\).

**Matched cross edge.** Let \(a,b\in A\) be a matched pair, let \(w\in B\), and put \(c_A,c_B\) as above. For the source \(\mathbf1_a-\mathbf1_w\), set
\[
\begin{aligned}
\phi_a&=c_A+\frac{1/2-1/m}{n}+\frac1{2(n+2)},&
\phi_b&=c_A+\frac{1/2-1/m}{n}-\frac1{2(n+2)},\\
\phi_x&=c_A-\frac1{mn}\quad(x\in A\setminus\{a,b\}),&
\phi_w&=c_B-\frac{1-1/n}{m},\\
\phi_y&=c_B+\frac1{mn}\quad(y\in B\setminus\{w\}).
\end{aligned}
\]
Direct substitution into the Laplacian verifies the source equation independently of the number of other matching edges: both endpoints of each other matching edge have equal potential. With \(D_0=mn(n+2)\), the signed potential differences on edge classes \(aw\), \(a(B\setminus w)\), \(bw\), \(b(B\setminus w)\), \((A\setminus\{a,b\})w\), \((A\setminus\{a,b\})(B\setminus w)\), and \(ab\) are respectively
\[
\begin{aligned}
&\frac{mn+m+n^2+n-2}{D_0},\quad
\frac{mn+m-n-2}{D_0},\quad
\frac{m+n^2+n-2}{D_0},\quad
\frac{m-n-2}{D_0},\\
&\frac{n-1}{mn},\quad-\frac1{mn},\quad\frac1{n+2}.
\end{aligned}
\]
The corresponding multiplicities are \(1,n-1,1,n-1,m-2,(m-2)(n-1),1\). All entries in the first line except possibly the fourth are strictly positive for \(m\ge4,n\ge2\); the fourth has the sign of \(m-n-2\). Taking absolute values therefore gives the cross-edge cut-column sum \(q_0+d_Q(m,n)\). Its diagonal entry is the first displayed potential difference. Using \(1+\sum |Q_{fe}|-2Q_{ee}\) gives the cross-edge cycle-column sum \(p_0+d_P(m,n)\). Both formulas coincide across \(m=n+2\).

**Inserted matching edge.** For a source between the two matched vertices, the potential is \(+1/(n+2)\) and \(-1/(n+2)\) at those vertices and zero elsewhere. The cut- and cycle-column sums are respectively
\[
q_M=\frac{2(n+1)}{n+2},\qquad p_M=\frac{3n}{n+2}.
\]
These never maximize: when \(m\le n+2\), the paired-cross excesses over \(q_M,p_M\) are
\[
\frac{(m-2)(n-1)}{mn}>0,\qquad
\frac{(n-1)((m-4)n+4(m-2))}{mn(n+2)}>0.
\]
When \(m\ge n+2\), they are
\[
\frac{(n-1)(m(n+4)-4(n+2))}{mn(n+2)}>0,\qquad
\frac{(n-1)(m(n+6)-6(n+2))}{mn(n+2)}>0.
\]
All four expressions are positive under their indicated parameter conditions. Thus the only possible maximizing columns are the paired and, if present, unmatched cross columns. Their comparisons give the three exact rows in the theorem.

**Saturation transition.** For \(n\ge5\), both \(d_Q,d_P\) are negative on \(m\le n+2\). Above that boundary their signs are those of \(m-(2n+2-4/n)\) and \(m-(2n-2)\), respectively. On the even integers \(m\ge4\), the strict drop of the cut norm occurs precisely when \(m\le2n\), and that of the cycle norm precisely when \(m\le2n-4\). The three claimed regimes follow. The example follows by direct rational substitution. This completes the proof for all admitted parameters.

## Verification

Run `python verify.py` with Python 3 and SymPy. The checker independently constructs grounded Laplacians and solves every electrical-current column over `fractions.Fraction` for \(333\) parameter triples, testing \(17{,}298\) edge columns against the theorem. Symbolic rational-identity checks reconstruct the seven current formulas, the branch differences, and continuity at the sign-change boundary. The finite computations are not used as a substitute for the unrestricted algebraic proof above.

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost* (arXiv:2305.12582v1, made public 21 May 2023), develops the Banach-space projection framework and treats tori and Hamming graphs, but does not state this matching-saturation norm law. Ge and Dong, arXiv:1904.07766v1, compute resistance quantities for **matching deletions across** the bipartition, a different operation. Ge, *Effective resistances and spanning trees in the complete bipartite graph plus a matching* (2021), and Cheng, Chen and Yan, *A type of generalized mesh-star transformation and applications in electrical networks* (2022), concern resistance distances and spanning trees on potentially overlapping matching-augmented graphs. Their accessible abstracts do not state the absolute-current \(\ell_1\) optimization or the matching-saturation transition. Because their full texts could not be inspected, an implicit derivation from their resistance formulas remains a specific originality risk. The theorem does not claim minimum norms among nonorthogonal projections.

## Limitations

The exact classification is confined to real, unit-weight graphs obtained by adding an internal matching to one class of a biclique, with \(m\ge4,n\ge2\). No statement is made for arbitrary internal graphs, general edge weights, nonorthogonal projection minima, or intermediate \(\ell_p\) norms. Existing resistance-distance literature could implicitly encode related current formulas; independent literature and mathematical review have not been performed.

## References

1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1 (21 May 2023), https://arxiv.org/abs/2305.12582 .
2. J. Ge and F. Dong, *Spanning trees in complete bipartite graphs and resistance distance in nearly complete bipartite graphs*, arXiv:1904.07766v1 (16 April 2019), https://arxiv.org/abs/1904.07766 .
3. J. Ge, *Effective resistances and spanning trees in the complete bipartite graph plus a matching*, Discrete Applied Mathematics 305 (2021), 145–153, https://doi.org/10.1016/j.dam.2021.09.008 .
4. S. Cheng, W. Chen, W. Yan, *A type of generalized mesh-star transformation and applications in electrical networks*, Discrete Applied Mathematics 320 (2022), 259–269, https://doi.org/10.1016/j.dam.2022.06.011 .
