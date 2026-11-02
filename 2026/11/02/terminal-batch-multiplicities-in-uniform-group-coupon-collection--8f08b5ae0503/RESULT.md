# Terminal-batch multiplicities in uniform group coupon collection: exact law, sparse collisions, and bulk lattice thinning

## Finding

A collection completed by random packages can reveal multiple previously missing coupon types in its final package. The probability of this event admits a sharp, uniform sparse-package asymptotic. When the package size is a positive fraction of the collection, the entire joint law of completion time and number of new terminal types has a lattice-dependent Poisson limit.

For integers \(n\ge2\), \(1\le s<n\), \(t\ge2\) and \(1\le b\le s\), the exact joint distribution is
\[
\Pr(T=t,B=b)=\binom nb\frac{(s)_{\underline b}}{(n)_{\underline b}}
\sum_{\ell=0}^{n-b}(-1)^\ell\binom{n-b}{\ell}
\left(\frac{\binom{n-b-\ell}{s}}{\binom ns}\right)^{t-1}.
\tag{1}
\]
The fraction with falling factorials is interpreted as zero when \(b>s\), and all binomial coefficients with upper argument smaller than their lower argument are zero.

**Sparse packages.** For any integer sequence \(2\le s_n<n\) with \(s_n/n\to0\),
\[
\Pr(B_n\ge2)=\frac{s_n-1}{2n}\left(1+O\left(\frac{s_n}{n}\right)\right),
\tag{2}
\]
where the relative-error constant is absolute. Explicit all-finite-parameter bounds are given below. Thus fixed package size \(s\ge2\) gives the exact first-order collision probability \((s-1)/(2n)\).

**Bulk packages.** Suppose \(s_n/n\to c\in(0,1)\), put \(q_n=1-s_n/n\) and
\[
a_n=\left\lfloor\frac{\log n}{-\log q_n}\right\rfloor,\qquad
\theta_n=nq_n^{a_n}.
\]
On any subsequence such that \(\theta_n\to\theta\), necessarily \(1\le\theta\le1/(1-c)\). With \(q=1-c\),
\[
\Pr(T_n-a_n=j,B_n=b)\ \longrightarrow\
 e^{-\theta q^{j-1}}\frac{(\theta c q^{j-1})^b}{b!}
 \quad(j\in\mathbb Z,\ b\ge1),
\tag{3}
\]
and convergence of the whole joint probability law is in total variation. Its limiting terminal multiplicity is nondegenerate; for example, when \(c=1/2\) and \(\theta=1\), the limiting probability of discovering two or more new types in the final draw is approximately \(0.278647896663\).

## Assumptions and scope

At each positive integer time, draw an independent uniformly distributed subset of exactly \(s\) distinct types from the same population \([n]\). Draws are independent across time, but types selected together in one draw are negatively dependent. Write \(M_t\) for the number of types never drawn through time \(t\), with \(M_0=n\). Set \(T=\inf\{t\ge1:M_t=0\}\) and \(B=M_{T-1}\); note that \(T\ge2\), \(1\le B\le s\), and \(T\) is almost surely finite. Write \((z)_{\underline b}=z(z-1)\cdots(z-b+1)\).

The asymptotic sparse result assumes only \(2\le s_n\) and \(s_n/n\to0\), not fixed \(s\); the bulk result assumes the proportion converges to a point strictly between zero and one. Neither result imposes independence within a package.

## Proof

### 1. Transition law and the exact joint formula

Given \(M_t=m\), exactly \(r\) missing coupons appear in the next package with probability
\[
 p_m(r)=\frac{\binom mr\binom{n-m}{s-r}}{\binom ns},
 \qquad \max(0,s-n+m)\le r\le\min(m,s).
 \tag{4}
\]
Fix a candidate set \(A\) of \(b\) types to be precisely the missing ones after \(t-1\) packages. All prior packages must avoid \(A\), and each of the \(n-b\) other types must appear at least once. Inclusion-exclusion over additional avoided types gives
\[
 \Pr(M_{t-1}=b)=\binom nb
 \sum_{\ell=0}^{n-b}(-1)^\ell\binom{n-b}{\ell}
 \left(\frac{\binom{n-b-\ell}{s}}{\binom ns}\right)^{t-1}.
\tag{5}
\]
Conditional on the history with \(b\) missing types, the next package covers all of them with probability
\(\binom{n-b}{s-b}/\binom ns=(s)_{\underline b}/(n)_{\underline b}\).
Multiplying (5) by this probability proves (1).

