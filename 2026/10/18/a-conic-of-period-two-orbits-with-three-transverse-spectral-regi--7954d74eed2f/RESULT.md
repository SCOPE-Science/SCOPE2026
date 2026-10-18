# A conic of period-two orbits with three transverse spectral regimes in a quadratic volume-preserving map

## Finding
Consider the canonical quadratic volume-preserving map of \(\mathbb R^3\)
\[
F(x,y,z)=\bigl(x+y,\ y+z-\varepsilon+\mu y+P(x,y),\ z-\varepsilon+\mu y+P(x,y)\bigr),
\qquad P(x,y)=a x^2+bxy+cy^2.
\]
On the natural positive-definite coefficient locus
\[
 a=b>0,\qquad c>a/4,\qquad \mu=-4,\qquad \varepsilon>0,
\]
write \(\kappa=c-a/4>0\). **Every primitive period-two orbit**, with no exceptions, is the unordered pair
\[
 s_-(m)=\left(m-\frac{d(m)}2,d(m),2d(m)\right),\qquad
 s_+(m)=\left(m+\frac{d(m)}2,-d(m),-2d(m)\right),
\]
where
\[
 -\sqrt{\varepsilon/a}<m<\sqrt{\varepsilon/a},\qquad
 d(m)=\sqrt{\frac{\varepsilon-a m^2}{\kappa}}>0.
\]
The endpoints \(m=\pm\sqrt{\varepsilon/a}\) correspond instead to fixed points. Thus one open arc of a real ellipse parametrizes all distinct primitive two-cycles, and the full period-two point set is the ellipse with its two fixed points removed.

At each member, the two-step derivative has the **exact characteristic polynomial**
\[
 \chi_m(\lambda)=(\lambda-1)\left[\lambda^2-(2+\Delta_m)\lambda+1\right],
 \qquad \Delta_m=4acm^2-4\kappa\varepsilon.
\]
The unavoidable eigenvalue \(1\) is tangent to the family. The other, transverse pair is (i) positive real reciprocal if \(\Delta_m>0\), (ii) distinct complex conjugates of modulus one if \(-4<\Delta_m<0\), and (iii) negative real reciprocal if \(\Delta_m<-4\). At \(\Delta_m=0\) the two transverse multipliers are \(+1\); at \(\Delta_m=-4\) they are \(-1\), with algebraic multiplicity two in each case.

**Sharp trichotomy:** For every choice \(a>0\), \(c>a/4\), all three open transverse spectral types coexist on the same period-two curve **if and only if**
\[
 \kappa\varepsilon>1.
\]
The positive-real/elliptic boundary is always at \(m^2=\kappa\varepsilon/(ac)\). The negative-real/elliptic boundary exists precisely when \(\kappa\varepsilon\ge1\), and is at \(m^2=(\kappa\varepsilon-1)/(ac)\); equality yields the single central point \(m=0\). This is an exact transition in **transverse linear spectrum**, not a claim of nonlinear orbital stability.

## Assumptions and scope
All variables and coefficients are real. The hypothesis \(a=b>0\), \(c>a/4\) makes \(P\) a positive-definite quadratic form because \(ac-b^2/4=a(c-a/4)>0\). The result concerns *least period exactly two* for the fixed map \(F\), and the eigenvalues of \(D(F^2)\) at those orbits. The derivative of the polynomial map exists globally, and \(\det DF\equiv1\). Statements at the two excluded endpoints or at either spectral equality concern algebraic multipliers only; no nonlinear stability classification is asserted. No assertion is made about higher periods, invariant tori, global boundedness, or structural persistence under perturbation away from the specified parameter locus.

## Proof
**1. Exhaustive reduction of period two.** If \(F(x,y,z)=(X,Y,Z)\) and \(F(X,Y,Z)=(x,y,z)\), comparison of the first coordinates gives \(X=x+y\) and \(Y=-y\). The defining second and third coordinates then force \(z=2y\), \(Z=-2y\). Put \(d=y\) and \(m=x+y/2\). For a primitive two-cycle \(d\ne0\), and the two states necessarily have the displayed forms \(s_-(m),s_+(m)\). Let \(R(x,y)=-\varepsilon+\mu y+P(x,y)\). Their exchange is equivalent to \(R(s_-)=-4d\) and \(R(s_+)=4d\), where only the first two coordinates are used in \(R\). Directly,
\[
 P(m-d/2,d)=a m^2+(b-a)md+\left(\frac a4-\frac b2+c\right)d^2,
\]
\[
 P(m+d/2,-d)=a m^2+(a-b)md+\left(\frac a4-\frac b2+c\right)d^2.
\]
Taking their sum and difference gives the **necessary and sufficient** scalar equations
\[
 \varepsilon=a m^2+\left(\frac a4-\frac b2+c\right)d^2,\qquad
 (a-b)m=\mu+4\quad(d\ne0).
\]
When \(a=b\) and \(\mu=-4\), they reduce exactly to \(\varepsilon=a m^2+\kappa d^2\). Positive definiteness yields an ellipse, with precisely two points at \(d=0\), both fixed, and all other points paired by \(d\leftrightarrow-d\). Taking \(d>0\) uniquely parametrizes distinct two-cycles. This proves both existence and exhaustion.

