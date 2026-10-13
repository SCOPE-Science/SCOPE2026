# A progression-free positive-relative-density family of binary palindromes

## Finding
Let \(\mathcal P_2\) be the positive integers whose ordinary base-two expansions are palindromes. Define \(L_1=5\) and \(L_{k+1}=2L_k+3\), and put
\[
\mathcal A=\{n\in\mathcal P_2:\text{the binary length of }n\text{ equals some }L_k\}.
\]
Then \(\mathcal A\) contains no nonconstant three-term arithmetic progression, whereas
\[
\limsup_{N\to\infty}\frac{|\mathcal A\cap[1,N]|}{|\mathcal P_2\cap[1,N]|}\ge\frac13.
\]
In particular the assertion, asked in Question 27 of Pongsriiam--Saito, that *every* positive-upper-relative-density subset of the base-two palindromes contains three distinct terms in arithmetic progression is false.

## Assumptions and scope
All integers are positive. An \(L\)-bit palindrome has exactly \(L\) binary digits, with first and last digit equal to one. An arithmetic progression of length three is nonconstant, so its terms may be ordered \(x<y<z\) with \(x+z=2y\). The result concerns base \(2\) and upper *relative* density inside binary palindromes; it does not assert positive ordinary density inside all integers.

## Proof
**Lemma 1 (fixed-length rigidity).** No three distinct binary palindromes of the same length \(L\) form an arithmetic progression. Indeed, let \(u<v<w\) be such palindromes with common positive difference \(d\). Put \(j=\nu_2(d)\). Since \(u,v\) agree below binary position \(j\) and differ at position \(j\), palindromicity implies that their highest differing position is \(L-1-j\), as well. The order \(u<v\) forces the binary digit of \(u\) at position \(j\) to be zero and that of \(v\) to be one. The same argument for \(v<w\), whose difference again has valuation \(j\), forces the digit of \(v\) at \(j\) to be zero, a contradiction.

**Lemma 2 (small-first-term rigidity).** Let \(L=2h+1\ge5\) be odd, and suppose \(0<x<y<z\), \(x+z=2y\), and both \(y,z\) are \(L\)-bit binary palindromes. If \(x<2^h\), then \(x=3\). The smallest \(L\)-bit palindrome is \(m=2^{L-1}+1\), and the next is \(m+2^h\), since the center bit is the least expensive editable digit. The largest is \(M=2^L-1\) and the next smaller is \(M-2^h\). From \(z=2y-x\le M\) we obtain
\[
0\le y-m\le\frac{x-3}{2}<2^{h-1}.
\]
As there is no palindrome strictly between \(m\) and \(m+2^h\), this gives \(y=m\). Therefore \(z=2m-x=2^L+2-x\), so \(0\le M-z=x-3<2^h\). The corresponding maximal gap forces \(z=M\), hence \(x=3\).

Now suppose three members of \(\mathcal A\) satisfy \(x<y<z\) and \(x+z=2y\). Their lengths belong to the strictly increasing set \(\{L_k\}\). Since \(z<2y\), the lengths of \(y\) and \(z\) differ by at most one; distinct selected lengths differ by more than one. Thus \(y\) and \(z\) have the same length \(L_k\). If \(x\) has that same length, Lemma 1 is a contradiction. Otherwise \(x\) has length at most \(L_{k-1}\), necessarily \(k\ge2\), whence
\[
x<2^{L_{k-1}}<2^{(L_k-1)/2}.
\]
Lemma 2 forces \(x=3\). But all members of \(\mathcal A\) have binary length at least five, contradiction. Thus \(\mathcal A\) is three-progression-free.

Finally, at the cutoff \(N_k=2^{L_k}-1\), writing \(L_k=2h+1\), precisely \(2^h\) binary palindromes have length \(L_k\). The total number of binary palindromes with length at most \(2h+1\) is
\[
2\sum_{j=1}^h2^{j-1}+2^h=3\cdot2^h-2.
\]
Since every \(L_k\)-bit palindrome belongs to \(\mathcal A\),
\[
\frac{|\mathcal A\cap[1,N_k]|}{|\mathcal P_2\cap[1,N_k]|}
\ge\frac{2^h}{3\cdot2^h-2}>\frac13.
\]
The sequence \(N_k\to\infty\), proving the limsup claim.

## Verification
The standalone `verify.py` independently enumerates all palindromes with binary lengths \(3\) through \(18\), checks fixed-length three-progression exclusion, tests the small-first-term lemma at odd lengths through \(17\), verifies the first two selected length layers, and checks the exact counting formula. Its successful output is included as `verification_output.txt`. These checks are finite corroboration; Lemmas 1 and 2 and the length recursion constitute the infinite proof.

## Relationship to prior work
Pongsriiam and Saito (2023), *Palindromes and Antipalindromes in Short Intervals*, Question 27, ask whether a positive-upper-relative-density subset of \(\mathcal P_b\) must contain a three-term arithmetic progression. Their Theorem 12 instead classifies gaps with infinitely many palindrome-pair representations; it does not address this density-Roth property. The construction above provides an explicit negative answer in base \(2\), with a quantified relative density. Pongsriiam (2021) studies maximum progression lengths for decimal palindromes, not progression-free positive-relative-density subsets in base \(2\). Phunphayap and Pongsriiam (2023) study counts across bases, rather than progression-avoiding subsets.

## Limitations
Only base \(2\) is treated. The construction has positive *upper relative* density, not claimed positive lower relative density or positive ordinary density. It does not decide whether every finite coloring of the binary palindromes has a monochromatic three-term arithmetic progression, which is a different part of Question 27. The conditional hypothesis on selected binary lengths is essential to the particular construction; no analogous claim is made for all odd lengths.

## References
- P. Pongsriiam and K. Saito, *Palindromes and Antipalindromes in Short Intervals*, Journal of Integer Sequences 26 (2023), Article 23.9.5, Theorem 12 and Question 27, https://cs.uwaterloo.ca/journals/JIS/VOL26/Saito/saito1.pdf. Publicly published 2023-12-11.
- P. Pongsriiam, *Longest Arithmetic Progressions of Palindromes*, Journal of Number Theory 222 (2021), 362–375, DOI 10.1016/j.jnt.2020.10.018.
- P. N. Phunphayap and P. Pongsriiam, *A Complete Comparison for the Number of Palindromes in Different Bases*, AIMS Mathematics 8 (2023), 9924–9932, DOI 10.3934/math.2023502.
