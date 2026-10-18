# Exact active-spectrum rank and pole budget for rank-one matrix-function updates

## Finding
Let \(A\in\mathbb R^{n\times n}\) be symmetric positive definite, let \(u\in\mathbb R^n\setminus\{0\}\), and take any nonzero real \(\tau\) for which \(B=A+\tau uu^{\mathsf T}\) remains positive definite. For every distinct eigenvalue \(\lambda\) of \(A\), denote its orthogonal spectral projector by \(P_\lambda\). Define the **active spectral grade**
\[
 r=\#\{\lambda:P_\lambda u\ne0\},\qquad
 \mathcal K=\operatorname{span}\{P_\lambda u:P_\lambda u\ne0\}.
\]
In particular, \(r=\dim\mathcal K=\dim\operatorname{span}\{u,Au,A^2u,\ldots\}\), with repeated eigenvalues counted only once.

**Theorem (positive-residue pole budget).** For any integer \(m\ge0\), distinct positive shifts \(t_1,\ldots,t_m\), strictly positive coefficients \(c_1,\ldots,c_m\), any real \(a\), and \(b\ge0\), set
\[
 f(x)=a+bx+\sum_{j=1}^{m}c_j\frac{x}{x+t_j},\qquad
 \delta=\begin{cases}1,&b>0,\\0,&b=0.\end{cases}
\]
Then
\[
 \boxed{\operatorname{rank}(f(B)-f(A))=\min\{r,m+\delta\}},
 \qquad \frac{f(B)-f(A)}{\tau}\succeq0,
\]
and the correction has range contained in \(\mathcal K\). The zero-pole, zero-linear-term case is allowed and gives the zero correction.

**Theorem (fractional-power saturation).** For each \(0<p<1\),
\[
 \boxed{\operatorname{rank}(B^p-A^p)=
 \operatorname{rank}(B^{-p}-A^{-p})=r}.
\]
The correction \((B^p-A^p)/\tau\) is strictly positive definite on \(\mathcal K\), and \((B^{-p}-A^{-p})/\tau\) is strictly negative definite there; both vanish on \(\mathcal K^\perp\). In contrast, both first-power and inverse-first-power corrections have rank exactly one. For simple-spectrum \(A\) and \(u\) nonorthogonal to every eigenvector, \(r=n\): the square-root and inverse-square-root corrections are exactly full rank although \(B-A\) has rank one.

## Assumptions and scope
Matrices are real, finite dimensional, symmetric and strictly positive definite, and powers are their principal spectral powers. Both positive updates and strictly admissible negative downdates are covered. All shifts and pole residues are positive and shifts are pairwise distinct. The formula concerns **exact algebraic rank**; it is not a statement about numerical rank at any nonzero tolerance. The affine coefficient \(a\) cancels from every difference. The use of \(\mathcal K\) is intrinsic: it depends only on which eigenspaces meet the update direction.

## Proof
**1. Exact resolvent identity.** For any \(t>0\), put \(v_t=(A+tI)^{-1}u\) and \(s_t=u^{\mathsf T}(A+tI)^{-1}u\). The Sherman–Morrison formula gives
\[
 (B+tI)^{-1}-(A+tI)^{-1}
 =-\frac{\tau}{1+\tau s_t}v_t v_t^{\mathsf T}.
\]
The denominator is strictly positive: this is immediate for \(\tau>0\), while for \(\tau<0\) the positive-definite downdate condition gives \(1+\tau u^{\mathsf T}A^{-1}u>0\), and \(s_t<u^{\mathsf T}A^{-1}u\). Since \(x/(x+t)=1-t/(x+t)\), subtraction yields the exact factorization
\[
 \frac{f(B)-f(A)}{\tau}
 =buu^{\mathsf T}+\sum_{j=1}^{m}
 \frac{c_jt_j}{1+\tau s_{t_j}}\,v_{t_j}v_{t_j}^{\mathsf T}.
 \tag{1}
\]
All nonzero scalar coefficients on the right are positive, so its range equals the span of the displayed vectors; no cancellation can lower the rank.

**2. Sharp rank by a Cauchy matrix.** List the \(r\) active eigenvalues as \(\lambda_1,\ldots,\lambda_r\), and normalize the mutually orthogonal nonzero vectors \(P_{\lambda_i}u\). In that orthonormal coordinate system, the components of \(v_{t_j}\) are nonzero row scalings of \(1/(\lambda_i+t_j)\), and those of \(u\) are nonzero row scalings of \(1\). The Cauchy matrix with entries \(1/(\lambda_i+t_j)\) has every square submatrix nonsingular because the \(\lambda_i\) and \(t_j\) are separately pairwise distinct. Adjoining the constant column also preserves nonsingularity of every square minor: a nontrivial linear combination of \(k-1\) shifted reciprocals and one constant becomes, after multiplying denominators, a polynomial of degree at most \(k-1\), which cannot vanish at \(k\) distinct \(\lambda_i\). Thus the displayed columns in (1) have rank exactly \(\min\{r,m+\delta\}\), proving the first theorem.

