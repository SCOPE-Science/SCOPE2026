# Complete maximal-matching polynomial and minimum-size multiplicities of cycle prisms

## Finding

For every integer \(n\ge 3\), let \(Y_n=C_n\square K_2\) be the prism with labeled columns \(i\in\mathbb Z/n\mathbb Z\). Write
\[
 M_n(z)=\sum_{F\text{ an inclusion-maximal matching of }Y_n}z^{|F|}.
\]
Define the polynomial
\[
\begin{aligned}
 D(t,z)={}&(1+tz-t^3z^2)\\
 &\quad\cdot(1-2tz-t^3z^2+t^3z^3-t^4z^3-t^5z^4).
\end{aligned}
\]
Then the entire cardinality distribution is uniquely specified by the formal power-series identity
\[
 \boxed{\displaystyle\sum_{n\ge3}M_n(z)t^n
       =-t\frac{\partial}{\partial t}\log D(t,z)-zt-5z^2t^2.}
\]
In particular, the saturation number (minimum size of an inclusion-maximal matching) and the exact number of matchings attaining it satisfy, for all \(n\ge3\),
\[
\boxed{\displaystyle s(Y_n)=\left\lceil\frac{2n}{3}\right\rceil,\qquad
 [z^{\lceil2n/3\rceil}]M_n(z)=
 \begin{cases}
 6,&n\equiv0\pmod3,\\
 2n,&n\equiv1\pmod3,\\
 n(5n-1)/3,&n\equiv2\pmod3.
 \end{cases}}
\]
The largest possible cardinality is \(n\), realized by the complete rung matching. For example,
\[
 M_3(z)=6z^2+4z^3,\quad M_4(z)=8z^3+9z^4,\quad
 M_5(z)=40z^4+11z^5.
\]

## Assumptions and scope

All graphs are finite, simple and labeled. The prism has vertices \((i,h)\) for \(i\in\mathbb Z/n\mathbb Z\) and \(h\in\{0,1\}\); its edges are two cycle rails \((i,h)(i+1,h)\) and the \(n\) rungs \((i,0)(i,1)\). A matching is a set of pairwise vertex-disjoint edges and is *inclusion-maximal* precisely when its uncovered vertices form an independent set. The polynomial counts labeled edge subsets, not matchings modulo rotation, reflection or rail exchange. In particular, the restriction \(n\ge3\) matters: the cyclic symbolic transfer representation has different edge-identification conventions for formal orders one and two. The claims are ordinary equalities over integer polynomials/formal power series; no convergence hypothesis is needed.

## Proof

**Local transfer bijection.** Encode the chosen edges in column \(i\) by \(a_i=(r_i,p_i,q_i)\), where \(r_i=1\) selects the rung and \(p_i,q_i=1\) select the two rail edges from column \(i\) to \(i+1\). No symbol may select a rung together with a rail edge, so use exactly
\[
 \mathcal A=\{(0,0,0),(0,1,0),(0,0,1),(0,1,1),(1,0,0)\}.
\]
For three consecutive symbols \(a=(r_0,p_0,q_0)\), \(b=(r_1,p_1,q_1)\), \(c=(r_2,p_2,q_2)\), let
\[
 u=p_0+p_1+r_1,\quad v=q_0+q_1+r_1,\quad
 u'=p_1+p_2+r_2,\quad v'=q_1+q_2+r_2.
\]
These are the incident selected-edge counts at the two vertices of the middle column and the next column. Define the triple to be *admissible* if and only if
\[
 u\le1,\ v\le1,\ u+v\ge1,\quad
 (u>0\ \text{or}\ u'>0),\quad (v>0\ \text{or}\ v'>0).
\]
The first two inequalities make the selected edges a matching; the third forbids an addable rung; the last two forbid an addable top or bottom rail edge. Imposing these conditions for every cyclic column is thus **necessary and sufficient** for an inclusion-maximal matching. No additional boundary conditions are required for \(n\ge3\).

Use states \((a,b)\in\mathcal A^2\) (25 states), and a directed transition \((a,b)\to(b,c)\) precisely for an admissible triple, with weight \(z^{r_b+p_b+q_b}\). Write \(T(z)\) for the corresponding \(25\)-by-\(25\) polynomial matrix (parallel arrows, if any, add their weights). Closed walks of length \(n\) correspond bijectively to the cyclic column encodings indexed by the labeled column zero; every chosen edge is weighted exactly once. Consequently
\[
 M_n(z)=\operatorname{tr}(T(z)^n)\qquad(n\ge3).
\]
This is a bijection, not merely a statistical approximation.

**Exact finite determinant.** Direct integer-polynomial evaluation of the fully specified 25-state matrix gives
\[
 \det(I-tT(z))=D(t,z).
\]
One transparent method, implemented in the standalone verifier, computes \(s_j(z)=\operatorname{tr}(T(z)^j)\) and then uses the Newton identities
\[
 c_0(z)=1,\qquad
 j c_j(z)=-\sum_{k=1}^{j}c_{j-k}(z)s_k(z)
 \quad(1\le j\le25)
\]
for the determinant coefficients \(\det(I-tT)=\sum_{j=0}^{25}c_j(z)t^j\). Its nonzero coefficients are exactly
\[
\begin{aligned}
 D(t,z)={}&1-tz-2t^2z^2+t^3(z^3-2z^2)+t^4z^4
 -2t^5z^4\\
 &+t^6(z^4-2z^5)+t^7z^5+t^8z^6.
\end{aligned}
\]
All remaining coefficients through degree 25 vanish. This is a finite exact identity over \(\mathbb Z[z]\), reproduced by the included source code from the stated five-symbol predicate; it does not rely on sampled values of \(z\). The formal trace-determinant identity now yields
\[
 -t\,\partial_t\log D(t,z)=\sum_{n\ge1}\operatorname{tr}(T(z)^n)t^n.
\]
For the two exceptional formal short lengths the traces are \(z\) and \(5z^2\), giving the displayed enumerator for actual prisms.

