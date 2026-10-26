# A functional limiting law for normalized reciprocal LCM powers

## Finding
For \(n\ge1\), put \(s(n)=\sigma(n)/n=\sum_{d\mid n}1/d\). For \(\kappa>1\), define the reciprocal LCM-power normalization
\[
Q_\kappa(n)=\left[\frac{n}{\kappa^{\omega(n)}}\sum_{d\mid n}\mu(d)s(n/d)^\kappa\right]^{1/(\kappa-1)}.
\]
There are canonical endpoint functions \(Q_1\) and \(Q_\infty=s\), defined explicitly below. Let \(N_X\) be uniformly distributed on \(\{1,\ldots,\lfloor X\rfloor\}\). On \(0\le t\le1\), put \(\kappa(t)=1/(1-t)\) when \(t<1\), and \(\kappa(1)=\infty\). Then the random continuous functions
\[
t\longmapsto\log Q_{\kappa(t)}(N_X)
\]
converge in distribution in the uniform-norm space \(C([0,1])\) to an explicitly defined continuous random Euler-product path. Every marginal of this path is non-atomic and has full topological support \([0,\infty)\) in logarithmic coordinates (equivalently \([1,\infty)\) before taking logarithms). The limiting paths are almost surely strictly increasing in the parameter. Every real marginal moment exists and is an absolutely convergent Euler product.

At the arithmetic-mean parameter \(\kappa=2\), the limiting first moment has the particularly simple exact value
\[
\lim_{X\to\infty}\frac1{\lfloor X\rfloor}\sum_{n\le X}Q_2(n)
=\prod_{p\text{ prime}}\left(1+\frac1{2p(p-1)}\right).
\]
This product is approximately \(1.42766\).

## Assumptions and scope
All primes are ordinary rational primes. For \(p\) prime and integer \(a\ge1\), put
\[
U_{p,a}=\sum_{j=0}^{a-1}p^{-j},\qquad W_{p,a}=U_{p,a}+p^{-a}.
\]
For \(1<\kappa<\infty\), define the strictly positive local factor
\[
q_\kappa(p^a)=\left(p^a\int_{U_{p,a}}^{W_{p,a}}u^{\kappa-1}\,du\right)^{1/(\kappa-1)}.
\]
Set
\[
q_1(p^a)=\exp\left(p^a\int_{U_{p,a}}^{W_{p,a}}\log u\,du\right),\qquad
q_\infty(p^a)=W_{p,a},\qquad q_\kappa(1)=1.
\]
Extend each \(Q_\kappa\) multiplicatively by \(Q_\kappa(n)=\prod_{p^a\parallel n}q_\kappa(p^a)\). For \(\kappa>1\), this agrees with the preceding normalization by the reciprocal-LCM convolution identity.

For each prime \(p\), let \(V_p\) be independent with
\[
\Pr(V_p=a)=(1-p^{-1})p^{-a}\quad(a=0,1,2,\ldots).
\]
The limiting path is
\[
Z(t)=\sum_p\log q_{\kappa(t)}(p^{V_p}),\qquad 0\le t\le1.
\]
All asserted convergence is unconditional. No claim is made that the marginal laws have Lebesgue densities, or that convergence has an effective rate.

## Proof
**Local identity and uniform estimate.** As \(W_{p,a}-U_{p,a}=p^{-a}\), the integral equals
\[
p^a\int_{U}^{W}u^{\kappa-1}du
=\frac{p^a}{\kappa}(W^\kappa-U^\kappa).
\]
The factor on the right is the normalized prime-power factor of the reciprocal LCM power. The generalized mean of a nonconstant positive interval is continuous and strictly increasing in its order. Consequently \(\kappa\mapsto q_\kappa(p^a)\) is continuous and strictly increasing on the compactified interval \([1,\infty]\). For every \(a\ge1\),
\[
1<q_1(p^a)\le q_\kappa(p^a)\le q_\infty(p^a)=W_{p,a}
\le (1-p^{-1})^{-1},
\]
so \(0<\log q_\kappa(p^a)\le2/p\), uniformly in \(a\ge1\) and \(1\le\kappa\le\infty\). Define the local logarithm to be zero at \(a=0\).

