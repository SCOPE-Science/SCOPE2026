# Complete maximal-repetition spectra of finite binary Cantor words

## Finding
Let \(C_0=1\) and \(C_k=\mu^k(1)\), where \(\mu(1)=101\) and \(\mu(0)=000\). A **run** is a zero-based half-open interval \([a,b)\) with a least positive period \(p\), length \(b-a\ge 2p\), and no one-symbol extension on either side within the ambient word preserving period \(p\). Runs are counted by position, not merely by their distinct factor values.

For every \(k\ge1\), the following two families are **all** runs of \(C_k\), without duplication.

1. Every maximal zero block of length \(3^e\), for \(1\le e\le k-1\), is a run of least period \(1\). There are \(2^{k-e-1}\) such blocks.
2. For every \(0\le j\le k-2\) and every position \(t\) of a \(1\) in \(C_{k-j-1}\), put \(h=k-j\), \(B=3^h\), and
   \[
   a=3^j\max\{0,3t-1\},\qquad
   b=3^j\min\{B,3t+4\},\qquad
   p=2\cdot3^j.
   \]
   Then \(([a,b),p)\) is a run. At each \(j\) there are exactly \(2^{k-j-1}\) such runs: two have length \(4\cdot3^j\), and the remaining \(2^{k-j-1}-2\) have length \(5\cdot3^j\).

In particular, the non-unit least periods are exactly \(2\cdot3^j\) for \(0\le j\le k-2\). The total number of runs and their total length are, respectively,
\[
\rho(C_k)=3\cdot2^{k-1}-3,\qquad
\operatorname{TRL}(C_k)=4\cdot3^k-13\cdot2^{k-1}+1.
\]
Thus \(\rho(C_k)/3^k\to0\) while \(\operatorname{TRL}(C_k)/3^k\to4\).

## Assumptions and scope
The alphabet is \(\{0,1\}\); factors are **contiguous**, and \(p\) denotes the **least** period, not an arbitrary period. All run endpoints are indices in the finite word \(C_k\), with \(0\le a<b\le3^k\). For \(k=1\) there are no runs, and the formulas give zero. No claim is made here about all finite prefixes of the infinite Cantor word, factors of arbitrary lengths, or Abelian repetitions.

## Proof

**1. Ternary block and gap facts.** The morphism preserves the absence of `11`: \(C_k\) begins and ends with `1`, has no adjacent ones, and has exactly \(2^k\) ones. Each source `1` produces a block `101`, whose paired ones are at residues \(0\) and \(2\) modulo \(3\). Every position congruent to \(1\) modulo \(3\) is zero. A one at residue \(0\) has a partner two positions to its right; a one at residue \(2\) has a partner two positions to its left. These partner positions lie in the word because they belong to the same substitution block.

Index the ones of \(C_k\) from \(0\) to \(2^k-1\). Their positions are obtained by expressing the index with \(k\) binary digits and replacing each binary digit \(1\) by ternary digit \(2\). On passing from one index \(i-1\) to the next \(i\), if \(e=\nu_2(i)\), the difference between their positions is \(3^e+1\). Indeed, the carry replaces \(e\) lower ternary `2` digits by `0` and changes the next `0` to `2`, for net displacement \(2\cdot3^e-2\sum_{s=0}^{e-1}3^s=3^e+1\). Thus the maximal zero blocks have lengths \(3^e\), and the number with exponent \(e\) is \(2^{k-e-1}\), for \(0\le e\le k-1\). Exactly those with \(e\ge1\) are period-one runs.

**2. The possible periods of a square containing a one.** Suppose \(C_k[a:a+2p]=UU\) is a square containing at least one one. If \(p\equiv1\pmod3\), the ones in the first copy must all have residue \(2\) modulo \(3\): a one of residue \(0\) would be matched in the second copy to residue \(1\), which is zero. Its corresponding one in the second copy has residue \(0\). Choose a one at offset \(r\) of the first copy. The partnered one two positions before it would violate the residue restriction unless \(r\le1\). The partnered one two positions after its second-copy mate would violate the restriction in the second copy unless \(r\ge p-2\). Hence \(p\le3\), impossible for positive \(p\equiv1\pmod3\) except \(p=1\); that case cannot contain a one because `11` does not occur.

If \(p\equiv2\pmod3\), the first-copy ones must have residue \(0\) and second-copy ones residue \(2\). The partner two positions after the first-copy one forces \(r\ge p-2\), while the partner two positions before its second-copy mate forces \(r\le1\). Again \(p\le3\), so \(p=2\).

If \(p=3q\), inspect just the positions divisible by \(3\) in both equal copies. They project, under \(C_k[3s]=C_{k-1}[s]\), to a square of period \(q\) in \(C_{k-1}\). This projected square contains a one: a one of residue \(0\) already projects, and if a one of residue \(2\) occurs in either copy, its mate in the **second** copy has a partnered one of residue \(0\) two places earlier, still inside the length-\(2p\) square since \(p\ge3\). Iterating the projection shows that every square containing a one has period \(p=2\cdot3^j\). In particular, the least period of any nonconstant run has this form. (All-zero factors have least period one.)

