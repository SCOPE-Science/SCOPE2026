# Rank-stratified square-zero representations of two-generator quantum complete intersections

## Finding
For every integer \(r\ge1\), every finite field \(k=\mathbb F_q\), every \(\zeta\in k^\times\), and every \(0\le s\le r\), the number of matrices \(Y\in M_{2r}(k)\) satisfying
\[
Y^2=0,\qquad XY=\zeta YX,\qquad \operatorname{rank}Y=s
\]
for a *fixed* square-zero matrix \(X\) of maximal rank \(r\) is
\[
\boxed{H_{r,s}(q)=\sum_{j=0}^{\lfloor r/2\rfloor}
\begin{bmatrix}r\\j\end{bmatrix}_q
\begin{bmatrix}r-j\\j\end{bmatrix}_q
|\mathrm{GL}_j(k)|\ q^{2j(r-j)}
\begin{bmatrix}r-2j\\s-2j\end{bmatrix}_q^{\!2}
|\mathrm{GL}_{s-2j}(k)|.}
\]
An out-of-range Gaussian coefficient and its entire summand are interpreted as zero. The empty general linear group has order one. Every individual rank count is *independent of the twisting parameter* \(\zeta\ne0\). The number of labelled ordered pairs of this kind is
\[
\boxed{\begin{bmatrix}2r\\r\end{bmatrix}_q|\mathrm{GL}_r(k)|\,H_{r,s}(q).}
\]

## Assumptions and scope
The parameter \(q\) is any prime power, including nonprime powers and characteristic two. Both generators have square zero; the first has **maximal possible square-zero rank** in even dimension \(2r\), while the second has prescribed rank \(s\). The representations are labelled matrix pairs, not conjugacy orbits. All ranks are ranks over \(k\). The algebra represented is the four-dimensional quantum complete intersection
\[
\Lambda_\zeta=k\langle u,v\rangle/(u^2,v^2,uv-\zeta vu).
\]
A square-zero \(2r\)-dimensional operator can have rank at most \(r\), and the maximal-rank locus is the natural open stratum in the square-zero variety. It consists of modules free of rank \(r\) over the dual-number subalgebra \(k[u]/(u^2)\). The Gaussian coefficient \(\begin{bmatrix}m\\t\end{bmatrix}_q\) counts \(t\)-subspaces of an \(m\)-space, and
\[
|\mathrm{GL}_t(k)|=\prod_{i=0}^{t-1}(q^t-q^i),\qquad|\mathrm{GL}_0(k)|=1.
\]

## Proof
**Step 1: Normal form of the first generator.** Every maximal-rank square-zero \(X\in M_{2r}(k)\) has \(\operatorname{im}X=\ker X\) of dimension \(r\). Choose a complementary \(r\)-space so that
\[
X=\begin{pmatrix}0&I_r\\0&0\end{pmatrix}.
\]
Write \(Y=\begin{psmallmatrix}A&C\\D&B\end{psmallmatrix}\). Comparing the four blocks of \(XY=\zeta YX\) gives \(D=0\) and \(B=\zeta A\). Hence **every** candidate, not merely a subclass, has the unique form
\[
Y=\begin{pmatrix}A&C\\0&\zeta A\end{pmatrix},\quad
A,C\in M_r(k).
\]
Its square vanishes if and only if
\[
A^2=0,\qquad AC+\zeta CA=0.
\]

**Step 2: Fixed reduced square-zero block.** Put \(j=\operatorname{rank}A\), so \(0\le j\le\lfloor r/2\rfloor\), and let \(h=r-2j\). Select a decomposition \(k^r=U\oplus T\oplus H\), with \(\dim U=\dim T=j\), \(\dim H=h\), and \(A\) the identity map from \(T\) to \(U\) and zero elsewhere. Write \(C\) as a three-by-three block matrix in this order. A direct block multiplication of \(AC+\zeta CA=0\) imposes precisely
\[
C_{T,U}=0,\quad C_{T,H}=0,\quad C_{H,U}=0,\quad
C_{T,T}=-\zeta C_{U,U}.
\]
All other blocks are arbitrary. In particular, the induced endomorphism \(\overline C\) of \(\ker A/\operatorname{im}A\cong H\) is exactly the unconstrained block \(C_{H,H}\). For each prescribed \(\overline C\), the number of matrices \(C\) satisfying the equation is
\[
q^{2j^2+2jh}=q^{2j(r-j)}.
\]
This also proves explicitly that the fiber count does not depend on the nonzero value of \(\zeta\).

**Step 3: Rank calculation.** The lower component of \(Y(u,v)=(Au+Cv,\zeta Av)\) has image of dimension \(j\). Restricting to its kernel \(v\in\ker A\), the upper component ranges over \(\operatorname{im}A+C(\ker A)\), whose dimension is \(j+\operatorname{rank}\overline C\). Thus
\[
\operatorname{rank}Y=2j+\operatorname{rank}\overline C.
\]
This is an equality for every admitted \(C\); it is not an inequality or a generic-rank assertion.

