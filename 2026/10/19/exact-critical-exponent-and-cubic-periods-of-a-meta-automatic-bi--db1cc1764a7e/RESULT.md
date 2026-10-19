# Exact critical exponent and cubic periods of a meta-automatic binary word

## Finding
Let \(\mu\) be the \(4\)-uniform morphism on \(\{0,1,2,3\}\) defined by
\[
\mu(0)=0112,\quad\mu(1)=1230,\quad\mu(2)=2301,\quad\mu(3)=3023.
\]
Let \(Z=\mu^\omega(0)\) and let \(B=\pi(Z)\), where \(\pi(0)=\pi(2)=0\) and \(\pi(1)=\pi(3)=1\). This is the binary sequence \(M_1\) of Campbell and Cloitre.

**Theorem.** The critical exponent of \(B\) is **exactly \(5\)**. More precisely, whenever a factor of \(B\) is a cube of a word of length \(p\), necessarily \(p\in\{2,6\}\). The longest \(p\)-periodic factors have lengths \(10\) for \(p=2\) and \(26\) for \(p=6\); in particular \(1010101010\) occurs at zero-based position \(2\) and realizes exponent \(5\).

## Assumptions and scope
All factors are contiguous and nonempty. A factor \(u\) has period \(p\) if \(u_i=u_{i+p}\) for \(0\le i<|u|-p\); its exponent is its length divided by its **least** positive period. The critical exponent is the supremum of these exponents over all factors. Here a cube of period \(p\) means a length-\(3p\) factor with period \(p\), whether or not \(p\) is its least period. All positions begin at zero.

## Proof
**Exact finite-factor principle.** Write \(P\) for the set of adjacent ordered pairs appearing in \(Z\). A direct substitution closure gives
\[
P=\{01,02,03,11,12,13,21,22,23,30\}.
\]
Indeed every symbol occurs in an iterate of \(0\); start with the within-image pairs in the four \(\mu(a)\)'s, then repeatedly add the boundary pair consisting of the last letter of \(\mu(a)\) and the first of \(\mu(b)\) whenever \(ab\) has been obtained. The displayed set is the resulting fixed point, hence contains all actual adjacent pairs. Every generated pair appears in the fixed point, proving equality.

For each \(L\ge1\), choose the least positive integer \(k\) such that \(4^k\ge L\). Every length-\(L\) factor of \(Z\) lies inside \(\mu^k(ab)\) for some \(ab\in P\), because it crosses at most one boundary between consecutive level-\(k\) blocks. Conversely, all such \(\mu^k(ab)\) occur in \(Z\). Thus the union of the length-\(L\) factors of those ten finite words is **exactly** the length-\(L\) factor set of \(Z\). Applying \(\pi\) gives the identical principle for \(B\). The starting position modulo \(4\) is the factor's local offset modulo \(4\) within the enumerated word.

**A desubstitution lemma.** The exact finite-factor calculation yields 100 distinct length-\(15\) factors of \(Z\), each occurring in a unique position residue modulo \(4\). It also finds no factor of \(Z\) having length \(2p+1\) and period \(p\) for any \(1\le p\le13\). Both assertions are finite equalities produced by `verify.py` using the preceding exact-factor principle.

We prove from them that \(Z\) is overlap-free, i.e. has no factor of length \(2p+1\) and period \(p\) for any positive \(p\). Suppose otherwise and choose an overlap with least possible period \(p\). The finite calculation forces \(p\ge14\). Within that overlap, the length-\(15\) factors at offsets \(0\) and \(p\) are identical, so unique position residues imply \(4\mid p\). Write \(p=4q\) and write the overlap's starting position as \(4s+r\), \(0\le r<4\). Because the first letters of \(\mu(0),\ldots,\mu(3)\) are pairwise different, comparing the overlap at positions \(4j-r\) and \(4j-r+p\), for \(1\le j\le q\), shows
\[
Z_{s+j}=Z_{s+q+j}.
\]
For \(j=0\), if \(r=0\) compare the first letters at relative offset \(0\); if \(r>0\) compare the **last** letters at relative offset \(3-r\), noting that the four image-ending letters \(2,0,1,3\) are distinct. This also yields \(Z_s=Z_{s+q}\). Hence \(Z_s\cdots Z_{s+2q}\) is an overlap of period \(q<p\), contradiction. Thus \(Z\) is overlap-free.

