# Exact two-regime E-optimal row sampling for one-outlier equicorrelated systems

## Finding
Let \(m\ge2\) be an integer and let \(U\in\mathbb R^{(m+1)\times(m+1)}\) be nonsingular with **unit-length rows** \(u_0,u_1,\ldots,u_m\). Assume that their inner products satisfy
\[
\langle u_i,u_j\rangle=c\quad(1\le i<j\le m),\qquad
\langle u_0,u_i\rangle=r\quad(1\le i\le m),
\]
where
\[
0<c<1,\qquad r>0,\qquad mr^2<1+(m-1)c.
\]
Fix independent row-selection probabilities \(p_i\ge0\), \(\sum_{i=0}^{m}p_i=1\). For the ordinary randomized Kaczmarz projection on a consistent system with row matrix \(U\), the **sharp worst-case conditional one-step mean-square progress coefficient** is
\[
\Lambda(p)=\lambda_{\min}\!\left(\sum_{i=0}^m p_i u_i u_i^{\mathsf T}\right).
\]
Put
\[
a=\frac{1+(m-1)c}{m},\qquad
\Theta=m(c-r^2)-r(1-c).
\]
Then the **unique global maximizing distribution**, without any symmetry assumption on \(p\), has
\[
p_0=p_*,\qquad p_1=\cdots=p_m=\frac{1-p_*}{m},
\]
where
\[
\boxed{\ p_*=
\begin{cases}
\dfrac{a+r}{1+a+2r},&\Theta\le0,\\[5pt]
\dfrac{c(1-c)}{m(c-r^2)+c(1-c)},&\Theta\ge0.
\end{cases}\ }
\]
Both displayed expressions agree at \(\Theta=0\). The exact optimal progress is
\[
\boxed{\ \Lambda_*=
\begin{cases}
\dfrac{a-r^2}{1+a+2r},&\Theta\le0,\\[6pt]
\dfrac{(1-c)(c-r^2)}{m(c-r^2)+c(1-c)},&\Theta\ge0.
\end{cases}\ }
\]
The unique optimal distribution is uniform if and only if \(r=c\). This is an exact statement for arbitrary independent probabilities, not only for exchangeable candidate weights.

There is also a singular many-row scaling law. For fixed \(\alpha>0\) and \(\beta>0\) with \(\alpha<\beta^2<1+\alpha\), let \(c=\alpha/m\), \(r=\beta/\sqrt m\), and let \(m\to\infty\) through admissible integers. Then
\[
\boxed{\ p_*\sim\frac{\beta}{\sqrt m},\qquad
\Lambda_*\sim\frac{1+\alpha-\beta^2}{m}.\ }
\]
Writing \(\Lambda_{\mathrm{unif}}\) for uniform row selection, the sharp ratio of one-step progress constants is
\[
\boxed{\ \frac{\Lambda_*}{\Lambda_{\mathrm{unif}}}\longrightarrow
\frac{2+\alpha+\sqrt{\alpha^2+4\beta^2}}2.\ }
\]
This factor is unbounded over these parameter families: choose \(\beta^2=\alpha+1/2\) and then let \(\alpha\to\infty\). Thus equal-norm row sampling can be arbitrarily worse in its sharp **one-step contraction coefficient**, even for a positive equicorrelation matrix with just one distinguished row. This is not a claim of an identical speedup in actual wall-clock time or in the exact multi-step mean-squared-error exponent.

## Assumptions and scope
Each Kaczmarz update projects orthogonally onto one of the hyperplanes \(\langle u_i,x\rangle=b_i\), sampling an index independently from a fixed probability distribution. The system is consistent, square, and nonsingular. The rows are real, normalized, and obey the correlations above. This is not a result for noisy/inconsistent problems, rectangular redundant row sets, adaptive selection, greedy rules, relaxed steps, or optimal finite-horizon trajectories. The objective is the worst-case **one-step conditional squared-Euclidean-error guarantee**, not the annealed exponent of the full random projection product.

The stated correlation range is exactly the positive-definiteness range of the prescribed row Gram matrix. It guarantees that such rows exist, up to an orthogonal transformation. The two branches meet continuously at \(\Theta=0\). At that boundary the smallest eigenvalue changes multiplicity in the symmetric optimizer.

