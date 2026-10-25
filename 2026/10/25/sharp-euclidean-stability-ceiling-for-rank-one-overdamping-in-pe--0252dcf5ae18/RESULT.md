# Sharp Euclidean stability ceiling for rank-one overdamping in perturbed implicit midpoint

## Finding

Consider a linear dissipative system \(\dot{x}=-Ax\) with a symmetric positive-definite (SPD) matrix \(A\). In the perturbed implicit midpoint update, suppose the implicit stage uses a different SPD matrix \(B\), while the final slope uses the true \(A\):
\[
u=(I+hB/2)^{-1}x,\qquad x^+=x-hAu,\qquad h>0.
\]
For arbitrary SPD \(A,B\), set \(C_h=I+hB/2\), \(D=B-A\), and \(K=(AD+DA)/2\). Then the step map \(T_h=I-hAC_h^{-1}\) is Euclidean nonexpansive exactly when
\[
2A+hK\succeq0.
\]
Equivalently, if \(\lambda_-\) is the smallest eigenvalue of \(A^{-1/2}KA^{-1/2}\), all positive steps are nonexpansive when \(\lambda_-\ge0\), while for \(\lambda_-<0\) the **exact inclusive step ceiling** is \(h\le-2/\lambda_-\).

More strikingly, let the surrogate be a positive rank-one overdamping, \(B=A+vv^\mathsf{T}\), with any nonzero \(v\in\mathbb R^d\). Define
\[
s=v^\mathsf{T}v,\qquad \alpha=v^\mathsf{T}Av,\qquad \beta=v^\mathsf{T}A^{-1}v,
\qquad \delta=\sqrt{\alpha\beta}-s\ge0.
\]
For every dimension \(d\ge1\), the precise alternatives are:

* If \(Av\) is parallel to \(v\) (equivalently \(\delta=0\)), the step strictly decreases the Euclidean norm of every nonzero vector for **every** \(h>0\).
* If \(Av\) is not parallel to \(v\) (equivalently \(\delta>0\)), the sharp threshold is
\[
\boxed{h_*=\frac4{\sqrt{(v^\mathsf{T}Av)(v^\mathsf{T}A^{-1}v)}-\|v\|_2^2}}.
\]
For \(0<h<h_*\), the Euclidean operator norm satisfies \(\|T_h\|_2<1\). At \(h=h_*\), it is exactly one; for every \(h>h_*\), it exceeds one. Hence an SPD surrogate that is larger than the exact generator in Loewner order can still cause genuine one-step Euclidean amplification.

Nevertheless, **for every** \(h>0\), the eigenvalues of \(T_h\) lie strictly in \((-1,1)\), and \(T_h\) is a strict contraction in the weighted norm \(\|x\|_{A^{-1}}=(x^\mathsf{T}A^{-1}x)^{1/2}\). Thus the amplification is a transient norm phenomenon, not spectral instability or growth in the natural weighted energy.

## Assumptions and scope

All matrices and vectors are real and finite-dimensional. The true operator \(A=A^\mathsf{T}\succ0\); the surrogate \(B=B^\mathsf{T}\succ0\); the step \(h\) is a positive real number. The generic contractivity test applies to every such pair \(A,B\). The sharp scalar formula requires exactly \(B=A+vv^\mathsf{T}\) with \(v\ne0\). The midpoint *stage* uses \(-Bu\), while the end-stage *slope* uses \(-Au\); this differs from classical midpoint using \(-A\) at both places. No explicit correction steps are added. Norms concern all initial states simultaneously, not a fixed trajectory, and are exact-arithmetic statements.

## Proof

