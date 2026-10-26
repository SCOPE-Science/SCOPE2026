# Five-run rigidity and the first collisions of binary factor-composition spectra

## Finding
For a nonempty finite binary word \(w\), let \(\Pi(w)\) be the **set**, without multiplicities, of Parikh vectors \((|u|_0,|u|_1)\) of all its nonempty contiguous factors \(u\). A run is a maximal constant-symbol block, and \(w^{\mathrm{rev}}\) is its reversal.

**Sharp reconstruction theorem.** For any two nonempty binary words \(u,v\), each with at most five runs,
\[
 \Pi(u)=\Pi(v)\quad\Longrightarrow\quad v\in\{u,u^{\mathrm{rev}}\}.
\]
Five is sharp: for every integer \(t\ge2\), the six-run words
\[
 u_t=0101\,0^t1,\qquad v_t=01\,0^t101
\]
are distinct, are not reversals, and satisfy \(\Pi(u_t)=\Pi(v_t)\). Explicitly their shared Parikh spectrum, partitioned by number \(j\) of ones, is
\[
\begin{array}{c|c}
 j&\{i:(i,j)\in\Pi(u_t)\}=\{i:(i,j)\in\Pi(v_t)\}\\\hline
 0&\{1,\ldots,t\}\\
 1&\{0,\ldots,t+1\}\\
 2&\{1,\ldots,t+2\}\\
 3&\{t+1,t+2\}
\end{array}.
\]
Moreover, the smallest length admitting two nonreversal binary words with identical factor-Parikh sets is exactly seven, as witnessed by \(u_2=0101001\) and \(v_2=0100101\).

## Assumptions and scope
The alphabet is the labeled binary alphabet \(\{0,1\}\); exchanging the labels is **not** an allowed equivalence. A factor is contiguous, not scattered. Factor multiplicities, order, and occurrence positions are not supplied. Both input words may have different run counts, provided each has at most five runs; their lengths and symbol totals are not assumed known in advance, but are recoverable from the unique maximal-sum vector. Reversal is intrinsically invisible to \(\Pi\). The collision family requires \(t\in\mathbb Z\), \(t\ge2\). The inverse construction below proves uniqueness in the restricted domain, not among arbitrary unrestricted binary words.

Write \(Z=|w|_0\), \(O=|w|_1\), and, for any \(j\) for which such vectors occur, define
\[
 L(j)=\min\{i:(i,j)\in\Pi(w)\},\qquad
 U(j)=\max\{i:(i,j)\in\Pi(w)\}.
\]
The set also reveals \(M_0=\max\{i:(i,0)\in\Pi(w)\}\) and \(M_1=\max\{j:(0,j)\in\Pi(w)\}\), with the maximum over an empty set interpreted as zero. These are exactly the longest zero-run and one-run lengths.

## Proof
### Step 1: the number of runs is recognizable up to five
The total counts \((Z,O)\) are recoverable as the unique factor composition whose coordinate sum is \(|w|\). If one symbol is absent, the word is constant. Suppose \(Z,O\ge1\). Then \(M_0=Z\) precisely when all zeros form one run, and \(M_1=O\) precisely when all ones form one run. Thus both equalities indicate two runs, and exactly one indicates three runs. In the three-run case, the central run is the entire occurrence set of its symbol, while the two outer run lengths sum to the other symbol total and their maximum is the corresponding \(M_i\). Therefore the two outer lengths are recovered as an unordered pair, which is sufficient up to reversal.

If \(M_0<Z\) and \(M_1<O\), a word with at most five runs has four or five. Determine the two spectrum properties
\[
 P_0:\ \exists j<O\ (Z,j)\in\Pi(w),\qquad
 P_1:\ \exists i<Z\ (i,O)\in\Pi(w).
\]
For a four-run word, both hold: reverse if necessary to write \(w=0^a1^b0^c1^d\), where all zeros occur together in a factor with \(b<O\) ones, and all ones in a factor with \(c<Z\) zeros. A five-run word starting and ending in zero has \(P_1\) true, by the factor \(1^b0^c1^d\), and \(P_0\) false: any factor containing all three zero runs must contain both intervening one runs. A five-run word starting and ending in one has the reversed truth pattern by symbol exchange. Thus the support identifies four versus five runs and, in the five-run case, the outer symbol.

