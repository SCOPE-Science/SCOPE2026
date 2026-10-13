# Convex-order rigidity of the covariance crossover in one-dimensional Poisson coverage

## Finding
Let a stationary marked Poisson process on the real line have germ intensity \(\lambda>0\), with independent identically distributed grain lengths \(L>0\) satisfying \(\mu=\mathbb E L\in(0,\infty)\) and \(\mathbb E L^2<\infty\). Every germ at \(x\) covers the interval \([x,x+L]\). For \(T>0\), let \(C_T\) count occupied-component *left endpoints* in \([0,T]\), and let \(V_T\) be the occupied Lebesgue length of \([0,T]\).

Define the stop-loss transform \(h(t)=\mathbb E(L-t)_+\) for \(t\ge0\). Then the mixed asymptotic covariance density exists and equals
\[
\kappa_L(\lambda):=\lim_{T\to\infty}\frac{\operatorname{Cov}(C_T,V_T)}{T}
=e^{-2\lambda\mu}\left[e^{\lambda\mu}-1-2\lambda\int_0^\infty\left(e^{\lambda h(t)}-1\right)\,dt\right].
\]
There is precisely one \(\lambda_L\in(0,\infty)\) at which this density vanishes; it is positive for \(0<\lambda<\lambda_L\) and negative for \(\lambda>\lambda_L\). Let \(c_*>0\) be the unique positive solution of \(e^{c_*}=1+2c_*\), numerically \(c_*=1.256431208626\ldots\). The sharp fixed-mean upper bound is
\[
0<\lambda_L\le\frac{c_*}{\mu},
\]
with equality exactly when \(L\) is deterministic. In addition,
\[
\lambda_L\le \frac{\mu}{\mathbb E L^2-\mu^2/2}.
\]
If \(L_1\le_{\mathrm{cx}}L_2\) in convex order with the same finite positive mean and finite second moments, then \(\kappa_{L_1}(\lambda)\ge\kappa_{L_2}(\lambda)\) for every \(\lambda>0\), and \(\lambda_{L_1}\ge\lambda_{L_2}\); both inequalities are strict if the distributions differ. At fixed mean, critical intensities have infimum zero over positive grain-length laws with finite second moment, but zero is never attained.

## Assumptions and scope
All quantities are defined on the complete stationary Poisson Boolean model on \(\mathbb R\), rather than on a process started at a finite boundary. A component left endpoint is a germ at which previously arriving intervals do not provide coverage. Almost surely there are no endpoint coincidences. The count \(C_T\) differs from the usual Euler characteristic of the clipped random closed set by the indicator that the left boundary is covered. The latter indicator has covariance with \(V_T\) bounded in absolute value by \(e^{-2\lambda\mu}\int_0^\infty(e^{\lambda h(t)}-1)\,dt<\infty\), so the corresponding mixed covariance densities agree. The result concerns the large-window covariance density and **does not assert** a unique sign transition for every finite-window covariance. The convex-order comparison requires equal means and convex-order comparability, not just a variance comparison.

## Proof
Write \(S(t)=\Pr(L>t)\), \(h(t)=\int_t^\infty S(u)\,du\), and \(p=1-e^{-\lambda\mu}\). A fixed location is unoccupied with probability \(e^{-\lambda\mu}\). By the marked Mecke formula, a germ at the origin begins an occupied component with probability \(e^{-\lambda\mu}\), independently of its own length. Conditional on this event and on insertion of the germ, the unoccupied probability at displacement \(s<0\) is
\[
\exp\{-\lambda[\mu-h(|s|)]\},
\]
and at \(s\ge0\) it is
\[
[1-S(s)]\exp\{-\lambda[\mu-h(s)]\}.
\]
Indeed, no earlier germ covers the origin; the Poisson measure of grains covering the target location but not the origin is \(\lambda[\mu-h(|s|)]\). For positive displacement the inserted grain itself must additionally fail to cover the target, which has probability \(1-S(s)\).

