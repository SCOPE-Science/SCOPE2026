# Wasserstein robustness radius for the affine dual Minkowski problem

## Statement

Let \(n\ge 3\), \(m\in\{2,\ldots,n-1\}\), and equip \(S^{n-1}\) with its geodesic distance \(d_S\). For \(1\le p<\infty\), let \(\mathcal P(S^{n-1})\) carry the \(p\)-Wasserstein metric \(W_p\). Define the closed-hemisphere-degenerate data
\[
\mathcal B=\{\nu\in\mathcal P(S^{n-1}):\nu(H_v)=1\text{ for some }v\in S^{n-1}\},
\qquad
H_v=\{u\in S^{n-1}:u\cdot v\ge0\}.
\]
For \(\mu\in\mathcal P(S^{n-1})\), define
\[
\Delta_p(\mu)
=
\min_{v\in S^{n-1}}
\left(\int_{S^{n-1}} d_S(u,H_v)^p\,d\mu(u)\right)^{1/p}.
\]

Then:

1. **Exact distance to loss of solvability.**
   \[
   \boxed{\operatorname{dist}_{W_p}(\mu,\mathcal B)=\Delta_p(\mu).}
   \]
   Since
   \[
   d_S(u,H_v)=\arcsin((-u\cdot v)_+),
   \]
   this is equivalently
   \[
   \boxed{
   \Delta_p(\mu)^p
   =
   \min_{v\in S^{n-1}}
   \int_{S^{n-1}}
   \arcsin((-u\cdot v)_+)^p\,d\mu(u).
   }
   \]

2. **Affine-dual Minkowski solvability is exactly positive transport depth.**
   By Zhang--Jin's general-measure theorem, a nonzero finite Borel measure is the affine dual curvature measure \(\widetilde C_m^a(K,\cdot)\) of a full-dimensional \(K\in\mathcal K_o^n\) if and only if it is not concentrated on a closed hemisphere. Hence, after normalizing total mass,
   \[
   \boxed{
   \mu\text{ is solvable}
   \iff
   \Delta_p(\mu)>0.
   }
   \]
   Consequently \(\Delta_p(\mu)\) is the **largest open \(W_p\)-radius guaranteed to preserve solvability**:
   every \(\nu\) satisfying \(W_p(\mu,\nu)<\Delta_p(\mu)\) remains solvable, while a nonsolvable datum occurs at distance exactly \(\Delta_p(\mu)\).

3. **The nearest nonsolvable perturbation is explicit.**
   If \(v_*\) minimizes the formula for \(\Delta_p\), choose a Borel nearest-point map
   \(P_{v_*}:S^{n-1}\to H_{v_*}\). Then
   \[
   \nu_*=(P_{v_*})_\#\mu\in\mathcal B,
   \qquad
   W_p(\mu,\nu_*)=\Delta_p(\mu).
   \]
   Thus the sharp adversarial perturbation is obtained by projecting all mass outside a minimizing hemisphere onto its boundary great sphere (with an arbitrary nearest-point choice at the antipode).

4. **Convexity and concavity.**
   The solvable set
   \[
   \mathcal A=\mathcal P(S^{n-1})\setminus\mathcal B
   \]
   is convex, open, and dense. Moreover
   \[
   \boxed{
   \Delta_p((1-t)\mu+t\nu)
   \ge
   (1-t)\Delta_p(\mu)+t\Delta_p(\nu)
   \quad(0\le t\le1),
   }
   \]
   so the exact robustness radius is concave under mixing. It is also \(1\)-Lipschitz:
   \[
   |\Delta_p(\mu)-\Delta_p(\nu)|\le W_p(\mu,\nu).
   \]

