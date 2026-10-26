# Sharp Bayesian reconstruction exponents and kernel-density extremes for binary additive cellular automata

## Finding

Let \(Q(z)=\sum_{j=0}^{d}c_jz^j\in\mathbb F_2[z]\) with \(d\ge1\) and \(c_0=c_d=1\). On the bilateral binary full shift, define
\[
(F_Qx)_i=\bigoplus_{j=0}^{d}c_jx_{i+j},\qquad i\in\mathbb Z.
\]
Let the input \(X_i\) be independent Bernoulli\((p)\) variables with \(0<p<1\). From the \(N\) consecutive output symbols \(Y_0,\ldots,Y_{N-1}\), let \(e_N(Q,p)\) be the minimum probability of incorrectly recovering the **entire** seed \((X_0,\ldots,X_{d-1})\) with an arbitrary measurable decoder. Its exact exponential error rate is governed by a periodic-point invariant.

Every nonzero bilateral kernel configuration \(k\) satisfying \(F_Q k=0\) is periodic. Write \(\rho(k)\) for its proportion of ones in one least period, and set
\[
\alpha_Q=\min_{k\in\ker F_Q\setminus\{0\}}\rho(k).
\]
Then, for every \(p\ne\tfrac12\),
\[
\boxed{\lim_{N\to\infty}-\frac1N\log e_N(Q,p)
  =\alpha_Q\log\frac1{2\sqrt{p(1-p)}}.}
\]
In particular, the shift-commuting factor map \(F_Q\) is one-to-one modulo sets of Bernoulli\((p)\) measure zero and is a measure-theoretic isomorphism onto its image process, despite possessing exactly \(2^d\) **topological** preimages of every output. In contrast, at \(p=\tfrac12\),
\[
\boxed{e_N(Q,1/2)=1-2^{-d}}\qquad\text{for all }N\ge1.
\]

For a fixed nonzero support width \(d\), the rate constant obeys sharp universal bounds
\[
\boxed{\frac1d\le\alpha_Q\le\frac{2^{d-1}}{2^d-1}.}
\]
The lower endpoint occurs **if and only if** \(Q(z)=1+z^d\). Every degree-\(d\) primitive binary polynomial attains the upper endpoint. These two endpoints are therefore both attained in every degree; exclusivity is asserted only at the lower endpoint.

## Assumptions and scope

All addition in the local rule is over \(\mathbb F_2\); logarithms are natural. The normalized polynomial is nonmonomial, and shifts of Laurent-polynomial rules reduce to the normalization above. The fixed observation window has \(N\ge1\), so the relevant input block has length \(L=N+d\). The Bayes error is for the entire \(d\)-bit initial seed, not an individual site or the entire infinite configuration from a finite window. The input measure is iid with full support and constant parameter \(p\) across every site. The asymptotic holds with \(d\), \(Q\), and \(p\) fixed as \(N\to\infty\).

A kernel configuration is specified by its \(d\) consecutive seed bits. The recurrence from \(F_Qk=0\) determines subsequent bits by \(c_d=1\) and preceding bits by \(c_0=1\). Its state transition permutes the \(2^d\) binary states; the all-zero state is fixed and any nonzero state lies on a cycle of length at most \(2^d-1\). Hence the minimum defining \(\alpha_Q\) is positive, finite, and exactly computable.

## Proof

**1. Finite fibers and their prior weights.** Given \((y_0,\ldots,y_{N-1})\), each seed \(s\in\mathbb F_2^d\) produces a unique length-\(L\) input word consistent with that output, by applying the nonzero trailing coefficient \(c_d\) successively. Thus there are exactly \(2^d\) input blocks in each finite fiber. Any two differ by a length-\(L\) restriction of one of the \(2^d-1\) nonzero periodic kernel configurations. For a word \(x\) of length \(L\), its probability is \(p^{w(x)}(1-p)^{L-w(x)}\), where \(w(x)\) is its Hamming weight. The optimum posterior decision is the maximum-prior candidate (MAP).

**2. Precise error comparison with half-binomial tails.** By bit complementation it suffices to take \(q=\min\{p,1-p\}<1/2\). Fix a nonzero kernel configuration \(k\) and let \(m_k(L)\) count the ones in its first \(L\) positions. Among these positions, the input contains a binomial number \(B\sim\operatorname{Bin}(m_k(L),q)\) of minority symbols. The competing word \(x\oplus k\) has strictly larger prior weight if and only if \(B>m_k(L)/2\), and at least equal prior weight if and only if \(B\ge m_k(L)/2\). On a strict comparison event, the true seed cannot be MAP; conversely, every MAP error requires at least one weak comparison event. Therefore, for every \(L=N+d\),
\[
\max_{k\ne0}\Pr\{\operatorname{Bin}(m_k(L),q)>m_k(L)/2\}
\ \le\ e_N(Q,p)\ \le\
\sum_{k\ne0}\Pr\{\operatorname{Bin}(m_k(L),q)\ge m_k(L)/2\}.
\]
Since each \(k\) is periodic, \(m_k(L)=\rho(k)L+O_Q(1)\), uniformly across the finite nonzero kernel. For fixed \(0<q<1/2\), the elementary central-binomial lower bound and exponential-moment upper bound give the **same** rate for strict and weak half-tails:
\[
\lim_{m\to\infty}-\frac1m\log\Pr\{\operatorname{Bin}(m,q)>m/2\}
=\lim_{m\to\infty}-\frac1m\log\Pr\{\operatorname{Bin}(m,q)\ge m/2\}
=\log\frac1{2\sqrt{q(1-q)}}.
\]
The upper bound follows from a Chernoff parameter \(\tfrac12\log[(1-q)/q]\); the central term with an appropriate integer rounding yields the lower bound by Stirling's formula. A finite maximum/sum preserves the smallest of finitely many positive exponential rates, proving the asserted \(\alpha_Q\) formula.

