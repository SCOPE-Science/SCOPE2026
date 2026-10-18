# Support-refined Jordan census for finite-field graph face algebras

## Finding

Let \(G=(V,E)\) be any finite simple graph with \(n=|V|\) and \(m=|E|\). For each finite field \(\mathbb F_q\) of characteristic \(p\), form the graded Artinian graph face algebra
\[
A_G=\mathbb F_q[x_v:v\in V]\big/\big(x_v^2,\ x_vx_w\ (\{v,w\}\notin E),\ x_vx_wx_z\ (v,w,z\text{ pairwise distinct})\big).
\]
The displayed generators run over all permitted distinct indices. Its basis consists of \(1\), the \(n\) vertex monomials, and the \(m\) edge monomials. Write \(\mathfrak m\) for its positive-degree ideal, and for \(u\in\mathfrak m\) write \(M_u:A_G\to A_G\) for multiplication by \(u\).

For \(S\subseteq V\), let \(h_G(S)\) be the number of vertices outside \(S\) with no neighbor inside \(S\). Let \(b_p(G[S])\) be the number of connected components of the induced graph on \(S\) **when \(p=2\)**, and the number of its **bipartite** connected components when \(p\ne2\). Isolated vertices are bipartite components. For nonempty \(S\), define
\[
r_p(S)=1+n-h_G(S)-b_p(G[S]),\qquad
s_p(S)=\begin{cases}1& p\ne2\text{ and }E(G[S])\ne\varnothing,\\0&\text{otherwise.}\end{cases}
\]
For \(u=\sum_v a_vx_v+\sum_e c_ex_e\), put \(S(u)=\{v:a_v\ne0\}\). The exact support-refined multiplication-rank distribution is
\[
\boxed{\begin{aligned}
\Phi_{G,q}(X,Y,Z)&=\sum_{u\in\mathfrak m}X^{\operatorname{rank}(M_u)}Y^{\operatorname{rank}(M_u^2)}Z^{|S(u)|}\\
&=1+(q^m-1)X+q^m\sum_{\varnothing\ne S\subseteq V}(q-1)^{|S|}X^{r_p(S)}Y^{s_p(S)}Z^{|S|}.
\end{aligned}}
\]
In particular, **every** radical element has nilpotent multiplication operator of index at most three. If the coefficient of \(X^rY^sZ^k\) is \(N\), there are precisely \(N\) elements with linear support size \(k\) and Jordan partition
\[
(3^s,\ 2^{r-2s},\ 1^{1+n+m-2r+s}).
\]
Thus \(\Phi_{G,q}\) determines every Jordan-type multiplicity for all \(q\), including even characteristics. The coefficient of \(Z\) is
\[
[Z]\Phi_{G,q}=q^m(q-1)\sum_{v\in V}X^{1+\deg_G(v)},
\]
so the support-refined invariant determines the graph's degree multiset.

The specialization \(Z=1\) can distinguish graphs whose face algebras have identical Hilbert functions. Over \(\mathbb F_2\), the four-vertex paw graph with edges \(\{01,02,03,12\}\) has rank-frequency vector \((1,15,16,96,128)\) at respective ranks \((0,1,2,3,4)\). The four-cycle with edges \(\{02,03,12,13\}\) has \((1,15,96,144)\) at ranks \((0,1,3,4)\). Both have Hilbert function \((1,4,4)\) and algebra dimension nine, yet their Jordan censuses differ.

## Assumptions and scope

The field is any finite field of prime-power order, including nonprime fields and characteristic two. The graph is finite, simple, undirected, and may be disconnected or contain isolated vertices; the empty graph is included. Vertex labels are used only to state the basis and examples. The object being counted is **each element** of the radical, not just linear forms with every coefficient nonzero, and not similarity classes of abstract nilpotent matrices. The polynomial records actual multiplicities among these elements.

## Proof

The algebra is concentrated in degrees zero, one, and two. Its radical satisfies \(\mathfrak m^3=0\), so \(M_u^3=0\) for all \(u\in\mathfrak m\). Let \(a=(a_v)_{v\in V}\) denote the degree-one part of \(u\). If \(a\ne0\), the image of \(1\) under \(M_u\) has a nonzero degree-one part. The other nonzero potential images arise by multiplying vertex generators, yielding the linear map \(B_a:\mathbb F_q^V\to\mathbb F_q^E\),
\[
(B_ay)_{\{i,j\}}=a_jy_i+a_iy_j.
\]
The degree-one part of \(M_u(1)\) is independent of the edge-space image \(\operatorname{im} B_a\); therefore \(\operatorname{rank}(M_u)=1+\operatorname{rank}(B_a)\).

