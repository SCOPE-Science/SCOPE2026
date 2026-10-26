# Three sharp optimal stage laws for mean-preserving randomized implicit Runge–Kutta damping

## Finding

The randomized semi-implicit and implicit two-stage Runge–Kutta constructions of Bochacik and Przybyłowicz [1] have the same amplification factor on the real scalar decay equation. Their usual uniformly sampled internal stage can be replaced by any probability law of mean one half. Within **all** such laws, the law minimizing expected squared amplification changes structure at two exact stiffness thresholds: endpoint sampling, asymmetric two-point sampling, and finally a deterministic midpoint.

For \(s>0\), put
\[
 c=\frac{\sqrt{17}-1}{4},\qquad d=\frac{2}{\sqrt3},\qquad
 a_s=\frac{2s^2+s-2}{s(s+2)}.
\]
For a probability measure \(\mu\) on \([0,1]\), let \(T\sim\mu\) and impose \(\mathbb ET=1/2\). Set
\[
 R_s(t)=\frac{1-s+st}{1+st},\qquad M_s(\mu)=\mathbb E_\mu[R_s(T)^2].
\]
The **unique** minimizer \(\mu_s^*\), among all Borel probability measures satisfying the mean condition, is
\[
\begin{array}{ll}
0<s\le c:&\displaystyle\mu_s^*=\frac12\delta_0+\frac12\delta_1,\\
c<s<d:&\displaystyle\mu_s^*=p_s\delta_{a_s}+(1-p_s)\delta_1,
\quad p_s=\frac1{2(1-a_s)},\\
s\ge d:&\displaystyle\mu_s^*=\delta_{1/2}.
\end{array}
\]
In the middle interval \(0<a_s<1/2\) and \(0<p_s<1\). The sharp optimal squared-amplification value is
\[
\inf_{\mu:\,\mathbb ET=1/2}M_s(\mu)=
\begin{cases}
\displaystyle\frac{s^4-2s^2+2}{2(1+s)^2},&0<s\le c,\\
\displaystyle\frac{8+4s-4s^2-s^3}{8(1+s)^3},&c<s<d,\\
\displaystyle\frac{(2-s)^2}{(2+s)^2},&s\ge d.
\end{cases}
\]
The values agree at both thresholds. In particular, for \(s=1\), the unique optimum samples \(T=1/3\) with probability \(3/4\) and \(T=1\) with probability \(1/4\); it yields \(M_1=7/64<1/9\), the squared amplification of the deterministic midpoint. For \(s=1/2\), the endpoint mixture yields \(25/72<9/25\). For \(s\ge d\), no nontrivial mean-preserving stage randomization can match the deterministic midpoint's squared amplification.

## Assumptions and scope