### Step 2: reconstruction of four runs
Reversal makes the four-run word \(0^a1^b0^c1^d\), with all parameters positive. Since any factor containing every one contains the full intervening zero run, the least zero count at \(j=O\) is \(L(O)=c\). Consequently \(a=Z-c\). For each integer \(1\le j\le O\),
\[
 U(j)=\begin{cases}
 \max(a,c),&1\le j<b,\\
 Z,&b\le j\le O.
 \end{cases}
\]
Indeed, a factor using fewer than \(b\) ones cannot bridge the first full one-run and hence cannot contain both zero runs; either zero run is individually attainable with exactly \(j\) adjacent ones. Conversely, when \(j\ge b\), take the entire first one-run, both zero runs, and \(j-b\) ones from the last run. Since \(a,c>0\), \(\max(a,c)<Z\). Therefore
\[
 b=\min\{j\ge1:U(j)=Z\},\qquad d=O-b.
\]
All four run lengths are recovered.

### Step 3: reconstruction of five runs
By exchanging the labels when needed, take \(w=0^a1^b0^c1^d0^e\), all five lengths positive. Every factor containing all \(O=b+d\) ones contains the full central zero run, while taking precisely \(1^b0^c1^d\) realizes \(c\) zeros. Thus \(L(O)=c\), and \(a+e=Z-c\). The maximum length of a one-only factor is \(M_1=\max(b,d)\); knowing also \(O\), recover the unordered pair \(\{b,d\}\).

Set \(q=\max(b,d)\). Then
\[
 U(q)=c+\max(a,e).
\]
To see the lower bound, the factor containing the entire first one-run, the central zeros and up to all \(a\) leading zeros realizes \(a+c\) zeros with \(q\) ones when \(q=b\). Similarly, for \(q=d\) the factor through the second one-run realizes \(c+e\). For the opposite side when its one-run is shorter, use the entire shorter one-run plus enough terminal ones of the longer run: this still includes the central zeros and its adjacent outer zero run, so both \(a+c\) and \(c+e\) are attainable with \(q\) ones. Any factor containing zeros from *both* outer runs necessarily contains all \(b+d>q\) ones, and a factor not doing so has at most \(c+\max(a,e)\) zeros. Hence the equality. It gives \(\max(a,e)=U(q)-c\) and therefore the unordered pair \(\{a,e\}\).

If \(a=e\) or \(b=d\), this information already determines the word up to reversal. Otherwise put \(s=\min(b,d)\) and \(M=\max(a,c,e)\). Since \(s<\max(b,d)\), a factor containing exactly \(s\) ones can bridge the shorter one-run completely but cannot bridge the longer one-run completely. Therefore
\[
 U(s)=\begin{cases}
 \max\{M,c+a\},&b<d,\\
 \max\{M,c+e\},&d<b.
 \end{cases}
\]
Here \(M\) is attainable by adjoining \(s\) ones to any of the three zero runs; a factor crossing both one runs without completing either adds at most \(c\) zeros. As \(c+\max(a,e)>M\), the equality \(U(s)=c+\max(a,e)\) holds precisely when the shorter one-run is adjacent to the larger *outer* zero run. This resolves the pairing of unequal outer and inner run lengths. The only remaining simultaneous exchange is reversal. All possible words with up to five runs have been reconstructed.

