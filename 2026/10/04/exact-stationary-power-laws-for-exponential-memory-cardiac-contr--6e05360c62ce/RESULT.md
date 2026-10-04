# Exact stationary power laws for exponential-memory cardiac control
## Finding
Consider the published controlled cardiac oscillator, written as an autonomous flow on \(\mathbb R^3\times\mathbb S^1\):
\[
\dot x=y,
\qquad
\dot y=-a(x-v_1)(x-v_2)y-\frac{x(x+d)(x+e)}{de}+A\sin\theta-\alpha u,
\]
\[
\dot u=y-\beta u,
\qquad
\dot\theta=\omega.
\]
For every compactly supported invariant probability measure \(\mu\), the following identities hold:
\[
\left\langle\frac{x(x+d)(x+e)}{de}\right\rangle_\mu=0,
\qquad
\langle uy\rangle_\mu=\beta\langle u^2\rangle_\mu,
\]
and
\[
\alpha\beta\langle u^2\rangle_\mu
=A\langle y\sin\theta\rangle_\mu
-a\langle(x-v_1)(x-v_2)y^2\rangle_\mu.
\]
Hence the feedback force \(-\alpha u\) contributes the exact mean power
\[
\langle(-\alpha u)y\rangle_\mu=-\alpha\beta\langle u^2\rangle_\mu\le0.
\]
If \(A\ne0\), \(\omega\ne0\), \(\alpha>0\), and \(\beta>0\), then \(\langle u^2\rangle_\mu>0\) for every compact invariant probability measure, so the controller's mean power is strictly negative.

## Assumptions and scope
The statement concerns the deterministic controlled system printed as System (16) in Yahalom and Puzanov, with \(de\ne0\). The strict inequality uses nonzero periodic forcing \(A\ne0\), nonzero phase speed \(\omega\ne0\), and positive controller parameters \(\alpha,\beta>0\). The identities apply to any compactly supported invariant probability measure of the phase-extended flow, including measures supported on periodic or chaotic recurrent responses. They do not assert pointwise monotonic decay of total energy.

For the cardiac example in the source, \(a=0.5\), \(v_1=0.97\), \(v_2=-1\), \(d=3\), \(e=6\), \(A=2.5\), and \(\omega=1.9\), so the strict mean-power conclusion applies to all three displayed positive controller choices.

## Proof
Let
\[
G(x)=\frac{x(x+d)(x+e)}{de},
\qquad
U(x)=\frac{x^2}2+\frac{d+e}{3de}x^3+\frac1{4de}x^4,
\]
so \(U'(x)=G(x)\). Define
\[
\mathcal E(x,y,u)=\frac12y^2+U(x)+\frac{\alpha}{2}u^2.
\]
Substitution of the vector field gives the exact pointwise identity
\[
\dot{\mathcal E}
=-a(x-v_1)(x-v_2)y^2-\alpha\beta u^2+A y\sin\theta.
\]
The mixed terms \(-\alpha uy\) and \(+\alpha uy\) cancel exactly.

For a compactly supported invariant probability measure, the integral of the generator applied to any smooth observable vanishes. Applying this to \(u^2/2\) gives
\[
0=\langle u(y-\beta u)\rangle_\mu,
\]
hence \(\langle uy\rangle_\mu=\beta\langle u^2\rangle_\mu\). Therefore the mean mechanical power of the feedback force \(-\alpha u\) is exactly \(-\alpha\beta\langle u^2\rangle_\mu\).

Applying invariance to \(x\) gives \(\langle y\rangle_\mu=0\), and then to \(u\) gives \(\langle u\rangle_\mu=0\). Because \((x-v_1)(x-v_2)y\) is the derivative along the flow of an antiderivative of \((x-v_1)(x-v_2)\), its invariant mean is zero. Since \(\dot\theta=\omega\ne0\), the phase marginal of any invariant probability measure is rotation-invariant, hence \(\langle\sin\theta\rangle_\mu=0\). Averaging the \(y\)-equation therefore yields \(\langle G(x)\rangle_\mu=0\).

Finally, averaging \(\dot{\mathcal E}\) gives the stated power decomposition. For strictness, suppose \(\langle u^2\rangle_\mu=0\). Continuity and nonnegativity force the support of \(\mu\) into \(u=0\). Invariance of the support then gives \(y=0\) from \(\dot u=y-\beta u\), and \(x\) is constant from \(\dot x=y\). But \(\theta\) traverses the circle when \(\omega\ne0\), while invariance of \(y=0\) would require \(-G(x)+A\sin\theta=0\) for every phase. This is impossible when \(A\ne0\). Thus \(\langle u^2\rangle_\mu>0\).

## Verification
The bundled symbolic checker verifies \(U'(x)=G(x)\), the complete cancellation in \(\dot{\mathcal E}\), and the polynomial primitive used for the invariant mean of the nonlinear damping term. The measure identities and strictness step are analytic consequences of invariance and support invariance, not finite numerical experiments.

## Relationship to prior work
Yahalom and Puzanov introduce the exponential-memory control \(u(t)=\int_0^t e^{-\beta(t-s)}y(s)\,ds\), convert it to the state equation \(\dot u=y-\beta u\), derive local linear stability conditions, and demonstrate numerically that several controller choices regularize the chaotic cardiac response. The article does not state the invariant-measure identities above or the exact nonlinear mean-power decomposition.

The earlier cardiac-control paper by Ferreira, de Paula, and Savi studies extended time-delayed feedback rather than this exponential-memory state, so its control equations do not imply these source-specific stationary laws. Standard passivity of a stable first-order filter is closely related to the sign of the controller term; the additional result here is the exact source-specific recurrent-state identity, strictness under nonzero periodic forcing, and its coupling to the nonlinear cardiac energy balance.

## Limitations
The result is a structural statement about recurrent statistical states. It does not prove existence, uniqueness, or global attraction of a periodic orbit for any controller parameters, and it does not replace the source's numerical bifurcation or stabilization analysis. Pointwise controller power \(-\alpha uy\) may have either sign; only its invariant mean is forced negative. The originality comparison cannot exclude every possible formulation in the general passivity literature, so the claim is deliberately limited to the exact identities for this published controlled oscillator.

## References
1. A. Yahalom and N. Puzanov, “Feedback Stabilization Applied to Heart Rhythm Dynamics Using an Integro-Differential Method,” Mathematics 12 (2024), 158. DOI: 10.3390/math12010158.
2. A. Yahalom and N. Puzanov, “Feedback stabilization applied to heart rhythm dynamics with integro-differential equations method,” preprint, first posted 2023-07-04. DOI: 10.21203/rs.3.rs-2853196/v1.
3. B. B. Ferreira, A. S. de Paula, and M. A. Savi, “Chaos Control Applied to Heart Rhythm Dynamics,” Chaos, Solitons & Fractals 44 (2011), 587–599. DOI: 10.1016/j.chaos.2011.05.009.
