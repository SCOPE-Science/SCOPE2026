# Sharp third-order stabilization criterion for prescribed Lotka–Volterra coexistence

## Finding

**Theorem (exact third-order design criterion).** Fix an integer \(n\ge1\), a desired strictly positive equilibrium \(z=(z_1,\ldots,z_n)\in(0,\infty)^n\), growth rates \(r\in\mathbb R^n\), and arbitrary prescribed pairwise coefficients \(S\in\mathbb R^{n\times n}\). In the higher-order Lotka–Volterra family
\[
\dot x_i=x_i\left(r_i+\sum_{j=1}^n S_{ij}x_j+\sum_{j,k=1}^n T_{ijk}x_jx_k\right),\qquad 1\le i\le n,
\]
allow any real, partner-symmetric third-order tensor \(T_{ijk}=T_{ikj}\), including repeated indices. Define
\[
h_i=2r_i+\sum_{j=1}^n S_{ij}z_j.
\]
There exists such a tensor \(T\) making \(z\) an equilibrium whose Jacobian is **Hurwitz** (every eigenvalue has strictly negative real part) **if and only if**
\[
\boxed{\text{either the entries of }h\text{ are not all equal, or }h=c\mathbf 1\text{ with }c>0.}
\]
Equivalently, third-order stabilization is impossible precisely when \(h=c\mathbf1\) for a common \(c\le0\). When the entries of \(h\) differ, a completely explicit construction uses only terms \(T_{ijj}x_j^2\) and gives a Jacobian with every eigenvalue equal to \(-1\); when \(h=c\mathbf1\) with \(c>0\), the construction gives a Jacobian with every eigenvalue equal to \(-c\).

This exactly identifies which **prescribed** growth-rate/pairwise-coefficient/abundance data admit linearly stable coexistence using at most three-body interactions. The previously established fourth-order universal existence theorem then shows that the excluded class requires order four if the target equilibrium is required to be Hurwitz. The result is not a claim of global attraction.

## Assumptions and scope

The sign convention is additive: \(S_{ij}\) is the coefficient of \(x_j\) in the per-capita growth of species \(i\). The pairwise coefficients \(r,S\) and target \(z\) are fixed; only the third-order coefficients are free. The new coefficients can have either sign and need not obey ecological sign, sparsity, magnitude, or distinct-partner constraints. A third-order interaction here is one involving the focal species and two (not necessarily distinct) partner indices; allowing repeated partner indices is explicit in the motivating higher-order model [1, Section 4, equation (3)]. The assertion concerns a **strictly Hurwitz linearization**, which implies local asymptotic stability. It does not rule out nonlinear attraction when an eigenvalue is zero.

## Proof

**Step 1: Normalize the prescribed equilibrium.** Put \(D=\operatorname{diag}(z_1,\ldots,z_n)\), \(y=D^{-1}x\), and \(B_{ij}=S_{ij}z_j\). Under this positive diagonal change of coordinates the dynamics is
\[
\dot y_i=y_i\bigl(r_i+\sum_j B_{ij}y_j+Q_i(y)\bigr),
\]
where \(Q_i\) is an arbitrary homogeneous quadratic polynomial determined by the third-order tensor. Let \(J\) denote the Jacobian of the normalized \(y\)-flow at \(\mathbf1\), assuming \(\mathbf1\) is an equilibrium. Differentiating at an equilibrium yields
\[
J_{ij}=B_{ij}+\partial_jQ_i(\mathbf1),\qquad
Q_i(\mathbf1)=-r_i-\sum_j B_{ij}.
\]
By Euler's identity for degree-two homogeneous polynomials,
\[
\sum_j\partial_jQ_i(\mathbf1)=2Q_i(\mathbf1).
\]
Consequently **every** permissible completion has the forced row sums
\[
J\mathbf1=s,\qquad s_i=-2r_i-\sum_jB_{ij}=-h_i.\tag{1}
\]
Conversely, **every real matrix** \(J\) with \(J\mathbf1=s\) is attainable as the exact normalized Jacobian: define
\[
C_{ij}=J_{ij}-B_{ij},\quad Q_i(y)=\tfrac12\sum_{j=1}^n C_{ij}y_j^2,\quad
T_{ijj}=\frac{C_{ij}}{2z_j^2},\quad T_{ijk}=0\ (j\ne k).\tag{2}
\]
Indeed the row-sum condition gives
\[
Q_i(\mathbf1)=\tfrac12(s_i-\sum_j B_{ij})=-r_i-\sum_jB_{ij},
\]
and \(\partial_jQ_i(\mathbf1)=C_{ij}\). Thus the prescribed equilibrium equation and its complete first derivative hold. In original \(x\)-coordinates the Jacobian is \(DJD^{-1}\), so has the same spectrum as \(J\).

**Step 2: Classify Hurwitz matrices with specified row sums.** If \(s=c\mathbf1\) with \(c\ge0\), then equation (1) makes \(c\) a real eigenvalue of every permissible \(J\); Hurwitz stability is impossible. If \(s=c\mathbf1\) with \(c<0\), choose \(J=cI\), which is Hurwitz and has the required row sums.

Suppose instead that \(s\) is nonconstant (necessarily \(n\ge2\)). The two vectors \(\mathbf1,s\) are linearly independent. Hence there exists a real row vector \(u^\top\) with
\[
u^\top\mathbf1=1,\qquad u^\top s=-1.
\]
For example, select coordinates \(p,q\) with \(s_p\ne s_q\), set all other entries of \(u\) to zero, and solve these two scalar equations. Define
\[
J=-I+(s+\mathbf1)u^\top.\tag{3}
\]
Then \(J\mathbf1=-\mathbf1+(s+\mathbf1)=s\). Moreover, the rank-one matrix \(N=(s+\mathbf1)u^\top\) satisfies
\[
N^2=(s+\mathbf1)(u^\top s+u^\top\mathbf1)u^\top=0.
\]
Therefore all eigenvalues of \(J=-I+N\) equal \(-1\), and it is Hurwitz. Equation (2) realizes this \(J\) with an explicitly specified third-order tensor.

