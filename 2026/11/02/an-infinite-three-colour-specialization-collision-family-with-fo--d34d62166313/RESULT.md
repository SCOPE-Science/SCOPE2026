# An infinite three-colour specialization collision family with fourth-colour separation

## Finding
Let \(C_{(a_1,\ldots,a_s)}\) denote the caterpillar with a path of \(s\) spine vertices and exactly \(a_i-1\) pendant leaves at its \(i\)-th spine vertex. Let \(X_T(\mathbf x)\) be its chromatic symmetric function, and let \(Z_T(\mathbf x;t)\) weight a proper colouring by \(t\) raised to the number of distinct colours used. For \(m\ge2\), \(\operatorname{ps}_m\) means substitution \(\mathbf x=(1,q,\ldots,q^{m-1},0,\ldots)\).

**Theorem.** For every integer \(r\ge1\), the nonisomorphic, \((3r+6)\)-vertex caterpillars
\[
 A_r=C_{(3,r+1,r,r+2)},\qquad B_r=C_{(3,r+2,r,r+1)}
\]
satisfy
\[
 \operatorname{ps}_3(Z_{A_r}(\mathbf x;t))
 =\operatorname{ps}_3(Z_{B_r}(\mathbf x;t)).
\]
Nevertheless, they are separated by the **ordinary** fourth principal specialization. Precisely,
\[
 [q^8]\bigl(\operatorname{ps}_4(X_{A_r})-\operatorname{ps}_4(X_{B_r})\bigr)
 =\begin{cases}-14,&r=1,\\-4,&r=2,\\-2,&r\ge3.\end{cases}
\]
The member \(r=2\), up to reversing the spine, was already exhibited as an isolated three-specialization collision by Bingham–Celano–Commins–Orellana–Pan–Simone (2026). The new assertion is the infinite simultaneous family and the uniform fourth-specialization separation certificate, not the isolated member.

## Assumptions and scope
The graphs are finite simple undirected labelled-by-spine caterpillars; graph isomorphism ignores the spine labels and reverses the composition if appropriate. The parameter \(r\) ranges over every positive integer. The colours in the specialized enumerators are indexed by \(0,1,\ldots,m-1\); their product weight is \(q\) to the total colour sum. Equality of specializations is equality as polynomials, with no evaluation of \(q\) or \(t\) assumed. No claim about \(\operatorname{ps}_4\) distinguishing every caterpillar is made.

## Proof
For \(m\ge2\), define
\[
 P_i^{(m)}(q)=\sum_{j\in\{0,\ldots,m-1\}\setminus\{i\}}q^j
 \quad(0\le i<m).
\]
If \(\ell=(\ell_1,\ldots,\ell_4)\) is the four-vector of pendant-leaf multiplicities, summing proper colourings over the four spine colours gives the exact finite formula
\[
 F_m(\ell;q)=
 \sum_{\substack{c_1,c_2,c_3,c_4\in\{0,\ldots,m-1\}\\
                   c_1\ne c_2,\ c_2\ne c_3,\ c_3\ne c_4}}
 q^{c_1+c_2+c_3+c_4}\prod_{j=1}^4(P_{c_j}^{(m)}(q))^{\ell_j}.
 \tag{1}
\]
By construction, \(F_m(\ell;q)=\operatorname{ps}_m(X_{C_{(\ell_1+1,\ldots,\ell_4+1)}})\). For the two trees, \(\ell=(2,r,r-1,r+1)\) and \(\ell'=(2,r+1,r-1,r)\). Write \(P_i=P_i^{(m)}(q)\), and \(\Delta_m(r;q)=F_m(\ell;q)-F_m(\ell';q)\).

In every summand of the difference, transferring one leaf from the fourth spine vertex to the second introduces the factor \(P_{c_4}-P_{c_2}\). Terms with \(c_2=c_4\) vanish. Group the remaining terms in pairs under interchanging \(c_2=i\) and \(c_4=j\), and sum independently over \(c_1\ne c_2\). This gives the identity valid for **all** \(m\ge2\), \(r\ge1\):
\[
 \Delta_m(r;q)=
 \sum_{0\le i<j<m} q^{i+j}P_i^rP_j^r(P_j-P_i)
 (q^jP_j^2-q^iP_i^2)
 \sum_{\substack{0\le h<m\\h\notin\{i,j\}}}q^hP_h^{r-1}.
 \tag{2}
\]
No division by a polynomial or analytic limit is used in (2).

For \(m=3\), the three possible leaf polynomials are
\[
 P_0=q(1+q),\quad P_1=1+q^2,\quad P_2=1+q.
\]
The \((i,j)=(0,2)\) summand in (2) vanishes because \(P_0^2=q^2P_2^2\). The \((0,1)\) and \((1,2)\) summands cancel identically: their third colours are respectively \(2\) and \(0\); substituting \(P_0=qP_2\), \(P_1-P_0=1-q\), and \(P_2-P_1=q(1-q)\) makes them negatives. Hence \(\Delta_3(r;q)=0\) for every \(r\ge1\).

