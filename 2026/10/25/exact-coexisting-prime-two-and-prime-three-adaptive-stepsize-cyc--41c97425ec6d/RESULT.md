# Exact prime-two and prime-three adaptive stepsize cycles with saddle-type return dynamics

## Finding

The original adaptive proximal-gradient method adaPGM of Latafat, Themelis, Stella and Patrinos (Algorithm 2.1, 2023) permits exact positive nonconstant stepsize cycles of prime periods two and three on the scalar strongly convex quadratic \(f(x)=\lambda x^2/2\), \(\lambda>0\), with \(g\equiv0\). Both cycles have a **saddle-type, locally unstable return map**: its multipliers are \(0\) and a real number smaller than \(-1\). In particular, the cycles are **not repelling periodic points in the two-dimensional all-directions sense**, because a one-dimensional family of nearby states is mapped exactly onto the cycle. Along the specified cycling trajectories the primal iterates nevertheless converge Q-linearly to the minimizer.

Put \(z_k=\lambda\gamma_k\). Let \(r_2>1\) be the unique root of \(r_2^3-r_2-1=0\) and set
\[
a_2=\frac{1+\sqrt{1+r_2^2}}{2r_2},\qquad b_2=r_2a_2.
\]
Initial normalized steps \((z_{-1},z_0)=(a_2,b_2)\) generate \(b_2,a_2,b_2,a_2,\ldots\), where \((a_2,b_2)\approx(1.003905171,1.329891208)\).

Let \(r_3>1\) be the unique solution of
\[
r_3^2(r_3-1)^2(r_3+1)^3=1,
\]
and define
\[
R=r_3\sqrt{1+r_3},\quad a_3=\frac{1+\sqrt{1+R^2}}{2R},\quad b_3=r_3a_3,\quad c_3=Ra_3.
\]
Initial \((z_{-1},z_0)=(a_3,b_3)\) generate \(b_3,c_3,a_3,b_3,c_3,a_3,\ldots\), with \((a_3,b_3,c_3)\approx(0.837216388,1.038488487,1.554408202)\). Uniqueness is asserted only within these positive, ordered branch itineraries and ratios; no complete periodic-orbit classification is claimed.

## Setting and exact scalar map

Use the unmodified 2023 adaPGM Algorithm 2.1, **not** the different later parametrized algorithm. Take \(x^{-1}=1\), the indicated \(\gamma_{-1},\gamma_0\), and \(x^0=(1-\lambda\gamma_0)x^{-1}\). Both initializations obey \(\gamma_0\ge\gamma_{-1}>0\). Because a scalar quadratic has \(\ell_k=c_k=\lambda\) for distinct iterates, and none of the cycle steps equals one, all quotients in the update are nondegenerate throughout. The normalized two-state map is
\[
T(u,v)=(v,\Phi(u,v)),\quad \Phi(u,v)=\min\{G(u,v),F(v)\},\quad G(u,v)=v\sqrt{1+v/u},
\]
\[
F(v)=\begin{cases}\frac12\sqrt{\frac{v}{v-1}},&v>1,\\+\infty,&0<v\le1.\end{cases}
\]
The primal update is \(x^{k+1}=(1-z_{k+1})x^k\). All algebra is exact over the reals.

## Proof of the cycles

**Prime two.** Consider one strict growth step \((b,a)\mapsto(a,b)\) followed by one strict cap step \((a,b)\mapsto(b,a)\), with \(b>a>0\) and \(r=b/a>1\). The growth equality \(G(b,a)=b\) is equivalent to \(r^3-r-1=0\), which has one root \(r_2>1\). The cap equality \(F(b)=a\) gives \(4ra^2-4a-r=0\), with unique positive solution \(a_2\). Direct inequalities certify \(1<a_2<b_2\), \(G(b_2,a_2)=b_2<F(a_2)\), and \(F(b_2)=a_2<G(a_2,b_2)\). Thus both selected branches are strict and the two distinct states form a prime-two orbit.

**Prime three.** Prescribe \(a<b<c\) and branch itinerary growth at \((c,a)\), growth at \((a,b)\), cap at \((b,c)\). Write \(r=b/a\) and \(s=c/b\). The two growth equalities require
\[
r^2=1+\frac1{rs},\qquad s^2=1+r.
\]
Eliminating \(s\) gives \(r(r^2-1)\sqrt{1+r}=1\), which is strictly increasing from zero to infinity on \((1,\infty)\). Its unique solution is \(r_3\); squaring yields exactly the displayed seventh-degree equation, with no spurious root for \(r>1\). With \(R=rs\), the cap condition \(F(c)=a\) is \(4Ra^2-4a-R=0\), giving the stated \(a_3\). Exact interval inequalities establish \(0<a_3<1<b_3<c_3\), \(F(a_3)=\infty>G(c_3,a_3)=b_3\), \(F(b_3)>G(a_3,b_3)=c_3\), and \(G(b_3,c_3)>F(c_3)=a_3\). All three branches are strict. The distinct states form a prime-three orbit, and the initial step constraint is satisfied.

