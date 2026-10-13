# Edge-open-packing polynomial and extremal multiplicities of sunlet graphs

## Finding
For every integer \(n\ge3\), let \(S_n\) be the sunlet graph obtained by attaching one pendant vertex \(u_i\) to every vertex \(v_i\) of the cycle \(C_n\), with indices in \(\mathbb Z/n\mathbb Z\). Write \(p_i=v_iu_i\) and \(c_i=v_iv_{i+1}\). Two **distinct** graph edges conflict if a **third** graph edge, distinct from both, joins an endpoint of one to an endpoint of the other. An edge-open packing is a set of pairwise nonconflicting edges. By convention, the empty set is included in the counting polynomial
\[
P_n(x)=\sum_{F\subseteq E(S_n)\atop F\text{ edge-open packing}}x^{|F|}.
\]

**Theorem.** In the state order \((0,0),(1,0),(0,1),(1,1)\), put
\[
W(x)=\begin{pmatrix}
1&x&x&x^2\\
1&0&0&0\\
0&1+x&0&x+x^2\\
0&1&0&0
\end{pmatrix}.
\]
For every \(n\ge3\), the exact enumerator is \(P_n(x)=\operatorname{tr}(W(x)^n)\). Equivalently, define **formal auxiliary polynomials**, which are not graph enumerators for \(n<3\), by
\[
P_0(x)=4,\quad P_1(x)=1,\quad P_2(x)=1+2x,\quad P_3(x)=1+6x+6x^2.
\]
For every \(n\ge4\),
\[
\boxed{P_n=P_{n-1}+xP_{n-2}+(x+2x^2)P_{n-3}+(x^2+x^3)P_{n-4}.}
\]
The corresponding rational generating function for the positive-index trace polynomials (only indices \(n\ge3\) represent sunlets) is
\[
\sum_{n\ge1}P_n(x)t^n=
\frac{t+2xt^2+3(x+2x^2)t^3+4(x^2+x^3)t^4}
{1-t-xt^2-(x+2x^2)t^3-(x^2+x^3)t^4}.
\]
In particular, every \(S_n\) has edge-open-packing number
\[
\rho_e^o(S_n)=\left\lfloor\frac{3n}{4}\right\rfloor.
\]
The number \(L_n\) of **maximum** edge-open packings is given, for \(q\ge0\) wherever \(n=4q+r\ge3\), by
\[
\boxed{
\begin{array}{c|c}
r&L_{4q+r}\\ \hline
0&4\ (q\ge1)\\
1&(4q+1)(4q^2+2q+3)/3\ (q\ge1)\\
2&2(2q+1)^2\ (q\ge1)\\
3&8q+6\ (q\ge0).
\end{array}}
\]

## Assumptions and scope
Graphs are finite, undirected, loopless and simple. The underlying cycle has at least three vertices. Edge-open packing uses the distinct-third-edge definition above, so adjacent selected edges need **not** conflict. The polynomial counts edge subsets, not edge colorings; its coefficient of \(x^k\) counts packings of cardinality \(k\). The empty set contributes the constant one. The order-zero, order-one and order-two polynomials in the recurrence are only algebraic initial conditions.

## Proof
**Local conflict classification.** At site \(i\) encode the chosen edges by a mask \(m_i\in\{0,1,2,3\}\), where bit one represents \(p_i\) and bit two represents \(c_i\). Directly examining all third edges of \(S_n\), for any \(n\ge3\), gives precisely the following conflicts (interpreted cyclically and without double-counting when congruences coincide): \(p_i\) against \(p_{i+1}\) and \(c_{i+1}\); \(c_i\) against \(p_{i+2}\) and \(c_{i+2}\); together with symmetric counterparts. Indeed, a third pendant edge cannot join endpoints belonging to two distinct selected edges, whereas a third cycle edge joining consecutive cycle vertices is the only possible bridge. The two chosen edges themselves are excluded as candidate third edges. Consequently the entire packing condition is exactly
\[
(m_i\mathbin{\&}1)\ne0\ \Longrightarrow\ m_{i+1}=0,
\qquad
(m_i\mathbin{\&}2)\ne0\ \Longrightarrow\ m_{i+2}=0
\]
for every cyclic index \(i\). In particular, both edges at a site may be chosen together.

**Four-state bijection.** Immediately before processing site \(i\), let \(f_0\in\{0,1\}\) say whether the current site must be empty, and \(f_1\in\{0,1\}\) say whether the next site is already forced empty. For a cyclic mask sequence these flags are uniquely determined:
\[
f_0=[m_{i-1}\mathbin{\&}1\ne0]\ \lor\ [m_{i-2}\mathbin{\&}2\ne0],
\qquad f_1=[m_{i-1}\mathbin{\&}2\ne0].
\]
If \(f_0=1\), the only permitted mask is zero; otherwise every mask is permitted. After choosing mask \(m\), the next state is
\[
(f_1\lor[m\mathbin{\&}1\ne0],\ [m\mathbin{\&}2\ne0]),
\]
with weight \(x^{\operatorname{popcount}(m)}\). Summing weights of masks that realize each transition gives exactly the displayed matrix \(W(x)\). Every feasible cyclic sequence has exactly one cyclic state trajectory, and conversely every closed length-\(n\) trajectory yields one feasible mask sequence. Fixing the labeled site zero removes rotation ambiguity. Therefore the weighted sum is precisely \(\operatorname{tr}(W(x)^n)\) for \(n\ge3\).

