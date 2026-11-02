# A sharp coefficient-cap frontier for finite termination of scalar Anderson acceleration

## Finding
For every scalar affine contraction \(g(x)=qx+b\) with \(0<q<1\), start exact depth-one Anderson acceleration from any \(x_0\ne x_*=b/(1-q)\), with \(x_1=g(x_0)\). At each subsequent step minimize the absolute affine combination of the two most recent residuals, subject to coefficient sum one and coefficient \(\ell^1\)-norm at most \(\Lambda>1\), then apply the same affine combination to their images under \(g\).

Put \(s=\sqrt{1-q}\). The iteration reaches its exact fixed point in finitely many steps if and only if
\[
\boxed{\quad \Lambda>\Lambda_*(q):=1+2\frac{1-s}{1+s}=\frac{3-s}{1+s}.\quad}
\]
Equality is **nonterminating**: at \(\Lambda=\Lambda_*(q)\), the normalized errors obey
\[
\frac{x_n-x_*}{x_0-x_*}=(1+ns)(1-s)^n>0\qquad(n\ge0).
\]
For \(1<\Lambda<\Lambda_*(q)\), the errors likewise never vanish. Write \(a=(\Lambda-1)/2\). Their exact root-linear factor is
\[
r_+(q,a)=\frac{q(1+a)+\sqrt{q^2(1+a)^2-4qa}}{2}<q.
\]

The **sharp uniform cap** over all positive scalar contractions is \(\Lambda=3\). At this cap the first exact-zero iterate has the closed form
\[
\boxed{\quad N(q)=\left\lceil\frac{\pi}{2\arccos\sqrt q}\right\rceil.\quad}
\]
In particular \(N(q)\sim\pi/(2\sqrt{1-q})\) as \(q\uparrow1\); any fixed cap strictly smaller than three leaves some positive scalar contraction nonterminating. These are exact-arithmetic conclusions, not floating-point stopping-tolerance statements.

## Assumptions and scope
At step \(n\ge1\), with \(r_j=g(x_j)-x_j\), choose \((\alpha_{n-1},\alpha_n)\) to minimize
\[
\left|\alpha_{n-1}r_{n-1}+\alpha_nr_n\right|
\quad\text{subject to}\quad
\alpha_{n-1}+\alpha_n=1,\qquad
|\alpha_{n-1}|+|\alpha_n|\le\Lambda,
\]
and set \(x_{n+1}=\alpha_{n-1}g(x_{n-1})+\alpha_ng(x_n)\). Stop immediately when a residual is zero. The first step is ordinary fixed-point iteration; memory is exactly one, no damping or additional regularization is applied, and the coefficient cap is constant throughout a run. All arithmetic and constrained minimizations are exact. The parameter \(b\in\mathbb R\) and the nonfixed initialization are unrestricted.

## Proof
**The constrained scalar projection.** Let \(e_n=x_n-x_*\), so \(r_n=(q-1)e_n\), and divide every error by the nonzero \(e_0\). We obtain \(u_0=1\), \(u_1=q\). Write \(a=(\Lambda-1)/2>0\). If \(0<u_n<u_{n-1}\), the admissible coefficient \(t=\alpha_{n-1}\) is exactly the interval \([-a,1+a]\), and the scalar least-squares objective is a positive constant times
\[
\left|u_n+t(u_{n-1}-u_n)\right|.
\]
At \(t=0\) the expression is positive; at the left endpoint it is \(w_n=(1+a)u_n-au_{n-1}\). If \(w_n>0\), the unique minimizer is \(t=-a\), yielding \(u_{n+1}=qw_n\in(0,u_n)\). If \(w_n\le0\), a feasible \(t\in[-a,0]\) makes the residual combination zero, so \(u_{n+1}=0\). Thus nonzero normalized errors remain strictly positive and decreasing, and their evolution before termination is the fixed recurrence
\[
 v_0=1,\quad v_1=q,\quad
 v_{n+1}=q\big((1+a)v_n-av_{n-1}\big).
\tag{1}
\]
More precisely, the capped iteration terminates exactly at the **first** index \(n\ge2\) for which \(v_n\le0\), setting that iterate to zero; if no such index exists it follows \(u_n=v_n>0\) forever. This induction uses only the two exact residual values and the stated cap.

