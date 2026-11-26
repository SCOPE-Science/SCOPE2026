# Full-range binomial left-loadedness and the partial-sum inequality

## Finding

Let \(n,m\) be positive integers with \(n\ge 2m\), \(X\sim\operatorname{Bin}(n,m/n)\), and
\[
\alpha_i=\Pr(X\le m-i)-\Pr(X\ge m+i),\qquad 1\le i\le m.
\]
For every \(1\le k\le m\), \(\sum_{i=1}^k\alpha_i\ge0\) (condition \(L_2\)). These inequalities are strict when \(n>2m\). Furthermore, when \(n>2m\) and \(m\ge3\), the sequence has a positive-to-negative single crossing, allowing zeros (condition \(L_1\)). In particular this proves Conjecture 4.1 of Fokkink, Papavassiliou and Pelekis in its full stated range.

## Assumptions and scope

The mean \(m\) is an integer and the success probability is at most one half. Left-loadedness in Definition 1.2 of [1] means that either \(L_1\) or \(L_2\) holds. The sign condition \(L_1\) means that the sequence is nonnegative up to a cutoff and nonpositive thereafter. The result is not an assertion about noninteger means or success probabilities above one half.

## Proof

When \(n=2m\) all \(\alpha_i\) vanish by binomial symmetry. Assume \(n>2m\). Write \(S_k=\sum_{i=1}^k\alpha_i\). Because the mean is \(m\), the expected positive and negative parts of \(X-m\) are equal. The tail-sum identities for these parts give
\[
 S_m=\sum_{i=m+1}^{n-m}\Pr(X\ge m+i)>0,
\]
where the term with \(i=m+1\) is positive. This proves \(L_2\) for \(m=1\). For \(m=2\) it suffices also to use \(\alpha_1>0\), which is Simmons' inequality as stated in [1, §3], [2].

Now suppose \(m\ge3\). Set \(N=n-m>m\), \(a_j=\Pr(X=j)\), and \(\beta_i=a_{m+i}/a_{m-i}\) for \(1\le i\le m\). The binomial mass ratio gives
\[
\frac{\beta_{i+1}}{\beta_i}=
\frac{m^2(N-i)(N+i+1)}{N^2(m+i+1)(m-i)},\qquad 1\le i<m.
\]
Subtracting the denominator from the numerator gives \((N-m)((N+m)i(i+1)-mN)\). Thus \(\beta_i\) first weakly decreases and then weakly increases. It starts at \(\beta_1=m(N+1)/(N(m+1))<1\).

To prove \(\beta_m>1\), write \(F_m(N)=\beta_m=\binom{N+m}{2m}(m/N)^{2m}\). For real \(x\ge m\) set
\[
h_m(x)=\log\frac{x+m+1}{x-m+1}+2m\log\frac{x}{x+1}.
\]
Then \(F_m(N+1)/F_m(N)=\exp(h_m(N))\), and
\[
h_m'(x)=\frac{2m(x+1-m^2)}{x(x+1)(x-m+1)(x+m+1)}.
\]
The derivative is negative before \(m^2-1\) and positive afterward; \(h_m\) tends to zero and is strictly negative on its increasing branch. At \(m\), \(\exp(h_m(m))=(2m+1)(m/(m+1))^{2m}>1\): for \(m=3\) its numerator and denominator are \(5103\) and \(4096\), and for \(m\ge4\), \((1+1/m)^{2m}<e^2<9\le 2m+1\). Hence \(h_m\) crosses zero once from above, and \(F_m(N)\) first rises and then descends, allowing a tie at the turn. Its left endpoint is \(F_m(m)=1\) and its limit is \(B_m=m^{2m}/(2m)!\). We have \(B_3=729/720>1\), and
\[
\frac{B_{m+1}}{B_m}=\left(1+\frac1m\right)^{2m}\frac{m+1}{2(2m+1)}>1,
\]
since the first three binomial terms of the power sum to \(5-1/m>2(2m+1)/(m+1)\) for \(m\ge3\). The first integer step of \(F_m\) is strictly increasing and the terminal limit exceeds one, so \(F_m(N)>1\) for all integers \(N>m\).

Consequently \(b_i=a_{m-i}-a_{m+i}=a_{m-i}(1-\beta_i)\) is nonnegative up to a cutoff and nonpositive thereafter. As \(\alpha_{i+1}=\alpha_i-b_i\), the \(\alpha_i\) first weakly decrease and then weakly increase. Simmons' inequality gives \(\alpha_1>0\), and the endpoint bound gives \(\alpha_m\le a_0-a_{2m}<0\). The increasing portion ends below zero; thus the whole sequence has the required single crossing. This proves \(L_1\). Before the cutoff, \(S_k\ge\alpha_1>0\); after it, \(S_k=S_m-\sum_{i=k+1}^m\alpha_i\ge S_m>0\). This proves \(L_2\) as well.

## Verification and relation to prior work

The proof is analytic on the infinite domain. The accompanying finite-grid checker corroborates the mass-ratio and endpoint inequalities and the disjunctive left-loadedness condition; it is not the proof of the partial-sum conclusion. The latter follows from the sign pattern and the mean identity. In fact, the same mean identity, Lemma 2.1 of [1], gives \(L_1\Rightarrow L_2\) on the entire domain of Definition 1.2, without requiring the binomial distribution.

The Poisson proof in [1] uses a similar sign-crossing mechanism. For the binomial, [1] establishes the cases \(m=1,2\) and a range \(4\le m\le n/3\); these do not cover all \(n\ge2m\). The published mean-three result addresses only \(m=3\). The partial-sum formulation was also posed on MathOverflow [3]. The full-domain contribution is the binomial ratio and endpoint argument that yields the requisite sign control through the previously uncovered range.

## References

1. R. Fokkink, S. Papavassiliou and C. Pelekis, “On the monotonicity of tail probabilities,” *Probability and Mathematical Statistics* 42 (2022), 133–141, DOI: 10.37190/0208-4147.00050.
2. T. C. Simmons, “A new theorem in probability,” *Proceedings of the London Mathematical Society* 26 (1894), 290–325, DOI: 10.1112/plms/s1-26.1.290.
3. [Simmons' inequality on binomial random variables](https://mathoverflow.net/questions/384456/simmons-inequality-on-binomial-random-variables), MathOverflow question 384456.
