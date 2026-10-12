# Sharp coprime-to-three period rigidity for cubes in the base-\(3/2\) digit-parity word

## Finding
Let \(x_n\) be the parity of the sum of the digits in the canonical base-\(3/2\) representation of \(n\), for every \(n\ge0\). A finite factor \(x_s\cdots x_{s+L-1}\) has period \(p\) when
\[
x_{s+j}=x_{s+j+p}\qquad(0\le j<L-p).
\]
This definition does not require that \(p\) be the least period.

**Theorem (sharp coprime-to-three cube rigidity).** For every triple of integers \(s\ge0\), \(p\ge1\), \(L\ge3p\) with \(\gcd(p,3)=1\), if \(x_s\cdots x_{s+L-1}\) has period \(p\), then
\[
p=2,\qquad 6\le L\le9.
\]
The upper length is attained: \(x_{12}\cdots x_{20}=101010101\), a factor of length \(9\) and period \(2\). Thus the largest exponent \(L/p\) among all factors with any period coprime to \(3\) is precisely \(9/2\). In particular every fifth power in the sequence has period divisible by \(3\). Conversely, a fifth power of period \(3\) occurs at index \(18\):
\[
x_{18}\cdots x_{32}=(101)^5.
\]
Here and below powers of words and periods are combinatorial, not powers of an arithmetic generating function.

## Assumptions and scope
The base-\(3/2\) digit representation is the unscaled sesquinary representation studied by Dekking, not the separately normalized rational-base expansion whose digit parity defines a different sequence. For \(n\ge0\), take the least significant digit \(r\in\{0,1,2\}\) congruent to \(n\pmod3\), then replace \(n\) by \(2(n-r)/3\) and repeat until zero. The parity of the digit sum is \(x_n\); set \(x_0=0\). The block substitution in the cited source yields for every integer \(m\ge0\)
\[
(x_{3m},x_{3m+1},x_{3m+2})=(x_{2m},1-x_{2m},x_{2m}).\tag{1}
\]
We consider all starting indices, all positive candidate periods (not only least periods), and all factor lengths. The arithmetic restriction \(\gcd(p,3)=1\) is intrinsic to the length-three substitution. No conclusion is claimed about periods divisible by \(3\).

## Proof
**1. Alternating factors have at most nine letters.** Define \(y_m=x_{2m}\). By (1), for every \(m\ge0\),
\[
y_{3m}=x_{6m}=x_{4m}=x_{6m+2}=y_{3m+1}.
\]
Hence every run of four consecutive symbols of \(y\) has two consecutive equal symbols: every four consecutive nonnegative indices include some pair \(3m,3m+1\). In particular, \(y\) has no alternating factor of length four.

Assume a ten-letter factor of \(x\) alternates. Its nine adjacent edges include exactly three edges of the form \((3m+2,3m+3)\), for three consecutive values of \(m\). By (1), these edges connect \(y_m\) and \(y_{m+1}\). Their alternation would force four consecutive symbols of \(y\) to alternate, a contradiction. Therefore every alternating factor of \(x\) has length at most \(9\). The factor \(x_{12}\cdots x_{20}=101010101\), obtained from (1), demonstrates sharpness.

**2. No three consecutive letters agree.** Every aligned block \(x_{3m}x_{3m+1}x_{3m+2}\) equals either \(010\) or \(101\). Every factor of length three, regardless of starting residue modulo \(3\), contains one of the pairs \((3m,3m+1)\) or \((3m+1,3m+2)\). These pairs have unequal letters, so no factor \(000\) or \(111\) occurs. In particular, a factor of length at least \(3\) cannot have period \(1\).

**3. Cubes with nonternary period are alternating.** Let a factor of length \(3p\) have period \(p\ge2\) and \(\gcd(p,3)=1\). Write its period as the cyclic binary word \((u_i)_{i\bmod p}\); thus \(x_{s+j}=u_{j\bmod p}\) throughout the factor. At least \(p-1\) complete aligned blocks of the form \((x_{3m},x_{3m+1},x_{3m+2})\) lie wholly inside this factor: there are exactly \(p\) if \(s\equiv0\pmod3\), and \(p-1\) otherwise.