**3. Measurable inversion and the fair-input discontinuity.** When \(p\ne1/2\), the error tends to zero exponentially. Equivalently, by the strong law on every nonzero periodic kernel support, all nontrivial competing seeds eventually have strictly smaller likelihood than the true seed, almost surely. Hence the seed is a measurable function of the entire one-sided output \((Y_i)_{i\ge0}\), and applying the same argument after every integer shift gives a shift-equivariant measurable inverse on a conull invariant set. If \(p=1/2\), every length-\(L\) input word is equally likely, so the \(2^d\) seeds are conditionally uniform for each output cylinder and the exact error is \(1-2^{-d}\). The uniformity also holds conditionally on the entire output by consistency of finite-dimensional conditional expectations. No finite output observation identifies the seed with probability one when \(0<p<1\), because every finite fiber candidate has positive prior probability.

**4. Lower sharp kernel-density bound and rigidity.** A nonzero kernel configuration contains no run of \(d\) consecutive zeros: such a run is the zero recurrence state, which generates only the zero configuration forwards and backwards. Averaging the number of ones over all cyclic windows of length \(d\) gives \(d\rho(k)\ge1\); hence \(\alpha_Q\ge1/d\). If equality holds, some nonzero kernel has exactly one one in **every** length-\(d\) window. The difference of consecutive window counts implies \(k_{i+d}=k_i\), so the kernel consists of a single one in each period of length \(d\). Substitute this configuration into \(Q\): for each position with residue not at the single one, the only possible nonzero input term is a unique interior coefficient \(c_j\), forcing \(c_1=\cdots=c_{d-1}=0\). Thus \(Q=1+z^d\). Conversely that polynomial admits a kernel sequence with one one per period of length \(d\), proving the equivalence.

**5. Upper sharp bound.** The invertible recurrence permutes all \(2^d-1\) nonzero seed states. Average \(\rho(k)\) uniformly over all such states: each state has the same periodic average as the fraction of steps whose first coordinate equals one. Exactly \(2^{d-1}\) nonzero seed states have this coordinate equal one. Thus the average of the nonzero orbit densities is \(2^{d-1}/(2^d-1)\), and their minimum cannot exceed that average. If \(Q\) is primitive, the nonzero state permutation has a single cycle of length \(2^d-1\) and every nonzero kernel has exactly this density. Primitive polynomials of each positive degree exist, so the upper bound is attained.

## Verification

The standalone standard-library checker `verify.py` recomputes every nonzero periodic kernel for all \(127\) normalized binary polynomials of degrees one through seven. It checks both density bounds and the unique lower-endpoint rule in each degree, as well as the three explicit examples \(\alpha_{1+z}=1\), \(\alpha_{1+z^2}=1/2\), and \(\alpha_{1+z+z^2}=2/3\). It independently enumerates the exact finite-fiber Bayes error in \(40\) small cases, then checks \(64\) instances of the strict/weak binomial comparison bounds against direct enumeration. It uses rational arithmetic for the finite probability tests. The complete unrestricted conclusions rely on the recurrence and asymptotic proof above, not on finite enumeration.

## Relationship to prior work

Kari and Taati (arXiv:1311.2319, Example 33) analyze the image of biased Bernoulli input under the adjacent XOR cellular automaton and its Gibbsian properties; this supplies a natural motivating statistical-mechanical context, but does not in the inspected material determine the general kernel-density Bayes error exponent or the sharp all-polynomial envelope. Lőrinczi, Maes and Vande Velde (1998, Proposition 3.3) analyze Gibbs/non-Gibbs behavior of related transformed Bernoulli measures, a different property of the output process. Ban and Chang (2009) study topological pressure and entropy of linear cellular automata, which does not by itself provide this particular finite-seed reconstruction exponent. Dow (1997) studies global injectivity for additive cellular automata, distinct from almost-everywhere invertibility under a specified biased probability law. Maximum-likelihood decisions, binomial large deviations, and primitive polynomial cycles are established ingredients; the evaluated all-rule rate, sharp extremal characterization, and probabilistic/topological distinction are the particular results here.

## Limitations

This is a self-reviewed mathematical finding and has not undergone independent audit or certified priority review. Access to Dow's full paper and Ban–Chang's full paper was incomplete; the possibility of earlier implicit or equivalent treatments in coding, filtering or symbolic dynamics remains a live priority risk. A finite computation cannot prove the full statement. Rates are asymptotic for fixed polynomial and fixed bias, and they do not imply noise robustness, a continuous inverse, temporal entropy identities, or a classification of the upper-bound equality cases beyond the primitive examples. The conclusion at \(p=1/2\) is exactly different; limits \(p\to1/2\) and \(N\to\infty\) are not interchangeable.

## References

1. J. Kari and S. Taati, *Statistical Mechanics of Surjective Cellular Automata*, arXiv:1311.2319 (first submitted 2013-11-10), https://arxiv.org/abs/1311.2319.
2. J. Lőrinczi, C. Maes, and K. Vande Velde, *Transformations of Gibbs Measures*, 1998, DOI: 10.1007/s004400050185.
3. J.-C. Ban and C.-H. Chang, *The Topological Pressure of Linear Cellular Automata*, Entropy 11 (2009), 271–284, DOI: 10.3390/e11020271.
4. R. Dow, *Additive cellular automata and global injectivity*, Physica D (1997), DOI: 10.1016/S0167-2789(97)00074-2.
5. B. Host, A. Maass, and S. Martínez, *Uniform Bernoulli measure in dynamics of permutative cellular automata with algebraic local rules*, DCDS 9 (2003), 1423–1446, DOI: 10.3934/dcds.2003.9.1423.
