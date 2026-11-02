# Exact edge-Lipschitz contraction threshold for nonlinear heat flow on clique bouquets

## Finding

For a bouquet of cliques sharing one hub, the individual-solution edge-Lipschitz contraction property of the discrete \(p\)-heat flow has a sharp, explicitly evaluated phase diagram. The logarithmic edge-gradient dissipation coefficient can be computed exactly, including cases with nonlinear expansion.

Write \(G=K_1\vee (K_{r_1}\sqcup\cdots\sqcup K_{r_m})\), where \(m\ge1\) and all blade sizes \(r_i\ge1\) are integers. Let \(N=\sum_i r_i\). For \(1<p<\infty\), put
\[
c_p=\begin{cases}1,&1<p\le2,\\2^{2-p},&p\ge2,\end{cases}
\qquad
\mu_p(G)=\max_{1\le i\le m}\bigl\{N-r_i-2-(r_i-1)c_p\bigr\}.
\]
For the unit-mass, unit-conductance graph \(p\)-heat flow \(S_t\) and the edge-Lipschitz seminorm \(L_G(u)=\max_{vw\in E(G)}|u_v-u_w|\),
\[
\sup_{L_G(u)=1}\left.\frac{d^+}{dt}L_G(S_tu)\right|_{t=0}=\mu_p(G),
\qquad
\boxed{\ L_G(S_tu)\le L_G(u)\ \text{for all }u,t\ge0\ \Longleftrightarrow\ \mu_p(G)\le0.\ }
\]
Here the derivative is the right derivative of a maximum of finitely many differentiable edge gaps. The finite supremum in the first display is attained by an explicit configuration.

The phase diagram has a concise form. For \(m=1\), contraction always holds. For \(m\ge4\), it always fails. For \(m=3\), it holds exactly when \(r_1=r_2=r_3=1\). For \(m=2\) with \(a=\min(r_1,r_2)\le b=\max(r_1,r_2)\), it holds precisely when
\[
 b\le 2+(a-1)c_p.
\]
In particular, when \(r_1=r_2=r\ge3\), contraction holds precisely for
\[
 1<p\le2+\log_2\frac{r-1}{r-2}.
\]
Thus the two-blade size-three bouquet contracts edge gradients through exponent \(p=3\) and expands them for every \(p>3\), despite having the same graph at all exponents.

Whenever \(\mu_p(G)>0\) and \(p\ne2\), normalized instantaneous edge-gradient growth is unbounded:
\[
\sup_{L_G(u)>0}\lim_{t\downarrow0}
\frac{L_G(S_tu)/L_G(u)-1}{t}=+\infty.
\]
This last assertion concerns instantaneous rates; it does not assert unbounded amplification at a fixed positive time.

## Assumptions and scope

Every clique has its unit graph edge lengths, every vertex has unit mass, and every edge has unit conductance. The graph has one hub, the vertices in blade \(i\) form a clique with that hub, and there are no edges between different blades. Signals are real-valued. For \(1<p<\infty\), define the continuous odd flux \(\phi_p(s)=|s|^{p-2}s\) for \(s\ne0\) and \(\phi_p(0)=0\). The evolution at every vertex is
\[
\frac{du_v}{dt}=\sum_{w\sim v}\phi_p(u_w-u_v).
\]
All quantifiers are over arbitrary initial vertex signals and all continuous times \(t\ge0\). The graph-edge seminorm uses the actual edges, not all pairs at graph distance more than one.

The vector field is continuous, including for \(1<p<2\), and generates a unique global differentiable solution. Indeed, a maximum principle bounds each trajectory within its initial minimum and maximum, giving global existence; and the monotonicity of \(\phi_p\) yields the dissipative inequality
\[
\langle F(u)-F(v),u-v\rangle
=-\sum_{\{x,y\}\in E(G)}
[\phi_p(u_y-u_x)-\phi_p(v_y-v_x)]
[(u_y-u_x)-(v_y-v_x)]\le0,
\]
which implies uniqueness. This justifies all one-sided time derivatives below even when \(\phi_p\) is not differentiable at zero.

## Proof

**1. Exact edge derivative bound.** For a nonconstant signal, set \(\ell=L_G(u)>0\), and orient any active edge \((v,w)\) so that \(u_v-u_w=\ell\). Its signed instantaneous gap derivative is \(F(u)_v-F(u)_w\). By translation invariance and the \((p-1)\)-homogeneity of \(F\), one may analyze \(\ell=1\), \(u_v=1\), \(u_w=0\).

An elementary scalar minimization gives
\[
\min_{0\le s\le1}\bigl\{s^{p-1}+(1-s)^{p-1}\bigr\}
=c_p.
\]
For \(1<p<2\), the minimum is at the endpoints; for \(p>2\), it occurs at \(s=1/2\); and for \(p=2\), the expression is identically one.

If both endpoints lie in the same blade \(i\), all their other \(r_i-1\) common neighbors (including the hub) have values in \([0,1]\). The direct edge gives \(-2\), and each common neighbor contributes at most \(-c_p\). Hence
\[
F(u)_v-F(u)_w\le -2-(r_i-1)c_p\le\mu_p(G).
\]

