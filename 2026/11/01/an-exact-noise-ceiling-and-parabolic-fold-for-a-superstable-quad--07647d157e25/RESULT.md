# An exact noise ceiling and parabolic fold for a superstable quadratic two-cycle

## Finding

Consider the one-dimensional set-valued map
\[
\mathcal F_\varepsilon(X)=\{1-x^2+u:x\in X,\ |u|\le\varepsilon\},
\qquad 0<\varepsilon\le1/20.
\]
A **separated two-band trap** is an ordered pair of nonempty compact real intervals \(I_0,I_1\) such that \(0\in I_0\), \(1\in I_1\), \(\sup I_0<\inf I_1\), and \(\mathcal F_\varepsilon(I_0)\subseteq I_1\), \(\mathcal F_\varepsilon(I_1)\subseteq I_0\). This is a robust property: it applies simultaneously to every allowed input sequence, not just almost surely to a particular noise distribution.

**Theorem.** Such a trap exists if and only if
\[
0<\varepsilon\le\varepsilon_c,\qquad
\varepsilon_c=\frac{\sqrt{73-22\sqrt{11}}}{4}
=0.0462700039045298489\ldots.
\]
For \(0<\varepsilon<\varepsilon_c\), let \(u_-\) and \(u_+\) be the two roots in the interval \((0,s_\varepsilon)\) of
\[
p_\varepsilon(u)=3\varepsilon-\varepsilon^2+2(1-\varepsilon)u^2-u^4-u,
\qquad
s_\varepsilon=\frac{-1+\sqrt{5-4\varepsilon}}2.
\]
Then \(0<u_-<u_+<s_\varepsilon\), and each root gives an *exact*, rather than merely trapping, swapped two-band pair:
\[
I_0(u)=[-3\varepsilon-\varepsilon^2,u],\qquad
I_1(u)=[1-u^2-\varepsilon,1+\varepsilon],
\]
\[
\mathcal F_\varepsilon(I_0(u))=I_1(u),\qquad
\mathcal F_\varepsilon(I_1(u))=I_0(u).
\]
The pair from \(u_-\) is the smallest compact forward-invariant set containing the deterministic two-cycle \(\{0,1\}\), and the corresponding boundary return is attracting; the pair from \(u_+\) has a repelling boundary return. At \(\varepsilon=\varepsilon_c\) the two saturated pairs coalesce at a double root \(u_c=0.2868859438756555727\ldots\), while the spatial gap between the bands still equals \(0.5845405074263887791\ldots>0.58\). For \(\varepsilon_c<\varepsilon\le1/20\), no separated two-band trap containing \(0\) and \(1\) exists, even with slack inclusions.

The two endpoint branches have an exact square-root fold. Define
\[
E=3-2\varepsilon_c-2u_c^2>0,\qquad
B=4(1-\varepsilon_c)-12u_c^2>0.
\]
As \(\varepsilon\uparrow\varepsilon_c\),
\[
u_\pm(\varepsilon)=u_c\pm\sqrt{\frac{2E}{B}}\sqrt{\varepsilon_c-\varepsilon}
+O(\varepsilon_c-\varepsilon),\qquad
\sqrt{2E/B}=1.3929388203121\ldots.
\]
At the critical parameter the two-step upper-endpoint recurrence, started a little below \(u_c\), has the parabolic law
\[
u_c-u_m\sim\frac{2}{Bm}\qquad(m\longrightarrow\infty),
\]
where \(m\) counts **two-step returns**, not individual time steps. This is one-sided algebraic approach of the endpoint, not a claim of two-sided local attraction of the critical trap.

## Assumptions and scope

