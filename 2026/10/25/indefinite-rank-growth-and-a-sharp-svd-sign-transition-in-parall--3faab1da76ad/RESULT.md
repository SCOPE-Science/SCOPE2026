# Indefinite rank growth and a sharp SVD sign transition in parallel low-rank integration

## Finding

Consider the parallel rank-adaptive basis-update method of Ceruti, Kusch, and Lubich (2023), with its three reduced subproblems integrated exactly and its block augmentation and singular-value truncation as specified in their Section 3.1. There are two related structural conclusions.

**Inertia of symmetric rank augmentation.** Start at a real symmetric positive matrix of rank \(r\), represented as \(Y_0=U_0S_0U_0^\top\) with \(S_0\succ0\). Assume the vector field is transpose-equivariant, and use identical orthonormal bases for the identical left and right augmented spaces. If the new basis contributes \(s\ge1\) independent directions and the old-old stage coefficient \(B\) is positive definite, then the *untruncated* augmented update has precisely \(r\) positive and \(s\) negative eigenvalues (plus any zero eigenvalues due to padding). In particular, nontrivial symmetric rank enlargement by this augmentation cannot preserve positive semidefiniteness.

**Exact rank-two truncation transition.** For every \(\gamma>0\), set
\[
G_\gamma=\begin{pmatrix}1&0&\gamma\\0&1&0\\\gamma&0&1+\gamma^2\end{pmatrix},\qquad
Y_0=\operatorname{diag}(1,1,0),\qquad \dot Y=G_\gamma-Y.
\]
The exact solution is positive definite at every \(h>0\). Put \(q=1-e^{-h}\), \(p=\gamma q\), and
\[
d=\frac{\sqrt{1+4p^2}-1}{2}.
\]
The untruncated parallel update is \(H=\begin{psmallmatrix}1&0&p\\0&1&0\\p&0&0\end{psmallmatrix}\), with eigenvalues \(1+d,1,-d\). Its *best rank-two Frobenius approximation obtained by the method's SVD* is positive semidefinite when \(p<\sqrt2\), but indefinite when \(p>\sqrt2\). The crossing \(p=\sqrt2\) has tied singular values and the rank-two SVD is not unique. For \(\gamma>\sqrt2\), the sharp transition occurs at
\[
h_*(\gamma)=-\log\left(1-\frac{\sqrt2}{\gamma}\right);
\]
for \(0<\gamma\le\sqrt2\), no finite positive step reaches the transition.

The negative-sign regime can pass the method's stated step-rejection tests: at \(\gamma=2\), \(h=3/2\), rank-truncation tolerance \(\vartheta=6/5\), and rejection multiplier \(c=10\), the algorithm selects rank two, produces a negative eigenvalue \(-d\), and rejects neither on full-rank growth nor on the normal-component criterion. Scaling both \(G_\gamma\) and \(Y_0\), and scaling \(\vartheta\) by the same positive factor, gives the same phenomenon at arbitrarily small *absolute* tolerances.

## Assumptions and scope

All matrices are real, all reduced differential equations are solved exactly, and the SVD and basis construction use exact arithmetic. For the inertia statement, the vector field satisfies \(F(t,X^\top)=F(t,X)^\top\), the initial factorization is symmetric, and corresponding left/right basis choices agree. Let \(s\) denote the dimension of the newly generated orthogonal subspace, not zero-filled basis columns. The old-old reduced coefficient \(B\in\mathbb R^{r\times r}\) is assumed positive definite. No claim is made for asymmetric basis choices or indefinite \(B\).

For the explicit example, \(G_\gamma\succ0\), the flow \(F(Y)=G_\gamma-Y\) is globally one-Lipschitz in Frobenius norm and is the gradient flow of \(\frac12\|Y-G_\gamma\|_F^2\). It preserves the positive-semidefinite cone. Rank-two SVD outcomes are characterized only away from the tied-singular-value boundary. Step rejection uses exactly the two optional criteria in Section 3.3 of the 2023 reference; the concrete example uses its illustrated multiplier \(c=10\).

