# Temporal refresh stabilizes the three-person local-flip opinion model with an exact Lyapunov exponent

## Finding

Consider the three-person symmetric local-flip map of Toth and Galam, but redraw the two flip probabilities independently and uniformly from \([0,1]\) before every *global discussion round*. Both probabilities are shared by all discussion groups during that round. For every deterministic initial population fraction \(p_0\in[0,1]\), the resulting infinite-population random recursion converges almost surely to an exact tie:
\[
 p_t\longrightarrow \tfrac12.
\]
Writing \(z_t=2p_t-1\), the process has the sharp uniform second-moment contraction
\[
 \mathbb E[z_{t+1}^{2}\mid z_t]=
 \frac{9-6z_t^2+5z_t^4}{24}\,z_t^2
 \le \frac38z_t^2.
\]
The Markov process has exactly one invariant probability measure: the point mass at \(p=\tfrac12\). If \(p_0\ne\tfrac12\), the majority signs \(\operatorname{sgn}(p_t-\tfrac12)\), for all integer \(t\ge1\), are independent fair signs, although the majority margin tends to zero. Their exact almost-sure exponential decay exponent is
\[
 \lim_{t\to\infty}\frac1t\log |p_t-\tfrac12|
 =\log(\tfrac32)-\tfrac32.
\]
In particular, the almost-sure per-round contraction factor is \(\tfrac32 e^{-3/2}\approx0.33469524\), even though an independent uniform *frozen* pair of parameters gives a linearly repelling tie with probability \(1/9\).

## Assumptions and scope

At time \(t\), let \(p_t\) denote the infinite-population fraction holding opinion A. As in the original local-flip rule, randomly composed independent discussion groups of size three adopt the group majority, except that a group decision is reversed with probability \(a_t\) when the majority is two-to-one and with probability \(b_t\) when the majority is unanimous. Conditional on the round's common environment \((a_t,b_t)\), the macroscopic recursion is
\[
 p_{t+1}=F_{a_t,b_t}(p_t),\qquad
 F_{a,b}(p)=(1-b)p^3+3(1-a)p^2(1-p)
 +3ap(1-p)^2+b(1-p)^3.
\]
The pairs \((a_t,b_t)\) are independent across all integer times \(t\ge0\); within each pair the coordinates are independent uniform \([0,1]\) variables. The initial fraction \(p_0\) is deterministic, although the convergence statement also holds for initial random fractions independent of future environments. The parameter refresh concerns the shared macroscopic environment, **not** independent parameter draws for different groups in one round. We make no finite-population absorption claim.

## Proof

**1. Exact conditional map and reflection.** Put \(z=2p-1\) and \(x=z^2\). Expanding the cubic update yields
\[
 z_{t+1}=z_t C(x_t,a_t,b_t),\qquad
 C(x,a,b)=\tfrac12\{3-x-3(1-x)a-(3+x)b\},
 \quad x_t=z_t^2.
\]
Equivalently,
\[
 C(x,a,b)=-\frac{3(1-x)}2(a-\tfrac12)
             -\frac{3+x}2(b-\tfrac12).
\]
Thus \(C(x,1-a,1-b)=-C(x,a,b)\). The joint uniform law is invariant under this reflection; hence, conditional on the entire past and whenever \(z_t\ne0\), the sign of \(z_{t+1}\) is a fair coin. The continuous conditional law has no atom at zero because the coefficient of \(b\) has absolute value at least \(3/2\). Therefore a nonzero initial imbalance remains nonzero at every finite time, almost surely. Sequential conditioning now proves that the signs at times \(1,2,\ldots\) are independent and identically distributed fair signs.

**2. Exact contraction and stationary law.** The conditional mean of \(C\) vanishes. The variance of an independent uniform \([0,1]\) coordinate equals \(1/12\), and so
\[
 \mathbb E[C(x,a,b)^2]
 =\frac{9(1-x)^2+(3+x)^2}{48}
 =\frac{9-6x+5x^2}{24}=:m(x).
\]
For \(0\le x\le1\), \(m(x)-3/8=x(5x-6)/24\le0\). The constant \(3/8\) is sharp as a uniform bound on the multiplier for nonzero states by taking \(x\downarrow0\). Consequently
\[
 \mathbb E[z_t^2]\le (3/8)^t z_0^2.
\]
For every \(\varepsilon>0\), Markov's inequality implies \(\sum_t\Pr(|z_t|>\varepsilon)<\infty\). Borel--Cantelli, applied to a countable sequence of \(\varepsilon\)'s, gives \(z_t\to0\) almost surely. If \(\mu\) is any invariant law, invariance and the same contraction imply
\(\int z^2\,d\mu\le(3/8)\int z^2\,d\mu\), hence \(\mu=\delta_0\) in the imbalance coordinate. The tie itself is fixed by every update.

