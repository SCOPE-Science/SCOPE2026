# Sharp adjacent-swap likelihood distortion for random parking-function outcomes

## Finding

Let \(p_n\) be the probability distribution on permutations of \(\{1,\ldots,n\}\) induced by the outcome of a uniformly chosen successful classical parking preference vector. For a permutation \(\sigma=(\sigma_1,\ldots,\sigma_n)\), let \(\sigma^{(i)}\) interchange entries in positions \(i\) and \(i+1\).

**Sharp positionwise theorem.** For every integer \(n\ge2\), every \(1\le i\le n-1\), and every \(\sigma\) with \(\sigma_i<\sigma_{i+1}\),

\[
\boxed{\frac1{i+1}\ \le\ \frac{p_n(\sigma^{(i)})}{p_n(\sigma)}\ \le\ \frac{i(n-i)}{i+1}.}
\]

Both bounds are attained for *every* admissible \((n,i)\). The lower extremizer is the increasing permutation \((1,2,\ldots,n)\). An upper extremizer is

\[
(2,3,\ldots,i,\ 1,\ n,\ i+1,i+2,\ldots,n-1),
\]

where the first or final displayed ranges may be empty. The upper extremizer has its adjacent rise at positions \(i,i+1\).

Thus the exact largest increase or decrease for a rise-to-descent adjacent swap is known at *each position*. In particular, the last adjacent position always decreases probability, while for \(n\ge4\) every earlier adjacent position admits a rising swap that *increases* probability. This is a sharp obstruction to monotone decrease of this parking-outcome law along right weak Bruhat covers.

Across all rising adjacent swaps, the smallest ratio is \(1/n\), while the largest is

\[
M_n=\max_{1\le i<n}\frac{i(n-i)}{i+1}
=n+2-\min_{2\le t\le n}\left(t+\frac{n+1}{t}\right).
\]

An optimizing integer \(t=i+1\) is among the two integers bracketing \(\sqrt{n+1}\), with the domain endpoints enforced. Consequently,

\[
M_n=n+2-2\sqrt{n+1}+O(n^{-1/2})\sim n.
\]

For \(n=2,3\) the largest ratio is \(1/2,1\), respectively; the first increasing swap appears at \(n=4\), when the global maximum is \(3/2\).

## Assumptions and scope

The classical parking experiment has \(n\) labeled cars, arriving in increasing car-label order, and \(n\) spots numbered from left to right. Car \(k\) chooses preferred spot \(a_k\in\{1,\ldots,n\}\), taking that spot if free and otherwise the first available spot to its right. Choose uniformly from the \((n+1)^{n-1}\) preference vectors for which every car parks. The resulting permutation \(\sigma_j\) records the car label at spot \(j\). All probabilities under \(p_n\) are strictly positive.

For \(1\le j\le n\) put

\[
\ell_j(\sigma)=\max\{h\in\{1,\ldots,j\}:\sigma_j>\sigma_k\text{ for }j-h+1\le k<j\}.
\]

The empty range is allowed, so \(\ell_j\ge1\). Equivalently, if \(k<j\) is the rightmost preceding index with \(\sigma_k>\sigma_j\), then \(\ell_j=j-k\), taking \(k=0\) when no such index exists. The already established parking-fiber formula is

\[
p_n(\sigma)=\frac{\prod_{j=1}^{n}\ell_j(\sigma)}{(n+1)^{n-1}}.
\]

The finding concerns ordinary classical parking functions, **not** the \(k\)-Naples, MVP, or nonuniform parking rules. The permitted adjacent swap must start from a strict rise; hence it adds exactly one inversion. There are no further restrictions on \(\sigma\).

## Proof

**1. The inherited fiber identity.** Fix an outcome \(\sigma\). The car labeled \(\sigma_j\) has to prefer one of the consecutive spots in the maximal suffix ending at \(j\) filled by smaller-labeled cars; exactly \(\ell_j(\sigma)\) choices give it position \(j\). Multiplying the independent allowed preferences for all labeled cars gives \(\prod_j\ell_j(\sigma)\) preimages. Dividing by the classical count \((n+1)^{n-1}\) yields the displayed probability formula. This identity predates the present result [1,2] and is used as an input, not claimed as new.

**2. An exact swap factorization.** Write \(a=\sigma_i<b=\sigma_{i+1}\), \(A=\ell_i(\sigma)\), and \(B=\ell_{i+1}(\sigma)\). Because the set of preceding entries larger than \(b\) is contained in those larger than \(a\),

\[
1\le A\le i,\qquad A+1\le B\le i+1.
\]

On exchanging \(a,b\), the lengths at positions \(i\) and \(i+1\) become \(B-1\) and \(1\), respectively. At any subsequent position \(j\ge i+2\), the length changes precisely when

\[
a<\sigma_j<b\quad\text{and}\quad
\sigma_j>\max\{\sigma_{i+2},\ldots,\sigma_{j-1}\};
\]

the second condition is vacuous when \(j=i+2\). Define \(\epsilon_j\in\{0,1\}\) to indicate this event. If \(\epsilon_j=1\), the closest larger predecessor moves from \(i+1\) to \(i\), so \(\ell_j\) changes from \(j-i-1\) to \(j-i\). If \(\epsilon_j=0\), it is unchanged. Hence the *exact identity*

\[
\frac{p_n(\sigma^{(i)})}{p_n(\sigma)}=
\frac{B-1}{AB}
\prod_{j=i+2}^n\left(\frac{j-i}{j-i-1}\right)^{\epsilon_j}.
\tag{1}
\]

