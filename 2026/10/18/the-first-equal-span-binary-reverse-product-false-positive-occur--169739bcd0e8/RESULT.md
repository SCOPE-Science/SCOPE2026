# The first equal-span binary reverse-product false positive occurs at 21 bits

## Finding

For any integer \(L\ge 2\), let \(\mathcal W_L\) consist of binary strings \(w=(w_0,\ldots,w_{L-1})\) with \(w_0=w_{L-1}=1\). Write \(P_w(z)=\sum_{j=0}^{L-1}w_jz^j\), \(N(w)=P_w(2)\), \(N(w^{\rm rev})=2^{L-1}P_w(1/2)\), and \(D_w=N(w)N(w^{\rm rev})\). Set the aperiodic correlations \(r_w(k)=\sum_{j=0}^{L-1-k}w_jw_{j+k}\), with \(0\le k<L\).

**Theorem.** For every \(2\le L\le 20\), two words in \(\mathcal W_L\) with the same \(D_w\) have identical autocorrelations at every lag. At \(L=21\) there is exactly one exceptional pair, modulo reversal of either word and interchange, namely

\[
\begin{aligned}
A&=\{0,2,3,4,6,8,11,14,15,20}\,,\\
B&=\{0,2,7,8,10,11,12,14,16,17,20}\,.
\end{aligned}
\]

The associated base-two integers are \(1100125\) and \(1269125\). Their bit reversals are \(1528417\) and \(1324889\); thus

\[
1100125\cdot1528417=1269125\cdot1324889=1681449752125.
\]

But \(r_A(0)=10\) and \(r_B(0)=11\), so \(|P_A(1)|^2=100\) and \(|P_B(1)|^2=121\). In particular, the two sets are **not** homometric and their full Fourier power spectra differ. Thus numerical equality at \(z=2\) is an unsound surrogate for equality of Fourier intensities, with sharp equal-span onset at twenty-one bits.

## Assumptions and scope

The theorem is exclusively about **equal-length**, endpoint-anchored binary words. These words encode finite subsets of integers with a common span \(L-1\), after shifting each minimum point to zero. Reflection corresponds to word reversal and leaves both the autocorrelation and the reverse product invariant. The theorem does not assert a global minimum if the two encodings have different lengths, nor any claim for lengths greater than \(21\). The \(L=1\) singleton case is trivial.

## Proof

**Autocorrelation equivalence.** Expanding gives the Laurent polynomial identity

\[
P_w(z)P_w(z^{-1})=r_w(0)+\sum_{k=1}^{L-1}r_w(k)(z^k+z^{-k}).
\]

Hence the correlations agree at every lag if and only if these Laurent polynomials agree, which is equivalent to \(|P_w(e^{it})|^2\) agreeing for every real \(t\). Conversely the reverse product is only one real evaluation:

\[
D_w=2^{L-1}P_w(2)P_w(1/2).
\]

Therefore full homometry implies equal reverse products, whereas the questioned converse is an independent assertion.

**Exact counterexample.** The two bitsets have the explicit factorizations

\[
\begin{array}{ll}
1100125=5^3\cdot13\cdot677,&1528417=11\cdot19\cdot71\cdot103,\\
1269125=5^3\cdot11\cdot13\cdot71,&1324889=19\cdot103\cdot677.
\end{array}
\]

Thus their reverse products agree by factor rearrangement. Direct popcounts give \(r_A(0)=10\) and \(r_B(0)=11\), which is already a decisive failure of homometry. Both bitsets have first and last bits equal to one, hence both spans are twenty.

**Exhaustive minimality and uniqueness certificate.** The supplied `verify.py` uses exact integer arithmetic and executes the complete finite census for every \(2\le L\le21\). For fixed \(L\), any anchored word is uniquely \(1+2u+2^{L-1}\) for an integer \(0\le u<2^{L-2}\); this enumerates **every** admissible word, not a sample. A bit-loop computes reversal. Since reversal preserves both reverse product and correlations, keeping only the smaller of each reversal pair loses no possible exceptional fiber. The verifier groups these representatives by their exact integer reverse product and, within each group, by their exact full vector \((r_w(0),\ldots,r_w(L-1))\). It certifies zero groups with more than one vector for lengths two through twenty, and at length twenty-one exactly one such group, with the two words stated above. At that length the group has exactly two reversal classes; the full computation independently rechecks their product, digit reversal, and differing cardinalities. This completes both quantified finite claims; no infinite search or unproved continuation is used.

The exact number of distinct numerical-product fibers, for lengths two through twenty-one, is reported by the verifier. In particular, at length twenty-one there are \(262231\) different reverse products among all reversal-normalized words and exactly one defective product fiber.

## Verification

Run `python3 verify.py` from this package. The program uses only Python standard-library integers, asserts the exhaustive classification for every length from two through twenty-one, and checks the two explicit reversal products. Its expected final line is `CERTIFIED: unique false-positive fiber at length 21`. The proof of the certificate's exhaustiveness is the bit-mask bijection and reversal reduction above; the program's assertions are not evidence for lengths outside the enumerated domain.

## Relationship to prior work

The MathPages note *Generating Functions for Point Set Distances* explicitly asks whether \(P_A(2)P_A^*(2)=P_B(2)P_B^*(2)\), with normalized reversal \(P^*(z)=z^{\deg P}P(1/z)\), forces equality of the full autocorrelation polynomials. It reports equality as sufficient throughout its tested point sets of maximum distance under sixteen and asks for a counterexample. The present pair supplies a negative answer and identifies the exact **equal-span** first failure at span twenty. The preceding assertion, and the smaller numerical-product fibers that represent actual homometric sets, were already known and are not claimed as new.

Xia and Xu's 2026 Fourier phase-retrieval study connects discrete point-set autocorrelations with full Fourier intensities and constructs genuinely homometric interval pairs. Their theorems require equality of the **entire Fourier magnitude**, not the reverse product at a single off-circle point. Their results therefore do not imply the converse under consideration; our witness even has unequal cardinalities and hence unequal Fourier magnitudes at frequency zero. Rosenblatt and Seymour characterize true homometric sets algebraically, likewise assuming full autocorrelation equality rather than equality of one numerical evaluation.

## Limitations

Only common-aperture binary words of lengths at most twenty-one are classified. All finite lower-bound checks are exact and exhaustive in that stated domain, but they do not establish a universal structural classification or a result for other integer bases. The MathPages source is undated; the date attached to the recent motivating Xia–Xu preprint is not represented as a date for the older MathPages question. Bibliographic coverage beyond the inspected texts is incomplete, and an independently published equivalent counterexample may exist. Independent external audit has not been performed.

## References

1. Yu Xia and Zhiqiang Xu, *Fourier Phase Retrieval for Finite Unions of Intervals*, arXiv:2606.19855v1, first posted 2026-06-18. https://arxiv.org/abs/2606.19855 ; open PDF https://pdfs.assets.alphaxiv.org/2606.19855v1.pdf .
2. *Generating Functions for Point Set Distances*, MathPages, undated online note, https://mathpages.com/home/kmath390/kmath390.htm (especially the section asking if equality of binary reverse products forces isospectrality).
3. J. Rosenblatt and P. D. Seymour, *The Structure of Homometric Sets*, SIAM Journal on Algebraic Discrete Methods 3 (1982), 343–350, DOI:10.1137/0603035.
