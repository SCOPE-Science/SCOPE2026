# Conditional singleton–size-class covariance has a sharp hierarchy of sign transitions

## Finding

For a set partition chosen uniformly from the \(S(n,k)\) partitions of \([n]\) into exactly \(k\) nonempty blocks, let \(X_r\) be the number of blocks of cardinality \(r\). Fix any \(j\ge2\). Whenever \(n,k\to\infty\) and \(k/n\to\alpha\in(0,1)\), define the unique \(x=x(\alpha)>0\) by
\[
\frac{x}{1-e^{-x}}=\frac1\alpha,
\quad p_r=\frac{x^r}{r!(e^x-1)},\quad
\mu=\frac{x}{1-e^{-x}},\quad
\sigma^2=\mu(1+x-\mu)>0.
\]
Then the exact asymptotic mixed covariance is
\[
\boxed{\lim_{n\to\infty}\frac{\operatorname{Cov}(X_1,X_j)}k
=-\frac{p_1p_j}{\sigma^2}\bigl[j+\mu(x-j)\bigr].}
\tag{1}
\]
For \(j=2\), the limit in (1) is negative for every \(\alpha\in(0,1)\). For each integer \(j\ge3\), the equation
\[
\boxed{x_j^2-jx_j+j(1-e^{-x_j})=0}\tag{2}
\]
has exactly one positive root. Setting \(\alpha_j=(1-e^{-x_j})/x_j\), the limit in (1) is positive when \(\alpha>\alpha_j\) and negative when \(\alpha<\alpha_j\). Accordingly, the finite-sample covariance has the indicated sign for all sufficiently large \(n\) along any such sequence. No sign conclusion is asserted when \(\alpha=\alpha_j\).

The thresholds are strictly ordered: \(\alpha_{j+1}<\alpha_j\) for every \(j\ge3\), and
\[
\lim_{j\to\infty}j\alpha_j=1,\qquad
\alpha_3=0.5464068225505325\ldots.
\tag{3}
\]
Thus singleton and sufficiently large fixed-size block counts become *positively* correlated in the fine-block regime, but are negatively correlated in the coarse-block regime; size-two blocks remain negatively correlated to first order throughout the whole density range.

## Assumptions and scope

The sample space is the set of all unlabelled-block set partitions of \([n]\), with every partition having exactly \(k\) blocks equally likely; \(S(n,k)\) denotes a Stirling number of the second kind. The block sizes themselves are positive integers. The integer \(j\ge2\) is held fixed as \(n\) and \(k\) grow and \(0<\alpha<1\) is fixed. The theorem does not cover \(\alpha=0\), \(\alpha=1\), a growing \(j\), or the critical rays \(\alpha=\alpha_j\). The classification concerns *leading-order covariance*, rather than exact finite-size signs.

## Proof

**1. Exact marked-block moments.** A distinguished block of size \(r\) is specified by its label set; the complement is partitioned into \(k-1\) blocks. Two distinguished disjoint blocks of sizes \(1\) and \(j\) leave \(k-2\) blocks. Therefore, with the convention \(S(a,b)=0\) for impossible indices,
\[
\begin{aligned}
\mathbb E X_1&=n\frac{S(n-1,k-1)}{S(n,k)},\\
\mathbb E X_j&=\binom nj\frac{S(n-j,k-1)}{S(n,k)},\\
\mathbb E(X_1X_j)&=n\binom{n-1}{j}\frac{S(n-j-1,k-2)}{S(n,k)}.
\end{aligned}
\tag{4}
\]
In particular, covariance is the third expression minus the product of the first two. These identities also define exact independent finite checks.

