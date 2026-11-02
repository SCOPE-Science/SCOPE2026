# Exact two-packing profiles and unique-response Roman weights on circular ladders

## Finding
For every integer \(n\ge3\), let \(Y_n=C_n\square K_2\) be the circular ladder, with vertices \((i,a)\), where \(i\in\mathbb Z/n\mathbb Z\) and \(a\in\{0,1\}\). A *two-packing* is a vertex set whose distinct elements have graph distance at least three. Put
\[
P_n(u)=\sum_{S\text{ a two-packing of }Y_n}u^{|S|}
      =\sum_{k=0}^{\lfloor n/2\rfloor}a_{n,k}u^k.
\]
Then the entire all-cardinality census is the explicit rational coefficient identity
\[
\boxed{P_n(u)=[x^n]\frac{x+6ux^3+4u^2x^4+5u^2x^5}{1-x-2ux^3-u^2x^4-u^2x^5}.}
\]
Equivalently, for \(1\le k\le\lfloor n/2\rfloor\) and \(t=n-2k\),
\[
\boxed{a_{n,k}=\begin{cases}
\displaystyle\frac nk\sum_{r=1}^{\min(k,t)}2^r\binom kr\binom{t-1}{r-1},&t\ge1,\\[4pt]
4,&t=0\text{ and }k\text{ even},\\
0,&t=0\text{ and }k\text{ odd},
\end{cases}\qquad a_{n,0}=1.}
\]
In particular the polynomial recurrence, with the coefficient-polynomial initial conditions listed below, is
\[
P_n=P_{n-1}+2uP_{n-3}+u^2P_{n-4}+u^2P_{n-5}\quad(n\ge8).
\]
The initial polynomials for \(n=3,4,5,6,7\), respectively, are
\[
1+6u,\quad 1+8u+4u^2,\quad 1+10u+10u^2,\quad
1+12u+24u^2,\quad 1+14u+42u^2+14u^3.
\]
The two-packing number and exact number \(m_n\) of maximum two-packings have three residue regimes:
\[
\boxed{(\rho_2(Y_n),m_n)=
\begin{cases}
((n-1)/2,\,2n),&n\text{ odd},\\
(n/2,\,4),&n\equiv0\pmod4,\\
(n/2-1,\,n(n-2)),&n\equiv2\pmod4.
\end{cases}}
\]
Furthermore, write \(U_n(z)\) for the polynomial counting all unique-response Roman dominating functions of \(Y_n\) by total weight. Then
\[
\boxed{U_n(z)=\sum_{k=0}^{\lfloor n/2\rfloor}a_{n,k}z^{2n-2k},\qquad
u_R(Y_n)=\begin{cases}n+1,&n\text{ odd},\\n,&n\equiv0\pmod4,\\n+2,&n\equiv2\pmod4.\end{cases}}
\]
The number of minimum-weight unique-response Roman functions equals \(m_n\).

## Assumptions and scope
All graphs are finite, simple, and undirected, and cycle indices are labeled, not taken modulo graph automorphisms. The order \(n\ge3\) includes the triangular-prism boundary. A unique-response Roman dominating function (URRDF) is \(f:V(Y_n)\to\{0,1,2\}\) such that every zero-labeled vertex has exactly one neighbor labeled two and every positively labeled vertex has no neighbor labeled two. Its weight is \(\sum_v f(v)\); \(u_R\) denotes the minimum weight here. The known general bijection between two-packings and URRDFs is *prior work*, not a new general theorem.

## Proof
**Local packing characterization.** Since each rung is an edge, no two packing vertices occupy a rung. Call an empty rung \(0\), a rung with its first vertex selected \(A\), and one with its second vertex selected \(B\). For selected \((i,a)\) and \((j,b)\), the graph distance is \(d_{C_n}(i,j)+\mathbf1_{a\ne b}\). Hence the resulting cyclic word over \(\{0,A,B\}\) is valid if and only if adjacent positions are never both occupied and positions at cyclic separation two are never occupied with the same layer letter. Both conditions are needed, including for \(n=3,4\).

**Transfer matrix and rational enumerator.** Valid consecutive two-letter states, in order, are \(00,0A,0B,A0,B0\). Appending a nonzero letter gets weight \(u\); appending zero gets weight \(1\). Checking the preceding paragraph gives the exact matrix
\[
M(u)=\begin{pmatrix}
1&u&u&0&0\\
0&0&0&1&0\\
0&0&0&0&1\\
1&0&u&0&0\\
1&u&0&0&0
\end{pmatrix}.
\]
For every \(n\ge3\), each indexed valid cyclic word corresponds bijectively to a length-\(n\) closed walk on these states, so \(P_n(u)=\operatorname{tr}(M(u)^n)\). Direct expansion (or splitting the state space by interchange of \(A\) and \(B\)) gives
\[
\det(I-xM(u))=(1+ux^2)(1-x-ux^2-ux^3)
=1-x-2ux^3-u^2x^4-u^2x^5.
\]
The formal trace-determinant identity \(\sum_{n\ge1}\operatorname{tr}(M^n)x^n=-x\partial_x\log\det(I-xM)\) yields the rational numerator and denominator stated above. Cayley–Hamilton gives the displayed polynomial recurrence, valid with physical-cycle initial terms from \(n=8\) onward.

