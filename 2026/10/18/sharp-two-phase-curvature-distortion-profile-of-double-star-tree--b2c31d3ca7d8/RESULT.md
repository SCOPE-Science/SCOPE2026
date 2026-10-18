# Sharp two-phase curvature-distortion profile of double-star trees

## Finding

For positive integers \(1\le a\le b\), let \(D_{a,b}\) be the tree with adjacent centers \(u,v\), \(a\) leaves attached to \(u\), and \(b\) leaves attached to \(v\). Put \(m=a+b+1\). Edge weights are positive, give normalized random-walk transition probabilities, and do **not** change the underlying unweighted graph distance in the Lin--Lu--Yau curvature definition. The curvature-distortion number \(\mathrm{DN}^{k}_{\mathrm{LLY}}(D_{a,b})\) is the minimum maximum-to-minimum edge-weight ratio among weightings with curvature at least \(k\) on every edge, with value \(+\infty\) if none exists.

Define the exact threshold
\[
k_*(a,b)=\frac{4}{2b+1+\sqrt{1+4a(b+1)}}.
\]
For every \(0\le k\le 2/m\), the distortion is
\[
\boxed{\mathrm{DN}^{k}_{\mathrm{LLY}}(D_{a,b})=T_{a,b}(k):=
\begin{cases}
\dfrac{k(a+b)+\sqrt{k^2(a-b)^2+16ab}}{2(2-k)},&0\le k\le k_*,\\[7pt]
\dfrac{ak(b+1)}{2-k(b+1)},&k_*\le k\le 2/m.
\end{cases}}
\]
For \(k>2/m\), no feasible weighting exists. The two displayed formulas agree at \(k=k_*\). The **unique normalized optimal weighting** assigns weight \(1\) to every leaf edge at \(u\), weight
\[
B_{a,b}(k)=\max\!\left\{1,\frac{kT_{a,b}(k)}{2-kb}\right\}
\]
to every leaf edge at \(v\), and weight \(T_{a,b}(k)\) to the central edge. All denominators are strictly positive on the stated domain.

If \(a<b\), then \(0<k_*<2/m\): the heavier leaf class activates at a **unique interior threshold**, where the optimal distortion is continuous but not differentiable; its right derivative is strictly larger than its left derivative. If \(a=b\), then \(k_*=2/m\) and there is no interior transition. At the two endpoints,
\[
T_{a,b}(0)=\sqrt{ab},\qquad T_{a,b}(2/m)=b+1,\qquad B_{a,b}(2/m)=\frac{b+1}{a+1}.
\]

## Assumptions and scope

Graphs are finite simple undirected trees. For an edge \(xy\) with positive weight \(w_{xy}\), the transition probability from \(x\) to \(y\) is \(p_x(y)=w_{xy}/\sum_{z\sim x}w_{xz}\). For idleness \(\alpha\in[0,1]\), define \(\mu_x^\alpha=\alpha\delta_x+(1-\alpha)\sum_{y\sim x}p_x(y)\delta_y\), and \(\kappa^w_{\mathrm{LLY}}(xy)=\lim_{\alpha\uparrow1}(1-W_1(\mu_x^\alpha,\mu_y^\alpha))/(1-\alpha)\), where \(W_1\) uses **combinatorial** distances. The distortion is \(\max_e w_e/\min_e w_e\). Only nonnegative target bounds \(k\ge0\) are asserted. The leaf counts \(a,b\) are integers and are ordered only to name the smaller and larger class; reversing the two centers does not change the result.

## Proof

**1. Edge curvature on a weighted tree.** For a tree, transportation cost between two probability distributions is the sum, over its edges, of the absolute mass imbalance across either component of the edge deletion. This follows by routing the signed mass surplus through the unique paths: the absolute net flow on every edge is forced, and these flows can be realized with no opposing cancellation. Apply this identity to \(\mu_x^{1-\varepsilon}\) and \(\mu_y^{1-\varepsilon}\) for adjacent vertices \(x,y\). For sufficiently small positive \(\varepsilon\), the cut at \(xy\) contributes \(1-\varepsilon(p_x(y)+p_y(x))\); all other relevant incident cuts contribute \(\varepsilon(1-p_x(y))\) and \(\varepsilon(1-p_y(x))\). Therefore
\[
\kappa^w_{\mathrm{LLY}}(xy)=2\bigl(p_x(y)+p_y(x)\bigr)-2.
\tag{1}
\]
This calculation also supplies a direct normalization check: for every weighted tree on \(m\) edges, summing (1) over edges yields \(2(m+1)-2m=2\), since each vertex's outgoing transition probabilities sum to one. Hence \(k>2/m\) is impossible.