**Positive and nonpositive recurrence phases.** The characteristic polynomial of (1) is \(p(z)=z^2-q(1+a)z+qa\), with discriminant \(\Delta=q^2(1+a)^2-4qa\). Put \(s=\sqrt{1-q}\in(0,1)\). Its two repeated-root parameters are
\[
a_-:=\frac{1-s}{1+s},\qquad a_+:=\frac{1+s}{1-s},
\]
with \(\Delta>0\) on \((0,a_-)\cup(a_+,\infty)\), and \(\Delta<0\) on \((a_-,a_+)\).

For \(0<a<a_-\), the two characteristic roots satisfy \(0<r_-<r_+<q\). Indeed \(p(q)=qa(1-q)>0\), and continuity from \(a=0\), where the roots are \(0,q\), fixes the side of both roots. Consequently
\[
v_n=r_+^n+\frac{q-r_+}{r_+-r_-}(r_+^n-r_-^n)>0\quad(n\ge0).
\]
The coefficient of \(r_+^n\) is positive, so its exact root-linear factor is \(r_+\), the quantity displayed in the finding.

At \(a=a_-\), the repeated root is \(r=1-s\) and matching the initial values gives \(v_n=(1+ns)r^n>0\) for every finite \(n\). This establishes both nontermination at equality and its precise asymptotic rate.

For \(a_-<a<a_+\), the roots are a nonreal conjugate pair \(Re^{\pm i\theta}\) with \(R>0\) and \(0<\theta<\pi\). The real sequence has the form \(v_n=R^n(\cos(n\theta)+B\sin(n\theta))\) for a real \(B\). It is negative for some positive integer \(n\): if \(\theta/(2\pi)\) is irrational the phases are dense, while if rational the sum of \(\cos(n\theta)+B\sin(n\theta)\) over a full nontrivial phase orbit is zero and its value at \(n=0\) is one. At \(a=a_+\), the repeated root is \(r=1+s>q\), so \(v_n=r^n[1+n(q/r-1)]\) is eventually negative. For \(a>a_+\), both positive real roots exceed \(q\) (they do at \(a_+\), and \(p(q)=qa(1-q)>0\) rules out crossings); the coefficient of the dominant root \(r_+\) is \((q-r_-)/(r_+-r_-)<0\), so \(v_n<0\) eventually. In all these cases, the first nonpositive hypothetical value leads to finite exact termination by the scalar projection established above. Hence termination is equivalent to \(a>a_-\), or exactly \(\Lambda>\Lambda_*(q)\).

**The cap-three stopping index and its optimality.** When \(\Lambda=3\), \(a=1\) and (1) is \(v_{n+1}=q(2v_n-v_{n-1})\). With \(\theta=\arccos\sqrt q\in(0,\pi/2)\), its unique solution is
\[
v_n=q^{n/2}\cos(n\theta).
\]
Starting at positive \(v_0\), the first nonpositive term occurs exactly at \(N(q)=\lceil\pi/(2\theta)\rceil\); all preceding terms are positive since the phase increment is less than \(\pi/2\). This proves the stopping-index formula and its square-root asymptotic as \(q\uparrow1\). Every \(q<1\) has \(\Lambda_*(q)<3\), so this cap always terminates. Conversely \(\Lambda_*(q)\uparrow3\) as \(q\uparrow1\), so any given \(1<\Lambda<3\) fails to terminate for some \(q<1\). Thus three is the smallest universal finite-termination cap.

## Verification
The standalone `verify.py` uses exact rational arithmetic to reconstruct the affine residual minimizer under the coefficient \(\ell^1\) cap and compare its iterates with recurrence (1). It checks 2,580 supplementary rational identities and comparisons, the repeated-root formula at \(q=3/4\), the cap-three stopping index across a rational grid, and invariance under affine translations and changes of the sign of the initial error.