**Large cubes cannot survive the binary coding.** The exact finite-factor calculation finds 186 length-\(29\) factors of \(B\), each in a unique position residue modulo \(4\). Suppose \(B\) contains a length-\(3p\) factor with period \(p\ge15\). Comparing length-\(29\) factors a distance \(p\) apart forces \(4\mid p\). Write \(p=4q\), \(q\ge4\), and the starting position as \(4s+r\). The four binary image blocks
\[
\pi\mu(0)=0110,\quad\pi\mu(1)=1010,\quad
\pi\mu(2)=0101,\quad\pi\mu(3)=1001
\]
are pairwise distinct. If \(r=0\), the cube of binary blocks forces a length-\(3q\) factor of \(Z\) with period \(q\), contrary to overlap-freeness. If \(r>0\), compare complete binary blocks at relative offsets \(4j-r\), \(1\le j\le2q-1\), with blocks a distance \(p\) later. Their equality and injectivity of the binary block map yield a factor \(Z_{s+1}\cdots Z_{s+3q-1}\) of length \(3q-1\) with period \(q\). Since \(q\ge4\), this contains an overlap of length \(2q+1\), another contradiction. Therefore every cube of \(B\) has \(p\le14\).

**Exact short-period census.** The exact-factor principle gives 592 different binary length-\(85\) factors. For each \(1\le p\le14\), calculate the greatest length of a \(p\)-periodic substring in any of those factors. In period order \(1,2,\ldots,14\), the complete resulting tuple is
\[
(2,10,6,10,10,26,14,18,17,18,18,26,20,36).
\]
Each maximum is less than \(85\), so it is not an artificial endpoint truncation: every shorter factor of the infinite word extends to length \(85\), and any putative longer periodic run would have a length-\(85\) periodic subfactor. Thus these are **global exact** maximal lengths, not sample-prefix estimates. Comparing each entry with \(3p\) leaves only \(p=2\) and \(p=6\) as possible cube periods. Their attainable maximal exponents are \(10/2=5\) and \(26/6=13/3\), respectively. A factor with exponent greater than \(5\) would contain a cube of its least period. This is impossible, by the large-period argument and short-period census. Finally, direct expansion verifies that the factor at position \(2\) is \(1010101010\), of least period \(2\). Therefore the critical exponent is exactly \(5\), as asserted.

## Verification
Run `python3 verify.py` in a directory containing the standalone accompanying script. The script uses only the Python standard library and checks: all ten adjacent pairs; the complete 100-factor and 186-factor phase-uniqueness certificates; the finite overlap exclusion through period 13; the exact 592-factor length-85 language and all fourteen maximal periodic lengths; comparison against independently expanded finite prefixes; and the exhibited fifth-power factor. `verification_output.txt` contains the observed output. These finite computations are used **only** at the precisely identified finite-certificate steps of the preceding infinite argument.

## Relationship to prior work
Campbell and Cloitre introduce this exact automatic word and analyze its defining recurrences, morphism, and factor complexity; their inspected presentation does not give its critical exponent or complete cubic-period classification [1]. Schaeffer and Shallit prove that critical exponents of automatic sequences are effectively computable in general, without computing the number for this specific word [2]. The present work gives a direct proof and finite reproducible certificates for the exact special-word value.

## Limitations
The result is specific to \(M_1\) with the displayed coding. It does not determine the critical exponent of the authors' second sequence or classify all noncubic fractional powers. The novelty comparison cannot exclude unindexed or differently described earlier treatments; independent validation has not been performed.

## References
[1] John M. Campbell and Benoît Cloitre, *Meta-automatic Sequences*, arXiv:2602.23395 (first submitted February 25, 2026), https://arxiv.org/abs/2602.23395 .

[2] Luke Schaeffer and Jeffrey Shallit, *The Critical Exponent is Computable for Automatic Sequences*, arXiv:1104.2303 (2011), https://arxiv.org/abs/1104.2303 .
