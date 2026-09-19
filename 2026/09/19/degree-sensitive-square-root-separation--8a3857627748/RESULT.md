# Degree-sensitive separation for integer linear forms in square roots

## Statement

Let \(a_1,\dots,a_K\) be positive integers with pairwise distinct square-free parts, let \(m_1,\dots,m_K\in\mathbb Z\) be not all zero, and put
\[
\Lambda=\left|\sum_{i=1}^K m_i\sqrt{a_i}\right|.
\]
Let \(J=\{i:m_i\ne0\}\), \(k=|J|\),
\[
Q=\sum_{i\in J}m_i^2a_i,
\qquad
E=\mathbb Q\bigl(\sqrt{-a_i}:i\in J\bigr),
\qquad
D=[E:\mathbb Q].
\]
If \(k\ge2\), then
\[
\boxed{
\Lambda\ge
\left(\frac{D}{D-2}Q\right)^{-(D-2)/4}.
}
\]
Equivalently, with \(M=\max_{i\in J}|m_i|\sqrt{a_i}\),
\[
\boxed{
\Lambda\ge
\left(1-\frac2D\right)^{(D-2)/4}(M\sqrt{k})^{-(D/2-1)}.
}
\]
For \(k=1\) the form is simply \(|m_i|\sqrt{a_i}\), so no separation argument is needed.

The degree \(D\) is completely explicit. If the square-free part of \(a_i\) has prime-parity vector \(v_i\in\mathbb F_2^{(\mathcal P)}\), then
\[
D=2^s,
\qquad
s=\operatorname{rank}_{\mathbb F_2}\{(1,v_i):i\in J\},
\]
where the leading coordinate records the square class of \(-1\). Thus the exponent is controlled by the actual negative-squareclass rank, rather than by the formal number of independent sign choices.

When \(D=2^k\), the first displayed inequality is exactly the sharp first inequality in Theorem 1.1 of Aymone--Figueredo--Táfula (2026). When \(D<2^k\), it is strictly degree-sensitive and replaces their coefficient exponent \(2^{k-1}-1\) by \(D/2-1\).

## Proof

Choose \(\sqrt{-a_i}=i\sqrt{a_i}\) and define
\[
\gamma=\sum_{i\in J}m_i\sqrt{-a_i}
=i\sum_{i\in J}m_i\sqrt{a_i}.
\]
Hence \(|\gamma|=\Lambda\). The number \(\gamma\) is an algebraic integer. By the linear independence of square roots with distinct square-free parts, \(\gamma\ne0\), so
\[
|N_{E/\mathbb Q}(\gamma)|\ge1.
\]

Write \(G=\operatorname{Gal}(E/\mathbb Q)\). For every active index \(i\), the action of \(G\) on \(\sqrt{-a_i}\) defines a nontrivial quadratic character \(\chi_i:G\to\{\pm1\}\). The characters \(\chi_i\) are pairwise distinct: equality of \(\chi_i\) and \(\chi_j\) would make \(\sqrt{a_i/a_j}\) rational, contradicting the distinct square-free parts. Character orthogonality therefore gives
\[
\sum_{\sigma\in G}|\sigma(\gamma)|^2
=\sum_{\sigma\in G}\left|\sum_{i\in J}m_i\chi_i(\sigma)\sqrt{a_i}\right|^2
=DQ.
\]

Complex conjugation \(c\in G\) sends every \(\sqrt{-a_i}\) to its negative. Thus
\[
|\gamma|=|c(\gamma)|=\Lambda.
\]
For \(k\ge2\), pairwise distinct nontrivial square classes give \(D\ge4\). Isolating the identity and complex-conjugation factors in the norm, and applying AM--GM to the squares of the remaining \(D-2\) conjugates, yields
\[
1
\le \Lambda^2\prod_{\sigma\ne1,c}|\sigma(\gamma)|
\le
\Lambda^2
\left(\frac{DQ-2\Lambda^2}{D-2}\right)^{(D-2)/2}
\le
\Lambda^2
\left(\frac{DQ}{D-2}\right)^{(D-2)/2}.
\]
Rearranging proves the first bound. Since \(Q\le kM^2\), the second follows immediately.

## Complete multiquadratic bases: an optimal exponent

Let \(p_1,\dots,p_r\) be distinct primes and set
\[
a_S=\prod_{j\in S}p_j
\qquad(S\subseteq\{1,\dots,r\}).
\]
There are \(K=2^r\) radicands. They form the usual basis of the real multiquadratic field \(\mathbb Q(\sqrt{p_1},\dots,\sqrt{p_r})\). All numbers \(\sqrt{-a_S}\) lie in
\[
E=\mathbb Q(i,\sqrt{p_1},\dots,\sqrt{p_r}),
\]
which has degree \(D=2^{r+1}=2K\). Applying the same norm-and-orthogonality argument in this ambient field gives, for every nonzero integer coefficient vector,
\[
\boxed{
\left|\sum_Sm_S\sqrt{a_S}\right|
\ge
\left(\frac{K}{K-1}\sum_Sm_S^2a_S\right)^{-(K-1)/2}.
}
\]
Consequently, if \(M=\max_S|m_S|\sqrt{a_S}\),
\[
\boxed{
\left|\sum_Sm_S\sqrt{a_S}\right|
\ge
\left(1-\frac1K\right)^{(K-1)/2}
(M\sqrt K)^{-(K-1)}.
}
\]
For this natural family the Aymone--Figueredo--Táfula coefficient exponent \(2^{K-1}-1\) is therefore reduced to \(K-1\).

