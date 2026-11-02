# Correlation-controlled growth of distinct scattered palindromes in binary Markov words

## Finding
For \(n\ge0\), let \(W_n=W_1\cdots W_n\) be the length-\(n\) prefix of a stationary symmetric two-state Markov chain. Its initial symbol is uniform, and each next symbol differs from the preceding one with probability \(t\in[0,1]\). Define \(P_n\) as the number of **distinct nonempty palindrome strings** that occur as scattered subsequences of \(W_n\); two positional embeddings of the same string count only once, and \(P_0=0\).

Define the following rational functions of \(z\):
\[
F_t(z)=\frac{tz}{1-(1-t)z},\qquad
S_t(z)=(1-t)z+\frac{t^2z^2}{1-(1-t)z},\qquad
I_t(z)=\frac{z(1+F_t(z))}{2},\qquad
H_t(z)=F_t(z)^2+S_t(z)^2.
\]
The expectation generating function is exactly
\[
\boxed{\sum_{n\ge0}\mathbb E_t[P_n]z^n=
\frac{2I_t(z)(1+S_t(z))}{(1-z)(1-H_t(z))}.}
\]
For each \(0<t<1\), \(H_t(r_t)=1\) has exactly one root \(r_t\in(0,1)\), and
\[
\boxed{\mathbb E_t[P_n]\sim K_t r_t^{-n},\quad
K_t=\frac{2I_t(r_t)(1+S_t(r_t))}{(1-r_t)r_tH_t'(r_t)}>0.}
\]
The exponential base \(\lambda(t)=r_t^{-1}\) **increases strictly with the transition probability** for \(0<t<1\). Its continuous endpoint values are
\[
\lambda(0)=1,\quad
\lambda(\tfrac12)=\frac{1+\sqrt2}{2},\quad
\lambda(1)=\sqrt{\frac{1+\sqrt5}{2}}.
\]
Thus the uniquely fastest exponential growth within this symmetric Markov family occurs at the perfectly alternating source \(t=1\). This optimizes the exponential rate, not necessarily each finite-length expectation.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\); the source is symmetric and stationary and has first-symbol law \((1/2,1/2)\). For \(0<t<1\) it is ergodic and irreducible, while \(t=0\) and \(t=1\) are included only in the exact generating function and endpoint-rate assertions. All occurrences are **scattered subsequences**, never contiguous factors; palindrome strings are counted without multiplicity. At \(t=0\), \(W_n\) is constant and \(P_n=n\). At \(t=1\), it is alternating up to a uniformly chosen first letter and the rational function becomes \(z(1+z)(1+z^2)/[(1-z)(1-z^2-z^4)]\). The aperiodic simple-pole asymptotic with \(K_t\) is asserted only for \(0<t<1\); the alternating endpoint has two dominant poles and parity-dependent leading constants.

## Proof
**1. Greedy occurrence times.** Fix a nonempty binary string \(u=u_1\cdots u_m\). Match its letters greedily in the infinite Markov source, and write \(\tau_j\) for the index of the \(j\)-th matched symbol. The greedy embedding exists inside \(W_n\) exactly when \(\tau_m\le n\). Stationarity gives \(\Pr(W_1=u_1)=1/2\). If \(W_1\ne u_1\), the first subsequent hit has geometric success parameter \(t\); therefore \(\tau_1\) has probability generating function \(I_t(z)=z(1+F_t(z))/2\), where \(F_t\) is the post-match waiting-time generating function for the **opposite** symbol. If the next target equals the matched symbol, a one-step return occurs with probability \(1-t\); otherwise the chain first flips and later returns, giving \(S_t(z)=(1-t)z+t^2z^2/[1-(1-t)z]\). By the strong Markov property, these post-match waits are independent conditional on the fixed target pattern. Consequently,
\[
\mathbb E[z^{\tau_m}\mathbf1_{\tau_m<\infty}]
=I_t(z)\prod_{j=2}^m
\begin{cases}S_t(z),&u_j=u_{j-1},\\F_t(z),&u_j\ne u_{j-1}.\end{cases}
\]
At \(t=0\) this remains a valid defective probability generating function: a never-hit target contributes probability zero.

**2. Palindrome adjacency encoding.** A nonempty binary palindrome is uniquely specified by its first symbol and its adjacent equal/different indicators. For an odd length \(2k+1\), the \(2k\) indicators are paired symmetrically, so the sum of its adjacent-wait products over every palindrome of that length is \(2(S_t^2+F_t^2)^k=2H_t^k\). For an even length \(2k+2\), the \(2k+1\) adjacency indicators contain a forced equal central pair, and all others occur twice; the product-weight sum is \(2S_tH_t^k\). Summing over \(k\ge0\) yields the total generating function of greedy completion times across all nonempty palindromes,
\[
G_t(z)=\frac{2I_t(z)(1+S_t(z))}{1-H_t(z)}.
\]
Since \(\Pr(\tau_m\le n)=[z^n]\mathbb E[z^{\tau_m}\mathbf1_{\tau_m<\infty}]/(1-z)\) and each distinct palindrome is counted once, the desired expectation is \(G_t(z)/(1-z)\). The interchange is coefficientwise finite because at time \(n\) no subsequence longer than \(n\) is possible.

**3. Dominant pole.** Assume \(0<t<1\). Both \(S_t,F_t\) have strictly positive coefficients and converge at least on \(|z|<1/(1-t)\), which contains the closed unit disk. The function \(H_t\) satisfies \(H_t(0)=0\), \(H_t(1)=2\), and is strictly increasing for real \(0<z\le1\). Thus the root \(r_t\in(0,1)\) exists uniquely and is simple. The coefficient of \(z^2\) in \(H_t\) is positive, and its \(z^3\)-coefficient is \(4t^2(1-t)>0\); the gcd of its positive support is therefore one. Equality in the coefficientwise triangle inequality shows \(H_t(z)\ne1\) on \(|z|=r_t\) except at \(z=r_t\). Also \(1-z\ne0\) there, and the numerator is strictly positive at \(r_t\). Hence the generating function has one simple dominant pole of radius \(r_t\), with principal part \(K_t/(1-z/r_t)\) and \(K_t\) as above. Rationality then gives the stated asymptotic.

**4. Strict growth-rate optimization.** Fix \(z\in(0,1)\) and put \(f=F_t(z)\). A direct identity is
\[
S_t(z)=z-(1-z)f,\qquad
H_t(z)=Q_z(f):=f^2+[z-(1-z)f]^2.
\]
At fixed \(z\), \(\partial_t f=z(1-z)/[1-z+tz]^2>0\). The quadratic \(Q_z\) is strictly convex and satisfies \(Q_z(0)=z^2<1\). At any positive solution of \(Q_z(f)=1\), its derivative with respect to \(f\) must therefore be strictly positive: the first positive level-one crossing of a strictly convex quadratic starting below one occurs on its increasing branch. For \(z=r_t\), we have just such a solution with \(f>0\); consequently \(\partial_t H_t(r_t)>0\). As \(\partial_z H_t(r_t)>0\), implicit differentiation gives
\[
\frac{dr_t}{dt}=-\frac{\partial_t H_t(r_t)}{\partial_z H_t(r_t)}<0.
\]
The root is continuous also at \(t=0,1\) by uniqueness and the limiting equations, so the exponential base increases strictly across the full parameter interval. At \(t=0\), \(H_0(z)=z^2\) and the generating function reduces to \(z/(1-z)^2\). At \(t=1\), \(H_1(z)=z^2+z^4\), hence the positive root gives \(\lambda(1)=\sqrt{(1+\sqrt5)/2}\). For \(t=1/2\), \(F_t=S_t=z/(2-z)\), so \(\lambda(1/2)=(1+\sqrt2)/2\).

## Verification
The accompanying executable `verify_markov_pal.py` uses only the Python standard library, including exact rational arithmetic. For every binary source word of lengths \(1\) through \(12\), it constructs all actual scattered subsequence strings and counts palindromes directly. Aggregating by number of symbol transitions gives exact Markov expectations, checked against the rational generating-function coefficients at \(t\in\{0,1/4,1/2,3/4,1\}\). A separate interval dynamic program checks all \(2^{15}\) source words at length \(15\). In addition, a 100-point parameter grid checks numerically that the positive root decreases, and the two special-root identities are checked. The script prints a single `VERIFY_OK` line on success. These are independent **finite** checks; the proof establishes the all-length claims.

## Relationship to prior work
Biers-Ariel, Godbole, and Kelley, *Expected Number of Distinct Subsequences in Randomly Generated Binary Strings* (arXiv:1704.08661, first posted 2017-04-27), include a two-state Markov source analysis for **unrestricted** distinct subsequences. Their Section 3.2 develops a four-coordinate recurrence; it does not impose a palindromic language restriction or derive this strict correlation-dependent palindrome growth law. Rubinchik and Shur, *The Number of Distinct Subpalindromes in Random Words* (arXiv:1505.08043, 2015), study **contiguous palindromic factors** under a uniformly independent source, which is a different random variable with different growth. The i.i.d. fair case \(t=1/2\) and deterministic alternating case \(t=1\) are known boundary instances of earlier scattered-palindrome enumeration, and are included here as consistency tests, not as originality claims. The new content is the genuinely correlated interval \(0<t<1\), its exact rational expectation and leading constant, and its strict exponential-rate comparison as the correlation changes.

## Limitations
This theorem concerns only **symmetric two-state Markov sources with stationary uniform marginals**. It makes no claim for asymmetric transitions, larger alphabets, nonstationary initial laws, or higher-order sources. It does not assert monotonicity of the finite-\(n\) expectation. The dominant-pole asymptotic has explicitly excluded \(t=1\), where the period-two denominator gives two conjugate dominant poles; only its growth base is stated. A more general weighted-language theorem not found in the searched literature might imply the result, so an independent literature audit remains warranted.

## References
1. Y. Biers-Ariel, A. Godbole, E. Kelley, *Expected Number of Distinct Subsequences in Randomly Generated Binary Strings*, arXiv:1704.08661 (first posted 2017-04-27), Section 3.2, https://arxiv.org/abs/1704.08661.
2. M. Rubinchik, A. M. Shur, *The Number of Distinct Subpalindromes in Random Words*, arXiv:1505.08043 (first posted 2015-05-29), https://arxiv.org/abs/1505.08043.