## Proof

**1. Block inertia.** Exact transpose equivariance implies equality of the reduced left and right \(K\)- and \(L\)-step solutions. Denote their common terminal matrix by \(K_1\). If \(\widetilde U\) is an orthonormal basis for the part of the range of \(K_1\) orthogonal to \(\operatorname{Ran}(U_0)\), the source algorithm's augmented coefficient is
\[
H=\begin{pmatrix}B&C^\top\\C&0\end{pmatrix},\qquad C=\widetilde U^\top K_1.
\]
Because \(\widetilde U\) spans the projected terminal range, \(C\) has full row rank \(s\). For \(B\succ0\), block Gaussian congruence transforms \(H\) into \(\operatorname{diag}(B,-CB^{-1}C^\top)\). The second block is strictly negative definite of size \(s\). Sylvester's law of inertia gives exactly \(r\) positive and \(s\) negative eigenvalues. Any zero-filled augmentation columns contribute only additional zero eigenvalues. This proves the structural statement.

**2. Positive exact flow and reduced substeps.** Write
\[
G_\gamma=L_\gamma L_\gamma^\top,\qquad
L_\gamma=\begin{pmatrix}1&0&0\\0&1&0\\\gamma&0&1\end{pmatrix}.
\]
Thus \(G_\gamma\succ0\). The exact flow is
\[
Y(h)=e^{-h}Y_0+(1-e^{-h})G_\gamma\succ0\quad(h>0).
\]
Take \(U_0=V_0=(e_1,e_2)\) and \(S_0=I_2\). The reduced basis equations in the source are \(\dot K=G_\gamma U_0-K\) and \(\dot L=G_\gamma U_0-L\). Hence
\[
K(h)=L(h)=\begin{pmatrix}1&0\\0&1\\\gamma q&0\end{pmatrix}.
\]
For every \(h>0\), the new direction is \(e_3\). The reduced old-old coefficient solves \(\dot B=I_2-B\) from \(I_2\), so \(B=I_2\). The new-old coefficient is \((p,0)\), giving exactly
\[
H=\begin{pmatrix}1&0&p\\0&1&0\\p&0&0\end{pmatrix}.
\]
This is the nonzero part of the possibly zero-padded augmented coefficient.

**3. Singular-value ordering.** The vector \(e_2\) is an eigenvector of eigenvalue \(1\). The remaining \(2\times2\) block has eigenvalues \(1+d\) and \(-d\), since \(d(d+1)=p^2\). Its singular values, including the \(e_2\) direction, are \(1+d\), \(1\), and \(d\). The first is always largest. If \(d<1\), the rank-two SVD retains the two positive eigendirections, and if \(d>1\), it retains the positive \(1+d\) direction and the negative \(-d\) direction. The equality \(d=1\) is equivalent to \(p=\sqrt2\); a singular-value tie makes the outcome nonunique. Since \(p=\gamma(1-e^{-h})\) grows strictly from zero to \(\gamma\), solving \(p=\sqrt2\) proves the unique finite threshold exactly when \(\gamma>\sqrt2\).

**4. Accepted negative-eigenvalue step.** Set \(\gamma=2\), \(h=3/2\). The inequality \(e^{3/2}>2+\sqrt2\) (for instance from the first four positive terms of its Taylor series) implies \(p=2(1-e^{-3/2})>\sqrt2\), hence \(d>1\). The ordered nonzero singular values are therefore \(1+d,d,1\). With \(\vartheta=6/5\), the rank-one discarded Frobenius norm is \(\sqrt{1+d^2}>\sqrt2>\vartheta\), whereas the rank-two discarded norm is \(1<\vartheta\). The minimal accepted rank is two and its negative eigenvalue is \(-d\). Here the source's normal-component diagnostic equals
\[
\eta=|e_3^\top F(Y_0)e_3|=\gamma^2+1=5.
\]
The rank does not reach the maximal doubled rank, and \(h\eta=15/2<10\vartheta=12\). Neither stated rejection criterion is triggered. Multiplication of the whole matrix evolution and the tolerance by any common positive scalar preserves the rank choice and rejection inequalities and scales the negative eigenvalue accordingly.