**Step 4: Exact finite-field factors.** The number of square-zero rank-\(j\) matrices \(A\) on an \(r\)-space is
\[
S_{r,j}(q)=\begin{bmatrix}r\\j\end{bmatrix}_q
\begin{bmatrix}r-j\\j\end{bmatrix}_q|\mathrm{GL}_j(k)|.
\]
Indeed, choose the image \(U\) (dimension \(j\)), a kernel of dimension \(r-j\) containing \(U\), and an isomorphism from the \(j\)-dimensional quotient onto \(U\). Independently, the number of rank-\(t\) endomorphisms of an \(h\)-space is
\[
G_{h,t}(q)=\begin{bmatrix}h\\t\end{bmatrix}_q^2|\mathrm{GL}_t(k)|,
\]
by choosing image, kernel and an induced isomorphism. Summing over \(j\) with \(t=s-2j\), and multiplying by the constant number of \(C\)-lifts, proves the first boxed formula.

**Step 5: Labelled first generators.** To count \(X\), select its common image/kernel \(r\)-space in \(k^{2r}\), and choose the isomorphism from the quotient onto that subspace. This gives \(\begin{bmatrix}2r\\r\end{bmatrix}_q|\mathrm{GL}_r(k)|\) possibilities, with the same \(Y\) count by conjugacy. This establishes the second boxed formula and completes the proof.

## Verification
A standalone Python 3 program `verify.py` enumerates **every** pair of blocks \((A,C)\) for seven small finite-field cases and directly tests matrix multiplication, the twisting identity, \(Y^2=0\), and \(\operatorname{rank}Y\). The validated cases are \((q,r,\zeta)=(2,1,1),(2,2,1),(3,2,1),(3,2,2),(4,2,2),(4,2,3),(2,3,1)\). The implementation includes polynomial-basis arithmetic in \(\mathbb F_4\), not merely prime-field arithmetic. For \((r,q)=(2,2)\), the rank fibers are \((1,9,18)\); for \((2,3)\), they are \((1,32,120)\), identically for both possible nonzero twists; for \((3,2)\), they are \((1,49,630,504)\). Each agrees with the formula. Run `python3 verify.py` to reproduce all checks; the final marker is `TWISTED_SQZERO_MAXRANK_OK 7 complete block enumerations`. The proof, not the finite checks, establishes arbitrary size and field order.

## Relationship to prior work
Bergh and Erdmann (2007) introduced extensive homological results for codimension-two quantum complete intersections; they do not give this rank-resolved representation count. Chen and Wang (2018) and Chen and Lu (2019) classify components and dimensions of anti-commuting and quantum-plane representation varieties, respectively, predominantly under characteristic-zero or algebraically closed hypotheses, not these labelled finite-field square-zero rank fibers. Huang (2021/2022), *Counting on the variety of modules over the quantum plane*, gives the unrestricted \(\zeta\)-commuting pair generating function, including aggregate nilpotent-pair independence of \(\zeta\) (Remark 4.1 and Eq. (59)); **that aggregate independence is prior work, not claimed here**. The new result conditions simultaneously on **both** square-zero constraints, maximal first-generator rank, and the complete second-generator rank distribution, with a specific Gaussian product-sum formula. Aggregate nilpotent counts do not determine these separate rank fibers. Huang's twisted-centralizer normal forms are related ingredients; the additional nonlinear square-zero restriction, homology-block rank relation, and individual coefficients are established explicitly above. The finite-field identity should not be construed as classifying all quantum-plane modules.

## Limitations
The first operator has maximal square-zero rank and the underlying vector-space dimension is even; arbitrary first-operator ranks, odd dimensions, modules up to isomorphism, other nilpotency indices and scheme-theoretic nonreduced structure are not classified. The independence of \(\zeta\) for nilpotent pairs without these refinements is already known. Relevant literature may contain implicit specializations that could affect publication priority; no independent audit or definitive historical novelty certification has been performed.

## References
1. P. A. Bergh and K. Erdmann, “(Co)homology of quantum complete intersections,” arXiv:0709.3029v1, first public 2007-09-19, especially Introduction and Section 2.
2. X. Chen and W. Wang, “Anti-commuting varieties,” arXiv:1805.00378v1, first public 2018-05-01, Introduction and Sections 2, 6.
3. X. Chen and M. Lu, “Varieties of modules over the quantum plane,” arXiv:1910.02198v1, first public 2019-10-05, Introduction and Sections 2–3, 6–7.
4. Y. Huang, “Counting on the variety of modules over the quantum plane,” *Algebraic Combinatorics* 5 (2022), 583–592, arXiv:2110.15570v1, DOI 10.5802/alco.230, especially Theorem 1.2, Section 4, Remark 4.1.
