# The first cyclic three-deck ambiguity: exactly three binary necklaces at length eight

## Finding

Let \(w=w_0\cdots w_{n-1}\) be a binary word. For each binary pattern \(u\) of length at most three, let \(\binom{w}{u}\) be the number of increasing position tuples of \(w\) spelling \(u\). Define the full three-binomial profile
\[
\mathcal D_3(w)=\bigl(\binom{w}{u}\bigr)_{u\in\{0,1\}^{1}\cup\{0,1\}^{2}\cup\{0,1\}^{3}}.
\]
For a cut \(i\), write \(\rho_i(w)=w_i\cdots w_{n-1}w_0\cdots w_{i-1}\). We call a necklace *ambiguous* if two **distinct** rotations have equal profiles.

**Theorem (sharp first cyclic ambiguity and complete shortest census).** For every length \(1\le n\le7\), every binary necklace has pairwise different three-binomial profiles on its distinct rotations. At length \(n=8\), precisely three of the 36 necklaces are ambiguous. Their lexicographically least rotations and their complete profile-collision classes (listed as zero-based cut indices) are:

| Canonical necklace | Number of distinct three-binomial profiles | Equal-profile cut classes with distinct rotations |
|---|---:|---|
| `00011011` | 6 | `{4,6}`, `{5,7}` |
| `00100111` | 6 | `{1,3}`, `{2,4}` |
| `00101101` | 7 | `{3,7}` |

All omitted cut classes are singletons, and no other length-eight necklace has distinct rotations with equal profiles. In particular there are exactly five unordered colliding rotation pairs, up to recording each pair inside its necklace, and all three ambiguous necklaces have four ones.

The full length-eight distribution of the number of distinct rotation profiles per necklace is
\[
\begin{array}{c|rrrrrr}\text{number of profiles}&1&2&4&6&7&8\\\hline
\text{number of necklaces}&2&1&3&2&1&27\end{array}.
\]

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). Subsequence positions are strictly increasing; subsequences are *scattered* (not necessarily contiguous), and multiplicities are retained. A necklace identifies words modulo cyclic rotation, not reversal or complement. Two different cut indices with identical rooted words (possible for periodic necklaces) are **not** counted as an ambiguity. The claim concerns the linear subsequence profile of each length-\(n\) rooted traversal, with no wraparound inside a subsequence. Only lengths at most eight are classified.

## Proof

**Reduction.** Equality of full three-binomial profiles implies equality of two-binomial profiles by definition. If the word is \(w=UV\) with \(|U|=s\), \(n=|w|\), \(A=|w|_0\) zeros, and \(a=|U|_0\) zeros, then direct counting of scattered `01` gives
\[
\binom{UV}{01}-\binom{VU}{01}=a(n-A)-(s-a)A=na-As.
\]
Consequently, if the two rooted words are three-binomially equivalent then \(na=As\). When \(0<A<n\), writing \(d=\gcd(A,n-A)\), any cut joining equal-profile rotations must have \(s\) divisible by \(n/d\). This simple arithmetic restriction excludes many potential pairs but is not used as a substitute for the exhaustive census below.

**Exact finite census.** The attached program `verify.py` implements the following deterministic exhaustive procedure. For each \(n=1,2,\ldots,8\), enumerate **all** \(2^n\) binary words and keep exactly the lexicographically least rotation from each necklace. For each such representative \(w\), enumerate every cut \(0\le i<n\), group the rooted words \(\rho_i(w)\) by the complete vector \(\mathcal D_3\), and retain a group as a collision only if it contains two different words. A direct definition-level subroutine evaluates every coordinate \(\binom{w}{u}\) by summing over every strictly increasing choice of \(|u|\) positions. Independently, a left-to-right subsequence recurrence constructs the same coordinates and is asserted to agree for every root. All loops and comparison predicates are supplied as executable, finite, standalone Python code and are small enough for complete reproduction.

The resulting exact counts are:

| \(n\) | Number of necklaces | Ambiguous necklaces |
|---:|---:|---:|
| 1 | 2 | 0 |
| 2 | 3 | 0 |
| 3 | 4 | 0 |
| 4 | 6 | 0 |
| 5 | 8 | 0 |
| 6 | 14 | 0 |
| 7 | 20 | 0 |
| 8 | 36 | 3 |

At length eight the same enumeration produces exactly the three complete collision-class lists in the theorem; comparing sets of **rooted strings** rather than indices ensures periodic rotations do not create false ambiguities. This establishes both the lower-length exclusion and the exhaustive length-eight classification.

**Direct sharpness witness.** The rotations `10110001` and `11000110` of the necklace `00011011` are different, but in the pattern order `000,001,010,011,100,101,110,111` their length-three scattered-subsequence count vectors both equal
\[
(4,6,6,3,12,12,9,4).
\]
The checker also verifies their length-one and length-two counts, as required by the definition. Thus the cutoff at eight is attained.

## Verification

Run `python3 verify.py` using only the Python standard library. It enumerates all 510 binary words of lengths one through eight and all rooted rotations of their 93 canonical necklaces; computes and compares the complete three-binomial profile by direct position combinations and by an independent dynamic recurrence; checks the full length-by-length distributions and exact exceptional cut classes; and cross-checks the independently published total counts of globally distinct length-three decks at lengths three through eight. Successful completion ends in `VERIFY_OK`. Both underlying arithmetic computations are exact integers, with no randomness, solver tolerance, or extrapolation. The proof is a finite exhaustion, not a statement about larger lengths.

## Relationship to prior work

Rigo and Salimov introduced finite-word binomial equivalence and studied the complexity of infinite words including Thue–Morse and Sturmian words; that general theory supplies the measurement concept but not the sharp rooted circular reconstruction threshold. Chrisnata and collaborators computed the total number \(D_3(n)\) of three-decks of all binary length-\(n\) words (not the number of decks obtained by rotating each individual necklace). Their counts \(D_3(7)=126\) and \(D_3(8)=247\) provide a useful independent benchmark: global three-deck ambiguity already exists at length seven, while ambiguity **inside a necklace** first occurs at eight. A separate earlier treatment of the finite Thue–Morse iterates determines the rotation profiles for that one infinite family, including the length-eight necklace `00101101`; that case is credited as prior, and is not claimed anew. The present contribution is the universal sharp cutoff and complete set of three exceptional necklaces and their colliding cut classes.

## Limitations

No unrestricted statement about \(n\ge9\), larger alphabets, other deck orders, deletion correction, or experimental read noise follows. The global-deck literature reports counts rather than the orbit-conditioned classification and was not available here in full publisher PDF; an unindexed finer enumeration could affect historical priority. The finite result should be independently reproduced and assessed before external scientific certification.

## References

1. M. Rigo and P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words*, 2013 open-access manuscript, https://orbi.uliege.be/handle/2268/149313 (public since 2013-05-27); also Theoret. Comput. Sci. 601 (2015), 47–57.
2. J. Chrisnata, H. M. Kiah, S. R. Karingula, A. Vardy, E. Yaakobi and H. Yao, *On the Number of Distinct k-Decks: Enumeration and Bounds*, Advances in Mathematics of Communications 17 (2023), 960–978; first conference version 2019; https://doi.org/10.3934/amc.2021032.