The deterministic map \(f(x)=1-x^2\) has the superstable period-two orbit \(0\mapsto1\mapsto0\). The perturbation is an arbitrary additive scalar input from the **closed interval** \([-\varepsilon,\varepsilon]\), independently selectable at each iteration. The theorem is concerned with ordered, cycle-compatible, separated **interval** traps containing both deterministic cycle points. There is no claim of uniform boundedness for arbitrary initial real points; this polynomial map has escaping orbits. No probabilistic independence assumption is needed for the trapping classification. The strict upper noise cutoff \(1/20\) ensures the elementary sign comparisons used in the global iff argument, and is not asserted to be the largest possible parameter range for any related phenomenon.

## Proof

**1. A necessary scalar inequality for every trap.** Write an arbitrary candidate as \(I_0=[a,u]\) and \(I_1=[v,w]\) with \(a\le0\le u<v\le1\le w\). Since \(\mathcal F_\varepsilon(\{0\})\subseteq I_1\), \(w\ge1+\varepsilon\). Since \(\mathcal F_\varepsilon(\{1\})\subseteq I_0\), \(u\ge\varepsilon>0\). Taking the images of the particular endpoints \(u\in I_0\) and \(v\in I_1\) gives
\[
v\le1-u^2-\varepsilon=:h>0,
\qquad
u\ge1-v^2+\varepsilon\ge1-h^2+\varepsilon=:g_\varepsilon(u).
\]
Here the last inequality uses \(0<v\le h\). Expanding gives \(g_\varepsilon(u)-u=p_\varepsilon(u)\). Hence every trap satisfies
\[
0<u<1,\qquad p_\varepsilon(u)\le0. \tag{1}
\]
This necessary condition covers **all** interval endpoints, not merely the normalized exact-image ansatz.