**3. Fractional powers as positive continua of resolvents.** For \(0<p<1\), the scalar Stieltjes identities, valid for all positive arguments, are
\[
 x^p=\frac{\sin(\pi p)}\pi\int_0^\infty
 t^{p-1}\frac{x}{x+t}\,dt,
 \qquad
 x^{-p}=\frac{\sin(\pi p)}\pi\int_0^\infty
 t^{-p}\frac1{x+t}\,dt.
\]
Applying the spectral calculus and the identity from step 1 gives convergent matrix integrals
\[
 \frac{B^p-A^p}{\tau}=
 \frac{\sin(\pi p)}\pi\int_0^\infty
 \frac{t^p\,v_tv_t^{\mathsf T}}{1+\tau s_t}\,dt,
 \quad
 -\frac{B^{-p}-A^{-p}}\tau=
 \frac{\sin(\pi p)}\pi\int_0^\infty
 \frac{t^{-p}\,v_tv_t^{\mathsf T}}{1+\tau s_t}\,dt.
 \tag{2}
\]
The integrands are positive semidefinite and have range in \(\mathcal K\). For \(w\in\mathcal K\setminus\{0\}\),
\[
 w^{\mathsf T}v_t
 =\sum_{i=1}^r\frac{w^{\mathsf T}P_{\lambda_i}u}{\lambda_i+t}
\]
is a nonzero rational function: partial-fraction uniqueness and the fact that the nonzero vectors \(P_{\lambda_i}u\) form an orthogonal basis of \(\mathcal K\) prevent it from vanishing identically. Hence its square is strictly positive except at finitely many positive \(t\). The positive weights in (2) imply strict quadratic-form positivity on \(\mathcal K\). Every vector in \(\mathcal K^\perp\) is annihilated. This proves both exact ranks and sign assertions.

**4. Endpoint and full-rank boundary.** At \(p=1\), \(B-A=\tau uu^{\mathsf T}\). For the inverse first power, Sherman–Morrison at \(t=0\) yields \(B^{-1}-A^{-1}=-\tau A^{-1}uu^{\mathsf T}A^{-1}/(1+\tau u^{\mathsf T}A^{-1}u)\), also rank one. The fractional formula therefore has a genuine rank discontinuity at the exponent endpoint whenever \(r>1\). Choosing \(A\) with simple positive eigenvalues and \(u\) with every eigenvector component nonzero makes \(r=n\), establishing the full-rank example for every dimension.

## Verification
The accompanying standalone script `verify_rank.py` rechecks the Sherman–Morrison factorization, rational-function rank identities for several pole budgets and both admissible update signs, and the spectral signs and nullity of fractional positive and inverse-power corrections. On the supplied deterministic examples it reports 27 exact rational/symbolic checks and 54 high-precision matrix-power checks. These finite calculations check implementation and representative boundary cases; the universal claims follow from steps 1–4, not from an enumeration or numerical rank threshold. Reproduce with `python verify_rank.py` using Python with SymPy and mpmath installed.

## Relationship to prior work
Shmueli–Drineas–Avron analyze **rapid decay and numerical low-rank approximation** of square-root and inverse-square-root updates and describe exact corrections as generally full rank; they do not state the active-spectral-grade equality or positive-residue pole-budget saturation. Beckermann–Cortinovis–Kressner–Schweitzer and the earlier work of Bernstein–Van Loan already establish **rational update formulas, Krylov exactness, and general degree-dependent rank upper bounds**. Those bounds are acknowledged: (1) gives a sharp *equality* under positivity of the residues and identifies the independent cap from the active eigenspace. Fasi–Higham–Liu provide exact low-rank principal roots when the unperturbed matrix is a scaled identity, which is the grade-one special case here. The present statement does not claim the classical resolvent formula, Stieltjes integral, Cauchy determinant, or generic rational upper bound as new.

## Limitations
The fractional equality concerns finite real SPD matrices and nonzero rank-one updates preserving positive definiteness. It need not hold without the stated sign structure or for arbitrary nonnormal matrices. Rational saturation requires positive residues; arbitrary signed rational coefficients can cancel. Full algebraic rank does **not** contradict small approximation error with low numerical rank, and the pole count is a necessary obstruction to exact recovery only within the specified rational family, not a universal lower bound on all approximation schemes. Earlier rational matrix-function literature may contain an unlocated equivalent specialization; no independent publication-priority audit has been performed.

## References
1. S. Shmueli, P. Drineas, H. Avron, *Low-Rank Updates of Matrix Square Roots*, arXiv:2201.13156 (first public 2022-01-31); https://arxiv.org/abs/2201.13156 ; published in *Numerical Linear Algebra with Applications*, DOI:10.1002/nla.2528.
2. B. Beckermann, A. Cortinovis, D. Kressner, M. Schweitzer, *Low-Rank Updates of Matrix Functions II: Rational Krylov Methods*, arXiv:2008.11501, https://arxiv.org/abs/2008.11501 , DOI:10.1137/20M1362553.
3. D. S. Bernstein, C. F. Van Loan, *Rational Matrix Functions and Rank-1 Updates*, *SIAM Journal on Matrix Analysis and Applications* 22 (2000), 145–154, DOI:10.1137/S0895479898333636.
4. M. Fasi, N. J. Higham, X. Liu, *Computing the Square Root of a Low-Rank Perturbation of the Scaled Identity Matrix*, DOI:10.1137/22M1471559; freely available preprint https://eprints.maths.manchester.ac.uk/2856/1/fhl22.pdf .
5. B. Beckermann, D. Kressner, M. Schweitzer, *Low-rank updates of matrix functions*, arXiv:1707.03045, https://arxiv.org/abs/1707.03045 .
