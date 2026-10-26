# Exact endpoint norms of radius-one radial Schur projections on stars

## Finding
For every integer \(n\ge1\), let \(X_n=\{0,1,\dots,n\}\) carry the graph metric of the star with hub \(0\) and \(n\) leaves. Define the radius-one Schur mask \(M_n=(\mathbf1_{\{d(i,j)\le1\}})_{i,j\in X_n}\), equivalently
\[
M_n=\begin{pmatrix}1&\mathbf1^*\\\mathbf1&I_n\end{pmatrix}.
\]
Then the ordinary and completely bounded operator norms, as well as the trace-class multiplier norm, are equal:
\[
\boxed{\ \|S_{M_n}:B(\ell_2(X_n))\to B(\ell_2(X_n))\|=\|S_{M_n}\|_{\mathrm{cb}}=\|S_{M_n}:S_1(X_n)\to S_1(X_n)\|=\frac{5n-1}{3n+1}.\ }
\]
The constants increase strictly with \(n\) and satisfy \(\frac53-\frac{5n-1}{3n+1}=\frac8{3(3n+1)}\). On any star with an infinite set of leaves the same radius-one mask defines a bounded normal Schur map on \(B(\ell_2)\), and its operator, completely bounded, and trace-class multiplier norms are all exactly \(5/3\).

## Assumptions and scope
All Hilbert spaces and matrices are complex. Write \(S_M(T)=(M_{ij}T_{ij})\), and use the Schatten trace norm \(\|T\|_1=\operatorname{Tr}|T|\). For an infinite star, the graph-distance mask is understood entrywise and extends from finite-rank matrices by the bounded normal Schur multiplier determined by its finite compressions. No homogeneity or bounded-degree assumption is made for the star.

## Proof
**Upper bound: an explicit Gram certificate.** Fix \(n\ge1\) and put
\[
 t=\frac{5n-1}{3n+1},\qquad d=t-1=\frac{2(n-1)}{3n+1},\qquad b=2-t=\frac{n+3}{3n+1}.
\]
Define the real symmetric matrix
\[
 A=\begin{pmatrix}t&b\mathbf1^*\\b\mathbf1&(t-d)I_n+dJ_n\end{pmatrix},
\]
where \(J_n=\mathbf1\mathbf1^*\). All diagonal entries of \(A\) equal \(t\). For \(w=(1,-\mathbf1)^\top\), direct calculation gives \(A-M_n=dww^*\succeq0\). Let \(P\) be the orthogonal projection onto vectors supported on the leaf coordinates with leaf-coordinate sum zero, and let \(r=(2n,n+1,\ldots,n+1)^\top\). A second exact identity is
\[
 A+M_n=2P+\frac{2}{n(3n+1)}rr^*\succeq0.
\]
Consequently \(G=\begin{pmatrix}A&M_n\\M_n&A\end{pmatrix}\succeq0\), because its orthogonal block diagonalization has blocks \(A+M_n\) and \(A-M_n\). This Gram matrix gives vectors \(u_i,v_i\) with \(\langle u_i,v_j\rangle=(M_n)_{ij}\) and \(\|u_i\|=\|v_i\|=\sqrt t\). For the diagonal embeddings \(V e_i=e_i\otimes u_i\) and \(W e_j=e_j\otimes v_j\), the identity \(S_{M_n}(T)=V^*(T\otimes I)W\) implies \(\|S_{M_n}\|_{\mathrm{cb}}\le\|V\|\|W\|=t\), hence also the ordinary operator bound.