At \(q=9/10\), \(\Lambda=3\), the hypothetical recurrence begins
\[
1,\quad\frac9{10},\quad\frac{18}{25},\quad\frac{243}{500},\quad\frac{567}{2500},\quad-\frac{729}{25000}.
\]
The true constrained method produces the first five positive values and then exactly zero at \(n=5\), as the analytic formula predicts. The verifier is supplementary: the proofs for all real \(q\), \(\Lambda\), and all iteration indices are the root classification and scalar projection above, not finite numerical sampling.

## Relationship to prior work
Lerman and Zhang's 2026 study supplies the exact sliding-window algorithm and the coefficient \(\ell^1\) cap. Its Section 7 and supplementary Section S6 prove improved asymptotic convergence rates when a polynomial certificate exists for every fixed cap greater than one; their comparison at cap one gives unaccelerated scalar Picard iteration. Those statements do not decide **finite** termination, its sharp cap as a function of the contraction, or an exact stopping index. The present result distinguishes two regimes that both have asymptotic factor smaller than \(q\): nontermination and exact termination.

Garner, Lerman, and Zhang consider windowed acceleration of symmetric contractions, and classical work of Toth and Kelley concerns contractive convergence rather than the present exact cap boundary. A published two-dimensional positive-contraction example of uncapped depth-one Anderson acceleration includes the classical observation that the scalar uncapped method reaches its fixed point at the first accelerated step; this does not imply the corresponding property when the required mixing coefficient lies outside the capped interval.

Barré, Taylor, and d'Aspremont analyze an \(\ell^1\)-constrained extrapolation of a precomputed finite sequence of plain fixed-point iterates, with polynomial/Chebyshev bounds. Their coefficient constraint is related, but their one-shot extrapolation does not use a *sliding two-residual window whose inputs are previous accelerated iterates*. Thus their finite-degree polynomial bounds do not establish the dynamical threshold above. The present result is a complete elementary benchmark for that distinct capped online recurrence, not an assertion that general constrained polynomial acceleration is new.

## Limitations
Only exact depth-one, unit-mixing Anderson acceleration on a one-dimensional **positive** affine contraction is classified. Negative scalar multipliers can have different early cancellation behavior. For nonlinear maps, several dimensions, noisy residuals, varying caps, damping, or finite-precision minimization, neither exact finite termination nor the universal cap-three guarantee follows. A finite numerical stopping tolerance is not equivalent to the theorem's exact zero. An older equivalent scalar safeguarded extrapolation calculation under other terminology cannot be excluded completely.

## References
1. G. Lerman and T. Zhang, *When Windowed Anderson Acceleration Converges Faster*, arXiv:2610.30073v1, first publicly posted 21 October 2026, https://arxiv.org/html/2610.30073v1 (especially Sections 2, 7, and S6).
2. C. Garner, G. Lerman, and T. Zhang, *Improved Convergence Factor of Windowed Anderson Acceleration for Symmetric Fixed-Point Iterations*, SIAM Journal on Numerical Analysis 64 (2026), 1891–1922; arXiv:2311.02490, https://arxiv.org/abs/2311.02490.
3. M. Barré, A. Taylor, and A. d'Aspremont, *Convergence of a Constrained Vector Extrapolation Scheme*, SIAM Journal on Mathematics of Data Science 4 (2022), 979–1002; original preprint arXiv:2010.15482v1, https://arxiv.org/pdf/2010.15482.
4. A. Toth and C. T. Kelley, *Convergence Analysis for Anderson Acceleration*, SIAM Journal on Numerical Analysis 53 (2015), 805–819, https://doi.org/10.1137/130919398.
5. *Depth-one Anderson acceleration can break a positive diagonal contraction in two dimensions*, published research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-depth-one-anderson-acceleration-can-break-a-positive-diagonal-co--5b097239b6a3.
