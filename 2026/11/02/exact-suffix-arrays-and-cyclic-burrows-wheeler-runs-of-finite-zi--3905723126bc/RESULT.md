# Exact suffix arrays and cyclic Burrows–Wheeler runs of finite Zimin words

## Finding
Fix distinct, increasingly ordered letters \(a_1<a_2<\cdots<a_n\), and define \(Z_0=\varepsilon\), \(Z_n=Z_{n-1}a_nZ_{n-1}\). For \(n\ge1\), let \(S_n\) be the zero-based suffix array of \(Z_n\), with the shorter suffix preceding a proper extension, and let \(B_n\) be its **sentinel-free cyclic** Burrows–Wheeler transform, formed by sorting all cyclic rotations and taking their preceding letters. Put \(L=2^{n-1}-1\). Then \(S_1=(0)\), and for every \(n\ge2\),
\[
S_n=(2L)\mathbin{\Vert}(2S_{n-1})\mathbin{\Vert}(2S_{n-1}+1),
\]
where scalar operations act entrywise and \(\Vert\) means concatenation. The sorted rotations occur in **the same order** as the sorted suffixes.

The transform is \(B_1=a_1\). For every \(n\ge2\), its complete letter-by-letter expression is
\[
\boxed{B_n=a_2a_3\cdots a_n\,a_1\left(\prod_{j=n-1}^{2}a_j^{\,2^{n-j}-1}\right)a_1^{\,2^{n-1}-1},}
\]
with product indexed in descending order and empty for \(n=2\). The original, unrotated word is row \(n\), counting rows from one. In particular, its number of maximal constant-letter runs is \(r(B_1)=1\), \(r(B_2)=2\), and
\[
\boxed{r(B_n)=2n-1\quad(n\ge3).}
\]
Thus the transform has \(O(n)=O(\log|Z_n|)\) constant-letter runs and an exact rank-parametrized formula, despite \(|Z_n|=2^n-1\). (Storing every run length separately in binary can use more than \(O(n)\) bits.)

## Assumptions and scope
A suffix is a contiguous suffix of the literal finite word, and the suffix array uses ordinary lexicographic order with proper prefixes smaller than their extensions. No end marker is appended to the word. The cyclic transform takes all \(2^n-1\) full-length rotations; this differs from the standard transform of a word **with** an appended marker. The alphabet order is essential. The occurrences of \(a_n\) are unique, so the word is primitive and its cyclic rotations are all distinct.

## Proof
**1. Interleaved recursion.** Let \(W=Z_{n-1}=w_0w_1\cdots w_{L-1}\), and let \(\sigma(a_j)=a_{j+1}\). An immediate induction on the definition of the Zimin word gives
\[
Z_n=a_1\sigma(w_0)a_1\sigma(w_1)\cdots a_1\sigma(w_{L-1})a_1.
\]
Every zero-based even position therefore contains \(a_1\), and every odd position contains a letter strictly larger than \(a_1\).

**2. Exact suffix ordering.** The suffix at position \(2L\) is the singleton \(a_1\) and is first. Every other suffix starting at an even position \(2i\), \(0\le i<L\), is \(a_1\sigma(w_i)a_1\sigma(w_{i+1})\cdots a_1\). Comparing two such suffixes is equivalent to comparing \(W[i:]\) and \(W[j:]\): the separating \(a_1\)'s match, \(\sigma\) preserves symbol order, and if one projected suffix is a proper prefix the shorter interleaved suffix also ends first. Hence the remaining even-position suffixes occur in order \(2S_{n-1}\). The suffix starting at odd position \(2i+1\) has the form \(\sigma(w_i)a_1\sigma(w_{i+1})\cdots a_1\); two odd-position suffixes occur in the same order as their corresponding suffixes of \(W\), namely \(2S_{n-1}+1\). An even-position suffix starts with \(a_1\); an odd-position suffix starts with a larger symbol. This proves the stated recurrence.

**3. Cyclic and suffix orders coincide.** Consider two distinct suffixes. If neither is a prefix of the other, the rotations starting at those positions are compared at the same first unequal letter, hence in the same order. Otherwise, suppose the shorter suffix is a proper prefix of the longer one. The shorter ends in the final letter \(a_1\). The matching letter at the corresponding internal location of the longer suffix is also \(a_1\), hence at an even zero-based position, and its *next* letter is at an odd position and is greater than \(a_1\). The cyclic continuation of the shorter suffix, however, starts with \(Z_n[0]=a_1\). Thus the shorter suffix also induces the lexicographically smaller rotation. This handles all comparisons, proving equality of the two orders.

