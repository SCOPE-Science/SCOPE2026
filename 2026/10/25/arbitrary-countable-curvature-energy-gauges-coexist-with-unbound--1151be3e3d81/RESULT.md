# Arbitrary countable curvature-energy gauges coexist with unbounded immersion mean curvature

## Finding
For every \(\eta>0\) and every countable family of **continuous, nondecreasing, finite-valued** gauges \(\Phi_i:[0,\infty)\to[0,\infty)\), indexed by positive integers and satisfying \(\Phi_i(0)=0\), there exists a smooth complete metric \(g\) on \(\mathbb R^4\) with the following simultaneous properties:

\[
\|g-\delta\|_{C^1(\delta)}<\eta,\quad
\sup_{\mathbb R^4}|\operatorname{Ric}_g|_g<\eta,\quad
\operatorname{inj}(\mathbb R^4,g)>0,\quad
|\operatorname{Ric}_g(x)|_g\longrightarrow0\ (|x|\to\infty),
\]
\[
\forall i\ge1:\quad \int_{\mathbb R^4}\Phi_i(|\operatorname{Rm}_g|_g)\,dV_g<\infty.
\]
At the explicitly separated points \(p_j=(4j,0,0,0)\), one has
\[
|\operatorname{Rm}_g|_g(p_j)=12j.
\]
For every integer \(N\ge4\) and every \(C^2\) isometric immersion \(F:(\mathbb R^4,g)\to\mathbb R^N\), the **normalized** mean-curvature vector \(H_F=\frac14\operatorname{tr}_g A_F\) satisfies
\[
|H_F(p_j)|^2\ge\frac38j\qquad (j\ge1).
\]
Therefore bounded mean curvature is impossible for every such immersion. Also \(c r^4\le \operatorname{Vol}_g(B_g(x,r))\le C r^4\) for all centers and radii, with positive constants independent of the center. In particular, choose the countable gauges \(t\mapsto t^q\) for all positive integers \(q\), together with \(t\mapsto e^{kt}-1\) for positive integers \(k\): one metric then has every finite global curvature power moment and every such exponential moment, despite its unbounded pointwise curvature.

## Assumptions and scope
The norm \(\|g-\delta\|_{C^1(\delta)}\) is the supremum of the Euclidean componentwise zero- and first-order derivatives of \(g-\delta\); the Ricci and full-curvature norms are induced by \(g\). Curvature-energy finiteness concerns integration against global Riemannian volume on the **noncompact** manifold, which has infinite total volume. The condition \(\Phi_i(0)=0\) is essential because \(g\) is Euclidean outside disjoint compact perturbations. The gauges are prescribed in advance and the metric may depend on the entire countable family. The target is finite-dimensional Euclidean space, with no restriction on codimension.

We use the explicit four-dimensional quadratic model from Cheng [1], whose primary MSC classification is 53C42. Set \(x=(x_1,x_2,x_3,x_4)\), \(r=|x|\), and
\[
P(x)=\begin{pmatrix}
x_2^2-x_3^2&-x_1x_2&x_1x_3&0\\
-x_1x_2&x_1^2-x_4^2&0&x_2x_4\\
x_1x_3&0&-x_1^2+x_4^2&-x_3x_4\\
0&x_2x_4&-x_3x_4&-x_2^2+x_3^2
\end{pmatrix}.
\]
Choose a smooth radial cutoff \(\chi\), equal to one for \(r\le1/4\) and zero for \(r\ge1/2\). For \(0<\varepsilon\le1/8\), put
\[
h_\varepsilon(x)=\frac12\chi(|x|)\log(|x|^2+\varepsilon^2)P(x),\qquad g_{a,\varepsilon}=\delta+a h_\varepsilon.
\]
The uniform analytic bounds on this model, including Ricci bounds, curvature envelope, and geodesic estimates, are those proved in Propositions 3.3 and 5.2 and Sections 4–5 of [1]. The new ingredient here is a simultaneous gauge-integrability diagonalization that preserves the precisely calibrated curvature peaks.

