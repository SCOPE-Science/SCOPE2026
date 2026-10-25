# Exact perfect-edge-domination counts and a strict cycle bound for lollipop graphs

## Finding

For integers \(c\ge3\) and \(t\ge1\), form the lollipop graph \(L_{c,t}\) by identifying one endpoint of a path of \(t\) edges with a vertex of the simple cycle \(C_c\). A *perfect edge dominating set* (PED-set) is a set \(P\subseteq E(G)\) for which every edge outside \(P\) is adjacent to exactly one edge of \(P\); edges inside \(P\) need not be independent. Let \(F_{c,t}\) denote the number of PED-sets of \(L_{c,t}\), including the entire edge set.

The complete two-parameter counting series is
\[
\sum_{c\ge3}\sum_{t\ge1}F_{c,t}X^{c-3}Y^{t-1}
=\frac{3+3Y^2+X(1+Y)+2X^2(1+Y)}{(1-X-X^3)(1-Y-Y^3)}.
\]
Equivalently, \(F_{c,t}=F_{c-1,t}+F_{c-3,t}\) for \(c\ge6\) and \(F_{c,t}=F_{c,t-1}+F_{c,t-3}\) for \(t\ge4\), with initial \(3\)-by-\(3\) table, rows \(c=3,4,5\), columns \(t=1,2,3\),
\[
(F_{c,t})=\begin{pmatrix}3&3&6\\4&5&8\\6&9&12\end{pmatrix}.
\]
For **every** such pair of integers,
\[
F_{c,t}<\#\operatorname{PED}(C_{c+t}).
\]
Thus cycles strictly beat all lollipop graphs of the same order in the PED-set enumeration, establishing this infinite connected-unicyclic subclass of Conjecture 5.1 in Grippo--Lin--Moyano--Vera (2026).

## Assumptions and scope

Graphs are finite, undirected, simple, and edge-labelled only for counting purposes. The cycle has \(c\ge3\) vertices, and the attached path introduces \(t\ge1\) further vertices, so \(|V(L_{c,t})|=c+t\). Both endpoints and the direction of the chosen cycle enumeration are immaterial to the number of PED-sets. The convention places no condition on the number of selected edges adjacent to a selected edge. The theorem concerns the specified lollipop family, not all unicyclic or all connected graphs.

## Proof

**1. Local edge states.** Give each edge a bit: \(1\) when selected and \(0\) when not. On a degree-two internal edge whose two distinct neighboring edges have bits \(u,w\), the PED condition is
\[
v=1\quad\text{or}\quad u+w=1,
\]
where \(v\) is its own bit. Order the pair states as \((0,0),(0,1),(1,0),(1,1)\). The transition matrix \(M\), with entries \(M_{(u,v),(v,w)}=1\) precisely when the displayed condition holds, is
\[
M=\begin{pmatrix}0&1&0&0\\0&0&1&1\\1&0&0&0\\0&0&1&1\end{pmatrix}.
\]
Direct matrix multiplication gives
\[
M^4=M^3+M,\qquad M^3h=M^2h+h,\qquad h=(0,1,1,1)^\mathsf T.
\]
The vector \(h\) accepts a terminal leaf edge: either its bit is selected or its unique preceding edge is selected.

**2. Tail enumeration.** Number the path edges outward from the cycle as \(f_1,\ldots,f_t\), with first bit \(p\). Suppose that the other two edges incident with its root have \(s\) selected edges, \(0\le s\le2\). Write \(H_t(s,p)\) for the number of assignments to the remaining path edges satisfying all PED constraints on the path edges. For \(t=1\),
\[
H_1(s,p)=\mathbf1\{p=1\ \mathrm{or}\ s=1\}.
\]
For \(t\ge2\), with \([Q]\) denoting the indicator of proposition \(Q\), the root constraint and the internal-edge transfers give the exact formula
\[
H_t(s,p)=\sum_{q=0}^1[p=1\ \mathrm{or}\ s+q=1]\,\bigl(M^{t-2}h\bigr)_{(p,q)}.
\]
The six values of \((s,p)\) have the following \(H_1,H_2,H_3,H_4\) tuples:
\[
\begin{array}{c|c}
(s,p)&(H_1,H_2,H_3,H_4)\\\hline
(0,0)&(0,1,2,2)\\
(0,1)&(1,2,2,3)\\
(1,0)&(1,0,1,2)\\
(1,1)&(1,2,2,3)\\
(2,0)&(0,0,0,0)\\
(2,1)&(1,2,2,3)
\end{array}
\]
These values verify \(H_4=H_3+H_1\). The identity \(M^3h=M^2h+h\) then verifies \(H_t=H_{t-1}+H_{t-3}\) for every \(t\ge5\). Hence this recurrence holds for all \(t\ge4\).