No independence or asymptotic approximation is used in this factorization.

**3. Uniform sharp upper and lower envelopes.** Because \(B\ge A+1\),

\[
\frac{B-1}{AB}=\frac1A\left(1-\frac1B\right)
\ge\frac1{i+1}.
\]

Indeed \(A\le i\) and \(B\ge A+1\), so the local factor is at least \(1/(A+1)\ge1/(i+1)\). Also, \(A\ge1\) and \(B\le i+1\) give

\[
\frac{B-1}{AB}\le\frac{i}{i+1}.
\]

Every factor in the product of (1) is at least one, and their product is bounded by the complete telescoping product

\[
\prod_{j=i+2}^n\frac{j-i}{j-i-1}=n-i.
\]

Together these bounds prove the theorem's two inequalities. For the increasing permutation, \(A=i\), \(B=i+1\), and all \(\epsilon_j=0\), achieving the lower bound. For the displayed upper witness, \(A=1\), \(B=i+1\), and every \(\epsilon_j=1\) for \(j\ge i+2\), achieving the upper bound. Each equality is thus realized for every \((n,i)\).

**4. Global optimization and monotonicity obstruction.** The smallest positionwise lower bound, over \(1\le i<n\), is \(1/n\). Setting \(t=i+1\), the upper envelope rewrites as \(n+2-t-(n+1)/t\). Its real-valued minimization is at \(t=\sqrt{n+1}\), and convexity implies the integer minimizer lies among the two adjacent integers, accounting for finite endpoints. Taylor expansion on the integer mesh gives error \(O(n^{-1/2})\) relative to the continuous maximum. At \(i=n-1\), the upper bound is \((n-1)/n<1\). If \(n\ge4\) and \(i\le n-2\), then \(i(n-i-1)>1\), hence \(i(n-i)/(i+1)>1\), and the upper witness exhibits an increase. For \(n=3\), both upper bounds are at most one; for \(n=2\), the sole upper bound is one-half. This completes the classification.

## Verification

The companion standalone `checker.py` uses only the Python standard library and exact rational arithmetic. Run `python3 checker.py` from the directory holding the extracted file. It exhaustively checks all permutations through \(n=8\), every rising adjacent swap at each position, equation (1), both claimed bounds, attainment by the explicit witnesses, and the normalization \(\sum_{\sigma\in S_n}\prod_j\ell_j(\sigma)=(n+1)^{n-1}\). Independently, it enumerates all \(n^n\) raw preference tuples through \(n=5\), simulates the parking process, and compares exact fiber counts against the product formula. The program reports `PASS: 475272 exact assertions; independent preference enumeration through n=5`.

These finite calculations check the implementation and special cases, not the general theorem. The all-\(n\) proof is the deterministic factorization and telescoping argument above.

## Relationship to prior work

The **exact mass formula** and its underlying parking-fiber count are classical; see Colmenarejo et al. [2, Proposition 3.3] and their explicit reference to Stanley [4]. Pinsky [1, Theorem 1], available as a preprint from 17 April 2024, applies the formula to the random permutation induced by uniform parking functions and studies global mass extremizers, typical values, positions of last-arriving cars, and left-to-right maxima. In particular, the known global mass maximum at the increasing permutation is **not** the claim here.

The additional claim here is the exact **positionwise sharp likelihood-ratio envelope over all right weak-order covers**, its two extremizer families, and the linear-in-\(n\) largest local increase. The known all-permutation mass formula is necessary but does not itself state or evaluate this optimization. The inspected relevant sections of [1] and [2] do not contain the swap factorization or the sharp bound. Diaconis–Hicks [3] study statistical properties of parking preference vectors, rather than these outcome-permutation edge ratios. Harris et al. [5] use a different MVP parking rule. A separate result for a different parking model cannot establish the present sharp inequalities.

## Limitations

The theorem addresses rising adjacent pairs in the classical parking-outcome permutation; it does **not** compare arbitrary permutation pairs, establish stochastic ordering of inversion counts, or extend automatically to nonuniform preference distributions or modified parking rules. While the inspected literature and mathematical-result searches did not identify an earlier statement of this sharp local optimization, the classical formula is strong enough that an unlocated published extremal consequence could overlap. Scientific priority therefore remains subject to further independent literature examination. The analysis is a self-review, not an independent audit.

## References

1. Ross G. Pinsky, *The distribution on permutations induced by a random parking function*, arXiv:2404.11529 (first public preprint 17 April 2024), Theorem 1 and Corollary 4. https://arxiv.org/abs/2404.11529
2. Laura Colmenarejo, Pamela E. Harris, Zakiya Jones, Christo Keller, Andrés Ramos Rodríguez, Eunice Sukarto and Andrés R. Vindas-Meléndez, *Counting k-Naples parking functions through permutations and the k-Naples area statistic*, arXiv:2009.01124 (first public 2 September 2020), Proposition 3.3. https://arxiv.org/abs/2009.01124
3. Persi Diaconis and Angela Hicks, *Probabilizing parking functions*, Advances in Applied Mathematics 89 (2017), 125–155. https://doi.org/10.1016/j.aam.2017.05.004
4. Richard P. Stanley, *Enumerative Combinatorics, Volume 2*, Cambridge University Press (1999), Exercise 5.49, as cited by [2]; this book was not independently inspected here.
5. Pamela E. Harris, T. Kamau, J. Martínez Mori and A. Tian, *On the outcome map of MVP parking functions*, arXiv:2207.13041 (2022). https://arxiv.org/abs/2207.13041