**2. A scalar lower bound valid for arbitrary (not necessarily symmetric) weights.** Normalize any feasible weighting by \(\min_e w_e=1\), and write \(t\) for the central-edge weight, \(X\) for the total weight of the \(a\) leaf edges at \(u\), and \(Y\) for that of the \(b\) leaf edges at \(v\). In particular \(t\ge1\), \(X\ge a\), \(Y\ge b\). Formula (1) gives the bridge constraint
\[
\frac{2t}{t+X}+\frac{2t}{t+Y}-2\ge k.
\tag{2}
\]
For a leaf edge of weight \(z\) at \(v\), (1) gives \(\kappa=2z/(t+Y)\). Summing the \(b\) required leaf inequalities proves \(2Y\ge bk(t+Y)\), so
\[
Y\ge b\max\!\left\{1,\frac{kt}{2-kb}\right\}.
\tag{3}
\]
The denominator is positive for \(k\le2/m\). Define
\[
\Phi_{a,b,k}(t)=\frac{2t}{t+a}+
\frac{2t}{t+b\max\{1,kt/(2-kb)\}}-2.
\tag{4}
\]
Equations (2)--(3) imply \(\Phi_{a,b,k}(t)\ge k\). For each fixed \(k\), the function \(\Phi\) is continuous and strictly increasing for positive \(t\): below the point where the maximum in (4) switches, both fractions are strictly increasing; above it the second fraction is the constant \(2-kb\), while the first still increases strictly. Thus the equation \(\Phi_{a,b,k}(t)=k\) has at most one positive solution, and every feasible central weight is at least that solution.

**3. Solving the two scalar branches.** When \(kt\le2-kb\), (4) becomes \(2t/(t+a)+2t/(t+b)-2=k\), equivalently
\[
(2-k)t^2-k(a+b)t-(2+k)ab=0.
\]
Its unique positive root is the first branch \(T_{a,b}(k)\) displayed above. This root is strictly increasing in \(k\), and the condition \(k(T_{a,b}(k)+b)\le2\) eventually becomes equality at precisely
\[
k_*=\frac{4}{2b+1+\sqrt{1+4a(b+1)}}.
\tag{5}
\]
To verify (5), impose \(t=2/k-b\) in the quadratic equation to obtain \(4-2(2b+1)k+(b-a)(b+1)k^2=0\); rationalizing its smaller root gives (5), valid also when \(a=b\) by continuity. Moreover \(k_*\le2/m\), with strict inequality exactly when \(a<b\), because \(\sqrt{1+4a(b+1)}\ge 2a+1\), with equality exactly for \(a=b\).

When \(kt\ge2-kb\), the second term of (4) is \(2-kb\). The scalar equality is therefore \(2t/(t+a)=k(b+1)\), with positive solution
\[
t=\frac{ak(b+1)}{2-k(b+1)}.
\tag{6}
\]
The two solutions meet at \(k_*\). Both are increasing in \(k\), and (6) reaches \(b+1\) at \(k=2/m\). Thus the unique positive solution of \(\Phi(t)=k\) is the announced \(T_{a,b}(k)\), and \(T_{a,b}(k)\le b+1\) throughout the feasible interval. As distortion is at least its normalized central weight, every admissible weighting has distortion at least \(T_{a,b}(k)\).

**4. Attaining the bound.** Give the central edge weight \(T=T_{a,b}(k)\), every leaf at \(u\) weight \(1\), and every leaf at \(v\) weight \(B=\max\{1,kT/(2-kb)\}\). The bridge has curvature exactly \(k\) by (4). Every leaf at \(u\) has curvature \(2/(a+T)\ge2/m\ge k\), because \(T\le b+1\). Every leaf at \(v\) has curvature \(2B/(bB+T)\ge k\) by the definition of \(B\). Finally \(1\le B\le T\): for the nontrivial branch, \(B/T=k/(2-kb)\le1\), since \(k(b+1)\le2\); also \(T\ge\sqrt{ab}\ge1\). Thus the weighting is normalized, its distortion is \(T\), and the lower bound is attained.

