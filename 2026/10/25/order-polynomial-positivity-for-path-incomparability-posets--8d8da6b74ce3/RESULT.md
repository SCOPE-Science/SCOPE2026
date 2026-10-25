# Order-polynomial positivity for path-incomparability posets

## Finding
For every integer \(n\ge 1\) and every subset \(E\subseteq\{1,\ldots,n-1\}\), define \(P_{n,E}\) on the naturally labeled elements \(1,\ldots,n\) by declaring \(i\prec j\), for \(i<j\), exactly when either \(j\ge i+2\), or \(j=i+1\) and \(i\notin E\). Thus the incomparability graph is the spanning subgraph of the path consisting of edges \(\{i,i+1\}\) with \(i\in E\). Let \(\Omega_{n,E}(t)\) count order-preserving maps \(P_{n,E}\to\{1,\ldots,t\}\) for positive integers \(t\).

**Theorem.** All ordinary monomial coefficients of \(\Omega_{n,E}(t)\) are nonnegative, and \(n!\,\Omega_{n,E}(t)\) has nonnegative integer coefficients. Consequently, the order polytope \(\mathcal O(P_{n,E})\) is Ehrhart positive with **strictly positive** coefficients, since its Ehrhart polynomial is \(\Omega_{n,E}(t+1)\). The result covers every choice of deleted consecutive comparabilities, in every dimension, including the complement of the zig-zag poset.

More precisely, if \(m_k(E)\) is the number of size-\(k\) matchings in the edge subset \(E\) of the path, then
\[
\Omega_{n,E}(t)=\sum_{k=0}^{\lfloor n/2\rfloor}m_k(E)\binom{t+n-1-k}{n},
\qquad
[t]\Omega_{n,E}(t)=\frac1{n!}\sum_{k=0}^{\lfloor n/2\rfloor}(-1)^k m_k(E)k!(n-1-k)!\ge 0.
\]

## Assumptions and scope
A poset is ordered by the transitive relation displayed above, not merely by adjacent cover edges. Each \(P_{n,E}\) has width at most two, because no three of its elements are pairwise incomparable. The empty poset is also included when applying the hereditary positivity theorem. The order polytope is \(\{x\in[0,1]^n:x_i\le x_j\text{ whenever }i\prec j\}\). No restriction on the components of \(E\), their number, or \(n\) is imposed.

## Proof
**1. Matchings enumerate linear extensions and descents.** In a linear extension, if \(i<j-1\), the element \(i\) must precede \(j\). Hence a permutation representing a linear extension can only differ from the identity by disjoint adjacent transpositions \((i,i+1)\) with \(i\in E\): a nontrivial run of length three is impossible because its first and third labels have prescribed relative order. Conversely every set of pairwise nonincident such transpositions is a valid extension. Each transposition creates exactly one descent and disjoint transpositions do not create further descents. Therefore the descent-generating polynomial of linear extensions is \(\sum_km_k(E)z^k\). Stanley's order-polynomial/linear-extension formula gives the first displayed identity.

**2. Linear coefficient is an alternating matching sum.** The product expression
\[
\binom{t+n-1-k}{n}=\frac1{n!}\prod_{r=-k}^{n-1-k}(t+r)
\]
contains exactly one zero factor. The derivative at zero is \((-1)^k k!(n-1-k)!/n!\), proving the second identity.

**3. The alternating terms are nonincreasing.** Define \(a_k=m_k(E)k!(n-1-k)!\) and take \(a_k=0\) beyond the matching number. Count ordered pairs consisting of a \((k+1)\)-edge matching and a distinguished edge of that matching. On deleting the distinguished edge one obtains a \(k\)-matching, with at most \(|E|-k\le n-1-k\) candidate edges available to insert. Thus
\[
(k+1)m_{k+1}(E)\le (n-1-k)m_k(E),
\qquad a_{k+1}\le a_k.
\]
Consequently the alternating sum \(a_0-a_1+a_2-a_3+\cdots\) is nonnegative by grouping successive terms in pairs (and, when applicable, retaining the final nonnegative term). Thus \([t]\Omega_{n,E}(t)\ge0\) for every \(n,E\).

