# A sharp two-cluster escape and locking phase diagram for biased Gaussian opinions

## Finding

For the zero-diffusion, full-line biased-Gaussian opinion-transport equation of Koertje and Sayama, a population concentrated in two groups has an **exact and complete global gap phase diagram**. The result differentiates irreversible merging, a translating finite-distance locked pair, and permanent separation. Which type occurs is controlled by the *orientation* of the larger group, the bias strength, and the initial separation. A universal saddle-node in the Gaussian interaction geometry separates the merger-only and stable-locking regimes when the larger group is on the left. When the larger group is on the right, one unstable gap instead separates merger from runaway separation.

The sharp geometric constants are
\[
 d_*=0.9077392338410746\ldots,\qquad R_*=0.29218254980097287\ldots,\qquad d_0=1.5557286306696719\ldots.
\]
Write \(\delta=2p-1\) for the excess mass of the **left** group. For every \(\delta>0\), the stable-separation branch first appears at the sharp bias
\[
 b_{\mathrm{lock}}(\delta)=\frac{2}{1+\delta R_*}.
\]
For \(b_{\mathrm{lock}}(\delta)<b<2\), the only two positive stationary gaps satisfy \(0<d_-<d_*<d_+<d_0\), with the smaller gap separating merging from the attracting locked gap. At criticality they meet in a saddle-node, and for \(b\downarrow b_{\mathrm{lock}}\) from above,
\[
 d_{\pm}(b)=d_*\pm\sqrt{\frac{-4}{\delta b_{\mathrm{lock}}^2 R''(d_*)}}\sqrt{b-b_{\mathrm{lock}}}+O(b-b_{\mathrm{lock}}).
\]
For \(\delta<0\) and \(b>0\), there is instead exactly one unstable positive gap \(d_{\mathrm{esc}}\): starting above it leads to asymptotically linear separation at exact speed \(cb|\delta|/e\).

## Assumptions and scope

Consider the probability measure \(P(t)\) on the entire real opinion axis solving the zero-diffusion conservation law weakly,
\[
 \partial_t P+\partial_x(Pv_P)=0,\quad
 v_P(x)=c\int_{\mathbb R}g_b(y-x)\,P(dy),\quad
 g_b(z)=e^{-(z-1)^2}+(b-1)e^{-(z+1)^2}.
\]
The mass is normalized to one, \(c>0\), and \(0\le b\le2\). Initially
\[
 P(0)=p\delta_{x_-(0)}+q\delta_{x_+(0)},\quad
 0<p<1,\quad q=1-p,\quad x_-(0)<x_+(0).
\]
These are two *opinion-group masses*, not two species with distinct interaction laws. The convolution **includes self-interaction** as in the source equation. Write \(d(t)=x_+(t)-x_-(t)>0\), \(\delta=p-q\) and \(m(t)=p x_-(t)+q x_+(t)\). No boundary reflections, positive diffusion, population births or interactions with omitted groups are included. The smooth bounded kernel is globally Lipschitz, so the characteristic flow yields the unique global two-atom weak solution; the two atoms cannot meet at finite time.

Define for \(d>0\)
\[
 h(d)=e^{-d^2}\cosh(2d),\quad j(d)=e^{-d^2}\sinh(2d),\quad
 R(d)=\frac{h(d)-1}{j(d)}
 =\frac{\cosh(2d)-e^{d^2}}{\sinh(2d)}.
\]
Let \(d_*\) be the unique positive solution of
\[
 e^{d_*^2}(\cosh(2d_*)-d_*\sinh(2d_*))=1
\]
with \(d_*>1/\sqrt2\). Let \(R_*=R(d_*)>0\) and let \(d_0>d_*\) be the unique positive root of \(\cosh(2d_0)=e^{d_0^2}\).

**Exhaustive classification for every initial gap \(d(0)>0\).**