5. **A convex-body surrogate and an exact \(W_\infty\) formula.**
   Define the one-sided \(L^p\) moment body \(Z_p^+(\mu)\subset\mathbb R^n\) by
   \[
   h_{Z_p^+(\mu)}(w)
   =
   \left(\int_{S^{n-1}}(u\cdot w)_+^p\,d\mu(u)\right)^{1/p}.
   \]
   (For \(p=1\), this is the Minkowski integral of the segments \([0,u]\), hence an ordinary zonoid.)
   For solvable \(\mu\), \(0\in\operatorname{int}Z_p^+(\mu)\). Writing
   \[
   r_0(C)=\max\{r\ge0:rB^n\subset C\}
   \]
   for the origin-centered inradius, one has the dimension-free comparison
   \[
   \boxed{
   r_0(Z_p^+(\mu))
   \le
   \Delta_p(\mu)
   \le
   \frac{\pi}{2}\,r_0(Z_p^+(\mu)).
   }
   \]
   Thus a purely Euclidean convex-body inradius gives a universal-factor certificate for the exact transport robustness radius.

   For \(W_\infty\), let
   \[
   K_\mu=\operatorname{conv}(\operatorname{supp}\mu).
   \]
   Solvability is equivalent to \(0\in\operatorname{int}K_\mu\), and the exact support-sensitive radius is
   \[
   \boxed{
   \operatorname{dist}_{W_\infty}(\mu,\mathcal B)
   =
   \arcsin r_0(K_\mu).
   }
   \]
   In particular, finite-\(p\) robustness records the distribution of mass beyond prospective hemispheres, while \(W_\infty\) robustness depends only on the convex hull of the support.

In particular, the new Zhang--Jin existence criterion admits an exact quantitative stability geometry in Wasserstein data space: solvable normalized data form an open dense convex region, their boundary is precisely the closed-hemisphere-degenerate locus, and \(\Delta_p\) is simultaneously the distance to that locus and a concave stability margin.

## Proof

### 1. Distance to measures supported in one closed set

Let \(X\) be a compact metric space, \(C\subset X\) nonempty and closed, and
\[
\mathcal P(C)=\{\nu\in\mathcal P(X):\nu(C)=1\}.
\]
For every \(\mu\in\mathcal P(X)\),
\[
\inf_{\nu\in\mathcal P(C)}W_p(\mu,\nu)^p
=
\int_X d(x,C)^p\,d\mu(x).
\]