## Verification

The standalone `verify.py` uses only NumPy and the exact reduced-step formulas above. It compares the predicted eigenvalues with independent symmetric eigensolvers over \(25\) parameter pairs, checks the two possible rank-two SVD sign regimes and exact truncation-error expressions, checks positive definiteness of the exact flow, and replays the strict rejection and singular-value comparisons for the concrete witness. Executing `python verify.py` with `requirements.txt` installed returns `VERIFY_OK 132`. These finite checks support the algebra; the all-parameter statements, inertia counts, and unique threshold follow from the preceding proof rather than sampling.

## Relationship to prior work

The parallel augmentation and its deliberately omitted lower-right block are due to Ceruti, Kusch, and Lubich (2023), their equations (6)--(10). Their Section 3.3 gives the two rejection tests. The source already notes that this parallel method loses some exactness and energy-preservation properties of the earlier serial BUG method; the present finding does not claim those qualitative observations as new. The added statement is the **exact inertia obstruction for every symmetric expanding step with positive old-old block**, together with the **sharp rank-two SVD sign ordering** and an explicit *nonrejected* negative-semidefinite-cone violation in a positive gradient flow.

The 2021 rank-adaptive BUG work uses an augmented Galerkin coefficient update instead of setting the new-new block identically to zero, so its structure-preservation results do not imply the sign threshold for the parallel method. Positive low-rank covariance propagation in Schmidt and coauthors (2023) uses a different factorized projection strategy. The Kraus-based positive low-rank method of Appelö and Cheng (2024) concerns Lindblad equations and supplies an alternative positivity-preserving construction, not a classification of the present parallel augmentation. The block-inertia congruence and standard SVD truncation are classical linear algebra; no novelty is claimed for them in isolation.

## Limitations

This is an exact one-step analysis. It does not assert instability, negative outputs after any required repeated step, or failure of other low-rank integrators. The generic inertia statement requires transpose-equivariant dynamics, matched symmetric bases, positive definite old-old coefficient, and a genuine new basis direction. The explicit sharp SVD transition is for the displayed three-dimensional family; it is not a universal parameter threshold for arbitrary positive matrix dynamics. At the equality threshold, a tied singular subspace makes the rank-two result nonunique. Finite numerical tests do not certify the analytical conclusions independently. Other choices of rejection multiplier and tolerance may repeat a step or truncate to another rank.

## References

1. G. Ceruti, J. Kusch, and C. Lubich, *A parallel rank-adaptive integrator for dynamical low-rank approximation*, arXiv:2304.05660, first submitted 2023-04-12, especially Sections 3.1--3.3 and equation (9). https://arxiv.org/html/2304.05660v1
2. G. Ceruti, J. Kusch, and C. Lubich, *A rank-adaptive robust integrator for dynamical low-rank approximation*, arXiv:2104.05247, first submitted 2021-04-12. https://arxiv.org/html/2104.05247v1
3. J. Schmidt, P. Hennig, J. Nick, and F. Tronarp, *The Rank-Reduced Kalman Filter: Approximate Dynamical-Low-Rank Filtering In High Dimensions*, arXiv:2306.07774, first submitted 2023-06-13. https://arxiv.org/abs/2306.07774
4. D. Appelö and Y. Cheng, *Kraus is King: High-order Completely Positive and Trace Preserving Low Rank Method for the Lindblad Master Equation*, arXiv:2409.08898, first submitted 2024-09-13. https://arxiv.org/abs/2409.08898
