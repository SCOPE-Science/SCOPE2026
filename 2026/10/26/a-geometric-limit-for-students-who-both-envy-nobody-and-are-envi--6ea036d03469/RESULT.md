# A geometric limit for students who both envy nobody and are envied by nobody

## Finding
For every integer \(n\ge 1\), assign \(n\) indivisible houses to \(n\) students by random serial dictatorship (RSD), with independently uniform complete strict preferences. Let \(C_n\) count students who simultaneously (i) receive their overall top-choice house, and (ii) are not envied by any other student. For every set \(T\) of \(k\) distinct serial positions, the exact joint-event probability is
\[
\Pr(\text{all positions in }T\text{ satisfy (i) and (ii)})=\frac{k!}{n^k}.
\]
Hence the joint indicators are exchangeable under permutations of serial positions, despite either marginal criterion being position-sensitive. In particular, for \(0\le j\le n\),
\[
\Pr(C_n=j)=\binom nj\sum_{r=0}^{n-j}(-1)^r\binom{n-j}{r}\frac{(j+r)!}{n^{j+r}},
\]
and
\[
\mathbb E[z^{C_n}]=\sum_{k=0}^n\frac{(n)_k}{n^k}(z-1)^k,\quad
\mathbb E C_n=1,\quad\operatorname{Var}(C_n)=2\left(1-\frac1n\right).
\]
As \(n\to\infty\), \(C_n\) converges in law to the geometric variable \(G\) supported on \(\{0,1,2,\ldots\}\) with \(\Pr(G=j)=2^{-j-1}\). The expected size of the union of the top-choice and unenvied sets is exactly \((n-1)/2+H_n\), where \(H_n=\sum_{r=1}^n1/r\).

## Assumptions and scope
The population and supply each have size \(n\ge1\), houses have unit capacity, and every student's strict ranking is independent and uniformly distributed over all \(n!\) permutations. RSD allocates to the next student her favorite remaining house in a fixed order, or equivalently an order independently randomized before preferences. A student envies another exactly when she strictly prefers the latter's assigned house over her own. In complete unit-capacity assignment, receiving the first choice is equivalent to envying nobody, since every house is assigned.

## Proof
Fix a serial order and let \(T\subseteq\{1,\ldots,n\}\) be a designated set of protected positions. Write \(r_j=n-j+1\) for the number of unallocated houses at position \(j\) and \(t_j=|T\cap\{1,\ldots,j-1\}|\) for the count of earlier protected positions. Each student's ranking is independent of all preceding rankings and house assignments.

If \(j\in T\), its candidate must receive her overall favorite house. Conditional on the history, the preferred house among all \(n\) is uniformly distributed; the chance it remains available equals \(r_j/n\). This automatically prevents the new student from envying all prior protected students. If \(j\notin T\), each previously protected student must remain unenvied by student \(j\); this requires the best of \(r_j\) still-available houses to rank above the \(t_j\) protected houses already assigned. By symmetry of the independent uniform ranking, this happens with probability \(r_j/(r_j+t_j)\). Every designated student's subsequent protection is thus encoded by independent conditional factors, giving
\[
P_n(T)=\prod_{j\in T}\frac{r_j}{n}\prod_{j\notin T}\frac{r_j}{r_j+t_j}.
\]
This probability depends only on \(k=|T|\). To see this, exchange protected status between two adjacent positions \(j\) and \(j+1\), with \(t\) protected positions preceding \(j\) and \(r=r_j\). When \(j\) is protected and \(j+1\) is not, their two factors multiply to \((r/n)((r-1)/(r+t))\). When \(j\) is not protected and \(j+1\) is protected, they multiply to \((r/(r+t))((r-1)/n)\), exactly equal. Every other position's factor is unchanged. Adjacent transpositions move any \(k\)-element protected subset into the last \(k\) positions, where its product is \(k!/n^k\). The claimed exact joint probabilities follow, including \(k=0\) and \(n=1\).

For each \(k\), summing the joint inclusion probabilities over all \(k\)-subsets gives \(\mathbb E\binom{C_n}{k}=\binom nk k!/n^k=(n)_k/n^k\). Expanding \(z^{C_n}=(1+(z-1))^{C_n}\) produces the stated probability generating function. Binomial inversion gives the displayed mass formula. The first two factorial moments are \(1\) and \(2(1-1/n)\), yielding the stated mean and variance. For every fixed \(z\) with \(0<z<1\), the generating function tends to the absolutely summable geometric series \(\sum_{k=0}^\infty(z-1)^k=1/(2-z)\), by dominated convergence since \(0\le(n)_k/n^k\le1\). This is the pgf of \(G\); pgf convergence implies weak convergence on nonnegative integers.

Finally, previously established expected counts are \((n+1)/2\) for the top-choice set and \(H_n\) for the unenvied set. Subtracting the new exact intersection expectation \(1\) gives \((n-1)/2+H_n\) for the expected union.

## Verification
`CHECK.py` uses exact rational arithmetic for all joint-inclusion event formulas through \(n=12\), inverts the complete law, and checks mean and variance against the theorem. Separately, it exhaustively enumerates independent strict-ranking profiles for \(n=1,2,3,4\), including all \(24^4=331776\) four-student profiles, independently simulating the RSD allocation and both envy properties. These are finite consistency checks; the theorem for arbitrary \(n\) follows from the preceding proof.

## Relationship to prior work
Ortega, Ziegler, Arribillaga, and Zhao (2026, Proposition 3) establish the expectation \(H_n\) of unenvied students under RSD, as well as the expected \((n+1)/2\) top-choice recipients. Their work develops the analogous DA expectation via a coupon-collector representation but does not derive the RSD **intersection** distribution, exchangeability, or the geometric limit presented here. Existing exact coupon-singleton distributions (Myers and Wilf, 2003) and the previously established distributional bridge between RSD unenvied counts and coupon singletons are separate results, not claimed here. The new event combines both envy directions and yields a different tight, geometric limiting count.

## Limitations
Randomization is essential. The exchangeability concerns doubly qualified *serial positions*, not the marginal indicator of receiving a top choice or that of remaining unenvied alone. The limit does not assert that the count is approximately Poisson; its variance tends to \(2\), not \(1\). Correlated preferences, unequal numbers of students and houses, or different assignment mechanisms are outside the theorem. The priority of unindexed equivalent statements has not been independently established, and no independent scientific audit has been performed.

## References
1. J. Ortega, G. Ziegler, R. P. Arribillaga, G. Zhao, *The Distribution of Envy in Matching Markets*, Economics Letters **263** (2026), 112936, DOI: 10.1016/j.econlet.2026.112936; open version arXiv:2603.23385 (2026-03-24). Article first publicly available online 2026-03-12 according to institutional publication record.
2. A. N. Myers and H. S. Wilf, *Some New Aspects of the Coupon-Collector's Problem*, SIAM Journal on Discrete Mathematics **17** (2003), 1–17, DOI: 10.1137/S0895480102403076; open arXiv:math/0304229 (2003-04-16), section 4.
3. J. Ortega, G. Ziegler, R. P. Arribillaga, G. Zhao, *Identifying and Quantifying (Un)Improvable Students*, arXiv:2407.19831 (first posted 2024-07-29).
