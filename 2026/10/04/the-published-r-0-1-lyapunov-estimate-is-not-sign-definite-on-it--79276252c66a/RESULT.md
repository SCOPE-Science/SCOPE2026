# The published \(R_0<1\) Lyapunov estimate is not sign-definite on its stated feasible region

## Finding

For the fractional SEARQ social-media-addiction model in Khirsariya and Aldosary (2026), the Lyapunov candidate used in Theorem 5.2 is not sign-definite on the full feasible region under the theorem's stated hypothesis \(R_0<1\). With
\[
L_0=\varphi\phi E+(\phi+\mu)A,
\]
the model gives the exact identity
\[
{}^{C}D_t^\alpha L_0=(\phi+\mu)(\mu+\varsigma+\rho)A\left(R_0\frac{S}{S^0}-1\right),
\qquad S^0=\frac{\pi}{\omega+\mu}.
\]
On the paper's stated feasible region
\[
\Omega=\left\{(S,E,A,R,Q)\in\mathbb R_+^5:S+E+A+R+Q\le\frac{\pi}{\mu}\right\},
\]
this derivative is nonpositive at every state if and only if
\[
R_0\le\frac{\mu}{\omega+\mu}.
\]
Hence the proof step that replaces \(S\) by \(S^0\) is not valid on all of \(\Omega\), and the published Lyapunov calculation does not establish the claimed global result on the entire interval \(\mu/(\omega+\mu)<R_0<1\).

## Assumptions and scope

The calculation uses the paper's system (2.1), its addiction-free equilibrium susceptible coordinate \(S^0=\pi/(\omega+\mu)\), its reproduction number in equation (5.5), and its feasible region in equation (4.4). Parameters \(\pi,\mu,\omega,\phi,\varphi,\beta,\vartheta,\varsigma\) are positive and \(\rho\ge0\), as required for the displayed expressions. The source also imposes the transmission-coefficient identification used in its total-population balance; no additional dynamical assumption is needed for the algebra below.

The claim concerns the exact Lyapunov candidate printed in Theorem 5.2 and the theorem's stated feasible region. It is not a claim that global asymptotic stability itself is false for every parameter choice with \(R_0<1\).

## Proof

The relevant infected-state equations are
\[
{}^{C}D_t^\alpha E=\beta\vartheta AS-(\phi+\mu)E,
\]
\[
{}^{C}D_t^\alpha A=\varphi\phi E-(\mu+\varsigma+\rho)A.
\]
The published proof chooses
\[
L_0=\varphi\phi E+(\phi+\mu)A.
\]
By linearity of the Caputo derivative,
\[
\begin{aligned}
{}^{C}D_t^\alpha L_0
&=\varphi\phi\left(\beta\vartheta AS-(\phi+\mu)E\right)
 +(\phi+\mu)\left(\varphi\phi E-(\mu+\varsigma+\rho)A\right)\\
&=A\left(\varphi\phi\beta\vartheta S-(\phi+\mu)(\mu+\varsigma+\rho)\right).
\end{aligned}
\]
Using the source definition
\[
R_0=\frac{\beta\vartheta\varphi\phi S^0}{(\phi+\mu)(\mu+\varsigma+\rho)},
\]
we obtain
\[
{}^{C}D_t^\alpha L_0=(\phi+\mu)(\mu+\varsigma+\rho)A\left(R_0\frac{S}{S^0}-1\right).
\]

The feasible-region bound is \(S\le\pi/\mu\), not \(S\le S^0\). Since
\[
\frac{\pi/\mu}{S^0}=\frac{\omega+\mu}{\mu},
\]
the derivative is nonpositive for every state of \(\Omega\) exactly when
\[
R_0\frac{\omega+\mu}{\mu}\le1,
\]
which is equivalent to
\[
R_0\le\frac{\mu}{\omega+\mu}.
\]
This proves sufficiency for all-state sign-definiteness.

For necessity, suppose
\[
\frac{\mu}{\omega+\mu}<R_0<1.
\]
Then \(S^0/R_0<\pi/\mu\). Choose any
\[
S\in\left(\frac{S^0}{R_0},\frac{\pi}{\mu}\right)
\]
and choose \(A>0\) small enough that \(S+A\le\pi/\mu\), with \(E=R=Q=0\). This state belongs to \(\Omega\), but \(R_0S/S^0>1\), so the displayed Caputo derivative is strictly positive.

An exact rational witness is
\[
\pi=\mu=\omega=\phi=\varphi=\vartheta=\varsigma=\rho=1,\qquad \beta=9.
\]
Then \(S^0=1/2\), \(R_0=3/4<1\), and at
\[
(S,E,A,R,Q)=\left(\frac45,0,\frac1{10},0,0\right)
\]
the total population is \(9/10\le1=\pi/\mu\), while
\[
{}^{C}D_t^\alpha L_0=\frac3{25}>0.
\]

## Verification

The accompanying `verify.py` reproduces the rational witness and the factorization with exact `Fraction` arithmetic. It checks the feasible-region inequality, \(R_0=3/4\), the sharp all-state threshold \(\mu/(\omega+\mu)=1/2\), and the positive derivative \(3/25\). The proof itself is symbolic and does not depend on numerical experimentation.

## Relationship to prior work

The source's deterministic model family traces to Alemneh and Alemu (2021), whose addiction-free global-stability result used a Castillo-Chavez decomposition rather than this fractional Lyapunov estimate. Kongson et al. (2021) studied a closely related five-compartment fractional social-media-addiction model with an Atangana-Baleanu-Caputo operator, but does not supply the sharp sign condition above for the 2026 theorem. Ali et al. (2024) analyzed a different six-compartment social-media-addiction/depression model and likewise used a Castillo-Chavez global-stability argument.

The present statement is source-specific: it compares the exact derivative of the exact Lyapunov function printed in Theorem 5.2 with the feasible region printed earlier in the same article. Targeted searches for the theorem, its inequality \(S\le S^0\), and equivalent threshold formulations did not locate a published correction or a prior statement of the sharp condition \(R_0\le\mu/(\omega+\mu)\) for this candidate.

## Limitations

The argument proves that the printed Lyapunov calculation is not sign-definite on the full stated feasible region when \(\mu/(\omega+\mu)<R_0<1\). It does not prove that the addiction-free equilibrium is unstable there, nor does it rule out a different Lyapunov function, an invariant-set refinement reached after positive time, or another global-stability argument. It also does not alter the local threshold calculation by itself.

## References

1. S. R. Khirsariya and S. F. Aldosary, “A fractional social media addiction model: graphical interpretation and numerical analysis,” *Boundary Value Problems* (2026), article 138. DOI: `10.1186/s13661-026-02279-9`.
2. H. T. Alemneh and N. Y. Alemu, “Mathematical modeling with optimal control analysis of social media addiction,” *Infectious Disease Modelling* 6 (2021), 405–419. DOI: `10.1016/j.idm.2021.01.011`.
3. J. Kongson et al., “On analysis of a nonlinear fractional system for social media addiction involving Atangana–Baleanu–Caputo derivative,” *Advances in Difference Equations* (2021). DOI: `10.1186/s13662-021-03515-5`.
4. A. Ali et al., “Mathematical modelling, analysis and numerical simulation of social media addiction and depression,” *PLOS ONE* 19 (2024), e0293807. DOI: `10.1371/journal.pone.0293807`.
