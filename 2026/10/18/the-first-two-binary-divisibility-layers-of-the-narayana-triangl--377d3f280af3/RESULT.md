# The first two binary divisibility layers of the Narayana triangle

## Finding

Let \(\mathcal N(n,k)=\frac1n\binom nk\binom n{k-1}\) for integers \(n\ge1\) and \(1\le k\le n\). For \(j\ge0\) and \(L\ge1\), define the exact two-adic layer counts
\[
A_j(L)=\#\{(n,k):1\le n<2^L,\ 1\le k\le n,\ \nu_2(\mathcal N(n,k))=j\}.
\]
Then, for every integer \(L\ge1\),
\[
\boxed{A_0(L)=\frac{5\cdot3^{L-1}-3}{2}.}
\]
For every integer \(L\ge2\), the first nonzero valuation layer has the exact count
\[
\boxed{A_1(L)=3^{L-1}-3.}
\]
At the boundary \(L=1\), \(A_1(1)=0\). In particular, among entries not divisible by four, the proportion having valuation exactly one tends to \(2/7\), while the ratio of valuation-one to odd entries tends to \(2/5\). These are counts of *entries*, not sums of their numerical values.

## Assumptions and scope

The valuation \(\nu_2(a)\) is the exponent of two in a positive integer \(a\), and \(s_2(a)\) is the number of ones in the binary expansion of a nonnegative integer \(a\). Put \(b(m,j)=\nu_2\binom mj\) for \(0\le j\le m\). A nonnegative integer \(j\) is a binary **submask** of \(m\) when every one-bit of \(j\) is also a one-bit of \(m\). By the binary case of Kummer's theorem (or Legendre's factorial formula), \(b(m,j)=s_2(j)+s_2(m-j)-s_2(m)\), and \(b(m,j)=0\) exactly when \(j\) is a submask of \(m\). No restriction is imposed on \(k\) beyond the full Narayana row.

## Proof

**1. Binary decomposition.** The factorial valuation formula gives
\[
\nu_2\binom{2m}{2j}=b(m,j),\qquad
\nu_2\binom{2m+1}{2j}=\nu_2\binom{2m+1}{2j+1}=b(m,j).
\]
For every \(m\ge1\) and \(1\le j\le m\), the Narayana entries in the even row \(2m\) occur in equal-valuation pairs, and each such pair has valuation
\[
\nu_2\mathcal N(2m,2j)
=\nu_2\mathcal N(2m,2(m-j)+1)
=b(m,j)+b(m-1,j-1).
\tag{1}
\]
Indeed, the ratio of adjacent binomial coefficients gives
\(b(m,j)-b(m-1,j-1)=\nu_2(m)-\nu_2(j)\), and substituting into the defining product yields (1). The two positions in each pair are distinct, and these pairs partition the row. For every \(m\ge0\), the odd row \(2m+1\) has
\[
\begin{aligned}
\nu_2\mathcal N(2m+1,2j+1)&=2b(m,j) &&(0\le j\le m),\\
\nu_2\mathcal N(2m+1,2j+2)&=b(m,j)+b(m,j+1) &&(0\le j<m).
\end{aligned}\tag{2}
\]

**2. Odd Narayana entries.** Set \(h=L-1\). In (1), zero valuation requires both terms to vanish. If \(m=2^r u\) with odd \(u\), the identity \(b(m,j)-b(m-1,j-1)=r-\nu_2(j)\) shows that this occurs precisely when \(j\) is a submask of \(m\) and \(\nu_2(j)=r\). There are \(2^{s_2(u)-1}\) possible \(j\), hence \(2^{s_2(u)}\) odd entries in row \(2m\). Summing over \(1\le m<2^h\) gives
\[
\sum_{r=0}^{h-1}\ \sum_{\substack{1\le u<2^{h-r}\\u\text{ odd}}}2^{s_2(u)}
=2\sum_{r=0}^{h-1}3^{h-r-1}=3^h-1.
\tag{3}
\]
In (2), odd-indexed positions contribute one odd entry for each submask of \(m\), and summing over \(0\le m<2^h\) gives \(3^h\). At the even-indexed positions, both adjacent binomial coefficients must be odd. If \(t=\nu_2(j+1)\), this happens precisely when the lowest \(t+1\) bits of \(m\) are all ones, while the higher bits of \(j\) are an arbitrary submask of those of \(m\). Summing over \(t\) and \(m<2^h\) yields
\[
\sum_{t=0}^{h-1}3^{h-t-1}=\frac{3^h-1}{2}.
\tag{4}
\]
Adding (3), the odd-position contribution, and (4) gives \(A_0(L)=(5\cdot3^h-3)/2\), including \(h=0\).

