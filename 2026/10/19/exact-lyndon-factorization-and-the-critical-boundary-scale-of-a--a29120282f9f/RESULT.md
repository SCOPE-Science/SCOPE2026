# Exact Lyndon factorization and the critical boundary scale of a two-parameter sparse morphism

## Finding
Fix integers \(q\ge2\) and \(r\ge1\), and use the binary alphabet ordered by \(0<1\). Consider the prolongable substitution
\[
\sigma(0)=0^q,\qquad \sigma(1)=1\,0^r1,
\]
with \(W_j=\sigma^j(1)\) and infinite fixed point \(C=\lim_{j\to\infty} W_j\). Define \(B_j=0^{r q^j} W_j\) and \(n_j=|W_j|\), for each integer \(j\ge0\).

**Finite, complete factorization:** For every integer \(k\ge0\), the unique Chen–Fox–Lyndon decomposition of \(W_k\) is
\[
W_k=1\; B_0\; B_1\cdots B_{k-1},
\]
with precisely \(k+1\) factors, each Lyndon and in strictly decreasing lexicographic order. In particular, every factor is given explicitly, not just its length.

**Infinite decomposition:** The infinite fixed point has the corresponding decreasing Lyndon decomposition
\[
C=1\; B_0\; B_1\; B_2\cdots .
\]
The factor \(B_j\) begins at zero-based position \(n_j\) and occupies exactly \(n_{j+1}-n_j\) positions. Its initial maximal run of zeros has length \(r q^j\). These starts are therefore canonical factor boundaries at every finite substitution depth.

**Exact boundary law and scale transition:** With \(n_0=1\),
\[
n_{j+1}=2n_j+r q^j,
\qquad
n_j=\begin{cases}
2^j+\dfrac{r(q^j-2^j)}{q-2},&q>2,\\[3pt]
2^j+rj2^{j-1},&q=2,
\end{cases}
\]
where the second summand in the \(q=2\) case is interpreted as zero for \(j=0\). The generating function is the rational expression
\[
\sum_{j\ge0}n_j z^j=\frac{1+(r-q)z}{(1-qz)(1-2z)}.
\]
Thus for fixed \(r\), factor boundaries grow asymptotically like \(\frac{r}{q-2}q^j\) when \(q>2\), but like \(\frac r2j2^j\) when \(q=2\). The uniform generalized-Cantor subfamily \(q\ge3,\ r=q-2\) has the especially simple exact boundary law \(n_j=q^j\).

## Assumptions and scope
All exponentiation in the substitution is **word repetition**, not numerical exponentiation. The alphabet is binary with \(0<1\), the pair \((q,r)\) ranges over all integers with \(q\ge2\) and \(r\ge1\), and \(j,k\) are arbitrary nonnegative integers. A nonempty finite word is Lyndon when it is lexicographically smaller than each nonempty proper suffix, using the standard convention that a proper prefix precedes the longer word. The Chen–Fox–Lyndon theorem gives a unique nonincreasing factorization of every finite word into Lyndon words. Here the factors are strictly decreasing. Boundary indices are zero-based. No claim is made about substituting \(r=0\), about reversing the alphabet order, or about arbitrary intermediate prefixes of \(C\).

## Proof
**1. Recursive block identity.** As \(\sigma(1)=1 0^r1\) and \(\sigma^j(0^r)=0^{r q^j}\), one obtains for every \(j\ge0\)
\[
W_{j+1}=W_j 0^{r q^j}W_j=W_jB_j.
\]
Because \(W_0=1\), induction immediately yields the claimed complete concatenation \(W_k=1B_0\cdots B_{k-1}\) and its increasing-prefix limit for \(C\). Each \(W_j\) begins and ends in \(1\), and \(W_j\) is nonempty.

**2. Sharp internal zero-run bound.** For \(j=0\), \(W_0\) has no zeros. For every \(j\ge1\), the largest run of consecutive zeros inside \(W_j\) has length exactly \(r q^{j-1}\). This is proved inductively from the displayed identity: the inserted run has length \(r q^{j-1}\), and all older runs are strictly shorter, since \(q\ge2\). As both copies of \(W_{j-1}\) start/end in \(1\), the inserted run cannot merge with a neighboring zero run.