**Uniform random Euler-product convergence.** Because \(\Pr(V_p\ge1)=1/p\),
\[
\mathbb E\sum_p\sup_{1\le\kappa\le\infty}|\log q_\kappa(p^{V_p})|
\le2\sum_pp^{-2}<\infty.
\]
Thus the random series for \(Z\) converges almost surely uniformly in \(t\); its sample paths are continuous. For \(N_X\) uniform as above, the corresponding tail satisfies, uniformly in \(X\),
\[
\mathbb E\sup_t\sum_{p>P,\,p\mid N_X}\log q_{\kappa(t)}(p^{v_p(N_X)})
\le2\sum_{p>P}\frac1p\frac{\lfloor X/p\rfloor}{\lfloor X\rfloor}
\le2\sum_{p>P}p^{-2}.
\]
For any fixed finite set of primes, the joint valuations of \(N_X\) converge in law to independent \(V_p\); this follows by the Chinese remainder theorem after truncating valuation levels. The finite-prime logarithmic paths consequently converge in \(C([0,1])\). The displayed uniform tail estimate, applied also to the independent model, gives convergence of the full paths via bounded-Lipschitz test functions on \(C([0,1])\).

**Strict ordering and full support.** Every local generalized mean is strictly increasing in \(\kappa\) for \(a\ge1\). Since almost surely at least one (indeed infinitely many) \(V_p\) is nonzero, \(Z(t)\) is strictly increasing in \(t\) almost surely. For each fixed finite \(\kappa\), Taylor expansion of the local integral yields
\[
\log q_\kappa(p)=\frac1{2p}+O_\kappa(p^{-2});
\]
for \(\kappa=\infty\), \(\log q_\infty(p)=\log(1+p^{-1})=p^{-1}+O(p^{-2})\). Thus these positive local increments tend to zero but have a divergent prime sum. Finite subset sums are dense in \([0,\infty)\): start sufficiently far out that each increment is smaller than a prescribed tolerance, then take successive primes until the target is crossed. Prescribe the chosen prime valuations as one, all other valuations up to a finite cutoff as zero, and use the summable expected tail beyond the cutoff to retain positive probability within any tolerance. This proves that every neighborhood of every point of \([0,\infty)\) has positive \(Z(t)\)-probability. Conversely \(Z(t)\ge0\), proving exact support.

**Absence of atoms.** For any prime \(p\ge3\), construct \(V_p\) by taking independent \(A_p\sim\operatorname{Bernoulli}(2/p)\), \(B_p\sim\operatorname{Bernoulli}(1/2)\), and a positive integer \(W_p^*\) having \(\Pr(W_p^*=a)=(1-p^{-1})p^{-(a-1)}\) for \(a\ge1\), then setting \(V_p=A_pB_pW_p^*\). Conditional on all \(A_p,W_p^*\), the contributions at active primes are independent fair Bernoulli variables times strictly positive coefficients \(\log q_\kappa(p^{W_p^*})\). Subsets of active primes yielding a fixed sum form an antichain: a proper inclusion strictly increases the sum. Sperner's theorem therefore bounds every conditional point mass by \(\binom{m}{\lfloor m/2\rfloor}/2^m\), where \(m=\sum_{3\le p\le P}A_p\). The expectation of \(m\) diverges because \(\sum_p1/p=\infty\), whereas its variance is at most its mean; hence \(m\to\infty\) in probability, and the maximal point mass of the partial sums tends to zero. Independent remaining prime terms cannot increase the maximal point mass. Every marginal law of \(Z\) is therefore atomless. Its distribution function is continuous and strictly increasing throughout its support.

