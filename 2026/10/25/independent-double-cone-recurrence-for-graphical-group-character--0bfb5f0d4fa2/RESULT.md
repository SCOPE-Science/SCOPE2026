# Independent double-cone recurrence for graphical-group character degrees

## Finding

Let \(\Gamma\) be any finite simple graph on \(n\geq1\) vertices and \(m\) edges. Over a finite field \(\mathbb F_q\), associate to a choice of edge coefficients \(\lambda\in\mathbb F_q^{E(\Gamma)}\) the alternating matrix \(B_\Gamma(\lambda)\) whose entry above the diagonal is \(\lambda_{ij}\) on graph edges and zero on nonedges. Let
\[
A_\Gamma(q,z)=\sum_{\lambda\in\mathbb F_q^{E(\Gamma)}} z^{\operatorname{rank} B_\Gamma(\lambda)/2}
 =\sum_r a_r(q)z^r.
\]
Put \(\Delta=\Gamma\vee\overline{K_2}\), the graph formed by adjoining two mutually nonadjacent vertices, each adjacent to every original vertex. Then \(\Delta\) has \(n+2\) vertices and \(m+2n\) edges, and **its complete alternating-rank enumerator is determined by that of \(\Gamma\)**:
\[
\boxed{A_\Delta(q,z)=\sum_r a_r(q)z^r\bigl[U_r+V_{r,d}z+W_{r,d}z^2\bigr],\qquad d=n-2r,}
\]
where
\[
\begin{aligned}
U_0&=1,\\
U_r&=q^{2r}+(q^{2r}-1)q^{2r-1}\quad(r\geq1),\\
V_{r,d}&=q^{4r}-U_r+q^{4r}(q+1)(q^d-1),\\
W_{r,d}&=q^{4r}(q^d-1)(q^d-q).
\end{aligned}
\]
Terms with zero coefficient may be omitted. This formula holds over **all finite fields** for alternating-matrix ranks, including characteristic two.

For **odd** \(q\), define the graphical group \(G_\Gamma(q)\) of class two from graph vertices and central edge commutators. The number of ordinary complex irreducible characters of degree \(q^j\) of \(G_\Delta(q)\) is exactly
\[
\boxed{q^{n+2-2j}[z^j]A_\Delta(q,z).}
\]
Thus character-degree polynomiality is preserved under this independent double-cone operation. In particular, every complete tripartite graphical group of the form \(G_{K_{2,a,b}}(q)\), for integers \(a,b\geq1\) and odd \(q\), has an explicit uniform degree distribution by substituting
\[
a_r(q)=\frac{\prod_{j=0}^{r-1}(q^a-q^j)(q^b-q^j)}{\prod_{j=0}^{r-1}(q^r-q^j)}\quad(0\leq r\leq\min(a,b))
\]
into the boxed recurrence with \(n=a+b\).

## Assumptions and scope

Graphs are finite and simple, and the two new vertices form an edgeless pair. Edge coordinates vary independently in the full field. The rank statement is valid in every finite characteristic; the character statement is asserted only for odd characteristic. In the latter statement, characters mean ordinary complex irreducible representations, and the graphical group has \(q^{n+m}\) elements before the two-vertex extension.

## Proof

**1. Reduction to a symplectic block.** Fix an old edge assignment with \(\operatorname{rank}B_\Gamma=2r\). An invertible change of the old vertex basis puts the matrix into \(J\oplus0_d\), where \(J\) is an invertible alternating \(2r\)-by-\(2r\) matrix and \(d=n-2r\). Because the new edges are unrestricted, their two coefficient rows are still uniformly and independently variable after this change. Split them as \(P\in M_{2,2r}(\mathbb F_q)\) and \(Q\in M_{2,d}(\mathbb F_q)\). The enlarged alternating matrix is congruent to
\[
J\ \oplus\begin{pmatrix}C&Q\\-Q^T&0_d\end{pmatrix},\qquad C=PJ^{-1}P^T.
\]
Here \(C\) is alternating of order two (zero diagonal even in characteristic two).

**2. The three possible increments.** Let \(s=\operatorname{rank}Q\). If \(s=2\), the residual alternating matrix has rank four, regardless of \(C\). If \(s=1\), it has rank two, regardless of \(C\): after changing the two new basis vectors and the \(d\) radical vectors, its only essential block is a nonzero alternating two-plane (the remaining one-dimensional new direction cannot create another alternating plane). If \(s=0\), its rank is zero for \(C=0\) and two for \(C\ne0\). Consequently the total rank increases by zero, two, or four, with no other possibility.

