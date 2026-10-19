# Two upper composition layers reconstruct binary words with at most three ones

## Finding
For a finite binary word \(w\), and an integer \(j\geq 0\), let \(H_j(w;z)\in\mathbb Z[z]\) be the polynomial in which the coefficient of \(z^\ell\) counts the **occurrences** (not just distinct types) of contiguous length-\(\ell\) factors containing exactly \(j\) ones. Only nonempty factors are counted. Let \(r\) denote the number of ones in \(w\).

**Theorem.** If \(1\leq r\leq3\), then the ordered pair of polynomials \((H_{r-1}(w;z),H_r(w;z))\), together with the known value \(r\), determines \(w\) uniquely up to reversal. For \(r=1\), the second polynomial \(H_1\) alone already suffices; for \(r=0\), the all-zero word is determined by its length. In particular, if \(r=3\), the two multiplicity distributions for compositions with exactly two or three ones suffice at **every length**, without knowing any composition counts having fewer ones. The same statements hold after exchanging the two binary symbols.

The cutoff is sharp for reconstruction from the **full** multiset of contiguous substring compositions: there exist length-eight words with four ones and equal complete composition multisets that are not reversals. The **topmost** layer by itself is insufficient for the three-one claim, even when the common length is given. The sufficiency (or failure) of the second-highest layer alone is not settled here.

## Assumptions and scope
Words have arbitrary finite length over \(\{0,1\}\). Substrings are contiguous, unlike scattered subsequences; their multiplicities are retained. The nonnegative zero-gap parameters include zero. Reconstruction is up to reversal, which preserves every \(H_j\), and the weight \(r\) is either a specified part of the promise or identified by the highest occupied one-count layer in the complete composition observation. The theorem makes no claim about arbitrary words of weight four or more, or recovery of orientation.

Write \(F_m(z)=\sum_{i=0}^m z^i\) for \(m\ge0\). Its product with \(F_t\) has degree \(m+t\) and largest coefficient \(\min(m,t)+1\). Thus, given the product of two such polynomials, their unordered length parameters can be read from its degree and peak coefficient.

## Proof
**Three ones.** Every such word has a unique representation
\[
w=0^a1\,0^b1\,0^c1\,0^d,\qquad a,b,c,d\in\mathbb Z_{\ge0}.
\]
A contiguous factor containing all three ones starts either on the first \(1\) or among the \(a\) preceding zeros, and terminates either on the third \(1\) or among the \(d\) following zeros. Hence
\[
H_3(w;z)=z^{b+c+3}F_a(z)F_d(z).
\]
A contiguous factor containing exactly two ones contains either the first and second ones or the second and third ones. Summing the independent choices of extra zeros at its ends gives
\[
H_2(w;z)=z^{b+2}F_a(z)F_c(z)+z^{c+2}F_b(z)F_d(z). \tag{1}
\]
Both identities include boundary cases in which any gap is zero.

The smallest exponent of \(H_3\) is \(b+c+3\). Divide by that monomial: the resulting \(F_aF_d\) has degree \(a+d\) and peak coefficient \(\min(a,d)+1\), so it recovers the **unordered** pair \(\{a,d\}\). The smallest exponent of \(H_2\) is \(\min(b,c)+2\), because both summands have nonnegative coefficients and nonzero constant factors. Combining it with \(b+c\), obtained from \(H_3\), recovers the unordered pair \(\{b,c\}\).

These pairs give at most four ordered gap quadruples. Reversal maps \((a,b,c,d)\) to \((d,c,b,a)\), leaving at most two inequivalent choices. Fix an orientation of the outer pair \((a,d)\). In the two possible orders of the middle pair, the difference between formula (1) is
\[
(F_a(z)-F_d(z))\bigl(z^{b+2}F_c(z)-z^{c+2}F_b(z)\bigr). \tag{2}
\]
If \(a\ne d\) and \(b\ne c\), the first factor in (2) is a nonzero polynomial (its degree detects the larger gap), while the second is nonzero because its two summands have distinct smallest exponents. The integral polynomial ring is a domain, so the difference cannot vanish. If \(a=d\), interchanging \(b,c\) is precisely reversal of the whole word; if \(b=c\), no interchange changes the word. Thus the two observed polynomials distinguish exactly the orientations permitted by reversal. The reconstruction procedure is constructive: recover the two unordered gap pairs, test at most four assignments in (1), and quotient by reversal.

