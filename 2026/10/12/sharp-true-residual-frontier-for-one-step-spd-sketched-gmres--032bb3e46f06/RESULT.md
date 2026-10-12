# Sharp true-residual frontier for one-step SPD sketched GMRES

## Finding

For a real symmetric positive-definite (SPD) matrix with spectral condition number \(\kappa\ge 1\), the sharp one-step Euclidean-residual amplification of sketched GMRES under a squared-norm \(\varepsilon\)-embedding of the two-dimensional residual search plane is

\[
\boxed{\displaystyle
\sup_{A,r,\Theta}\frac{\|r-\alpha Ar\|_2}{\|r\|_2}
=\frac{\kappa-1}{(\kappa+1)\sqrt{1-\varepsilon^2}}\,,\qquad 0\le\varepsilon<1,}
\]

where \(\alpha\) minimizes the *sketched* residual norm. The supremum is attained in dimension two for every \(\kappa>1\), including \(\varepsilon=0\). For \(\kappa=1\), the ratio is always zero. In particular, a true-residual-nonexpansive first step for **every** admissible SPD system, start, and embedding is guaranteed precisely when

\[
\varepsilon\le\frac{2\sqrt{\kappa}}{\kappa+1}.
\]

For \(\kappa>1\) and larger embedding distortion, an exact two-dimensional sketch produces strict residual *growth*. Relative to exact GMRES, the optimal worst-case sketch penalty is \((1-\varepsilon^2)^{-1/2}\), rather than the frequently quoted generic quasi-optimality factor \(\sqrt{(1+\varepsilon)/(1-\varepsilon)}\).

## Assumptions and scope

Let \(n\ge2\), let \(A\in\mathbb R^{n\times n}\) be symmetric positive definite, and write \(\mu=\lambda_{\min}(A)>0\), \(L=\lambda_{\max}(A)\), and \(\kappa=L/\mu\). Let \(r=b-Ax_0\ne0\). Let \(\Theta\in\mathbb R^{s\times n}\), with \(s\ge2\), be any deterministic or realized random linear sketch satisfying

\[
(1-\varepsilon)\|z\|_2^2\le\|\Theta z\|_2^2\le(1+\varepsilon)\|z\|_2^2
\quad\text{for every }z\in W:=\operatorname{span}\{r,Ar\},
\]

for a fixed \(0\le\varepsilon<1\). Define the first sketched minimal-residual step \(x_1=x_0+\alpha r\), where

\[
\alpha=\operatorname*{argmin}_{t\in\mathbb R}\|\Theta(r-tAr)\|_2
=\frac{(Ar)^\mathsf T\Theta^\mathsf T\Theta r}{\|\Theta Ar\|_2^2};
\qquad r_1=r-\alpha Ar.
\]

The minimizer is unique because the embedding is positive definite on \(W\). The supremum fixes \(\kappa\) and \(\varepsilon\), and varies \(n,A,r,\Theta\) subject to these requirements. No distributional assumption on \(\Theta\), and no embedding requirement outside \(W\), is imposed. The statement concerns the true Euclidean **residual**, not Euclidean solution error or a multi-step trajectory.

## Proof

**Step 1: exact oblique-projection distortion.** Put \(w=Ar\), \(u=w/\|w\|_2\), and decompose the normalized residual as \(r/\|r\|_2=c u+d v\), where \(v\perp u\) is a unit vector and \(c>0\), \(d\ge0\), \(c^2+d^2=1\). Here \(c=r^\mathsf T Ar/(\|r\|_2\|Ar\|_2)\). If \(d=0\), the one-step residual is zero and the conclusion is immediate. Otherwise \(u,v\) form an orthonormal basis for \(W\). Let \(B=[u\ v]^\mathsf T\Theta^\mathsf T\Theta[u\ v]\), with entries \(B_{11}=u^\mathsf T\Theta^\mathsf T\Theta u\) and \(B_{21}=v^\mathsf T\Theta^\mathsf T\Theta u\). The embedding condition means every eigenvalue of \(B\) lies in \([1-\varepsilon,1+\varepsilon]\). Direct least-squares algebra yields