**3. Cycle enumeration with one trivalent root.** List the cycle-edge bits in cyclic order as \(e_0,\ldots,e_{c-1}\). Put \(a=e_0\), \(b=e_{c-1}\), \(x=e_1\), \(y=e_{c-2}\), and \(p=f_1\). All internal cycle-edge constraints are counted by the matrix coefficient \((M^{c-2})_{(a,x),(y,b)}\). The two root-incident cycle edges are valid exactly when
\[
A=[a=1\ \mathrm{or}\ x+b+p=1],\qquad B=[b=1\ \mathrm{or}\ y+a+p=1].
\]
Consequently, with all five variables summed over \(\{0,1\}\),
\[
F_{c,t}=\sum_{a,b,x,y,p} A B\,(M^{c-2})_{(a,x),(y,b)}H_t(a+b,p).
\]
This also covers \(c=3\): the single transition enforces that \(x=y\). The exact matrix identity \(M^4=M^3+M\) implies \(M^{c-2}=M^{c-3}+M^{c-5}\) for \(c\ge6\); hence \(F_{c,t}=F_{c-1,t}+F_{c-3,t}\). The recurrence from step 2 similarly gives \(F_{c,t}=F_{c,t-1}+F_{c,t-3}\) for \(t\ge4\). Direct evaluation of the displayed finite sum at \(c=3,4,5\) and \(t=1,2,3\) yields the nine entries in the finding. These recurrences are jointly sufficient to determine every coefficient and yield the stated rational generating series by standard formal power-series multiplication: \((1-X-X^3)(1-Y-Y^3)\) leaves precisely the numerator shown.

**4. Strict comparison.** Let \(B_n=\#\operatorname{PED}(C_n)\). Every circular binary word of length \(n\ge3\) satisfying the local rule corresponds to one PED-set of \(C_n\), so \(B_n=\operatorname{tr}(M^n)\). In particular, \(B_4,B_5,B_6,B_7,B_8=5,6,10,15,21\), and \(B_n=B_{n-1}+B_{n-3}\) for \(n\ge6\). For \(D_{c,t}=B_{c+t}-F_{c,t}\), the nine initial differences are
\[
(D_{c,t})_{c=3,4,5;\,t=1,2,3}=\begin{pmatrix}2&3&4\\2&5&7\\4&6&9\end{pmatrix}.
\]
They are positive. Both \(D_{c,t}=D_{c-1,t}+D_{c-3,t}\) for \(c\ge6\) and \(D_{c,t}=D_{c,t-1}+D_{c,t-3}\) for \(t\ge4\) hold by subtraction. First induct on \(c\) for each of the three initial tail lengths, then induct on \(t\) for every \(c\); positivity follows throughout. This proves the strict inequality for all stated parameters.

## Verification

Run `python3 verify.py` using Python 3 (standard library only). The verifier constructs the stated matrix, proves the two exact integer-matrix identities entry by entry, and compares the nine initial values with an independent direct enumeration. It exhaustively checks every labelled edge subset on lollipops satisfying \(c\ge3\), \(t\ge1\), \(c+t\le15\), and every edge subset of cycles \(C_n\) for \(3\le n\le15\). It also checks both recurrences and the inequality on the finite grid \(3\le c\le30\), \(1\le t\le30\). `verification_output.txt` is the resulting output; it is not the infinite proof.

## Relationship to prior work

Grippo, Lin, Moyano, and Vera (arXiv:2607.03894v1, July 4, 2026), define PED counting, give general linear-time algorithms on generalized series-parallel graphs, and establish \(B_n=B_{n-1}+B_{n-3}\) for cycles. Their Conjecture 5.1 proposes \(\#\operatorname{PED}(G)\le\#\operatorname{PED}(C_{|V(G)|})\) for every connected graph; their full 30-page preprint does not state the two-parameter lollipop enumeration or prove this subclass of the conjecture. A generic counting algorithm on a graph is not an all-parameter extremal comparison. The preceding paper by Grippo, Lin, and Vera (arXiv:2509.04598v2) addresses algorithms for \(P_6\)-free graphs and counting in that restricted class, which does not cover lollipops of arbitrarily large cycle length. The foundational Lu--Ko--Tang work (2002) introduces PED optimization, not the present counting bound. No historical-priority certification is claimed.

## Limitations

The theorem does not cover general unicyclic graphs with multiple attached trees or arbitrary connected graphs. The direct enumeration is finite; the infinite claim relies on the transfer identities and positivity induction. The literature comparison includes a full-text examination of the main 2026 source and a scoped examination of the 2025 predecessor, but unpublished or differently named equivalent results may exist; independent historical review remains appropriate.

## References

- Luciano N. Grippo, Min Chih Lin, Verónica Moyano, and Camilo Vera, *Counting perfect edge dominating sets: extremal results and linear-time algorithms*, arXiv:2607.03894v1, first publicly submitted July 4, 2026, especially Theorems 3.6, 4.4, 5.2 and Conjecture 5.1. https://arxiv.org/abs/2607.03894
- Luciano N. Grippo, Min Chih Lin, and Camilo Vera, *Perfect Edge Domination in P6-free Graphs and in Graphs Without Efficient Edge Dominating Sets*, arXiv:2509.04598v2; first submitted September 4, 2025. https://arxiv.org/abs/2509.04598
- Chin Lung Lu, Ming-Tat Ko, and Chuan Yi Tang, *Perfect edge domination and efficient edge domination in graphs*, Discrete Applied Mathematics 119 (2002), 227--250. DOI: 10.1016/S0166-218X(01)00198-6.