**4. Heredity upgrades one coefficient to all coefficients.** Every induced subposet of \(P_{n,E}\), relabeled in the increasing order of its original labels, again has the form \(P_{r,E'}\): originally nonadjacent indices remain comparable, while consecutive indices in the subsequence may or may not be incomparable. Thus the class is closed under taking lower ideals and complementary upper filters. Theorem 3.4 of Ferroni–Morales–Panova (2026), explicitly used here as a prior theorem, states that such a hereditary class with nonnegative order-polynomial linear coefficients has nonnegative coefficients in all degrees, with integer coefficients after factorial scaling. Applying that theorem proves \(n!\Omega_{n,E}(t)\in\mathbb Z_{\ge0}[t]\).

**5. Strict Ehrhart positivity.** For a nonempty poset, \(\Omega_{n,E}(0)=0\) and its leading coefficient is the positive number of linear extensions divided by \(n!\). Shifting its nonnegative-coefficient polynomial to \(t+1\) makes the coefficient of every power \(t^j\), including \(0\le j\le n\), strictly positive. Stanley's order-polytope identity then identifies the shift with the Ehrhart polynomial. The empty poset gives constant Ehrhart polynomial \(1\) separately.

## Verification
The standalone Python 3 program `verify.py` uses only the standard library and exact integer arithmetic. It exhaustively checks all \(1023\) labeled choices \((n,E)\) with \(1\le n\le10\), compares the alternating linear-coefficient identity, confirms termwise monotonicity of \(a_k\), tests every ordinary order-polynomial coefficient, and independently compares \(381\) small order-map counts by direct enumeration with the reconstructed polynomial. Its successful output is:

`EXACT_OK path_cases=1023 independent_counts=381 zero_linear=[(2, 1), (3, 3)]`

These finite checks support the proof but do not establish the theorem for arbitrarily large \(n\); the universal argument is in steps 1–5.

## Relationship to prior work
Ferroni, Morales and Panova, *Skew shapes, Ehrhart positivity, and beyond*, arXiv:2503.16403 (first public 20 March 2025), published 2026, proves the hereditary linear-term reduction used in step 4. Their Section 7.1 formulates width-two positivity as Conjecture 7.1 and specifically reports that the complement zig-zag family has been computationally checked through \(n\le200\), without an all-dimensional proof. Their main positivity theorem covers skew **cell** posets, while their Section 7 explicitly distinguishes the width-two posets associated with skew diagrams. This theorem gives a structural infinite-family case of that conjecture and includes an all-dimensional proof for their complement zig-zag example. The matching formula uses the classical linear-extension expansion of order polynomials, also not claimed new.

Previously established results proving order-polytope Ehrhart positivity for dimensions at most \(13\) only address finitely many dimensions and do not imply the all-dimensional statement. This contribution is the matching-term monotonicity certificate for the whole hereditary family together with its consequence via the already-published meta-theorem.

## Limitations
This is not a proof of the width-two conjecture for arbitrary incomparability graphs, nor an independent proof of the published hereditary positivity theorem. Possible equivalent prior results under the terminology of naturally labeled unit-interval orders, near-chain posets, or forbidden-adjacent-comparison posets remain a historical-priority risk. Independent audit has not been performed.

## References
1. L. Ferroni, A. H. Morales and G. Panova, *Skew shapes, Ehrhart positivity, and beyond*, arXiv:2503.16403 (submitted 20 March 2025), *Proceedings of the London Mathematical Society* **133** (2026), e70204, https://doi.org/10.1112/plms.70204. Theorem 3.4 and Section 7.1, Remarks 7.2–7.3. Open full HTML: https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/plms.70204.
2. R. P. Stanley, *Two poset polytopes*, *Discrete & Computational Geometry* **1** (1986), 9–23, and *Enumerative Combinatorics*, vol. 1, 2nd ed. (2012): order polytopes and linear-extension expansions.
3. F. Liu, W. Xin and A. Zhang, *Order Polytopes of Dimension \(\le13\) are Ehrhart Positive*, arXiv:2412.07164 (2024); https://arxiv.org/abs/2412.07164.