Consider the real test equation \(u'(t)=-\lambda u(t)\) with \(\lambda>0\), a fixed positive step \(h\), and \(s=\lambda h\). Draw each internal stage fraction \(T_k\in[0,1]\) independently from the same prescribed law \(\mu\) with \(\mathbb ET_k=1/2\). Only the exact, scalar one-step damping factor and its iterates are assessed; the law may depend on the dimensionless stiffness \(s\). The degenerate midpoint law is allowed. No random forcing or oracle noise is added.

For either randomized implicit construction in [1], direct solution of the linear stage equation gives \(u_{k+1}=R_s(T_k)u_k\). Consequently, for every deterministic \(u_0\in\mathbb R\) and integer \(k\ge0\),
\[
\mathbb E|u_k|^2=|u_0|^2\bigl(M_s(\mu)\bigr)^k.
\]
Thus the distributional minimization is **simultaneously** optimal at every positive step count for squared norm of the numerical iterate, not a claim about global error to the exact solution or accuracy for general time-dependent differential equations.

## Proof

Let \(g_s(t)=R_s(t)^2\) on \([0,1]\). Because \(1+st>0\), all expressions below are well defined. Minimization over measures with mean \(1/2\) will follow from three global affine lower supports for \(g_s\), each with a uniquely determined equality set.

**Endpoint regime.** Let \(L_{0,s}(t)=(1-t)g_s(0)+t g_s(1)\). Exact rational simplification yields
\[
g_s(t)-L_{0,s}(t)
=\frac{s^3t(t-1)\bigl(s(s^2-2)t+2s^2+s-2\bigr)}{(1+s)^2(1+st)^2}.
\]
If \(0<s\le c\), then \(s^2<2\) and \(2s^2+s-2\le0\), so the parenthesized affine factor is negative for every \(0<t<1\). Therefore \(g_s(t)>L_{0,s}(t)\) in the open interval, with equality at the endpoints only. Integrating and using the imposed mean gives \(M_s(\mu)\ge L_{0,s}(1/2)\). Equality forces support on \(\{0,1\}\) and the mean fixes the two masses to \(1/2\), proving uniqueness. Evaluating the chord gives the first expression for the minimum.

**Asymmetric two-point regime.** Define
\[
a_s=\frac{2s^2+s-2}{s(s+2)},\qquad
L_{a,s}(t)=g_s(a_s)+g_s'(a_s)(t-a_s).
\]
The exact tangency identity is
\[
g_s(t)-L_{a,s}(t)
=\frac{s(1-t)\,[s(s+2)(t-a_s)]^2}{4(1+s)^3(1+st)^2}\ge0.
\]
The function \(a_s\) is strictly increasing because
\[
a_s'=\frac{3s^2+4s+4}{s^2(s+2)^2}>0,
\]
and \(a_c=0\), \(a_d=1/2\). Thus \(0<a_s<1/2\) when \(c<s<d\). The lower support touches \(g_s\) exactly at \(\{a_s,1\}\), and every mean-half measure satisfies \(M_s(\mu)\ge L_{a,s}(1/2)\). The unique feasible measure supported on the two contact points gives the stated masses. Direct evaluation of \(L_{a,s}(1/2)\) gives the middle formula.

**Midpoint regime.** The tangent \(L_{m,s}(t)=g_s(1/2)+g_s'(1/2)(t-1/2)\) obeys
\[
g_s(t)-L_{m,s}(t)=
\frac{s^3(2t-1)^2\bigl[2s(s-2)t+s^2+4s-4\bigr]}
{(s+2)^3(1+st)^2}.
\]
For \(d\le s\le2\), the bracket is decreasing in \(t\) and has minimum \(3s^2-4\ge0\) at \(t=1\). For \(s\ge2\), it is increasing and has minimum \(s^2+4s-4>0\) at \(t=0\). Hence it is nonnegative throughout \([0,1]\). The mean constraint yields \(M_s(\mu)\ge g_s(1/2)\), with equality only for \(\mu=\delta_{1/2}\). At \(s=d\), the additional point \(t=1\) contacts the tangent but cannot receive positive mass in a mean-half law supported at \(\{1/2,1\}\). The minimum is \(((2-s)/(2+s))^2\), as asserted.

These regimes cover every \(s>0\), and the equality arguments prove the uniqueness at both thresholds as well. Substitution verifies continuity of the piecewise minimum and the stated rational examples. Independence of stages then gives the exact all-step moment law above. \(\square\)

## Verification

The standalone file `CHECK.py` uses exact symbolic factorization to verify all three global support identities, the mass identities, the optimum values and their agreement at the regime boundaries. It also checks illustrative rational two-point designs exhaustively over a finite grid; these grid calculations are **not** used to infer any universal inequality. Run `python CHECK.py` with Python and SymPy installed. The analytical affine support inequalities above prove the unrestricted distributional optimization.

## Relationship to prior work

Bochacik and Przybyłowicz [1] introduced the two implicit randomized Runge–Kutta constructions, used independent **uniform** stage fractions, and analyzed their mean-square and almost-sure stability regions. In particular, the uniform-law real mean-square stability boundary is investigated in their Section 3.2. The present theorem instead solves the moment-constrained optimization over **every** stage probability law, including atomic and degenerate laws; it does not assert a new stability formula for the uniform law. The earlier randomized explicit Runge–Kutta analysis [2] studies a different multiplier and uniform stage sampling, so it does not supply this implicit-scheme distributional optimizer.

## Limitations

The optimization concerns one real negative Dahlquist mode with known \(s\), squared amplification, and independent stages. Its optimal law varies with \(s\), so it is not automatically jointly optimal across a spectrum of modes. The mean-half constraint is a specified design restriction, not a proof of quadrature unbiasedness for arbitrary irregular time dependence. The result does not establish a global strong or weak convergence order on nonlinear or nonautonomous differential equations, nor an improvement in approximation error to the exact solution. The supporting-line approach is elementary in principle; a broader general theorem in probability-measure moment optimization might imply this specialization, and publication priority remains subject to wider literature inspection.

## References

[1] T. Bochacik and P. Przybyłowicz, *Convergence and stability of randomized implicit two-stage Runge–Kutta schemes*, arXiv:2404.19059, first submitted 2024-04-29, especially Sections 1.2 and 3; https://arxiv.org/abs/2404.19059 .

[2] T. Bochacik, M. Goćwin, P. M. Morkisz, and P. Przybyłowicz, *Randomized Runge–Kutta method—stability and convergence under inexact information*, arXiv:2006.12131, first submitted 2020-06-22, especially Sections 2 and 5; https://arxiv.org/abs/2006.12131 .
