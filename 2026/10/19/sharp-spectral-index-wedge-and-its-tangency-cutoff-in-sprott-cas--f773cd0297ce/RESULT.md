# Sharp spectral-index wedge and its tangency cutoff in Sprott case H

## Finding
Consider the classical two-parameter Sprott H vector field
\[
\dot x=-y+z^2,\qquad \dot y=x+ay,\qquad \dot z=x-bz,
\qquad a>0,\ b>0.
\]
Its two equilibria are the origin and \(E=(-b^2/a,b^2/a^2,-b/a)\). Let \(m_+(E)\) denote the number of Jacobian eigenvalues with strictly positive real part, counted with algebraic multiplicity. Set \(t=b/a\).

**Theorem (complete positive-parameter index partition).** Away from the imaginary-axis spectral locus,
\[
m_+(E)=\begin{cases}3,&0<t<1/\sqrt2\ \text{and}\ a^2<\dfrac{1-2t^2}{t(1-t)},\\
1,&\text{otherwise}.
\end{cases}
\]
Every point of the exceptional locus is uniquely parameterized by
\[
a_H(t)=\sqrt{\frac{1-2t^2}{t(1-t)}},\quad
b_H(t)=\sqrt{\frac{t(1-2t^2)}{1-t}},\quad 0<t<1/\sqrt2.
\]
There the spectrum is \(\{a_H(t)-b_H(t),\ \pm i\sqrt{t/(1-t)}\}\), with one strictly positive real eigenvalue and a neutral conjugate pair.

**Sharp fixed-\(b\) dichotomy.** The function \(b_H(t)\) has its unique maximum \(1/\sqrt2\) at \(t=1/2\). Thus for every \(0<b<1/\sqrt2\) there are precisely two values of \(a>0\) with an imaginary pair; between them \(m_+(E)=3\), and outside them \(m_+(E)=1\). At \(b=1/\sqrt2\) the two values coalesce at \(a=\sqrt2\) and the index is one on both sides. For \(b>1/\sqrt2\) the index is one for every \(a>0\). The tangency point is spectral, not an assertion of nondegenerate one-parameter Hopf dynamics.

## Assumptions and scope
Parameters \(a,b\) range over the entire positive quadrant; the assertion is about the unique *nonzero equilibrium* and the exact signs of real parts of the linearization. At the neutral curve \(m_+(E)=1\) under the strict-positive definition, but the equilibrium is nonhyperbolic and is excluded from the hyperbolic partition above. No solution boundedness or nonlinear cycle is assumed or inferred.

## Proof
The equilibrium equations give \(y=z^2\), \(x=-az^2=bz\), whence \(z=0\) or \(z=-b/a\). At the second solution the Jacobian is
\[
J_E=\begin{pmatrix}0&-1&-2b/a\\1&a&0\\1&0&-b\end{pmatrix},
\]
with characteristic polynomial
\[
P(\lambda)=\lambda^3+(b-a)\lambda^2+
(1-ab+2b/a)\lambda-b.
\]
Write \(p=b-a\), \(q=1-ab+2b/a\) and \(\Delta=pq+b\). Since \(P(0)=-b<0\) and \(P(\lambda)\to+\infty\) for real positive \(\lambda\), the spectrum always contains at least one positive real eigenvalue. Whenever \(p\ne0\) and \(\Delta\ne0\), the Routh first column for positive-real-part root counting is
\[
1,\qquad p,\qquad \frac{\Delta}{p},\qquad-b.
\]
If \(p<0\) and \(\Delta<0\), this column has exactly three sign changes; in every other nondegenerate sign configuration, exactly one. At \(p=0\), note \(\Delta=b>0\); an imaginary pair cannot occur there, and continuity from \(p>0\) gives index one. If \(p>0\) and \(\Delta=0\), the factorization \(P(\lambda)=(\lambda+p)(\lambda^2+q)\) has \(q=-b/p<0\); the roots are nonzero real, and the index is still one. Only \(p<0\), \(\Delta=0\) produces a purely imaginary pair, since then \(q=-b/p>0\).

Substituting \(b=at\) gives the exact identity
\[
\Delta=a\bigl[a^2t(1-t)+2t^2-1\bigr].
\]
The conditions \(p<0\) and \(\Delta<0\) are therefore equivalent to \(0<t<1/\sqrt2\) and \(a^2<(1-2t^2)/[t(1-t)]\). Setting \(\Delta=0\) in this region gives the stated \(a_H(t),b_H(t)\). There, \(P(\lambda)=(\lambda+b-a)(\lambda^2+q)\) and direct substitution yields \(q=t/(1-t)\), proving the spectrum formula.

Lastly, define \(g(t)=b_H(t)^2=t(1-2t^2)/(1-t)\). Elementary differentiation yields
\[
g'(t)=\frac{(2t-1)(2t^2-2t-1)}{(t-1)^2}.
\]
The quadratic factor is negative on \(0<t<1/\sqrt2\); hence \(g\) increases strictly to \(g(1/2)=1/2\) and decreases strictly thereafter, with \(g\to0\) at both endpoints. Each horizontal level \(0<b^2<1/2\) therefore cuts the locus twice. Since \(t=b/a\) decreases strictly with \(a\) at fixed \(b\), the two crossings enclose precisely the index-three region. At the maximal level they merge tangentially, and above it none occurs. \(\square\)

## Verification
Run `python sprott_h_checker.py` with SymPy installed. The standalone script reconstructs the equilibria, Jacobian, full characteristic polynomial, Routh determinant identity, imaginary-pair frequency, and exact derivative and maximum of \(g\). It additionally tests seven sample spectra numerically; those samples are supplementary, not the proof of a global statement. The analytic Routh and monotonicity arguments above cover all \(a,b>0\).

## Relationship to prior work
Sprott's 1994 paper introduces case H and tabulates equilibrium indices at selected parameters, including the standard chaotic case. Sprott and Linz (2000) review these finite examples and their local spectra; Sprott's 2013 technical note displays numerical attractor-type regions throughout two-parameter space. In contrast, the present claim is the *entire exact two-parameter unstable-index partition of the nonzero equilibrium*, including a sharp upper \(b\) cutoff and a coalescing pair of imaginary-axis crossings. Equilibrium-index changes alone neither imply nor classify chaotic attractors or true nonlinear Hopf cycles.

## Limitations
The result is purely local and spectral. It neither proves Lyapunov coefficient nondegeneracy at the imaginary-pair locus nor existence/stability of periodic orbits. The degenerate fixed-\(b\) tangency must not be called a generic one-parameter Hopf bifurcation. Establishing that no historically overlooked treatment derives the same full parameter partition remains subject to independent literature verification.

## References
1. J. C. Sprott, “Some simple chaotic flows,” *Physical Review E* **50** (1994), R647–R650, doi:10.1103/PhysRevE.50.R647, first published 1994-08-01.
2. J. C. Sprott and S. J. Linz, “Algebraically Simple Chaotic Flows,” *International Journal of Chaos Theory and Applications* **5** (2000), no. 2. Available at `https://sprott.physics.wisc.edu/pubs/paper250.pdf`.
3. J. C. Sprott, “Dynamic Regions in Simple Chaotic Flows,” technical note dated 2013-04-27, updated 2014-09-01, `https://sprott.physics.wisc.edu/technote/regions.htm`.
