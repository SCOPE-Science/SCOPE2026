# A 56-periodic reflection Lefschetz character for six-row grid independence complexes

## Finding

For every integer \(n\geq 1\), let \(G_n=P_n\square P_6\) be the Cartesian-product grid graph and \(X_n=\operatorname{Ind}(G_n)\) its simplicial independence complex. Let the commuting involutions \(a(x,y)=(n+1-x,y)\) and \(b(x,y)=(x,7-y)\) act on \(X_n\), and set \(r=ab\). Define the *reduced Lefschetz character*

\[
\mathcal L_n(g)=\sum_{i\geq0}(-1)^i\operatorname{tr}\!\left(g_*\mid\widetilde H_i(X_n;\mathbb Q)\right).
\]

The complete character on \(C_2\times C_2=\{1,a,b,r\}\) is

\[
\boxed{\bigl(\mathcal L_n(1),\mathcal L_n(a),\mathcal L_n(b),\mathcal L_n(r)\bigr)=\bigl(-F_n,-F_{q(n)},-U_n,-Z_n\bigr),}
\]

where \(q(n)=(n+1)/2\) for odd \(n\) and \(q(n)=n/2-1\) for even \(n\). The auxiliary integer sequences are specified completely by

\[
F_0=1,\qquad F_{j+28}=F_j\quad(j\geq0),\qquad (U_0,U_1,U_2,U_3)=(1,-1,-1,1),\quad U_{j+4}=U_j.
\]

The full first period of \(F\), indexed from \(1\) through \(28\), is

\[
\begin{aligned}
(F_1,\ldots,F_{14})&=(1,-1,-1,3,1,-3,1,5,-1,-5,3,5,-3,-3),\\
(F_{15},\ldots,F_{28})&=(5,3,-5,-1,5,1,-3,1,3,-1,-1,1,1,1).
\end{aligned}
\]

The full first period of the new half-turn sequence \(Z\), indexed from \(1\) through \(56\), is

\[
\begin{aligned}
(Z_1,\ldots,Z_{14})&=(-1,1,1,-1,1,1,-1,3,1,-1,3,-3,-1,3),\\
(Z_{15},\ldots,Z_{28})&=(-3,3,3,-3,3,-1,-3,5,-1,1,5,-5,1,1),\\
(Z_{29},\ldots,Z_{42})&=(-5,5,1,-1,5,-3,-1,3,-3,3,3,-3,3,-1),\\
(Z_{43},\ldots,Z_{56})&=(-3,3,-1,1,3,-1,1,1,-1,1,1,-1,1,1).
\end{aligned}
\]

In particular, \(Z_{n+56}=Z_n\) for every \(n\ge1\), and **56 is the least positive period** of \(Z\) and of the four-entry character. For every \(n\ge1\), the half-turn reduced Lefschetz number belongs to \(\{\pm1,\pm3,\pm5\}\). This is a refinement of the published period-28 ordinary Euler characteristic, not a new claim about the nonequivariant homotopy types.

For illustration, the published nonequivariant equivalence \(X_8\simeq\bigvee^5S^{11}\) and the character formula imply that the genuine \(C_2\times C_2\) representation on \(\widetilde H_{11}(X_8;\mathbb Q)\) has character \((5,-1,1,3)\). Its one-dimensional character decomposition consists of two trivial constituents, one constituent with \(a\) acting by minus one and \(b\) by plus one, and two constituents where both generators act by minus one.

## Assumptions and scope

The graph \(P_j\) is the simple path on \(j\) vertices; \(P_0\) means the empty graph only for interpreting \(F_0\). Grid edges join vertices of Manhattan distance one. The independence complex contains the empty simplex, and the reduced Lefschetz number is normalized using the augmented simplicial chain complex (including its degree-minus-one term). The parameter \(n\) ranges over all positive integers, and all homology representations use coefficients in \(\mathbb Q\). The group action can be nonfaithful for the smallest \(n\).