## Proof
**1. Uniform local geometry and curvature calibration.** The source establishes absolute constants \(a_0,C_0,C_1>0\) such that for \(0<a\le a_0\), independent of \(\varepsilon\), one has \(0.9\delta\le g_{a,\varepsilon}\le1.1\delta\), \(\|a h_\varepsilon\|_{C^1}\le C_0a\), and
\[
|\operatorname{Ric}_{g_{a,\varepsilon}}|\le C_1(a+a^2),\quad
|\operatorname{Rm}_{g_{a,\varepsilon}}(x)|\le
C_1(a+a^2)\Bigl(1+\log_+\frac1{|x|+\varepsilon}\Bigr)
\quad (|x|\le1/2).
\]
The tensor is identically zero outside the supporting ball. At \(x=0\), the metric is Euclidean and its first derivatives vanish. The Hessian equals \(a\log(\varepsilon)\partial^2P\). The curvature tensor is linear in the metric Hessian at that point, so the exact quadratic-tensor calculation gives
\[
\operatorname{Ric}(0)=0,\quad
|\operatorname{Rm}(0)|=12a\log(1/\varepsilon).
\]
These identities, including the zero Ricci contraction and full curvature coefficient squared \(144\), are reproduced symbolically by `verify_peak.py`.

**2. Decoupling a peak from each fixed energy.** Fix a positive integer \(j\). For each \(a\in(0,\min(a_0,1)]\), set
\[
\varepsilon_j(a)=\exp(-j/a),\quad
E_{a,j}(r)=C_1(a+a^2)\left(1+\log_+\frac1{r+\varepsilon_j(a)}\right),\quad 0\le r\le1/2.
\]
Since \(\log_+(1/(r+\varepsilon_j(a)))\le j/a\), for \(0<a\le1\) the envelope obeys \(0\le E_{a,j}(r)\le 2C_1(j+1)\), uniformly in \(r\). For each fixed \(r>0\), \(E_{a,j}(r)\to0\) as \(a\downarrow0\); only the single point \(r=0\) can retain a peak. Consequently, for every fixed index \(i\), continuity at zero, monotonicity, and dominated convergence on the Euclidean half-ball give
\[
\lim_{a\downarrow0}\int_{B(0,1/2)} \Phi_i(E_{a,j}(|x|))\,dx=0.
\]
Here domination is by the finite constant \(\Phi_i(2C_1(j+1))\) on a fixed finite-volume ball; no unproved integrability of a logarithmic singularity is invoked. Moreover \(\varepsilon_j(a)\le1/8\) once \(a\) is sufficiently small.

**3. Simultaneous diagonal selection.** Choose a positive sequence \(a_j\) recursively, with \(a_j\le \min\{a_0,2^{-j},\eta/(10C_0),c(\eta)\}\) and \(\varepsilon_j=\exp(-j/a_j)\), so small that
\[
(1.1)^2\int_{B(0,1/2)}\Phi_i(E_{a_j,j}(|x|))\,dx<2^{-j}\quad\text{for every }1\le i\le j.
\]
This is possible because there are only finitely many inequalities for each \(j\) and all their left-hand sides tend to zero as \(a_j\downarrow0\). Choose \(c(\eta)>0\) so that \(C_1(c+c^2)<\eta\), and small enough for the uniform injectivity estimate in Step 5. Define
\[
g(x)=\delta+\sum_{j=1}^{\infty}a_jh_{\varepsilon_j}(x-p_j),\qquad p_j=(4j,0,0,0).
\]
The supports are pairwise disjoint and locally finite. Thus \(g\) is smooth, complete, uniformly bilipschitz to \(\delta\), \(C^1\)-close to \(\delta\), and its Ricci tensor has the asserted small bound; because \(a_j\to0\), the Ricci bound also tends to zero along supports escaping to infinity. The mean-curvature obstruction peaks are exactly \(12a_j\log(1/\varepsilon_j)=12j\).

For each fixed \(i\), the curvature energy splits into a finite sum over \(j<i\) (finite since those individual perturbations are smooth on compact balls) plus a tail bounded by \(\sum_{j\ge i}2^{-j}<\infty\), since \(dV_g\le(1.1)^2dx\), the envelopes dominate the curvature, and each gauge is nondecreasing. Outside the supports the metric is Euclidean, and the integrand vanishes because \(\Phi_i(0)=0\). This proves simultaneous global integrability. Bilipschitz comparison of distances and volumes gives uniform fourth-order volume growth.

