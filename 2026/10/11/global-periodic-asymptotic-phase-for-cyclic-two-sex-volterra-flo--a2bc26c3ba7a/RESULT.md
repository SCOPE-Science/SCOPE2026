# Global periodic asymptotic phase for cyclic two-sex Volterra flows

## Finding

For the symmetric cyclic three-type, two-sex inheritance family below, **every initial state whose two sexes collectively contain all three types** has a complete asymptotic description. Female–male imbalance decays at the exact rate \(e^{-t}\), the mean population never loses a type, and its product of coordinates converges with an explicit \(e^{-2t}\) error bound. The mean population either converges to the equal-frequency equilibrium or asymptotically follows one uniquely phased periodic orbit of the zero-sum three-species replicator system. Thus the full off-diagonal four-dimensional state space has no other omega-limit sets under the stated support assumption.

Put \(s=(x+y)/2\), \(d=(x-y)/2\), \(D=\|d(0)\|_1\), \(H(t)=s_1(t)s_2(t)s_3(t)\), and
\[
m_0=H(0)\exp(-2\theta D).
\]
For every \(t\ge0\),
\[
\boxed{\quad H(t)\ge m_0>0,\qquad
|\log H_\infty-\log H(t)|\le\frac{\theta D^2}{2m_0}e^{-2t},\qquad d(t)=e^{-t}d(0).\quad}
\]
The limit \(H_\infty\in[m_0,1/27]\) is well-defined. If \(H_\infty<1/27\), there is a **unique asymptotic phase** \(z_\infty\) on the regular periodic level \(\Gamma_{H_\infty}\) for which
\[
\boxed{\ \|s(t)-\Phi_t(z_\infty)\|=O((1+t)^2e^{-2t}).\ }
\]
Consequently the omega-limit set of \((x(t),y(t))\) equals \(\{(z,z):z\in\Gamma_{H_\infty}\}\). If \(H_\infty=1/27\), both sexes converge to \(u=(1/3,1/3,1/3)\) at rate \(O(e^{-t})\), and the omega-limit set is \(\{(u,u)\}\). All norms on the finite-dimensional state space are equivalent; the rate constants depend on the fixed trajectory.

## Assumptions and scope

Let \(\Delta^2=\{v\in[0,1]^3:\sum_{i=1}^3v_i=1\}\). Indices are read cyclically, so \(i+3=i\). Fix \(\theta\in(0,1]\). For cyclic winner–loser pairs \((i,j)=(1,2),(2,3),(3,1)\), define the parental-type offspring probabilities, equal for daughters and sons and symmetric under exchange of parents, by
\[
p_{ij,i}^{(f)}=p_{ji,i}^{(f)}=p_{ij,i}^{(m)}=p_{ji,i}^{(m)}=(1+\theta)/2,
\]
\[
p_{ij,j}^{(f)}=p_{ji,j}^{(f)}=p_{ij,j}^{(m)}=p_{ji,j}^{(m)}=(1-\theta)/2.
\]
For identical parental types the offspring copies that type with probability one; all other probabilities vanish. Write \(Q_i(x,y)=\sum_{j,k}p_{jk,i}x_jy_k\), using the common offspring law. The continuous system is
\[
\dot x_i=Q_i(x,y)-x_i,\qquad \dot y_i=Q_i(x,y)-y_i
\qquad(i=1,2,3).
\]
The theorem applies to every \((x(0),y(0))\in\Delta^2\times\Delta^2\) for which \(x_i(0)+y_i(0)>0\) for each \(i\). It does not demand interior positivity of **each** sex separately. The \(\theta=1/2\) case includes the explicit cyclic offspring example in Rasulov (2026), Section 3.2, Example 1. The theorem concerns this continuous ODE, not iterates of the discrete stochastic operator. The boundary case where at least one type is absent from both sexes is not covered by the positive-product conclusions.

## Proof

