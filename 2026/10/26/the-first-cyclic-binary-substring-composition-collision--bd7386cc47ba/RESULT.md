# The first cyclic binary substring-composition collision

## Finding
For binary circles of every length from \(1\) through \(11\), the multiset of compositions of all cyclic contiguous windows of every length determines the circle up to rotation and reversal. At length \(12\), there are exactly \(224\) dihedral classes (bracelets) and \(223\) different complete observations. Precisely one observation is shared by two bracelets, with canonical representatives

```text
001011001101
001011010011
```

All other observations have exactly one bracelet preimage. At length \(12\), the classical two-point-autocorrelation observation instead has \(23\) ambiguous pairs of bracelets. Thus the complete cyclic window-composition observation is a strictly stronger reconstruction measurement and, in particular, has a later first failure of injectivity. The displayed exceptional pair also gives a distinct ambiguous pair of bracelets at every length divisible by \(12\), by taking the same positive integer power of both words.

## Assumptions and scope
For a binary circle \(w=(w_0,\dots,w_{n-1})\), indices are taken modulo \(n\). Define the cyclic window weight
\[
S_{w,k}(i)=\sum_{j=0}^{k-1}w_{i+j},\qquad 1\le k\le n,\quad 0\le i<n,
\]
and its *composition histogram*
\[
H_{w,k}(a)=\#\{i:0\le i<n,\ S_{w,k}(i)=a\},\qquad 0\le a\le k.
\]
The full observation is \(\mathcal H(w)=(H_{w,k})_{k=1}^n\). All \(n\) cyclic starting sites, including repeated factors, are counted. In contrast to linear-substring reconstruction, windows may wrap around the designated origin. A dihedral bracelet identifies words related by cyclic rotation or reversal, but **not** arbitrary bit complementation. A collision means two *different* bracelets share \(\mathcal H\). The finite uniqueness and census assertions concern all binary circles of lengths \(1\le n\le12\); the periodic construction applies to every positive multiple of \(12\). No universal classification for greater lengths is asserted.

## Proof
**1. Observation invariances and recovery of the omitted half.** Rotation merely permutes window starts; reversal sends each window to a reversed window of the same length and weight. Hence \(\mathcal H\) is a bracelet invariant. Let \(R=\sum_iw_i\). The windows of length \(k\) and their complementary cyclic windows of length \(n-k\) give
\[
H_{w,k}(a)=H_{w,n-k}(R-a),\qquad 1\le k<n.
\]
The length-\(n\) histogram consists of \(n\) copies of weight \(R\). Consequently \(\mathcal H\) is fully and exactly encoded by \(R\) together with the histograms for \(1\le k\le\lfloor n/2\rfloor\). This reduction is used, without discarding any information, in the exhaustive certificate.

**2. The unique length-twelve ambiguity exists.** Let \(u=\mathtt{001011001101}\), \(v=\mathtt{001011010011}\). Both have \(R=6\). For lengths \(1\) through \(6\), their common histograms, with coordinates \(a=0,1,\ldots,k\), are respectively

| \(k\) | Shared counts \((H_{w,k}(0),\ldots,H_{w,k}(k))\) |
|---|---|
| 1 | \((6,6)\) |
| 2 | \((2,8,2)\) |
| 3 | \((0,6,6,0)\) |
| 4 | \((0,2,8,2,0)\) |
| 5 | \((0,0,6,6,0,0)\) |
| 6 | \((0,0,1,10,1,0,0)\) |

The complementary-window identity proves equality also for lengths \(7\) through \(12\). Independently enumerating all rotations and reversals gives different minimum representatives \(u\) and \(v\); hence they are not the same bracelet.

**3. Exhaustive, finite uniqueness and multiplicity proof.** A certificate enumerates every integer in \(\{0,\ldots,2^n-1\}\) for each \(n\) from \(1\) through \(12\), treats its \(n\)-bit expansion as a word (including leading zeroes), takes the lexicographically least rotation or reversed rotation, and groups the resulting distinct canonical representatives by their exact reduced integer-valued histograms from Step 1. It uses no floating-point computation or probabilistic hashes. All \(2^{12}=4096\) words, not a sampled subset, are considered at the largest length. A second implementation independently calculates canonical representatives from strings and calculates each histogram with a moving sum, checking the two versions on every word. The verified \((\text{length},\text{bracelets},\text{observations})\) counts are

| Length | Bracelets | Observations |
|---:|---:|---:|
| 1 | 2 | 2 |
| 2 | 3 | 3 |
| 3 | 4 | 4 |
| 4 | 6 | 6 |
| 5 | 8 | 8 |
| 6 | 13 | 13 |
| 7 | 18 | 18 |
| 8 | 30 | 30 |
| 9 | 46 | 46 |
| 10 | 78 | 78 |
| 11 | 126 | 126 |
| 12 | 224 | 223 |