The exponent \(K-1\) is optimal for fixed radicands, up to the multiplicative constant. Indeed, because this family contains \(1\), the standard pigeonhole form of Dirichlet approximation applied to the other \(K-1\) basis elements produces infinitely many nonzero integer coefficient vectors of height \(H\) with linear form \(O(H^{-(K-1)})\). Hence no lower bound with a smaller coefficient exponent can hold uniformly over all integer coefficients for these fixed radicands.

## Example

For \(a=(1,2,3,6)\) and \(m=(-5,1,-5,5)\),
\[
\Lambda=|-5+\sqrt2-5\sqrt3+5\sqrt6|
\approx 0.00140823844460058,
\qquad Q=252.
\]
The negative square classes have rank \(3\), so \(D=8\). The new bound is
\[
\Lambda\ge336^{-3/2}\approx1.6236450166\times10^{-4}.
\]
The exact Aymone--Figueredo--Táfula bound using \(K=4\) is
\[
\Lambda\ge288^{-7/2}\approx2.4667565658\times10^{-9}.
\]
The real biquadratic norm of the displayed linear form is exactly \(4\); in \(\mathbb Q(i,\sqrt2,\sqrt3)\), the norm of its imaginary multiple is \(16\).

For complete multiquadratic bases, the coefficient exponents compare as follows:

| \(K\) | degree \(D\) | degree-sensitive exponent | Aymone--Figueredo--Táfula exponent |
|---:|---:|---:|---:|
| 2 | 4 | 1 | 1 |
| 4 | 8 | 3 | 7 |
| 8 | 16 | 7 | 127 |
| 16 | 32 | 15 | 32767 |
| 32 | 64 | 31 | 2147483647 |

## Relation to prior work

Aymone, Figueredo and Táfula prove an explicit uniform separation bound by taking the product over all \(2^K\) sign choices, isolating two opposite factors, and applying AM--GM plus Rademacher orthogonality. The present refinement replaces that formal sign cube by the actual conjugates in the multiquadratic field generated by the negative active radicands. This preserves their second-moment identity while reducing the number of conjugates whenever there are multiplicative square-class relations.

The general principle that algebraic dependence can lower the effective algebraic degree is classical and is not claimed here as new; separation-bound literature including Burnikel--Fleischer--Mehlhorn--Schirra already discusses losses caused by degree overestimation. The contribution claimed here is the explicit rank-sensitive formula above, its exact agreement with the recent Aymone--Figueredo--Táfula bound in the full-rank case, and the sharp \(K-1\) exponent for complete multiquadratic bases.

Eisenbrand--Haeberle--Singer prove a singly exponential lower bound for fixed radicands using the Subspace Theorem, but its positive constant depends on the radicands and is ineffective. The bound here is elementary and explicit in the radicands through \(Q\) and the computable squareclass rank.

## Limitations

Originality is asserted only to the best of our knowledge. The full text of Dubickas (2024), which is specifically cited by Aymone--Figueredo--Táfula for a related product argument, was not inspected; its bibliographic metadata and the description in the 2026 primary source were inspected. It is therefore the most relevant residual literature risk. The theorem does not improve the recent exact bound when the negative active square classes have full rank, and it does not resolve the general Sum-of-Square-Roots complexity problem. The optimality statement concerns the coefficient exponent for fixed complete multiquadratic bases, not a universal optimal constant.

## Reproducibility

`artifacts/verify_examples.py` computes the negative-squareclass ranks for complete multiquadratic bases, checks the exact norm and both explicit bounds in the \(\{1,2,3,6\}\) example, and performs a finite coefficient sanity check. `artifacts/verification_output.txt` contains its output. These computations support the examples; the theorem itself is proved above.

## References

1. M. Aymone, S. Figueredo, C. Táfula, *Quantitative linear independence for square roots*, arXiv:2609.14161 (2026).
2. A. S. Besicovitch, *On the linear independence of fractional powers of integers*, J. London Math. Soc. 15 (1940), 3--6.
3. C. Burnikel, R. Fleischer, K. Mehlhorn, S. Schirra, *A strong and easily computable separation bound for arithmetic expressions involving radicals*, Algorithmica 27 (2000), 87--99. DOI: 10.1007/s004530010005.
4. A. Dubickas, *Approximate equality for two sums of roots*, J. Complexity 84 (2024), 101866. DOI: 10.1016/j.jco.2024.101866.
5. F. Eisenbrand, M. Haeberle, N. Singer, *An improved bound on sums of square roots via the subspace theorem*, SoCG 2024, Article 54. DOI: 10.4230/LIPIcs.SoCG.2024.54.