Set \(S=\{i:a_i\ne0\}\). If \(j\notin S\) has a neighbor \(i\in S\), the edge equation \(a_iy_j=0\) forces \(y_j=0\). Exactly \(h_G(S)\) coordinates outside \(S\) remain free. For \(i\in S\), write \(y_i=a_it_i\). Every induced edge \(\{i,j\}\in E(G[S])\) imposes \(t_i+t_j=0\). Along a connected bipartite component these equations leave one scalar free. Along a component containing an odd cycle they leave one scalar free in characteristic two but force zero in odd characteristic, since transport around the cycle yields \(2t_i=0\). These are all constraints and prove
\[
\dim\ker B_a=h_G(S)+b_p(G[S]),\quad
\operatorname{rank}(B_a)=n-h_G(S)-b_p(G[S]).
\]
The formula for \(r_p(S)\) follows.

Because the edge monomials are linearly independent,
\[
u^2=2\sum_{\{i,j\}\in E(G[S])}a_i a_j x_ix_j
\]
is nonzero precisely when \(p\ne2\) and an edge has both endpoints in \(S\). Multiplication by \(u^2\) kills the radical and sends \(1\) to \(u^2\). Hence \(\operatorname{rank}(M_u^2)=s_p(S)\). This also shows \(0\le2s_p(S)\le r_p(S)\), as required for the Jordan multiplicities. The Jordan formula is the standard decomposition for an endomorphism with cube zero: the counts of three-blocks and blocks of size at least two are respectively \(s\) and \(r-s\).

For each fixed nonempty support \(S\), there are \((q-1)^{|S|}\) choices for the nonzero degree-one coefficients and independently \(q^m\) choices of edge coefficients. Neither rank depends on the latter coefficients. When \(S=\varnothing\), the zero radical element has rank zero, while the remaining \(q^m-1\) pure-degree-two elements have multiplication rank one and square rank zero. Summing produces the polynomial. For a singleton \(S=\{v\}\), there are no induced edges, \(b_p(G[S])=1\), and \(h_G(S)=n-1-\deg_G(v)\); the coefficient-of-\(Z\) identity follows. The displayed paw and four-cycle distributions follow by evaluating the finite subset sum.

## Verification

The accompanying standalone file `verify_graph_face_jordan.py` directly constructs the multiplication matrices from the algebra's monomial basis and performs finite-field row reductions on both \(M_u\) and \(M_u^2\). It separately evaluates the subset-sum formula, including its support-size variable. Exhaustive checks covered 99 complete graph-field configurations, including every labeled graph with at most four vertices over \(\mathbb F_2\), all graphs with at most three vertices over \(\mathbb F_3\) and \(\mathbb F_4\), and the paw/four-cycle examples over \(\mathbb F_3\). A further 128 support-formula configurations covered all four-vertex labeled graphs over fields of orders three and five. The checker uses no third-party packages and explicitly constructs the field with four elements. Run `python3 verify_graph_face_jordan.py` to reproduce the checks. Finite computations corroborate, but do not establish, the all-graph proof.

## Relationship to prior work

Dao and Nair study the same Artinian square-zero-variable face rings and, via the unsigned incidence matrix, establish an appropriate full-support degree-one multiplication rank in characteristic zero for weak Lefschetz questions. That incidence mechanism is **prior work**, not a new lemma here. The present result instead describes the full elementwise and support-refined finite-field distribution of \(\operatorname{rank}(M_u)\) jointly with \(\operatorname{rank}(M_u^2)\), tracks characteristic two and odd-cycle effects, and counts all quadratic perturbations. Nguyen and Tran analyze weak Lefschetz properties for paths and cycles, not this all-graph all-element rank polynomial. Altafi, Iarrobino, and Macias Marques provide the Jordan-type framework and surveys of related Lefschetz questions, without this census. Migliore, Nagel, and Schenck study weak Lefschetz properties in quotients by quadratic monomials, not the particular complete support-refined Jordan distribution. No claim of novelty is made for the underlying incidence-matrix lemma or for standard Jordan block identities.

## Limitations

The theorem is restricted to graph face algebras truncated after degree two. It does not determine the analogous census for higher-dimensional simplicial complexes, arbitrary monomial ideals, or arbitrary nilpotent matrices. The subset-sum formula is finite and exact but can require exponentially many subsets for general graphs; no polynomial-time algorithm is claimed. The literature comparison does not establish historical uniqueness: an equivalent enumeration may occur in older incidence, modular representation, or finite-algebra literature under different terminology. Independent mathematical audit has not been performed.

## References

1. H. Dao and R. Nair, *On the Lefschetz Property for Quotients by Monomial Ideals Containing Squares of Variables*, arXiv:2112.09434v1 (17 December 2021). Especially the incidence-matrix and bipartite-component rank discussion.
2. H. D. Nguyen and Q. H. Tran, *The Weak Lefschetz Property of Artinian Algebras Associated to Paths and Cycles*, arXiv:2310.14368 (2023).
3. N. Altafi, A. Iarrobino, and P. Macias Marques, *Jordan Type of an Artinian Algebra, a Survey*, arXiv:2307.00957 (2023).
4. J. Migliore, U. Nagel, and H. Schenck, *The Weak Lefschetz Property for Quotients by Quadratic Monomials*, Mathematica Scandinavica 126 (2020), DOI:10.7146/math.scand.a-116681.