**5. Uniqueness and the phase transition.** Suppose any normalized optimal weighting has distortion \(T\). Since its central weight \(t\) satisfies \(T\ge t\ge T\), it has \(t=T\). Strict monotonicity of both fractions in (2), together with equality \(\Phi(T)=k\), forces \(X=a\) and \(Y=b\max\{1,kT/(2-kb)\}\). Every \(u\)-leaf therefore has weight \(1\). Before and at \(k_*\), every \(v\)-leaf has weight \(1\); above \(k_*\), equality in the sum of the \(v\)-leaf curvature inequalities forces every such leaf to have the common weight \(kT/(2-kb)\). Hence the normalized optimum is unique.

For \(a<b\), the threshold lies in the interior. At the common value \(t_*=T(k_*)\), differentiating the first and second defining equations yields, respectively,
\[
T'_-(k_*)=\left(\frac{2a}{(t_*+a)^2}+\frac{2b}{(t_*+b)^2}\right)^{-1},\qquad
T'_+(k_*)=\frac{(b+1)(t_*+a)^2}{2a}.
\]
The second is strictly larger than the first. When \(a=b\), (5) is the endpoint, and no interior differentiability claim is made. This completes the proof.

## Verification

The accompanying `verify_double_star.py` evaluates the closed formula and independently solves the scalar necessary-condition equation by bisection, checks every class's true curvature inequality, and compares with numerical constrained minimization on orbit-constant weights. It also checks the endpoint curvatures in exact rational arithmetic and compares 180 edge curvatures against independently solved finite-dimensional Wasserstein transportation linear programs on small trees. A direct proof, not the experiments, establishes the result for unbounded \(a,b\) and every real \(k\) in the interval.

Run in an environment with Python 3, SciPy and NumPy: `python verify_double_star.py`. The accompanying `verification_output.txt` records the actual run. The computation cannot independently prove uniqueness or absence of a prior publication.

## Relationship to prior work

Qing Xia's *Curvature-Distortion Numbers of Graphs: Nonnegative Lin--Lu--Yau Curvature* (arXiv:2609.12125, Section 4.1) determines exactly the **zero-target** double-star value \(\sqrt{ab}\). The later *Curvature-Distortion Numbers of Graphs: Prescribed Lin--Lu--Yau Curvature Lower Bounds* (public Zenodo preprint September 15, 2026; arXiv:2610.21454, Sections 2 and 4) establishes the **general implicit fixed-point characterization**, feasibility and monotonicity for all finite trees. Its examples explicitly give \(P_4\) and the maximum-target \(D_{1,2}\), but not the all-parameters closed two-phase profile or the exact interior activation threshold of this finding. The latter is an explicit family-level refinement, not a replacement for the general theorem.

Bai--Cheng--Hua, *Discrete Einstein metrics on trees* (arXiv:2604.22449), and Cheng, *Positive-Curvature Discrete Einstein Metrics on Trees* (arXiv:2605.20862), concern constant-curvature (Einstein) weights and their spectral classification. Such weights describe the top feasible endpoint, not the constrained minimum-distortion profile at all lower targets. Available records of earlier graph-curvature constructions do not identify the same two-parameter optimization or phase boundary.

## Limitations

The theorem applies only to double stars with positive leaf counts and to curvature computed using fixed combinatorial graph distance, not edge-length transport distance. The proof does not classify larger trees. The general existence and uniqueness of optimal weights for arbitrary trees, the zero-target double-star value and the endpoint examples are known; this result claims only the **explicit complete profile, weights and interior phase transition**. The September 2026 Zenodo document was inspected for public-date metadata and abstract, whereas its October arXiv successor was examined in HTML full text. Literature searches and mathematical-record comparison reduce but cannot remove the risk of an earlier equivalent parameterization. Independent mathematical review and definitive bibliographic priority have not been performed.

## References

1. Qing Xia, *Curvature-Distortion Numbers of Graphs: Prescribed Lin--Lu--Yau Curvature Lower Bounds*, Zenodo version v1, published 2026-09-15, DOI: 10.5281/zenodo.22757916; arXiv:2610.21454 (v1, 2026-10-15), https://arxiv.org/html/2610.21454v1 .
2. Qing Xia, *Curvature-Distortion Numbers of Graphs: Nonnegative Lin--Lu--Yau Curvature*, arXiv:2609.12125 (v1, 2026-09-10), https://arxiv.org/html/2609.12125v2 .
3. Shuliang Bai, Haoxuan Cheng, and Bobo Hua, *Discrete Einstein metrics on trees*, arXiv:2604.22449 (v1, 2026-04-24), https://arxiv.org/html/2604.22449v3 .
4. Haoxuan Cheng, *Positive-Curvature Discrete Einstein Metrics on Trees*, arXiv:2605.20862 (v1, 2026-05-20), https://arxiv.org/html/2605.20862v2 .
