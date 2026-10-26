# Exact finite-identification resonances and optimal waiting time for Bernoulli ProxSkip on affine quadratics

## Finding

The original Bernoulli ProxSkip iteration, which skips expensive proximal calls at independent Bernoulli trials, exhibits an exact finite-identification dichotomy on affine-constrained isotropic quadratics. Let \(c=1-\gamma a\in(0,1)\) and \(0<p<1\). Starting immediately after a successful proximal call from a feasible point with nonzero normal control error, the primal variable becomes **permanently feasible** and the control variable becomes **exactly correct** in a finite number of further iterations almost surely **if and only if**
\[
 p=p_m(c):=\frac{1}{S_m(c)},\qquad S_m(c)=\sum_{j=0}^{m-1}c^j,\qquad m\in\{2,3,\ldots\}.
\]
The geometric inter-call gap length \(J=m\) then annihilates the normal control error. If \(H\) is the number of further iterations until the first such gap completes, set \(s=p(1-p)^{m-1}\). Its exact probability generating function and mean are
\[
 \mathbb E[w^H]=\frac{s w^m}{1-\frac{pw}{1-(1-p)w}+s w^m},\qquad
 \mathbb E[H]=\frac{1}{p^2(1-p)^{m-1}}.
\]
Among **all genuinely skipping resonant settings**, the unique global minimum is
\[
 \min \mathbb E[H]=\frac{27}{4},\qquad m=2,\quad c=\frac12,\quad p=\frac23.
\]
Off the resonance set, a feasible initial point with nonzero normal control error leaves the constraint infinitely often almost surely; ordinary asymptotic convergence is not contradicted.

## Assumptions and scope

Fix any finite dimension \(d\ge1\), a proper linear subspace \(T\subsetneq\mathbb R^d\), and its nonzero normal space \(N=T^\perp\). Let \(C=c_0+T\), where \(c_0\in N\), and let \(P_C\) and \(Q=P_N\) denote Euclidean affine and orthogonal projections. For arbitrary \(z\in\mathbb R^d\) and \(a>0\), minimize
\[
 f(x)+\iota_C(x),\qquad f(x)=\frac a2\|x-z\|^2.
\]
Its unique solution is \(x_\star=P_C z\); the control equilibrium \(h_\star=\nabla f(x_\star)=a(x_\star-z)\) lies in \(N\). Choose \(\gamma>0\) with \(0<\gamma a<1\), set \(c=1-\gamma a\), choose \(p\in(0,1)\), and initialize the control \(h_0\in N\). The independent success indicators satisfy \(\Pr(\theta_k=1)=p\).

Use exactly the ProxSkip update of Mishchenko et al., Algorithm 1:
\[
 \widehat x_{k+1}=x_k-\gamma(\nabla f(x_k)-h_k),\qquad
 x_{k+1}=\begin{cases}
 P_C(\widehat x_{k+1}-(\gamma/p)h_k),&\theta_k=1,\\
 \widehat x_{k+1},&\theta_k=0,
 \end{cases}\qquad
 h_{k+1}=h_k+\frac p\gamma(x_{k+1}-\widehat x_{k+1}).
\]
All statements are in exact arithmetic. For the waiting-time law, take the origin of time *immediately after any successful proximal update* at which the control error is nonzero. The result applies to every such post-success state, without requiring an originally feasible initialization. Starting from any \(x_0\) and \(h_0\in N\), resonance implies almost-sure finite identification after the first success and a subsequent matching gap; if control is already exact, identification is immediate after that success.

## Proof

**1. Invariant normal control and linear normal dynamics.** Put \(v_k=h_k-h_\star\in N\), \(r_k=Q(x_k-x_\star)\in N\), and \(t_k=P_T(x_k-x_\star)\in T\). Since the projection of a normal translation onto \(C\) is unchanged, \(P_C(y-(\gamma/p)h_k)=P_Cy\). Consequently \(h_k\in N\) at all times and
\[
 t_{k+1}=ct_k,\qquad \widehat r_{k+1}=cr_k+\gamma v_k.
\]
A skipped call sets \((r_{k+1},v_{k+1})=(cr_k+\gamma v_k,v_k)\), while a successful call sets
\[
 (r_{k+1},v_{k+1})=\left(0,\ v_k-\frac p\gamma(cr_k+\gamma v_k)\right).
\]
These statements follow directly from the displayed algorithm, without probabilistic approximations.

**2. Exact renewal multiplier.** Immediately after a successful call, \(r=0\). If the next successful call occurs on the \(j\)-th subsequent iteration, there are \(j-1\) failed calls. Its preceding normal trial iterate is \(\widehat r=\gamma S_j(c)v\), hence the new normal control error is exactly
\[
 v_{\mathrm{new}}=(1-p S_j(c))v_{\mathrm{old}},\qquad S_j(c)=\frac{1-c^j}{1-c}.
\]
Because \(S_j(c)\) strictly increases in \(j\), an exact zero multiplier occurs precisely when \(p=1/S_m(c)\) for one integer \(m\ge2\). The case \(m=1\) would require \(p=1\), excluded here. At resonance a gap of length \(m\) makes \(r=v=0\), an invariant absorbing normal state for all subsequent random choices. For a nonzero \(v\) at the initial post-success state, no other finite sequence can kill the error.