**Step 3: Translate the criterion.** The sole forbidden case \(s=c\mathbf1\) with \(c\ge0\) is identical to \(h=-c\mathbf1\) with common value \(-c\le0\), establishing the assertion in both directions and for every \(n\ge1\). The positive orthant is forward-invariant locally because every equation contains the corresponding positive coordinate as a factor. Strictly negative Jacobian real parts imply local asymptotic stability at \(z\).

**Sharp example (two species).** Set \(z=(1,1)\) and fix \(S=-I_2\). With \(r=(-1,-2)\), the resulting \(h=(-3,-5)\) is nonconstant. The construction gives
\[
J=\begin{pmatrix}11&-8\\18&-13\end{pmatrix},\quad
Q_1(y)=6y_1^2-4y_2^2,\quad Q_2(y)=9y_1^2-6y_2^2.
\]
At the prescribed equilibrium, \(\operatorname{tr}(J)=-2\), \(\det(J)=1\), and both eigenvalues are \(-1\). Notice that all fixed intrinsic growth rates are negative and the pairwise model alone cannot admit a positive equilibrium.

For the **same** fixed pairwise matrix but \(r=(-1,-1)\), now \(h=(-3,-3)\), so no third-order tensor can make \(z=(1,1)\) Hurwitz. Fourth order does suffice: independently for \(i=1,2\), set
\[
\dot x_i=x_i(-1-x_i+6x_i^2-4x_i^3).
\]
Its per-capita factor vanishes at \(x_i=1\) and has derivative \(-1\) there; hence the equilibrium \((1,1)\) has Jacobian \(-I_2\). The example demonstrates that the third/fourth-order distinction is genuine, even with ordinary competitive self-interaction at the pairwise level.

## Verification

The standalone `verify.py` uses exact rational arithmetic and the fixed random seed `20261018`. Run `python3 verify.py` in the directory containing this document. It checks the equilibrium equations, direct-coordinate Jacobian similarity, necessary row sums, the explicit rank-one nilpotent identity, and the sharp two-species examples in 1,190 finite rational parameter instances, across dimensions \(1\) through \(7\). Its expected terminal line begins `EXACT_REPLAY_OK`. These finite computations are not a substitute for Steps 1–3, which prove the theorem for **all** dimensions and real coefficients.

## Relationship to prior work

Çelik, Isoldi, Portakal and Zucal [1, Theorem 4.2] construct second- and third-degree *per-capita* polynomial terms to stabilize every prescribed pairwise system at the all-ones equilibrium, thus using fourth-order ecological interactions. They also give a third-order instance [1, Example 4.1]. Neither statement classifies exactly which fixed data can be stabilized by third-order terms alone. The present theorem proves that third-order suffices off one explicit constant-vector obstruction, supplies its necessary and sufficient boundary, accommodates arbitrary positive targets, and demonstrates a case where fourth order is necessary for Hurwitz stability.

Gibbs and collaborators [2] study prescribed equilibrium abundances with third-order interactions and how correlations with fixed pairwise coefficients affect local stability. Their main full text analyzes constrained/random ensembles and sufficient stabilizing patterns, rather than an all-coefficient necessity-and-sufficiency criterion for the third-order existence problem. Their supplementary material was not fully accessible in this review, so possible stronger coverage there remains a priority risk. Duran-Sala, Meloni and Calleja-Solanas [3] address stability in competition models with pairwise and higher-order interactions; the accessible abstract does not establish or refute the unrestricted exact design criterion, and that source was not used for a full-text exclusion conclusion. An independent literature audit is still needed for historical priority.

## Limitations

This is a theorem about **existence of some tailored higher-order coefficients**, not a claim that random or biologically realizable interactions are stabilizing. The construction can use large coefficients when the row-sum vector approaches the constant-vector obstruction. It allows terms with a repeated partner index and arbitrary real signs; imposing distinct partners, nonnegativity, tensor structure, or conservation laws may change the answer. Strict Hurwitz stability is stronger than nonlinear local attraction at a nonhyperbolic equilibrium, which is deliberately not classified. Nor does local stability imply global attractivity or exclude other equilibria. The theorem is a mathematical design classification, not empirical evidence for any particular ecosystem.

## References

[1] T. Ö. Çelik, V. A. Isoldi, I. Portakal, and G. Zucal, *Stable Coexistence in Ecologies and Games*, arXiv:2609.09286, initial public version 2026-09-08. https://arxiv.org/abs/2609.09286 . Particularly Sections 4 and 4.1, Example 4.1, Theorem 4.2 and equation (3).

[2] T. L. Gibbs, G. Gellner, S. A. Levin, K. S. McCann, A. Hastings, and J. M. Levine, *When can higher-order interactions produce stable coexistence?*, Ecology Letters 27 (2024), e14458, DOI:10.1111/ele.14458. https://onlinelibrary.wiley.com/doi/10.1111/ele.14458 . Particularly Model form and Question 3.

[3] M. Duran-Sala, S. Meloni, and V. Calleja-Solanas, *On the stability of competitive ecological communities with pairwise and higher-order interactions*, arXiv:2501.09172, initial public version 2025-01-15. https://arxiv.org/abs/2501.09172 . Abstract reviewed; not relied on for whole-document absence.
