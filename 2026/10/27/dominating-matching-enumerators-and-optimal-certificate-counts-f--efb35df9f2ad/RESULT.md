# Dominating-matching enumerators and optimal-certificate counts for circular prisms

## Finding
Let \(P_n=C_n\square K_2\) be the labelled circular prism, \(n\ge3\). A *dominating matching* is a matching whose endpoint vertices dominate \(P_n\). Write \(d_n(s)\) for the number of such matchings comprising \(s\) edges; different matchings are counted separately even when they have the same endpoint set. Then the complete enumerator \(D_n(y)=\sum_s d_n(s)y^s\) equals \(\operatorname{tr}(T(y)^n)\) for the explicit 49-state transfer matrix in the proof. Moreover
\[
\min\{s:d_n(s)>0\}=\left\lceil\frac n3\right\rceil.
\]
The exact number \(c_n=d_n(\lceil n/3\rceil)\) of minimum dominating matchings is the following quasi-polynomial. Write \(n=3k+r\), \(0\le r\le2\). For \(r=0\), \(k\ge1\),
\[
c_n=\begin{cases}3,&k\text{ odd},\\9,&k\text{ even}.\end{cases}
\]
For \(r=2\), \(k\ge1\),
\[
c_n=n(2k+3),
\]
and for \(r=1\), \(k\ge1\),
\[
c_n=n\left(\frac{2k^3+12k^2+25k+6}{6}+2-(-1)^k\right).
\]
(The cases \(r=1,2\) begin at \(n=4,5\), respectively.) In particular, there are \(42\) minimum matchings on \(P_4\) and \(147\) on \(P_7\). Their edge sets, rather than just their endpoint vertex sets, are enumerated.

## Assumptions and scope
The graph has vertices \((i,t)\) where \(i\in\mathbb Z/n\mathbb Z\) and \(t\in\{0,1\}\). It has two cycle edges from each vertex in its own layer, and one rung to the opposite layer. The graph is cubic for all stated \(n\) and bipartite exactly when \(n\) is even. The cyclic labelling is fixed; no quotient by dihedral symmetries is taken. A matching is a set of pairwise vertex-disjoint edges; its endpoints dominate if every vertex belongs to or neighbors an endpoint. The paired-domination number is therefore twice the minimum number of edges in a dominating matching. The new enumerator counts matching certificates, not merely paired-dominating vertex sets. The minimum cardinality is already known from Gorzkowska et al. (2023, Proposition 18); its exact count of matching certificates is the new enumerative assertion.

## Proof
**Sharp minimum size.** An edge has two endpoints. Since \(P_n\) is cubic, the union of their closed neighborhoods contains at most six vertices. A dominating matching with \(s\) edges therefore dominates at most \(6s\) of the \(2n\) vertices, giving \(s\ge\lceil n/3\rceil\). Selecting rung edges at cyclicly spaced columns with gaps at most three, using precisely \(\lceil n/3\rceil\) rungs, attains the bound: each chosen rung dominates both layers in its own column and the adjacent columns. This proves the stated minimum; it is not the principal novelty claim.

**Transfer-state encoding.** Put \(X=\{0,1,2,4,6\}\). For each column \(i\), choose a symbol \(a_i\in X\): \(0\) means no edge begins there; \(1\) selects its rung; \(2\) selects the upper horizontal edge from \(i\) to \(i+1\); \(4\) selects the lower horizontal edge; \(6\) selects both horizontals. Its edge weight is the number of nonzero bits in the symbol. A cyclic word describes a matching exactly when every adjacent pair \((a,b)\) is *compatible*: neither has a repeated upper horizontal bit, neither has a repeated lower horizontal bit, and a horizontal from \(a\) cannot meet a rung in \(b\). Formally,
\[
\mathrm{comp}(a,b)\iff\neg((a\mathbin{\&}b\mathbin{\&}2)\lor(a\mathbin{\&}b\mathbin{\&}4)\lor((a\mathbin{\&}6)\land(b\mathbin{\&}1))),
\]
where \(\&\) denotes bitwise AND on the indicated integers and \(\land\) is Boolean AND. Define \(U(a,b)\) to mean \((b\mathbin{\&}1)\lor(a\mathbin{\&}2)\lor(b\mathbin{\&}2)\), and \(L(a,b)\) by replacing bit \(2\) with bit \(4\). Thus \(U(a,b)\) and \(L(a,b)\) respectively mean that the upper and lower vertices of the column represented by \(b\) are matching endpoints.

Let \(Q(a,b,c,d)\) be the conjunction
\[
[U(a,b)\lor U(b,c)\lor U(c,d)\lor L(b,c)]
\land[L(a,b)\lor L(b,c)\lor L(c,d)\lor U(b,c)].
\]
This says precisely that both layer vertices of the column represented by \(c\) are dominated. Let \(\mathcal S\) consist of triples \((a,b,c)\in X^3\) with \(\mathrm{comp}(a,b)\) and \(\mathrm{comp}(b,c)\). There are \(49\) states. Define \(T(y)\), indexed by \(\mathcal S\), by adding \(y^{\operatorname{bits}(d)}\) in position \(((a,b,c),(b,c,d))\) whenever \(\mathrm{comp}(c,d)\) and \(Q(a,b,c,d)\) both hold, where \(\operatorname{bits}(d)\) is the number of binary-one digits of \(d\). There are exactly \(147\) such labelled transitions.