## Local return dynamics: unstable, but not repelling in all directions

The exact state-map Jacobian on a strict growth branch, with \(q=v/u\) and \(s=\sqrt{1+q}\), is
\[
DT_G(u,v)=\begin{pmatrix}0&1\\-q^2/(2s)&(2+3q)/(2s)\end{pmatrix}.
\]
On a strict cap branch,
\[
DT_F(u,v)=\begin{pmatrix}0&1\\0&-F(v)/(2v(v-1))\end{pmatrix}.
\]
The return Jacobian contains one cap factor, hence has rank at most one and determinant zero. For the prime-two orbit beginning at \((b_2,a_2)\), the ordered product is \(J_2=DT_F(a_2,b_2)DT_G(b_2,a_2)\). For the prime-three orbit beginning at \((c_3,a_3)\), the product is \(J_3=DT_F(b_3,c_3)DT_G(a_3,b_3)DT_G(c_3,a_3)\). Exact rational interval evaluations using the companion verifier bound their nonzero multipliers by
\[
-2.057<\operatorname{tr}J_2<-2.056,\qquad -1.327<\operatorname{tr}J_3<-1.326.
\]
The other multiplier is exactly zero in each case. Thus each cycle has a locally expanding direction and is Lyapunov unstable, but it is not a repeller with expansion in every nearby direction.

The distinction is constructive. For the prime-two cycle take any \(v\) sufficiently close to \(a_2\) and set
\[
u(v)=\frac{v}{(b_2/v)^2-1}.
\]
Then \(u(v)>0\), \(u(a_2)=b_2\), and \(G(u(v),v)=b_2\). Strict branch inequalities persist by continuity, so \(T(u(v),v)=(v,b_2)\) and \(T^2(u(v),v)=(b_2,a_2)\) for every sufficiently close \(v\), since the second update selects the cap \(F(b_2)=a_2\). Accordingly, arbitrarily close states off the periodic orbit enter it exactly after two steps. An analogous stable transverse direction follows from the rank-one return map for the prime-three cycle. Hence the original stronger description 'locally repelling' is not valid when interpreted as an all-directions two-dimensional repeller; **saddle-type local instability** is the precise claim.

## Primal convergence

For the two-cycle the primal multiplier over a period is \((1-a_2)(1-b_2)\in(0,1)\). For the three-cycle it is \((1-a_3)(1-b_3)(1-c_3)\in(0,1)\). Every individual normalized cycle step lies in \((0,2)\), so the corresponding primal iterates converge Q-linearly to the unique minimizer, although the stepsizes do not converge. This conclusion holds for the precisely initialized cycles, not arbitrary stepsize states.

## Verification and prior work

The accompanying `verify_cycles.py` provides exact rational interval isolation of the algebraic roots, strict branch comparisons, nonzero return multipliers and primal contraction bounds. Independent direct state-map substitution confirms the two cycles and the explicit two-step stable-preimage curve. Finite numerical traces are not the proof of infinite recurrence: the algebraic equalities and strict branch inequalities are.

Latafat, Themelis, Stella and Patrinos introduce the original 2023 update and observe apparently cyclic stepsizes without establishing these exact cycles. The later Latafat–Themelis–Patrinos 2024 parameterized rule has a different curvature-cap coefficient. A published plastic-constant two-cycle for the Bregman-adaptive B-adaPGα update has yet another cap and distinct cycle values; it does not imply this original-rule prime-three cycle. The novelty assessed is existence of two exact prime periods for the original map, the explicit algebraic construction, and their saddle-type return spectra despite convergent primal variables. Priority over unindexed specializations is not asserted.

The result is restricted to one-dimensional quadratics, selected valid initial steps and the stated itineraries. It neither gives a census of all periodic orbits nor typical attraction/repulsion dynamics across general objectives. A zero return multiplier and an expanding one are consistent with coexistence of strongly stable and unstable local directions.

### Sources

1. P. Latafat, A. Themelis, L. Stella, P. Patrinos, *Adaptive proximal algorithms for convex optimization under local Lipschitz continuity of the gradient*, arXiv:2301.04431, Algorithm 2.1 and Section 4.3, https://arxiv.org/abs/2301.04431.
2. P. Latafat, A. Themelis, P. Patrinos, *On the convergence of adaptive first order methods: Proximal gradient and alternating minimization algorithms*, PMLR 242 (2024), 197–208, https://proceedings.mlr.press/v242/latafat24a/latafat24a.pdf.
3. H. Ou, P. Latafat, A. Themelis, *Linesearch-free adaptive Bregman proximal gradient for convex minimization under local relative smoothness*, arXiv:2508.01353.
