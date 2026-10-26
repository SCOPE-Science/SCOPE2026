# A sharp positional-gap law for inversions under increasing-subsequence conditioning

## Finding

Let \(n\geq k\geq2\) be integers and let \(\Pi\) be a uniformly random permutation of \(\{1,\ldots,n\}\). Write \(I=\sum_{1\leq u<v\leq n}\mathbf 1\{\Pi(u)>\Pi(v)\}\) for the number of inversions. Fix a strictly increasing position set \(S=(s_1,\ldots,s_k)\) and condition on
\[
E_S=\{\Pi(s_1)<\cdots<\Pi(s_k)\}.
\]
Define the interior empty-position gaps \(d_j=s_{j+1}-s_j-1\), \(1\leq j<k\), and their weighted total
\[
G(S)=\sum_{j=1}^{k-1}j(k-j)d_j.
\]
Then the following **exact positional-gap law** holds for all \(n,k,S\):
\[
\boxed{\mathbb E[I\mid E_S]=\frac{n(n-1)}4-\frac{k(k-1)}4-\frac{G(S)}{k+1}.}
\tag{1}
\]
In particular, the exact sharp range over all position sets of size \(k\) is
\[
\boxed{\frac{n(n-1)}4-\frac{k(k-1)}4-\frac{\lfloor k^2/4\rfloor(n-k)}{k+1}
\ \leq\ \mathbb E[I\mid E_S]\ \leq\ \frac{n(n-1)}4-\frac{k(k-1)}4.}
\tag{2}
\]
The upper endpoint holds precisely when the selected positions are consecutive. If \(n>k\), the lower endpoint holds precisely when no unused position lies outside the selected range and every interior empty position lies in a central gap \(j\) maximizing \(j(k-j)\) (one central gap for even \(k\), two for odd \(k\)); when \(n=k\), both endpoints agree.

Let \(\mu_{n,k}\) denote the law obtained by selecting \(S\) uniformly from all \(k\)-subsets of positions and then sampling \(\Pi\) uniformly conditional on \(E_S\). Then
\[
\boxed{\mathbb E_{\mu_{n,k}}I=\frac{n(n-1)}4-\frac{k(k-1)(2n+k+3)}{12(k+1)}.}
\tag{3}
\]
If \(Z_{n,k}\) denotes the number of increasing subsequences of length \(k\) in a uniform permutation, equivalently
\[
\boxed{\operatorname{Cov}(Z_{n,k},I)=-\frac{\binom nk}{k!}\,\frac{k(k-1)(2n+k+3)}{12(k+1)}<0.}
\tag{4}
\]
Equations (2)--(4) are consequences of the single positional-gap identity (1).

## Assumptions and scope

Permutations are sampled uniformly from the full symmetric group. The position subset is deterministic in (1)--(2), and it is uniformly sampled independently before conditioning in (3). The conditioning event has probability \(1/k!>0\) for every eligible set. Inversion pairs always use positions, not permutation cycles or inverse images. The theorem is finite and exact; it does not assume that \(k\) stays fixed as \(n\) grows.

## Proof

**Step 1: expected comparisons.** Every inversion indicator of an unrestricted uniform permutation has expectation \(1/2\), giving \(\mathbb E I=n(n-1)/4\). Conditional on \(E_S\), the values at the selected positions form the increasing ordering of a uniformly selected \(k\)-subset of values, while the remaining values are uniformly assigned to unselected positions. Each of the \(\binom k2\) pairs with both positions selected is certainly increasing, so its contribution to the change in expected inversions is \(-1/2\). Every comparison between two unselected positions remains fair and contributes no change.

For an unselected position \(u\), the relative position of its value among the \(k\) selected values is uniformly distributed among the \(k+1\) possible gaps. Therefore, against selected rank \(a\), the probability of \(\Pi(u)>\Pi(s_a)\) is \((k+1-a)/(k+1)\), and of \(\Pi(u)<\Pi(s_a)\) is \(a/(k+1)\). There are \(s_a-a\) unselected positions before \(s_a\) and \(n-s_a-(k-a)\) afterward. Relative to the unrestricted expectation \(1/2\), the net contribution from these comparisons is
\[
\frac{k+1-2a}{2(k+1)}\bigl[(s_a-a)-(n-s_a-k+a)\bigr].
\]
Summing this over \(1\leq a\leq k\) gives
\[
-\frac1{k+1}\left[\sum_{1\leq a<b\leq k}(s_b-s_a)-\sum_{1\leq a<b\leq k}(b-a)\right]
=-\frac1{k+1}\sum_{j=1}^{k-1}j(k-j)(s_{j+1}-s_j-1).
\]
The second equality follows because each interior excess gap \(d_j\) occurs in exactly \(j(k-j)\) pairs spanning the gap. Adding the contribution \(-\binom k2/2\) of selected-selected comparisons proves (1).

**Step 2: sharp optimization.** The \(k+1\) nonnegative numbers \(s_1-1\), \(d_1,\ldots,d_{k-1}\), and \(n-s_k\) sum to \(n-k\). Every interior coefficient \(j(k-j)\) is positive and at most \(\lfloor k^2/4\rfloor\). Thus \(0\leq G(S)\leq\lfloor k^2/4\rfloor(n-k)\). Equality on the left requires all interior gaps to vanish. For \(n>k\), equality on the right requires both exterior gaps to vanish and all interior empty positions to be allocated to the coefficient-maximizing central gaps. These allocations exist and yield (2).