1. \(b=0\), any \(\delta\): the gap strictly decreases to zero. The weighted barycenter is stationary.
2. \(0<b<2\), \(\delta=0\): the gap strictly decreases to zero.
3. \(0<b\le2\), \(\delta<0\): there is exactly one positive root \(d_{\mathrm{esc}}\) of \(R(d)=-(2-b)/(|\delta|b)\) (for \(b=2\), it is \(d_0\)). Gaps below it shrink to zero; at it they stay constant and translate; gaps above it diverge to infinity, satisfying \(d(t)/t\to cb|\delta|/e\).
4. \(0<b<2\), \(\delta>0\), \(b<b_{\mathrm{lock}}(\delta)\): every positive gap shrinks to zero.
5. \(0<b<2\), \(\delta>0\), \(b=b_{\mathrm{lock}}(\delta)\): the gap \(d_*\) is semistable. Initial gaps below \(d_*\) shrink to zero; the gap \(d_*\) remains fixed; initial gaps above \(d_*\) decrease to \(d_*\).
6. \(0<b<2\), \(\delta>0\), \(b>b_{\mathrm{lock}}(\delta)\): there are exactly two positive roots \(d_-<d_+\). Initial gaps below \(d_-\) shrink to zero; \(d_-\) remains fixed; every initial gap above \(d_-\) converges to \(d_+\). Thus \(d_-\) is repelling and \(d_+\) attracting.
7. \(b=2\), \(\delta>0\): every positive gap converges to the unique attracting positive separation \(d_0\). For \(b=2\), \(\delta=0\), every positive gap remains exactly constant.

A constant positive gap means two *traveling* point masses, not a stationary opinion distribution. For all cases the weighted barycenter satisfies the strictly positive speed identity when \(b>0\):
\[
 \dot m=\frac{cb}{e}\big[p^2+q^2+2pq\,h(d)\big]>0.
\]
If \(d(t)\to0\) and \(b<2\), then \(\lim_{t\to\infty}\log d(t)/t=-2c(2-b)/e\). In the borderline merging case \(b=2\), \(\delta<0\), \(d(t)\sim e/(2c|\delta|t)\). The statements also hold at \(c\ne1\) by rescaling time, and at any common translation of the initial opinions.

## Proof

**Exact reduction and well-posedness.** Substitution of the atomic measure into the weak equation gives the characteristic velocities
\[
 \dot x_-=c[p g_b(0)+q g_b(d)],\qquad
 \dot x_+=c[p g_b(-d)+q g_b(0)].
\]
The kernel and its first derivative are bounded, so the velocities are Lipschitz in the two coordinates. A unique global solution exists. Its gap obeys a scalar Lipschitz equation with the fixed solution \(d=0\), hence a strictly positive initial gap cannot reach zero in finite time. Using \(g_b(0)=b/e\) and Gaussian addition identities gives the *exact*, not asymptotic, equations
\[
 \dot d=\frac{c}{e}\left[\delta b(h(d)-1)-(2-b)j(d)\right]
       =\frac{c}{e}j(d)\left[\delta b R(d)-(2-b)\right],
\]
\[
 \dot m=\frac{cb}{e}\left[p^2+q^2+2pq h(d)\right].
\]
Since \(j(d)>0\) for positive \(d\), the bracket determines the entire phase portrait.

**A unique shape maximum.** Direct differentiation yields
\[
 R'(d)=\frac{2(F(d)-1)}{\sinh^2(2d)},\quad
 F(d)=e^{d^2}(\cosh(2d)-d\sinh(2d)),
\]
\[
 F'(d)=e^{d^2}(1-2d^2)\sinh(2d).
\]
The function \(F\) starts at \(F(0)=1\), rises strictly until \(d=1/\sqrt2\), and then decreases strictly to negative infinity. Therefore it crosses level one exactly once more, at \(d_*>1/\sqrt2\). Hence \(R\) is strictly increasing from \(R(0+)=0\) to \(R_*\), and strictly decreasing afterward, with \(R(d)\to-\infty\). Its unique positive zero \(d_0\) lies beyond \(d_*\). At its maximum,
\[
 R''(d_*)=\frac{2e^{d_*^2}(1-2d_*^2)}{\sinh(2d_*)}<0.
\]
This fully characterizes all possible crossings of each horizontal level.

**Sign and convergence.** If \(\delta=0\) and \(b<2\), or \(b=0\), the bracket is strictly negative. If \(\delta<0\) and \(b>0\), it is negative below the unique negative-level intersection of \(R\), and positive above. If \(\delta>0\), it is strictly negative everywhere when \((2-b)/(\delta b)>R_*\); zero once at equality; and changes signs negative–positive–negative across the two roots if \(0<(2-b)/(\delta b)<R_*\). At \(b=2\), the bracket is \(2\delta R(d)\), whose signs are read from the unique zero \(d_0\). These are precisely the stated cases. Standard uniqueness of one-dimensional autonomous flows gives the asserted limits: bounded monotone solutions converge to equilibria, and in the escape regime the sign cannot reverse and the only possible unbounded limit is infinity. Since \(h(d),j(d)\to0\) as \(d\to\infty\), the escaping gap derivative tends to \(cb|\delta|/e\), proving the exact asymptotic speed by time averaging.