This theorem determines the *virtual alternating homology representation* for arbitrary \(n\); it does not assert that homology is concentrated in one degree for arbitrary \(n\), or identify the separate actions on each nonzero homology group. The actual single-degree representation at \(n=8\) follows by combining the formula with a separately published homotopy classification.

## Proof

**1. Signed orbit formula.** Let \(g\) be a graph automorphism. A nonempty independent vertex subset fixed setwise by \(g\) is a disjoint union of \(s\) cycles of \(g\) containing altogether \(t\) vertices. Its oriented simplex contributes \((-1)^{t-1}(-1)^{t-s}=(-1)^{s-1}\) to the alternating simplicial trace. The empty simplex contributes \(-1\) in augmented degree minus one. Delete every cycle that contains a graph edge; on the remaining cycles put an edge when an original graph edge joins their vertices. Call this finite *orbit-conflict graph* \(Q_g\). The augmented Hopf trace identity therefore yields

\[
\mathcal L_n(g)=-I(Q_g;-1),\qquad I(Q;t)=\sum_{J\ \mathrm{independent\ in}\ Q} t^{|J|}.
\]

This equality holds for each automorphism, whether or not it has fixed vertices, and accounts for orientation signs rather than counting setwise fixed simplices without signs.

**2. Quotients for three reflections.** The identity produces \(-F_n\), where \(F_j=I(P_j\square P_6;-1)\). The horizontal reflection \(a\) identifies paired columns. For odd \(n\), its quotient is \(P_{(n+1)/2}\square P_6\). For even \(n\), all orbits in the central paired columns contain an edge and are deleted; the quotient is \(P_{n/2-1}\square P_6\). The vertical reflection \(b\) pairs rows \((1,6),(2,5),(3,4)\). The last orbit contains a vertical edge and is deleted, leaving \(P_n\square P_2\), whose signed independence polynomial is \(U_n\).

**3. Half-turn boundary conditions.** Let \(\mathcal S\) be the \(21\) subsets of \(\{1,\ldots,6\}\) with no two consecutive elements. For each \(p\in\mathcal S\), put \(w_p=(-1)^{|p|}\). Define the explicitly integral \(21\)-by-\(21\) matrix

\[
T_{p,q}=\begin{cases}(-1)^{|q|}&p\cap q=\varnothing,\\0&\text{otherwise.}\end{cases}
\]

Let \(\mathbf1\) be the all-ones column, and define columns \(e,o\) by

\[
\begin{aligned}
e(p)&=\mathbf1_{\{1,6\}\not\subseteq p}\,\mathbf1_{\{2,5\}\not\subseteq p},\\
o(p)&=1-\mathbf1_{p\cap\{1,6\}=\varnothing}-\mathbf1_{p\cap\{2,5\}=\varnothing}.
\end{aligned}
\]

Row-by-row independent-set enumeration gives, for all \(k\ge1\),

\[
F_k=w^{\mathsf T}T^{k-1}\mathbf1,\qquad
Z_{2k}=w^{\mathsf T}T^{k-1}e,\qquad
Z_{2k+1}=w^{\mathsf T}T^{k-1}o,
\]

and \(Z_1=-1\). Indeed, the half-turn quotient of an even-width grid has \(k\) full columns; the seam forbids simultaneous choices from each of the row pairs \(\{1,6\}\) and \(\{2,5\}\). For an odd-width grid it has \(k\) full columns and a final partial column with two competing orbits \(\{1,6\}\) and \(\{2,5\}\); selecting neither or either gives the column \(o\). The third central orbit \(\{3,4\}\) is forbidden by an internal edge. At \(n=1\), the quotient is one edge, so its signed independence count is \(-1\).

**4. Exact matrix certificate and global period.** Direct integer multiplication of the explicitly defined matrix establishes the three finite identities

\[
T^{28}\mathbf1=\mathbf1,\qquad T^{28}e=e,\qquad T^{28}o=o.
\]