**3. Exactly one factor of two.** For \(m\ge1\) define
\[
E(m)=\#\{1\le j\le m:b(m,j)+b(m-1,j-1)=1\},\quad
O(m)=\#\{0\le j<m:b(m,j)+b(m,j+1)=1\}.
\]
Write \(m=2^r u\) with odd \(u\). In \(E(m)\), the two nonnegative valuations sum to one if either the second is zero and the first is one, or vice versa. The valuation-difference identity in step 1 makes these cases respectively \(\nu_2(j)=r-1\) and \(\nu_2(j)=r+1\). The first is possible only for \(r\ge1\): then \(j-1\) must be a submask of \(m-1\), giving \(2^{s_2(u-1)}\) choices. In the second, \(j\) must be a submask of \(m\); this requires \(u\equiv3\pmod4\) and gives \(2^{s_2(\lfloor u/4\rfloor)}\) choices. Consequently,
\[
E(m)=\mathbf1_{r\ge1}\,2^{s_2(u-1)}
+\mathbf1_{u\equiv3\ (\mathrm{mod}\ 4)}\,2^{s_2(\lfloor u/4\rfloor)}.
\tag{5}
\]
For \(1\le m<2^h\), the total contributions from the first and second summands of (5) are, separately,
\[
\sum_{r=1}^{h-1}3^{h-r-1}=\frac{3^{h-1}-1}{2},
\qquad
\sum_{r=0}^{h-2}3^{h-r-2}=\frac{3^{h-1}-1}{2}.
\]
Empty sums are zero. Therefore
\[
\sum_{1\le m<2^h}E(m)=3^{h-1}-1\qquad(h\ge1).
\tag{6}
\]

For \(O(m)\), reflection \(j\mapsto m-j-1\) exchanges \(b(m,j)\) and \(b(m,j+1)\); the two cases \((0,1)\) and \((1,0)\) therefore have equal counts. In the \((0,1)\) case, \(j\) must be a submask of \(m\), and the adjacent-binomial ratio forces
\[
\nu_2(m-j)-\nu_2(j+1)=1.
\]
Put \(t=\nu_2(j+1)\). This condition says that \(m\) has exactly \(t\) trailing one-bits, its next bit is zero, and the following bit is one; \(j\) has its lowest \(t\) bits equal to one, followed by two zero-bits. Its higher bits may be any submask of the higher bits of \(m\). Equivalently, writing \(t=\nu_2(m+1)\),
\[
O(m)=2\,\mathbf1_{\text{bit }t+1\text{ of }m\text{ is }1}\,
2^{s_2(\lfloor m/2^{t+2}\rfloor)}.
\tag{7}
\]
Each relevant \(m\) has the unique binary form \(m=2^{t+2}q+2^{t+1}+2^t-1\). Summing (7) over \(m<2^h\) gives
\[
\sum_{0\le m<2^h}O(m)
=2\sum_{t=0}^{h-2}3^{h-t-2}=3^{h-1}-1\qquad(h\ge1).
\tag{8}
\]
Finally, (1) duplicates each even-row contribution to valuation one, and (2) shows that the odd-indexed positions in odd rows always have even valuation. By (6)--(8), for \(L=h+1\ge2\),
\[
A_1(L)=2\sum_{1\le m<2^h}E(m)+\sum_{0\le m<2^h}O(m)
=3(3^{h-1}-1)=3^{L-1}-3.
\]
For \(L=1\), only \(\mathcal N(1,1)=1\) occurs. The limiting ratios follow immediately from the two exact formulas, since the number of entries having valuation at most one is \(A_0(L)+A_1(L)\).

## Verification

Execute `python3 artifacts/verify.py` from the directory containing this document. The self-contained program verifies (5) and (7) for all \(1\le m\le256\), compares the binary valuation formula with exact binomial-integer Narayana values for every entry in rows \(1\le n\le127\), and checks both complete dyadic layer counts for \(1\le L\le10\). Successful replay prints `VERIFY_OK`. This finite computation is a check on the derivation; it is not the proof of the all-length formulas, which is the submask enumeration above.

## Relationship to prior work

Bóna and Sagan (2005), Theorem 1.2, characterize individual Narayana numbers not divisible by a prime using Kummer's theorem; their Section 3 explicitly raises the question of extending the methods to exact prime-adic orders. Eu, Liu, and Yeh (2006) study congruences of related combinatorial quantities, and OEIS A335965 records the number of odd entries in each Narayana row. The zero-valuation formula above is a consistency refinement of this established parity viewpoint; **the claimed new information is the exact valuation-one count over complete binary-length cutoffs**. A later study by Pinheiro, Vascon, and Craveiro (2026) supplies congruences for the *central-column* Narayana numbers modulo powers of two, not the entire triangular distribution. The integer sequence produced by the valuation-one formula also occurs numerically as OEIS A058809 in unrelated enumerative settings; numerical coincidence does not supply the Narayana valuation interpretation.

## Limitations

This theorem counts only two-adic valuations zero and one. It does not classify valuations at least two, other primes, or general non-dyadic cutoffs. The proof is elementary and exact; computational verification is finite and does not constitute independent mathematical validation. Priority remains subject to independent literature assessment, especially any general unpublished formula for the valuation distribution of Narayana arrays.

## References

1. M. Bóna and B. E. Sagan, *On divisibility of Narayana numbers by primes*, 2005, arXiv:math/0505382, https://arxiv.org/abs/math/0505382 (full text: https://users.math.msu.edu/users/sagan/Papers/Old/dnn.pdf).
2. S.-P. Eu, S.-C. Liu and Y.-N. Yeh, *On the Congruences of Some Combinatorial Numbers*, *Studies in Applied Mathematics* 116 (2006), 135–144, https://doi.org/10.1111/j.1467-9590.2006.00337.x.
3. OEIS A335965, *Number of odd numbers in the n-th row of the Narayana triangle*, https://oeis.org/A335965.
4. G. F. Pinheiro, G. M. Vascon and I. M. Craveiro, *Congruences of Narayana numbers modulo primes and powers of primes*, 2026, https://periodicos.ufs.br/ReviSe/article/download/23795/18603.
5. OEIS A058809, *The sequence lambda(3,n)*, https://oeis.org/A058809.
