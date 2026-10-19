# Exact trust–disagreement separatrix and critical slowing in two-agent adaptive opinion dynamics

## Finding

For the two-agent, self-weight-normalized opinion dynamics with symmetric logistic edge adaptation introduced by Nugent, Gomes, and Wolfram [1], an exact first integral separates complete consensus from permanent opinion disagreement. This separation holds for every strictly decreasing, positive \(C^2\) interaction kernel crossing \(1/2\) transversely. It also identifies a nontrivial critical orbit on which the opinion gap tends to a positive value while the edge weight vanishes algebraically, with universal exponents \(1\) and \(2\).

Let \(\phi:[0,2]\to(0,1]\) be \(C^2\), strictly decreasing, and satisfy \(\phi(0)>1/2>\phi(2)\). Let \(r\in(0,2)\) be the unique root \(\phi(r)=1/2\), and assume \(\phi'(r)<0\). Define the exact separation potential

\[
F(d)=\int_r^d\frac{1-2\phi(s)}{2s\phi(s)}\,ds,\qquad 0<d\le 2.
\]

For initial opinion gap \(d_0\in(0,2]\) and initial mutual trust \(w_0\in(0,1)\), the following alternatives are exhaustive:

1. If \(d_0\le r\), the agents converge to consensus and their tie converges to unit weight.
2. If \(d_0>r\), let \(w_*(d_0)=\tanh(F(d_0))\). For \(w_0>w_*(d_0)\), they converge to consensus with tie weight tending to one.
3. If \(d_0>r\) and \(w_0<w_*(d_0)\), the tie decays to zero and disagreement tends to the unique \(d_\infty\in(r,d_0)\) satisfying
   \[
   F(d_\infty)=F(d_0)-\operatorname{artanh}(w_0).
   \]
4. If \(d_0>r\) and \(w_0=w_*(d_0)\), then \(d(t)\downarrow r\), \(w(t)\downarrow0\), and
   \[
   \lim_{t\to\infty}t(d(t)-r)=\frac{1}{-\phi'(r)},\qquad
   \lim_{t\to\infty}t^2w(t)=\frac{1}{-r\phi'(r)}.
   \]

The agents' arithmetic mean opinion is constant in all four cases. At consensus, \(\lim_{t\to\infty}t^{-1}\log d(t)=-\phi(0)\). In the permanent-disagreement regime, \(\lim_{t\to\infty}t^{-1}\log w(t)=2\phi(d_\infty)-1<0\).

## Assumptions and scope

There are exactly two agents with opinions \(x_1,x_2\in[-1,1]\), reciprocal off-diagonal edge weights \(w_{12}=w_{21}=w\), permanent self-weights \(w_{11}=w_{22}=1\), and normalized degrees \(k_1=k_2=1+w\). The system is exactly [1, equations (8), (11), (12)] with no additional rate multiplier:

\[
\dot x_1=\frac{w}{1+w}\phi(|x_1-x_2|)(x_2-x_1),\quad
\dot x_2=\frac{w}{1+w}\phi(|x_1-x_2|)(x_1-x_2),
\]
\[
\dot w=w(1-w)\bigl(2\phi(|x_1-x_2|)-1\bigr).
\]

The initial values satisfy \(x_i(0)\in[-1,1]\), \(d_0=|x_1(0)-x_2(0)|>0\), and \(0<w_0<1\). Endpoints \(w_0=0\) and \(w_0=1\) are fixed-weight boundary cases outside the asserted trichotomy, not counterexamples. Equal initial opinions give trivial consensus, with the weight increasing to one under \(\phi(0)>1/2\). The bounded opinion interval is forward invariant since each opinion moves toward the other.

## Proof

**Reduction and invariant.** Since \(x_1+x_2\) is conserved and the signed difference cannot change sign, write \(d=|x_1-x_2|\). The equations reduce to

\[
\dot d=-\frac{2w}{1+w}\phi(d)d,\qquad
\dot w=w(1-w)(2\phi(d)-1).
\]

The vector field is locally Lipschitz on the compact physical state space; its boundary is invariant. From \(0<w_0<1\) and \(d_0>0\), neither \(w=0\), \(w=1\), nor \(d=0\) can be reached at finite time. Because

\[
\frac{d}{dt}\operatorname{artanh}(w)=\frac{w}{1+w}(2\phi(d)-1)
\]

and

\[
\frac{d}{dt}F(d)=\frac{1-2\phi(d)}{2d\phi(d)}\dot d=\frac{w}{1+w}(2\phi(d)-1),
\]

we obtain the conserved quantity

\[
\boxed{\operatorname{artanh}(w(t))-F(d(t))=\operatorname{artanh}(w_0)-F(d_0).}
\]

**Potential geometry and the sharp boundary.** The strict monotonicity of \(\phi\) implies \(F'<0\) on \((0,r)\), \(F'(r)=0\), and \(F'>0\) on \((r,2]\). Hence \(F(r)=0\) is its strict global minimum and \(F(d)>0\) away from \(r\). Moreover, since \(\phi(0)>1/2\), the integrand is asymptotic to a negative constant divided by \(d\) near zero; therefore \(F(d)\to+\infty\) as \(d\downarrow0\).

The gap is strictly decreasing while \(d,w>0\), so it has a nonnegative limit. Because \(d\) decreases and \(\phi\) decreases, \(2\phi(d(t))-1\) is nondecreasing in time. Thus the sign of \(\dot w\) switches at most once (from negative to positive), and \(w\) also has a limit. If \(d_\infty>0\) and \(w\) has a positive limit, then \(\dot d\) is eventually bounded away from zero in the negative direction, a contradiction. Therefore every nonconsensus orbit must have \(w_\infty=0\). Conversely, if \(d\to0\), then for all large times \(2\phi(d)-1\) is uniformly positive; logistic comparison forces \(w\to1\).

When \(d_0\le r\), \(d(t)<r\) for every positive time, so \(\dot w>0\), whence \(w\) cannot decay to zero and the orbit reaches consensus.

Suppose \(d_0>r\), and abbreviate \(C=\operatorname{artanh}(w_0)-F(d_0)\). If \(C<0\), the invariant \(\operatorname{artanh}(w)=F(d)+C\ge0\) forbids \(d\) from reaching \(r\). The only possible limit is \(d_\infty\in(r,d_0)\) with \(w_\infty=0\), determined uniquely by \(F(d_\infty)=-C\). If \(C>0\), the invariant precludes a limiting \(w=0\) with \(d_\infty\ge r\) because \(F(d)\ge0\) there; the trajectory must pass below \(r\), where the preceding monotonic argument yields consensus. If \(C=0\), the trajectory cannot reach \(r\) in finite time (that would require \(w=0\)); it also cannot end above \(r\) (that would imply \(w_\infty=\tanh(F(d_\infty))>0\)). Thus \(d\downarrow r\) and \(w\downarrow0\). The sign of \(C\) is exactly the sign of \(w_0-\tanh(F(d_0))\).

**Critical asymptotics.** On the critical curve \(C=0\), put \(z=d-r>0\). Taylor expansion using \(\phi(r)=1/2\) and \(\phi'(r)<0\) gives

\[
F(r+z)=\frac{-\phi'(r)}{r}z^2+O(z^3),\qquad
w=\tanh(F(r+z))=\frac{-\phi'(r)}{r}z^2+O(z^3).
\]

Substitution in the gap equation shows

\[
\dot z=\phi'(r)z^2+O(z^3).
\]

Hence \(\frac{d}{dt}(1/z)=-\dot z/z^2\to-\phi'(r)>0\). Cesàro averaging implies \(1/(t z)\to-\phi'(r)\), yielding \(t z\to1/(-\phi'(r))\). Combining this with the quadratic weight expansion proves \(t^2w\to1/(-r\phi'(r))\).

**Off-critical exponential rates.** In the consensus basin, \(w\to1\), \(d\to0\), and the first ODE gives \(d(\log d)/dt\to-\phi(0)\); averaging yields the displayed logarithmic rate. In the polarization basin \(d\to d_\infty>r\) and \(w\to0\); the logistic equation gives \(d(\log w)/dt\to2\phi(d_\infty)-1<0\), proving its rate.

## Verification

For the rational example \(\phi(d)=1/(1+d)\), the threshold crossing is \(r=1\) and integration is elementary:

\[
F(d)=\frac{d-1-\log d}{2}.
\]

With \(d_0=2\), the exact critical initial trust is

\[
\boxed{w_*=\tanh\left(\frac{1-\log2}{2}\right)\approx0.15223377.}
\]

On this critical trajectory, \(t(d(t)-1)\to4\) and \(t^2w(t)\to4\). A standalone standard-library verification script, `verify.py`, recomputes the invariant, numerically integrates all three basins, checks the unique polarization limit and checks convergence toward the two critical coefficients. These finite computations corroborate but are not substitutes for the preceding infinite-time proof.

For the motivating exponential interaction \(\phi(d)=e^{-\alpha d}\), assume \(\alpha>\log(2)/2\), so \(r=\log(2)/\alpha\in(0,2)\). The potential is

\[
F(d)=\frac12\left(\operatorname{Ei}(\alpha d)-\operatorname{Ei}(\log2)-2\log\frac d r\right),
\]

where \(\operatorname{Ei}\) denotes the classical real exponential integral. Critical trajectories obey \(t(d-r)\to2/\alpha\) and \(t^2w\to2/\log2\).

## Relationship to prior work

Nugent, Gomes, and Wolfram [1], Sections 3.2 and 3.4, introduce the same logistic weight dynamics and observe through simulations that a strictly positive exponential interaction kernel can coexist with clustering caused by disappearing ties. Their Equation (12) identifies when a tie initially increases or decreases, but that instantaneous sign condition does not determine a future consensus basin. Their Proposition 3.4 concerns **memory** weight dynamics rather than the present logistic process. This result gives an exact global basin partition and sharp transition rates in the minimal reciprocal pair.

The later work of Nugent, Calatayud Fernandez, and Gomes [2] proves convergence to clusters and identifies limiting edge-weight alternatives under full-support interactions, including logistic weights (Theorem 3.1 and Corollaries 3.2–3.4). Those qualitative conclusions are compatible with this theorem, but do not imply its initial-data separatrix, limiting separation formula, or critical algebraic rates. Their Section 5 develops short-time network-weight approximations, rather than the present exact global invariant. Nugent, Gomes, and Wolfram [3] investigate network control with another weight-control mechanism. Sugishita et al. [4] study tie-decay networks driven by temporal contacts, with a structurally different edge law.

## Limitations

The classification requires exactly two reciprocally connected agents, symmetric tie weight, fixed unit self-weights, identical opinion responsiveness, and smooth monotone positive interactions crossing \(1/2\). It is not a global threshold theorem for larger heterogeneous networks, time-varying kernels, discontinuous bounded-confidence rules, arbitrary tie feedback, or weighted-degree normalizations that omit self-weights. Strict transverse crossing is required for the stated powers; a flat crossing may produce other critical exponents. No novelty claim is made about the general method of first integrals for planar ODEs; the claim concerns this model-specific integral, sharp basin criterion and critical behavior. Specialist literature might contain an equivalent formulation not found in the sources inspected. Independent validation has not been performed.

## References

[1] A. J. Nugent, S. N. Gomes, and M.-T. Wolfram, *On evolving network models and their influence on opinion formation*, arXiv:2305.09483v1 (public 2023-05-16); *Physica D* 456 (2023), 133914. https://arxiv.org/abs/2305.09483

[2] A. Nugent, C. Calatayud Fernandez, and S. N. Gomes, *Emergent structures in coupled opinion and network dynamics*, arXiv:2602.03738v1 (2026). https://arxiv.org/abs/2602.03738

[3] A. Nugent, S. N. Gomes, and M.-T. Wolfram, *Steering opinion dynamics through control of social networks*, arXiv:2404.09849v1 (2024). https://arxiv.org/abs/2404.09849

[4] K. Sugishita, M. A. Porter, M. Beguerisse-Díaz, and N. Masuda, *Opinion dynamics on tie-decay networks*, *Physical Review Research* 3 (2021), 023249. https://doi.org/10.1103/PhysRevResearch.3.023249
