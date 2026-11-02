# Symmetry-protected cycle selection and a positive half-turn defect in cubic rigid oscillators

## Finding

Fix \(0<\kappa<1\), put \(q=\sqrt{\kappa}\), \(a=(q+q^{-1})/2>1\), and consider the \(2\pi\)-periodic Abel equation
\[
\frac{dr}{d\theta}=\sin\theta\,r^2+\varepsilon(\cos2\theta-\kappa)r^3.\tag{1}
\]
For every fixed \(\kappa\) and all sufficiently small \(0<\varepsilon<\varepsilon_0(\kappa)\), (1) has **exactly one** positive periodic solution \(r_\varepsilon\). It is a hyperbolic repeller. The solution has the explicit uniform profile
\[
r_\varepsilon(\theta)=\frac1{a+\cos\theta}+\varepsilon\frac{J_q(\theta)}{(a+\cos\theta)^2}+O_\kappa(\varepsilon^2),\quad 0\le\theta\le2\pi,\tag{2}
\]
where
\[
J_q(\theta)=2\sin\theta-4a\arctan\!\left(\frac{q\sin\theta}{1+q\cos\theta}\right).\tag{3}
\]
The denominator inside the inverse tangent is positive for \(0<q<1\), so (3) uses the ordinary continuous principal branch. The axial radii and transverse multiplier obey the symmetry-improved laws
\[
r_\varepsilon(0)=\frac{2q}{(1+q)^2}+O_\kappa(\varepsilon^2),\qquad
r_\varepsilon(\pi)=\frac{2q}{(1-q)^2}+O_\kappa(\varepsilon^2),\tag{4}
\]
\[
\log\Lambda_\varepsilon=\frac{16\pi\kappa^2}{(1-\kappa)^2}\varepsilon+O_\kappa(\varepsilon^3).\tag{5}
\]
Most importantly, the first nonzero change in the **half-turn inverse-radius defect** is strictly positive and of exact quadratic order:
\[
\boxed{\;\frac1{r_\varepsilon(\pi)}-\frac1{r_\varepsilon(0)}+2
=\mathcal D(\kappa)\,\varepsilon^2+O_\kappa(\varepsilon^4),\quad
\mathcal D(\kappa)=\frac12\int_0^\pi
\frac{\sin\theta\,J_q(\theta)^2}{(a+\cos\theta)^2}\,d\theta>0.\;}\tag{6}
\]
For every compact \(K\subset(0,1)\), the conclusions and error estimates are uniform in \(\kappa\in K\) when \(\varepsilon\) is sufficiently small. In the associated planar rigid cubic oscillator, the physical period is exactly \(2\pi\).

## Assumptions and scope

Equation (1) is the polar radial equation of the real planar cubic system
\[
\begin{aligned}
\dot u&=-v+u\big[v+\varepsilon(1-\kappa)u^2-\varepsilon(1+\kappa)v^2\big],\\
\dot v&=u+v\big[v+\varepsilon(1-\kappa)u^2-\varepsilon(1+\kappa)v^2\big].
\end{aligned}\tag{7}
\]
Indeed \(\dot\theta=1\). A positive periodic radial solution is a simple closed orbit around the origin. Only the branch \(\varepsilon>0\) is asserted to be the unique positive periodic orbit of the full system; small negative \(\varepsilon\) is used solely as an analytic continuation near the selected orbit for reflection identities. The unperturbed equation has the open period annulus \(0<r(0)<1/2\), with
\[
r^{(0)}(\theta;\rho)=\frac{\rho}{1-\rho(1-\cos\theta)}.
\]
The phase section is fixed at \(\theta=0\). The symbol \(\Lambda_\varepsilon\) denotes the nontrivial Floquet multiplier of the planar orbit, equivalently the derivative of the \(2\pi\)-return map of (1).

## Proof