### Step 4: six-run ambiguity and minimal length
For every \(t\ge2\), the words \(u_t=0101\,0^t1\) and \(v_t=01\,0^t101\) contain \(t+2\) zeros and three ones, have six nonempty runs, and are not reversals. Direct factor analysis gives the stated four rows of their common spectrum. For \(j=0\), the longest zero run has length \(t\); for \(j=1\), the middle one adjacent to the long zero block yields every zero count from zero to \(t+1\); for \(j=2\), factors spanning appropriate adjacent one-runs yield every count from one to \(t+2\); and for \(j=3\), all one-runs must be spanned, forcing \(t+1\) internal zeros and allowing at most one additional outer zero. No larger \(j\) is possible. This proves the equality of spectra and failure of uniqueness.

At lengths at most five, every binary word has at most five runs, so the reconstruction theorem applies. At length six, any six-run word is strictly alternating, with both monochromatic-run maxima equal to one. Another word with the same Parikh support must likewise have both maxima one, hence must also be strictly alternating; its only alternative is the reversal. Thus no nonreversal collision occurs below length seven; \(u_2,v_2\) attain seven.

## Verification
Run `python3 verify.py` using only Python's standard library. The verifier directly enumerates every nonempty contiguous factor, compares support classes modulo reversal for all words with at most five runs and lengths one through sixteen, and independently exercises the explicit reconstruction algorithm against those complete factors. It also tests all \(7^5=16807\) positive five-run parameter tuples with lengths between one and seven, and checks the complete six-run family for \(2\le t\le69\), including every row of the claimed spectrum. The expected message begins `VERIFY_OK`. These computations check bounded instances; the unrestricted theorem follows from the preceding run-by-run arguments, not from the finite tests.

## Relationship to prior work
Burcsi, Fici, Lipták, Ruskey and Sawada established that equality of complete binary factor-Parikh sets is equivalent to simultaneous equality of the zero and one prefix-normal forms; their general criterion (Theorem 4) does not itself give the five-run recovery formulas or sharp six-run boundary. Cunha and collaborators developed efficient indexing for run-length-compressible binary texts, focusing on query algorithms rather than inverse uniqueness. Afshar, Amir, Goodrich and Matias established that reversing a word preserves all ordinary yes/no jumbled-query answers; they studied stronger queries to remove this obstruction. Fleischmann and collaborators studied the coarser *single* prefix-normal equivalence and its palindromic representatives, not the simultaneous two-form reconstruction claimed here. The present contribution is the sharp low-run inverse theorem plus an infinite minimal-obstruction family, derived in the exact factor-Parikh support model.

## Limitations
The result concerns binary alphabets, a set-valued observation, and at most five runs; it makes no claim of unique reconstruction for six or more runs. Reversal cannot be distinguished, and the theorem does not reconstruct from a single prefix-normal form or from a bounded-length substring observation. The code verifies only finite ranges. Published equivalent specializations could exist in unindexed literature; the present comparison does not constitute an independent novelty certification.

## References
1. P. Burcsi, G. Fici, Z. Lipták, F. Ruskey and J. Sawada, *On Prefix Normal Words and Prefix Normal Forms*, arXiv:1611.09017, first public version November 28, 2016, especially Theorem 4 and Sections 2–3. https://arxiv.org/abs/1611.09017
2. L. Cunha, S. Dantas, T. Gagie, R. Wittler, L. Kowada and J. Stoye, *Fast and Simple Jumbled Indexing for Binary Run-Length Encoded Strings*, CPM 2017, LIPIcs 78, article 19. DOI:10.4230/LIPIcs.CPM.2017.19. https://doi.org/10.4230/LIPIcs.CPM.2017.19
3. R. Afshar, A. Amir, M. T. Goodrich and P. Matias, *Adaptive Exact Learning in a Mixed-Up World*, arXiv:2007.08787, 2020, Section 4, Lemma 9. https://arxiv.org/abs/2007.08787
4. P. Fleischmann, M. Kulczynski, D. Nowotka and D. B. Poulsen, *On Collapsing Prefix Normal Words*, arXiv:1905.11847, 2019, Sections 1–4. https://arxiv.org/abs/1905.11847
