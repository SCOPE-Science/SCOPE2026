# Exact edge-open-packing enumeration and optimal rigidity of ladder graphs

## Finding

Let \(L_n=P_2\square P_n\) be the ladder with \(n\ge1\) rungs. An **edge-open-packing** is a set of edges containing no pair for which a third, different graph edge joins an endpoint of one to an endpoint of the other. Let \(E_n(z)=\sum_B z^{|B|}\), summed over all such sets (including the empty set). Then the complete size-enumerator has the following rational ordinary generating function:

\[
\sum_{n\ge1} E_n(z)t^n=\frac{tN(t,z)}{D(t,z)},
\]
\[
\begin{aligned}
N(t,z)={}&1+z+t(3z+4z^2)+t^2(z+5z^2+2z^3)\\
&+t^3z^4+t^4(z^4-z^3),\\
D(t,z)={}&1-t-2t^2z-t^3(z+5z^2+z^3)\\
&-t^4z^3-t^5(z^4-z^3).
\end{aligned}
\]

In particular, every ladder with \(n\ge1\) has edge-open-packing number \(\rho_e^o(L_n)=n\). The number \(M_n=[z^n]E_n(z)\) of maximum packings is

\[
M_n=\begin{cases}1,&n=1,\\4,&n\ge2\text{ and }n\equiv2\pmod3,\\2,&n\ge2\text{ and }n\not\equiv2\pmod3.\end{cases}
\]

The proof below also classifies the maximum sets by alternating local star patterns. On specializing to \(z=1\), the total number \(a_n=E_n(1)\) satisfies \(a_n=a_{n-1}+2a_{n-2}+7a_{n-3}+a_{n-4}\) for every \(n\ge5\), with initial values \(a_1,a_2,a_3,a_4=(2,9,21,54)\).

## Assumptions and scope

All graphs are finite, simple, and undirected. Name the vertices of the two rows \(u_i,v_i\), for \(1\le i\le n\). Write \(r_i=u_iv_i\) for a rung and \(p_i=u_iu_{i+1}\), \(q_i=v_iv_{i+1}\) for the upper and lower horizontal edges, respectively, for \(1\le i<n\). The local state in column \(i\) is a mask \(s_i\) with bit \(1\) representing \(r_i\), bit \(2\) representing \(p_i\), and bit \(4\) representing \(q_i\). In the last column, only \(r_n\) exists, so \(s_n\in\{0,1\}\). Define \(w(s)\) to be the number of set bits of \(s\). Here \(P_1\) has one vertex and \(L_1=K_2\).

## Proof

**Local exclusion criterion.** The only allowed masks in any nonfinal column are \(S=\{0,1,2,3,4,5\}\): upper and lower horizontal edges in the same column conflict. All remaining conflicting pairs of edges lie in columns of offset one or two, with the following exhaustive lists, where the first item in each ordered pair occurs in the earlier column:

\[
\begin{array}{c|l}
\text{offset }1&(r,r),\ (r,p),\ (r,q),\ (p,q),\ (q,p)\\
\text{offset }2&(p,r),\ (p,p),\ (q,r),\ (q,q).
\end{array}
\]

There are no conflicts at greater offsets. Indeed, such a conflict requires a third edge joining endpoints of two chosen edges; examining the three kinds of ladder edge and their endpoints gives exactly the listed pairs. Conversely each listed pair has the requisite third ladder edge. Thus a sequence \(s_1,\ldots,s_n\) encodes an edge-open-packing if and only if every consecutive pair passes the offset-one test and every pair two positions apart passes the offset-two test. This is a bijection, not an approximation.

**Exact generating function.** A transfer state is an allowed ordered pair \((a,b)\) of consecutive column masks, including the initial state \((0,0)\); there are exactly 17 such states. For \(a,b\in S\), let \(C_d(a,b)\) mean that no forbidden offset-\(d\) pair has both of its bits selected. Let \(F_{a,b}\) be the formal generating series for all nonempty possible continuations after two previous masks \(a,b\). Then

\[
F_{a,b}=t\sum_{c\in\{0,1\}}[C_1(b,c)C_2(a,c)]z^{w(c)}
+t\sum_{c\in S}[C_1(b,c)C_2(a,c)]z^{w(c)}F_{b,c}.
\]

In these indicator brackets, \([P]=1\) when the proposition \(P\) holds, otherwise zero. The first term stops with the final rung column, and the second term appends an interior column, so the recurrence counts each ladder packing exactly once. Its unique formal-power-series solution exists because every right-hand occurrence of \(F\) is multiplied by \(t\). The full exact 17-state rational-function certificate in `rational_certificate.json` supplies a common denominator \(D\) and one polynomial numerator for each state. Direct polynomial multiplication verifies all 17 identities after clearing \(D\). The initial numerator is \(tN(t,z)\), proving the displayed rational function. The independent verification program checks these *symbolic polynomial identities*, not merely a finite series prefix.

**Maximum size.** Put \(h(a,b)=w(b)-1\) when \(b\ne0\). For \(b=0\), put \(h(a,0)=0\) if \(a\in\{0,3,5\}\), and \(h(a,0)=-1\) otherwise. Every permitted transition \((a,b)\to(b,c)\) satisfies

\[
w(c)-1\le h(b,c)-h(a,b).
\]

