# Exact cyclic symbol-pair enumerators of odd-prime affine Reed–Muller codes

## Finding

For every odd prime \(p\ge3\) and integer \(m\ge2\), let \(C_{p,m}\) be the affine evaluation code over \(\mathbb F_p\), with \(p^m\) coordinates in lexicographic base-\(p\) order. For \(v\in C_{p,m}\), write \(z(v)\) for the number of cyclic adjacent pairs equal to \((0,0)\). The entire zero-pair distribution is

\[
Q_{p,m}(u):=\sum_{v\in C_{p,m}}u^{z(v)}
=u^{p^m}+(p-1)+p(p-1)\left[1+\sum_{r=1}^{m-1}
\left(p-2+u^{p^{r-1}}+u^{(p-1)p^{r-1}}\right)
\prod_{j=r+2}^{m}\left(p-1+u^{(p-1)p^{j-2}}\right)\right].
\]

Empty products equal one. The complete cyclic symbol-pair weight enumerator is \(W_{p,m}(Z)=Z^{p^m}Q_{p,m}(Z^{-1})\), because each nonzero adjacent pair has pair-weight one. Exactly \(2^m\) distinct pair weights occur (including zero), and the minimum positive pair weight is \(p^m-p^{m-1}+1\), attained by exactly \(p(p-1)\) codewords. Exactly \(p(p-1)^m+(p-1)\) codewords have full pair weight \(p^m\).

## Assumptions and scope

The field is the prime field \(\mathbb F_p\). Coordinates are the points \(x=(x_1,\ldots,x_m)\in\{0,\ldots,p-1\}^m\) in ascending lexicographic order (\(x_m\) varies fastest). A codeword is the list of evaluations of one affine function \(f(x)=c+\sum_{i=1}^{m}a_i x_i\pmod p\). There are exactly \(p^{m+1}\) distinct codewords. Adjacent pairs use cyclic wraparound from the final coordinate to the first. The pair weight is the number of cyclic length-two windows with at least one nonzero coordinate, not ordinary Hamming weight. The theorem is not asserted for arbitrary coordinate permutations, nonprime fields, or general window widths.

## Proof

**Carry description.** Put \(S_i=\sum_{j=i}^{m}a_j\in\mathbb F_p\), with \(S_{m+1}=0\). A lexicographic successor step at which digit \(i\) increments and later digits wrap changes each affected digit by \(+1\pmod p\), hence changes \(f\) by \(S_i\). Include the final cyclic step as a carry at \(i=1\). For \(i\ge2\), the number of such steps is \((p-1)p^{i-1}\); for \(i=1\), it is \(p\). A zero-zero pair can occur only at a step with \(S_i=0\).

The all-zero affine function contributes \(u^{p^m}\); each nonzero constant function contributes one to the coefficient of \(u^0\). Now assume \(a\ne0\), and let \(r\) be its first nonzero coefficient index. For \(i>r\), there are \((p-1)p^{i-1}\) carry steps, and the earlier digit \(x_r\) runs freely and uniformly through \(\mathbb F_p\). Exactly \((p-1)p^{i-2}\) of them have \(f(x)=0\) if \(S_i=0\), and none have a zero-zero pair otherwise.

For \(i\le r\), the total number of zero-zero pairs is exactly \(p^{r-1}\) when \(S_r=0\), and zero otherwise, independently of \(c\). To see this for \(r\ge2\): for \(i<r\), all nonzero-coefficient digits equal \(p-1\) before the carry, so \(f=c-S_r\). If \(S_r=0=c\), the number of such carries is \(p+\sum_{i=2}^{r-1}(p-1)p^{i-1}=p^{r-1}\). If \(S_r=0\) but \(c\ne0\), none of these contribute; instead, at \(i=r\), the condition \(f=0\) fixes exactly one of the \(p-1\) possible nonterminal values of \(x_r\), while all \(p^{r-1}\) earlier-digit choices remain free. For \(r=1\), the \(p\) cyclic digit-one carries directly contain exactly one zero-zero occurrence when \(S_1=0\). Thus in all cases

\[
z(f)=p^{r-1}[S_r=0]+\sum_{i=r+1}^{m}(p-1)p^{i-2}[S_i=0],
\]

where \([P]\) denotes the indicator of proposition \(P\). In particular the count is independent of \(c\).

**Counting affine functions.** The transformation from the coefficients \((a_r,\ldots,a_m)\) to \((S_r,\ldots,S_m)\) is invertible, and \(a_r\ne0\) is exactly \(S_r\ne S_{r+1}\). For fixed \(r<m\), summing over the allowed pair \((S_r,S_{r+1})\) gives

\[
(p-1)\left[(p-2)+u^{p^{r-1}}+u^{(p-1)p^{r-1}}\right].
\]

