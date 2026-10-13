# Exact length-four binary \(B_3\)-codes
## Finding
Let \(C\subseteq\{0,1\}^4\). Call \(C\) a binary \(B_3\)-code when the coordinatewise integer sum
\[
\{u,v,w\}\longmapsto u+v+w\in\{0,1,2,3\}^4
\]
is injective on unordered multisets of three codewords, with repetitions allowed. Then \(|C|\le 6\). Exactly \(656\) labeled six-word codes attain equality. Under the full Hamming-isometry group \((C_2)^4\rtimes S_4\), the maximum codes form exactly six orbits of sizes
\[
16,\ 64,\ 96,\ 96,\ 192,\ 192,
\]
with stabilizer orders \(24,6,4,4,2,2\), respectively.

## Assumptions and scope
Addition in the definition is ordinary coordinatewise integer addition, not addition modulo two. An unordered multiset allows the same codeword to occur two or three times. “Labeled” means that the sixteen binary words of length four retain their coordinate labels; a code itself is an unordered subset. The acting group consists of arbitrary coordinate permutations together with independently complementing any coordinate in every word. The result is only for block length four and does not assert an asymptotic rate or a classification for other lengths.

## Proof
For a fixed candidate \(C\), enumerate all unordered three-element multisets of \(C\). For \(|C|=6\) there are \(\binom{8}{3}=56\) such multisets. The \(B_3\) condition is exactly that their 56 coordinatewise sum vectors are pairwise distinct.

There are \(\binom{16}{6}=8008\) six-subsets of \(\{0,1\}^4\). Exhaustive evaluation finds exactly \(656\) satisfying the \(B_3\) condition, so size six is attained. The property is hereditary under taking subsets. Therefore, if a code of size at least seven existed, some seven-subset would itself be a \(B_3\)-code. Exhaustive evaluation of all \(\binom{16}{7}=11440\) seven-subsets finds none, proving \(|C|\le6\).

For the equality classification, act on each of the 656 maximum codes by the \(384=2^4\cdot4!\) Hamming isometries. A coordinate permutation merely permutes coordinates of every three-sum. Complementing one coordinate sends that coordinate of every three-sum from \(s\) to \(3-s\), so the \(B_3\) property is preserved. Exact orbit enumeration partitions the 656 maxima into orbit sizes \(16,64,96,96,192,192\). Orbit-stabilizer then gives stabilizer orders \(384/16=24\), \(384/64=6\), \(384/96=4\), \(384/96=4\), \(384/192=2\), and \(384/192=2\).

Representatives of the six orbits are
\[
\begin{aligned}
&\{0000,0001,0010,0100,1000,1111\},\\
&\{0000,0001,0110,1010,1100,1111\},\\
&\{0000,0001,0010,0111,1011,1100\},\\
&\{0000,0001,0110,1010,1101,1111\},\\
&\{0000,0001,0010,0101,1011,1100\},\\
&\{0000,0001,0010,0111,1011,1101\}.
\end{aligned}
\]
Their pairwise Hamming-distance distributions for distances \(1,2,3,4\) are, in the same order,
\[
(4,6,4,1),\ (1,9,4,1),\ (2,7,6,0),\ (2,6,6,1),\ (3,6,6,0),\ (2,9,3,1).
\]

## Verification
The standalone `verify.py` reconstructs all sixteen words, checks the \(B_3\) predicate in two independently written encodings, enumerates all 8008 six-subsets and all 11440 seven-subsets, and independently partitions all maxima under all 384 Hamming isometries. It must terminate with
`VERIFY_OK maximum=6 labeled_maxima=656 orbits=6 orbit_sizes=16,64,96,96,192,192`.

The machine-readable census produced by the verifier has SHA-256 `b5e7a2ad97c9c608797740bd17f220c740fa1ae4623085f61478a1cf810d9748` when serialized exactly as specified in the verifier.

## Relationship to prior work
Derksen's 2003 paper gives the standard additive definition of a \(B_h\)-sequence and uses \(B_h\)-sequences to construct error-correcting codes; its tables concern bounds for ordinary Hamming codes rather than exact binary-cube \(B_h\)-code maxima. D'yachkov and Rykov's 1981 multiple-access paper defines the binary-column \(B_s\)-code model in which repeated-column sums must be distinct and derives general and asymptotic length bounds, but the inspected text does not give this length-four equality census or its Hamming-isometry classification. Gu's later treatment defines binary \(B_h\)-codes exactly as shared-codebook zero-error adder codes and focuses on asymptotic rates and random coding; its inspected full text likewise does not give this finite classification.

Thus the present statement is not a corollary of the cited general bounds or constructions: both the upper bound at this finite parameter and the complete equality-orbit census require an exact finite argument.

## Limitations
The upper bound is a finite exhaustive theorem, not a general inequality in the block length. The literature comparison cannot exclude an obscure or poorly indexed historical tabulation that was not found; in particular, the 1981 literature is old and partly available through translated or OCR-derived text. No claim is made about independent external validation.

## References
1. Harm Derksen, “Error Correcting Codes and \(B_h\)-Sequences,” arXiv:math/0311385v1, submitted 2003-11-21.
2. A. G. D'yachkov and V. V. Rykov, “On a Coding Model for a Multiple-Access Adder Channel,” Problems of Information Transmission 17(2) (1981), 94–104.
3. Yuzhou Gu, “Zero-error communication over adder MAC,” arXiv:1809.07364v1, submitted 2018-09-19.