**2. Conditional independent-size representation.** Let \(Y_1,\ldots,Y_k\) be independent zero-truncated Poisson variables with law \(\mathbb P(Y=r)=x^r/[r!(e^x-1)]\), \(r\ge1\). Conditional on \(\sum_iY_i=n\), their ordered size profile has mass proportional to \(\prod_i (Y_i!)^{-1}\), exactly the probability of the ordered block sizes of a uniform set partition into \(k\) blocks, after uniformly ordering its blocks. Thus \(X_r\) is the number of indices with \(Y_i=r\) under this conditioning, for any \(x>0\). The map \(x\mapsto\mu(x)=x/(1-e^{-x})\) is strictly increasing from 1 to infinity, since its derivative is the positive variance divided by \(x\). Therefore the chosen saddle \(x\) exists uniquely.

**3. Covariance from a uniform saddle expansion.** Put
\[
F(z;u,v)=e^z-1+(e^u-1)z+(e^v-1)\frac{z^j}{j!}.
\]
Marking the size-one and size-\(j\) classes gives exactly
\[
\mathbb E(e^{uX_1+vX_j})=
\frac{[z^n]F(z;u,v)^k}{[z^n]F(z;0,0)^k}.
\tag{5}
\]
For \(k/n\) in a compact subinterval of \((0,1)\), the positive solution \(\zeta(u,v)\) of \(\zeta F_z/F=n/k\) is analytic near \((u,v)=(0,0)\), taking value \(x_{n,k}\) there, where \(\mu(x_{n,k})=n/k\) and \(x_{n,k}\to x\). Coefficients of \(F\) have span one, so the Cauchy coefficient circle has a unique maximum at its positive saddle; outside a fixed small arc there is an exponential modulus gap. Taylor expansion of the integrand on that arc through the nonzero quadratic coefficient gives, uniformly in a fixed complex neighborhood of the marks,
\[
\log[z^n]F(z;u,v)^k
=k\left[\log F(\zeta;u,v)-\frac nk\log\zeta\right]
-\frac12\log(2\pi k\,\operatorname{Var}_{u,v}Y)+O(k^{-1}).
\tag{6}
\]
The error and its first two derivatives are uniform by analytic continuation and Cauchy estimates. Here \(\operatorname{Var}_{u,v}Y\) is the positive saddle variance, analytically continued near zero. Because \(n/k\to1/\alpha\), the second mixed derivative of (6), divided by \(k\), converges to the corresponding second derivative of the Legendre-type saddle free energy.

Write \(I_r=\mathbf1_{\{Y=r\}}\). Implicit differentiation of the saddle condition (or differentiation of the free energy) gives the Schur-complement formula
\[
\lim\frac{\operatorname{Cov}(X_1,X_j)}k
=\operatorname{Cov}(I_1,I_j)-
\frac{\operatorname{Cov}(I_1,Y)\operatorname{Cov}(I_j,Y)}{\operatorname{Var}Y}.
\tag{7}
\]
Since \(j\ne1\), \(\operatorname{Cov}(I_1,I_j)=-p_1p_j\) and \(\operatorname{Cov}(I_r,Y)=p_r(r-\mu)\). The zero-truncated Poisson variance is \(\sigma^2=\mu(1+x-\mu)\), yielding
\[
-\frac{p_1p_j}{\sigma^2}\bigl[\sigma^2+(1-\mu)(j-\mu)\bigr]
=-\frac{p_1p_j}{\sigma^2}\bigl[j+\mu(x-j)\bigr],
\]
which proves (1). This analytic step is essential: a merely weak Gaussian limit without moment control would not establish covariance convergence.