**3. Runs of least period two.** In \(C_h=\mu(C_{h-1})\), any length-four period-two factor containing a one is `0101` or `1010`. Its two ones are at distance \(2\); since different `101` image blocks are separated by at least three zeros, the two ones belong to a unique image block `101`, indexed by a position \(t\) at which \(C_{h-1}[t]=1\). The longest period-two factor around this block is `01010`, obtained by adding one zero on either side, provided that side is inside \(C_h\). A further extension would require another one at distance \(2\) from the leftmost or rightmost one, which cannot occur. Therefore the exact period-two runs are
\[
 [\max\{0,3t-1\},\min\{3^h,3t+4\}),
 \quad C_{h-1}[t]=1,
\]
provided \(h\ge2\). The first and last image blocks yield intervals of length \(4\); all others yield length \(5\). The number of runs is the number \(2^{h-1}\) of ones in \(C_{h-1}\). For \(h=1\), the whole word `101` is too short to contain a run.

**4. Exact inflation of nonconstant runs.** Let \(p=3q\) and let \(([a,b),p)\) be a nonconstant run of \(C_k\). If \(a\equiv2\pmod3\), the preceding symbols, both at residue \(1\), are zero, so period \(p\) extends left. If \(a\equiv1\pmod3\), the comparison at position \(a+1\) is valid (because the run has length at least \(2p\)); that comparison holds also at \(a-1\), since the residues \(0\) and \(2\) within each `101` or `000` image block are equal. Either case contradicts left maximality. Thus \(a\equiv0\pmod3\), including the left endpoint \(a=0\).

Similarly, if \(b\equiv1\pmod3\), the next symbols are both zero, so the run extends right. If \(b\equiv2\pmod3\), the comparison at \(b-2\) (and at \(b-p-2\)) is valid and implies the comparison at \(b\), because residues \(0\) and \(2\) in a substitution block agree. Thus \(b\equiv0\pmod3\). Projection gives the interval \([a/3,b/3)\) of period \(q\) in \(C_{k-1}\). Its least period must be \(q\), or its image would have a smaller period; it is maximal, since any one-symbol period-\(q\) extension would lift to a three-symbol period-\(p\) extension. Hence projection takes the original run to a nonconstant run of the previous level.

Conversely, the image under \(\mu\) of every nonconstant run of least period \(q\ge2\) has period \(3q\). Its least period is \(3q\): a shorter period \(d\) would, by step 2, be of the form \(2\cdot3^r\). The case \(d=2\) is impossible for a nonconstant image of at least two full blocks, because an aligned image beginning `000` cannot be nonconstant and period two, while an image beginning `101` would require its next three letters to be `010`, which is neither `000` nor `101`. For \(3\mid d\), projection gives a period \(d/3<q\) of the source factor, also impossible. The image is maximal: a left period-\(3q\) extension would equate the residue-\(2\) positions of two preceding source blocks, extending the source run to the left; a right extension would equate the residue-\(0\) positions of the following source blocks, extending it to the right. Consequently \(\mu\) is a bijection from nonconstant runs at the previous level to nonconstant runs with periods divisible by three at the current level. Repeated projection reduces every nonconstant run to the period-two family of step 3, and repeated inflation produces exactly the displayed intervals.

**5. Enumeration.** For each \(0\le j\le k-2\), step 4 lifts \(2^{k-j-1}\) distinct period-two runs at level \(k-j\), two of length \(4\cdot3^j\) and \(2^{k-j-1}-2\) of length \(5\cdot3^j\). Adding zero-block runs from step 1 gives
\[
\rho(C_k)=(2^{k-1}-1)+(2^k-2)=3\cdot2^{k-1}-3.
\]
Their total length is
\[
\sum_{e=1}^{k-1}3^e2^{k-e-1}
+\sum_{j=0}^{k-2}3^j\bigl[2\cdot4+(2^{k-j-1}-2)\cdot5\bigr]
=4\cdot3^k-13\cdot2^{k-1}+1.
\]
All claimed multiplicities, periods, lengths, and limits follow.

## Verification
The standalone `checker.py` independently enumerates all maximal least-period runs without using the proposed construction, and compares the resulting sets of interval-period triples to the explicit construction at every level \(1\le k\le6\). It separately verifies exact period/length histograms and the two total formulas. Direct results include \(\rho(C_2)=3\), \(\rho(C_3)=9\), \(\rho(C_4)=21\), \(\rho(C_5)=45\), and \(\rho(C_6)=93\); their total lengths are \(11,57,221,765,2501\). These finite checks support, but do not replace, the unrestricted proof above.

## Relationship to prior work
Baturo, Piątkowski and Rytter (2013) give run-count formulas for **standard Sturmian words**, whose defining recursion and factor structure differ from the Cantor morphism. Glen and Simpson (2013) introduce total run length and establish general extremal and average bounds over words, not a Cantor-word spectrum. General periodicity arguments alone do not imply the precise Cantor-word period, position, and length formulas above. The direct Cantor-specific classification, the full period-length distribution, and the total run length are the claims assessed here.

## Limitations
The classification is for complete iterates of the specified morphism. It does not treat arbitrary prefixes, general ternary substitutions, or Abelian and approximate periods. The literature comparison cannot eliminate the possibility that equivalent formulas have appeared in less accessible sources. The self-review is not independent mathematical validation.

## References
- P. Baturo, M. Piątkowski, and W. Rytter, “The maximal number of runs in standard Sturmian words,” *Electronic Journal of Combinatorics* **20**(1), P13 (2013). DOI: 10.37236/2473. First publicly dated version verified: 2013-01-21.
- A. Glen and J. Simpson, “The total run length of a word,” arXiv:1301.6568 (first submitted 2013-01-28); *Theoretical Computer Science* **501** (2013), 41–48.
