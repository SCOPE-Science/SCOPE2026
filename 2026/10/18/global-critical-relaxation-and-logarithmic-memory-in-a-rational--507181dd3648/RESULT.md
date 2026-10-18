# Global critical relaxation and logarithmic memory in a rational planar flip map

## Finding

Consider the planar rational map
\[
F_b(x,y)=\left(-\frac{x}{1+y^2},\ x+by\right),\qquad -1<b<1.
\]
For every initial \((x_0,y_0)\in\mathbb R^2\), its forward orbit converges to \((0,0)\). If \(x_0\ne0\), there is a finite real constant \(C=C(b,x_0,y_0)\) such that
\[
\boxed{\frac1{x_n^2}=\frac{2n}{(1+b)^2}+\frac{5+b}{2(1+b)^3}\log n+C+O\!\left(\frac{\log n}{n}\right).}
\]
A more precise stable-fiber expansion and signed asymptotic are
\[
\frac{y_n}{x_n}=-\frac1{1+b}-\frac{x_n^2}{(1+b)^4}+O(x_n^4),
\]
\[
\boxed{\lim_{n\to\infty}(-1)^n\sqrt n\,(x_n,y_n)
=\frac{\operatorname{sgn}(x_0)}{\sqrt2}(1+b,-1).}
\]
The second-coordinate critical amplitude is independent of the transverse multiplier \(b\), whereas the logarithmic memory correction depends on it. If \(x_0=0\), the trajectory is exactly \((0,b^n y_0)\), and may instead decay exponentially.

## Assumptions and scope

The parameter \(b\) is a fixed real number strictly between \(-1\) and \(1\), and initial data are arbitrary finite real numbers. The parameter multiplying the first coordinate is fixed at the critical value \(a=1\). All errors and limiting statements are as \(n\to\infty\); implicit constants may depend on \(b\) and the starting point. We do not assert uniformity near either endpoint of the parameter interval. For \(x_0\ne0\), the first coordinate never vanishes and alternates in sign. The result is a global convergence theorem, not merely a local center-manifold statement.

## Proof

**1. Global approach to the origin.** If \(x_0=0\), the exact axis orbit gives the result. Otherwise set \(u_n=|x_n|>0\). The identity \(u_{n+1}=u_n/(1+y_n^2)\) shows that \(u_n\) decreases to some \(U\ge0\) and that the sign of \(x_n\) alternates. The recursion \(y_{n+1}=x_n+b y_n\) is a stable affine filter because \(|b|<1\); it follows that if \(U>0\), then
\[
(-1)^n\operatorname{sgn}(x_0)y_n\longrightarrow-\frac{U}{1+b}.
\]
Indeed, after multiplying by \((-1)^{n+1}\operatorname{sgn}(x_0)\), the recursion has multiplier \(-b\) and forcing \(-u_n\); convergence follows by splitting its geometric convolution into a finite initial segment and a tail. Thus \(y_n^2\to U^2/(1+b)^2>0\), so \(u_{n+1}/u_n\to (1+U^2/(1+b)^2)^{-1}<1\), contradicting \(u_n\to U>0\). Therefore \(U=0\), and the same stable filter gives \(y_n\to0\).

**2. Exact normalized recursions and the leading scale.** For nonzero \(x_n\), define \(q_n=x_n^2\), \(r_n=y_n/x_n\), and \(s_n=1/q_n\). Direct substitution yields the *exact* identities
\[
q_{n+1}=\frac{q_n}{(1+r_n^2q_n)^2},\qquad
r_{n+1}=-(1+b r_n)(1+r_n^2q_n),\qquad
s_{n+1}-s_n=2r_n^2+r_n^4q_n.
\]
Because \(r_n^2q_n=y_n^2\to0\), the second identity is an eventually contracting nonautonomous affine recurrence: its slope has absolute value \(|b|(1+y_n^2)<\rho<1\) for all sufficiently large \(n\). Its constant term tends to \(-1\), so
\[
r_n\longrightarrow r_*=-\frac1{1+b}.
\]
Consequently \(s_{n+1}-s_n\to c=2/(1+b)^2\), giving \(s_n/n\to c\), \(q_n\sim 1/(cn)\). These statements hold even for \(b=0\).

**3. Stable-fiber expansion with controlled remainder.** Write \(\delta_n=r_n-r_*\). The exact recurrence is
\[
\delta_{n+1}=-b\delta_n-(1+b r_n)r_n^2q_n.
\]
Now \(q_n=O(1/n)\), while \(r_n\) is bounded. Summation against the geometric kernel of the stable multiplier \(-b\) gives \(\delta_n=O(1/n)\). Set \(A=-(1+b)^{-4}\) and \(e_n=\delta_n-Aq_n\). Since \(q_{n+1}-q_n=O(q_n^2)\) and
\[
(1+b r_n)r_n^2=\frac1{(1+b)^3}+O(1/n),
\]
the cancellation \(A(1+b)=-(1+b)^{-3}\) yields \(e_{n+1}=-b e_n+O(n^{-2})\). Another geometric convolution gives \(e_n=O(n^{-2})=O(q_n^2)\). Hence
\[
r_n=-\frac1{1+b}-\frac{q_n}{(1+b)^4}+O(q_n^2).
\]