### 2. Sparse terminal-collision asymptotics and finite bounds

Consider the embedded chain of strictly decreasing missing counts: suppress unsuccessful draws that leave \(M\) unchanged. Each positive state \(m\) can be visited at most once, and the chain is absorbed at \(0\).

When the chain is at \(m=2\), the probability of jumping directly to \(0\) at its next strict decrease equals
\[
 h_{n,s}=\frac{\Pr(\text{both missing types selected})}
 {\Pr(\text{at least one missing type selected})}
 =\frac{s-1}{2n-s-1}.
\tag{6}
\]
Therefore \(\Pr(B=2)=h_{n,s}\Pr(\text{the embedded chain visits }2)\).

Let \(c_n=s/n\). For each specific set of \(r\) missing types the probability all are selected in a given package is \((s)_{\underline r}/(n)_{\underline r}\le c_n^r\). From a positive state \(m\), the probability of a strict decrease at the next ordinary draw is at least \(c_n\), since a fixed missing type is drawn with that probability. To skip state \(2\) from any state \(m\ge3\), a strict jump must select at least \(m-1\) of the \(m\) missing types. By a union bound, its one-draw probability is at most \(m c_n^{m-1}\), and its probability conditioned on a strict decrease is at most \(m c_n^{m-2}\). Summing over potentially visited states yields
\[
 \Pr(\text{embedded chain never visits }2)
 \le \sum_{m=3}^{\infty}m c_n^{m-2}
 = \frac{c_n(3-2c_n)}{(1-c_n)^2}
 =:\eta(c_n).
\tag{7}
\]
Similarly, for absorption from \(m\ge3\) the probability of a one-draw jump that includes all \(m\) missing coupons is at most \(c_n^m\). Conditional on leaving \(m\), the probability is at most \(c_n^{m-1}\); summing over visited \(m\ge3\) gives
\[
\Pr(B\ge3)\le\sum_{m=3}^{\infty}c_n^{m-1}
 =\frac{c_n^2}{1-c_n}.
\tag{8}
\]
Combining (6)–(8), for every \(n\ge3\) and \(2\le s<n\),
\[
 h_{n,s}\max\{0,1-\eta(c_n)\}
 \le\Pr(B\ge2)\le h_{n,s}+\frac{c_n^2}{1-c_n}.
\tag{9}
\]
Since \(h_{n,s}=(s-1)/(2n)\,(1+O(c_n))\) and the added error is \(O(c_n h_{n,s})\) uniformly for \(s\ge2\), (9) proves (2).

### 3. Bulk missing-count process and terminal law

For any fixed integer \(k\ge1\), the falling factorial moment of \(M_t\) is exactly
\[
 \mathbb E(M_t)_{\underline k}
 =(n)_{\underline k}
 \left(\frac{(n-s)_{\underline k}}{(n)_{\underline k}}\right)^t.
\tag{10}
\]
Indeed each of \(k\) specified distinct coupons must be avoided in all \(t\) independent packages. Under \(s_n/n\to c\in(0,1)\), for fixed \(k,j\) and \(t=a_n+j\), the bracket in (10) is \(q_n^k(1+O_k(1/n))\) while \(t=O(\log n)\). Along a subsequence \(\theta_n\to\theta\), (10) thus converges to \((\theta q^j)^k\). The factorial-moment method (or the generating-function expansion) yields
\[
 M_{a_n+j}\Longrightarrow \operatorname{Poisson}(\theta q^j).
\tag{11}
\]
For every fixed \(m\), the hypergeometric transition (4) converges to independently retaining each of \(m\) missing types with probability \(q\). Coupling this finite-state transition over any fixed number of consecutive times to (11) gives joint finite-dimensional convergence to a death chain satisfying
\[
 \widetilde M_j\sim\operatorname{Poisson}(\theta q^j),\qquad
 \widetilde M_{j+1}\mid\widetilde M_j\sim\operatorname{Binomial}(\widetilde M_j,q).
\tag{12}
\]
Poisson splitting implies the successive first-discovery counts
\(N_j=\widetilde M_{j-1}-\widetilde M_j\) are mutually independent Poisson variables of respective means \(\theta c q^{j-1}\) on every finite set of integer times. A consistent two-sided construction is \(\widetilde M_j=\sum_{i>j}N_i\), each sum finite almost surely.

