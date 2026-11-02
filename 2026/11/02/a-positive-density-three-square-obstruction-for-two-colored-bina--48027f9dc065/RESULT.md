# A positive-density three-square obstruction for two-colored binary partitions

## Finding
Let \(b_2(n)\) count partitions of \(n\) into powers of two with each part in either of two colors. For every integer \(t\ge0\),
\[
b_2(128t+36)\equiv b_2(128t+62)\equiv112\pmod{128}.
\]
Among all residues \(r\in\{0,1,\ldots,127\}\), exactly \(r=36,62\) satisfy \(b_2(128t+r)\equiv112\pmod{128}\) for every \(t\ge0\). In particular,
\[
\liminf_{X\to\infty}\frac1X\#\{0\le n<X:\ b_2(n)\text{ is not a sum of three integer squares}\}\ge \frac1{64}.
\]
No existence of a density, or equality with this lower bound, is claimed.

## Assumptions and scope
All arithmetic is in formal integer power series. Set
\[
B(x)=\prod_{j\ge0}(1-x^{2^j})^{-2}=\sum_{n\ge0}b_2(n)x^n.
\]
Its coefficients are strictly positive integers. The congruence is universal in the nonnegative integer \(t\), and the classification of residue classes is specific to modulus \(128\) and target residue \(112\). For three-square representability, zero-valued square variables are allowed.

## Proof
The product gives the functional equation \(B(x^2)=(1-x)^2B(x)\). The polynomial \(P(x)=1+2x+5x^2\) obeys
\[
(1-x)^2P(x)-P(x^2)=-8x^3.
\]
Comparing coefficients inductively, with constant coefficient \(1\), proves \(B(x)\equiv P(x)\pmod8\).

Put \(R=128\) and form the explicitly finite integer polynomial
\[
T(x)=\prod_{j=0}^6\left(\sum_{a=0}^{2^{7-j}-1}x^{a2^j}\right)^2
=\prod_{j=0}^6\left(\frac{1-x^{128}}{1-x^{2^j}}\right)^2.
\]
Its degree is exactly \(14\cdot128-2(128-1)=1538\). Splitting the infinite product after \(j=6\) yields the exact identity
\[
B(x)=\frac{T(x)}{(1-x^{128})^{14}}B(x^{128}).
\]
For \(0\le r<128\), define its decimation polynomial \(T_r(y)=\sum_{k\ge0}[x^{128k+r}]T(x)y^k\). Extracting the terms of degree congruent to \(r\) gives
\[
\sum_{t\ge0}b_2(128t+r)y^t=\frac{T_r(y)B(y)}{(1-y)^{14}}.
\]
Direct finite polynomial multiplication with the explicitly given fourteen geometric factors proves, for both \(r=36\) and \(r=62\), the same coefficient certificate modulo \(128\):
\[
T_r(y)\equiv16(7+7y+y^2+y^3+6y^4+6y^5+2y^6+2y^7+3y^8+3y^9+5y^{10}+5y^{11})\pmod{128}.
\]
The elementary polynomial identity modulo \(8\), independently checked coefficient by coefficient, is
\[
(7+7y+y^2+y^3+6y^4+6y^5+2y^6+2y^7+3y^8+3y^9+5y^{10}+5y^{11})(1+2y+5y^2)\equiv7(1-y)^{13}\pmod8.
\]
Consequently \(T_r(y)B(y)\equiv112(1-y)^{13}\pmod{128}\). Because \(1-y\) is a unit in formal power series, the decimated generating function equals \(112/(1-y)\pmod{128}\), proving the two congruences for all \(t\ge0\).

To prove the asserted *fixed-congruence* classification, apply the same finite polynomial construction to all \(128\) residues. A uniform congruence to \(112\) is equivalent to \(T_r(y)B(y)\equiv112(1-y)^{13}\pmod{128}\). Since \(B(y)\) is invertible, this forces each coefficient of \(T_r(y)\) to be divisible by \(16\). Thereafter the test reduces to the explicit polynomial identity modulo \(8\) displayed above. The standalone certificate checks every residue and finds precisely \(36,62\). Since \(\deg T=1538\), this is an exhaustive finite polynomial identity check, rather than a finite-index sample.

Finally \(112+128k=16(8k+7)\) for \(k\ge0\); by Legendre's three-square theorem no such integer is a sum of three squares. The two disjoint arithmetic progressions have combined natural density \(2/128=1/64\), which proves the lower-density bound.

## Verification
Run `python3 verify.py` with a standard Python 3 installation. It constructs the exact polynomial \(T\) modulo \(128\), checks all residue classes through polynomial identities, and independently calculates the first \(8192\) coefficients using two unbounded-coin updates for each power of two. The output is `VERIFY_OK degree 1538 certified_residues [36, 62] independent_coefficients 8192`. The unrestricted conclusion depends on the finite polynomial certificate and formal-series proof, not on the sampled coefficients.

## Relationship to prior work
Gawron, Miska and Ulas (2017), Theorem 5.4, prove \(\nu_2(b_2(32t+4))=\nu_2(b_2(32t+30))=4\); these progressions contain the new residue classes but do not determine the odd parts modulo \(8\). Sobolewski and Ulas (first posted 2022) solve three-square questions principally for color counts of the form \(2^k-1\) and explicitly pose the general-color case as Problem 7.2. Their general 2-automaticity theorem and low-modulus identities do not supply the displayed modulo-\(128\) congruence or the positive-density obstruction for color count two. The proof here uses these published themes, rather than claiming general three-square density results for two colors.

## Limitations
Only two explicit classes are certified. This does not classify every index at which \(b_2(n)\) is nonrepresentable or establish the existence of an overall natural density. The conclusion is conditional on the standard three-square theorem, and its originality relative to inaccessible or unindexed sources requires independent bibliographic scrutiny.

## References
- M. Gawron, P. Miska, and M. Ulas, *Arithmetic properties of coefficients of power series expansion ...*, Monatshefte für Mathematik 185 (2018), 307–360. First online 7 April 2017. DOI: 10.1007/s00605-017-1041-2.
- B. Sobolewski and M. Ulas, *Values of Binary Partition Function Represented by a Sum of Three Squares*, arXiv:2211.16622, first posted 29 November 2022; Results in Mathematics 78 (2023), article 188, DOI: 10.1007/s00025-023-01966-8.
- A.-M. Legendre, classical three-square theorem.