For each such block put \(r\equiv3m-s\pmod p\). By (1),
\[
(u_r,u_{r+1},u_{r+2})=(a,1-a,a),
\]
so both circular adjacent edges \(r\to r+1\) and \(r+1\to r+2\) have unequal endpoints. The aligned indices \(m\) are consecutive, and multiplication by \(3\) permutes residues modulo \(p\). Therefore the set \(S\) of residues \(r\) from these aligned blocks contains all but at most one residue modulo \(p\).

Fix any circular edge \(i\to i+1\pmod p\). It is covered by the displayed relations if \(r=i\) or \(r=i-1\). These residues are distinct because \(p\ge2\), and at most one residue is absent from \(S\). Thus every circular adjacent edge has unequal endpoints:
\[
u_{i+1}=1-u_i\qquad\text{for every }i\pmod p.
\]
Going once around the cycle forces \(p\) even, and the entire factor is alternating.

**4. Complete the classification.** A factor with period \(p=1\) and length at least \(3p\) is impossible by Step 2. For \(p\ge2\), Step 3 shows that a factor of length \(L\ge3p\) with \(\gcd(p,3)=1\) must alternate. By Step 1, \(L\le9\). Hence \(3p\le9\), giving \(p\le3\); the required evenness leaves only \(p=2\). This proves the main theorem. For shorter factors \(L<3p\), the exponent \(L/p<3\); for the longer factors the theorem gives \(L/p\le9/2\). The sharp length-nine factor above realizes exponent \(9/2\), proving the global restricted-period assertion. Any fifth power has \(L=5p\ge3p\), so its period cannot be coprime to \(3\). Finally the displayed period-three fifth power is checked directly using (1). \(\square\)

## Verification
The proof is symbolic and requires no exhaustive computation. The independently implemented digit-extraction checker in `verify.py` cross-checks the first \(5000\) bits against the recurrence, validates the aligned-block identities, scans cube periods coprime to \(3\) up to \(90\) in a prefix of length \(120000\), confirms the maximum alternating factor length within that prefix, and tests the circular edge-cover combinatorics for the first \(90\) periods. Reproduce with `python3 verify.py`; its stored output is `verification_output.txt`. These finite computations provide error checks, not an infinite proof.

## Relationship to prior work
Dekking's 2023 paper defines the unscaled base-\(3/2\) parity sequence, proves the relevant two-to-three block identity, and states Shallit's conjecture that its unrestricted critical exponent is \(5\). Dekking and Keane's earlier work explicitly notes a fourth power of the alternating word, without excluding all other coprime-to-three cube periods. Subsequent work of Cassaigne, Espinoza, Rigo, and Stipulanti (2026) establishes frequency and recurrence properties for the related rational-base words; its results on these properties do not give the present complete coprime-period cube classification. The OEIS entry A357448 gives the recurrence and initial terms but no such period-exclusion theorem. The present conclusion is a sharp restriction on a natural infinite period class, not a resolution of the whole critical-exponent conjecture.

## Limitations
This proves nothing about the possible cube periods divisible by \(3\) and does not establish the full critical exponent. The existence of a fifth power of period \(3\) is compatible with the theorem. The bibliographic comparison is bounded by the primary papers and searchable resources inspected; equivalent unpublished or unindexed results are possible. The 2014 article by Edgar, Olafson, and Van Alstine could not be retrieved at its cited URL; no claim of exhaustive negative coverage of that article is made.

## References
1. F. M. Dekking, *The Thue–Morse Sequence in Base 3/2*, Journal of Integer Sequences **26** (2023), Article 23.2.3; arXiv:2301.13563, first posted 2023-01-31. https://cs.uwaterloo.ca/journals/JIS/VOL26/Dekking/dek25.pdf
2. F. M. Dekking and M. Keane, *Two-block substitutions and morphic words*, Advances in Applied Mathematics **148** (2023), 102536; arXiv:2202.13548. https://arxiv.org/pdf/2202.13548
3. J. Cassaigne, B. Espinoza, M. Rigo, and M. Stipulanti, *Symbols frequencies in the Thue–Morse word in base \(3/2\) and related conjectures*, arXiv:2602.21895v1 (2026). https://arxiv.org/pdf/2602.21895
4. OEIS Foundation, A357448, *Fixed point starting with 0 of the two-block substitution*. https://oeis.org/A357448
