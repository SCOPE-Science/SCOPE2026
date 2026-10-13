# Exact one-dimensional reduction of the qubit Umegaki reward half-space divergence
## Finding
Let \\(F=|0\\rangle\\langle0|\\) be the qubit reward projector. Write a faithful arm as
\\[
\\rho=\\frac12\\bigl(I+p\\sigma_x+m\\sigma_z\\bigr),
\\qquad p>0,\\qquad p^2+m^2<1,
\\]
after a phase rotation about the \\(z\\)-axis. Let the confusing half-space be
\\[
\\Lambda_\\tau=\\{\\sigma:\\operatorname{Tr}(\\sigma F)\\ge\\tau\\},
\\qquad \\frac{1+m}2<\\tau<1,
\\]
and put \\(z=2\\tau-1\\).

Then the Umegaki half-space divergence
\\[
D_{\\mathrm{inf}}(\\rho,\\tau)=\\inf_{\\sigma\\in\\Lambda_\\tau}D(\\rho\\|\\sigma)
\\]
has a unique minimizer. It lies on the reward boundary, in the real plane spanned by the arm coherence and the reward axis:
\\[
\\sigma_*=\\frac12\\bigl(I+x_*\\sigma_x+z\\sigma_z\\bigr),
\\qquad 0<x_*<\\sqrt{1-z^2}.
\\]
Thus the full matrix optimization is exactly one-dimensional.

Set
\\[
R=\\sqrt{p^2+m^2},\\qquad q(x)=\\sqrt{x^2+z^2},
\\]
and
\\[
C_R=\\frac12\\left[(1+R)\\log\\frac{1+R}2+(1-R)\\log\\frac{1-R}2\\right].
\\]
Then
\\[
D_{\\mathrm{inf}}(\\rho,\\tau)=D(x_*),
\\]
where
\\[
D(x)=C_R-\\frac12\\log\\frac{1-q(x)^2}4
-\\frac{px+mz}{q(x)}\\operatorname{artanh}q(x),
\\]
and \\(x_*\\) is the unique zero of
\\[
D'(x)=\\frac{x}{1-q^2}-\\frac{p\\operatorname{artanh}q}q
-\\frac{x(px+mz)}{q^3}\\left(\\frac{q}{1-q^2}-\\operatorname{artanh}q\\right).
\\]

For the numerical qubit instance of arXiv:2609.40339v1, \\(p=0.9\\), \\(m=0\\), and \\(z=0.9\\). The unique solution is
\\[
x_*=0.255924326128\\ldots,
\\qquad
D_{\\mathrm{inf}}=1.117330054762\\ldots\\ \text{nats}.
\\]
The paper's exact single-copy exponent is
\\[
K_{\\mathrm{inf}}=\\operatorname{kl}(0.5,0.95)=0.830365603411\\ldots.
\\]
Therefore its quantum-memory converse can reduce the exploration coefficient by at most
\\[
1-\\frac{K_{\\mathrm{inf}}}{D_{\\mathrm{inf}}}
=0.256830513176\\ldots,
\\]
which analytically resolves the source's quoted numerical value of about \\(25.7\\%\\).

## Assumptions and scope
The arm is a faithful qubit state and is noncommuting with the reward projector, so \\(p>0\\) and \\(p^2+m^2<1\\). The threshold is strictly above the arm mean and strictly below one. A rotation about the reward axis makes the transverse Bloch component real and nonnegative without changing either the constraint or the divergence.

The finding evaluates the Umegaki half-space quantity used in the quantum-memory converse. It does not solve the source's separate composite-testing or adaptive-regret attainability problem.

## Proof
Any feasible \\(\\sigma\\) with reward coordinate strictly larger than \\(z\\) can be mixed with \\(\\rho\\) until the reward coordinate first reaches \\(z\\). If \\(\\sigma_t=(1-t)\\rho+t\\sigma\\), joint convexity gives
\\[
D(\\rho\\|\\sigma_t)\\le tD(\\rho\\|\\sigma)<D(\\rho\\|\\sigma)
\\]
for \\(0<t<1\\). Hence every minimizer is on the boundary \\(s_z=z\\).