A separate three-state transfer matrix for a two-row strip likewise fixes its all-ones boundary vector after four steps. All four equalities are reproducibly evaluated, coordinate by coordinate over exact integers, in the included standalone verifier. Thus the formulas of step 3 prove periods \(28\) for \(F\) and \(56\) for the even and odd subsequences of \(Z\). The endpoint values \(F_0=F_{28}=1\) and \(Z_1=Z_{57}=-1\), also checked by their respective finite formulas, close the boundary cases. The displayed lists follow from the same explicit matrix products. Therefore all four Lefschetz entries are 56-periodic.

Since \(Z_1\ne Z_{29}\), 28 is not a period; similarly \(Z_1\ne Z_9\) and \(Z_1\ne Z_8\), ruling out periods 8 and 7. Every proper divisor of 56 divides at least one of those three numbers, so the least period is 56. Its first-period list has absolute values precisely \(1,3,5\), giving the stated universal bound.

**5. Representation example.** At \(n=8\), the preceding formulas give reduced Lefschetz values \((-5,1,-1,-3)\). The established homotopy type is \(\bigvee^5 S^{11}\), hence the actual degree-11 homology character is \((5,-1,1,3)\). The four ordinary character inner products in \(C_2\times C_2\) equal \(2,1,0,2\) for sign pairs \((+,+),(-,+),(+,-),(-,-)\), respectively.

## Verification

The standalone reproducibility artifact `artifacts/verify.py` uses only the Python standard library. Its exact-integer operations construct the 21 transfer states and all three boundary vectors from their definitions, check each of the three matrix identities after 28 multiplications, construct the 28- and 56-entry tables, certify four-periodicity for the two-row strip, and exclude every proper period divisor of 56. An independent orbit-graph construction with deletion-contraction recursion checks all four group elements for \(1\le n\le8\) (32 symmetry cases); it does not reuse the transfer-matrix quotient formula. The same verifier also checks all four character multiplicities are integers for \(1\le n\le120\).

To replay, extract the artifact beside these files and execute `python3 artifacts/verify.py` with ordinary Python 3; the expected line begins `VERIFY_OK`. Finite direct enumerations are checks, not the proof of the all-parameter assertion. The all-parameter proof follows from the exact matrix equalities and orbit descriptions.

## Relationship to prior work

Matsushita and Wakatsuki [1] determine the nonequivariant homotopy types for every six-row grid (Theorem 1.1) and its ordinary Euler-characteristic period 28 (Corollary 1.2). Their proof uses vertical reflection to identify certain auxiliary graphs, but does not calculate the action of the reflection group on homology or a half-turn Lefschetz character. The already known nonequivariant values \(F\) are included only to state the complete four-element character.

Bousquet-Mélou, Linusson, and Nevo [2] develop general hard-square transfer methods, including matrices for rectangular grids and partial transfer spectra. That machinery supports the counting framework but does not give the three specific half-turn boundary vectors and their exact 56-periodic character. The new statement is not a consequence of the published ordinary Euler table alone, since homotopy equivalences do not specify how graph automorphisms act. The explicit finite boundary-matrix calculation is the distinguishing step.

## Limitations

The result is an equivariant **Euler/Lefschetz** classification, not an equivariant homotopy equivalence and not a complete decomposition of every individual homology degree. It is confined to six-row open rectangular grids and rational coefficients. The 56-periodic virtual character may conceal cancellation among different homological degrees. The matrix certificate proves its exact algebraic identities but does not address arbitrary-width grids. No assertion of mathematical priority beyond inspected sources is made; an unindexed or indirectly equivalent equivariant calculation remains a bibliographic risk.

## References

[1] T. Matsushita and S. Wakatsuki, *Independence complexes of \((n\times6)\)-grid graphs*, arXiv:2207.10363, first publicly posted 2022-07-21, Theorem 1.1, Corollary 1.2, and Section 3. https://arxiv.org/html/2207.10363v2

[2] M. Bousquet-Mélou, S. Linusson, and E. Nevo, *On the independence complex of square grids*, arXiv:math/0701890, Sections 6–7 (transfer matrices, rectangular-grid spectra). https://arxiv.org/html/math/0701890v2
