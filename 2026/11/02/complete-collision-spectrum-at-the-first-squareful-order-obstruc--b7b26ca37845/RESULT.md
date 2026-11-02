# Complete collision spectrum at the first squareful-order obstruction for power permutations

## Finding
For a permutation \(\sigma\) of \(\{1,2,\ldots,10\}\), let
\[
R_{\sigma}=\{i^{\sigma(i)}\bmod 10:1\le i\le10\},\qquad K(\sigma)=|R_{\sigma}|.
\]
The exact distribution among all \(10!=3,628,800\) permutations is
\[
\sum_{\sigma\in S_{10}}z^{K(\sigma)}=
9792z^{5}+537408z^{6}+1822464z^{7}+1175040z^{8}+84096z^{9}.
\]
In particular, \(5\le K(\sigma)\le9\), exactly \(84,096\) permutations miss only one residue, and the proportion of such almost-complete permutations is \(73/3150\).

## Assumptions and scope
Exponents are a bijection from the ten bases \(1,\ldots,10\) onto \(1,\ldots,10\), and powers are reduced modulo \(10\). The statistic counts distinct residues, not multiplicities. Modulus \(10=2\cdot5\) is the smallest even modulus with prime half \(p\) but nonsquarefree \(p-1\); it is therefore the first obstruction of this specific type in Leonetti's criterion for complete power-residue systems. This result concerns exactly modulus \(10\), not an asymptotic family.

## Proof
Let \(v_{i,j}\in\{0,\ldots,9\}\) be the least nonnegative residue of \(i^j\) modulo \(10\). For subsets \(J\subseteq\{1,\ldots,10\}\) and \(R\subseteq\{0,\ldots,9\}\), let \(D_i(J,R)\) count assignments of distinct exponents to the first \(i\) bases whose used-exponent set is \(J\) and whose resulting residue set is \(R\). Define \(D_0(\varnothing,\varnothing)=1\), with other initial entries zero. Then
\[
D_i(J\cup\{j\},R\cup\{v_{i,j}\})\mathrel{+}=D_{i-1}(J,R)
\quad\text{for every }j\notin J.
\]
This recurrence partitions every partial assignment uniquely according to its final exponent. Consequently, at \(i=10\), the exact coefficient of \(z^k\) is the sum of \(D_{10}(\{1,\ldots,10\},R)\) over all residue sets \(R\) of size \(k\). Binary masks for \(J\) and \(R\) implement these finite operations without approximation. Direct integer evaluation gives the five stated coefficients and zero at all other exponents; their sum equals \(10!\). This finite recurrence is an exhaustive proof, not sampling.

## Verification
The complete standalone implementation `verify.py` evaluates the recurrence with arbitrary-precision integers. An independent implementation `verify.cpp` enumerates all \(10!\) exponent permutations lexicographically, reducing each modular power by repeated multiplication, and checks the same five coefficients. Both return `VERIFY_OK`. The rational fraction \(84096/3628800=73/3150\) is exact.

## Relationship to prior work
Leonetti's 2018 paper expressly observes that modulus \(10\) is not nice; his 2026 sequel proves that even \(n\ge6\) is nice precisely when \(n/2\) is prime and \(n/2-1\) is squarefree. Those existence/nonexistence statements force the absence of the coefficient of \(z^{10}\), but do not determine the distribution among \(z^5,\ldots,z^9\). The present result gives the complete quantitative loss profile at the first prime-half squareful obstruction.

## Limitations
This classification is finite and says nothing about analogous distributions for larger moduli or asymptotic probabilities. The exact numbers are verified by finite exhaustive methods and are not an infinite-family theorem. Unindexed earlier enumerations remain possible.

## References
1. P. Leonetti, *A characterization of Sophie Germain primes – II*, arXiv:2609.20208 (first public 25 July 2026), Theorem 1.3, https://arxiv.org/abs/2609.20208.
2. P. Leonetti, *A characterization of Sophie Germain primes*, International Journal of Number Theory 14 (2018), 653–660; arXiv:1305.0893, Theorem 2 and introductory observation that \(10\) is not nice, https://arxiv.org/abs/1305.0893.
3. K. Kowitz, *Generalized “Riesel” numbers and nice numbers*, Discrete Mathematics, Algorithms and Applications 16 (2024), DOI:10.1142/S1793830924501040 (related existence constructions only).