**1. Exact congruence test.** Because \(C_h\) is SPD, it is invertible. Put \(T_h=(C_h-hA)C_h^{-1}\). Transposition gives \(T_h^\mathsf{T}=C_h^{-1}(C_h-hA)\), so without assuming commutativity,
\[
\begin{aligned}
C_h(I-T_h^\mathsf{T}T_h)C_h
&=C_h^2-(C_h-hA)^2\\
&=h(C_hA+AC_h)-h^2A^2\\
&=h\{2A+h[(AB+BA)/2-A^2]\}\\
&=h(2A+hK).
\end{aligned}
\]
Congruence by an invertible SPD matrix preserves positive semidefiniteness. Thus \(T_h^\mathsf{T}T_h\preceq I\) is equivalent to \(2A+hK\succeq0\), with equality directions corresponding exactly. Congruence by \(A^{-1/2}\) yields \(2I+hS\succeq0\) for \(S=A^{-1/2}KA^{-1/2}\), proving the general spectral criterion, including its boundary.

**2. Rank-one spectrum and angular obstruction.** Put \(a=A^{1/2}v\) and \(b=A^{-1/2}v\). For \(D=vv^\mathsf{T}\),
\[
S=\tfrac12(ab^\mathsf{T}+ba^\mathsf{T}),
\quad a^\mathsf{T}b=s,
\quad\|a\|_2^2=\alpha,
\quad\|b\|_2^2=\beta.
\]
If \(a,b\) are linearly independent, their span is invariant, and the restriction of \(S\) has eigenvalues \((s+\sqrt{\alpha\beta})/2\) and \((s-\sqrt{\alpha\beta})/2\); all other eigenvalues, if any, are zero. To check the two eigenvalues directly, expand the restriction in the orthonormal basis starting with \(a/\|a\|_2\); the resulting symmetric two-by-two matrix has trace \(s\) and determinant \((s^2-\alpha\beta)/4\). Strict Cauchy–Schwarz gives \(s<\sqrt{\alpha\beta}\); its smaller eigenvalue is therefore \(-\delta/2\). Part 1 now gives \(2-h\delta/2\ge0\), i.e. \(h\le4/\delta\). At equality the congruence matrix has a zero eigenvalue, while for larger steps it has a negative direction, proving exact sharpness.

If \(a,b\) are linearly dependent, Cauchy–Schwarz gives \(\delta=0\) and \(S\succeq0\). The proportionality \(A^{1/2}v=cA^{-1/2}v\) is equivalent to \(Av=cv\) for some positive \(c\). Thus the all-step case is exactly eigenvector alignment. For every \(0<h<h_*\) in the nonaligned case and every finite \(h>0\) in the aligned case, \(2I+hS\succ0\); hence strict Euclidean contraction follows. In the exceptional one-dimensional case all nonzero \(v\) are automatically aligned, so the same conclusion holds without introducing a nonexistent second eigenvalue.

**3. Stable spectrum despite one-step amplification.** Since \(B=A+vv^\mathsf{T}\succeq A\succ0\),
\[
0\prec hA\preceq hB\prec 2C_h=2I+hB.
\]
Consequently all eigenvalues of \(hC_h^{-1/2}AC_h^{-1/2}\) lie strictly in \((0,2)\). As \(T_h=C_h^{1/2}(I-hC_h^{-1/2}AC_h^{-1/2})C_h^{-1/2}\), all eigenvalues of \(T_h\) lie in \((-1,1)\). Thus \(T_h^n\to0\) for every fixed \(h>0\), even when \(\|T_h\|_2>1\).

**4. Weighted energy.** Direct expansion, again requiring no commutativity, gives
\[
C_h(A^{-1}-T_h^\mathsf{T}A^{-1}T_h)C_h
=h(2I+h(B-A)).
\]
For \(B=A+vv^\mathsf{T}\), the right side is SPD for every \(h>0\). It follows that \(\|T_hx\|_{A^{-1}}<\|x\|_{A^{-1}}\) for every nonzero \(x\). More generally, for arbitrary SPD \(B\), weighted nonexpansivity holds exactly when \(2I+h(B-A)\succeq0\), and this criterion is sharp.