**3. Each explicit factor is Lyndon.** Fix any \(j\ge0\), and put \(m=rq^j\). The word \(B_j=0^mW_j\) begins with exactly \(m\) zeros, since \(W_j\) begins in \(1\). Consider an arbitrary nonempty proper suffix \(S\) of \(B_j\). If \(S\) begins in \(1\), then \(B_j<S\). Otherwise \(S\) begins in a run of \(h\) zeros. If \(S\) starts inside the leading block, \(h<m\). If it starts in \(W_j\), then \(h\le rq^{j-1}<m\) when \(j\ge1\); for \(j=0\), this latter possibility cannot occur. Therefore every proper suffix beginning in \(0\) has fewer than \(m\) initial zeros. Lexicographic comparison at position \(h\) gives \(B_j<S\) (at that position \(B_j\) still has a zero while the suffix has a one). Hence \(B_j\) is Lyndon. The single-letter word \(1\) is also Lyndon.

**4. Strict factor order and completeness.** The initial run of zeros in \(B_{j+1}\) has length \(r q^{j+1}>rq^j\). Therefore \(B_{j+1}<B_j\) for every \(j\ge0\), while \(B_0<1\). Thus the decomposition in step 1 is a sequence of Lyndon words in strictly decreasing order. By uniqueness of the finite Chen–Fox–Lyndon factorization it is the *entire* decomposition of every \(W_k\), including \(k=0\). Since the finite decompositions have the same first factors for all sufficiently large \(k\), passing to the increasing-prefix limit gives the displayed infinite factor sequence. (Equivalently, this is the infinite factorization with infinitely many finite decreasing Lyndon blocks in the conventional infinite-word factorization terminology.)

**5. Exact locations and generating function.** Taking lengths in step 1 gives \(n_{j+1}=2n_j+rq^j\). Since \(B_j\) is appended immediately after \(W_j\), its start is exactly \(n_j\) and its length is \(n_{j+1}-n_j\). Solving the nonhomogeneous recurrence gives \(2^j+r(q^j-2^j)/(q-2)\) when \(q\ne2\). At the double root \(q=2\), summing \(n_{j+1}/2^{j+1}=n_j/2^j+r/2\) yields \(n_j=2^j+rj2^{j-1}\). Finally, multiply the recurrence by \(z^{j+1}\) and sum over \(j\ge0\):
\[
\Big(\sum_{j\ge0}n_jz^j\Big)(1-2z)
=1+\frac{rz}{1-qz},
\]
which simplifies to the claimed generating function. The stated asymptotics and uniform-subfamily identity follow directly. These deductions use no unverified infinite enumeration. \(\square\)

## Verification
The accompanying standalone Python file `verify_lyndon.py` constructs finite substitutions directly, computes an independent Duval/Chen–Fox–Lyndon factorization, and checks exact factor contents, factor counts, strict order, factor starts, and length formulas over a rectangular grid of parameter pairs at every computationally feasible depth. It also checks the morphic block identity against direct construction. The test reports the exact number of checked finite words; no finite test substitutes for the all-parameter proof.

## Relationship to prior work
Goc, Saari, and Shallit (2012) establish general properties of Lyndon factors and Lyndon factorization of automatic and recurrent words, including algorithmic regularity and examples involving classical automatic words. Their inspected paper does not give the explicit factor content or boundary generating function for \(0\mapsto0^q,\ 1\mapsto10^r1\) across all integers \(q\ge2,r\ge1\). Lü, Chen, Guo, and Wen (public 2015; journal 2016) treat a related generalized Cantor substitution subfamily \(r=q-2\), concentrating on ordinary and permutation complexity, not this Lyndon decomposition. Prior results on the period-doubling word concern a different fixed point. The standard uniqueness theorem and the general existence of factoring algorithms are accepted background; the specific two-parameter closed classification and its critical \(q=2\) scale are the proposed contribution.

## Limitations
No assertion is made about the novelty of the standard finite Lyndon factorization theorem itself. Explicit closed formulas are given only for complete substitution iterates and the infinite fixed point, not arbitrary truncations or factorizations under reverse order. Related morphism families could conceivably have equivalent unindexed published classifications; the originality conclusion is conditional on inspected accessible literature. Computational tests cover bounded parameter ranges and lengths only; the infinite result is justified by the proof.

## References
1. D. Goč, K. Saari, J. Shallit, *Primitive Words and Lyndon Words in Automatic and Linearly Recurrent Sequences*, arXiv:1207.5124 (first posted July 21, 2012), https://arxiv.org/abs/1207.5124.
2. X.-T. Lü, J. Chen, Y. Guo, Z.-X. Wen, *On the permutation complexity of the Cantor-like sequences*, *Theoretical Computer Science* 616 (2016), 100–110, doi:10.1016/j.tcs.2015.12.022 (first online December 29, 2015).
3. Chen–Fox–Lyndon factorization theorem and Duval's linear-time algorithm, standard results; see the background and citations in reference 1.
