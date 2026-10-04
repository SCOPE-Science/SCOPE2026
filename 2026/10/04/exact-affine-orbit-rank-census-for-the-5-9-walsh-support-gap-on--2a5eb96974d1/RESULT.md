# Exact affine-orbit rank census for the \(5,9\) Walsh-support gap on \((\mathbb Z/2\mathbb Z)^4\)
## Finding
Let \(G=(\mathbb Z/2\mathbb Z)^4\). Identify \(G\) with the four-bit vectors \(0,1,\ldots,15\), and write the Walsh--Fourier matrix as
\[
W_{u,v}=(-1)^{u\cdot v},\qquad u,v\in G.
\]
There are exactly two affine orbits of five-element subsets of \(G\). Representatives and orbit sizes are
\[
S_1=\{{0,1,2,3,4\}},\quad |\operatorname{{Orb}}(S_1)|=1680,
\]
and
\[
S_2=\{{0,1,2,4,8\}},\quad |\operatorname{{Orb}}(S_2)|=2688.
\]
These orbit sizes sum to \(4368=\binom{{16}}{{5}}\), so they exhaust all five-point supports.

For a seven-character set \(T\subset G\), put \(R_i(T)=W[T,S_i]\). The exact census is:

- For \(S_1\), exactly \(3248\) of the \(11440=\binom{{16}}{{7}}\) sets \(T\) satisfy \(\operatorname{{rank}}R_1(T)<5\). Their rank distribution is \(3200\) of rank \(4\) and \(48\) of rank \(3\). Among them, \(3184\) have row space containing a coordinate functional, so every kernel vector has at least one zero coefficient on \(S_1\). The remaining \(64\) contain no coordinate functional in the row space, but their row space contains at least one Walsh row indexed outside \(T\), so every kernel vector has at least eight Fourier zeros.
- For \(S_2\), exactly \(160\) choices of \(T\) have rank below \(5\); all have rank \(4\), and every one has a coordinate functional in its row space.

Therefore no nonzero \(f:G\to\mathbb C\) satisfies simultaneously
\[
|\operatorname{{supp}} f|=5,\qquad |\operatorname{{supp}}\widehat f|=9.
\]

## Assumptions and scope
The Fourier transform is the unnormalized Walsh transform
\[
\widehat f(u)=\sum_{{v\in G}} f(v)(-1)^{{u\cdot v}}.
\]
Only support cardinalities matter, so normalization does not change the statement. The coefficients of \(f\) are arbitrary complex numbers; this is not a Boolean-valued or indicator-only result. The affine action on \(G\) preserves time-support size and, through the dual linear action together with character phases from translations, preserves Fourier-support size.

## Proof
Fix a five-point support \(S\) and a seven-character set \(T\). A coefficient vector \(c\in\mathbb C^S\) gives Fourier zeros on every character in \(T\) exactly when
\[
W[T,S]c=0.
\]
Let \(K=\ker W[T,S]\). To obtain exact time support \(S\), every coordinate functional on \(K\) must be nonzero at the chosen vector. To obtain exactly the seven Fourier zeros in \(T\), every Walsh row indexed by \(G\setminus T\) must also be nonzero on that vector.

For any linear functional \(\ell\) on \(\mathbb C^S\), \(\ell\) vanishes identically on \(K\) if and only if its coefficient vector lies in the row space of \(W[T,S]\). Hence an exact \(5\)-by-\(9\) support pair exists for \(S,T\) if and only if all three conditions hold: \(\operatorname{{rank}}W[T,S]<5\); no coordinate vector belongs to that row space; and no Walsh row indexed outside \(T\) belongs to that row space. If none of these finitely many functionals vanishes identically on \(K\), their kernels are finitely many proper subspaces of the nonzero complex vector space \(K\), so their union cannot cover \(K\); a vector avoiding all of them exists.

It remains to inspect finitely many row spaces. Affine translations, coordinate permutations, and elementary transvections partition all five-point supports into the two explicit orbits above. The exact row-space census for the two representatives is the one stated in the Finding. Every rank-deficient case violates at least one of the two nonvanishing conditions, proving the nonexistence statement.

## Verification
The accompanying `verify_f2_4_5_9.py` is a standalone standard-library verifier. It constructs the stated affine generators, performs breadth-first orbit enumeration, and checks that the two support orbits are disjoint and have total size \(\binom{{16}}{{5}}\). For each representative it enumerates all \(\binom{{16}}{{7}}=11440\) seven-frequency sets.

A modular rank calculation modulo the prime \(1000003\) is used only as a sound full-rank filter: rank \(5\) modulo that prime exhibits a nonzero integer minor and therefore proves rank \(5\) over \(\mathbb Q\). Every case that survives the filter is recomputed by exact rational row reduction with `fractions.Fraction`; coordinate and extra-row membership in the exact row space are then checked over \(\mathbb Q\). Thus no floating-point tolerance enters the certificate. The packaged replay prints the two orbit sizes, the rank distributions and obstruction counts above, followed by `VERIFY_OK`.

## Relationship to prior work
Krahmer, Pfander and Rashkov formulate an exact rank criterion for prescribed Fourier support pairs (their Lemma 3.4) and present Figure 2 as numerical evidence for the achieved and non-achieved pairs for every finite Abelian group of order at most \(16\). They explicitly describe those Figure 2 data as numerical and explain that the computations can require tens of millions of singular-value calculations. The elementary abelian group \(G=(\mathbb Z/2\mathbb Z)^4\) is one of the four order-\(16\) groups in that figure. Their paper does not give the two affine five-support orbits, the exact rational rank census above, or the split between forced time-coordinate zeros and forced additional Fourier zeros.

Meshulam's divisor-interpolation uncertainty inequality gives general lower bounds on Fourier-support size for finite Abelian groups, but for a five-point support in a group of order \(16\) it does not resolve the exact value \(9\). Searches for the same claim under Walsh, Hadamard, exact-support, affine-orbit, rank-deficient-submatrix and elementary-abelian terminology did not locate a published statement of the census above. The bare absence of the support pair was already represented numerically in the historical diagram; the contribution here is the exact affine-orbit rank classification and its tolerance-free proof.

## Limitations
This is a finite classification specific to five-point supports and seven prescribed Fourier zeros on \(G=(\mathbb Z/2\mathbb Z)^4\). It does not classify the complete uncertainty diagram for \(G\), nor does it assert an infinite-family theorem. The computational certificate is exhaustive because the affine-orbit partition and every seven-character set for each representative are explicitly enumerated; it should not be extrapolated beyond this finite domain. A residual originality risk remains for an equivalent small Walsh-matrix census published under terminology not found by the targeted searches.

## References
1. F. Krahmer, G. E. Pfander, P. Rashkov, *Uncertainty in time--frequency representations on finite Abelian groups and applications*, arXiv:math/0611493 (first public version 2006-11-16); Applied and Computational Harmonic Analysis 25 (2008), 209--225, DOI 10.1016/j.acha.2007.09.008.
2. R. Meshulam, *An uncertainty inequality for finite abelian groups*, European Journal of Combinatorics 27 (2006), 63--67, DOI 10.1016/j.ejc.2004.07.009.