**3. Exact pathwise exponent.** For \(x\in[0,1]\), define
\[
 h(x)=\mathbb E_{a,b}\log|C(x,a,b)|.
\]
These expectations are finite. Indeed, for fixed \(a,x\), the affine function of \(b\) has slope with magnitude \((3+x)/2\ge3/2\), and its values lie in \([-3/2,3/2]\). Integration with respect to \(b\) therefore gives a uniform upper bound on \(\mathbb E|\log|C(x,a,b)||^2\); the logarithmic singularity at zero is integrable. This uniform bound also makes \(h\) continuous on \([0,1]\), by truncation and dominated convergence.

For \(z_0\ne0\), the exact logarithmic recursion is
\[
 \log|z_n|=\log|z_0|+
 \sum_{t=0}^{n-1}\log|C(z_t^2,a_t,b_t)|.
\]
Subtracting the conditional means \(h(z_t^2)\) produces martingale differences of uniformly bounded second moments. The martingale strong law (apply convergence to their reciprocally weighted series and then Kronecker's lemma) gives their arithmetic average tending to zero almost surely. Since \(z_t\to0\), continuity of \(h\) and Cesaro averaging give
\(n^{-1}\log|z_n|\to h(0)\).

At \(x=0\), \(C(0,a,b)=\tfrac32(1-a-b)\). The random variable \(s=|1-a-b|\) has density \(2(1-s)\) on \([0,1]\), so
\[
 h(0)=\log(\tfrac32)+2\int_0^1(1-s)\log s\,ds
 =\log(\tfrac32)-\tfrac32.
\]
Finally, \(\log|p_n-\tfrac12|=\log|z_n|-\log2\), which has the same asymptotic exponent.

**4. Frozen-environment contrast.** For a constant pair \((a,b)\), the linearized multiplier at the tie is \(C(0,a,b)=\tfrac32(1-a-b)\). Its absolute value is greater than one exactly when \(a+b<1/3\) or \(a+b>5/3\). Those two corner triangles have total area \(2\cdot(1/3)^2/2=1/9\) under the uniform parameter law. This describes the frozen-parameter local instability, and is not asserted to be an instability of the independently refreshed process.

## Verification

Run `python verify_temporal_galam.py` with Python 3.9 or later. It uses only the standard library, reproduces 2,217 exact-rational tests of the cubic identity, coefficient reflection, positivity and conditional moment formulas, and performs a seeded 180,000-step numerical illustration of the logarithmic exponent and fair-sign frequencies. The finite numerical checks are *not* used in place of the analytic proof.

## Relationship to prior work

Toth and Galam (2021), Sections 4.1 and Appendix, define the three-person local-flip rule and classify fixed points and stability for **fixed** flip parameters. Toth (first public preprint 2022; published 2024), Section II.A, studies the distribution of these static fixed-point properties when the two parameters are sampled uniformly; its large-group theorems concern variation across randomly parameterized fixed models. Those results do not imply an almost-sure law for fresh common parameters at every round. Gimenez and coauthors (2023) consider a *different* time-varying contrarian mechanism driven by an oscillatory propaganda field and asynchronous four-person encounters; their setting neither specializes to the independent common two-parameter law here nor gives the displayed exponent. General results on random iterated maps motivate the Lyapunov approach, but do not supply this local-flip model's exact contraction factor, independent fair-majority-sign law, and pathwise rate without a model-specific calculation.

## Limitations

This is an exact theorem for the infinite-population shared-environment recursion with two independent uniform flip parameters renewed every round. It does not establish conclusions for finite noisy agent populations, individual-group-independent parameter draws, correlated parameter distributions, or arbitrary nonuniform time variation. A different law may break reflection symmetry and change both stability and majority-sign statistics. The literature comparison is evidence-based rather than a mathematical proof of novelty, and equivalent results in the broader random-iteration literature cannot be excluded completely. No external independent validation has been performed.

## References

1. G. Toth and S. Galam, *Deviations from the Majority: A Local Flip Model*, arXiv:2107.09344 (first public version 20 July 2021), https://arxiv.org/abs/2107.09344.
2. G. Toth, *Models of Opinion Dynamics with Random Parametrisation*, arXiv:2211.13601 (first public version 24 November 2022), https://arxiv.org/abs/2211.13601; *Journal of Mathematical Physics* 65, 073301 (2024), https://doi.org/10.1063/5.0159643.
3. M. C. Gimenez, L. Reinaudi, S. Galam and F. Vazquez, *Contrarian Majority Rule Model with External Oscillating Propaganda and Individual Inertias*, arXiv:2309.05765 (2023), https://arxiv.org/abs/2309.05765.
4. J. Yan et al., *Transition to anomalous dynamics in a simple random map*, arXiv:2308.09269 (2023), https://arxiv.org/abs/2308.09269.