**4. Transform recurrence and primary row.** By Step 2 the suffix array starts with \(2L\), followed by positions \(2i\) with \(i\) in \(S_{n-1}\), and then positions \(2i+1\) in the same old order. The letters immediately preceding these starts cyclically are, respectively, \(a_2\), the sequence \(\sigma(B_{n-1})\) with the entry belonging to the old start \(i=0\) replaced by \(a_1\), and a final block of \(L\) copies of \(a_1\). Indeed, for \(i>0\) the predecessor of \(2i\) is \(\sigma(w_{i-1})\), whereas the predecessor of position zero is the final letter \(a_1\). For each odd start \(2i+1\), the predecessor is exactly \(a_1\).

Let \(h_n\) be the zero-based row occupied by start position zero. Since \(S_1=(0)\) and the start-zero position enters the second block of the recurrence, \(h_1=0\) and \(h_n=h_{n-1}+1=n-1\). Hence the primary BWT row is \(n\) in one-based indexing; the exceptional replacement in the old transform occurs at its row \(n-1\). Inductively, the old explicit formula has this occurrence of \(a_1\) immediately after the increasing prefix \(a_2\cdots a_{n-1}\). Raising all its other letters by one, making this single replacement, and adjoining the leading \(a_2\) and trailing \(a_1^L\) gives precisely the asserted descending-product expression. The base case \(n=2\) follows from \(B_1=a_1\).

**5. Counting maximal runs.** For \(n\ge3\), the explicit expression consists of \(n-1\) distinct singleton letters in its initial increasing block, one central \(a_1\), then \(n-2\) nonempty descending-symbol blocks, and one final \(a_1\) block; adjacent blocks have different letters. The total is \(2n-1\). For \(n=2\), the descending product is empty and the two adjacent \(a_1\) blocks merge, giving exactly two runs. Rank one has one run. This completes the proof.

## Verification
Run `python3 checker.py` with Python 3. It builds the finite Zimin words directly, sorts every suffix from scratch through rank \(11\), and sorts all cyclic rotations independently through rank \(9\). It checks the suffix-array recurrence, equality of suffix and rotation orders, the full transform, the primary row, and the run-count exceptions. Checked lengths range from \(1\) to \(2047\). These finite checks serve as reproducibility tests; the quantified theorem is established by Steps 1–5, not extrapolation.

## Relationship to prior work
Burrows and Wheeler introduced the cyclic transform in their May 10, 1994 report. Simpson and Puglisi characterized certain **fully clustered** BWT outputs and proved results over larger alphabets; their main form has one block per alphabet letter, whereas the present transform has \(2n-1\) runs for \(n\ge3\) and alternates an increasing and decreasing list of symbols. Brlek and collaborators obtained explicit BWT formulas for Thue–Morse and generalized Fibonacci/Tribonacci morphic words. Their example on the word \(abacaba=Z_3\) reproduces the rank-three specialization here; their general results concern different recursive families and do not imply the all-rank Zimin suffix-array or BWT expression. Fici and collaborators analyze palindromic structure of Zimin words rather than these lexicographic and compression invariants. The statement is made with these overlapping low-rank examples credited, not as a new definition of BWT or Zimin words.

## Limitations
The result does not concern the sentinel-terminated transform, alphabet re-orderings, arbitrary homomorphic images of Zimin patterns, or the limiting infinite-alphabet word as an infinite input to BWT. It does not prove an optimal run bound across all words with the same length/alphabet. Since \(Z_n\) uses \(n\) distinct letters, the universal lower bound of \(n\) BWT runs already follows simply from symbol presence, and the exact result provides a factor approaching two over this bound, not an optimality claim. Historical-priority completeness has not been independently established.

## References
1. M. Burrows and D. J. Wheeler, *A Block-sorting Lossless Data Compression Algorithm*, SRC Research Report 124, May 10, 1994. https://www.cs.jhu.edu/~langmea/resources/burrows_wheeler.pdf
2. J. Simpson and S. J. Puglisi, *Words with Simple Burrows-Wheeler Transforms*, Electronic Journal of Combinatorics 15 (2008), R83, published June 20, 2008. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v15i1r83/pdf/
3. G. Fici, T. Gagie, J. Kärkkäinen and D. Kempa, *A Subquadratic Algorithm for Minimum Palindromic Factorization*, preprint March 10, 2014. https://arxiv.org/abs/1403.2431
4. S. Brlek, A. Frosini, I. Mancini, E. Pergola and S. Rinaldi, *Burrows-Wheeler Transform of Words Defined by Morphisms*, 2019. https://flore.unifi.it/bitstream/2158/1171602/6/BWT-morphism_%20Last.pdf
5. A. Restivo and G. Rosone, *Burrows–Wheeler Transform and Palindromic Richness*, Theoretical Computer Science 410 (2009), 3018–3026. https://doi.org/10.1016/j.tcs.2009.03.008