This proves equality of the \(t=1\) third specializations. Each graph is a connected bipartite tree. Its two bipartition classes have sizes \(r+3\) and \(2r+3\), because for its pendant counts \(\ell\) the classes have orders \(2+\ell_1+\ell_3\) and \(2+\ell_2+\ell_4\), in some order. With three available colours, every proper colouring uses exactly two or three colours. The two-colour contribution to both specialized \(t\)-polynomials is identically
\[
 t^2\sum_{\substack{i,j\in\{0,1,2\}\\i\ne j}}q^{(r+3)i+(2r+3)j}.
\]
Subtracting these equal two-colour contributions from the equal ordinary third specializations also equates the three-colour contributions, proving equality with the full \(t\)-grading.

For separation, specialize (2) to \(m=4\) and use
\[
 P_0=q+q^2+q^3,\quad P_1=1+q^2+q^3,\quad
 P_2=1+q+q^3,\quad P_3=1+q+q^2.
\]
Introduce the formal power series \(H(z,q)=\sum_{r\ge1}z^r\Delta_4(r;q)\). The geometric-series identity
\[
 \sum_{r\ge1}z^rP_i^rP_j^rP_h^{r-1}
 =\frac{zP_iP_j}{1-zP_iP_jP_h}
\]
transforms (2) into a **finite rational expression**:
\[
 H(z,q)=\sum_{0\le i<j<4}\ \sum_{h\notin\{i,j\}}
 \frac{zq^{i+j+h}P_iP_j(P_j-P_i)(q^jP_j^2-q^iP_i^2)}
 {1-zP_iP_jP_h}.
 \tag{3}
\]
For reproducible verification of the critical coefficient, expand each denominator as a formal series in \(q\) through degree eight. Grouping the resulting coefficient \([q^8]\) by the six pairs \((i,j)\), their contributions to \([q^8]H\) are, respectively,
\[
\begin{array}{c|c}
 (i,j)&[q^8]\text{ contribution}\\\hline
 (0,1)&z(z^3+4z^2+3z-1)\\
 (0,2)&-2z\\
 (0,3)&-z(z+4)\\
 (1,2)&-z(z^4+2z^3-2z^2+2z-4)/(z-1)\\
 (1,3)&-z(z^3+2z^2-z-3)/(z-1)\\
 (2,3)&0
\end{array}
\]
These are exact polynomial/rational arithmetic identities, reproduced by `verify.py` using a coefficient recurrence, not numerical fitting. Summation simplifies to
\[
 [q^8]H(z,q)=-14z-4z^2-\frac{2z^3}{1-z}.
\]
Comparing coefficients of \(z^r\) proves the claimed three cases for all \(r\), so the fourth ordinary principal specializations differ.

Finally, both four-part compositions have endpoints at least two and have the same length. They are neither equal nor mutual reversals for any integer \(r\ge1\). The canonical-spine isomorphism criterion for caterpillars therefore proves \(A_r\not\cong B_r\).

## Verification
Run `python verify.py` after extracting this complete package; its only nonstandard dependency is SymPy. It reconstructs all six rational pair contributions by exact coefficient recurrence and asserts the closed \(z\)-series identity. Independently, a vertex-adjacency tree dynamic program computes the full refined proper-colouring enumerators for both trees at \(r=1,\ldots,6\) and both palettes. A separate direct colouring enumeration checks the dynamic program for \(r=1\) with three and four colours and \(r=2\) with three colours. All checks passed. Finite checks support, but do not replace, the all-\(r\) algebraic proof above.

## Relationship to prior work
Bingham et al., *Principal specializations of the t-chromatic symmetric function*, arXiv:2610.31785v1 (first publicly submitted 2026-10-22), introduce the invariant and prove recovery theorems for elongated bistars and three-spine-vertex caterpillars. Their Discussion exhibits one three-specialization collision: \((3,4,2,3)\) and \((4,2,3,3)\). This is the \(r=2\) member here, up to reversal, so its mere existence is prior work. Their fourth-specialization reconstruction conjectures are supported computationally on certain bounded families, but do not imply an all-\(r\) algebraic separation for these two families. The present finding supplies the infinite extension and its explicit witness.

Arunkumar–Narayanan–Rao–Sawant (arXiv:2307.02234v2) prove that the **full** chromatic symmetric function distinguishes proper \(q\)-caterpillars. The full invariant is stronger than a fixed finite principal specialization, so this theorem neither prohibits nor supplies the asserted collisions. The more general full-invariant caterpillar reconstruction results discussed there have the same inapplicability. Source and priority limitations are recorded in `REVIEW.md`.

## Limitations
The equality assertion concerns the third *principal specialization*, not the full chromatic symmetric function, and is restricted to the explicit four-spine infinite family. The difference certificate uses the ordinary fourth specialization; it does not settle whether every caterpillar is distinguished by its fourth specialization. The known \(r=2\) collision is not itself claimed as new. Independent historical-priority and mathematical audits have not been performed.

## References
1. A. Bingham, K. Celano, P. Commins, R. Orellana, J. Pan, and M. C. Simone, *Principal specializations of the t-chromatic symmetric function*, arXiv:2610.31785v1, 2026-10-22, https://arxiv.org/html/2610.31785v1 (Sections 3, 5, 6).
2. G. Arunkumar, N. Narayanan, R. Rao B. V., and S. S. Sawant, *Proper q-caterpillars are distinguished by their Chromatic Symmetric Functions*, arXiv:2307.02234v2, 2023-07-21, https://arxiv.org/html/2307.02234v2.
3. R. P. Stanley, *A symmetric function generalization of the chromatic polynomial of a graph*, Advances in Mathematics 111 (1995), 166–194, as referenced in [1] and [2].