**Saturation and sharp multiplicities.** Substitute \(t=s/y^2\) and \(z=y^3\); this sends each term \(t^n z^k\) to \(s^n y^{3k-2n}\). The determinant transforms to
\[
\begin{aligned}
 E(s,y):=D(s/y^2,y^3)
 ={}&(1-s^3)^2-s(1-s^6)y\\
 &+(-2s^2-2s^5+s^8)y^2
 +(s^3-2s^6)y^3+s^4y^4.
\end{aligned}
\]
As \(E(s,0)=(1-s^3)^2\) is invertible in \(\mathbb Q[[s]]\), the series \(-s\partial_s\log E\) contains **no negative powers of \(y\)**. It follows that \([z^k]M_n(z)=0\) whenever \(3k<2n\). To show this bound is attained and enumerate every optimizer, extract the first three \(y\)-coefficients:
\[
\begin{aligned}
 [y^0](-s\partial_s\log E)&=\frac{6s^3}{1-s^3},\\
 [y^1](-s\partial_s\log E)&=s\frac{d}{ds}\frac{s(1+s^3)}{1-s^3},\\
 [y^2](-s\partial_s\log E)&=s\frac{d}{ds}\frac{s^2(5+6s^3-s^6)}{2(1-s^3)^2}.
\end{aligned}
\]
For \(n\equiv0,1,2\pmod3\), respectively, the lowest permitted power has \(y\)-degree zero, one, or two. The corresponding \(s^n\)-coefficients are \(6\), \(2n\), and \(n(5n-1)/3\); they are positive for the admissible orders \(n\ge3\). Hence the lower bound and the multiplicity formulas hold for **all** orders, not just tested examples.

## Verification

The accompanying standalone `verify_prism_maximal_matchings.py` uses only the Python standard library. Running `python3 verify_prism_maximal_matchings.py` on the supplied file reconstructs all 25 transfer states and 53 weighted arcs, calculates the exact determinant through order 25 using integer-polynomial Newton identities, and compares the entire polynomial with unrestricted independent matching enumeration for every \(3\le n\le12\). The verifier also checks the minimum coefficient formula through \(n=25\) and reports:

`VERIFY_OK 25_states 53_arcs determinant_degree_8 trace_orders_1..25 brute_orders_3..12 brute_search_nodes=5142377 minimum_coefficients_3..25`

The \(5{,}142{,}377\) figure is the number of recursive candidate-search nodes, not the number of maximal matchings. Exhaustive enumeration is a cross-check; unrestricted proof for general \(n\) is the transfer bijection, exact determinant, and formal coefficient argument above. Setting \(z=1\) reproduces the previously known ungraded prism-maximal-matching sequence OEIS A284703 and its characteristic denominator, a separate external comparison rather than a novelty assertion.

## Relationship to prior work

Došlić and Zubac (2015 online; 2016 volume), Sections 2 and 5, introduced the *maximal matching polynomial* and enumerated maximal matchings of the **open** ladder \(P_n\square K_2\), plus other graph chains. Their Proposition 5.2 is an ungraded open-ladder generating function. It does not assert the closed-cycle prism size distribution or the three-residue extremal multiplicities here. Hertz et al. (2022), Section 5.4, likewise analyze **open** ladders and their average maximal matching size, not this closed periodic family.

Crucially, the **ungraded** number of maximal matchings in the \(n\)-prism is *already published* as OEIS A284703 (Weisstein, 2017; recurrence contributed by Howroyd). In fact \(D(t,1)=(t^2-t+1)(t^3-t-1)(t^3+2t^2+t-1)\) agrees exactly with its denominator. The ungraded counting sequence and its scalar rational generating function are **not** claimed as new. The statement here refines those known totals to **every cardinality coefficient** and obtains the sharp residue-class formulas for the number of smallest saturated configurations. A scalar ungraded recurrence does not imply these refinements. A wider search for synonymous graded prism enumerations remains a priority limitation.

## Limitations

The result concerns labeled ordinary cycle prisms \(C_n\square K_2\) with \(n\ge3\), not Möbius ladders, crossed prisms, open ladders, or arbitrary generalized Petersen graphs. It counts inclusion-maximal, not only maximum, matchings. The previously recorded ungraded total is not new. No independent mathematical audit or historical priority certification has been performed. Related publications might contain an equivalent bivariate transfer calculation or minimum-layer enumeration under terms such as saturated dimers, maximal independent edge sets, or edge domination polynomials.

## References

1. T. Došlić and I. Zubac, *Counting maximal matchings in linear polymers*, Ars Mathematica Contemporanea 11 (2016), 255–276. Published online 2015-11-30. DOI: https://doi.org/10.26493/1855-3974.851.167. Relevant material: Sections 2, 5, Proposition 5.2.
2. E. W. Weisstein and A. Howroyd, OEIS A284703, *Number of maximal matchings in the n-prism graph*, entered 2017-04-01, recurrence and generating function added 2017-05-16. https://oeis.org/A284703.
3. A. Hertz, M. Bonte, A. Devillez, and H. Mélot, *The average size of maximal matchings in graphs*, arXiv:2204.10236 (first public 2022-04-21). https://arxiv.org/abs/2204.10236. Relevant material: Section 5.4.