## Proof
**1. Exact progress and existence.** For error \(e=x-x_*\), the update on normalized row \(u_i\) gives \(e^+=e-\langle u_i,e\rangle u_i\), whence
\[
\mathbb E[\|e^+\|_2^2\mid e]
=\|e\|_2^2-e^{\mathsf T}\left(\sum_i p_i u_i u_i^{\mathsf T}\right)e.
\]
Taking the supremum over nonzero \(e\) identifies the displayed sharp coefficient \(\Lambda(p)\). The Gram matrix has transverse eigenvalue \(1-c>0\) of multiplicity \(m-1\), and a two-dimensional block with determinant \(1+(m-1)c-mr^2>0\); therefore it is positive definite. Compactness of the probability simplex gives a maximizer. A boundary distribution has zero smallest eigenvalue, whereas strictly positive weights have positive smallest eigenvalue, so every maximizer is interior.

**2. Unrestricted uniqueness and symmetry.** A general argument for square nonsingular row sets establishes strict uniqueness. Write
\[
F(p)=\frac1{\Lambda(p)}
=\lambda_{\max}\!\left(\sum_i\frac{v_i v_i^{\mathsf T}}{p_i}\right),
\]
where \(v_i\) is column \(i\) of \(U^{-1}\). At an interior optimum \(p^*\), a positive semidefinite unit-trace top-eigenspace matrix \(Z\) supplies the Lagrange stationarity conditions \(v_i^{\mathsf T}Zv_i=F(p^*)(p_i^*)^2>0\) for every \(i\). Indeed the common multiplier equals \(F(p^*)\) after multiplying stationarity by \(p_i^*\) and summing. For any other interior probability vector \(p\), the Rayleigh/eigenspace variational inequality and strict Cauchy--Schwarz yield
\[
F(p)\ge\sum_i\frac{v_i^{\mathsf T}Zv_i}{p_i}
\ge\left(\sum_i\sqrt{v_i^{\mathsf T}Zv_i}\right)^2=F(p^*),
\]
with equality only for \(p=p^*\). Thus the maximizing distribution is unique. Since permutations of ordinary rows preserve their Gram matrix, they preserve the objective, and uniqueness forces \(p_1=\cdots=p_m=q=(1-p_0)/m\).

**3. Exact two-mode reduction.** Set \(p=p_0\), \(q=(1-p)/m\). The nonzero eigenvalues of the information matrix agree with those of the weighted row Gram matrix \(P^{1/2}(UU^{\mathsf T})P^{1/2}\). The latter has eigenvalue
\[
\lambda_T(p)=\frac{(1-c)(1-p)}m
\]
of multiplicity \(m-1\), and two remaining eigenvalues whose trace and determinant are
\[
\tau(p)=a+(1-a)p,
\qquad
\Delta(p)=(a-r^2)p(1-p).
\]
Let \(\lambda_-(p)\) be the smaller root of \(\lambda^2-\tau(p)\lambda+\Delta(p)=0\). Consequently \(\Lambda(p)=\min\{\lambda_T(p),\lambda_-(p)\}\).

**4. Optimizing the lower core eigenvalue.** Because \(r>0\), the square-root discriminant in
\[
\lambda_-(p)=\frac{\tau(p)-\sqrt{\tau(p)^2-4\Delta(p)}}2
\]
is strictly convex; hence \(\lambda_-(p)\) is strictly concave. Implicit differentiation gives the unique stationary point
\[
p_s=\frac{a+r}{1+a+2r},\qquad
\lambda_-(p_s)=\frac{a-r^2}{1+a+2r}.
\]
It increases up to \(p_s\) and decreases thereafter; \(\lambda_T(p)\) is strictly decreasing. At this point,
\[
\lambda_-(p_s)-\lambda_T(p_s)=
\frac{\Theta}{m(1+a+2r)}.
\]
If \(\Theta\le0\), no descending transverse mode can improve the core maximum, so \(p_s\) is globally optimal. If \(\Theta>0\), the increasing core eigenvalue meets the decreasing transverse eigenvalue once before \(p_s\). Substituting \(\lambda=\lambda_T(p)\) in the characteristic polynomial and using \(\Theta>0\) yields
\[
p_c=\frac{c(1-c)}{m(c-r^2)+c(1-c)}.
\]
The minimum increases up to this crossing and decreases thereafter, proving the second formula and its value. Strict uniqueness from Step 2 extends the reduced calculation to all probability vectors.