**4. Logarithmic correction and finite renormalized limit.** In the exact inverse-square increment, substitute the expansion from Step 3:
\[
\begin{aligned}
s_{n+1}-s_n
 &=2r_n^2+r_n^4q_n\\
 &=c+Hq_n+O(q_n^2)=c+\frac H{s_n}+O(s_n^{-2}),\\
c&=\frac2{(1+b)^2},\qquad H=\frac{5+b}{(1+b)^5}.
\end{aligned}
\]
Since \(s_n\sim cn\), summing the last recurrence first gives \(s_n=cn+O(\log n)\). Put \(d=H/c=(5+b)/(2(1+b)^3)\). Then
\[
\big(s_{n+1}-c(n+1)-d\log(n+1)\big)-
\big(s_n-cn-d\log n\big)
 =O\!\left(\frac{\log n}{n^2}\right).
\]
The right side is absolutely summable, hence \(s_n-cn-d\log n\to C\) for a finite real \(C\); bounding its tail proves \(O(\log n/n)\). The coefficient \(d\) is strictly positive on the entire stated parameter interval.

**5. Amplitudes in physical coordinates.** From \(nq_n\to1/c=(1+b)^2/2\) and exact alternation of the sign of \(x_n\),
\[
(-1)^n\sqrt n\,x_n\to\operatorname{sgn}(x_0)\frac{1+b}{\sqrt2}.
\]
Multiplication by \(r_n\to-1/(1+b)\) establishes the asserted \(y_n\) limit. The exceptional axis orbit follows from direct substitution. This completes the proof.

## Verification

The accompanying standalone `verify.py` checks symbolic cancellation of the critical stable-fiber coefficient and the exact coefficients \(c\), \(H\), \(H/c\), then performs independent finite-iterate corroborations at representative parameters and initial conditions. It prints `VERIFY_OK` on success. Execute `python verify.py` with Python 3 and SymPy installed. The algebraic and convergence arguments above establish the theorem; finite trajectories are not used to certify infinitely many iterates.

## Relationship to prior work

Elhadj and Sprott introduced and explored the rational two-dimensional map in 2011. Somarakis and Baras (2013), Section 4.2 and Proposition 3, proved global asymptotic stability of the origin for \(|a|<1\), \(|b|<1\); their Section 4.3 and Proposition 5 analyze the period-doubling transition at \(a=1\) using a local center-manifold expansion. Neither of the inspected full texts states global convergence *on* the critical boundary, a parameter-explicit inverse-square logarithmic correction, or a transverse amplitude independent of \(b\). Generic center-manifold treatments of critical period doubling (e.g., Leonel, Ferreira and Oliveira 2026) establish the familiar local inverse-square-root exponent, not this global map-specific logarithmic law. A distinct positive rational flip map has a published logarithmic relaxation law, but it is a different dynamical system and its numerical coefficients do not imply the present formulas.

## Limitations

The theorem does not cover \(|b|\ge1\), \(a\ne1\), nor non-real states. Its limiting constant \(C\) is not supplied in closed form. The asymptotic error is pointwise in fixed \(b\) and initial data, and the transient can be extremely long for values near the boundary. Independent historical priority evaluation has not been performed. The 2011 original and the 2013 follow-up are both publicly identified, but the exact initial public day of the older 2011 work could not be reliably established; the day-precise source record used here is the verified 2013 publication date. An earlier technical report cited in the 2013 paper could not be independently inspected.

## References

1. Z. Elhadj and J. C. Sprott, *On the Dynamics of a New Simple 2-D Rational Discrete Mapping*, International Journal of Bifurcation and Chaos 21 (2011), 155–160, doi:10.1142/S0218127411028325; author-hosted full text: https://sprott.physics.wisc.edu/pubs/paper310.pdf.
2. C. Somarakis and J. S. Baras, *On the Dynamics of a Simple Rational Planar Map*, International Journal of Bifurcation and Chaos 23 (2013), 1330021, doi:10.1142/S0218127413300218; author-hosted full text: https://user.eng.umd.edu/~baras/publications/journals/2013_IJBC_Somarakis_Baras_Dynamics.pdf.
3. E. D. Leonel, J. P. C. Ferreira and D. F. M. Oliveira, *A phenomenological description of critical slowing down at period-doubling bifurcations* (2026), arXiv:2602.04091.
