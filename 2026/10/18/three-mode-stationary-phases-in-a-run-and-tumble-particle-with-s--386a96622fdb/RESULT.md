# Three-mode stationary phases in a run-and-tumble particle with saturating rates

## Finding

A one-dimensional run-and-tumble particle with saturating spatially dependent speeds and tumbling rates can have **exactly three strict local maxima** in its stationary position density: one at the origin and one on each side. This behavior occurs on an open set of admissible parameters. On the natural rate-length slice where the tumbling-rate steepness is four times the speed steepness, the entire classification into one, two, or three strict maxima is determined by a strictly concave cubic.

For \(v_0>v_1>0\), \(\gamma_0>\gamma_1>0\), and \(u>0\), consider the right- and left-moving speeds and switching rates

\[
v_\pm(x)=v_0\mp v_1\tanh(ux),\qquad
\gamma_\pm(x)=\gamma_0\pm\gamma_1\tanh(4ux).
\]

Define

\[
k=uv_1^2,\quad m=\gamma_0v_1,\quad n=4\gamma_1v_0,\qquad
Q(y)=(k-m-ky)(1+6y+y^2)-n(1+y).
\]

The stationary position density is even and positive, and has **at most three strict local maxima**. Write \(q_0=Q(0)\), \(q_1=Q'(0)\), and \(q_{\max}=\max_{0\le y\le1}Q(y)\). The exhaustive strict-maxima classification is:

1. **Three maxima:** \(q_0<0<q_{\max}\). There are two simple roots \(0<y_-<y_+<1\); the origin and the two positions \(\pm u^{-1}\operatorname{artanh}\sqrt{y_+}\) are strict local maxima, and \(\pm u^{-1}\operatorname{artanh}\sqrt{y_-}\) are strict local minima.
2. **Two maxima:** \(q_0>0\), or \(q_0=0\) and \(q_1>0\). The origin is a local minimum (possibly flat), and there is exactly one strict maximum on each side.
3. **One maximum:** all other cases. The origin is the unique strict local maximum. Equality \(q_{\max}=0\) with \(q_0<0\) produces two horizontal shoulders, not further maxima.

In particular, at the strictly admissible parameter point

\[
(v_0,v_1,\gamma_0,\gamma_1,u,g)
=(1,\tfrac12,\tfrac38,\tfrac14,4,16),
\]

where \(g=4u\), the cubic is

\[
Q(y)=\frac{-3+46y-83y^2-16y^3}{16}.
\]

Its signs are exactly \(Q(0)=-3/16<0\), \(Q(1/4)=49/256>0\), and \(Q(1)=-7/2<0\). Therefore this stationary density has exactly three strict maxima and two strict minima. This exhibits a genuinely trimodal stationary phase in an open parameter neighborhood, not a fine-tuned limiting case.

## Assumptions and scope

The particle evolves on the entire real line. In state \(+\), it moves deterministically at velocity \(+v_+(x)\) and switches to state \(-\) at intensity \(\gamma_+(x)\); in state \(-\), it moves at velocity \(-v_-(x)\) and switches to state \(+\) at intensity \(\gamma_-(x)\). All parameter inequalities above are strict. There is no translational Brownian noise. The base model allows two independent positive steepness parameters \(u\) and \(g\); the complete cubic trichotomy concerns the slice \(g=4u\), while the displayed example persists for nearby independent \(g\) and \(u\).

Because the speeds are bounded away from zero, the jump intensities are strictly positive, and the outward-directed drift of the logarithmic stationary flux is strictly negative at both spatial tails, the standard zero-current stationary solution is integrable and determines the stationary density. The stationary density decays exponentially in \(|x|\) in the strict-speed regime \(v_0>v_1\).

## Proof

**Stationary density and its logarithmic derivative.** The stationary forward equations imply a constant total flux. Integrability at spatial infinity forces zero flux, so \(v_+p_+=v_-p_-=:J(x)\). The remaining equation then gives

\[
J'(x)=J(x)\left[\frac{\gamma_-(x)}{v_-(x)}-\frac{\gamma_+(x)}{v_+(x)}\right].
\]

Consequently, for a positive normalizing constant \(C\),

\[
p(x)=C\left(\frac1{v_+(x)}+\frac1{v_-(x)}\right)
\exp\left\{\int_0^x\left[\frac{\gamma_-(s)}{v_-(s)}-\frac{\gamma_+(s)}{v_+(s)}\right]ds\right\}.
\]

The prefactor and exponent are both even in \(x\). At positive infinity the integrand approaches \(-2(\gamma_0v_1+\gamma_1v_0)/(v_0^2-v_1^2)<0\), proving exponential integrability. Direct differentiation yields, with \(t=\tanh(ux)\),

\[
\frac{p'(x)}{p(x)}=
\frac{2}{v_0^2-v_1^2t^2}
\left[k t(1-t^2)-mt-\gamma_1v_0\tanh(4ux)\right].
\]

**Exact cubic reduction.** The fourfold hyperbolic-angle identity states

\[
\tanh(4\operatorname{artanh}t)=\frac{4t(1+t^2)}{1+6t^2+t^4}.
\]

For \(x>0\), put \(y=t^2\in(0,1)\). Substitution gives the exact factorization

\[
\boxed{\frac{p'(x)}{p(x)}=
\frac{2t\,Q(y)}{(v_0^2-v_1^2t^2)(1+6y+y^2)}.}
\]

Every factor outside \(Q(y)\) is strictly positive for \(x>0\). Thus the sign of the stationary density's derivative is exactly the sign of \(Q(y)\). The map \(x\mapsto y\) is strictly increasing from \((0,\infty)\) onto \((0,1)\).

**Strict concavity and exhaustive classification.** Expanding the polynomial,

\[
Q(y)=(k-m-n)+(5k-6m-n)y-(5k+m)y^2-ky^3,
\]

so

\[
Q''(y)=-2(5k+m)-6ky<0,\qquad Q(1)=-8m-2n<0.
\]

Therefore \(Q'\) is strictly decreasing on \([0,1]\), \(Q'(1)=-8k-8m-n<0\), and \(Q\) has at most two zeros on \((0,1)\). When \(Q(0)<0\), precisely two simple roots occur if and only if \(\max_{[0,1]}Q>0\). Their signs alternate negative, positive, negative, giving the two local minima followed by two off-center maxima, together with a strict origin maximum. If \(Q(0)>0\), there is exactly one root and the origin is a strict local minimum. If \(Q(0)=0\), the sign immediately to its right is positive exactly when \(Q'(0)>0\); otherwise strict concavity forces it to be negative. These alternatives give the claimed full classification, including degenerate shoulder cases. There are no other strict extrema.

**Strict, open trimodality.** For the displayed rational parameters, the polynomial has strictly negative, positive, and negative values at \(0\), \(1/4\), and \(1\), respectively. Strict concavity forces exactly two simple roots in \((0,1)\). The origin's curvature satisfies \(p''(0)/p(0)=2uQ(0)/v_0^2=-3/2<0\), so all three maxima are strict. The off-center critical points are nondegenerate because both roots are simple and \(dy/dx>0\). Their persistence, together with the strict origin curvature, follows from continuity and the implicit function theorem for all sufficiently small independent perturbations of the six physical parameters, including perturbations away from \(g=4u\).

## Verification

The standalone `VERIFY.py` script uses rational arithmetic to check the four-angle identity, the cubic coefficient identity, strict concavity, endpoint values, and the exact rational three-sign witness. It separately compares direct stationary-log-derivative evaluations with the polynomial sign at 400 positive positions. Executed with Python 3, it reports **6,407 checks passed**. The checks validate symbolic manipulations and one reproducibility witness; the global trichotomy is established by the analytic argument above, not by sampling.

For the rational example, the positive root positions are approximately \(x_-=0.0706086037\) and \(x_+=0.1978814642\), corresponding respectively to the positive-side minimum and maximum. These approximations are not used in the proof.

## Relationship to prior work

Monthus (2021) gives the general zero-current stationary law for spatially dependent run-and-tumble speeds and switching intensities. Jain and Chatterjee (arXiv:2405.13521, first public version 22 May 2024) specialize to the saturating hyperbolic-tangent model, supply the stationary density, and investigate its mode transition. Their discussion before the unimodal/bimodal criterion explicitly conditions on an assumed bound of two maxima; it does not establish the general triple-mode phase or the cubic phase analysis given here. This finding claims neither the general stationary-density formula nor the exact tanh model as new. Bressloff (2021) treats trapping with constant-speed and inhomogeneous switching in a distinct setting.

The present contribution is an exact **modal-count theorem** for the fourfold steepness slice and an explicit **admissible trimodal regime** that demonstrates why origin curvature alone cannot classify the global stationary shape. General stationary formulas provide the starting point but do not supply this classification.

## Limitations

The exact at-most-three maximum theorem is proved only for \(g=4u\), not for all independent positive steepness pairs. Near the explicit example, existence of three strict maxima persists without that equality, but an unrestricted global maximum-count theorem is not asserted. The density is smooth; the analysis does not cover singular zero-speed boundaries or finite-time transient densities. Algebraic reduction does not establish uniqueness of the scientific observation in all unpublished literature. There has been no independent external audit.

## References

1. K. Jain and S. Chatterjee, *Run-and-tumble particle with saturating rates*, arXiv:2405.13521 (first posted 22 May 2024), https://arxiv.org/abs/2405.13521 ; full preprint https://arxiv.org/pdf/2405.13521. Especially equations (1)–(4), (7)–(17) and Appendix A.
2. C. Monthus, *Large deviations at various levels for run-and-tumble processes with space-dependent velocities and space-dependent switching rates*, arXiv:2103.08885 (2021), https://arxiv.org/pdf/2103.08885. Especially Section II and Appendix A.
3. P. C. Bressloff, *Trapping of a run-and-tumble particle in an inhomogeneous domain: the weak noise limit*, arXiv:2102.10372 (2021), https://arxiv.org/pdf/2102.10372. Especially Sections II–III.