If the active edge joins the hub \(h\) to a blade-\(i\) vertex \(a\), orient it so that \(u_h=1\), \(u_a=0\). Every remaining vertex \(b\) of blade \(i\) has \(u_b\in[0,1]\), while every vertex \(z\) outside that blade has \(u_z\in[0,2]\). The exact derivative identity is
\[
F(u)_h-F(u)_a=-2
-\sum_{b\in B_i\setminus\{a\}}
\bigl[(1-u_b)^{p-1}+u_b^{p-1}\bigr]
+\sum_{z\notin B_i}\phi_p(u_z-1).
\]
The final sum has \(N-r_i\) terms, each at most \(1\). Therefore
\[
F(u)_h-F(u)_a\le N-r_i-2-(r_i-1)c_p\le\mu_p(G).
\]
By replacing the signal with its negative when necessary, these two edge types cover every orientation. The maximum-of-finitely-many-smooth-in-time-functions formula yields
\[
D^+L_G(u)\le \mu_p(G)L_G(u)^{p-1}
\qquad\text{whenever }L_G(u)>0.
\]

**2. Attainment and sharpness.** Choose a blade \(i\) attaining the maximum in \(\mu_p(G)\). Set the hub value to \(1\), choose one vertex \(a\) in blade \(i\) with value \(0\), set each other vertex of blade \(i\) to \(0\) when \(1<p\le2\) and \(1/2\) when \(p>2\), and set every vertex in every other blade to \(2\). Every edge gap is at most one, the active hub–\(a\) gap is one, and the derivative computed above is exactly \(\mu_p(G)\). Thus the upper bound for the right derivative is sharp and the stated supremum is a maximum.

If \(\mu_p(G)\le0\), the differential inequality for the locally Lipschitz function \(t\mapsto L_G(S_tu)\) implies that it is nonincreasing. Conversely, if \(\mu_p(G)>0\), the explicit maximizing configuration has a strictly increasing active gap for all sufficiently small positive times. This proves the if-and-only-if claim.

Scaling this witness by a positive factor \(R\) changes the initial gap from \(1\) to \(R\), and its derivative from \(\mu_p(G)\) to \(\mu_p(G)R^{p-1}\). Consequently, its normalized initial growth rate is \(\mu_p(G)R^{p-2}\), which diverges by choosing \(R\to\infty\) for \(p>2\) or \(R\downarrow0\) for \(1<p<2\). This proves the unbounded-rate assertion, but not fixed-time unbounded amplification.

**3. Explicit phase diagram.** Set \(r_* =\min_i r_i\). Because the expression \(N-r_i-2-(r_i-1)c_p\) is strictly decreasing in \(r_i\), the maximum is
\[
\mu_p(G)=N-r_*-2-(r_*-1)c_p.
\]
For one blade, this is strictly negative. For four or more blades, \(N\ge4r_*\) makes the coefficient strictly positive. For three blades, \(N\ge3r_*\) gives \(\mu_p(G)\ge (2-c_p)r_*-2+c_p\), which is zero only when all blades have size one; any larger blade configuration makes the coefficient positive. For two blades, \(N=a+b\) gives \(\mu_p(G)=b-2-(a-1)c_p\), as claimed. For equal blades of size \(r\ge3\), the inequality becomes \(2^{2-p}\ge(r-2)/(r-1)\) whenever \(p\ge2\), yielding the stated sharp transition.

## Verification

The standalone standard-library program `verify_bouquet_pheat_lipschitz.py` reconstructs every graph edge and flux rather than using the closed-form derivative. Running `python verify_bouquet_pheat_lipschitz.py` reports `EXACT_WITNESS_SHARPNESS_OK 108`, `EXACT_GRID_DINI_UPPER_BOUND_OK 2536`, `NONLINEAR_PHASE_DIAGRAM_OK 384 strict_failure_cases= 378`, and `BALANCED_TWO_BLADE_THRESHOLD_OK p*=3`, ending in `ALL_CLIQUE_BOUQUET_PHEAT_CHECKS_OK`. These finite exact-arithmetic and diagnostic checks support the algebra; all graph sizes and real exponents are covered by the analytical proof, not finite enumeration.

## Relationship to prior work

Mugnolo's *Parabolic theory of the discrete \(p\)-Laplace operator* (2012, subsequent revisions) establishes well-posedness, order preservation and contractivity in vertex-function norms. In particular, its Proposition 3.9 concerns the \(\ell^\infty\) norm on **functions**, not the maximum of differences across edges of one nonlinear trajectory. The present result studies this separate seminorm and gives an exact coefficient depending on blade multiplicities and the exponent. Hua and Mugnolo (2014) investigate time regularity and long-time behavior of graph \(p\)-heat, rather than this phase diagram. The linear heat-gradient-curvature framework of Münch and Wojciechowski (2017) has exponent two and does not evaluate the nonlinear phase transition.

These comparisons are based on the identified material in the accessible source texts. An equivalent derivation under another terminology or outside the inspected literature remains possible; literature search absence alone is not proof of priority.

## Limitations

The coefficient and classification assume finite simple clique bouquets, uniform unit masses and conductances, real vertex signals, and \(1<p<\infty\). Arbitrary weighted bouquets, other graph classes, metric interpolation beyond graph edges, and infinite graphs are not classified. The unbounded instability concerns normalized **instantaneous** rates only. It makes no assertion of unbounded amplification at fixed positive time or of two-input nonexpansivity.

## References

1. D. Mugnolo, *Parabolic theory of the discrete p-Laplace operator*, arXiv:1207.1996v1 (first posted 2012-07-09), full revised text at https://arxiv.org/html/1207.1996v3, especially Sections 3–4 and Proposition 3.9.
2. B. Hua and D. Mugnolo, *Time regularity and long-time behavior of parabolic p-Laplace equations on infinite graphs*, arXiv:1410.1584v1 (2014-10-06), https://arxiv.org/html/1410.1584v1, especially Sections 1 and 3.
3. F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875 (2017), https://arxiv.org/abs/1712.00875, comparison limited to the stated linear-heat scope.
