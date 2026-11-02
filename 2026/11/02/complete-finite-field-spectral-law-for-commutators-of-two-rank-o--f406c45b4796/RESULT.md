# Complete finite-field spectral law for commutators of two rank-one matrices

## Finding

Let \(n\ge2\), let \(q\) be any prime power, put \(k=\mathbb F_q\), and denote by \(\mathcal R_n(q)\) the set of all matrices in \(M_n(k)\) of rank exactly one. For each ordered pair \((X,Y)\in\mathcal R_n(q)^2\), write \(C=XY-YX\). Set
\[
Q=\frac{(q^n-1)^2}{q-1},\quad
N_0=\frac{(q^n-1)(q^{n-1}-1)}{q-1},\quad
N_1=(q^n-1)q^{n-1},\quad
A=\frac{(q^{n-1}-1)^2}{q-1}.
\]
Here \(Q\) is the number of rank-one matrices; \(N_0\) and \(N_1\) respectively count those of trace zero and trace nonzero, and \(Q=N_0+N_1\).

**Theorem (exact rank and spectral distribution).** The numbers \(Z_r\) of ordered pairs whose commutator has rank \(r\) are
\[
Z_0=QA+(q-1)N_1,\qquad
Z_2=(q-1)N_0q^{2n-2}+(q-1)N_1(q^{n-1}-1)^2,\qquad
Z_1=Q^2-Z_0-Z_2.
\]
No commutator has rank exceeding two. Every rank-one commutator is square-zero. For a rank-two commutator there is a unique \(\Delta\in k\) with
\[
\chi_C(T)=T^{n-2}(T^2-\Delta).
\]
The number \(Z_{2,\Delta}\) of ordered pairs with rank-two commutator and this parameter equals
\[
Z_{2,0}=N_1(q-1)(q^{n-1}-1)(q^{n-2}-1)
\]
and, for each \(\Delta\in k^\times\),
\[
Z_{2,\Delta}=h_q(\Delta)N_0q^{2n-2}
  +N_1(q-1)(q^{n-1}-1)q^{n-2},\qquad
h_q(\Delta)=\#\{c\in k^\times:c^2=\Delta\}.
\]
Thus \(h_q(\Delta)=1\) for even \(q\), while for odd \(q\) it is two on nonzero squares and zero on nonsquares.

**Complete Jordan information.** Rank-zero commutators vanish, rank-one commutators have nilpotent type \(J_2(0)\oplus0_{n-2}\), and rank-two commutators with \(\Delta=0\) have nilpotent type \(J_3(0)\oplus0_{n-3}\) (the latter exist exactly when \(n\ge3\)). For \(\Delta\ne0\), the image is a two-dimensional invariant summand and \(C\) is zero on a complementary kernel: its characteristic polynomial on the image is \(T^2-\Delta\). If \(q\) is odd this image operator is semisimple over an algebraic closure; over \(k\) it splits exactly when \(\Delta\) is a square. If \(q\) is even, write \(\Delta=c^2\) with unique \(c\in k^\times\). The number of such pairs with **diagonalizable** \(C\) is exactly
\[
Z^{\mathrm{diag}}_{2,c^2}=N_0q^{2n-3},
\]
and the remaining
\[
Z^{\mathrm{J}}_{2,c^2}=N_0(q-1)q^{2n-3}
+N_1(q-1)(q^{n-1}-1)q^{n-2}
\]
have one \(2\times2\) Jordan block for eigenvalue \(c\) and zero blocks in the kernel. Here diagonalizable means diagonalizable over \(k\). This gives every rational canonical form attained, together with its exact ordered-pair multiplicity.

## Assumptions and scope

The field has \(q\ge2\) elements, of arbitrary characteristic. The dimension is an integer \(n\ge2\). Both matrices are nonzero of rank exactly one; pairs are ordered and counted with multiplicity (not up to simultaneous conjugacy). The counts \(Z_{2,\Delta}\) distinguish every parameter in the field, not just square classes. No assertion is made about ranks or spectra for two arbitrary higher-rank matrices. The theorem is characteristic-free except for the explicit square-root and Jordan refinements.

## Proof

**Rank-one representations and trace strata.** Write \(X=uv^{\mathsf T}\), \(Y=st^{\mathsf T}\), with each of \(u,v,s,t\) nonzero. Scaling \((u,v)\) by \((\lambda,\lambda^{-1})\) leaves \(X\) fixed, and these are all the duplicates, giving \(Q\). The trace of \(X\) is \(\delta=v^{\mathsf T}u\). For each nonzero \(u\), there are \(q^{n-1}-1\) nonzero \(v\) with \(v^{\mathsf T}u=0\), and \((q-1)q^{n-1}\) choices with nonzero trace, before dividing by \(q-1\). Hence the stated \(N_0,N_1\).