**2. The critical parameter and global obstruction.** Direct differentiation gives
\[
p'_\varepsilon(u)=4u(1-\varepsilon-u^2)-1,
\qquad p''_\varepsilon(u)=4(1-\varepsilon)-12u^2.
\]
Eliminating \(u\) from \(p_\varepsilon(u)=p'_\varepsilon(u)=0\) yields
\[
256\varepsilon^4-2336\varepsilon^2+5=0.
\]
Its only positive root in \((0,1/20)\) is the stated \(\varepsilon_c\). The corresponding \(u_c\), determined uniquely in \((0.286,0.288)\), is explicitly
\[
u_c=\frac{51+64\varepsilon_c^3-16\varepsilon_c^2-556\varepsilon_c}{88}.
\]
Substitution verifies \(p_{\varepsilon_c}(u_c)=p'_{\varepsilon_c}(u_c)=0\). The exact factorization
\[
p_{\varepsilon_c}(u)=(u-u_c)^2 H(u),\qquad
H(u)=2(1-\varepsilon_c)-3u_c^2-2u_cu-u^2
\]
shows that \(p_{\varepsilon_c}(u)\ge0\) for all \(u\in[0,1]\), with equality only at \(u_c\). Indeed, \(H\) is decreasing on \([0,1]\), and the rational bounds \(0.046<\varepsilon_c<0.047\), \(0.286<u_c<0.288\) imply
\[
H(1)>2(1-0.047)-3(0.288)^2-2(0.288)-1>0.
\]
For any \(u\in[0,1]\) and \(\varepsilon\in[\varepsilon_c,1/20]\),
\[
\partial_\varepsilon p_\varepsilon(u)=3-2\varepsilon-2u^2\ge0.9.
\]
Thus \(p_\varepsilon(u)>0\) everywhere on \((0,1)\) if \(\varepsilon>\varepsilon_c\). Condition (1) rules out *every* separated two-band trap in this parameter range.

**3. Existence of both saturated pairs below the fold.** Fix \(0<\varepsilon<\varepsilon_c\). On \([0,u_c]\), \(p''_\varepsilon>0\), while \(p_\varepsilon(0)>0\) and \(p_\varepsilon(u_c)<0\), the latter because \(\partial_\varepsilon p_\varepsilon(u_c)>0\) and \(p_{\varepsilon_c}(u_c)=0\). Therefore there is exactly one root \(u_-\in(0,u_c)\), crossed with \(p'_\varepsilon(u_-)<0\). In fact \(u_->3\varepsilon+\varepsilon^2\): substituting the lower bound gives
\[
p_\varepsilon(3\varepsilon+\varepsilon^2)=-\varepsilon^2(\varepsilon+2)
(\varepsilon^5+10\varepsilon^4+34\varepsilon^3+42\varepsilon^2+7\varepsilon-8)>0
\]
for \(0<\varepsilon<1/20\), and the convexity argument locates its crossing above this bound. The function \(p_\varepsilon\) is strictly increasing from \(u_c\) to \(s_\varepsilon\): its derivative is concave on the positive half-line, positive at \(u_c\) and positive at \(s_\varepsilon\), where \(p'_\varepsilon(s_\varepsilon)=4s_\varepsilon^2-1>0\). Also \(p_\varepsilon(s_\varepsilon)=2\varepsilon>0\). Hence there is exactly one second root \(u_+\in(u_c,s_\varepsilon)\), crossed with positive derivative. (For this range, \(s_\varepsilon>0.59>u_c\).)

For either root, \(u>3\varepsilon+\varepsilon^2\) and \(u<s_\varepsilon\) imply \(0\in I_0\), \(0<\inf I_1\), \(\sup I_0<\inf I_1\), and \(u\ge|\inf I_0|\). As \(f\) has its maximum at zero and decreases on the positive half-line, direct interval arithmetic gives
\[
\mathcal F_\varepsilon(I_0)=[1-u^2-\varepsilon,1+\varepsilon]=I_1,
\]
\[
\mathcal F_\varepsilon(I_1)=[-3\varepsilon-\varepsilon^2,g_\varepsilon(u)]=I_0.
\]
This constructs the traps. Since \(g'_\varepsilon(u)=p'_\varepsilon(u)+1\), the small branch has \(0<g'_\varepsilon(u_-)<1\), whereas the large branch has \(g'_\varepsilon(u_+)>1\). These statements classify the boundary return, not sample-path Lyapunov exponents.

For minimality of the smaller pair among closed invariant sets containing \(\{0,1\}\), iterate the interval-valued reachability operator from those two points, taking cumulative unions at each parity. Every resulting set is contained in the smaller pair. Because the additive input has full interval support, after finite steps both parity components are intervals, containing \(0\) and \(1\), respectively. Their increasing endpoints converge to an exact swapped invariant interval pair. The limiting upper endpoint must satisfy \(p_\varepsilon(u)\le0\) by step 1, whereas \(p_\varepsilon(u)>0\) for \(0\le u<u_-\). Containment in the smaller pair therefore forces its upper endpoint to be \(u_-\), and equality in the endpoint bounds forces all other endpoints. Thus the closure of reachable states equals the smaller pair and lies in every closed forward-invariant set containing the original orbit.

**4. Endpoint fold and critical slowing.** At the critical parameter \(p_{\varepsilon_c}\) has exactly one root in \([0,1]\), so the normalized exact-image pair is uniquely specified. The spatial gap is \(1-u_c^2-\varepsilon_c-u_c>0.58\), evaluated using the explicit expressions. Since \(\partial_\varepsilon p_{\varepsilon_c}(u_c)=E>0\) and \(p''_{\varepsilon_c}(u_c)=B>0\), Taylor expansion gives
\[
0=-E(\varepsilon_c-\varepsilon)+\tfrac12 B(u-u_c)^2
+O\bigl((\varepsilon_c-\varepsilon)|u-u_c|+|u-u_c|^3+(\varepsilon_c-\varepsilon)^2\bigr),
\]
which proves the stated two-branch square-root law. At criticality, for an endpoint \(u_m<u_c\) sufficiently near \(u_c\), \(u_{m+1}=g_{\varepsilon_c}(u_m)\) increases to \(u_c\). Writing \(d_m=u_c-u_m\),
\[
d_{m+1}=d_m-\tfrac12 B d_m^2+O(d_m^3).
\]
Therefore \(d_{m+1}^{-1}-d_m^{-1}\to B/2\), whence \(m d_m\to2/B\). This is a one-sided, two-step endpoint asymptotic.

## Verification

The standalone `verify.py` checks the exact critical polynomial numerically; both saturated interval images on 23 subcritical parameter samples; stability and repulsion of the two boundary branches; the critical factorization on randomized parameters; the strict obstruction on parameter and endpoint grids above threshold; the fold coefficient; and the critical inverse-iteration law. These finite diagnostics do not establish the universal theorem: the inequalities, algebraic elimination and interval arguments above are the proof.

Run `python3 verify.py` from the same folder; it requires only the Python standard library. For independent exact-algebra checks of the resultant and critical factorization, run `python3 symbolic_check.py` (requires SymPy). The symbolic checker was executed successfully and returned `PASS 4 exact polynomial certificates`.

## Relationship to prior work

Lamb, Rasmussen and Tey (2025 preprint; 2026 journal publication) introduce and numerically study boundary/topological bifurcations of *two-dimensional* noisy Hénon maps with spherical bounded input, including fold mechanisms of a boundary map. This finding treats a distinct, degenerate **scalar**, one-coordinate-noise quadratic model, gives an algebraic threshold and proves an all-traps obstruction. Their general conceptual terminology and the set-valued reachability approach are prior art.

Sato, Doan, Lamb and Rasmussen (2018) study a noisy logistic map with a **period-three** attractor at growth parameter approximately \(3.83\). Their Eq. (12) supplies a *generic* composition-and-tangency criterion for a critical noise value, but does not state the present exact radical for the superstable period-two parameter, prove the present global separation equivalence, or compute the parabolic endpoint law. Tey, Olicón-Méndez, Lamb and Aihara (2025) treat early-warning statistics for bounded-noise **order-preserving diffeomorphisms**; their boundary-fold mechanism is conceptually relevant, but cannot directly cover the present non-invertible quadratic folding map. The exact algebraic noise ceiling, necessity against arbitrary interval endpoints, and the persistent physical gap form the assessed contribution. The map here is affinely conjugate to the logistic map with growth parameter \(1+\sqrt5\), so the present claim is **not** proposed as a new class of stochastic models. Unlocated specialized logistic-noise calculations remain a historical-priority risk.

## Limitations

No claim is made that every real trajectory remains bounded, that all random pullback attractors have this form, that the critical pair attracts from both sides, or that any two-dimensional Hénon bifurcation has the same value. Noise is scalar and set-valued; the statements are independent of a particular probability distribution and concern two alternating **interval** bands containing the specified superstable orbit. The complete iff classification here is restricted to \(0<\varepsilon\le1/20\). Historical originality was assessed against inspected accessible literature and mathematical records, not independently certified against every publication.

## References

1. J. S. W. Lamb, M. Rasmussen, W. H. Tey, *Bifurcations of the Hénon Map with Additive Bounded Noise*, arXiv:2504.02776, first posted 2025-04-03; subsequently SIAM J. Appl. Dyn. Syst. 25 (2026), 351–374, DOI: 10.1137/25M174797X.
2. Y. Sato, T. S. Doan, J. S. W. Lamb, M. Rasmussen, *Dynamical characterization of stochastic bifurcations in a random logistic map*, arXiv:1811.03994, first posted 2018-11-09; in particular Eq. (12).
3. W. H. Tey, G. Olicón-Méndez, J. S. W. Lamb, K. Aihara, *Anticipating bifurcations of random dynamical systems through tails of stationary densities*, arXiv:2510.15057, first posted 2025-10-16; order-preserving setting.
4. D. Steinsaltz, *Random logistic maps and Lyapunov exponents*, Indagationes Mathematicae 12 (2001), 557–584, DOI: 10.1016/S0019-3577(01)80042-2. A background theorem about random point convergence, not a source for the threshold computed here.