\[
\frac{\alpha\|Ar\|_2}{\|r\|_2}
=c+d\frac{B_{21}}{B_{11}},\qquad
\frac{\|r_1\|_2}{\|r\|_2}
=d\sqrt{1+\left(\frac{B_{21}}{B_{11}}\right)^2}.
\]

Because \(\|B-I\|_2\le\varepsilon\), the squared length of its first-column error satisfies \((B_{11}-1)^2+B_{21}^2\le\varepsilon^2\). Writing \(t=B_{11}-1\), we obtain

\[
\left(\frac{B_{21}}{B_{11}}\right)^2
\le\max_{-\varepsilon\le t\le\varepsilon}\frac{\varepsilon^2-t^2}{(1+t)^2}
=\frac{\varepsilon^2}{1-\varepsilon^2}.
\]

For \(0<\varepsilon<1\), the unique maximizer of this scalar expression is \(t=-\varepsilon^2\); the derivative is \(-2(\varepsilon^2+t)/(1+t)^3\). The same inequality is immediate at \(\varepsilon=0\). Consequently

\[
\|r_1\|_2/\|r\|_2\le d/\sqrt{1-\varepsilon^2}.
\]

**Step 2: sharp SPD angle bound.** Normalize \(r\) to unit length and regard the eigenvalue of \(A\) as a random variable \(T\in[\mu,L]\) whose weights are the squared spectral coordinates of \(r\). Put \(m=\mathbb E[T]\). The pointwise inequality \((T-\mu)(L-T)\ge0\) gives \(\mathbb E[T^2]\le(\mu+L)m-\mu L\). Therefore

\[
c^2=\frac{m^2}{\mathbb E[T^2]}
\ge\frac{m^2}{(\mu+L)m-\mu L}
\ge\frac{4\mu L}{(\mu+L)^2}.
\]

The last inequality follows by minimizing over \(m\in[\mu,L]\), with equality at \(m=2\mu L/(\mu+L)\). Hence \(d=\sqrt{1-c^2}\le(L-\mu)/(L+\mu)=(\kappa-1)/(\kappa+1)\). Both inequalities are simultaneously sharp.

**Step 3: simultaneous equality.** For any \(\kappa>1\), set

\[
A=\begin{pmatrix}1&0\\0&\kappa\end{pmatrix},\qquad
r=\begin{pmatrix}\sqrt\kappa\\1\end{pmatrix},\qquad
u=\frac{Ar}{\|Ar\|_2},\quad
v=\frac{r-c\|r\|_2u}{d\|r\|_2}.
\]

This gives \(c=2\sqrt\kappa/(\kappa+1)\) and \(d=(\kappa-1)/(\kappa+1)\). In the orthonormal basis \([u\ v]\), choose the sketch Gram matrix

\[
B=I+
\begin{pmatrix}
-\varepsilon^2&\varepsilon\sqrt{1-\varepsilon^2}\\
\varepsilon\sqrt{1-\varepsilon^2}&\varepsilon^2
\end{pmatrix}.
\]

The perturbation squares to \(\varepsilon^2 I\), so \(B\) has eigenvalues exactly \(1-\varepsilon\) and \(1+\varepsilon\). It has \(B_{11}=1-\varepsilon^2\) and \(B_{21}=\varepsilon\sqrt{1-\varepsilon^2}\), simultaneously saturating Step 1. Let \(U=[u\ v]\) and choose the real square-root sketch \(\Theta=B^{1/2}U^\mathsf T\) (or embed this two-row sketch isometrically in higher ambient dimension). Then \(\Theta^\mathsf T\Theta\) restricted to \(W\) has Gram matrix \(B\) and the displayed worst-case factor is attained. When \(\kappa=1\), \(Ar=\mu r\), so the minimizer is \(\alpha=1/\mu\) and \(r_1=0\) for every admissible sketch.

**Step 4: threshold and exact witness.** The sharp factor is at most one exactly when \((\kappa-1)^2\le(\kappa+1)^2(1-\varepsilon^2)\), equivalently \(\varepsilon\le2\sqrt\kappa/(\kappa+1)\). This is both sufficient and, by Step 3, necessary for universal nonexpansion. For a rational strict-growth example take

