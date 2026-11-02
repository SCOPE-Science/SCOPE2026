# Sharp majority reversal and skewness correction for strongly mixing Allee patches

## Finding

Consider the deterministic cubic strong-Allee metapopulation on a complete, symmetrically mixed collection of \(n\ge2\) identical patches:
\[
\dot x_i=r x_i(x_i-\theta)(1-x_i)+\mu(\bar x-x_i),\qquad
\bar x=\frac1n\sum_{j=1}^n x_j.
\]
For every \(r>0\), \(\mu>r\), and initial vector \(a=(a_1,\ldots,a_n)\in[0,1]^n\) with \(0<q_0=n^{-1}\sum_i a_i<1\), there is exactly one critical \(\theta_c=\theta_c(\mu,r,a)\in(0,1)\). Every patch converges to capacity \(1\) if \(0<\theta<\theta_c\), every patch converges to extinction \(0\) if \(\theta_c<\theta<1\), and every patch converges to \(\theta_c\) if \(\theta=\theta_c\).

Define initial centered moments
\[
V_0=\frac1n\sum_i(a_i-q_0)^2,\qquad
T_0=\frac1n\sum_i(a_i-q_0)^3.
\]
For fixed \(n,r,a\) and \(\mu/r\to\infty\), the first finite-mixing correction to the mean-field threshold is
\[
\boxed{\theta_c=q_0+\frac r\mu\left(\frac{1-2q_0}{2}V_0-\frac13T_0\right)
       +O\!\left(\frac{r^2}{\mu^2}\right).}
\]
In particular, initial populations with identical mean and variance can have opposite first-order corrections because of their third centered moments.

If exactly \(m\in\{1,\ldots,n-1\}\) patches start at capacity and the rest start empty, put \(p=m/n\). Then **for every \(\mu>r\)**, not just asymptotically,
\[
\boxed{\theta_c>p\ \text{if }p<\tfrac12;\qquad
\theta_c=p\ \text{if }p=\tfrac12;\qquad
\theta_c<p\ \text{if }p>\tfrac12.}
\]
Moreover,
\[
\boxed{\theta_c=p+\frac r\mu\frac{p(1-p)(1-2p)}6
               +O\!\left(\frac{r^2}{\mu^2}\right).}
\]
For one initially occupied patch among three, \(\theta_c=1/3+r/(81\mu)+O(r^2/\mu^2)\). In the balanced two-patch case, the threshold is **exactly** \(1/2\) for every \(\mu>r\).

As a distributional illustration, the three-patch initial configurations \((9/10,2/5,1/5)\) and \((1/10,3/5,4/5)\) have the same mean \(1/2\) and variance \(13/150\), but opposite third centered moments \(3/250\) and \(-3/250\). Their critical thresholds are \(1/2-r/(250\mu)+O(r^2/\mu^2)\) and \(1/2+r/(250\mu)+O(r^2/\mu^2)\), respectively.

## Assumptions and scope

The system is continuous-time, deterministic, fully connected, and has uniform exchange toward the mean at rate \(\mu\). The local cubic response is identical across patches. This exchange normalization is important: the two-patch model with coupling \(c(x_j-x_i)\) corresponds here to \(\mu=2c\). All conclusions concern the invariant cube \([0,1]^n\), the stated initial vector, and \(\mu>r\). The strict majority sign law is claimed only for the specified binary initial vectors; the general-vector result is asymptotic and permits either sign. No uniform error bound in increasing \(n\) is asserted.

## Proof