Subtracting the unconditional occupied probability \(p\), let \(k(s)\) denote the resulting difference of conditional and unconditional occupied probabilities. A second use of Mecke and Fubini gives the **exact finite-window identity**
\[
\operatorname{Cov}(C_T,V_T)
=\lambda e^{-\lambda\mu}\int_{-T}^{T}(T-|s|)k(s)\,ds.
\]
The kernel is integrable: for \(s>0\), the absolute values of its two half-line contributions are bounded by constants depending on \(\lambda,\mu\) times \(S(s)+h(s)\), and \(\int_0^\infty h(s)\,ds=\mathbb E L^2/2<\infty\). Dominated convergence therefore gives the covariance density. Pairing \(k(s)\) and \(k(-s)\), and integrating \(S(s)e^{\lambda h(s)}\) via \(h'(s)=-S(s)\), yields
\[
\int_0^\infty S(s)e^{\lambda h(s)}\,ds
=\frac{e^{\lambda\mu}-1}{\lambda},
\]
which proves the displayed expression for \(\kappa_L\).

Set \(H_L(\lambda)=e^{2\lambda\mu}\kappa_L(\lambda)\). By Tonelli and the second-moment assumption, its entire power series on the positive real axis is
\[
H_L(\lambda)=\mu\lambda+
\sum_{m=2}^\infty \lambda^m
\left[\frac{\mu^m}{m!}-\frac{2}{(m-1)!}\int_0^\infty h(t)^{m-1}\,dt\right].
\]
The convexity of the positive-part function gives \(h(t)\ge(\mu-t)_+\). Consequently
\[
\int_0^\infty h(t)^{m-1}\,dt\ge\frac{\mu^m}{m}
\qquad(m\ge2),
\]
so **every coefficient after the linear term is strictly negative**. Hence \(H_L(\lambda)/\lambda\) strictly decreases from \(\mu\) at zero. It is bounded above by \((2\lambda\mu+1-e^{\lambda\mu})/\lambda\), which tends to negative infinity. There is therefore exactly one positive zero, with the asserted sign orientation.

The same inequality yields \(H_L(\lambda)\le2\lambda\mu+1-e^{\lambda\mu}\), whose positive zero occurs at \(c_*/\mu\). Equality at a positive intensity forces \(h(t)=(\mu-t)_+\) almost everywhere, which is equivalent to deterministic \(L=\mu\). The quadratic coefficient is \(\mu^2/2-\mathbb E L^2\), producing the stated second-moment upper bound.

Finally, if \(L_1\le_{\mathrm{cx}}L_2\), the stop-loss characterization says \(h_1(t)\le h_2(t)\) at all \(t\ge0\). Substitution in the covariance formula gives pointwise ordering of the full density curves and, by their unique crossovers, reverse ordering of their zeros. If the laws are distinct, their stop-loss functions differ on a set of positive measure, giving strict inequalities. To see that there is no positive uniform lower bound at fixed mean, take two positive grain lengths \(a_p=p\mu\) and \(b_p=[\mu-(1-p)a_p]/p\), with respective probabilities \(1-p\) and \(p\), and let \(p\downarrow0\). Their second moments diverge and the second-moment bound forces \(\lambda_{L_p}\to0\).

## Verification
The reproducible standard-library script `verify_boolean.py` tests the Poisson-conditioning kernel against an independent piecewise integration for discrete grain laws, the deterministic-grain closed formula, negative higher Taylor coefficients, sign bracketing, and representative convex-order chains. It completed 322 numerical and algebraic consistency checks. For mean-one grain lengths, deterministic \(L=1\) gives \(\lambda_L\approx1.256431208626\), whereas equally weighted two-point laws supported at \((0.5,1.5)\), \((0.2,1.8)\), and \((0.05,1.95)\) give approximately \(0.988321061619\), \(0.704007224295\), and \(0.585010895765\), respectively. Numerical checks are not proofs of the universal results; the proof above supplies the infinite-volume and all-grain arguments.

## Relationship to prior work
General second-order formulas for intrinsic volumes of Poisson Boolean models are established by Hug, Last, and Schulte (2013 preprint; 2016 journal article), including asymptotic mixed Euler-characteristic/volume covariance in broad dimensions and grain distributions (notably their Corollary 6.2). Their general covariance machinery is **not** claimed to be new here. The result isolated here is instead the dimension-one **all-grain single-zero theorem**, the **entire-curve convex-order monotonicity**, and the **sharp deterministic upper boundary**. Heinrich and Molchanov's earlier germ–grain central limit theorem covers broader classes of random measures and supplies further probabilistic context. Related one-dimensional Poisson clump distributions have also been studied by Betancort-Rijo. The earlier general covariance formulas could make the present density identity implicit; the added sign and convex-order conclusions require the separate inequalities proved above.

## Limitations
No finite-window universal sign statement, multidimensional analogue, heavy-tailed infinite-second-moment extension, or exhaustive historical priority is claimed. The general covariance formula may also be recoverable from existing intrinsic-volume literature. The 1992 clump paper could not be fully inspected through accessible lawful sources, leaving some risk of prior implicit special-case coverage. The result has received the stated self-review but no independent scientific audit.

## References
1. D. Hug, G. Last, and M. Schulte, *Second-order properties and central limit theorems for geometric functionals of Boolean models*, arXiv:1308.6519v1, publicly submitted 2013-08-29; Annals of Applied Probability 26 (2016), 73–135. https://arxiv.org/abs/1308.6519
2. L. Heinrich and I. S. Molchanov, *Central limit theorem for a class of random measures associated with germ–grain models*, CWI Report BS-R9518 (1995); Advances in Applied Probability 31 (1999), 283–314. https://ir.cwi.nl/pub/4967/
3. J. Betancort-Rijo, *Clusters in one-dimensional Poissonian distributions of points: Exact approach*, Physical Review A 46 (1992), 4549–4559. https://doi.org/10.1103/PhysRevA.46.4549