**4. The transition and its ordering.** The sign-relevant bracket has the same sign as
\[
h_j(x)=x^2-jx+j(1-e^{-x}),
\quad j+\mu(x-j)=\frac{h_j(x)}{1-e^{-x}}.
\]
For \(j=2\), \(h_2'(x)=2(x-1+e^{-x})>0\) for \(x>0\), and \(h_2(0)=0\), so (1) is negative. For \(j\ge3\), let
\[
q_j(x)=\frac{h_j(x)}x=x-j+j\int_0^1e^{-tx}\,dt.
\]
Then \(q_j(0+)=0\), \(q_j'(0+)=1-j/2<0\), \(q_j''(x)=j\int_0^1t^2e^{-tx}\,dt>0\), and \(q_j'(x)\to1\), \(q_j(x)\to\infty\). Strict convexity gives exactly one positive root, with \(h_j<0\) before it and \(h_j>0\) afterward. Since \(\alpha=(1-e^{-x})/x\) strictly decreases in \(x\), the claimed sign classification follows.

At the positive root, \(j=x_j^2/(x_j-1+e^{-x_j})\). The right side is strictly increasing in \(x>0\): after multiplication by its positive denominator squared, its derivative has the sign of \((x-2)+(x+2)e^{-x}>0\), since \((x-2)e^x+x+2\) has two zero initial derivatives and second derivative \(xe^x>0\). Hence \(x_j\) strictly increases with \(j\), so \(\alpha_j\) strictly decreases. For \(j\ge3\), direct evaluation of \(h_j\) at \(j-2\) and \(j-1\) puts \(x_j\in(j-2,j-1)\); the root identity yields \(j\alpha_j=j-x_j\). From \(j-x_j=j(1-e^{-x_j})/x_j\) and \(x_j\to\infty\) one obtains \(j-x_j\to1\), proving (3).

## Verification

The independent `verify.py` uses exact Stirling-number arithmetic and enumerates all restricted-growth strings through eight points. It compares three separately counted moments to (4), then checks the limiting covariance numerically at increasing sample sizes and the uniqueness/ordering constraints by bisection. At the packaging verification, it reports 270 checks passed. All infinite assertions are proved above, not by finite experiments.

## Relationship to prior work

Timashev (2003) directly treats the same uniform distribution on \(S(n,k)\) set partitions, establishing one-size marginal moments, Poisson and normal local laws. Its accessible full text shows one-size distributions and factorial-moment techniques; the mixed singleton–size-class covariance, positive correlation phase, unique threshold roots, and their ordering are not stated in the inspected results. Arratia and DeSalvo (2016, especially Sections 1–3) describe a general conditioning/Poisson representation for assemblies with a fixed component count, developing different low-rank asymptotics; that representation helps explain (5) but does not state this macroscopic block-density crossover. Barbour and Gnedin (2008, Sections 2–6) study a different infinite-box occupancy regime with prescribed box frequencies, and their covariance formulas do not imply the positive conditional set-partition phase without a new argument. More generally, standard multivariate saddle methods imply the covariance reduction (7) in many assembly models; the structural transition in (2)–(3), not the generic method, is the contribution assessed here.

## Limitations

The result is first-order in \(k\), for each fixed \(j\). It is silent at the critical values \(\alpha=\alpha_j\), and does not give the exact finite \(n,k\) transition or a joint limit for growing \(j\). It does not claim complete historical priority: an older general multivariate saddle-point treatment could imply the formula implicitly. The finite verification program is not a proof of the asymptotic or uniqueness statements.

## References

1. A. N. Timashev, “Random partitions of sets with a known number of blocks,” *Diskretnaya Matematika* 15(2) (2003), 138–148, DOI 10.4213/dm201, https://www.mathnet.ru/eng/dm201. English version published 2003-07-01: *Discrete Mathematics and Applications* 13(3) (2003), 307–317, DOI 10.1515/156939203322385919.
2. R. Arratia and S. DeSalvo, “Poisson and independent process approximation for random combinatorial structures with a given number of components, and near-universal behavior for low rank assemblies,” arXiv:1606.04642 (2016), https://arxiv.org/html/1606.04642v2.
3. A. D. Barbour and A. V. Gnedin, “Small counts in the infinite occupancy scheme,” arXiv:0809.4387 (2008), https://arxiv.org/html/0809.4387v1.
4. P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press (2009), Chapter VIII (saddle-point estimates).

