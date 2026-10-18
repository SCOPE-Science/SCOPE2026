# Exact finite dyadic \(2\)-abelian complexity of Rudin–Shapiro factors through length \(65536\)

## Finding
Let \(r_i\in\{0,1\}\) be the parity of the number of adjacent occurrences of the bit pattern \(11\) in the ordinary binary expansion of \(i\), and let \(P_r^{(2)}(n)\) be the number of \(2\)-abelian equivalence classes of length-\(n\) contiguous factors of the infinite word \(r_0r_1\cdots\). Equivalence means equal counts of all one-letter and two-letter factors.

**Finite exact theorem.** For every integer \(m\) with \(4\le m\le16\), and \(n=2^m\), the following verified equality holds:
\[
P_r^{(2)}(2^m)=\begin{cases}
16(2^{m/2}-1),&m\text{ even},\\
16(3\cdot2^{(m-3)/2}-1),&m\text{ odd}.
\end{cases}
\]
This is a collection of thirteen exact finite assertions; the right-hand formula is **not claimed for any other integer** \(m\). The values are:

| \(m\) | \(n\) | \(P_r^{(2)}(n)\) |
|---:|---:|---:|
| 4 | 16 | 48 |
| 5 | 32 | 80 |
| 6 | 64 | 112 |
| 7 | 128 | 176 |
| 8 | 256 | 240 |
| 9 | 512 | 368 |
| 10 | 1024 | 496 |
| 11 | 2048 | 752 |
| 12 | 4096 | 1008 |
| 13 | 8192 | 1520 |
| 14 | 16384 | 2032 |
| 15 | 32768 | 3056 |
| 16 | 65536 | 4080 |

## Assumptions and scope
Indices start at zero. Binary letters \(0,1\) encode the original signed Rudin–Shapiro sequence by \(r_i=0\) for sign \(+1\) and \(r_i=1\) for sign \(-1\). Each factor is contiguous; its starting index ranges over **all** nonnegative integers. All statements count distinct profiles rather than occurrences. The finite exponent interval is inclusive.

## Proof
We establish a complete finite generating family for factors of every asserted length, then evaluate it exactly with the standalone deterministic program `verify.py`.

**1. Four-state fixed point.** Encode state \(2b+p\) by a bit \(b\in\{0,1\}\) and parity \(p\in\{0,1\}\). Define the length-two morphism
\[
\sigma(2b+p)=(2b)\,\bigl(2(b\mathbin{\mathrm{xor}}p)+1\bigr).
\]
Its fixed point beginning with state \(0\) has the state \(2r_i+(i\bmod2)\) at index \(i\): this follows by induction from \(r_{2j}=r_j\) and \(r_{2j+1}=r_j\mathbin{\mathrm{xor}}(j\bmod2)\). Letter projection \(c(2b+p)=b\) yields the required infinite binary word.

**2. Exhaustive adjacent-state pair lemma.** The set of consecutive state pairs in the fixed point is exactly
\[
Q=\{(0,1),(0,3),(1,0),(1,2),(2,1),(2,3),(3,0),(3,2)\}.
\]
All eight pairs already occur in \(\sigma^4(0)\). Conversely, the internal pairs of the four substitution images are \((0,1),(0,3),(2,3),(2,1)\); the boundary pairs obtained by substituting the two letters of every pair in \(Q\) are \((1,0),(3,2),(1,2),(3,0)\). Their union is exactly \(Q\). Starting from \(0\), induction on the substitution depth excludes every other pair. Thus the lemma holds for the infinite fixed point.

**3. Full length-\(n\) factor lemma.** For \(n=2^m\), each occurrence of a length-\(n\) factor begins in one aligned \(\sigma^m\)-supertile and lies entirely in that tile or crosses only into its successor. Its binary content therefore appears in \(c(\sigma^m(ab))\) for some \((a,b)\in Q\). Conversely every \((a,b)\in Q\) occurs in the state word, so every length-\(n\) window of \(c(\sigma^m(ab))\) occurs in the binary word. Hence the union of those windows, with no unproved cutoff, is **exactly** the infinite word's factor set.

**4. Complete class fingerprints.** For a binary word of fixed length \(n\ge2\), let \(K\) be the number of ones, \(U\) the number of adjacent \(01\) occurrences, and \(a,b\) its first and last bits. Then the remaining counts are
\[
N_{10}=U+a-b,\qquad N_{11}=K-U-a,\qquad N_{00}=n-1-K-U+b.
\]
Consequently \((K,U,a,b)\) is a necessary and sufficient fingerprint for \(2\)-abelian equivalence. `verify.py` constructs the eight pair-images, scans every length-\(n\) window, inserts these fingerprints into a set, and counts it. A complete listing of the thirteen counts and SHA-256 hashes of canonical sorted fingerprints is in `certificates.json`. Program assertions check exactly the tabulated identities. The preceding three mathematical reductions prove that this finite computation is exhaustive for the **infinite** factor sets, not merely a prefix sample.

## Verification
Run `python3 verify.py` in the directory containing `verify.py` and `certificates.json`; no third-party packages are needed. The program prints the complete certificate and terminates with `VERIFY_OK`. The finite pair closure and coding recurrence are asserted. For each length it checks every one of the eight pair-images and all length-\(n\) starting positions. For \(4\le m\le10\), a separately constructed direct digit-parity prefix independently reproduces the **same full fingerprint sets**, and selected individual windows check all four adjacent-pair counts directly. `certificates.json` records independently reproducible canonical SHA-256 fingerprints. The largest evaluation is \(n=65536\).

## Relationship to prior work
Parreau, Rigo, Rowland and Vandomme (2014/2015) developed \(\ell\)-abelian complexity methods and proved \(2\)-regularity for the Thue–Morse and period-doubling sequences; their studied sequences do not include this Rudin–Shapiro fingerprint census. Lü, Chen, Wen and Wu (first circulated 2016) treated the **ordinary abelian** complexity of Rudin–Shapiro, counting only the total number of ones. The finer counts here retain adjacent-pair multiplicities and ordered endpoints, so ordinary abelian complexity does not determine the asserted values. The method gives a complete finite factor-set certificate through a state-pair closure.

## Limitations
The mathematical factor-cover lemmas hold for every dyadic length, but the stated numerical identities are verified only for \(4\le m\le16\). No infinite dyadic formula, \(2\)-regularity theorem, asymptotic statement or uniqueness claim beyond this interval follows from the thirteen evaluations. Novelty remains subject to an independent literature review; an earlier unindexed computational table cannot be categorically excluded. No external independent audit is claimed.

## References
1. A. Parreau, M. Rigo, E. Rowland and É. Vandomme, *A New Approach to the 2-Regularity of the ℓ-Abelian Complexity of 2-Automatic Sequences*, arXiv:1405.3532 (initial public posting 2014-05-14); *Electronic Journal of Combinatorics* 22 (2015), P1.27.
2. X. Lü, J. Chen, Z. Wen and W. Wu, *On the Abelian Complexity of the Rudin-Shapiro Sequence*, arXiv:1606.06935 (initial public posting 2016-06-22); *Journal of Mathematical Analysis and Applications* 451 (2017), 822–838.
