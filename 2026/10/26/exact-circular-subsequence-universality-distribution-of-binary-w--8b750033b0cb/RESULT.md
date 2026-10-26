# Exact circular subsequence-universality distribution of binary words

## Finding

Fix the **binary alphabet** \(\Sigma=\{0,1\}\), even when the word itself is constant. A word is \(k\)-subsequence-universal when every element of \(\Sigma^k\) occurs as a scattered subsequence. For a finite word \(w\), let \(\zeta(w)\) be the largest \(k\) for which **one common cyclic rotation** of \(w\) is \(k\)-subsequence-universal. The rotation is allowed to depend on \(w\), but not on the target subsequence. Let \(C_{n,k}\) be the number of **indexed**, not rotation-identified, binary words \(w\) of length \(n\ge1\) with \(\zeta(w)=k\).

Then for every positive integer \(n\), \(C_{n,0}=2\), and, for \(1\le k\le\lfloor n/2\rfloor\),

\[
C_{n,k}=2^k\left[\binom{n-k-1}{k}+2\binom{n-k-1}{k-1}\right]-2\mathbf1_{\{n=2k\}}.
\]

All other \(C_{n,k}\) vanish. The equivalent exact bivariate generating function is

\[
\boxed{\sum_{n\ge1}\sum_{k\ge0}C_{n,k}z^nu^k
=\frac{z(1+4zu)}{1-z-2uz^2}+\frac{z}{1-z}-\frac{2uz^2}{1-uz^2}.}
\]

In particular the number of length-\(2k\) words attaining the largest possible circular index \(k\) is \(2^{k+1}-2\); for odd length \(2k+1\), the corresponding count is \((2k+1)2^k\), whenever \(k\ge1\). The first coefficient rows, ordered by \(k=0,1,\dots\), are: \(n=1:(2)\), \(n=2:(2,2)\), \(n=3:(2,6)\), \(n=4:(2,8,6)\), \(n=5:(2,10,20)\), \(n=6:(2,12,36,14)\).

## Assumptions and scope

An indexed binary word is a choice of one symbol at each of \(n\) positions, and two cyclic shifts are counted as different source words when they have different indexed strings. Complementary words are counted separately. In the present fixed-alphabet convention, a constant word has \(\zeta=0\); it would have index \(n\) if its own one-letter support were used as alphabet. The theorem refers to one common rotation for all target subsequences; it does not count the *adaptive-cut* notion in which each target may choose a different rotation.

For a word \(w=w_0\cdots w_{n-1}\), introduce its cyclic transition set
\[
E(w)=\{\{i,(i+1)\bmod n\}: w_i\ne w_{(i+1)\bmod n}\}.
\]
For \(n=2\), the two oriented boundary occurrences are distinguished, though they have the same endpoints and so cannot both belong to a matching. For \(n=1\), the transition set is empty. The cyclic transition graph has vertices representing positions and edges the unequal adjacent pairs.

## Proof

**Lemma 1 (matching characterization).** The circular universality index \(\zeta(w)\) equals the maximum number \(\nu(w)\) of pairwise vertex-disjoint cyclic transition edges.

For the upper bound, any \(k\)-universal rotation can be cut into \(k\) consecutive nonempty blocks that each contain both binary letters (the standard arch-factorization criterion for subsequence universality). Every such block contains two adjacent unequal letters; taking one transition edge from each of the disjoint blocks produces a matching among the cyclic transition edges, hence \(k\le\nu(w)\). Conversely, choose any \(k\) vertex-disjoint cyclic transition edges. They specify \(k\) disjoint two-letter blocks, each containing both letters. A cyclic cut between two such blocks, or at their common boundary when they cover the entire cycle, makes the blocks appear in a linear rotation in the same cyclic order. That rotation is a superword of a concatenation of \(k\) complete-alphabet blocks and is therefore \(k\)-universal. Thus \(\zeta(w)=\nu(w)\). This also covers \(k=0\) and the two-position cycle.

**Lemma 2 (runs of transitions).** Set \(e_i=1\) if \(w_i\ne w_{(i+1)\bmod n}\), and \(e_i=0\) otherwise. A binary cycle yields a transition vector \(e\) with an even number of ones, and each such vector determines exactly two words (initial symbol \(0\) or \(1\)). If \(e\) has at least one zero, its maximal cyclic runs of ones are separated by zeros. A run with \(\ell\ge0\) ones contributes exactly \(\lceil\ell/2\rceil\) to the matching number, where a zero-length run contributes zero. The transition graph is a disjoint union of paths, each of \(\ell\) edges; the matching number of such a path is \(\lceil\ell/2\rceil\). If all \(e_i=1\), parity forces \(n\) even, and the transition graph is an even cycle with matching number \(n/2\).

**Weighted enumeration.** Mark each occurrence of a zero in the transition vector as the beginning of a block \(0 1^\ell\), with \(\ell\ge0\). A block has length \(\ell+1\) and index contribution \(\lceil\ell/2\rceil\). For a parity-marker \(v\in\{1,-1\}\), its generating function is