**1. Exact reduction and invariance.** All \(p_{jk,i}\) are nonnegative and sum to one over offspring types. Hence the product simplex is forward invariant: at a zero coordinate the derivative is nonnegative, both coordinate sums are constant, and the polynomial ODE has global forward solutions. Set \(s=(x+y)/2\) and \(d=(x-y)/2\). Subtraction gives \(\dot d=-d\), hence \(d(t)=e^{-t}d(0)\). Since \(x_i=s_i+d_i\ge0\) and \(y_i=s_i-d_i\ge0\), we always have \(|d_i|\le s_i\). Also \(s_i'(t)=Q_i(x(t),y(t))-s_i(t)\ge-s_i(t)\); the assumption \(s_i(0)>0\) implies \(s_i(t)>0\) at each finite time.

The symmetric bilinear offspring law satisfies, for arbitrary vectors \(a,b\) with \(\sum_i a_i=\sum_i b_i=1\),
\[
Q_i(a,a)=a_i+\theta a_i(a_{i+1}-a_{i-1}).
\]
More generally, \(Q_i(v,v)=v_i\sum_jv_j+\theta v_i(v_{i+1}-v_{i-1})\) for any real vector \(v\). Symmetry in the parents gives
\[
Q(s+d,s-d)=Q(s,s)-Q(d,d).
\]
As \(\sum_i s_i=1\) and \(\sum_i d_i=0\), the exact mean equation is
\[
\boxed{\ \dot s_i=\theta s_i(s_{i+1}-s_{i-1})
-\theta d_i(d_{i+1}-d_{i-1}),\quad \dot d_i=-d_i.\ }
\]
The first term is the unperturbed zero-sum cyclic replicator vector field \(F_i(s)\); write the second as \(g_i(t)\). Because \(d(t)=e^{-t}d(0)\), \(g(t)\) is an exactly exponentially decaying perturbation of order \(e^{-2t}\), not merely order \(e^{-t}\). Also \(\sum_i g_i=0\).

**2. Product lower bound and exact stabilization.** Let \(H(s)=s_1s_2s_3\). Dividing the equations by the positive \(s_i\) and summing, the cyclic terms cancel:
\[
\frac{d}{dt}\log H(s(t))
=-\theta\sum_{i=1}^3\frac{d_i(t)}{s_i(t)}[d_{i+1}(t)-d_{i-1}(t)]. \tag{1}
\]
Using \(|d_i|/s_i\le1\), we obtain
\[
\left|\frac{d}{dt}\log H\right|
\le\theta\sum_i|d_{i+1}-d_{i-1}|
\le2\theta\|d(0)\|_1e^{-t}.
\]
Integration proves \(H(t)\ge H(0)e^{-2\theta D}=m_0>0\). The elementary inequality \(s_js_k\le1\) and \(H=s_is_js_k\) imply \(s_i(t)\ge H(t)\ge m_0\) for all \(i,t\). This excludes approach to all three boundary faces, uniformly in time.

The sharpened estimate from (1) is
\[
\left|\frac{d}{dt}\log H\right|
\le\frac{\theta}{m_0}\sum_i|d_i|\,|d_{i+1}-d_{i-1}|
\le\frac{\theta D^2}{m_0}e^{-2t},
\]
since \(|d_{i+1}-d_{i-1}|\le\|d(t)\|_1\). The derivative is absolutely integrable. Therefore the finite limit \(\log H_\infty\) exists, and integration over \([t,\infty)\) gives
\[
|\log H_\infty-\log H(t)|\le \frac{\theta D^2}{2m_0}e^{-2t}.
\]
By the arithmetic–geometric mean inequality, \(H_\infty\le1/27\). The estimate also implies \(H(t)-H_\infty=O(e^{-2t})\). In particular, the limit is strictly positive for every initial state in scope.

**3. Geometry of the limiting levels.** The unperturbed flow \(\Phi_t\) of \(F_i(z)=\theta z_i(z_{i+1}-z_{i-1})\) preserves the simplex and \(H(z)\). On its positive interior, \(\log H=\sum_i\log z_i\) is strictly concave and has its unique critical point and maximum at \(u=(1/3,1/3,1/3)\). Thus, for every \(h\in(0,1/27)\), the level
\[
\Gamma_h=\{z\in\Delta^2:\ z_i>0\ (i=1,2,3),\ H(z)=h\}
\]
is one smooth simple closed curve surrounding \(u\), because it is the regular boundary of the strictly convex superlevel set. The vector field has no zero on \(\Gamma_h\) and is tangent to it. Therefore \(\Gamma_h\) is precisely one periodic orbit, with a smooth period \(T(h)>0\) varying with \(h\).

For clarity, smooth action–angle coordinates can be constructed explicitly: the transversal half-line \(z_1=z_2=q\), \(z_3=1-2q>1/3\), with \(0<q<1/3\), meets each \(\Gamma_h\) once at the unique root of \(q^2(1-2q)=h\). The crossing is transverse, since \(\dot z_1-\dot z_2=2\theta q(3q-1)\ne0\). Flowing from this transversal produces smooth coordinates \((h,\varphi)\), with normalized angular speed \(\omega(h)=2\pi/T(h)\). On any compact annulus \(0<h_-\le H(z)\le h_+<1/27\), differentiating the explicit action–angle translation yields the uniform derivative bound
\[
\sup_{z\text{ in annulus}}\|D\Phi_t(z)\|\le C(1+|t|),\qquad t\in\mathbb R. \tag{2}
\]
The compact annulus can be chosen slightly larger to accommodate short segments between sufficiently close points.

**4. Noncentral case: a unique periodic asymptotic phase.** If \(H_\infty<1/27\), the convergence in step 2 confines \(s(t)\), for all sufficiently large \(t\), to a fixed compact regular annulus of the unperturbed flow. Set \(z(t)=\Phi_{-t}(s(t))\). The chain rule, the group law for \(\Phi_t\), the mean equation, and (2) give
\[
\dot z(t)=D\Phi_{-t}(s(t))\,g(t),\qquad
\|\dot z(t)\|\le C(1+t)e^{-2t}.
\]
It follows by absolute integration that \(z(t)\to z_\infty\) and \(\|z(t)-z_\infty\|=O((1+t)e^{-2t})\). Since \(H(z(t))=H(s(t))\to H_\infty\), the limit belongs to \(\Gamma_{H_\infty}\). Applying the forward bound (2) to the pair \(z(t),z_\infty\) gives
\[
\|s(t)-\Phi_t(z_\infty)\|
=\|\Phi_t(z(t))-\Phi_t(z_\infty)\|
=O((1+t)^2e^{-2t}).
\]
The asymptotic phase is unique: two different points of one nonstationary periodic orbit have a fixed strictly positive orbital separation at the same time (apply \(\Phi_{-t}\) to the hypothesized coincidence, or use smooth periodic phase coordinates). Combining \(x=s+d\), \(y=s-d\), and \(d(t)=e^{-t}d(0)\), the full state is \(O(e^{-t})\) from the synchronized periodic trajectory \((\Phi_t(z_\infty),\Phi_t(z_\infty))\). Its omega-limit set is exactly the full diagonal copy of \(\Gamma_{H_\infty}\), because the reference orbit is periodic and the tracking error vanishes.

**5. Central case.** If \(H_\infty=1/27\), step 2 gives \(1/27-H(s(t))=O(e^{-2t})\). On the tangent plane \(\sum_i(z_i-1/3)=0\), expansion at the strict nondegenerate maximum gives
\[
H(u+w)=1/27-\tfrac16\sum_iw_i^2+w_1w_2w_3.
\]
Compactness and the uniqueness of the maximum imply \(s(t)\to u\), after which the quadratic expansion proves \(\|s(t)-u\|=O(e^{-t})\). The same rate for both sexes follows from the exact \(d(t)\) equation. Their omega-limit set is the single diagonal equilibrium. This exhausts the dichotomy.

## Verification

The offspring-law reduction and the cancellation of the unperturbed product derivative are polynomial identities valid for all real \(\theta\); they were independently expanded symbolically in SymPy 1.14 on the full six-coordinate system, using the two simplex constraints only after expansion. A numerical diagnostic for \(\theta=1/2\), \(s(0)=(1/2,1/3,1/6)\), and \(d(0)=(1/15,-1/20,-1/60)\) retains all three positive mean coordinates and exhibits exponentially decaying sex imbalance. The exact ODE identity, the explicit analytic product estimates, and the compact-annulus phase-coordinate proof—not these finite diagnostics—establish the theorem for all initial states in scope.

A proof replay needs no computer calculation: substitute the offspring coefficients into the symmetric bilinear form, subtract the sex equations, sum \(\dot s_i/s_i\), integrate the two elementary exponential bounds, and apply the transversal construction on the strictly convex positive product levels. The phase derivative bound in (2) follows from differentiating \((h,\varphi)\mapsto(h,\varphi+\omega(h)t)\). All constants implicit in asymptotic notation are trajectory-dependent and no uniform estimate is claimed near the vanishing-product boundary or the central resonance.

## Relationship to prior work

Rasulov (2026, Section 3.2, Lemma 6 and Example 1) proves periodicity **on the invariant diagonal** \(x=y\) under the skew-rank condition, including the cyclic inheritance coefficients \(3/4\) and \(1/4\). The present claim concerns **all off-diagonal initial states with full collective support**, and obtains explicit persistence, convergence of a formerly nonconserved product, and asymptotic phase tracking with rates; these do not follow from diagonal invariance or the diagonal periodicity theorem alone.

Earlier two-sex continuous-time studies by Rasulov (2024) handle particular two-type extreme operators and convergence to equilibria. The full Mathematical Notes article was checked; in particular its equation (2.6) already identifies exact exponential decay of the sex difference in the two-type context. Thus exact sex-difference decay **alone** is not presented as new. The qualitative product/periodic-shadowing conclusion in this three-type cyclic setting is the central added assertion. Rozikov and Jamilov (2011) concern discrete two-sex Volterra operators; their discrete results do not automatically imply the continuous-time orbit classification. The 2024 Lobachevskii paper *On a Volterra Dynamical System of a Two-Sex Population* is a plausible additional comparator but only its abstract and bibliographic data were accessible, so complete negative coverage cannot be asserted for that text. General asymptotically autonomous and integrable perturbation results may subsume qualitative portions; the explicit population-specific product bound, support boundary, and quantitative phase tracking require comparison in any future independent literature audit.

## Limitations

The theorem requires common symmetric daughter/son heredity, the three-cycle, \(0<\theta\le1\), and full **collective** three-type support at the initial time. For initially absent types the product bound vanishes and other boundary dynamics are possible. The assertion is for the **continuous** ODE rather than the discrete update. The exact limiting product and asymptotic phase depend on the initial pair, and no closed elementary expression for either is asserted. Tracking constants need not be uniform as the limiting product approaches zero or its maximum \(1/27\). The result does not prove any statement for asymmetric female/male heredity, higher-dimensional cycles, or stochastic noise. A same-model scientific review is not an independent audit.

## References

1. X. R. Rasulov, *Analytical solutions of one class of Volterra quadratic stochastic operators of a two-sex population with continuous time*, arXiv:2610.06895v1, first public 28 September 2026, Sections 2 and 3.2, especially Lemma 6 and Example 1. https://arxiv.org/html/2610.06895v1
2. X. R. Rasulov, *On the Qualitative Analysis of a Class of Volterra Quadratic Stochastic Operators with Continuous Time*, Mathematical Notes **116** (2024), 1080–1093, DOI:10.1134/S0001434624110208. Open author-hosted PDF: https://uniwork.buxdu.uz/resurs/13150_1_094740AB52E50118C9B454EACABA9B94990124E1.pdf
3. X. R. Rasulov, *On a Volterra Dynamical System of a Two-Sex Population*, Lobachevskii Journal of Mathematics **45** (2024), 3975–3985, DOI:10.1134/S199508022460448X (abstract and citation available; full text not verified).
4. U. A. Rozikov and U. U. Jamilov, *Volterra quadratic stochastic operators of a two-sex population*, Ukrainian Mathematical Journal **63** (2011), 1136–1153, DOI:10.1007/s11253-011-0568-y (discrete operators).