For integers \(j\) and \(b\ge1\), since a terminal draw must see all previously missing types,
\[
 \Pr(T_n=a_n+j,B_n=b)=
 \Pr(M_{a_n+j-1}=b)\frac{(s_n)_{\underline b}}{(n)_{\underline b}}.
\tag{13}
\]
By (11), the first factor tends to \(e^{-\theta q^{j-1}}(\theta q^{j-1})^b/b!\), and the second to \(c^b\), proving (3) pointwise. The putative limit has total mass one:
\[
\sum_{b=1}^{\infty}e^{-\theta q^{j-1}}\frac{(\theta c q^{j-1})^b}{b!}
=e^{-\theta q^j}-e^{-\theta q^{j-1}},
\quad
\sum_{j\in\mathbb Z}(e^{-\theta q^j}-e^{-\theta q^{j-1}})=1.
\tag{14}
\]
Pointwise convergence of nonnegative masses on a countable space to a probability law implies total-variation convergence. In particular,
\[
\lim\Pr(B_n\ge2)=1-\sum_{j\in\mathbb Z}
 e^{-\theta q^{j-1}}\theta c q^{j-1}.
\tag{15}
\]
These formulas give the exact simultaneous-completion probability on each lattice phase subsequence and the example stated above.

## Verification

The included standard-library checker \(`checks/check.py`\) reproduces the finite formula against exact-rational hypergeometric dynamic programming and an independent complete enumeration of ordered small packages, tests factorial moments and transition approximations across bulk sizes, and calculates the embedded strict-decrease chain exactly for many finite parameter values. It checks (9) and the sparse coefficient numerically for additional larger populations. In the completed execution, all 1,162 assertions passed. These finite experiments do not replace the proof of the uniform sparse bound or the asymptotic Poisson law.

## Relationship to prior work

Betken and Thäle (arXiv:2202.07485; earliest posted 2022-02-15) develop one-time unseen-count Gaussian/Poisson approximations for uniform group drawings at fixed package size. Schilling and Henze (2021) provide related Poisson limits for coupon occurrence counts. Berend and Sher (arXiv:2509.17201, 2025) study optimal drawing distributions and, notably, already treat uniform sampling with package size proportional to the population, including completion-time scaling and one-time asymptotics. None of those facts about a one-time missing count is claimed as new. The present statement addresses the **number of simultaneously newly completed types**, the sharp \((s-1)/(2n)\) sparse collision coefficient with explicit finite bounds, and the joint terminal time/multiplicity law.

Stadje (1990) studied group drawings and finite waiting-time distributions. The full text of that older paper was unavailable for complete comparison; its possible relationship to the exact finite formula remains a priority risk. Standard occupancy inclusion-exclusion and Poisson thinning themselves are classical; originality is asserted only for the combined terminal-multiplicity classification and sharp sparse coefficient, to the extent established by the inspected literature.

## Limitations

The model requires independent packages that are uniformly distributed among all subsets of a *fixed size*, with distinct types inside a package; it does not cover nonuniform package laws or sampling with repeated types within one package. The sparse relative error applies only as \(s_n/n\to0\), and bulk limits require the explicit subsequence phase \(\theta_n\to\theta\). The bounds may be crude when \(s/n\) is not small. Finite experiments are not exhaustive over all \(n,s\). Historical priority, especially against inaccessible older full texts, requires separate expert assessment. The derivation does not claim independent external validation.

## References

1. C. Betken and C. Thäle, *Approaching the coupon collector's problem with group drawings via Stein's method*, arXiv:2202.07485, first posted 2022-02-15; *Journal of Applied Probability* (2023), doi:10.1017/jpr.2023.6. https://arxiv.org/abs/2202.07485
2. J. Schilling and N. Henze, *Two Poisson limit theorems for the coupon collector’s problem with group drawings*, *Journal of Applied Probability* 58 (2021), 966–977, doi:10.1017/jpr.2021.15. https://doi.org/10.1017/jpr.2021.15
3. D. Berend and T. Sher, *On a Conjecture of Schilling Regarding the Coupon Collector's Problem*, arXiv:2509.17201 (2025). https://arxiv.org/abs/2509.17201
4. W. Stadje, *The Collector's Problem with Group Drawings*, *Journal of Applied Probability* (1990), doi:10.2307/1427566. https://doi.org/10.2307/1427566