**1. Reciprocal transformation and exact selection.** On any positive solution set
\[
c(\theta)=\frac1{r(\theta)}+1-\cos\theta,\qquad A_\kappa(\theta)=\cos2\theta-\kappa.
\]
Then
\[
c'=-\varepsilon\frac{A_\kappa(\theta)}{c-1+\cos\theta}.\tag{8}
\]
At \(\varepsilon=0\), every constant \(c>2\) is a periodic solution, corresponding to \(0<\rho=1/c<1/2\). The first displacement coefficient at \(c=a+1\) is \(-I_\kappa(a)\), where
\[
I_\kappa(a)=\int_0^{2\pi}\frac{\cos2\theta-\kappa}{a+\cos\theta}\,d\theta
=\frac{2\pi}{\sqrt{a^2-1}}\big[q(a)^2-\kappa\big],\quad
q(a)=a-\sqrt{a^2-1}.\tag{9}
\]
The last equality follows by the Fourier coefficients of \((a+\cos\theta)^{-1}\): the zeroth coefficient is \(1/\sqrt{a^2-1}\), and its second cosine coefficient is \(q(a)^2/\sqrt{a^2-1}\). As \(a\) increases from \(1\) to infinity, \(q(a)\) decreases strictly from \(1\) to \(0\). Consequently (9) has the unique zero \(q(a)=\sqrt\kappa=q\), and
\[
I_\kappa'(a)=-\frac{16\pi\kappa^2}{(1-\kappa)^2}\ne0\quad\text{at the zero}.\tag{10}
\]
The return displacement divided by \(\varepsilon\) extends real-analytically to \(\varepsilon=0\). The analytic implicit function theorem yields a unique local positive periodic branch \(c_\varepsilon\) near \(c=a+1\). For \(\varepsilon>0\), the global half-period convexity uniqueness theorem of Bravo Trinidad–Tian–Zhao (2026, Proposition 7) applies with \(\alpha=-\varepsilon\kappa<0\), \(\beta=\varepsilon> -\alpha\), and \(\gamma=0\). In particular, its exact hypotheses are satisfied since \(A(\theta+\pi)=A(\theta)\), \(B(\theta+\pi)=-B(\theta)\), \(B>0\) on \((0,\pi)\), the cubic coefficient has two simple half-period zeros, and the reparameterized coefficient quotient has positive second derivative
\[
\frac{d^2}{dz^2}\left(\frac{A}{B}\right)
=\varepsilon\frac{3-\kappa-2\kappa(1-z)^2}{[z(2-z)]^{5/2}}>0,\quad z=1-\cos\theta\in(0,2).
\]
That theorem rules out any other positive periodic orbit and independently gives hyperbolic instability. This global uniqueness statement is **credited to the source**, not presented as an independent new uniqueness proof.

