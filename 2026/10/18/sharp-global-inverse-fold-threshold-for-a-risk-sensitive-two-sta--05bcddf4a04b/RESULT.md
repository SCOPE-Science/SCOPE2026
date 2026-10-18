# Sharp global inverse-fold threshold for a risk-sensitive two-state learning map

## Finding

For a two-dimensional risk-sensitive multiplicative-weights map with a linearly adapting belief, the entire inverse-image multiplicity is controlled by a single *effective folding parameter*. Strong enough belief adaptation makes the system injective for **arbitrarily large** learning intensity, while weaker adaptation produces a two-fold curve and a strip of three-to-one inverse images in the ambient extension.

For the map defined below let
\[
B=a\left(1-\frac{ckp_1}{1-k}\right).
\]
If \(B<4\), its real-plane extension in log-odds coordinates is a real-analytic diffeomorphism; at \(B=4\), it is a bijective homeomorphism whose inverse has sharp local Hölder exponent \(1/3\); and if \(B>4\), it has exactly three preimages in an explicit open strip, exactly two on the strip edges, and one elsewhere. On the physically admissible open square, injectivity holds **if and only if** \(B\le4\). These are pointwise/global invertibility statements, not stability or chaos theorems.

For \(a>4\), the critical adaptation rate is therefore
\[
k_{\mathrm{inj}}=\frac{a-4}{a-4+acp_1}.
\]
The physical map is one-to-one exactly for \(k\ge k_{\mathrm{inj}}\), and is a smooth embedding for \(k>k_{\mathrm{inj}}\). In particular, if \(k\ge (1+cp_1)^{-1}\) and \(k<1\), it is a smooth embedding for every \(a>0\). The strip width opens according to \(\frac13(B-4)^{3/2}+O((B-4)^{5/2})\) as \(B\downarrow4\).

## Assumptions and scope

Fix real parameters \(a>0\), \(c>0\), \(0<k<1\), \(0<b<1\), \(p_0\ge0\), \(p_1>0\), and \(p_0+p_1\le1\). Define \(F:(0,1)^2\to(0,1)^2\) by
\[
F(x,q)=(X,Q),\qquad
X=\frac{x}{x+(1-x)\exp(a(x-b+cq))},\quad
Q=(1-k)q+k(p_0+p_1x).
\]
Under the displayed assumptions \(0<X<1\) and \(0<Q<1\) whenever \(0<x,q<1\). The closed unit square is forward invariant, but injectivity is asserted here only on its interior. For **ambient inverse multiplicities**, let \(t=\log(x/(1-x))\), \(S(t)=(1+e^{-t})^{-1}\), and extend the same formula to all \((t,q)\in\mathbb R^2\) with target \((T,Q)\in\mathbb R^2\), where \(T=\log(X/(1-X))\). Unlike the physical map, this extension admits arbitrary real beliefs.

Introduce the affine target coordinate
\[
z=T-ab+\frac{ac}{1-k}(Q-kp_0),\qquad B=a\left(1-\frac{ckp_1}{1-k}\right),\quad h_B(t)=t-BS(t).
\]
For \(B>4\) write \(d=\sqrt{1-4/B}\in(0,1)\), \(u=\log((1+d)/(1-d))=2\operatorname{artanh}d\), and
\[
H_{\max}=-u-\frac B2(1-d),\qquad
H_{\min}=u-\frac B2(1+d).
\]
The stated three-to-one strip is exactly the set of \((T,Q)\in\mathbb R^2\) for which \(H_{\min}<z<H_{\max}\); it should **not** be interpreted as three physical inverse images at every point of that strip.

## Proof

**Exact inverse reduction.** The log-odds formula gives \(T=t-a(S(t)-b+cq)\). Solving the second coordinate yields
\[
q=\frac{Q-kp_0-kp_1S(t)}{1-k}.
\]
Substitution gives, with no approximation, \(h_B(t)=z\). Conversely each real root \(t\) of this equation determines one and only one real \(q\) by the displayed equation. Hence the full inverse multiplicity is the multiplicity of the scalar level equation.

**Global monotonicity and critical order.** Since
\[
h'_B(t)=1-BS(t)(1-S(t)),\qquad 0<S(t)(1-S(t))\le\tfrac14,
\]
we have \(h'_B>0\) everywhere if \(B<4\). Also \(h_B(t)-t\) is bounded, so \(h_B\) is onto \(\mathbb R\), and the analytic inverse-function theorem makes the ambient map an analytic diffeomorphism. At \(B=4\), \(h'_4\ge0\) with a single zero \(t=0\), implying strict monotonicity and a continuous global inverse. Direct expansion gives
\[
h_4(t)=-2+\frac{t^3}{12}-\frac{t^5}{120}+O(t^7).
\]
On every fixed \(Q\)-section, \(|t|\sim12^{1/3}|z+2|^{1/3}\); thus the inverse is locally \(1/3\)-Hölder there and not \(\alpha\)-Hölder for any \(\alpha>1/3\). The Jacobian vanishes on \(t=0\), so it is not a diffeomorphism.