To check this without relying on a search: when \(c\ne0\), the new potential equals \(w(c)-1\). If \(b\in\{3,5\}\), the rung bit of \(b\) forces \(c=0\), so otherwise \(h(a,b)\le0\). If \(c=0\), verify separately \(b=0\), \(b\in\{1,2,4\}\), and \(b\in\{3,5\}\); the claimed inequality is immediate from the definition. Telescoping from \((0,0)\), whose potential is zero, through the final state, whose last mask belongs to \(\{0,1\}\) and potential is at most zero, gives \(\sum_i w(s_i)\le n\).

**Sharpness, rigidity and multiplicity.** Equality requires every potential inequality to be tight and the final potential to be zero. The tight-transition conditions follow from the previous case check: a nonzero next mask is tight only from potential zero, while a zero next mask is tight only after a nonzero previous mask. Remove tight transitions from which no valid final state of potential zero is reachable. The remaining strings are precisely the following alternating patterns. Let \(T=(2,3,0)\) and \(B=(4,5,0)\), representing three-edge stars centered in the top and bottom rows. Consecutive complete triples must alternate \(T,B,T,B,\ldots\) or \(B,T,B,T,\ldots\). The permitted boundary pieces are \((2,1)\), \((4,1)\) at the right, or \((3,0)\), \((5,0)\) at the left, with the row alternating at each junction:

* For \(n=3k\), \(k\ge1\): exactly \(k\) alternating complete triples, in either initial row; two choices.
* For \(n=3k+1\), \(k\ge1\): one left boundary piece, \(k-1\) alternating complete triples, and the forced opposite-row right boundary piece; two choices. For \(n=1\), the unique maximum is the rung.
* For \(n=3k+2\), \(k\ge0\): either \(k\) alternating complete triples followed by a right boundary piece, or a left boundary piece followed by \(k\) alternating complete triples; each family has two row choices and the families are disjoint.

This can also be read directly from the 17-state transition rule; all other equality branches lead to a terminal potential of \(-1\) or a dead end. Every displayed string passes the full offset-one and offset-two tests, so all are genuine packings with \(n\) edges. This proves both the sharp bound and the exact \(1,2,4\) maximum-set counts. Specializing the rational generating function at \(z=1\) yields denominator \(1-t-2t^2-7t^3-t^4\), proving the total-count recurrence.

## Verification

Run `python3 verify.py` in the directory containing `rational_certificate.json`. The verifier uses Python's standard library only. It checks all 17 exact polynomial identities with integer coefficients, all 17 potential-state transitions, exhaustive edge-subset feasibility for ladder orders \(1\) through \(6\) (74,898 subsets), coefficients and maximum counts through order 200, and the total-count recurrence through order 39. Recorded output is in `verification_output.txt`; the printed totals for the first six orders are \((2,9,21,54,161,425)\). Finite checks support but do not replace the formal generating-function certificate and the potential argument.

## Relationship to prior work

Chelladurai, Kalimuthu and Soundararajan (2022) introduced edge-open-packing sets and computed scalar maxima for paths, cycles, complete multipartite graphs, wheels and the Petersen graph. Cardoso and collaborators' injective-edge-coloring framework is equivalent to partitioning all edges into open packings; the 2023 product-graph study records the known injective edge chromatic index \(\chi_i'(L_n)=3\) for \(n\ge3\). This implies that at least one color class has at least \(n\) edges but does **not** imply that no larger packing exists, much less count the optimal packings or their entire polynomial. Brešar and Samadi (2024) give complexity results and a tree algorithm, not the ladder enumeration. Recent broader-class maximum-packing algorithms do not state the exact ladder polynomial or the optimal-set multiplicity. The present contribution is the rational all-cardinality enumerator and the rigid, residue-dependent classification of all maxima.

## Limitations

The classification is for ordinary two-row *open* ladders with free path ends, not cylindrical ladders, Möbius ladders, wider rectangular grids, induced matchings or other packing conventions. Exact integer-arithmetic complexity does not imply a bit-complexity bound independent of coefficient size. Complete worldwide priority cannot be proved from literature searches; in particular an unindexed equivalent enumeration could exist. The review presented with this finding is same-model; independent scientific audit has not been performed.

## References

1. G. Chelladurai, K. Kalimuthu and S. Soundararajan, “Edge open packing sets in graphs,” *RAIRO Operations Research* 56 (2022), 3765–3776, DOI: 10.1051/ro/2022171. Full publicly accessible article text: https://www.researchgate.net/publication/364182825_Edge_open_packing_sets_in_graphs.
2. B. Brešar and B. Samadi, “Edge open packing: complexity, algorithmic aspects, and bounds,” arXiv:2403.00750, first posted 2024-03-01, https://arxiv.org/abs/2403.00750.
3. C. K. Bhanupriya, C. Dominic and M. S. Sunitha, “Injective edge coloring of product graphs and some complexity results,” *Filomat* 37 (2023), 3959–3979, DOI: 10.2298/FIL2312959C, https://www.researchgate.net/publication/369452495_Injective_edge_coloring_of_product_graphs_and_some_complexity_results.
4. G. K. Das and K. Santra, “Maximum Edge Open Packing on AT-Free, Chordal, and Convex Bipartite Graphs,” arXiv:2610.02275, https://arxiv.org/abs/2610.02275.