Indeed, when \(S_{r+1}=0\), there are \(p-1\) nonzero choices of \(S_r\) with the larger exponent; when \(S_{r+1}\ne0\), exactly one choice \(S_r=0\) has the smaller exponent, and \(p-2\) choices give exponent zero, for each of the \(p-1\) nonzero values of \(S_{r+1}\). Every subsequent suffix variable \(S_j\), for \(j\ge r+2\), contributes independently the factor \((p-1)+u^{(p-1)p^{j-2}}\). Multiply by the \(p\) choices of \(c\). For \(r=m\), the contribution is \(p(p-1)\) at exponent zero. Adding constant functions yields the displayed expression for \(Q_{p,m}\).

**Support, extrema, and multiplicity.** Let \(E_m\) be the set of exponents \(z(v)\) arising from nonzero affine codewords. The factored expression gives \(E_1=\{0\}\) and, for all \(m\ge2\),

\[
E_m=E_{m-1}\ \dot\cup\ \bigl(E_{m-1}+(p-1)p^{m-2}\bigr)\ \dot\cup\ \{p^{m-2}\}.
\]

Induction gives \(\max E_{m-1}=p^{m-2}-1\). Since \(p\ge3\), the three sets are disjoint: the first lies below \(p^{m-2}\), and the translated set starts at \((p-1)p^{m-2}>p^{m-2}\). Hence \(|E_m|=2|E_{m-1}|+1=2^m-1\) and \(\max E_m=p^{m-1}-1\). The all-zero word has pair weight zero and all other weights are \(p^m-z\) for \(z\in E_m\), proving the \(2^m\)-weight statement and the minimum distance. The maximal nonzero exponent is realized precisely when \(S_2=\cdots=S_m=0\) and \(S_1\ne0\): there are \(p-1\) possibilities for \(S_1\) and \(p\) for \(c\), giving \(p(p-1)\) minimum-weight words. Finally, the coefficient of \(u^0\) counts nonzero constants and affine coefficient tuples whose relevant suffix values are all nonzero; the geometric sum is \((p-1)+p[(p-1)+(p-2)\sum_{r=1}^{m-1}(p-1)^{m-r}]=p(p-1)^m+(p-1)\). This completes the proof.

## Verification

The standalone checker `verify_oddprime_pair.py` computes the displayed polynomial by independent integer-polynomial convolution and compares it to an independently coded direct enumeration of all cyclic adjacent pairs of every affine word. It verifies every instance with \(p\in\{3,5,7\}\) and \(1\le m\le6,3,3\), respectively, and additionally checks the binary contrast \(p=2\), \(1\le m\le5\). The direct checks are finite corroboration, not a substitute for the general proof. Run `python3 verify_oddprime_pair.py`; a successful run ends with `VERIFY_OK`.

For example, for \(p=3\), \(m=3\), the ordered pair-weight multiplicities are \(A_0=1\), \(A_{19}=6\), \(A_{20}=6\), \(A_{21}=12\), \(A_{24}=6\), \(A_{25}=12\), \(A_{26}=12\), \(A_{27}=26\). These sum to \(3^4=81\).

## Relationship to prior work

Liu and Pan (arXiv:2103.16299, Section 4) give generalized \(b\)-symbol weight techniques and examples for classical codes, but do not state the lexicographic odd-prime affine evaluation-code pair-weight multiplicity formula above. Ma and Luo (arXiv:1911.02184, Theorems 2–3) determine cyclic pair weights for (variant) simplex codes under their multiplicative finite-field coordinate orderings; those constructions have a different length, dimension, and pair-weight support, and neither theorem contains the displayed distribution. Miezaki and Munemasa (arXiv:2303.16349) give Jacobi and harmonic weight-enumerator results for binary first-order Reed–Muller codes, not the ordered odd-prime symbol-pair metric. Standard Hamming-weight distributions do not determine cyclic pair-weight multiplicities under an arbitrary coordinate ordering.

## Limitations

The formula requires the stated **lexicographic coordinate order**, an odd prime field, and cyclic windows of length two. Its use for a different coordinate permutation is unjustified without new analysis. The general statement is proved; the checker tests only small prime/dimension combinations. Exhaustive literature discovery is not claimed, and an unindexed equivalent result could exist. No independent assessment is represented by this document.

## References

1. H. Liu and X. Pan, *Generalized b-symbol weights of Linear Codes and b-symbol MDS Codes*, arXiv:2103.16299, public version 30 March 2021, https://arxiv.org/abs/2103.16299.
2. J. Ma and J. Luo, *Symbol-pair Weight Distributions of Some Linear Codes*, arXiv:1911.02184, 2019, https://arxiv.org/abs/1911.02184.
3. T. Miezaki and A. Munemasa, *Jacobi polynomials and harmonic weight enumerators of first-order Reed–Muller codes and extended Hamming codes*, arXiv:2303.16349, 2023, https://arxiv.org/abs/2303.16349.