**Fold geometry.** For \(B>4\), the two zeros of \(h'_B\) are exactly \(t=-u\) and \(t=u\), corresponding to \(S(t)=(1\mp d)/2\). They are nondegenerate: \(h''_B(t)=-B S(t)(1-S(t))(1-2S(t))\), nonzero at either critical point. The function is strictly increasing on \(( -\infty,-u)\), decreasing on \((-u,u)\), and increasing on \((u,\infty)\), with respective local maximum \(H_{\max}\) and minimum \(H_{\min}\). Its end limits are \(-\infty\) and \(+\infty\). Therefore the scalar level equation, and hence the ambient planar map, has respectively three, two, or one **distinct** real inverse images inside, on, or outside the two boundary lines.

The exact strip width is
\[
W(B)=H_{\max}-H_{\min}=Bd-4\operatorname{artanh}d.
\]
Because \(B=4/(1-d^2)\), differentiation with respect to \(d\) gives \(W'(d)=8d^2/(1-d^2)^2>0\) and \(W(0)=0\); therefore the strip is nonempty. Expanding \(d=\sqrt{(B-4)/B}\) and \(\operatorname{artanh}d\) yields
\[
W(B)=\tfrac13(B-4)^{3/2}+O((B-4)^{5/2}).
\]

**Jacobian and physical noninjectivity.** Differentiating in \((t,q)\) coordinates gives
\[
\det D(T,Q)=(1-k)\{1-BS(t)(1-S(t))\}.
\]
If \(B\le4\), scalar injectivity proves physical injectivity; for \(B<4\), smooth invertibility on the image follows from the inverse construction. If \(B>4\), choose either critical \(t_0\in\{-u,u\}\) and any interior belief \(q_0\in(0,1)\). Fix the target belief \(Q_0=(1-k)q_0+k(p_0+p_1S(t_0))\). The function \(q(t)=[Q_0-kp_0-kp_1S(t)]/(1-k)\) is continuous and equals \(q_0\) at \(t_0\); hence it remains in \((0,1)\) for \(t\) near \(t_0\). Levels sufficiently close to the strict local extremum \(h_B(t_0)\) have two distinct roots arbitrarily near \(t_0\), both giving admissible beliefs and the identical target \((T,Q_0)\). Thus the physical map is not injective, not merely singular.

**Sharp adaptation threshold.** The inequality \(B\le4\) is automatic when \(a\le4\). When \(a>4\), elementary rearrangement, using \(1-k>0\), shows it is equivalent to \(k\ge (a-4)/(a-4+acp_1)\). Strict inequality is equivalent to \(B<4\); equality gives the cubic critical line. If \(k\ge (1+cp_1)^{-1}\), then \(ckp_1/(1-k)\ge1\), hence \(B\le0<4\) for every \(a>0\). This concludes the classification.

## Verification

The standalone `check_inverse_geometry.py` reproduces the symbolic Jacobian identity, the order-three Taylor coefficient, 400 seeded inverse-reduction/recovery checks, admissible physical double preimages, seven explicit ambient three-preimage samples, three small-width scaling checks, and 25 sampled Jacobian positivity checks in the highly adaptive parameter regime. It reports 436 finite diagnostics and two exact symbolic identities. The analytical proof above, not the finite diagnostics, establishes all quantifiers and limiting assertions. Run it using Python 3 with `sympy` and `scipy` installed.

For the illustrative parameters \(c=500\), \(p_1=0.001\), and \(k=0.865\) used in the motivating numerical study, \(ckp_1/(1-k)>1\). Thus the physical map is a smooth embedding for every \(a>0\) at those fixed parameters. This fact does not independently establish any chaotic invariant set; reported chaotic behavior in the motivating paper is numerical/observational.

## Relationship to prior work

Metaxas and Sapsis (arXiv:2606.29967v1, Sections 2–3 and Appendix A.1) define and study the same coupled state/belief dynamics, focusing on equilibria, multistability and numerical bifurcations. The precise global inverse multiplicity and sharp dependence on belief-adaptation rate are not among the claims inspected there. Chotibut, Falniowski, Misiurewicz and Piliouras (arXiv:1807.06831v1, Sections 2–3) study the separate one-dimensional autonomous MWU map and its logistic derivative threshold; the unadapted one-dimensional fold mechanism is therefore known. It does not alone classify the coupled two-dimensional map: the explicit elimination, effective parameter, physical versus ambient distinctions, and arbitrary-intensity adaptation threshold are the subject of this result. Palaiopanos, Panageas and Piliouras (arXiv:1703.01138v1, Sections 1–2) discuss nonconvergent constant-step MWU game dynamics, rather than this inverse problem. An equivalent treatment in broader two-dimensional economic learning or skew-product literature remains possible.

## Limitations

The theorem assumes affine belief updating, strictly interior physical states, and \(0<k<1\). It does not classify dynamics on the boundary, singularity types for modified nonlinear belief laws, stability of fixed points, invariant measures, or existence of chaotic attractors. The ambient count of three generally does not equal the number of admissible physical inverse images. At \(B=4\), smooth invertibility fails even though set-theoretic injectivity remains. The verified first-public date belongs to the motivating preprint, not to this derivation. This work has undergone self-review only; no independent mathematical audit is claimed.

## References

1. K. Metaxas and T. P. Sapsis, *Risk-Sensitive Learning in Population Games under Extreme Events: Bifurcations and Chaotic Dynamics*, arXiv:2606.29967v1 (posted 2026-06-29), https://arxiv.org/abs/2606.29967 . Sections 2.2–2.3, 3 and Appendix A.1.
2. T. Chotibut, F. Falniowski, M. Misiurewicz and G. Piliouras, *Family of chaotic maps from game theory*, arXiv:1807.06831v1 (2018), https://arxiv.org/abs/1807.06831 . The one-dimensional map and derivative calculations in Sections 2–3.
3. G. Palaiopanos, I. Panageas and G. Piliouras, *Multiplicative Weights Update with Constant Step-Size in Congestion Games: Convergence, Limit Cycles and Chaos*, arXiv:1703.01138v1 (2017), https://arxiv.org/abs/1703.01138 .