Indeed, if \(\pi\) couples \(\mu\) to a measure supported on \(C\), then
\(d(x,y)\ge d(x,C)\) for \(\pi\)-almost every \((x,y)\), hence
\[
\int d(x,y)^p\,d\pi(x,y)
\ge
\int d(x,C)^p\,d\mu(x).
\]
Conversely, the nearest-point correspondence
\[
x\mapsto\{y\in C:d(x,y)=d(x,C)\}
\]
has nonempty compact values and admits a Borel selector \(P_C\). The coupling
\((\mathrm{id},P_C)_\#\mu\) attains the lower bound.

Applying this to \(C=H_v\),
\[
\operatorname{dist}_{W_p}(\mu,\mathcal P(H_v))^p
=
\int d_S(u,H_v)^p\,d\mu(u).
\]
Since
\[
\mathcal B=\bigcup_{v\in S^{n-1}}\mathcal P(H_v),
\]
taking the infimum over \(v\) gives the asserted distance formula. The minimum is attained because
\[
(v,u)\mapsto d_S(u,H_v)^p
\]
is continuous on the compact product \(S^{n-1}\times S^{n-1}\).

For \(u\cdot v<0\), if \(\theta=\arccos(u\cdot v)\in(\pi/2,\pi]\), the nearest point of \(H_v\) lies on its equator and has angular distance
\(\theta-\pi/2=\arcsin(-u\cdot v)\). For \(u\cdot v\ge0\) the distance is zero. This proves the explicit formula.

### 2. Positivity is exactly the hemisphere condition

If \(\mu\) is concentrated on \(H_v\), then the corresponding integral is zero, so \(\Delta_p(\mu)=0\). Conversely, if \(\mu\) is not concentrated on any closed hemisphere, then for every \(v\),
\[
\mu(S^{n-1}\setminus H_v)>0,
\]
and \(d_S(u,H_v)>0\) there. Thus
\[
F_\mu(v)=\int d_S(u,H_v)^p\,d\mu(u)>0
\]
for every \(v\). The function \(F_\mu\) is continuous on the compact sphere, hence
\(\min_vF_\mu(v)>0\).

Zhang and Jin prove that, for \(n\ge3\) and \(2\le m\le n-1\), a nonzero finite Borel measure \(\eta\) is representable as
\(\widetilde C_m^a(K,\cdot)\) by a full-dimensional \(K\in\mathcal K_o^n\) if and only if \(\eta\) is not concentrated on a closed hemisphere. The condition is invariant under multiplying \(\eta\) by a positive constant; the affine dual curvature measure is \(mn\)-homogeneous, so normalization of total mass loses no solvability information. The equivalence with \(\Delta_p>0\) follows.

Because \(\Delta_p\) is exactly the metric distance to \(\mathcal B\), the open ball of radius \(\Delta_p(\mu)\) around a solvable \(\mu\) avoids \(\mathcal B\), while the minimizing projection constructed above produces an element of \(\mathcal B\) at the boundary radius. This proves sharpness.

### 3. Topology and mixing

The set \(\mathcal B\) is closed. To see this, suppose
\(\mu_j\in\mathcal P(H_{v_j})\) and \(\mu_j\to\mu\) in \(W_p\). Passing to a subsequence, \(v_j\to v\). Joint continuity of
\((u,v)\mapsto d_S(u,H_v)^p\) and weak convergence on the compact sphere give
\[
0
=
\int d_S(u,H_{v_j})^p\,d\mu_j(u)
\longrightarrow
\int d_S(u,H_v)^p\,d\mu(u),
\]
so \(\mu\in\mathcal P(H_v)\).

Its complement \(\mathcal A\) is therefore open. It is dense because for any \(\mu\) and any probability measure \(\sigma\) with full support,
\[
\mu_\varepsilon=(1-\varepsilon)\mu+\varepsilon\sigma
\]
is not concentrated on any closed hemisphere and converges to \(\mu\) as \(\varepsilon\downarrow0\).

It is convex: if \(0<t<1\) and
\((1-t)\mu+t\nu\) were concentrated on \(H_v\), then
\[
0=((1-t)\mu+t\nu)(H_v^c)
=(1-t)\mu(H_v^c)+t\nu(H_v^c),
\]
forcing both \(\mu\) and \(\nu\) to be concentrated on the same hemisphere, contrary to \(\mu,\nu\in\mathcal A\).

Finally,
\[
\Delta_p(\mu)^p
=
\inf_v L_v(\mu),
\qquad
L_v(\mu)=\int d_S(u,H_v)^p\,d\mu(u),
\]
is an infimum of linear functionals of \(\mu\), hence is concave. Therefore
\[
\Delta_p((1-t)\mu+t\nu)
\ge
\big((1-t)\Delta_p(\mu)^p+t\Delta_p(\nu)^p\big)^{1/p}
\ge
(1-t)\Delta_p(\mu)+t\Delta_p(\nu).
\]
The \(1\)-Lipschitz property follows from the general metric inequality
\[
|\operatorname{dist}(x,B)-\operatorname{dist}(y,B)|\le d(x,y)
\]
applied to \((\mathcal P(S^{n-1}),W_p)\) and \(B=\mathcal B\).

### 4. One-sided \(L^p\) moment bodies and the \(W_\infty\) endpoint

The function
\[
w\mapsto
\left(\int (u\cdot w)_+^p\,d\mu(u)\right)^{1/p}
\]
is positively homogeneous and subadditive by \((a+b)_+\le a_++b_+\) and Minkowski's inequality, hence is the support function of a compact convex set \(Z_p^+(\mu)\). If \(\mu\) is solvable, then for every unit \(w\) there is positive \(\mu\)-mass with \(u\cdot w>0\). Compactness therefore gives
\[
r_0(Z_p^+(\mu))
=
\min_{|w|=1}
\left(\int (u\cdot w)_+^p\,d\mu(u)\right)^{1/p}
>0.
\]
Since
\[
x\le\arcsin x\le\frac{\pi}{2}x,\qquad 0\le x\le1,
\]
the explicit formula for \(\Delta_p\), with \(w=-v\), yields
\[
r_0(Z_p^+(\mu))
\le\Delta_p(\mu)
\le\frac{\pi}{2}r_0(Z_p^+(\mu)).
\]

For \(W_\infty\), the fixed-closed-set argument becomes
\[
\operatorname{dist}_{W_\infty}(\mu,\mathcal P(C))
=
\operatorname*{ess\,sup}_{x\sim\mu}d(x,C).
\]
Hence
\[
\operatorname{dist}_{W_\infty}(\mu,\mathcal B)
=
\min_v
\max_{u\in\operatorname{supp}\mu}
\arcsin((-u\cdot v)_+).
\]
A compact subset of \(S^{n-1}\) is contained in a closed hemisphere exactly when the origin is not in the interior of its Euclidean convex hull. Thus for solvable \(\mu\),
\[
0\in\operatorname{int}K_\mu,\qquad
K_\mu=\operatorname{conv}(\operatorname{supp}\mu).
\]
For such \(K_\mu\),
\[
\max_{u\in\operatorname{supp}\mu}(-u\cdot v)_+
=
h_{K_\mu}(-v),
\]
and
\[
\min_{|v|=1}h_{K_\mu}(v)=r_0(K_\mu).
\]
Monotonicity of \(\arcsin\) gives
\[
\operatorname{dist}_{W_\infty}(\mu,\mathcal B)
=
\arcsin r_0(K_\mu).
\]

## Context and originality boundary

Zhang and Jin (2026) establish the exact qualitative existence criterion for the affine dual Minkowski problem with general measures when \(m>1\): solvability is equivalent to not being concentrated on a closed hemisphere. Their paper discusses stability as one of the classical themes surrounding Minkowski problems, but its stated general-measure theorem is qualitative; no Wasserstein distance-to-degeneracy formula, sharp perturbation radius, nearest bad datum, concavity of a robustness margin, one-sided-\(L^p\)-moment-body comparison, or \(W_\infty\)/convex-hull inradius formula was located in the current version.

The fixed-closed-set identity used above is an elementary optimal-transport fact. The claimed contribution is not that identity in isolation, nor Zhang--Jin's existence theorem, but their combination with the geometry of closed hemispheres to obtain an exact and explicit stability theory for this newly solved affine dual Minkowski problem.

The same transport lemma can be reused for other geometric prescription problems whose exact admissibility criterion is exclusion from a compact family of support constraints. No claim is made here that this abstract principle itself is new.

## Limitations

- This result quantifies **existence robustness of the datum**, not continuity, uniqueness, or condition numbers of the realizing convex body \(K\).
- Wasserstein robustness is stated on the fixed-mass probability slice. Positive rescaling of finite data is handled separately by the homogeneity of \(\widetilde C_m^a\).
- No dimension-uniform lower bound for \(\Delta_p\) follows from qualitative solvability alone; admissible measures can approach the bad locus arbitrarily closely.
- The argument uses the Zhang--Jin theorem only in the range \(n\ge3\), \(2\le m\le n-1\).
- The motivating preprint is very recent. Later revisions or unindexed parallel observations may overlap with this stability refinement.
- The 2025 Cai--Leng--Wu--Xi paper introducing the affine dual Minkowski problem was identified as relevant background; its full text was not inspected here for an explicit Wasserstein robustness statement. The available descriptions concern the construction of affine dual curvature measures and the even problem, so this remains a residual originality risk rather than evidence of coverage.

## References

1. Cheng Zhang and Hailin Jin, *Affine dual Minkowski problem for general measures*, arXiv:2609.20003 (2026), especially Theorem 1.5 and the homogeneity statement in Section 2.4.
2. Xiaxing Cai, Gangsong Leng, Yuchi Wu, Dongmeng Xi, *Affine dual Minkowski problems*, Advances in Mathematics 467 (2025), 110184, DOI: 10.1016/j.aim.2025.110184.
3. Cédric Villani, *Optimal Transport: Old and New*, Springer, 2009, for standard Wasserstein-space background.
