# Reversal-freeness at length four for every nonbinary digit-sum residue word

## Finding
Let \(m\ge 3\) be an integer and define the infinite word \(T_m=(t_m(j))_{j\ge0}\) over \(\mathbb Z/m\mathbb Z\) by \(t_m(j)=s_2(j)\bmod m\), where \(s_2(j)\) counts the ones in the binary expansion of \(j\). Let \(\mathcal F_m(n)\) be its set of contiguous factors of length \(n\), \(\rho_m(n)=|\mathcal F_m(n)|\) its factor complexity, and \(r_m(n)\) the number of factors up to reversal, where two present factors are identified only when one is the reverse of the other.

**Theorem.** Every length-three factor whose reversal occurs is a palindrome; moreover, no length-four factor occurs together with its reversal. In particular, for every integer \(m\ge3\) and every \(n\ge4\), no length-\(n\) factor has a reversal occurring in \(T_m\), and
\[
r_m(n)=\rho_m(n)\qquad(n\ge3).
\]
The exact initial values are
\[
r_m(1)=m,\qquad r_m(2)=\frac{m(m+1)}2,\qquad r_m(3)=2m^2-m.
\]
The length-four threshold is sharp: length-three palindromes occur (in fact exactly \(2m\) distinct such palindromic factors occur).

## Assumptions and scope
These are one-sided infinite binary-digit-sum words with *binary base fixed at two*, reduced modulo every integer \(m\ge3\); not the distinct family formed by the digit sum in base \(m\). A factor is contiguous, not a scattered subsequence. Reversal is ordinary symbol reversal, not reversal followed by a symbol permutation. The claims apply to all indices and all lengths, with no eventuality or computational cutoff.

## Proof
For \(j\ge0\), the elementary carry identity \(s_2(j+1)-s_2(j)=1-v_2(j+1)\) gives the consecutive modular difference
\[
d_j=t_m(j+1)-t_m(j)\equiv1-v_2(j+1)\pmod m.
\]
Here \(v_2(k)\) is the largest exponent of two dividing the positive integer \(k\). Whenever \(j\) is even, \(d_j=1\). Consequently any two adjacent differences include a \(1\), since exactly one of \(j,j+1\) is even.

Consider a length-three factor \((a,b,c)\), with differences \(p=b-a\) and \(q=c-b\) in \(\mathbb Z/m\mathbb Z\). The preceding observation forces \(p=1\) or \(q=1\). If its reversal \((c,b,a)\) also occurs, applying the same observation to its differences \((-q,-p)\) forces \(p=-1\) or \(q=-1\). Since \(1\ne-1\pmod m\) for \(m\ge3\), the two conditions together force \((p,q)=(1,-1)\) or \((-1,1)\). Thus \(a=c\): **every pair of reversed present triples is a single palindrome**.

Suppose now that a length-four factor \(w=(a,b,c,d)\) and its reverse both occur. Each of the two length-three subfactors of \(w\) has its reverse as a subfactor of the reversed word, so the previous paragraph forces \(a=c\) and \(b=d\). Hence \(w=(a,b,a,b)\) is alternating. Its first two increments are \((\delta,-\delta)\), where \(\delta=b-a\); at least one must be \(1\), so \(\delta\in\{1,-1\}\). We next show \(\delta\ne-1\): if an alternating factor had differences \((-1,1,-1)\), then its starting index \(j\) must be odd, since \(d_j=1\) at every even index. The numbers \(j+1\) and \(j+3\) are consecutive even numbers. Exactly one is congruent to \(2\pmod4\), so exactly one of \(v_2(j+1),v_2(j+3)\) equals \(1\). Thus one of \(d_j,d_{j+2}\) equals \(0\), contradicting the required value \(-1\) (nonzero in \(\mathbb Z/m\mathbb Z\)). Therefore any alternating factor must have \(\delta=1\). But the reversal of \((a,b,a,b)\) is \((b,a,b,a)\), whose first increment is \(-\delta=-1\), which cannot occur. This contradiction proves that no length-four factor is present together with its reverse.

If some factor of length \(n>4\) occurred together with its reverse, its length-four prefix and the reversal of that prefix would also occur. This is impossible, proving reversal-freeness at all lengths \(n\ge4\). At length three the only factors whose reversal is present are palindromes, so no two *distinct* present factors are identified by reflection. Therefore \(r_m(n)=\rho_m(n)\) for all \(n\ge3\).