**5. Smallest explicit rational witness.** Choose
\[
A=\begin{pmatrix}1&0\\0&4\end{pmatrix},\quad
v=\begin{pmatrix}1\\1\end{pmatrix},\quad
B=\begin{pmatrix}2&1\\1&5\end{pmatrix}.
\]
Here \(s=2\), \(\alpha=5\), \(\beta=5/4\), so \(\delta=1/2\) and \(h_*=8\). At \(h=8\) take \(w=(1,-1/2)^\mathsf{T}\), \(x=C_hw=(7,-13/2)^\mathsf{T}\); its update is \((-1,19/2)^\mathsf{T}\), with exactly equal squared Euclidean norm \(365/4\). At \(h=16\), the same \(w\) gives \(x=(13,-25/2)^\mathsf{T}\) and \(T_hx=(-3,39/2)^\mathsf{T}\). Therefore
\[
\frac{\|T_hx\|_2^2}{\|x\|_2^2}=\frac{1557}{1301}>1.
\]
No one-dimensional example can show this effect, because rank-one overdamping commutes with a scalar \(A\).

## Verification

The attached standalone `checker.py` uses only Python's standard library (`fractions`, `itertools`, `math`) and can be run as `python3 checker.py`. It performs 1,792 exact-rational two-dimensional tests of both congruence identities and the rank-one sign prediction, including noncommuting SPD matrices. It also reproduces both equality and strict-amplification witnesses exactly. Finite tests do not establish the full-dimensional or all-step claims: those conclusions follow from the algebra in the Proof section.

## Relationship to prior work

Driscoll, Gottlieb, Grant, Herrera, Kakumanu, Sawicki, and Stephens [1] formulate the perturbed implicit midpoint stage/end update in their equations (10a–b), and study perturbation-error bounds and stable corrections. The exact Euclidean one-step contractivity ceiling for a rank-one SPD stage perturbation is not stated in the analyzed sections or results of [1]. Driscoll and coauthors [2] study smooth perturbations and high-order DIRK methods under local consistency conditions; their stability/error analysis addresses a different question, not this exact rank-one norm criterion. Grant [3] provides the foundational mixed-precision framework. Classical B-stability of the unperturbed Runge–Kutta method [4] does not apply without modification when the implicit stage and end-stage derivative use two different generators.

The general algebraic test uses elementary congruence and the Jordan product of SPD matrices. Those ingredients and the fact that SPD Jordan products need not be positive are not asserted to be new. The specific substantive classification is the sharp scalar frontier for every rank-one overdamping direction, the exact eigenvector-alignment exception, and the simultaneous all-step weighted contraction and spectral stability. No claim is made for general implicit Runge–Kutta methods, nonlinear systems or high-order corrected methods.

## Limitations

The model represents a *fixed linear surrogate* at each implicit stage; it does not model random roundoff, changing operators, inexact solves controlled only by residual tolerances, or nonlinear dependence. The step map is generally not second-order accurate for fixed \(B\ne A\) as \(h\to0\), despite using the midpoint tableau: the source's additional consistency conditions are not assumed. Spectral stability for a fixed matrix does not control arbitrary products of matrices with varying \(h\) or varying \(B\). The Euclidean threshold concerns one-step operator norm, not energy in a physical mass matrix or long-time uniform bounds under parameter variation. Earlier operator-norm literature might contain an equivalent formulation; bibliographic priority beyond the inspected sources is not certified.

## References

[1] J. Driscoll, S. Gottlieb, Z. J. Grant, C. Herrera, T. S. Kakumanu, M. H. Sawicki, M. Stephens, *Stable corrections for perturbed diagonally implicit Runge–Kutta methods*, arXiv:2603.24451v1, 25 March 2026. https://arxiv.org/html/2603.24451v1

[2] J. Driscoll, S. Gottlieb, Z. J. Grant, C. Herrera, T. S. Kakumanu, M. Stephens, *Smooth perturbations of diagonally implicit Runge–Kutta methods*, arXiv:2604.14479, April 2026. https://arxiv.org/pdf/2604.14479

[3] Z. J. Grant, *Perturbed Runge–Kutta methods for mixed precision applications*, J. Sci. Comput. 92 (2022), arXiv:2012.13055. https://arxiv.org/abs/2012.13055

[4] M. Crouzeix, *Sur la B-stabilité des méthodes de Runge–Kutta*, Numer. Math. 32 (1979), 75–82.