**Two ones.** Write \(w=0^a1\,0^b1\,0^c\). The polynomial \(H_2=z^{b+2}F_aF_c\) recovers \(b\) and \(\{a,c\}\) exactly by its smallest exponent, residual degree, and peak coefficient. The two possible orders of \(a,c\) are reversals. In particular, retaining both \(H_1,H_2\) suffices.

**One or zero ones.** For \(w=0^a1\,0^b\), the same calculation gives \(H_1=zF_aF_b\), recovering the unordered pair \(\{a,b\}\). If no ones occur, the length of the single zero run specifies the word; its nonempty zero-only composition spectrum determines that length.

**Sharp boundaries.** The length-five words \(11001\) and \(10101\) have three ones and \(H_3=z^5\), yet are not reversals. Consequently the highest layer alone is insufficient even at fixed length. The two length-eight words \(01001101\) and \(01101001\) each have four ones, are not reversals, and have identical **complete** substring-composition multisets. This classical example is independently checked by the accompanying program and is reproduced only as a boundary, not claimed as a new construction. It rules out extending the unique-reconstruction guarantee to arbitrary four-one words even with all layers available.

## Verification
Run `python3 verify_sparse.py`, with Python 3 standard library only. The program independently enumerates factor-composition counts and checks both displayed polynomial identities for all \(8^4=4096\) four-gap quadruples with gaps between zero and seven. It verifies uniqueness of the reconstruction up to reversal across all \(7315\) weight-three words of lengths three through twenty-one, and checks both sharp boundary examples against direct complete spectra. Expected output begins with `VERIFY_OK` and reports the experiment counts. The finite checks corroborate rather than replace the algebraic all-length proof.

## Relationship to prior work
Acharya, Das, Milenkovic, Orlitsky, and Pan formulated reconstruction from the complete contiguous-substring composition multiset and proved length-dependent reconstruction statements together with a general bivariate-polynomial equivalence criterion [1]. In particular, their length-eight four-one collision is used above as a sharpness witness. These broad results do not provide the stated **two top one-count layers** reconstruction theorem for sparse binary words, nor the explicit four-gap decoding identity (2).

Gupta and Mahdavifar further developed algebraic string reconstruction from substring compositions [2]. Their setting concerns complete composition observations and different algebraic reconstruction tools, not a theorem requiring only two sparse composition layers. The present result is an elementary structural restriction of the observation model; its proof does not assume that general polynomial-factorization reconstruction has been solved. Mathematical overlap is possible through equivalent specialized statements not located in the literature examined.

## Limitations
The reconstruction guarantee stops at three occurrences of the minority symbol; it does not determine the optimal recovery guarantees for other partial-layer observations at higher weights. The reconstruction presupposes exact noiseless composition multiplicities and a known/recognizable binary alphabet, and orientation remains undetermined. No probabilistic robustness or algorithmic bit-complexity optimality is asserted. Relevant unindexed specialized reconstruction literature could contain an equivalent theorem; the absence of a search match is not itself a proof of originality.

## References
[1] J. Acharya, H. Das, O. Milenkovic, A. Orlitsky, S. Pan, *String Reconstruction from Substring Compositions*, arXiv:1403.2439 (initial public preprint, 2014-03-10), later SIAM Journal on Discrete Mathematics, DOI 10.1137/140962486; especially Sections 2, 4–6.

[2] S. Gupta and H. Mahdavifar, *A New Algebraic Approach for String Reconstruction from Substring Compositions*, arXiv:2201.09955 (2022), introduction and main algebraic framework.