**2. Exact transverse multipliers.** At \(s_-(m)\) and \(s_+(m)\), put \(u=2am\), \(v_\pm=-4+am\pm2\kappa d\). Their respective Jacobians have the form
\[
 J_\pm=\begin{pmatrix}1&1&0\\u&1+v_\pm&1\\u&v_\pm&1\end{pmatrix}.
\]
Each has determinant one. Direct matrix multiplication gives
\[
 \operatorname{tr}(J_-J_+)=3+a^2m^2-4\kappa^2d^2.
\]
The smooth two-cycle family supplies a nonzero tangent vector fixed by \(D(F^2)\), hence one multiplier is \(1\). Because the other two have product one, their sum equals \(\operatorname{tr}(J_-J_+)-1\). The ellipse equation and \(a+4\kappa=4c\) imply
\[
 a^2m^2-4\kappa^2d^2=4acm^2-4\kappa\varepsilon=\Delta_m,
\]
which proves the characteristic polynomial. Classifying roots of \(\lambda^2-(2+\Delta_m)\lambda+1\) by its discriminant \(\Delta_m(\Delta_m+4)\) gives the stated spectra.

**3. Sharp coexistence threshold.** For the allowed parameter interval, \(m^2\) runs through \([0,\varepsilon/a)\). Therefore \(\Delta_m\) increases from \(-4\kappa\varepsilon\) to the excluded upper endpoint \(a\varepsilon>0\). It always crosses \(0\) inside the interval; it attains values below \(-4\) if and only if \(\kappa\varepsilon>1\). Both boundary locations follow by solving \(\Delta_m=0\) and \(\Delta_m=-4\). In particular, the negative-hyperbolic, elliptic, and positive-hyperbolic transverse regimes coexist exactly as claimed.

## Verification
The companion `check_exact.py` performs exact rational-arithmetic checks of the two-step exchange, the determinant, the full characteristic polynomial, and three witness orbits on one ellipse. It uses only Python's standard library. For \(a=b=c=1\), \(\mu=-4\), \(\varepsilon=2\), the three exact witnesses \(m=0,1,5/4\) have respectively \(d^2=8/3,4/3,7/12\) and \(\Delta_m=-6,-2,1/4\). Their transverse polynomials are respectively \(\lambda^2+4\lambda+1\), \(\lambda^2+1\), and \(\lambda^2-(9/4)\lambda+1\), giving each open spectral type. The proof, not finite checks, establishes the universal statement.

## Relationship to prior work
Lomelí and Meiss (1998) explicitly identify coefficient degeneracies in which infinitely many period-two orbits may occur and give a line-family example. The present claim **does not assert novelty for mere existence of nonisolated cycles**. It gives instead the exact ellipse of all least-period-two states on a positive-definite singular subfamily, an explicit two-step characteristic polynomial *along the entire family*, and a sharp within-family spectral trichotomy and threshold. In the equivalent shift-map quadratic form, the earlier exceptional equality between the first and last quadratic coefficients corresponds to \(a=b\) here.

Dullin and Meiss (arXiv:0807.0678, Appendix C) give an isolated period-two formula with denominator \(a-b\) and treat the region \(a\ne b\). This formula does not describe the singular ellipse or its transverse multiplier variation. General volume-preserving multiplier diagrams classify possible spectra once traces are known; they do not themselves supply the trace as a function of the period-two curve. The present calculation supplies that missing dependence.

## Limitations
No claim is made of a structurally stable one-parameter family; an eigenvalue \(1\) is always present. The terms elliptic and hyperbolic describe only the remaining two eigenvalues, not absolute orbital stability in three dimensions. Algebraic multiplicities at \(\Delta_m\in\{-4,0\}\) do not determine Jordan structure or nonlinear bifurcations. The original 1998 paper's complete PDF could not be inspected in the literature comparison; accessible indexed primary passages already recognize exceptional infinite two-cycle families, so further bibliographic overlap is possible for details of their transverse spectrum. Independent validation has not been performed.

## References
1. H. E. Lomelí and J. D. Meiss, *Quadratic volume-preserving maps*, **Nonlinearity** 11 (1998), 557–574. DOI: 10.1088/0951-7715/11/3/009. (Earlier discussion of exceptional period-two families.)
2. H. R. Dullin and J. D. Meiss, *Quadratic Volume-Preserving Maps: Invariant Circles and Bifurcations*, arXiv:0807.0678, first public version 2008-07-04; **SIAM Journal on Applied Dynamical Systems** 8 (2009), 76–128. Appendix C (generic period-two formula and stability discussion). DOI: 10.1137/080728160.
