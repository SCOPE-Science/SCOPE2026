# Exact induced-matching polynomial and maximum-set multiplicities of cycle prisms

## Finding
For each integer \(n\ge3\), let \(P_n=C_n\square K_2\), the graph consisting of two \(n\)-cycles and corresponding rungs. An **induced matching** is an edge set whose incident vertices induce precisely those disjoint edges. Define
\[
I_n(z)=\sum_{M\,\text{an induced matching of }P_n}z^{|M|}.
\]
Then, with \(t\) a formal variable,
\[
\boxed{\sum_{n\ge3}I_n(z)t^n=-t\frac{\partial}{\partial t}\log\!\left[(1+zt^2)(1-t-2zt^2-zt^3+z^2t^4)\right]-t-(1+2z)t^2.}
\]
The logarithmic derivative is expanded as a formal power series around \(t=0\). In particular, the largest possible size is \(\lfloor n/2\rfloor\), and its exact multiplicity is
\[
\boxed{[z^{\lfloor n/2\rfloor}]I_n(z)=\begin{cases}n^2,&n\ge3\text{ odd},\\6,&n\equiv0\pmod4,\\2,&n\equiv2\pmod4.\end{cases}}
\]
The first polynomials are \(I_3(z)=1+9z\), \(I_4(z)=1+12z+6z^2\), \(I_5(z)=1+15z+25z^2\), and \(I_6(z)=1+18z+57z^2+2z^3\).

## Assumptions and scope
The underlying graphs are finite, simple, undirected cycle prisms; \(n\ge3\). Label each cycle's vertices \((i,T)\) and \((i,B)\), with \(i\in\mathbb Z/n\mathbb Z\). The three edge types starting at column \(i\) are \(R_i=\{(i,T),(i,B)\}\), \(T_i=\{(i,T),(i+1,T)\}\), and \(B_i=\{(i,B),(i+1,B)\}\). Every edge is in precisely one such column and type, including when \(n=3\). An edge set is encoded by a cyclic word \(s_0\cdots s_{n-1}\) over \(\{0,R,T,B\}\), with at most one edge type selected at a column. This restriction is necessary because the three edges starting at one column pairwise meet or have adjacent endpoints.

## Proof
**1. Complete local criterion.** Two occupied consecutive column indices cannot occur in an induced matching: each choice has a pair of incident or adjacent endpoints. If exactly one intervening column is empty, the allowable directed pairs of edge types are exactly
\[
\mathcal A=\{(R,R),(R,T),(R,B),(T,B),(B,T)\}.
\]
For example, two top edges at cyclic distance two have adjacent nearest endpoints, whereas a top and a bottom edge at that distance do not. These statements follow by inspecting the endpoints above. Conversely, if all cyclic adjacent columns are not both occupied and every distance-two ordered pair belongs to \(\mathcal A\), any two selected edges with farther starting columns have endpoints at graph distance at least two; hence the selected edges form an induced matching. For \(n=3,4\), the cyclic conditions inspect the same physical pair in both orientations when necessary, so the criterion still holds (and can be verified directly from the stated endpoint lists).

**2. Seven-state transfer.** Use states \((a,b)\) with \(a,b\in\{0,R,T,B\}\), excluding two nonzero symbols; there are seven. From \((a,b)\) to \((b,c)\) allow a transition precisely when \(b=0\) or \(c=0\), and, when both \(a,c\) are nonzero, require \((a,c)\in\mathcal A\). The transition weight is \(z\) when \(c\ne0\), and \(1\) otherwise. Write \(T(z)\) for the resulting \(7\times7\) matrix. Every cyclic word satisfying the local criterion yields exactly one closed walk of length \(n\) in this directed state graph, with weight \(z^{|M|}\). Conversely every such walk gives a unique word. Therefore
\[
I_n(z)=\operatorname{tr}(T(z)^n),\qquad n\ge3.
\]
Expanding the finite determinant (or applying ordinary integer polynomial elimination) gives the exact identity
\[
\det(1-tT(z))=(1+zt^2)(1-t-2zt^2-zt^3+z^2t^4).
\]
Because \(-t\partial_t\log\det(1-tT)=\sum_{j\ge1}\operatorname{tr}(T^j)t^j\) as formal series, the complete-polynomial formula follows after removing the auxiliary traces \(\operatorname{tr}(T)=1\) and \(\operatorname{tr}(T^2)=1+2z\). The latter are transfer traces only, not induced-matching polynomials of simple two-column prisms.