**3. Exact counts.** The number of \(2\)-by-\(d\) matrices \(Q\) of ranks zero, one, and two is respectively
\[
1,\qquad(q+1)(q^d-1),\qquad(q^d-1)(q^d-q).
\]
The number of choices of \(P\) is \(q^{4r}\). For \(r\ge1\), the condition \(PJ^{-1}P^T=0\) says its two row vectors are symplectically orthogonal. Choosing the first row zero gives \(q^{2r}\) possibilities for the second; choosing the first row nonzero gives \(q^{2r}-1\) choices followed by \(q^{2r-1}\) choices in its orthogonal hyperplane. This yields \(U_r\). For \(r=0\), \(P\) is the unique empty matrix and \(U_0=1\). Combining the rank cases gives \(U_r\), \(V_{r,d}\), and \(W_{r,d}\); summing over all old edge assignments proves the recurrence. For each fixed old assignment these multiplicities sum to \(q^{2n}\), the number of added edge assignments.

**4. From alternating ranks to characters.** In odd characteristic the graphical group admits the usual class-two presentation with vertex vector space \(V\cong\mathbb F_q^n\), central edge vector space \(Z\cong\mathbb F_q^m\), and commutator map \(\beta:V\times V\to Z\). Fix a nontrivial additive character of \(\mathbb F_q\). Every central character of \(Z\) arises from one \(\lambda\in Z^*\) and determines the alternating form \(\lambda\circ\beta\), with matrix \(B_\Gamma(\lambda)\). When its rank is \(2r\), the associated twisted group algebra decomposes into \(q^{n-2r}\) matrix blocks of order \(q^r\): choose a symplectic basis on the quotient by the radical and diagonalize the radical's abelian action. Hence there are \(q^{n-2r}\) irreducibles of degree \(q^r\) over this central character. Repeating this for \(\Delta\) proves the character formula, with no assertion about characteristic-two characters.

**5. Complete tripartite specialization.** For \(\Gamma=K_{a,b}\), the alternating edge matrix is \(\begin{psmallmatrix}0&M\\-M^T&0\end{psmallmatrix}\). Its rank is twice the rank of the unrestricted \(a\)-by-\(b\) matrix \(M\). The standard independent-column count gives precisely the formula for \(a_r(q)\) above. This proves the stated infinite-family specialization without additional restrictions on \(a\) or \(b\).

## Verification

The embedded standalone program `verify_double_independent_cone.py` enumerates every edge assignment and computes alternating-matrix ranks by modular elimination, independently of the symplectic-block proof. It verifies eight complete field/graph configurations. The largest checked example has twelve new-graph edges (\(4{,}096\) assignments over \(\mathbb F_2\)); a separate characteristic-three example has eight edges (\(6{,}561\) assignments). In addition, direct enumerations verify the rank count of rectangular matrices for the complete-bipartite specialization.

For example, for \(\Delta=K_{2,2,2}\) over \(\mathbb F_3\), the recurrence gives alternating rank-half multiplicities \((1,1376,198288,331776)\), yielding character-degree multiplicities \((729,111456,1784592,331776)\) at degrees \((1,3,9,27)\). Their degree-squared sum is \(3^{18}\), the group order. This last six-vertex calculation is an algebraic consequence of the recurrence, not a claim of literal exhaustion of all \(3^{12}\) edge assignments.

## Relationship to prior work

Graph-defined two-step nilpotent Lie algebras and their rigidity are established background (Mainkar, 2013). The central link between alternating ranks and character degrees, and the general question of character-degree enumerations for graphical groups, are explained in Rossmann (2022), especially Section 1.6. Rossmann's Section 5 establishes a **join formula for conjugacy-class distributions**, not the present character-degree rank transition. An existing published result treats a **single universal added vertex**, including \(K_{1,a,b}\); two successive universal-vertex operations would join the newly added vertices and produce a different graph. The present double-cone recurrence has its own nonzero symplectic-row-pair correction and produces \(K_{2,a,b}\). No claim is made that the general rank-to-character correspondence, the single-vertex recurrence, or the rectangular rank formula is new.

## Limitations

The closed recurrence specifically concerns adding **two mutually nonadjacent universal neighbors**; it does not classify character-degree distributions for arbitrary graph joins, any number of independent new neighbors, or characteristic-two graphical groups. The full body of the closest single-vertex published research record was unavailable through the accessible reader, so historical priority of the two-vertex recurrence is subject to that residual comparison. Independent mathematical audit has not been performed.

## References

1. M. G. Mainkar, *Graphs and two-step nilpotent Lie algebras*, first public version 12 October 2013, arXiv:1310.3414v1; journal version *Groups, Geometry, and Dynamics* 9 (2015), 55–65.
2. T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564v1, *Bulletin of the London Mathematical Society* 54 (2022), 1923–1943, DOI: 10.1112/blms.12665. See Section 1.6 (character degree question) and Section 5 (different, conjugacy-class join invariant).
3. *Coning recurrence for character degrees of graphical groups*, published mathematical record identifier 732adc755a75, title and abstract-level comparison; full text not available through the accessible reader.
