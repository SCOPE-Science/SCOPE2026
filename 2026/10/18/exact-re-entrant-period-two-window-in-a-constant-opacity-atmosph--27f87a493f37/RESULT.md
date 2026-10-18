# Exact re-entrant period-two window in a constant-opacity atmospheric map

## Finding

Consider the constant-opacity atmospheric map of Bromley and Chiang,
\[
F_{p_1,p_2,\gamma}(x)=p_1\exp\!\left[p_2\left(2^{-1/4}-\bigl(a+b e^{-\gamma x}\bigr)^{-1/4}\right)\right],\qquad x\ge0,
\]
where \(p_1,p_2>0\), \(\gamma>1\), \(a=1+\gamma^{-1}\), and \(b=1-\gamma^{-1}\). Define, for \(t>0\),
\[
\Phi_\gamma(t)=\frac{b}{4}\,t e^{-t}(a+b e^{-t})^{-5/4},\qquad
R_\gamma(t)=\frac{b e^{-t}}{a+b e^{-t}}.
\]
There is a unique \(t_\gamma\in(1,8/3)\) satisfying
\[
\frac1{t_\gamma}-1+\frac54 R_\gamma(t_\gamma)=0.
\]
Set \(p_{2,\mathrm{crit}}(\gamma)=1/\Phi_\gamma(t_\gamma)\).

**Exact global phase theorem.** For every \(p_1,p_2>0\) and \(\gamma>1\):

1. The map has exactly one positive fixed point \(x_*\). If \(p_2\le p_{2,\mathrm{crit}}(\gamma)\), every orbit in \([0,\infty)\) converges to \(x_*\), and there is no primitive two-cycle.
2. If \(p_2>p_{2,\mathrm{crit}}(\gamma)\), the equation \(p_2\Phi_\gamma(t)=1\) has exactly two solutions \(0<t_-<t_\gamma<t_+\). Define
\[
 p_1^{\pm}=\frac{t_\pm}{\gamma}\exp\!\left[p_2\left((a+b e^{-t_\pm})^{-1/4}-2^{-1/4}\right)\right].
\]
These satisfy \(0<p_1^-<p_1^+\). Precisely for \(p_1^-<p_1<p_1^+\), the map has one primitive two-cycle \(\{x_-,x_+\}\) with \(x_-<x_*<x_+\). The two-cycle is attracting, every orbit other than the fixed-point orbit tends to it, and the fixed point is repelling. For \(p_1\le p_1^-\) or \(p_1\ge p_1^+\), every orbit converges to the unique fixed point and there is no primitive two-cycle. Both threshold endpoints are included in this last assertion, even though the fixed-point multiplier is then exactly \(-1\).

In particular, increasing \(p_1\) at fixed \(p_2>p_{2,\mathrm{crit}}\) gives a **fixed point, then a unique attracting two-cycle, then a fixed point again**. All statements hold for arbitrary initial \(x\ge0\). As an illustrative numerical evaluation (not an interval certificate), \(\gamma=3\), \(p_2=30\) gives \(p_{2,\mathrm{crit}}\approx28.343173522\) and \((p_1^-,p_1^+)\approx(1.149552000,4.045507638)\).

## Assumptions and scope

The state \(x\) is nonnegative optical depth. The three parameters are constant throughout an orbit. The strict condition \(\gamma>1\) is essential: it selects the decreasing (nuclear-winter) branch. No stochastic forcing, evolving opacity, finite-precision dynamics, or time-varying parameters are assumed. Claims about convergence are for infinite exact-real iterations, not fixed finite iteration counts.

## Proof