**2. Shape and reflection cancellation.** In (8), at the selected unperturbed orbit the denominator is \(a+\cos\theta\). Differentiating in \(\varepsilon\) at zero gives \(\partial_\varepsilon c_\varepsilon(\theta)|_0=C_1-J_q(\theta)\), with \(J_q'=A_\kappa/(a+\cos\theta)\), \(J_q(0)=J_q(\pi)=J_q(2\pi)=0\). Formula (3) is obtained by differentiating its right side and checking the initial condition. Analyticity holds uniformly in \(\theta\) and locally uniformly in \(\kappa\).

Under the reversal \(\theta\mapsto-\theta\), equation (1) with \(\varepsilon\) becomes the equation with \(-\varepsilon\), since \(\sin\theta\) is odd and \(\cos2\theta-\kappa\) is even. Thus the analytic continuation satisfies
\[
r_{-\varepsilon}(\theta)=r_\varepsilon(-\theta).
\]
The values at \(0\) and \(\pi\) are even analytic functions of \(\varepsilon\); in particular \(C_1=0\). This proves (2)–(4). Moreover, the return map at \(-\varepsilon\) is the inverse of the return map at \(\varepsilon\), so \(\Lambda_{-\varepsilon}=\Lambda_\varepsilon^{-1}\); hence \(\log\Lambda_\varepsilon\) is an odd analytic function. The differentiated return map of (8), together with (10), yields its linear coefficient \(-I_\kappa'(a)\), proving (5) and the exact absence of a quadratic term.

**3. Positive quadratic half-turn defect.** By the same symmetry, \(c_\varepsilon(\pi)-c_\varepsilon(0)\) is even analytic. Expand the periodic solution of (8) as
\[
c_\varepsilon(\theta)=a+1-\varepsilon J_q(\theta)+\varepsilon^2 C_2(\theta)+O_\kappa(\varepsilon^3).
\]
Comparison of the second-order terms in (8) gives
\[
C_2'(\theta)=-\frac{J_q(\theta)J_q'(\theta)}{a+\cos\theta}
=-\frac12\frac{(J_q(\theta)^2)'}{a+\cos\theta}.
\]
Integrating on \([0,\pi]\) and using \(J_q(0)=J_q(\pi)=0\) gives
\[
C_2(\pi)-C_2(0)=\frac12\int_0^\pi\frac{\sin\theta\,J_q(\theta)^2}{(a+\cos\theta)^2}\,d\theta=\mathcal D(\kappa).
\]
Since \(J_q'(0)=(1-\kappa)/(a+1)>0\) and \(\sin\theta>0\) inside the interval, the integral is strictly positive. Finally, \(c_\varepsilon(\pi)-c_\varepsilon(0)=1/r_\varepsilon(\pi)-1/r_\varepsilon(0)+2\), and even analyticity eliminates all odd powers, yielding the \(O(\varepsilon^4)\) remainder in (6). The original-time period is exactly \(2\pi\) because \(\dot\theta=1\).

## Verification

Run the self-contained numerical cross-check with Python, SciPy and NumPy:

```bash
python verify_abel.py
```

It evaluates the exact integral in (6), integrates (8) and its variational equation, solves the section periodicity condition for several \(\kappa\) and small positive and negative \(\varepsilon\), checks the predicted Floquet slope and the reflection parity, and compares the second-order coefficient to the observed half-turn defect. All computations use the included source file and are supplementary to the analytic proof. The exact identities (8)–(10), time-reversal argument, and positive integral are what establish the infinite-parameter theorem.

## Relationship to prior work

Bravo Trinidad, Tian and Zhao (arXiv:2610.19340v1, 14 October 2026), Proposition 7, prove the global positive-cycle uniqueness and instability for the trigonometric Abel normal form. This theorem is used here and is **not new**. Their Lemma 2 treats origin Lyapunov quantities and their Proposition 7 does not give the perturbative selection profile, reflection-parity cancellation of the quadratic log-multiplier term, or the strictly positive quadratic half-turn inverse-radius defect. Gasull's 2024 survey, Section 4.2, develops the general first-order Melnikov/implicit-function method for perturbations of Riccati centers; the method itself is also **not new**. The mathematical contribution assessed here is the explicit singular-annulus selection with a symmetry-protected full-orbit profile and, in particular, the nonvanishing signed second-order half-turn defect (6), with its improved even-power remainder. Earlier work on cubic rigid systems and Abel equations supplies further background and may warrant priority review.

## Limitations

The theorem applies to the exact one-parameter perturbation line (1) for each fixed \(0<\kappa<1\), or uniformly on compact subintervals. It does not claim uniformity as \(\kappa\to0\) or \(\kappa\to1\). It does not classify arbitrary cubic rigid fields, nonpositive periodic solutions, the basin of the repeller, or large perturbations. Numerical integration alone would not prove the theorem. Priority over all historical Abel and rigid-system literature has not been independently certified.

## References

1. J. L. Bravo Trinidad, R. Tian and Y. Zhao, *Uniqueness of Limit Cycles for Abel Equations and Planar Systems*, arXiv:2610.19340v1 (first submitted 14 October 2026), especially Lemma 2, Proposition 5, Proposition 7, and Theorem 2. https://arxiv.org/html/2610.19340v1
2. A. Gasull, *From Abel's differential equations to Hilbert's 16th problem*, São Paulo Journal of Mathematical Sciences (published online 28 September 2024), Section 4.2. https://doi.org/10.1007/s40863-024-00471-2
3. A. Gasull, R. Prohens and J. Torregrosa, *Limit cycles for rigid cubic systems*, Journal of Mathematical Analysis and Applications 303 (2005), 391–404; background on cubic rigid systems and limit-cycle bifurcation. https://doi.org/10.1016/j.jmaa.2004.07.030
