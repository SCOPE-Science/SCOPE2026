# Sharp cyclic-covering codimension at binary length \(28\)

## Finding

Let \(\sigma\) be cyclic right rotation on \(\mathbb F_2^{28}\), and let \(h_2(n)\) denote the largest codimension of a linear subspace \(U\le\mathbb F_2^n\) whose cyclic shifts cover the whole space. Then

\[
\boxed{h_2(28)=4.}
\]

In particular, there is an explicitly defined binary linear \([28,24]\) space \(U\) such that \(\bigcup_{j=0}^{27}\sigma^j U=\mathbb F_2^{28}\). This closes the previously recorded interval \(3\le h_2(28)\le4\).

## Assumptions and scope

All arithmetic in the following construction is over \(\mathbb F_2\). Represent a word \((v_0,\ldots,v_{27})\) by \(v(t)=\sum_{i=0}^{27}v_i t^i\) in \(\mathbb F_2[t]/(t^{28}+1)\). The cyclic right shift is multiplication by \(t\).

Define

\[
 f(t)=t^3+t+1,\qquad P(t)=f(t)^3=t^9+t^7+t^6+t^5+t^2+t+1.
\]

Let \(R=\mathbb F_2[t]/(P)\), a nine-dimensional vector space. Write \(s\in R\) as a nine-bit integer \(\sum_{j=0}^8 s_j2^j\). For a nine-bit mask \(a\), set \(\ell_a(s)=\sum_{j=0}^8a_js_j\pmod2\). Let

\[
K=\ker\ell_{\mathtt{020}}\cap\ker\ell_{\mathtt{1B0}}\cap
  \ker\ell_{\mathtt{179}}\cap\ker\ell_{\mathtt{0E1}},
\]

where the hexadecimal masks are simply the coefficient vectors of four binary linear functionals, not field elements. Let \(\pi:\mathbb F_2[t]/(t^{28}+1)\to R\) be reduction modulo \(P\), and put \(U=\pi^{-1}(K)\). Equivalently, \(U\) is the common kernel of the four binary length-\(28\) parity-check masks (lowest bit = coordinate zero):

```
0A882A20
0922B9B0
0E90E779
0976F8E1
```

These rows are independent, so \(\dim U=24\).

## Proof

**A compatible quotient.** The polynomial \(f\) divides \(t^7+1\); hence \(P=f^3\) divides \((t^7+1)^4=t^{28}+1\). Therefore \(\pi\) is a well-defined, surjective linear map. Let \(T:R\to R\) be multiplication by \(t\bmod P\). It satisfies \(\pi\sigma=T\pi\), and \(T^{28}=I\). The four masks defining \(K\) are linearly independent (ordinary elimination over \(\mathbb F_2\)), so \(K\) has dimension five and \(U\) codimension four.

**Complete quotient orbit certificate.** Identify \(R\) with the integers \(0,\ldots,511\) by coefficient bits. Multiplication by \(t\) is the exact recurrence

\[
T(s)=\begin{cases}
2s,&s<256,\\
(2s)\mathbin{\mathrm{xor}}743,&s\ge256.
\end{cases}
\]

The following is the complete orbit decomposition of the \(512\) quotient states. In each row, \(r\) is the least integer in its orbit, \(d\) is the orbit length, and \(j\) gives a witnessed exponent for which \(T^j(r)\in K\). All entries are exact integers; the hexadecimal masks defining \(K\) are above.

| \(r\) | \(d\) | \(j\) | \(r\) | \(d\) | \(j\) |
|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 0 | 1 | 28 | 1 |
| 3 | 28 | 1 | 5 | 28 | 23 |
| 7 | 28 | 6 | 9 | 28 | 21 |
| 11 | 14 | 10 | 13 | 28 | 4 |
| 15 | 28 | 9 | 19 | 28 | 23 |
| 21 | 28 | 5 | 25 | 28 | 9 |
| 27 | 28 | 5 | 29 | 14 | 7 |
| 31 | 28 | 14 | 33 | 28 | 7 |
| 35 | 28 | 16 | 37 | 28 | 10 |
| 49 | 14 | 12 | 65 | 28 | 0 |
| 69 | 7 | 0 | 83 | 14 | 9 |