Set \(a=v^{\mathsf T}s\), \(b=t^{\mathsf T}u\), and \(d=t^{\mathsf T}s\). Direct multiplication gives
\[
C=a\,ut^{\mathsf T}-b\,sv^{\mathsf T}.
\]
When \(a=b=0\), \(C=0\). Otherwise, if both \(a,b\ne0\), the two summands cancel exactly when the rank-one operators \(X,Y\) are proportional. If precisely one of \(a,b\) is zero then \(C\ne0\). Moreover \(C\) has rank two precisely when \(a,b\ne0\), \(u,s\) are independent, and \(v,t\) are independent. All remaining nonzero commutators have rank one. A commutator has trace zero. A rank-one matrix with trace zero has square zero, since \((wv^{\mathsf T})^2=(v^{\mathsf T}w)wv^{\mathsf T}\).

**Counting rank zero.** For fixed \(X\), \(a=b=0\) means \(s\in\ker v\setminus\{0\}\) and \(t\in\operatorname{ann}(u)\setminus\{0\}\). Modulo the \(q-1\) scaling duplicates this gives exactly \(A\) possible \(Y\). The other possibility for cancellation is \(Y=\lambda X\), \(\lambda\in k^\times\). It lies already in the first case exactly when \(\delta=0\). Therefore the number for fixed \(X\) is \(A\) when \(\delta=0\), and \(A+q-1\) otherwise. Summing proves the formula for \(Z_0\).

**The rank-two spectral parameter.** On the two-dimensional space \(W=\operatorname{span}\{u,s\}\), which is the image when \(\operatorname{rank}C=2\), the matrix of \(C\) in basis \((u,s)\) is
\[
\begin{pmatrix}ab&ad\\-b\delta&-ab\end{pmatrix}.
\]
Its trace is zero and its determinant is \(-ab(ab-\delta d)\). Put \(\Delta=ab(ab-\delta d)\). Since \(C\) maps the ambient space into \(W\), its characteristic polynomial is \(T^{n-2}(T^2-\Delta)\). If \(\Delta=0\), the displayed \(2\times2\) matrix is nonzero (as \(ab\ne0\)), trace zero and determinant zero; hence it is nonzero nilpotent of rank one and square zero. Since \(C\) maps onto \(W\), \(C^2\) has rank one and \(C^3=0\): precisely one Jordan block has size three, and all others have size one. Necessarily \(n\ge3\). If \(\Delta\ne0\), then \(C|_W\) is invertible, so the ambient space splits as \(W\oplus\ker C\), and the claimed nonzero characteristic-factor classification follows.

**Counting rank two with trace-zero first input.** Suppose \(\delta=0\). The conditions \(a,b\ne0\) automatically force the required independence: \(v(u)=0\) but \(v(s)=a\ne0\), and \(t(u)=b\ne0\). We then have \(\Delta=(ab)^2\). For each prescribed \(c=ab\in k^\times\), choosing the nonzero \(a,b\) with product \(c\), and the independent affine-hyperplane choices for \(s,t\), yields
\[
\frac{(q-1)q^{n-1}q^{n-1}}{q-1}=q^{2n-2}
\]
distinct \(Y\). For each \(\Delta\ne0\), there are \(h_q(\Delta)\) eligible values \(c\). Summing over the \(N_0\) trace-zero first matrices proves their stated contribution.

**Counting rank two with nonzero-trace first input.** Suppose \(\delta\ne0\). By a change of basis we may use \(u=e_1\), \(v=\delta e_1\), and write \(s=(s_1,s')\), \(t=(t_1,t')\). The rank-two condition is exactly \(s_1,t_1\ne0\) and \(s',t'\ne0\). Here \(a=\delta s_1\), \(b=t_1\), and
\[
\Delta=-ab\,\delta(t'\mathbin{\cdot}s').
\]
Fixing \(ab\in k^\times\), the nonzero vectors \(s',t'\in k^{n-1}\) have exactly \((q^{n-1}-1)(q^{n-2}-1)\) ordered choices with dot product zero, and \((q^{n-1}-1)q^{n-2}\) choices for each specified nonzero dot product. These are the standard counts of a nonzero vector and a hyperplane (or affine hyperplane) evaluation. After allowing all \(q-1\) values of \(ab\), and accounting for the \(q-1\) scaling redundancy of the representation of \(Y\), we obtain per fixed \(X\):
\[
\#\{Y:\operatorname{rank}C=2,\Delta=0\}=(q-1)(q^{n-1}-1)(q^{n-2}-1)
\]
and for each \(\Delta\ne0\):
\[
\#\{Y:\operatorname{rank}C=2,\Delta\}=(q-1)(q^{n-1}-1)q^{n-2}.
\]
Multiplication by \(N_1\) and addition of the trace-zero case proves both \(Z_{2,\Delta}\) formulas. Summing the \(q-1\) nonzero spectral parameters, together with the zero parameter, gives \(Z_2\). The remaining pairs yield \(Z_1=Q^2-Z_0-Z_2\).