A closed walk of length \(n\) in this matrix uniquely specifies the \(n\) symbols and tests every column for domination, including the wraparound columns. Conversely every dominating matching gives such a closed walk, with a unique fixed-column origin. The transfer identity follows:
\[
D_n(y)=\operatorname{tr}(T(y)^n),\quad n\ge3.
\]

**Exact minimum coefficient.** The symbolic finite certificate `verify.py` reconstructs these \(49\) states and their \(147\) transitions. Give each transition adding \(s\) edges the integer cost \(3s-1\). It computes an integer potential \(h\) satisfying nonnegative reduced costs \(3s-1+h(\text{source})-h(\text{target})\) on every transition. On closed walks, the sum of reduced costs is exactly \(3s-n\), since the potentials telescope. Let \(A_j\) be the 49-state adjacency matrix of the transitions with reduced cost \(j\) for \(j=0,1,2\), let \(z\) be a formal variable, and put \(R=(I-zA_0)^{-1}\). The following are exact rational identities, verified with integer symbolic arithmetic by the supplied checker:
\[
\det(I-zA_0)=(1-z^3)(1-z^6),
\]
\[
\operatorname{tr}(RA_1)=\frac{z(3-z^3)}{(1-z^3)^2},\qquad
\operatorname{tr}(RA_2)=\frac{1+3z^3}{1-z^6},
\]
\[
\operatorname{tr}(RA_1RA_1)=\frac{z^2(3-z^3)(2z^6-5z^3+5)}{(1-z^3)^4}.
\]
The usual formal trace-log identity
\[
-z\frac{\partial}{\partial z}\log\det(I-zA(u))=\sum_{n\ge1}\operatorname{tr}(A(u)^n)z^n
\]
with \(A(u)=\sum_{j\ge0}u^jA_j\) enumerates closed walks by length and total reduced cost. Because all reduced costs are nonnegative, only \(A_0,A_1,A_2\) can contribute to coefficients of \(u^0,u^1,u^2\). These coefficients are
\[
F_0(z)=z\frac{d}{dz}\left(-\log\det(I-zA_0)\right),
\]
\[
F_1(z)=z\frac{d}{dz}\left(z\operatorname{tr}(RA_1)\right),
\]
\[
F_2(z)=z\frac{d}{dz}\left(z\operatorname{tr}(RA_2)+\frac{z^2}{2}\operatorname{tr}(RA_1RA_1)\right).
\]
For a minimum matching of \(s=\lceil n/3\rceil\), the reduced cost \(3s-n\) is \(0,1,2\) for lengths congruent to \(0,2,1\pmod3\), respectively. The coefficient of \(z^n\) in the appropriate \(F_j\) is thus \(c_n\). Extracting these coefficients gives \(3+6\mathbf 1_{2\mid k}\), \(n(2k+3)\), and the stated cubic-in-\(k\) factor multiplied by \(n\), in the respective residue cases. This proves the formula for every \(n\ge3\), not merely for the finite test range.

## Verification
Run `python verify.py` using Python 3.10+ and SymPy 1.12+. It rebuilds the state graph, constructs an exact reduced-cost potential and the four rational-matrix identities, and checks all coefficients against independent brute-force edge-subset enumeration for \(3\le n\le9\). It further checks the minimum coefficient of the transfer enumerator through \(n=30\). Expected output begins `VERIFY_OK states=49 arcs=147` and reports 35,425 checked dominating matchings in the brute-force range. The exact symbolic identities, not the finite test cases, certify the infinite coefficient formulas.

## Relationship to prior work
Lu and Wu's 2026 paper gives sharp general upper bounds for paired domination in cubic bipartite graphs, covering the even-circumference prism subfamily. The minimum paired-domination number of every cycle prism is explicitly proved in Proposition 18 of Gorzkowska et al. (2023): \(\gamma_{pr}(C_n\square K_2)=2\lceil n/3\rceil\). The present minimum-edge formula is credited as previously known, not claimed as new. Mynhardt and Schurch (2011) study paired domination in prisms and give classes of prism-number equalities, whereas the present object is the number of *matching certificates* of each size. Gorzkowska and collaborators study prism stability under deletions and prove the minimum value, but not the enumerator of its matching certificates. Allagan (2026) enumerates minimum **ordinary dominating vertex sets** of prisms, a distinct invariant: it neither imposes matching certificates nor provides their full edge-cardinality polynomial. The present explicit transfer enumeration and optimal-certificate quasi-polynomial do not follow merely from an extremal paired-domination number or an ordinary dominating-set census.

## Limitations
The assertion is restricted to labelled circular prisms and to matchings dominating by their endpoint vertices. It does not give an enumerator of *distinct* paired-dominating vertex sets, since more than one matching can certify the same set. It does not apply to arbitrary cubic bipartite graphs, path ladders, or twisted prisms. The full text of the 2011 prism paper could not be reviewed in this investigation, leaving some historical-priority risk. Further independent proof and priority assessments have not been performed.

## References
1. C. Lu and Q. Wu, *Paired Domination in Cubic Bipartite Graphs* (2026), arXiv:2609.30152v1, first public 2026-09-24.
2. C. M. Mynhardt and M. Schurch, *Paired domination in prisms of graphs*, Discussiones Mathematicae Graph Theory 31 (2011), 5–23, DOI:10.7151/DMGT.1526.
3. A. Gorzkowska et al., *Total and paired domination stability in prisms* (2023), DOI:10.7151/DMGT.2421.
4. J. Allagan, *Exact Dominion of the Prism Graph: Enumeration by Congruence Class via Cyclic Words* (2026), DOI:10.1155/ijmm/1411005.