**3. Maximum size and multiplicity.** Any two occupied columns must have cyclic separation at least two. Therefore at most \(\lfloor n/2\rfloor\) columns are occupied; all-rung selections with that spacing attain the bound. For \(n=2k+1\), a selection of \(k\) columns has exactly one cyclic gap of length three and \(k-1\) gaps of length two. There are exactly \(n\) such column sets, specified by the unique length-three gap. Cutting after that gap leaves a linear chain of \(k\) chosen types. Its allowable successive pairs are exactly \(\mathcal A\): either all \(R\)'s, or a first \(T\) or \(B\) at any of the \(k\) positions followed by forced alternating \(T,B\). Thus it admits \(1+2k=n\) type assignments. The odd maximum-set count is \(n^2\).

For \(n=2k\), the \(k\) occupied columns must be one of two alternating cyclic index classes. Each class admits the all-rung type assignment. Any non-rung type forces alternating \(T,B\) all around that cyclic class, which closes if and only if \(k\) is even; then there are two such additional assignments per class. Therefore the even count is \(6\) when \(n\) is a multiple of four, and \(2\) otherwise.

## Verification
The standalone Python 3 standard-library program `verify.py` reconstructs the seven-state transition matrix, computes its bivariate determinant by the signed permutation expansion, and confirms the displayed factorization over exact integers. It reconstructs each prism graph directly from its endpoint lists and compares all \(4^n\) cyclic type words against both the local criterion and exact transfer-matrix coefficients for \(3\le n\le9\), totaling \(349{,}504\) words. It also checks maximum degrees and top coefficients for \(3\le n\le44\). Execute `python3 verify.py` in a directory containing this result and the script. The general theorem is proved by the bijections and gap classification, not by the finite tests.

## Relationship to prior work
The definition and general context of induced/strong matchings occur in Joos, Rautenbach and Sasse's 2013 study of subcubic graphs, which proves global size bounds rather than cycle-prism enumeration. Mathar's 2024 study of non-bonding dominoes gives the exact analogous polynomial for **open** two-column rectangular boards (his Table 2 and Equation (8)); those boards correspond to path ladders \(P_n\square K_2\), not closed cycle prisms \(C_n\square K_2\). For instance, the open four-column polynomial is \(1+10z+9z^2\), whereas the cyclic four-column polynomial is \(1+12z+6z^2\). Existing matching-polynomial tables for prisms count **ordinary** matchings and hence differ from induced matchings already for the triangular prism. Other work on strong edge colorings and dominating induced matchings addresses distinct invariants. The evaluated cyclic formula and its parity-sensitive exact maximum-set counts are the contribution assessed here.

## Limitations
The theorem is restricted to simple cycle prisms and induced matchings. The state-space formula is not an all-width cylinder theorem. The references inspected do not establish priority conclusively: a differently indexed polynomial for generalized Petersen graphs or cylindrical non-bonding dominoes could be equivalent. No independent audit has been performed.

## References
1. F. Joos, D. Rautenbach and T. Sasse, *Induced Matchings in Subcubic Graphs*, arXiv:1312.1110, first version 4 December 2013; Sections 1–3, particularly Theorems 1–2. https://arxiv.org/abs/1312.1110
2. R. J. Mathar, *Bivariate Generating Functions Enumerating Non-Bonding Dominoes on Rectangular Boards*, arXiv:2404.18806, 29 April 2024; Section 3, Table 2 and Equation (8). https://arxiv.org/abs/2404.18806
3. M. Chen, L. Miao and S. Zhou, *Strong Edge Coloring of Generalized Petersen Graphs*, *Mathematics* **8** (2020), 1265; Sections 1–2. https://doi.org/10.3390/math8081265
4. *Matching Polynomials of Symmetric, Semisymmetric, Double Group Graphs, Polyacenes, Wheels, Fans, and Symmetric Solids in Third and Higher Dimensions*, *Symmetry* **17** (2025), 133; section on ordinary matching polynomials of prism graphs. https://doi.org/10.3390/sym17010133
5. OEIS A102079, ordinary matching counts of prism graphs. https://oeis.org/A102079