**1. Invariance, mixing, and possible limits.** Let \(f_\theta(s)=r s(s-\theta)(1-s)\). At \(x_i=0\) the right side is nonnegative and at \(x_i=1\) it is nonpositive, so \([0,1]^n\) is invariant. The derivative \(f_\theta'(s)/r=-3s^2+2(1+\theta)s-\theta\) is linear in \(\theta\); its endpoint forms \(2s-3s^2\) and \(-3s^2+4s-1\) both range within \([-1,1/3]\) for \(s\in[0,1]\). Thus \(f_\theta\) is \(r\)-Lipschitz throughout the physical interval.

Put \(q=\bar x\), \(z_i=x_i-q\), \(V=n^{-1}\sum_i z_i^2\), and \(T=n^{-1}\sum_i z_i^3\). Centering the equations gives
\[
\dot V=\frac2n\sum_i z_i\bigl(f_\theta(x_i)-f_\theta(q)\bigr)-2\mu V
\le-2(\mu-r)V.
\]
Hence \(V(t)\le V_0e^{-2(\mu-r)t}\) and all patch differences vanish. Cubic expansion is **exact**:
\[
\dot q=f_\theta(q)+G(t),\qquad
G(t)=r\bigl[(1+\theta-3q)V-T\bigr].\tag{1}
\]
Since \(|z_i|\le1\), \(|T|\le V\), and \(|1+\theta-3q|\le2\), the forcing satisfies \(|G(t)|\le3rV_0e^{-2(\mu-r)t}\). To establish convergence without assuming it, let \(F'(q)=-f_\theta(q)\). Equation (1) gives \(dF(q(t))/dt=-f_\theta(q(t))^2-f_\theta(q(t))G(t)\). Boundedness and integrability of \(G\) imply \(\int_0^\infty f_\theta(q(t))^2dt<\infty\). Its integrand is uniformly continuous, so it tends to zero. The connected limit set of the scalar \(q(t)\) is therefore one point of \(\{0,\theta,1\}\); all \(x_i(t)\) share that limit.

**2. Unique critical threshold.** Increasing \(\theta\) strictly decreases \(f_\theta(s)\) at each \(s\in(0,1)\), while the off-diagonal derivatives of the full vector field equal \(\mu/n>0\). The cooperative comparison theorem therefore orders solutions for a common initial vector: if \(\theta_1<\theta_2\), then \(x_i(t;\theta_1)\ge x_i(t;\theta_2)\) for all \(i,t\ge0\). At \(\theta=0\) the positive post-mixing population grows to \(1\); at \(\theta=1\) it declines to \(0\). Hyperbolic stability of the uniform equilibria \(0\) and \(1\) makes these outcomes open in \(\theta\), yielding at least one parameter at which the limiting state is neither \(0\) nor \(1\), hence is \(\theta\). There cannot be two such parameters: the comparison would then force \(\theta_1\ge\theta_2\) for \(\theta_1<\theta_2\). Call the unique parameter \(\theta_c\). Comparison with its trajectory also forces convergence to \(1\) below it and to \(0\) above it.

**3. An exact threshold identity.** Factor \(f_\theta(q)=a(q)(q-\theta)\) with \(a(q)=r q(1-q)\ge0\). At the critical trajectory define \(A(t)=\int_0^t a(q(s))ds\). Differentiating \(e^{-A(t)}(q(t)-\theta_c)\) and using convergence \(q(t)\to\theta_c\) yields the exact improper-integral identity
\[
\theta_c-q_0=\int_0^\infty e^{-A(t)}G(t)\,dt.\tag{2}
\]
In particular \(|\theta_c-q_0|\le 3rV_0/[2(\mu-r)]\). Thus \(\theta_c=q_0+O(r/\mu)\) as \(\mu/r\to\infty\).

For the first correction set \(\tau=\mu t\) and \(\varepsilon=r/\mu\). The centered equations in fast time are \(dz_i/d\tau=-z_i+O(\varepsilon|z|)\); variation of constants and the exponential variance bound give \(z_i(\tau/\mu)=z_i(0)e^{-\tau}+O(\varepsilon\tau e^{-c\tau})\) for any fixed \(c<1\), uniformly in \(\tau\ge0\) once \(\varepsilon\) is sufficiently small. Also \(q(\tau/\mu)=q_0+O(\varepsilon\tau)\), \(\theta_c=q_0+O(\varepsilon)\), and \(e^{-A(\tau/\mu)}=1+O(\varepsilon\tau)\). Inserting these estimates into (2), with the exponentially decaying majorants controlling all tails, gives
\[
\theta_c-q_0=\frac r\mu\left[(1-2q_0)V_0
   \int_0^\infty e^{-2\tau}d\tau
   -T_0\int_0^\infty e^{-3\tau}d\tau\right]
   +O(\varepsilon^2).
\]
The two integrals are \(1/2\) and \(1/3\), proving the centered-moment formula with a genuine asymptotic error, not merely a formal expansion.

**4. Exact binary majority sign.** With a fraction \(p\) of patches initially at \(1\) and the remainder at \(0\), symmetry leaves just two trajectories \(u(t)\) and \(v(t)\), with \(u(0)=1\), \(v(0)=0\), and \(q=pu+(1-p)v\). Put \(w=u-v\). Uniqueness and invariance give \(0<w(t)<1\) for every \(t>0\). At the reference parameter \(\theta=p\), whenever \(q=p\), the exact average equation gives
\[
\dot q=r p(1-p)(1-2p)w^2(1-w).\tag{3}
\]
Initially \(q=p\), \(\dot q=0\), \(\dot w=-\mu\), and therefore \(\ddot q(0)=r\mu p(1-p)(1-2p)\). If \(p<1/2\), the mean immediately enters \(q>p\) and cannot cross back because the vector field on the boundary \(q=p\) points strictly upward. It cannot converge back to \(p\): for \(q>p\) sufficiently near \(p\) and \(w\) small, both \(f_p(q)\) and the right-hand correction \(G\) in (1) are positive, making \(q\) strictly increasing. Since \(w\to0\), the only remaining limit is \(1\). The transformation \((x_i,\theta)\mapsto(1-x_i,1-\theta)\) yields extinction for \(p>1/2\). At \(p=1/2=\theta\), the two-class identity \(f_{1/2}(u)+f_{1/2}(1-u)=0\) makes \(q\equiv1/2\) an invariant solution, and mixing forces all patches to that level. The unique-threshold classification from step 2 proves the three exact inequalities.

For binary data, the variance and third central moment are \(V_0=p(1-p)\), \(T_0=p(1-p)(1-2p)\). Substitution in step 3 gives the claimed coefficient. The three-patch example and the pair of equal-mean/equal-variance distributions follow by rational substitution.

## Verification

The accompanying `check.py` uses exact rational arithmetic to verify the cubic central-moment identity and the binary boundary-drift identity over thousands of rational inputs, and numerically integrates representative finite-rate trajectories. It verifies the \(1/81\) coefficient, the complementary initial-distribution examples, and the predicted direction of the critical shifts. Run `python3 check.py` with Python 3; the expected terminal line is `VERIFY_OK assertions=67180`. Numerical agreement does not replace the proof of uniqueness, exact sign, or asymptotic error bounds.

## Relationship to prior work

Kang and Lanchier (2010, arXiv:1003.0121v1) introduce precisely the cubic strong-Allee reaction and investigate deterministic two-patch dispersal and extinction/expansion basins. Their discussion explicitly motivates the initial occupied fraction as a high-dispersal guide to many-patch outcomes; their main deterministic theorems concern two patches and do not give the finite-mixing skewness correction, the all-\(n\) binary majority sign, or the unique all-initial-vector threshold proved here. For two patches, their pairwise coupling is related to the present mean coupling by a factor of two.

Lanchier (2013, arXiv:1301.0125v1) considers a stochastic interacting-patch process with mixing jumps and local threshold resets, not the cubic deterministic differential equation or its fast-mixing first correction. Gyllenberg, Hemminki, and Tammaru (1999) analyze a two-patch biparental-reproduction and competition model, so the inspected abstract does not establish the present finite-rate threshold classification. Related local two-patch equilibrium classifications do not imply the present initial-condition-dependent threshold asymptotics.

## Limitations

The theorem treats an idealized deterministic, identical-patch, complete-graph model, with \(\mu>r\) as a sufficient synchronization condition rather than a sharp necessity claim. No conclusion is drawn for slow mixing, environmental or demographic randomness, heterogeneous growth rates, or graph geometries other than uniform complete mixing. The computed coefficients are exact within the stipulated model but have not been fitted to empirical invasion data. Historical priority is provisional: older literature on fast-diffusion reduction or Allee front thresholds might encode a mathematically equivalent first correction; the 1999 two-patch paper was not available in full.

## References

1. Y. Kang and N. Lanchier, *Expansion or extinction: deterministic and stochastic two-patch models with Allee effects*, arXiv:1003.0121v1 (public abstract timestamp 2010-02-27). https://arxiv.org/abs/1003.0121 ; https://arxiv.org/pdf/1003.0121
2. N. Lanchier, *The role of dispersal in interacting patches subject to an Allee effect*, arXiv:1301.0125v1 (2013-01-01); *Advances in Applied Probability* 45 (2013), 1182–1197. https://arxiv.org/pdf/1301.0125
3. M. Gyllenberg, J. Hemminki, and T. Tammaru, *Allee effects can both conserve and create spatial heterogeneity in population densities*, *Theoretical Population Biology* 56 (1999), 231–242. https://doi.org/10.1006/tpbi.1999.1430
