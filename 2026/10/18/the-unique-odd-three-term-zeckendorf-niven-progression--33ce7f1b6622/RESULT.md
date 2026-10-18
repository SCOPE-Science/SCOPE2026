# The unique odd three-term Zeckendorf–Niven progression

## Finding
Let \(F_2=1,F_3=2,F_{j+2}=F_{j+1}+F_j\) be Fibonacci numbers and let \(s_Z(n)\) denote the number of summands in the canonical Zeckendorf decomposition of the nonnegative integer \(n\), with \(s_Z(0)=0\). A positive integer \(n\) is Zeckendorf–Niven when \(s_Z(n)\mid n\). **Among all positive odd integers \(n\), the three terms \(n,n+2,n+4\) are all Zeckendorf–Niven if and only if \(n=1\).** Thus the only odd three-term progression is \((1,3,5)\).

The structural reason is the following universal *parity-rigidity lemma*: for every integer \(n\ge0\), if \(s_Z(n),s_Z(n+2),s_Z(n+4)\) have the same parity, then either \(s_Z(n)=s_Z(n+2)\) or \(s_Z(n+2)=s_Z(n+4)\).

## Assumptions and scope
The Fibonacci indexing is \(F_2=1,F_3=2,F_4=3,F_5=5\); Zeckendorf summands are nonconsecutive in index. The conclusion is unconditional for all positive odd starting values. It makes no claim about even starting values, for which longer runs are known.

## Proof
**1. Greedy count recurrence.** For each \(k\ge2\) and \(F_k\le n<F_{k+1}\), the highest Zeckendorf summand of \(n\) is \(F_k\), and \(0\le n-F_k<F_{k-1}\). Thus
\[
s_Z(n)=1+s_Z(n-F_k).
\]
The formula is also valid for \(n=F_k\), using \(s_Z(0)=0\).

**2. Boundary counts.** For \(k=2r\ge10\), the values \(s_Z(F_k-d)\) for \(d=4,3,2,1\), in that order, are
\[
(r-1,\ r-2,\ r-1,\ r-1).
\]
For \(k=2r+1\ge9\) they are
\[
(r-1,\ r-1,\ r-1,\ r).
\]
Direct Zeckendorf expansions of the four integers immediately below \(F_9=34\) give \((3,3,3,4)\); those immediately below \(F_{10}=55\) give \((4,3,4,4)\). To propagate the formulas, for \(k\ge11\) and \(1\le d\le4\) use \(F_k-d=F_{k-1}+(F_{k-2}-d)\), where \(0\le F_{k-2}-d<F_{k-2}\). Therefore \(s_Z(F_k-d)=1+s_Z(F_{k-2}-d)\). By induction on parity of \(k\), the displayed formulas follow for every indicated \(k\).

For \(0\le j\le4\) the counts \(s_Z(F_k+j)\) are \((1,2,2,2,3)\) whenever \(k\ge9\), since \(F_k+j\) has greedy leading summand \(F_k\) and the remainders \(0,1,2,3,4\) have counts \((0,1,1,1,2)\).

**3. Parity-rigidity induction.** Direct substitution using the greedy recurrence checks the lemma for \(0\le n<34\); the exact finite verifier repeats all \(34\) tests. Suppose the lemma holds below \(n\ge34\). Choose \(k\) so that \(F_k\le n<F_{k+1}\). If \(n+4<F_{k+1}\), then the three counts in question are each one greater than the corresponding counts at \(n-F_k\), \(n-F_k+2\), \(n-F_k+4\). Since \(n-F_k<n\), the induction hypothesis applies; parity equality and adjacent equality are both preserved when adding one.

Otherwise, let \(m=F_{k+1}\) and write \(n=m-d\), where \(1\le d\le4\); here \(m\ge F_{10}\). The three arguments are \(m-d,m-d+2,m-d+4\). From the formulas above, for either parity of the Fibonacci index, the cases \(d=2,3\) always contain two counts of opposite parity. For \(d=1\) the latter two counts are both \(2\); for \(d=4\) the former two counts are equal (\(r-1\) in either index parity). Hence whenever all three counts have the same parity, two adjacent counts coincide. This closes the induction.

**4. Odd progressions.** If positive odd integers \(n,n+2,n+4\) are all Zeckendorf–Niven, then their three positive counts \(s_Z\) are odd divisors of odd integers. The lemma forces one adjacent pair of counts to agree, say \(s_Z(n+2j)=s_Z(n+2j+2)=s\), where \(j\in\{0,1\}\). Their difference is \(2\), so \(s\mid2\). Because \(s\) is odd and positive, \(s=1\). Both adjacent numbers are therefore Fibonacci numbers. The only pairs of odd Fibonacci numbers differing by \(2\) are \((1,3)\) and \((3,5)\): the Fibonacci sequence begins \(1,2,3,5,8,13\) and thereafter successive gaps exceed \(2\); nonconsecutive gaps are still larger, except \(1,3\). Thus the starting value is \(n=1\), or \(n=3\) if the equal pair is its first two entries. The latter fails because \(s_Z(7)=2\) does not divide \(7\). Finally \(s_Z(1)=s_Z(3)=s_Z(5)=1\), so \((1,3,5)\) does qualify.

## Verification
Run `python3 VERIFY.py` using only the standard library; the packaged script returns `VERIFY_OK`. It recomputes the initial induction cases, the two boundary tables and symbolic parity cases, and tests the three-term lemma through \(n=99999\). These finite tests are ancillary; the recurrence induction proves the infinite claim.

## Relationship to prior work
Lao, Miller, Rosa, Shiliaev, Tresch, Wong and Zhang (arXiv:2606.24006, first publicly available 22 June 2026) proved broad existence in arithmetic progressions, established that the only step-two runs of length at least eight lie in \((2,4,\ldots,18)\), and constructed infinite five-term step-two runs. Their Section 4 does not state the odd-start three-term classification. The present lemma instead analyzes the parity of the Zeckendorf summand count at three consecutive odd arguments. The result is compatible with their longer even-start examples. Other work on Zeckendorf digit statistics does not, in the sources inspected, identify this local equal-neighbor rigidity.

## Limitations
Only the odd-start step-two three-term problem is classified; for even starts the cited source exhibits nine terms, and this theorem does not settle optimal run lengths outside those known examples. Originality assessment is based on available full texts and mathematical search and cannot exclude an unlocated equivalent consequence of general Fibonacci-automatic-sequence theory. The review is not independent validation.

## References
- K. Lao et al., *On Zeckendorf-Niven Numbers and Arithmetic Progressions*, arXiv:2606.24006v1 (22 June 2026), especially Sections 1, 4, 5; https://arxiv.org/html/2606.24006v1.
- Zeckendorf's canonical decomposition theorem, as stated in Theorem 1.1 of Lao et al.