**3. Almost-sure dichotomy.** Consecutive inter-success lengths \(J_1,J_2,\ldots\) are independent with \(\Pr(J=j)=p(1-p)^{j-1}\). At resonance each block has independent probability \(s=p(1-p)^{m-1}>0\) of having length \(m\), so a first matching block occurs almost surely in finite time. Off resonance, every multiplier is nonzero, so the normal control error remains nonzero at every completed success. Infinitely many success-then-failure patterns occur almost surely, and each such failure moves the primal variable from \(C\) to normal displacement \(\gamma v\ne0\). Thus a feasible start with \(v_0\ne0\) violates the constraint infinitely many times almost surely.

**4. Exact waiting distribution.** Let \(H\) sum independent geometric gap lengths until the first one equal to \(m\), inclusive. The probability generating function follows from the first-block decomposition:
\[
 G(w)=s w^m+\left(\frac{pw}{1-(1-p)w}-s w^m\right)G(w),
\]
which rearranges to the formula in the Finding. The renewal equation for the mean is \(\mathbb E[H]=\mathbb E[J]+(1-s)\mathbb E[H]\), with \(\mathbb E[J]=1/p\); hence \(\mathbb E[H]=1/(ps)\). The number of successful proximal calls needed has geometric law with parameter \(s\) and mean \(1/s\).

**5. Global optimum across resonance orders.** For \(m=2\), the resonance relation gives \(p=1/(1+c)\), hence
\[
 \mathbb E[H]=\frac{(1+c)^3}{c}.
\]
Its derivative \((1+c)^2(2c-1)/c^2\) has a unique zero and strict global minimum at \(c=1/2\), giving \(p=2/3\) and \(27/4\). For every \(m\ge3\),
\[
 p^2(1-p)^{m-1}\le p^2(1-p)^2\le\frac1{16},
\]
so \(\mathbb E[H]\ge16>27/4\). This also proves uniqueness among all integer orders and admissible \(c,p\).

## Verification

The accompanying standalone `verify.py` uses only the Python standard library and exact rational arithmetic. It instantiates a three-dimensional affine constraint, performs actual ProxSkip iterates with prescribed inter-success lengths for four rational resonance pairs, checks that the control vanishes only at the matching gap, verifies the absorbing state under arbitrary further success/failure patterns, confirms nonresonant positive multipliers, and checks the stated optimum and higher-order bounds. Running `python verify.py` prints `VERIFY_OK 192`. These finite checks are consistency evidence; the proof above establishes the infinite-time and all-dimension statements.

## Relationship to prior work

Mishchenko, Malinovsky, Stich and Richtárik introduce the exact randomized ProxSkip iteration and prove geometric decay of a Lyapunov quantity for strongly convex smooth objectives (Algorithm 1 and Theorem 3.6, 2022). Their convergence rate does not determine whether a skipped-proximal process ever becomes *permanently* feasible in finitely many iterations, nor a discrete resonance set and its hitting-time law. Condat and Richtárik's RandProx-Skip reduces to ProxSkip in a specialization (Appendix A.1); its general convergence theory does not imply the exact affine-quadratic inter-success multiplier or its optimal waiting time. The finite manifold-identification results of Liang, Fadili and Peyré concern deterministic forward–backward methods with proximal processing at every step and therefore do not decide the behavior of skipped proximal steps with an evolving control variable. Other randomized projection absorption phenomena concern different transition maps. These comparisons concern mathematical implications, not merely matching terminology.

## Limitations

Finite identification here means permanently meeting the affine constraint and exactly identifying the *normal control*, not attaining the full minimizer at finite time unless the tangential initial error vanishes. The exact resonances form thin tuning curves and are fragile to parameter error and finite precision. Initial controls must lie in the normal subspace. The result makes no assertion about general nonsmooth penalties, non-isotropic or nonlinear objectives, noisy gradients, or nonindependent skip decisions. Its exact waiting-time optimum describes a deliberately tuned class of finite-absorption settings, not optimal general-purpose ProxSkip tuning or computational runtime. Previously undiscovered equivalent calculations remain possible.

## References

1. K. Mishchenko, G. Malinovsky, S. Stich, P. Richtárik, *ProxSkip: Yes! Local Gradient Steps Provably Lead to Communication Acceleration! Finally!*, arXiv:2202.09357v1 (first public 2022-02-18), Algorithm 1, Theorem 3.6 and Appendix B. https://arxiv.org/abs/2202.09357
2. L. Condat, P. Richtárik, *RandProx: Primal–Dual Optimization Algorithms with Randomized Proximal Updates*, arXiv:2207.12891, Appendix A.1 (full-text revision v3 examined). https://arxiv.org/abs/2207.12891
3. J. Liang, J. Fadili, G. Peyré, *Activity Identification and Local Linear Convergence of Forward–Backward-type Methods*, arXiv:1503.03703, SIAM Journal on Optimization 27 (2017). https://arxiv.org/abs/1503.03703