**Characteristic two refinement.** Assume \(q\) is even and \(\Delta=c^2\ne0\). The restriction \(C|_W\) has characteristic polynomial \((T-c)^2\). Its diagonalizability is equivalent to \(C|_W=cI_W\); equivalently \(C^2=cC\) on the ambient space (the complement \(\ker C\) has eigenvalue zero). If \(\delta\ne0\), the lower-left entry \(-b\delta\ne0\) rules out the scalar restriction, so every such commutator has the nontrivial Jordan block. If \(\delta=0\), the displayed restriction has form \(\bigl(\begin{smallmatrix}c&ad\\0&c\end{smallmatrix}\bigr)\), which is scalar exactly when \(d=0\). For fixed \(ab=c\), the equation \(t(s)=0\) cuts a codimension-one affine slice in the free parameters, leaving \(q^{2n-3}\) distinct \(Y\) (rather than the total \(q^{2n-2}\)). There are \(N_0\) choices of \(X\), proving the diagonalizable count. Subtracting from \(Z_{2,c^2}\) gives the nonsemisimple count. This completes the classification. \(\square\)

## Verification

The accompanying standalone `verify.py` constructs finite fields of sizes \(2,3,4,5\), enumerates every rank-one matrix and every ordered pair for the cases \((q,n)=(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(5,2)\). It constructs the commutator directly, computes ranks independently by finite-field Gaussian elimination, computes the second characteristic coefficient from principal minors, and tests square-zero / index-three behavior and the characteristic-two diagonalizable split. It independently evaluates all proposed closed formulas in each case. Run `python verify.py` in the directory of the included files; successful output ends in `VERIFY_OK`. Exhaustive checks of those finite parameters do not themselves establish the theorem for all \(q,n\); the preceding symbolic argument does.

## Relationship to prior work

Zhekai Pang's 21 October 2026 work (arXiv:2610.29240v1) studies sharp *weighted Frobenius-norm inequalities* for commutators of rank-one complex matrices. The same rank-one input geometry motivates the present field-independent algebraic derivation, but inequalities over \(\mathbb C\) do not imply finite-field exact spectral multiplicities or characteristic-two Jordan counts. Cheng and Liang (2020) classify constraints on singular values, eigenvalues, and diagonal elements of commutators of \(2\times2\) complex rank-one matrices; their analytic realizability statements do not give these finite-field pair counts. Classical counts of commuting pairs of arbitrary finite-field matrices address the zero-commutator problem for a larger input class and do not directly supply the rank-two spectral fiber distribution here. Directly covering prior work was not identified in the targeted comparisons, but lack of identification is not proof of historical priority.

## Limitations

All pairs are ordered and rank exactly one. The formulas do not count simultaneous-conjugacy orbits of pairs, and they are not statements about operators of higher input ranks. Only finite fields are enumerated, although the elementary rank/Jordan implications hold more generally. Historic equivalences under alternative terminology remain possible. Independent review of the proof or its originality has not been performed.

## References

1. Zhekai Pang, *A sharp weighted commutator inequality for rank-one matrices*, arXiv:2610.29240v1 (first public 2026-10-21), https://arxiv.org/abs/2610.29240 .
2. Che-Man Cheng and Yaru Liang, *Singular Values, Eigenvalues and Diagonal Elements of the Commutator of 2 x 2 Rank One Matrices*, Electronic Journal of Linear Algebra **36** (2020), 1–20, https://journals.uwyo.edu/index.php/ela/article/download/4955/4949/5283 .
3. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, Journal of the London Mathematical Society **83** (2011), 470–492, DOI:10.1112/jlms/jdq088 (abstract available; full paper not independently inspected).
4. Jason Fulman and Robert Guralnick, *Enumeration of commuting pairs in Lie algebras over finite fields*, literature comparison concerning unrestricted commuting pairs.