**Onset exponent and rates.** For \(\delta>0\), the double-root condition is \(\delta b R_*=2-b\), hence \(b_{\mathrm{lock}}\). Taylor expansion of \(\delta bR(d)-(2-b)\) at \((d_*,b_{\mathrm{lock}})\) has positive bias derivative \(\delta R_*+1=2/b_{\mathrm{lock}}\) and negative second gap derivative \(\delta b_{\mathrm{lock}}R''(d_*)\). Solving its nondegenerate quadratic fold gives the displayed square-root law and remainder. Finally \(h(d)-1=d^2+O(d^4)\), \(j(d)=2d+O(d^3)\) near zero. Therefore for \(b<2\) a merging gap has \(\dot d/d\to-2c(2-b)/e\); at \(b=2,\delta<0\), \(\dot d/d^2\to-2c|\delta|/e\), which integrates to the stated reciprocal-time law. No appeal to a finite simulation is used for global claims.

## Verification

Run `python verify_two_cluster.py` with Python, SymPy, mpmath and SciPy. The executable independently reconstructs each atom's original convolution velocity and the derived gap/barycenter identities; symbolically checks the two shape derivatives; numerically isolates the critical constants and representative roots; checks the saddle-node square-root coefficient at two scales; integrates the **original two-coordinate** characteristic system for representative merger, finite-locking, frozen and escape cases. These finite tests are reproducibility aids, not proofs of uniqueness, global convergence, or original publication priority. The proof above independently establishes those assertions.

For example, with left mass \(p=3/4\), bias \(b=1.95\), the sharp fold is \(b_{\mathrm{lock}}\approx1.7450617100053024\) and the two gap roots are \(d_-\approx0.1031108146372065\), \(d_+\approx1.5068315350334762\). Reversing the mass orientation to \(p=1/4\) at the same bias instead produces a single escape threshold \(d_{\mathrm{esc}}\approx1.5986399073041026\).

## Relationship to prior work

Koertje and Sayama introduced this **exact kernel** and PDE (arXiv:2310.01564v1, posted 2023-10-02; later *Physical Review E* 109, 034304, 2024). They studied linear instability, diffusive numerical group drift, periodic or wall boundaries, and the possibility of more massive groups outrunning smaller groups on an infinite line. In particular their discussion explicitly raises the untested possibility that some smaller groups may be left behind. Their homogeneous-state critical bias \(2-2D_P/c\) is a *different* criterion, not the atomic two-group fold derived here. This result specializes to zero diffusion and atomic data, and provides sharp initial-gap criteria, globally attracting finite-distance motion, escaping speeds, and a mass-dependent saddle-node—not those pre-existing effects.

Sayama's earlier 2020 nonlocal opinion kernel model (*Physical Review E* 102, 012303; arXiv:2002.01049) investigates the role of information range on polarization and does not use the asymmetric biased-Gaussian kernel in the present theorem. Generic characteristics for aggregation equations imply that atom-supported solutions can be reduced to ODEs, but do not by themselves supply the explicit Gaussian shape-root and orientation-sensitive classification. The exact complete phase portrait and its threshold, rather than the elementary reduction alone, is the claim assessed here.

## Limitations

The theorem is restricted to precisely two atomic clusters, a normalized common kernel, the full real line, and *zero diffusion*. It makes no claim for three or more groups, smooth density profiles, finite-width clusters, finite domains, wall conditions, or positive diffusion; in particular a zero-diffusion locked pair need not survive diffusion. Source-paper simulations use positive diffusion in several regimes, so numerical behavior in those regimes is not implied by this theorem. The 2023 thesis cited by the motivating article was not available for full-text comparison; priority over unindexed specialist results is not independently established. Numerical digits and example trajectories are secondary checks, not global proof certificates.

## References

- Christian Koertje and Hiroki Sayama, *Collective group drift in a PDE-based opinion dynamics model with biased perception kernels*, arXiv:2310.01564v1, first publicly posted 2023-10-02, https://arxiv.org/abs/2310.01564. Journal version: *Physical Review E* **109** (2024), 034304, https://doi.org/10.1103/PhysRevE.109.034304. Full arXiv HTML version https://arxiv.org/html/2310.01564v3; specifically Eqs. (1), (4), §§III–IV and appendices.
- Hiroki Sayama, *Enhanced ability of information gathering may intensify disagreement among groups*, arXiv:2002.01049 (2020), https://arxiv.org/abs/2002.01049; *Physical Review E* **102** (2020), 012303, https://doi.org/10.1103/PhysRevE.102.012303.
- Christian Koertje, *Modeling Continuous Opinion Dynamics with Biased Interactions*, master's thesis, Binghamton University (2023), cited in the first reference; full text not verified in this review.