**Recurrence.** Exact cofactor expansion of the explicit four-by-four matrix gives
\[
\det(\lambda I-W)=\lambda^4-\lambda^3-x\lambda^2-(x+2x^2)\lambda-(x^2+x^3),
\]
and hence
\[
\det(I-tW)=1-t-xt^2-(x+2x^2)t^3-(x^2+x^3)t^4.
\]
For every positive integer \(n\), the formal identity \(\operatorname{tr}(W^n)=[t^n](-t\,\partial_t\log\det(I-tW))\) proves the displayed rational generating function. Newton identities supply the formal initial trace terms, and taking the order-zero Newton term as four yields exactly the listed \(P_0,P_1,P_2,P_3\). The quartic characteristic identity then yields the recurrence for every \(n\ge4\); the order-four case can also be checked directly from the displayed initial polynomials. Thus the recurrence is a theorem for all genuine \(n\ge3\), not an extrapolation from small cases.

**Degree and leading coefficient.** All coefficients in the recurrence are nonnegative. Starting with the stated initial terms, induction by residues modulo four gives \(\deg P_n=\lfloor 3n/4\rfloor\) for all \(n\ge3\). To count maximum sets, compare only terms reaching that degree. If \(L_n=[x^{\lfloor3n/4\rfloor}]P_n\), the residue-wise leading-coefficient recurrences are
\[
\begin{aligned}
L_{4q}&=L_{4q-4} &&(q\ge2),\\
L_{4q+1}&=L_{4q-3}+16q^2-8q+6 &&(q\ge1),\\
L_{4q+2}&=2(2q+1)^2 &&(q\ge1),\\
L_{4q+3}&=8q+6 &&(q\ge1).
\end{aligned}
\]
Here the two explicit expressions in the last two lines result by substitution of the previous residue classes into the six summands of the polynomial recurrence. The base cases are \(L_3=6\), \(L_4=4\), \(L_5=15\), \(L_6=18\). Summing the quadratic increments in the second line yields \(L_{4q+1}=(4q+1)(4q^2+2q+3)/3\). This proves every extremal multiplicity in the table. \(\square\)

## Verification
The standalone file `verify_eop.py` constructs the edge-conflict relation **directly from all unordered pairs of edges and distinct possible third edges**, not from the two local mask implications. It enumerates all \(2^{2n}\) candidate edge subsets for \(3\le n\le9\): exactly 349,504 candidates. Their full coefficient vectors agree with the recurrence. It also separately constructs the displayed four-state matrix and verifies its exact characteristic polynomial and trace coefficients symbolically with SymPy; independently constructs a 16-state two-mask transfer matrix and checks its symbolic determinant identity. The degree and leading-coefficient formulas are checked through \(n=32\). Run `python verify_eop.py` with Python 3 and SymPy available; the matching recorded output is `verify_output.txt`. These finite checks support, but do not replace, the unrestricted combinatorial proof.

## Relationship to prior work
Chelladurai–Kalimuthu–Soundararajan (2022) introduced edge-open packing and determined extremal information including the ordinary **cycle** case; a cycle without leaves is not the present graph. Brešar–Samadi (first posted 1 March 2024) studied its complexity and a linear-time algorithm for its **maximum on trees**, whereas sunlets are unicyclic and the present invariant records every set size. Cardoso–Cerdeira–Cruz–Dominic developed injective edge coloring; an edge-open packing is a permissible color class, but their index and conflict-graph formulation do not give this family-specific enumerator. Pandey–Santra (2025) characterized graph classes via prescribed maximum edge-open-packing numbers; that scalar characterization does not count packings. Gayathri–Venkataraman (2026) reports scalar bounds for unicyclic graphs, but its full article was not accessible for a conclusive statement-by-statement comparison. The generic reduction of packings to independent sets of a conflict graph is acknowledged: the contribution here is the explicit four-state transfer, quartic all-size recurrence and exact extremal multiplicities for **every** sunlet.

## Limitations
The theorem concerns exactly one pendant edge per vertex of a single cycle; it does not assert an algorithm for general unicyclic graphs or general graph edge-open-packing polynomials. The count of maximum packings does not enumerate injective edge colorings. Earlier equivalent transfer descriptions may exist under independence-polynomial terminology; an inaccessible 2026 unicyclic-bounds article leaves additional scalar-overlap risk. Bibliographic completeness and independent audit are not asserted.

## References
1. G. Chelladurai, K. Kalimuthu, S. Soundararajan, *Edge open packing sets in graphs*, RAIRO Operations Research **56** (2022), 3765–3776, DOI: 10.1051/ro/2022171.
2. B. Brešar, B. Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, arXiv:2403.00750v1, first posted 2024-03-01; later Theoretical Computer Science (2024).
3. D. Cardoso, J. O. Cerdeira, J. Cruz, C. Dominic, *Injective edge chromatic index of a graph*, arXiv:1510.02626v1; Filomat (2019).
4. A. Pandey, K. Santra, *Edge open packing: further characterizations*, arXiv:2508.01935v1 (2025).
5. C. Gayathri, Y. Venkataraman, *On edge open packing sets of graphs*, South East Asian Journal of Mathematics and Mathematical Sciences **22** (2026), 25–36, DOI: 10.56827/SEAJMMS.2026.2201.2 (abstract inspected; full text unavailable).