**Direct coefficient formula.** For \(k\ge1\), choose the cyclically ordered occupied rung positions; their \(k\) forward gaps \(d_i\) sum to \(n\) and satisfy \(d_i\ge2\). If \(d_i=2\), the two endpoint layer letters must differ; if \(d_i\ge3\), they can be equal or different. Put \(t=n-2k\). If \(t\ge1\), choose \(r\ge1\) gaps exceeding two. There are \(\binom kr\binom{t-1}{r-1}\) choices of their positions and positive excesses. The short-gap constraints form \(r\) paths (rather than a closed cycle), so exactly \(2^r\) layer assignments are valid. Choosing a distinguished selected rung gives \(n\) placements, while each actual packing has \(k\) choices for that distinguished rung. Thus multiply by \(n/k\). When \(t=0\), all gaps equal two, so the colors alternate around a cycle: there are two choices if \(k\) is even and none otherwise. Their \(n/k=2\) placements give four packings. The empty packing is unique.

**Sharp extrema.** The gap inequality gives \(k\le\lfloor n/2\rfloor\). If \(n\) is odd, equality uses exactly one gap of three and the remaining gaps of two. Those valid configurations exist and number \(2n\). If \(4\mid n\), equality uses all gaps two, with two possible alternating layer assignments and two rung parities: exactly four packings. If \(n\equiv2\pmod4\), equality would require an odd cyclic alternation and is impossible. The size \(k=n/2-1\) is attainable. It has total excess two: either one gap has excess two or two gaps have excess one. Substitution into the coefficient formula yields \(n(n-2)\) maximum packings. This also covers \(n=6\).

**Roman-weight translation.** As established in the cited general literature, a URRDF is uniquely specified by its two-labeled vertices, which form a two-packing \(S\); precisely the three neighbors of each vertex in \(S\) receive zero, and every other vertex not in \(S\) receives one. Since \(Y_n\) is cubic and closed neighborhoods of two-packing vertices are disjoint, if \(|S|=k\) then there are \(k\) twos, \(3k\) zeros and \(2n-4k\) ones. The weight is \(2n-2k\), proving the bivariate-to-weight translation and the three-case exact minimum formula.

## Verification
The standalone \(\texttt{verify.py}\) bundled with this result performs independent all-subset graph-distance enumeration of every two-packing for \(3\le n\le12\), and direct all-ternary-labeling tests against the original URRDF constraints for \(3\le n\le6\). It independently computes \(\det(I-xM)\) over the integer bivariate polynomial ring by the 120-term Leibniz formula, and checks the transfer-matrix census, binomial formula, recurrence through \(n=60\), and exact extremal predictions through \(n=100\). On the reviewed artifact it prints \(\texttt{VERIFY_OK}\). These finite tests are corroboration; the proof above establishes the results for every integer \(n\ge3\).

## Relationship to prior work
Fernau and Mann (2023, arXiv:2309.07018v1, Section 3.3 and Section 4) explicitly give the general bijection between two-packings and unique-response Roman dominating functions and an algorithm to enumerate the latter. This known bijection is used without novelty claim. Brešar, Klavžar, and Rall (2023, arXiv:2309.04963v1, Sections 1–3) establish a result relating *open* packing of bipartite prisms to two-packing of the base graph and bounds for hypercubes; their statements do not supply an all-cardinality two-packing polynomial for circular ladders. The currently checked literature does not establish this five-state determinant, explicit coefficient formula, or exact residue-dependent counts of optimum configurations. The distinction between open packing and two-packing is substantive; their sets satisfy different neighborhood-disjointness requirements.

## Limitations
No publication-priority claim is made against unindexed or inaccessible sources. The exact formulas apply to the ordinary circular ladders \(C_n\square K_2\) only, not arbitrary prisms, Möbius ladders, or other Roman domination variants. The transfer-matrix technique is standard; the claimed contribution is its evaluated closed formula and extremal census for this graph family. The general packing–URRDF bijection and routine translation of packing size into Roman weight are not new. An independent mathematical audit has not been performed.

## References
1. H. Fernau and K. Mann, *Perfect Roman Domination and Unique Response Roman Domination*, arXiv:2309.07018v1, publicly available 2023-09-13, https://arxiv.org/abs/2309.07018 . The relevant paper portions are Sections 1.2, 3.3, and 4.
2. B. Brešar, S. Klavžar, and D. F. Rall, *Packings in bipartite prisms and hypercubes*, arXiv:2309.04963v1, publicly available 2023-09-10, https://arxiv.org/abs/2309.04963 . The relevant material is the definitions and Sections 1–3.
3. *Exact values for three domination-like problems in circular and infinite grid graphs of small height*, arXiv:1708.00758v1, https://arxiv.org/abs/1708.00758 . A related, but inequivalent, cyclic local-state enumeration framework for identifying and locating codes.