Write a boundary Bloch vector as \\(s=(x\\cos\\phi,x\\sin\\phi,z)\\), with \\(x\\ge0\\) and \\(q=|s|<1\\). The logarithm of a faithful qubit state has the exact form
\\[
\\log\\sigma=\\frac12\\log\\frac{1-q^2}4\\,I
+\\frac{\\operatorname{artanh}q}q\\,s\\cdot\\sigma.
\\]
Consequently
\\[
\\operatorname{Tr}(\\rho\\log\\sigma)=
\\frac12\\log\\frac{1-q^2}4
+\\frac{\\operatorname{artanh}q}q
(px\\cos\\phi+mz).
\\]
For fixed \\(x\\), the coefficient of \\(\\cos\\phi\\) is strictly positive, so the divergence is uniquely minimized at \\(\\phi=0\\). This gives the displayed one-variable function \\(D(x)\\).

On the positive-definite cone, \\(\\sigma\\mapsto-\\operatorname{Tr}(\\rho\\log\\sigma)\\) is strictly convex for faithful \\(\\rho\\), because \\(-\\log\\) is strictly operator convex and \\(\\rho>0\\). Its restriction to the affine boundary line is therefore strictly convex. Direct differentiation gives the displayed derivative. At \\(x=0\\),
\\[
D'(0)=-p\\frac{\\operatorname{artanh}z}z<0.
\\]
As \\(x\\uparrow\\sqrt{1-z^2}\\), the leading \\((1-q^2)^{-1}\\) term in \\(D'(x)\\) has coefficient \\(x[1-r\\cdot s]\\), which is positive because \\(|r|<1\\) and \\(|s|\\to1\\). Hence \\(D'(x)\\to+\\infty\\). Strict convexity gives exactly one zero and therefore the unique minimizer.

## Verification
The bundled verifier evaluates the closed form and derivative, brackets the unique stationary point for the source's running qubit instance, reproduces the stated \\(D_{\\mathrm{inf}}\\), computes \\(K_{\\mathrm{inf}}\\), and checks the resulting exploration-coefficient reduction. These finite calculations corroborate the numerical specialization only; the all-parameter reduction and uniqueness are analytic.

## Relationship to prior work
Ng's 2026 quantum-bandit paper defines the Umegaki half-space divergence, proves that it is the quantum-memory converse quantity, and reports the running qubit instance numerically. It does not give the one-dimensional analytic reduction or the minimizing Bloch coordinate above. The same paper explicitly leaves attainability of the Umegaki floor open.

Olivares and Paris study minimum quantum Kullback entropy under observable constraints, but their constrained optimization minimizes \\(D(\\sigma\\|\\rho)\\) in the first argument. The present problem minimizes \\(D(\\rho\\|\\sigma)\\) in the second argument; the two projections have different Euler equations and their exponential-family solution does not imply this result. General numerical work on optimizing quantum relative entropy likewise does not supply the qubit reward-half-space formula.

A prior qubit unitary-orbit result determines relative-entropy behavior when the spectrum of the second state is fixed and only its eigenbasis varies. Here both the spectrum and eigenbasis of \\(\\sigma\\) vary under a linear reward constraint, so that orbit result does not imply the half-space minimizer.

## Limitations
The theorem is stated for faithful noncommuting qubit arms and a rank-one projector reward. Singular arms, higher-dimensional systems, and general multi-eigenvalue effects require separate analysis. The numerical values are not a proof that the Umegaki converse is operationally attainable by a quantum-memory bandit policy.

## References
1. S. H. Ng, *The Single-Copy Quantum Bandit Is Classical: An Exact Spectral Collapse*, arXiv:2609.40339v1, first public 30 September 2026.
2. S. Olivares and M. G. A. Paris, *Quantum estimation via minimum Kullback entropy principle*, arXiv:0708.0956v3.
3. H. Fawzi and O. Fawzi, *Efficient optimization of the quantum relative entropy*, arXiv:1705.06671.
