# Exact inverse-list law for length-four palindromic duplication

## Finding

Let \(\Sigma\) be an alphabet with \(q\ge2\) symbols. A length-four palindromic duplication changes a word \(x=uvz\), where \(|v|=4\), into \(uvv^Rz\), with \(v^R\) denoting the reversal of \(v\). For \(n\ge4\), define \(P_4(y)\) as the set of all *distinct* length-\(n\) words that can produce \(y\in\Sigma^{n+4}\) through exactly one such duplication, and put \(M_q(n)=\max_{y\in\Sigma^{n+4}}|P_4(y)|\).

**Theorem.** For every \(q\ge2\) and every \(n\ge4\),

\[
M_q(n)=\left\lfloor\frac{n-1}{3}\right\rfloor.
\]

For every choice of distinct letters \(a,b\in\Sigma\), the length-\(n+4\) prefix of the infinite periodic word \((aab)^\omega\) attains the maximum.

## Assumptions and scope

All words are linear rather than cyclic; a duplicated source block and its reversed inserted copy are contiguous. There is exactly one duplication of *four* symbols, and the two selected letters in the construction are unequal. The parent count identifies coincident words, even if they arise through different inverse positions. No complement involution, balance, run constraint, or probability model is assumed. Positions in the proof are indexed from zero.

## Proof

A position \(i\) of a received word \(y\in\Sigma^{n+4}\) is a valid inverse start precisely when its eight-symbol factor \(y_i\cdots y_{i+7}\) has the form \(vv^R\), where \(|v|=4\). Inverting at this start removes positions \(i+4,\ldots,i+7\), yielding the parent

\[
p_i(y)=y_0\cdots y_{i+3}\,y_{i+8}\cdots y_{n+3}.
\]

There are \(m=n-3\) possible starts, \(0\le i\le n-4\).

**Local collision lemma.** If two distinct valid inverse starts differ by one or two, their resulting parents coincide. To prove this, translate the earlier start to zero and inspect the union of the two palindromic constraints. For a displacement of one, the full nine-symbol span is forced to be constant; both inversions consequently delete four equal letters. For a displacement of two, the ten-symbol span is forced to have the pattern

\[
a\,b\,b\,a\,a\,b\,b\,a\,a\,b
\]

for some (not necessarily distinct) letters \(a,b\). Deleting positions \(4,5,6,7\) or positions \(6,7,8,9\) leaves the same six-symbol local outcome \(a\,b\,b\,a\,a\,b\). In both cases the unchanged outside prefix and suffix agree as well. This proves the lemma without any restriction on \(q\).

Choose one valid inverse start for each *different* parent. The collision lemma implies that any two chosen starts are at least three apart. At most \(\lceil m/3\rceil=\lfloor(n-1)/3\rfloor\) indices from \(\{0,\ldots,m-1\}\) can have this separation. Hence \(|P_4(y)|\le\lfloor(n-1)/3\rfloor\) for every received word.

For sharpness choose \(a\ne b\) and take \(y\) to be the length-\(n+4\) prefix of \((aab)^\omega\). Every start \(i\) divisible by three is valid: the eight-letter factor starting there is \(aab aabaa\), which reads identically backward. There are exactly \(\lfloor(n-1)/3\rfloor\) such starts in \(0\le i\le n-4\). Moreover, if \(i<j\) are two of these starts, the parent obtained at \(i\) has the letter \(b\) at output coordinate \(i+4\), inherited from \(y_{i+8}\), while the parent obtained at \(j\) still has the letter \(a\) there, inherited from \(y_{i+4}\). These coordinates exist because the later start is legal. The resulting parents are pairwise different. The lower bound matches the upper bound, proving the theorem. \(\square\)

## Verification

The attached standalone Python file `verify_pal4.py` enumerates every received word at \(4\le n\le14\) for \(q=2\), \(4\le n\le8\) for \(q=3\), \(4\le n\le6\) for \(q=4\), and \(4\le n\le5\) for \(q=5\). It compares their actual sets of distinct inverse parents with the claimed maximum. The code also checks the local-collision identities symbolically via equality classes imposed by the two overlapping palindrome constraints. Finally it tests the explicit periodic construction at every length through \(n=300\). Run with `python3 verify_pal4.py`; the accompanying `verify_pal4.out` records the completed execution and `VERIFY_OK`. Finite computation tests the argument, but does not replace the preceding all-length proof.

## Relationship to prior work

Zabokritskiy (2026), Section 6, Lemma 6.1, gives the general bound of \(n-k+1\) parents for a length-\(k\) palindrome duplication. For \(k=4\) this is \(n-3\); the exact sharp value here is \(\lfloor(n-1)/3\rfloor\). Section 5 of that paper instead concerns the *forward* two-error descendant sphere, a different invariant. The even-length reverse-complement conjugacy in Section 4 transfers the present one-step inverse-count result to the corresponding conjugate channel under that paper's assumptions.

Lenz, Wachter-Zeh and Yaakobi (2017), Appendix A, Lemma 15, bound palindromic *deletion* spheres by runs of palindrome-valid positions but do not resolve the additional collisions between starts separated by two at duplication length four. Their exact specialized deletion formulas concern lengths one and two, not four. Sun and Ge (2026) study coding bounds and constructions rather than this exact inverse-list extremum. The central new distinction is the distance-two collision lemma together with the period-three extremizer; neither follows from simply counting eligible palindrome windows.

## Limitations

The theorem determines the maximum number of distinct one-step ancestors, not the complete distribution of ancestor counts or all maximizing received words. It does not assert a sharp *two-step* inverse-list value or give an optimal error-correcting codebook. It is specific to length-four palindromic duplication; no assertion is made for every duplication length divisible by four. Literature comparisons cannot rule out an undiscovered equivalent statement.

## References

1. A. L. Zabokritskiy, *Coding for Multiple Reverse-Complement and Palindromic Duplications*, arXiv:2609.00779, first public 2026-09-01; especially Sections 2, 4–6. https://arxiv.org/abs/2609.00779
2. A. Lenz, A. Wachter-Zeh and E. Yaakobi, *Duplication-Correcting Codes*, arXiv:1712.09345, first public 2017-12-24; Appendix A, Lemmas 12–15. https://arxiv.org/abs/1712.09345
3. Y. Sun and G. Ge, *On the Palindromic/Reverse-Complement Duplication Correcting Codes*, arXiv:2602.01151, first public 2026-02-01. https://arxiv.org/abs/2602.01151