At length \(12\), the exact group-size distribution is \(222\) observations with one bracelet and one observation with the two bracelets displayed in Step 2; there are no larger groups. All eleven shorter lengths have only singleton groups. The certificate independently confirms the expected length-twelve bracelet count \(224\) (also obtained from Burnside's lemma as \((4224+1152)/24\)). The full enumeration and cross-implementation equality establish the finite classification, not an inference from a partial search. Its complete source code and the auxiliary comparison table are bundled as `verify.py` and `homometric_pairs_n12.csv`.

**4. Comparison with homometry.** Define the cyclic autocorrelation \(C_d(w)=\sum_{i=0}^{n-1}w_iw_{i+d}\) and the histogram-derived second moment \(F_k(w)=\sum_a a^2H_{w,k}(a)\), setting \(F_0=0\). Expanding the squared window sums, for every \(1\le k\le n\), yields
\[
F_k=kR+2\sum_{d=1}^{k-1}(k-d)C_d.
\]
Consequently for \(1\le d<n\),
\[
C_d=\frac{F_{d+1}-2F_d+F_{d-1}}2.
\]
Thus identical complete window observations imply identical cyclic autocorrelations, or homometry. The converse fails: the finite certificate enumerates exactly \(23\) distinct ambiguous *pairs* of length-twelve bracelets sharing an autocorrelation vector, but only the single pair in Step 2 shares every window histogram. Among the other \(22\) homometric pairs, \(17\) are first distinguished by window length \(3\), three by length \(4\), and two by length \(5\). The auxiliary CSV lists all \(23\) pairs and the first distinguishing window length, with \(0\) indicating the surviving collision.

**5. Periodic extension.** Let \(r\ge1\) and form \(u^r\) and \(v^r\), where exponentiation means repeated concatenation, so both have length \(12r\). Every length-\(L\) cyclic window can be written as \(q\) full twelve-letter periods and a remainder of length \(s\), where \(L=12q+s\), \(0\le s<12\). Its weight is \(6q\) plus the weight of the length-\(s\) window of its underlying twelve-letter word. Each underlying start occurs exactly \(r\) times. Step 2 therefore gives identical histograms for all \(L\). If the repeated words were related by rotation or reversal, examining any twelve consecutive letters would make \(u\) and \(v\) dihedrally equivalent, contrary to Step 2. Hence there are genuine collisions at every length divisible by \(12\).

## Verification
Run `python3 verify.py` from a directory containing `verify.py` and `homometric_pairs_n12.csv`. The standard-library-only program exhaustively verifies the complete classification through length \(12\), the independent canonical-representative and spectrum implementations, the \(23\)-pair homometry comparison and CSV, and the finite cyclic moment identities. The program additionally checks the periodic witnesses for powers one through five, while Step 5—not these finite checks—proves the assertion for all positive powers. Successful completion prints `VERIFY_OK`. The maximum enumeration comprises exactly \(4096\) words at length \(12\). No randomized or statistical argument is used for the theorem.

## Relationship to prior work
The classical cyclic Z-relation/homometry is the equality of two-point interval vectors and is documented by Mandereau et al. (2011) and Jedrzejewski--Johnson (2013). In particular, the latter enumerates the length-twelve Z-related pairs by subset cardinality, with \(19\) pairs for cardinalities at most six; adding the complementary cardinalities seven and eight gives the \(23\) pairs in our comparison. That **weaker** statistic permits collisions as early as length \(8\), while the complete cyclic *contiguous-window-composition* observation studied here is injective through length \(11\). Mandereau et al.'s broader \(k\)-deck counts configurations of chosen positions and is not identical to counting the weight distribution of each consecutive cyclic window. Acharya et al. (2014) study compositions of **linear** contiguous substrings, not wrapping cyclic windows. Their reconstruction results therefore neither supply nor imply this cyclic length-twelve census. This work does not claim discovery of homometric pairs or the linear substring-composition reconstruction problem.

## Limitations
The finite injectivity threshold and exact length-twelve class distribution rely on an exhaustive, reproducible integer computation whose complete search space is proved to be enumerated; they are not replaced here by a shorter symbolic classification. The all-length claim is only the infinite subsequence of lengths divisible by \(12\). For other larger lengths, neither injectivity nor the full ambiguity distribution is determined. Historical priority remains subject to earlier unindexed treatments of cyclic window-sum multispectra; literature comparison does not prove unique precedence. No independent mathematical audit has been performed.

## References
1. J. Mandereau, D. Ghisi, E. Amiot, M. Andreatta, C. Agon, “Z-relation and homometry in musical distributions,” *Journal of Mathematics and Music* **5** (2011), 83–98; first available online 15 September 2011. DOI: `10.1080/17459737.2011.608819`.
2. J. Mandereau, D. Ghisi, E. Amiot, M. Andreatta, C. Agon, “Discrete phase retrieval in musical structures,” *Journal of Mathematics and Music* **5** (2011), 99–116; first available online 15 September 2011. DOI: `10.1080/17459737.2011.608820`.
3. F. Jedrzejewski, T. Johnson, “The Structure of Z-Related Sets,” *Mathematics and Computation in Music*, LNCS **7937** (2013), 128–137; `arXiv:1304.6608` (23 April 2013). DOI: `10.1007/978-3-642-39357-0_10`.
4. J. Acharya, H. Das, O. Milenkovic, A. Orlitsky, S. Pan, “String Reconstruction from Substring Compositions,” `arXiv:1403.2439` (first public 10 March 2014).