**1. Fixed point and slope parametrization.** Write \(c=2^{-1/4}\), \(u=e^{-\gamma x}\), and \(h(x)=(a+bu)^{-1/4}\). Since \(b>0\),
\[
 h'(x)=\frac{b\gamma}{4}\,u(a+bu)^{-5/4}>0,\qquad F'(x)=-p_2F(x)h'(x)<0.
\]
Thus \(F(0)=p_1>0\), \(F\) is positive, strictly decreasing and bounded, and \(F(x)-x\) changes sign exactly once. At its unique positive fixed point \(x_*\),
\[
 |F'(x_*)|=p_2x_*h'(x_*)=p_2\Phi_\gamma(\gamma x_*).
\]
Solving \(F(x_*)=x_*\) for \(p_1\) gives
\[
 p_1=x_*\exp[p_2(h(x_*)-c)].
\]
The derivative of the right side is \(\exp[p_2(h-c)](1+p_2x_*h')>0\); its range as \(x_*\) runs from zero to infinity is \((0,\infty)\). Hence the fixed point traverses the entire positive half-line strictly monotonically with \(p_1\).

**2. The sharp slope threshold.** Direct logarithmic differentiation gives
\[
 \frac{\Phi_\gamma'(t)}{\Phi_\gamma(t)}
 =\frac1t-1+\frac54 R_\gamma(t).
\]
The function \(R_\gamma(t)\) is strictly decreasing, with \(0<R_\gamma(t)<1/2\), so the displayed logarithmic derivative decreases strictly from \(+\infty\) to \(-1\). It is positive at \(t=1\), negative at \(t=8/3\), and has exactly one zero \(t_\gamma\). Since \(\Phi_\gamma(t)>0\) and tends to zero at both ends, this zero is its unique strict global maximum. The parameter-plane alternatives and the two positive threshold solutions follow from the formula for \(|F'(x_*)|\) in step 1.

**3. A uniform strict Schwarzian bound.** For a smooth map \(f\) with nonvanishing derivative, put \(Sf=f'''/f'-\tfrac32(f''/f')^2\). The Schwarzian composition identity \(S(f\circ g)=(Sf\circ g)(g')^2+Sg\), together with \(S(e^z)=-1/2\), \(S(e^{-\gamma x})=-\gamma^2/2\), and \(S(z^{-1/4})=15/(32z^2)\), gives the exact identity
\[
 SF(x)=\gamma^2\left(-\frac12+\frac{15}{32}R_\gamma(\gamma x)^2\right)-\frac{p_2^2}{2}h'(x)^2
 <-\frac{49}{128}\gamma^2<0.
\]
Here the strict inequality uses \(R_\gamma<1/2\). Consequently the increasing map \(G=F^2\) also has \(SG<0\) everywhere, since \(SG=(SF\circ F)(F')^2+SF\). The function \(Q=(G')^{-1/2}\) is strictly convex because \(Q''=-\tfrac12(SG)Q>0\).

**4. Complete classification of period two.** Fixed points of \(G\) are the unique fixed point \(x_*\) and any members of primitive two-cycles. There are at most three distinct fixed points of \(G\): four such roots of \(G(x)-x\) would give, by Rolle's theorem, three distinct solutions of \(G'(x)=1\), equivalently three intersections of strictly convex \(Q\) with height one, which is impossible. If three roots \(x_-<x_*<x_+\) exist, Rolle's theorem produces two points \(c_-\in(x_-,x_*)\) and \(c_+\in(x_*,x_+)\) with \(Q(c_-)=Q(c_+)=1\). Strict convexity forces \(Q(x_*)<1\), hence \(G'(x_*)>1\), or equivalently \(|F'(x_*)|>1\). Therefore \(|F'(x_*)|\le1\) excludes all primitive two-cycles, **including the neutral boundary**.

Conversely, suppose \(|F'(x_*)|>1\), so \(G'(x_*)>1\). Set \(H(x)=G(x)-x\). Then \(H(0)>0\), \(H(x_*)=0\), \(H'(x_*)>0\), and \(H(x)<0\) for all \(x>p_1\), because \(G(x)\le p_1\). Thus the intermediate value theorem supplies one zero on each side of \(x_*\), and the preceding bound makes these the only two other zeros. Since \(F\) has only one fixed point, it exchanges them. Moreover, the same convexity argument shows \(Q(x_-)>1\) and \(Q(x_+)>1\) (both lie outside the derivative-one points \(c_-<c_+\)), so the multiplier \(0<G'(x_\pm)<1\): the unique two-cycle is attracting.

**5. Global convergence.** The increasing continuous map \(G\) sends the half-line into a bounded positive interval. For any \(x_0\ge0\), the even subsequence \(G^n(x_0)\) is monotone after the first step, because \(G\) is increasing, and bounded, hence converges to a fixed point of \(G\). When only \(x_*\) exists, every orbit converges to \(x_*\). When the three fixed points exist, the signs of \(H\) and monotonicity force convergence to \(x_-\) for \(x_0<x_*\), to \(x_+\) for \(x_0>x_*\), and persistence at \(x_*\) if \(x_0=x_*\). Odd subsequences converge to the images under \(F\), completing the proof.

## Verification

The accompanying standalone Python 3 script `opacity_map_verify.py` performs 306 numerical diagnostics on the analytic derivative and fixed-point identities at 28 parameter pairs, and independently computes the two example thresholds and physical two-cycle versus fixed-point behavior. It returned `PASS 306 diagnostics`. These tests are supplementary; the additional `schwarzian_check.py` (which requires `mpmath`) verified the exact Schwarzian identity at five parameter/state configurations using 50-digit differentiation. The proof of the continuum and global claims is analytical and does not depend on sampling.

## Relationship to prior work

Bromley and Chiang introduced precisely this constant-opacity map and illustrated fixed-point and two-cycle regimes in numerical \(\gamma\)-sweeps. They describe local fixed-point slope criteria and observe that the model cannot be chaotic because it is monotone. The present theorem does not claim these observations as new. It identifies the **sharp critical response parameter**, proves the **two-sided, re-entrant \(p_1\) window**, establishes **uniqueness and global attraction** of the cycle, and resolves **neutral endpoints** for this particular map. The method uses the classical negative-Schwarzian composition/minimum-principle framework; these general identities and classical interval-map results are not claimed as new.

## Limitations

The threshold coordinates are given implicitly, not in elementary closed form. All \(p_1\) and \(p_2\) are admitted mathematically, although a physical model may restrict parameter ranges. The example thresholds are floating-point approximations without rigorous rounded-interval certificates. The theorem does not apply to Bromley and Chiang's variable-opacity Maps B and C and does not make predictions for full radiation hydrodynamics. Novelty is assessed against inspected accessible primary and related sources; equivalent or unindexed antecedents remain a possibility. No independent mathematical audit is claimed.

## References

1. J. Bromley and E. Chiang, *Chaotic winds from a dying world: a one-dimensional map for evolving atmospheres*, arXiv:2302.04898v1 (public 2023-02-09), Section 2.1 and Eq. (6); published in *Monthly Notices of the Royal Astronomical Society* **521** (2023), 5746–5759. https://arxiv.org/abs/2302.04898
2. B. San Martín and F. Correa, *On the Use of the Schwarzian Derivative in Real One-Dimensional Dynamics*, arXiv:2409.00959v2 (revision 2025-04-04; original first posted 2024-09-02), Sections 2–4 (standard Schwarzian composition and Singer framework). https://arxiv.org/abs/2409.00959