\[
A=\operatorname{diag}(1,9),\quad r=(3,1)^\mathsf T,\quad
\varepsilon=\frac45,\quad
\Theta^\mathsf T\Theta=\operatorname{diag}\left(\frac95,\frac15\right).
\]

The sketch has squared-norm distortion exactly \(\varepsilon\), its coefficient is \(\alpha=5/9\), and \(r_1=(4/3,-4)^\mathsf T\), so \(\|r_1\|_2/\|r\|_2=4/3>1\). At the boundary \(\varepsilon=3/5\), choose instead \(\Theta^\mathsf T\Theta=\begin{pmatrix}197/125&21/125\\21/125&53/125\end{pmatrix}\), with eigenvalues \(1\pm3/5\); the true-residual ratio is exactly one. This verifies the non-strict boundary as well as a strict-growth case.

## Verification

The standalone standard-library Python program `verify.py` reconstructs the two rational equality witnesses and checks their sketch Gram eigenvalues exactly, evaluates 56 independent extremizer constructions, and tests 10,500 random two-mode SPD/embedding pairs against the proved bound. Executing `python3 verify.py` on the packaged program prints `VERIFY_OK`. The analytic inequalities and equality constructions above, not the finite tests, establish the universal assertion. No interval certificate or probabilistic performance guarantee is claimed.

## Relationship to prior work

Bucci and Durastante [1, Section 2] define sketched GMRES under precisely a squared-norm subspace embedding, and explicitly note that the unsketched true residual need not decrease; their principal result [1, Theorem 1] is a sketched Anderson-acceleration equivalence, not a sharp residual ratio. Burke, Güttel, and Soodhalter [2, Section 3] give a general quasi-optimality factor \(\sqrt{(1+\varepsilon)/(1-\varepsilon)}\) for sketched GMRES; it provides an upper bound but not the sharp, smaller SPD first-step factor and cannot imply the exact tolerance frontier. Epperly and Webber [3, Section 2] give sharp *distribution-specific mean-square* sketched-regression analyses, not a worst-case deterministic SPD one-step residual threshold. Burke, Carson, and Ma [4] analyze finite-precision stability, a distinct question. Jang and Grigori [5, Section 5] compare sketched-norm GMRES with reorthogonalized true-norm variants without the stated threshold.

The two ingredients, Kantorovich's SPD angle inequality and the geometry of oblique least-squares projections, are classical. The proposed contribution is their simultaneous sharpness for the *specific sketched first GMRES step* and the resulting necessary-and-sufficient embedding tolerance for universal true-residual nonexpansion; neither ingredient is claimed as independently new.

## Limitations

The result covers **one** real-arithmetic, exact-arithmetic GMRES step, an SPD matrix, and a sketch that is an embedding on the *full plane* spanned by the initial residual and its image. It does not establish contraction of every later sketched GMRES step under a fixed sketch, nor does it cover nonsymmetric, indefinite, complex, adaptive, finite-precision, or non-embedding sketches. For \(\kappa>1\), the equalities can be realized by a two-row sketch on a two-dimensional active subspace, but this does not show that typical randomized sketches saturate them. A classical equivalent result under an oblique-projection or operator-angle formulation is possible; no claim of exhaustive literature uniqueness is made.

## References

[1] A. Bucci and F. Durastante, “An Equivalence result for sketched Anderson Acceleration and sketched GMRES,” arXiv:2607.04904v1 (first public 2026-07-06). https://arxiv.org/html/2607.04904v1

[2] L. Burke, S. Güttel, and K. M. Soodhalter, “GMRES with randomized sketching and deflated restarting,” arXiv:2311.14206v2. https://arxiv.org/html/2311.14206v2

[3] E. N. Epperly and R. J. Webber, “Sharp analysis of sketched least squares and randomized low-rank approximation,” arXiv:2605.19096v2. https://arxiv.org/html/2605.19096v2

[4] L. Burke, E. Carson, and Y. Ma, “On the numerical stability of sketched GMRES,” arXiv:2503.19086v3. https://arxiv.org/html/2503.19086v3

[5] Y. Jang and L. Grigori, “Randomized Orthogonalization Process With Reorthogonalization,” *Numerical Linear Algebra with Applications* (2025), DOI:10.1002/nla.70029. https://doi.org/10.1002/nla.70029