**Step 3: uniform marked-position mixture.** Choosing a uniform \(k\)-subset \(S\) is equivalent to choosing uniformly a weak composition of \(n-k\) into the \(k+1\) exterior/interior gaps. Each gap consequently has mean \((n-k)/(k+1)\). Since
\[
\sum_{j=1}^{k-1}j(k-j)=\frac{k(k-1)(k+1)}6,
\]
we obtain \(\mathbb E_S G(S)=k(k-1)(n-k)/6\). Averaging (1) and simplifying proves (3).

**Step 4: the covariance identity.** Let \(U_n\) be uniform measure and put \(Z_{n,k}(\pi)=\sum_{|S|=k}\mathbf1_{E_S}(\pi)\). Since \(U_n(E_S)=1/k!\), the mixture is the exact size-bias tilt
\[
\frac{\mathrm d\mu_{n,k}}{\mathrm d U_n}(\pi)
=\frac{k!}{\binom nk}Z_{n,k}(\pi)
=\frac{Z_{n,k}(\pi)}{\mathbb E_{U_n}Z_{n,k}}.
\]
Consequently
\[
\operatorname{Cov}_{U_n}(Z_{n,k},I)
=\mathbb E_{U_n}Z_{n,k}\bigl(\mathbb E_{\mu_{n,k}}I-\mathbb E_{U_n}I\bigr).
\]
Using \(\mathbb E_{U_n}Z_{n,k}=\binom nk/k!\) and (3) yields (4); all factors in its magnitude are positive.

## Verification

The standalone program `verify_gap_law.py` uses exact rational arithmetic and enumerates **every** permutation for each \(2\leq n\leq7\), with every eligible selected-position set \(S\) and every \(2\leq k\leq n\). It independently computes inversion sums conditioned on the increasing event, checks (1), checks both attained extremes in (2), averages over position sets to verify (3), and independently computes the covariance in (4). The run checks \(1,4,11,26,57,120\) distinct marked-position conditions for sizes \(2,3,4,5,6,7\), respectively, and returns `PASS`. The program and its exact output are included. These exhaustive small-size computations corroborate, but do not replace, the all-size proof.

For a separate hand-check at \(n=8\), \(k=4\), consecutive marks \(S=(2,3,4,5)\) give \(\mathbb E[I\mid E_S]=11\), whereas split marks \(S=(1,2,7,8)\) give \(39/5\). Under uniform random marks, (3) gives \(47/5\). The sharp difference between layouts is \(16/5\), matching \(\lfloor 4^2/4\rfloor(8-4)/(4+1)\).

## Relationship to prior work

Pinsky's 2004 preprint (arXiv:math/0407353) defines the same increasing-subsequence count and exactly the same uniform marked-position mixture \(\mu_{n,k}\), and investigates laws of large numbers and total-variation approximation for that mixture. In the inspected introduction, definitions, and proof setup, it does **not** state a positional-gap law or the mean inversion formulas here. Janson, Nakamura and Zeilberger (arXiv:1312.3955; Journal of Combinatorics 2015) study mixed moments of permutation-pattern counts and provide general computational techniques, including several explicit fixed-length examples. Their framework overlaps with the covariance corollary, but the examined exact-moment examples do not state the all-\(k\) conditional positional law or the sharp central-gap placement rule. Even-Zohar (arXiv:1811.07883) studies asymptotic fluctuations of fixed-length pattern profiles rather than prescribed increasing positions. Thus the principal distinction is the **all-size, position-resolved conditional identity with sharp geometry**, not a claim that mixed pattern moments were previously unstudied.

The closest searched research records concerned inversion-indicator precision geometry and cycle-count/inversion covariances; neither treats conditioning on an increasing marked position set. General methods for pattern mixed moments may, in principle, be adapted to recover a part of (4), but that is not the same as an already stated or directly implied sharp positional optimization theorem.

## Limitations

The claim does not assert stochastic domination of the complete inversion-count distribution, nor monotonicity at every fixed inversion number. It concerns only the conditional first moment and the stated unconditional covariance. The conditioning is on *one prescribed increasing subsequence*, not on its being longest or unique. Although relevant accessible papers and record searches were checked, historical priority beyond the inspected sources remains unverified independently; especially, general mixed-pattern moment methods might contain an unrecognized specialization. No claims of independent formal verification or external certification are made.

## References

1. R. G. Pinsky, *Law of large numbers for increasing subsequences of random permutations and an approximation result for the uniform measure*, first posted 21 July 2004, arXiv:math/0407353, especially the definition of \(\mu_{n,k}\) and Proposition 1. https://arxiv.org/abs/math/0407353
2. S. Janson, B. Nakamura, and D. Zeilberger, *On the Asymptotic Statistics of the Number of Occurrences of Multiple Permutation Patterns*, first posted 13 December 2013, arXiv:1312.3955, especially the mixed-moment discussion. https://arxiv.org/abs/1312.3955
3. C. Even-Zohar, *Patterns in Random Permutations*, arXiv:1811.07883, especially the fixed-pattern-profile asymptotic framework. https://arxiv.org/abs/1811.07883
