# Strong uncertainty for the index-four norm-one symmetry over \(\mathbb{F}_{25}\)
## Finding
Let \(H\) be the unique index-four subgroup of \(\mathbb{F}_{25}^{\times}\). Since \(|H|=6\), it is also the norm-one subgroup for \(\mathbb{F}_{25}/\mathbb{F}_5\). For every character \(\chi:H\to\mathbb{C}^{\times}\), the compressed Fourier matrix has the nonvanishing-minors property exactly when
\[
\operatorname{ord}(\chi)\in\{1,6}.
\]
Thus the trivial character and the two characters of order \(6\) have the strong uncertainty property, while the character of order \(2\) and the two characters of order \(3\) do not.

## Assumptions and scope
Use \(\mathbb{F}_{25}=\mathbb{F}_5[a]/(a^2-2)\), with primitive element \(g=1+2a\) of order \(24\), and set \(H=\langle g^4\rangle\). For \(j\in\{0,1,2,3,4,5}\), define \(\chi_j((g^4)^t)=\zeta_6^{jt}\). The nontrivial-character orbit representatives are \(R=S=\{1,g,g^2,g^3}\); for \(j=0\), adjoin \(0\). The canonical additive character is \(\varepsilon_s(x)=\zeta_5^{\operatorname{Tr}(sx)}\), where \(\operatorname{Tr}(u+va)=2u\) in \(\mathbb{F}_5\).

## Proof
Garcia, Karaali, and Katz show that the compressed Fourier matrix has entries \(\sum_{h\in H}\chi(h)\varepsilon_s(hr)\), and that its nonvanishing-minors property is equivalent to the strong uncertainty property. With the representatives above, every entry lies in \(\mathbb{Z}[\zeta_{30}]\), because \(\zeta_5=\zeta_{30}^6\) and \(\zeta_6=\zeta_{30}^5\).

Work exactly in
\[
\mathbb{Z}[z]/(\Phi_{30}(z)),\qquad
\Phi_{30}(z)=z^8+z^7-z^5-z^4-z^3+z+1.
\]
The supplied verifier constructs all six compressed matrices and reduces every determinant to its unique degree-less-than-eight representative. For \(j=0,1,5\), all minors are nonzero: respectively \(251,69,69\) minors are checked. For \(j=2,4\), exactly ten \(2\times2\) minors vanish. For \(j=3\), exactly thirty-four minors vanish: eight of size \(1\), eighteen of size \(2\), and eight of size \(3\). Since \(\operatorname{ord}(\chi_j)=6/\gcd(j,6)\) for \(j\ne0\), this is precisely the stated order classification.

For explicit failure witnesses, when \(j=2\) the minor on rows \(\{0,1}\) and columns \(\{0,3}\) is exactly zero; when \(j=3\), the entry in row \(0\), column \(1\) is exactly zero. These are identities in the cyclotomic integer ring, not numerical approximations.

## Verification
Run `python verify_f25_index4.py`. It uses only integer arithmetic, finite-field arithmetic, and polynomial reduction modulo \(\Phi_{30}\). It independently reconstructs \(\mathbb{F}_{25}\), verifies that \(g\) has order \(24\), builds \(H\), forms the six matrices, enumerates every square minor, and checks the exact zero counts. Successful replay ends with `VERIFY_OK`.

## Relationship to prior work
Tao's prime-order uncertainty theorem ties Fourier-support uncertainty to Chebotarev nonvanishing of Fourier minors. Garcia, Karaali, and Katz introduced the symmetry-compressed formulation over finite fields, proved the proper-subfield obstruction, completely treated index \(2\), treated the trivial-character index-\(3\) case, and posed the general criterion problem. Their \(\mathbb{F}_{25}\) table concerns the index-\(2\) subgroup; it does not state the index-\(4\) classification above. Díaz Padilla and Ochoa Arango later characterize index \(3\) for nontrivial characters. The present result treats the next index and gives a complete character-by-character classification for the first non-prime index-\(4\) field not eliminated by the proper-subfield obstruction: over \(\mathbb{F}_9\) the index-\(4\) subgroup lies in \(\mathbb{F}_3\), whereas the order-six subgroup of \(\mathbb{F}_{25}^{\times}\) cannot lie in \(\mathbb{F}_5^{\times}\), which has order \(4\).

## Limitations
This is an exact classification only for the index-four subgroup of \(\mathbb{F}_{25}^{\times}\). It does not give a general index-four criterion over arbitrary non-prime finite fields, nor does it classify larger norm-one subgroups. The originality check found no source stating this \(\mathbb{F}_{25}\) index-four classification, but absence from the searched literature is not a proof of global novelty.

## References
1. T. Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286, first posted 2003-08-29.
2. S. R. Garcia, G. Karaali, D. J. Katz, *An improved uncertainty principle for functions with symmetry*, arXiv:1807.07648.
3. D. F. Díaz Padilla, J. A. Ochoa Arango, *On an uncertainty principle for small index subgroups of finite fields*, arXiv:2310.09992; Open Mathematics 23 (2025), 20250178.