\[
B_v(z,u)=\sum_{\ell\ge0}z^{\ell+1}v^\ell u^{\lceil\ell/2\rceil}
=\frac{z+vuz^2}{1-uz^2}.
\]

For vectors with at least one zero, cyclic sequences of these blocks account for position-labeled transition strings via
\[
F_v(z,u)=z\frac{\partial}{\partial z}\sum_{j\ge1}\frac{B_v(z,u)^j}{j}
=z\frac{\partial}{\partial z}\bigl[-\log(1-B_v(z,u))\bigr].
\]
Indeed, a transition vector of length \(n\) with \(j\) zeros has \(n\) choices of indexed starting position but \(j\) choices of which zero begins its block list, giving the factor \(n/j\) at the coefficient level. This remains valid for periodically repeating block lists, since the count is of indexed words rather than rotation orbits. Combining the contributions \(v=1\) and \(v=-1\) removes vectors with an odd number of ones and multiplies each even-parity vector by two, exactly the number of binary lifts. The all-ones vectors, possible only for positive even lengths, contribute separately
\[
2\sum_{j\ge1}z^{2j}u^j=\frac{2uz^2}{1-uz^2}.
\]

Since \(1-B_1=(1-z-2uz^2)/(1-uz^2)\) and \(1-B_{-1}=(1-z)/(1-uz^2)\), direct differentiation gives
\[
F_1=\frac{z(1+4uz)}{1-z-2uz^2}-\frac{2uz^2}{1-uz^2},\qquad
F_{-1}=\frac{z}{1-z}-\frac{2uz^2}{1-uz^2}.
\]
Thus \(F_1+F_{-1}+2uz^2/(1-uz^2)\) is precisely the claimed generating function.

Finally, for \(j\ge0\), the coefficient of \(z^mu^j\) in \((1-z-2uz^2)^{-1}\) is \(2^j\binom{m-j}{j}\) whenever \(m\ge2j\), and zero otherwise. Applying this to the two numerator terms, adding the constants and subtracting the all-ones correction proves the explicit coefficient formula for every \(n\ge1\). At \(n=2k\), the only nonzero binomial term is the second, giving \(2^{k+1}-2\); at \(n=2k+1\) they combine to \((2k+1)2^k\). The proof is exact and does not extrapolate from experiments.

## Verification

The accompanying `verify.py` uses three separately specified computations: a direct greedy arch count over every rotation, a maximum-matching calculation from cyclic runs of transitions, and the closed coefficient formula. It exhaustively compares them for all \(\sum_{n=1}^{17}2^n=262142\) binary words of lengths one through seventeen, including constant and alternating boundary cases. A separate integer-polynomial recurrence verifies coefficients of the bivariate rational identity through length \(256\), with row sums \(2^n\). Run `python3 verify.py` with only the Python standard library; successful completion prints the documented marker. The proof above, not this finite computation, establishes the all-length result.

## Relationship to prior work

Barker, Fleischmann, Harwardt, Manea, and Nowotka (2020) introduced scattered-factor circular universality and proved the fundamental arch characterization and comparisons with universality of powers. Fleischmann, Germann, and Nowotka (2021) studied the remainders of arch factorizations and provided algorithms for the circular index. Schnoebelen and Veron (2023) gave an arch-jumping algorithm for arbitrary alphabets and compressed words. These results explain how to **compute the index of one input** and imply the existence of disjoint rich blocks. The present claim concerns a different, all-length enumeration problem: the full indexed binary distribution by that circular index. Its explicit matching reduction, parity-weighted cycle enumeration, and bivariate generating function do not follow as a stated numerical distribution from those cited results; an undiscovered equivalent formulation remains possible.

## Limitations

The result is specific to a fixed binary alphabet; for larger alphabets a rich block requires more than a single unequal adjacent pair. It counts indexed words, not necklaces or bracelets. It does not address the stronger adaptive-cut notion that permits a separate cut for every target subsequence. The enumeration may have an equivalent formulation in other combinatorial enumeration or symbolic-dynamics literature that has not been located. No independent expert mathematical validation is claimed.

## References

1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, D. Nowotka, *Scattered Factor-Universality of Words*, DLT 2020; arXiv:2003.04629, https://arxiv.org/html/2003.04629v1 (initial public version 2020-03-10).
2. P. Fleischmann, S. B. Germann, D. Nowotka, *Scattered Factor Universality — The Power of the Remainder*, arXiv:2104.09063, https://arxiv.org/pdf/2104.09063 (initial public version 2021-04-19).
3. P. Schnoebelen, J. Veron, *On Arch Factorization and Subword Universality for Words and Compressed Words*, WORDS 2023, pp. 274–287; arXiv:2304.11932, https://arxiv.org/abs/2304.11932 (initial public version 2023-04-24).