For completeness, every triple having increments \((p,q)\) with \(p=1\) or \(q=1\) does occur. Fix arbitrary residues \(a,p,q\). If \(p=1\), choose \(v\ge1\) with \(1-v\equiv q\pmod m\), choose \(k\ge0\) with \(s_2(k)\equiv a-(v-1)\pmod m\), and set \(j=2^v(2k+1)-2\). Then \(j\) is even, \(s_2(j)=s_2(k)+v-1\), and the two differences are \((1,1-v)\). If \(q=1\), choose \(v\ge1\) with \(1-v\equiv p\pmod m\), choose \(k\ge0\) with \(s_2(k)\equiv a-v\pmod m\), and set \(j=2^v(2k+1)-1\). Then \(j\) is odd, \(s_2(j)=s_2(k)+v\), and the two differences are \((1-v,1)\). For any desired nonnegative binary digit count \(h\), the integer \(2^h-1\) has digit sum \(h\), so the choices of \(k\) always exist. Hence all admissible triples occur. There are \(m\) choices of initial letter and \(2m-1\) choices of a pair of differences with at least one component equal to \(1\). Thus \(\rho_m(3)=2m^2-m\); precisely \(2m\) of these triples have increments \((1,-1)\) or \((-1,1)\), and these are the palindromes. All \(m^2\) two-letter words appear as prefixes of the present three-letter words, and all \(m\) letters appear. Reflection identifies an ordered pair with its reversal, yielding \(r_m(2)=m(m+1)/2\), while \(r_m(1)=m\). This proves every asserted count and the sharpness of length four. \(\square\)

## Verification
The accompanying standard-library Python program `check.py` constructs length-65536 prefixes by two independent methods (binary digit count and dyadic recursion) for each \(m=3,4,5,6,7,8\), directly checks all possible three-letter patterns and the factor and reflection statements up to length ten, and verifies the two-letter and three-letter counts. Run `python3 check.py`. The infinite theorem is established by the proof above, not inferred from these finite checks.

## Relationship to prior work
Allouche, Campbell, Li, Shallit and Stipulanti, *The reflection complexity of sequences over finite alphabets* (first public arXiv posting June 13, 2024), define the invariant and state in Question 62 that equality \(r_m(n)=\rho_m(n)\) for \(m=3\), \(n\ge3\) was already known, while a similar statement was suggested for larger moduli. The theorem above proves this equality simultaneously for every \(m\ge3\), including \(m=4\), and strengthens it to the absence of any reflected length-four factor. Allouche and Shallit's *Sums of Digits, Overlaps, and Palindromes* (2000) analyzes palindromes of these digit-sum words, but a bound on palindromic factors alone does not exclude two distinct mutually reversed factors. Blažek, Dvořáková and Pelantová, *Generalized reflection complexity* (2026), study a different \(H\)-complexity over binary alphabets and generalized binary Thue–Morse words; their results do not give the ternary-and-higher alphabet reversal-free statement here.

## Limitations
This result does not provide a closed form for the full factor complexity \(\rho_m(n)\) when \(n\ge4\); rather it proves that the reflection complexity equals it. It concerns only binary-base digit counts modulo \(m\ge3\). Historical literature may contain an equivalent observation under different terminology; the principal comparison is to the explicitly published question and inspected related work. No independent mathematical audit has been performed.

## References
1. J.-P. Allouche, J. M. Campbell, S. Li, J. Shallit, M. Stipulanti, *The reflection complexity of sequences over finite alphabets*, arXiv:2406.09302 (2024), especially Question 62, p. 31. https://arxiv.org/abs/2406.09302
2. J.-P. Allouche and J. Shallit, *Sums of Digits, Overlaps, and Palindromes*, Discrete Mathematics and Theoretical Computer Science 4 (2000), 1–10, especially Section 5. https://www.kurims.kyoto-u.ac.jp/EMIS/journals/DMTCS/volumes/abstracts/pdfpapers/dm040101.pdf
3. A. Blažek, L. Dvořáková, E. Pelantová, *Generalized reflection complexity*, arXiv:2610.14637 (2026), especially Section 6.2. https://arxiv.org/abs/2610.14637