To check completeness without traversing \(2^{28}\) words, iterate the displayed recurrence from the listed least representatives and mark visited states. There is one orbit of length one, one of length seven, four of length fourteen and sixteen of length twenty-eight, all disjoint. Their sizes total

\[
1+7+4\cdot14+16\cdot28=512.
\]

The membership test for a state \(s\) is the four-bit parity condition \(\ell_a(s)=0\) for each of the four given masks. Applying this test to each recorded \(T^j(r)\) proves that every quotient orbit meets \(K\).

Now fix any \(v\in\mathbb F_2^{28}\), and write \(s=\pi(v)\in R\). Its \(T\)-orbit has some member in \(K\); hence \(\pi(\sigma^jv)=T^j s\in K\) for some \(j\in\{0,\ldots,27\}\). Therefore \(\sigma^jv\in U\). This proves cyclic coverage.

**Matching upper bound.** If a codimension-\(c\) subspace in \(\mathbb F_2^{28}\) has twenty-eight cyclic shifts whose union is the whole space, the union bound gives \(2^{28}\le28\cdot2^{28-c}\). Thus \(2^c\le28<32\), and \(c\le4\). Together with the construction, \(h_2(28)=4\).

## Verification

The accompanying `verify.py` is standalone Python and uses only exact integer operations. It independently multiplies \(f\) three times, checks \(P\mid t^{28}+1\), verifies the four check-mask ranks and the length-\(28\) parity-check rows, regenerates all \(22\) quotient orbits and their witnessed kernel hits, and tests every one of the \(512\) quotient states. It outputs `CYCLICALLY_COVERING_28_VERIFY_OK` when all assertions pass. The finite certificate is exhaustive in the quotient because \(\pi\) is surjective and intertwines cyclic shifts; it is not a sample of the original space.

## Relationship to prior work

Aaronson, Groenland and Johnston's table of small values explicitly records the interval \(3\le h_2(28)\le4\), rather than an exact value. Their product inequality and existing examples give lower bounds but not the four-check construction above. The subsequent 2026 works of Wang and Shi and of Li and Yuan address cyclic-code criteria, prime-length and double-prime cases, and other geometric families. In particular, Wang–Shi's \(h_2(2p)=2\) theorem assumes that two is primitive modulo \(p\); it does not apply to \(p=7\) or to length \(28\). The 2026 work of Li, Yuan, Li and Zeng primarily classifies the zero-codimension case and reports the distinct known exact value at length \(21\). This result supplies a separate exact length-\(28\) value with a small direct certificate.

## Limitations

The theorem is specific to binary length \(28\), and does not classify all optimal cyclically covering subspaces or establish formulas at larger lengths. The supplied verification is a finite exact quotient calculation plus the written algebraic proof; it is not independent mathematical review. A 2025 study by Sun, Ma and Zeng may contain additional implications not resolved without full-text access, so definitive publication priority is not claimed.

## References

1. J. Aaronson, C. Groenland, T. Johnston, *Cyclically covering subspaces in* \(\mathbb F_2^n\), arXiv:1903.10613, particularly Appendix A, entry \(n=28\). https://arxiv.org/abs/1903.10613
2. P. J. Cameron, D. Ellis, W. Raynaud, *Smallest cyclically covering subspaces of* \(\mathbb F_q^n\) *and lower bounds in Isbell's conjecture*, arXiv:1810.03485. https://arxiv.org/abs/1810.03485
3. X. Wang, M. Shi, *Cyclic codes and cyclically covering subspaces*, arXiv:2607.24351, first submitted 2026-07-27. https://arxiv.org/abs/2607.24351
4. Y. Li, P. Yuan, *Discrete Fourier Transform Approach to Cyclically Covering Subspaces of* \(\mathbb F_q^n\), arXiv:2606.13307. https://arxiv.org/abs/2606.13307
5. Y. Li, P. Yuan, S. Li, Y. Zeng, *On cyclically covering subspaces of* \(\mathbb F_q^n\), arXiv:2602.04558. https://arxiv.org/abs/2602.04558
6. M. Sun, C. Ma, L. Zeng, *Cyclically covering subspaces of* \(\mathbb F_q^n\), *Finite Fields and Their Applications* 106 (2025), 102625, https://doi.org/10.1016/j.ffa.2025.102625 (full text not examined).