**4. Euclidean mean-curvature obstruction.** At every \(p_j\), exact algebra gives \(\operatorname{Ric}_g(p_j)=0\), hence scalar curvature zero, while \(|\operatorname{Rm}_g|(p_j)=12j\). Let \(A\) be the second fundamental form of any \(C^2\) Euclidean isometric immersion. The Gauss equation implies \(|\operatorname{Rm}|\le 2|A|^2\). Its scalar trace reads \(\mathrm{Scal}=16|H|^2-|A|^2\), for normalized \(H=\frac14\operatorname{tr}A\). At the selected points, \(|A|^2=16|H|^2\), hence
\[
12j\le 32|H(p_j)|^2,\quad\text{or}\quad |H(p_j)|^2\ge3j/8.
\]
There is no finite global bound for the mean-curvature vector of any such immersion.

**5. Global positive injectivity radius.** We do not infer injectivity solely from the bilipschitz bound or bounded Ricci. The source's Sections 4–5 prove that for this explicit tensor profile, for each short geodesic segment of length \(\ell\le1\), there is a uniform integral bound
\[
\int_\gamma |\operatorname{Rm}|\,ds\le C a_*\ell\left(1+\log\frac4\ell\right),\quad a_*:=\sup_j a_j,
\]
independent of the individual \(\varepsilon_j\), because a short segment intersects at most one support and its residence time in a small coordinate ball is uniformly controlled. The Jacobi/short-loop arguments of Proposition 5.2 of [1] then give a positive global injectivity-radius bound when \(a_*\) is sufficiently small. The proof uses only the uniform small-amplitude and separation hypotheses, not equality of the amplitudes; these are met here. This completes the construction.

## Verification
Run `python verify_peak.py` with SymPy installed. It checks exact quadratic identities \(\operatorname{tr}P=0\), \(\partial_iP_{ij}=0\), \(x_iP_{ij}=0\), \(\Delta P_{ij}=0\), as well as the Ricci contraction and Euclidean full-curvature norm of the quadratic coefficient: \(\|R(P)\|^2=144\), ensuring the center coefficient \(12\). The infinite-dimensional conclusion does **not** follow from computation: the simultaneous-energy step is proved by pointwise convergence, bounded domination, and a finite-at-each-stage diagonal choice, while global injectivity invokes the proved uniform geodesic estimate from [1].

## Relationship to prior work
Cheng [1, §§3–6] constructs uniformly nearly Euclidean four-dimensional metrics with small decaying Ricci curvature, positive injectivity radius and pointwise full-curvature peaks, proving a counterexample to the bounded-mean-curvature immersion question. Its variable-amplitude example prescribes curvature growth; it does **not** impose arbitrary prescribed countable global curvature-energy gauges. The present statement retains the exact nonembedding mechanism but adds a simultaneous family of integrability constraints that can grow arbitrarily quickly with curvature, by concentration and a new gauge-by-gauge diagonal argument. Cheeger–Naber [2, Theorems 1.8, 1.13] establish local curvature-integrability estimates under other geometric hypotheses; those results are neither constructions with freely prescribed global gauges nor bounded-mean-curvature immersion statements. Hence no coverage or implication of the current countable-gauge existence result was located in the inspected primary texts or the available related-result searches.

## Limitations
The quantifiers require the metric to be selected **after** choosing the countable gauges. No single metric is asserted to integrate every possible continuous gauge. Each gauge is finite-valued and continuous at zero and vanishes at zero; no claim covers, for example, \(\Phi(0)>0\) on an infinite-volume manifold. Although the example has every prescribed global Orlicz-type energy finite, it has no global uniform bound on full curvature, and no assertion about the existence of an isometric immersion is made. The proof of uniform injectivity imports precise analytic and geodesic estimates from [1], while the independent algebraic reproduction and the new diagonal argument are given here. Closely related unindexed constructions could affect priority; no independent mathematical audit has been performed.

## References
[1] H. Cheng, *A counterexample to Yau's bounded-mean-curvature embedding question*, arXiv:2610.00153v1 (first publicly posted 10 September 2026), especially Propositions 3.3 and 5.2 and §§3–6. https://arxiv.org/abs/2610.00153

[2] J. Cheeger and A. Naber, *Regularity of Einstein manifolds and the codimension 4 conjecture*, arXiv:1406.6534v10 (2015), especially Theorems 1.8 and 1.13. https://arxiv.org/abs/1406.6534