**Matching trace-class witness.** Define a positive unit vector \(x\) by
\[
 x_0^2=\frac{n+1}{3n+1},\qquad x_j^2=\frac2{3n+1}\quad(1\le j\le n),
\]
and take the rank-one projection \(Q=xx^*\), so \(\|Q\|_1=1\). The real symmetric matrix \(B=S_{M_n}(Q)\) has the three eigenvalue levels
\[
 \frac{2(n+1)}{3n+1}\quad(\text{once}),\qquad
 \frac{2}{3n+1}\quad(\text{multiplicity }n-1),\qquad
 -\frac{n-1}{3n+1}\quad(\text{once}).
\]
Indeed, the leaf-sum-zero subspace is a \(\frac2{3n+1}\)-eigenspace; the restriction to the hub and normalized all-leaf vector has trace \(\frac{n+3}{3n+1}\) and determinant \(-\frac{2(n^2-1)}{(3n+1)^2}\), yielding the stated two other eigenvalues. For \(n=1\), the displayed last eigenvalue is zero. Hence
\[
 \|S_{M_n}(Q)\|_1=\frac{2(n+1)+2(n-1)+(n-1)}{3n+1}=t.
\]
The trace-class norm of a Schur multiplier equals the operator norm of the transpose-mask multiplier by trace duality; the mask here is real symmetric. Thus \(\|S_{M_n}\|_{B\to B}\ge t\), and all three finite-dimensional bounds are sharp. Explicitly, the sign of \(B\) (choosing the sign \(+1\) on its zero eigenspace) is the unitary \(U=I-2vv^*\), where \(v=(x_0,-x_1,\ldots,-x_n)\); it witnesses operator-norm sharpness as well.

**Infinite stars.** Every finite matrix corner of an infinite-star radius-one mask is either a finite-star mask with some number of leaves or a diagonal mask on leaves. Its Schur multiplier norm and completely bounded norm are at most \(5/3\). The same estimate therefore holds for the normal entrywise Schur multiplier, because its operator norm and each matrix amplification norm are determined by finite-support compressions. Conversely every finite \(n\)-leaf star is a corner, and its norm is \(\frac{5n-1}{3n+1}\to5/3\). Finally, trace duality yields the stated trace-class norm.

## Verification
The included standalone `CHECK.py` performs exact rational-arithmetic checks of both positive-semidefinite decompositions and the two-dimensional spectral characteristic equation at 26 sample sizes, including \(n=1,2,3,24,32,48\). Running `python3 CHECK.py` reports `PASS: 26 exact rational certificates; n=2 norm 9/7, limit 5/3`. The analytic proof covers every integer \(n\ge1\) and infinite leaf sets; the finite checks alone do not.

## Relationship to prior work
González-Pérez, Parcet, Pérez García, and Wang study radial Schur multipliers on trees for \(1<p<\infty\), emphasizing exceptional behavior at the endpoints. This theorem provides an exact endpoint value for the radius-one ball on a natural family of trees. Levene's classification already contains the \(n=2\) mask and its exact \(9/7\) norm (Proposition 5.1(8)); that case is a consistency check, **not a novelty claim**. His Remark 5.3 calculates a rectangular \([\mathbf1\ I_n]\) pattern, a different mask. The new contribution is the uniform formula for all \(n\ge3\), the sharp infinite-star value, and common explicit upper/lower certificates. Davidson and Donsig give general Schur-multiplier norm/factorization principles but not this specific star formula.

## Limitations
This is a result for star graph balls of radius one, not for every tree or larger radii. It does not determine intermediate Schatten-exponent norms, classifications of extremizers, or norms of arbitrary radial masks. The finite \(n=2\) case was previously known. An unlocated equivalent historical formula remains possible despite targeted comparison; no assertion of exhaustive literature priority is made.

## References
- A. González-Pérez, J. Parcet, J. Pérez García, and S. Wang, *Radial Schur multipliers on trees and the failure of Fourier-Schur transference*, arXiv:2610.15881v1, first posted 2026-10-11. https://arxiv.org/abs/2610.15881
- R. H. Levene, *Norms of idempotent Schur multipliers*, New York J. Math. 20 (2014), 325–352, Proposition 5.1(8) and Remark 5.3. https://nyjm.albany.edu/j/2014/20-19p.pdf
- K. R. Davidson and A. P. Donsig, *Norms of Schur Multipliers*, Theorem 1.1 (factorization criterion). https://www.math.uwaterloo.ca/~krdavids/Preprints/DavDon_schur.pdf