**Moments and the explicit case.** For any real \(s\), absolute convergence of the random logarithm and independence give
\[
\mathbb E\exp(sZ(t))
=\prod_p\left(1-\frac1p\right)\sum_{a=0}^{\infty}p^{-a}q_{\kappa(t)}(p^a)^s.
\]
This converges absolutely, since its local factors are \(1+O_s(p^{-2})\). To justify convergence of the corresponding empirical moments, for positive \(h\) use \(Q_\kappa(n)^h\le\prod_{p\mid n}(1-p^{-1})^{-h}\). Expand the latter product as \(\prod_{p\mid n}(1+c_p)\) with \(c_p=(1-p^{-1})^{-h}-1=O_h(1/p)\). Averaging over \(n\le X\) bounds its mean by \(\prod_p(1+c_p/p)<\infty\), uniformly in \(X\). This proves uniform integrability for any fixed power by taking a larger power; negative moments are bounded by one. Hence all asserted moments converge.

At \(\kappa=2\), the local generalized mean is the ordinary arithmetic mean:
\[
q_2(p^a)=\frac{U_{p,a}+W_{p,a}}2
=\frac{1-\frac12(1+p^{-1})p^{-a}}{1-p^{-1}}.
\]
Summing its geometric valuation law gives the exact local expectation
\[
\left(1-\frac1p\right)\sum_{a=0}^{\infty}p^{-a}q_2(p^a)
=1+\frac1{2p(p-1)},
\]
which establishes the displayed Euler-product first moment.

## Verification
The standalone standard-library Python checker `check.py` verifies, using exact rational arithmetic, that \(Q_2(n)\) agrees with an independently evaluated ordered two-divisor LCM sum for every integer \(1\le n\le200\). It also verifies the prime-power generalized-mean formula for selected primes and exponents, plus bounded-tail comparisons for the local Euler factors. Run `python check.py` to reproduce `VERIFY_OK`. The analytic arguments above, not finite computation, prove the functional convergence, full support, and lack of atoms.

## Relationship to prior work
Molnar's *Reciprocal LCM powers and Robin's criterion* (arXiv:2610.12816, first posted October 8, 2026) defines \(Q_\kappa\) and proves local estimates, parameter monotonicity, average and extremal orders, and Robin-type inequalities. Its inspected full text does not give a joint function-space limiting distribution, marginal support and non-atomicity, or the displayed Euler-product mean for \(Q_2\). Fan, Kobayashi and Molnar's earlier *A family of analogues to the Robin criterion* (arXiv:2511.02106) treats the distinct, unnormalized LCM-power family. The classical Erdős–Wintner theory can yield scalar distributional existence for appropriate additive logarithms; this is acknowledged rather than claimed novel. Davenport's continuity theorem for \(\sigma(n)/n\), discussed and extended by Jennings, Pollack and Thompson (arXiv:1306.0537), covers the endpoint \(\kappa=\infty\), not the function-space law across the reciprocal normalization.

The distinguishing statement here is the **joint continuous monotone random path** through all finite parameters and both endpoints, with its non-atomic full-support marginals and explicit special-parameter first moment. Priority beyond the inspected sources and indexed searches has not been independently established.

## Limitations
The conclusion establishes weak convergence in \(C([0,1])\), not almost-sure convergence for a deterministic sequence of integers and not an effective convergence rate. A continuous strictly increasing distribution function need not have an absolutely continuous density; no such density is claimed. The evidence does not exclude an unindexed general functional arithmetic-distribution theorem subsuming this construction. The accompanying finite checker is not a substitute for the infinite proof.

## References
1. Grant Molnar, *Reciprocal LCM powers and Robin's criterion*, arXiv:2610.12816 (first public preprint October 8, 2026), https://arxiv.org/abs/2610.12816.
2. Steve Fan, Mits Kobayashi, and Grant Molnar, *A family of analogues to the Robin criterion*, arXiv:2511.02106 (2025), https://arxiv.org/abs/2511.02106.
3. Emily Jennings, Paul Pollack, and Lola Thompson, *Variations on a theorem of Davenport concerning abundant numbers*, arXiv:1306.0537 (2013), https://arxiv.org/abs/1306.0537.
4. H. Davenport, *Über numeri abundantes* (1933), as referenced in [3].