**5. Uniform characterization and scaling.** In the first branch, \(p_s>1/(m+1)\), because
\[
p_s-\frac1{m+1}=
\frac{(m-1)(c+r)}{(m+1)(1+a+2r)}>0.
\]
In the second branch, the sign of \(p_c-1/(m+1)\) is the sign of \(r^2-c^2\); hence uniformity occurs exactly at \(r=c\). For \(c=\alpha/m\), \(r=\beta/\sqrt m\) under \(\alpha<\beta^2<1+\alpha\), the first branch holds for large \(m\), giving the displayed expansions. The least eigenvalue under uniform sampling is \((m+1)^{-1}\) times the smaller eigenvalue of
\[
\begin{pmatrix}1&\sqrt m\,r\\ \sqrt m\,r&1+(m-1)c\end{pmatrix},
\]
for sufficiently large \(m\); its limit after multiplication by \(m\) is \((2+\alpha-\sqrt{\alpha^2+4\beta^2})/2\). Dividing the two positive limits yields the claimed ratio and unbounded-factor construction.

## Verification
The accompanying `verify_sampling.py` checks the two characteristic identities and the stationary derivative symbolically, and conducts exact-rational full-Gram determinant checks across 355 admissible parameter instances. It also independently optimizes the full smallest eigenvalue in the symmetry-reduced coordinate, tests asymmetric competitors, and verifies the Kaczmarz one-step mean-square identity by constructing normalized rows from Gram Cholesky factors. The recorded local replay produced **2,851 passing assertions**. These finite checks corroborate the algebra but do not establish the all-parameter theorem; Steps 1--5 do.

## Relationship to prior work
Strohmer and Vershynin (2007) gave the foundational randomized Kaczmarz exponential-convergence analysis with norm-based row probabilities. Gower and Richtárik (2015) subsequently formulated optimized fixed sampling as a semidefinite program, but their general framework does not evaluate the present exchangeable-with-one-outlier correlation class in closed form. Agaskar, Wang and Lu (2014) optimized the *exact asymptotic mean-square exponent*, which is a different optimization objective; the spectral one-step estimate considered here need not optimize that exponent. Pukelsheim and Torsney (1991) provided general fixed-point/equivalence conditions for optimal weights on linearly independent experimental-design support points, including E-optimality; these conditions do not state the two present formulas, the exact transverse/core transition, or the singular unbounded-efficiency family.

A published result titled *Closed-form optimal coordinate sampling for inverse-positive SPD quadratics* solves the same spectral sampling objective **under entrywise nonnegative inverse**. The present correlation matrix has strictly negative exceptional-to-ordinary entries in its inverse whenever \(r>0\). Thus it is never inverse-positive under the stated hypotheses, and the published inverse-positive closed form does not cover this family. The separately published *Exact finite-horizon cost of asymptotically optimal two-row Kaczmarz overrelaxation* concerns a different two-row cyclic and relaxed algorithm. These results and general E-optimal-design theory remain important contexts, not claimed novelties. Whether another source explicitly contains this exact specialization has not been independently ruled out.

## Limitations
Optimality is only for fixed iid row probabilities and the sharp conditional one-step squared-error guarantee. It neither determines the exact annealed multi-step exponent nor asserts superiority over different projection, iterative or adaptive methods. The large-\(m\) gain is a ratio of sharp progress coefficients; implementation time and finite-horizon performance are not analyzed. The result applies only to the prescribed positive correlation class of nonsingular square real systems. Historical equivalence remains a residual risk, especially through unindexed saturated E-optimal-design or Kaczmarz specializations. No independent mathematical audit has been performed.

## References
1. T. Strohmer and R. Vershynin, *A randomized Kaczmarz algorithm with exponential convergence*, arXiv:math/0702226, first submitted 8 February 2007, https://arxiv.org/abs/math/0702226.
2. R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, arXiv:1506.03296, first submitted 10 June 2015, https://arxiv.org/abs/1506.03296.
3. A. Agaskar, C. Wang and Y. M. Lu, *Randomized Kaczmarz algorithms: Exact MSE analysis and optimal sampling probabilities*, GlobalSIP 2014, DOI:10.1109/GlobalSIP.2014.7032145, https://dash.harvard.edu/entities/publication/73120379-2750-6bd4-e053-0100007fdf3b.
4. F. Pukelsheim and B. Torsney, *Optimal weights for experimental designs on linearly independent support points*, Ann. Statist. 19 (1991), 1614--1625, DOI:10.1214/aos/1176348265, https://www.math.uni-augsburg.de/htdocs/emeriti/pukelsheim/1991d.pdf.
5. *Closed-form optimal coordinate sampling for inverse-positive SPD quadratics*, public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-inverse-positive-optimal-coordinate-sampling--82c9d23eb995.
6. *Exact finite-horizon cost of asymptotically optimal two-row Kaczmarz overrelaxation*, public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-finite-horizon-cost-of-asymptotically-optimal-two-row-kacz--d549f7251aa1.
