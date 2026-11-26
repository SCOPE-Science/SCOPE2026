# A sharper period bound for order-four orientable sequences

## Finding
For every even integer \(k\ge4\), every \(k\)-ary orientable sequence of order \(4\) with period \(m\) satisfies
\[
 m\le \frac{k^4-2k^2-3k}{2}.
\]
The previously published even-alphabet bound is \(m\le (k^4-2k^2)/2\). The bound above improves it by \(3k/2\). Combined with the existing explicit cycles of lengths \(106\) and \(603\) in [5, 6], it gives exact maxima at \(k=4\) and \(k=6\), respectively.

## Assumptions and scope
Let \(S=(s_i)\) be periodic over \(\mathbb Z_k\), with least period \(m\) and even \(k\ge4\). For \(i\in\mathbb Z/m\mathbb Z\) let \(w_i=s_i s_{i+1}s_{i+2}s_{i+3}\) be the window read cyclically. Orientable of order four means that \(w_i\ne w_j\) for all distinct \(i,j\), and \(w_i\ne w_j^R\) for all \(i,j\), including \(i=j\), where \(R\) denotes ordinary reversal. Equivalently, every occurring window is nonpalindromic and at most one starting position in a period is allowed per reversal class.

## Proof
Use the de Bruijn digraph with triples as vertices and length-four words as directed edges from their prefix triple to their suffix triple. Delete every symmetric edge \(abba\), obtaining \(B_k^*(3)\), with \(k^4-k^2\) edges or
\[
N=\frac{k^4-k^2}{2}
\]
reversal-pairs of edges.

Let \(B(S,4)\) be the union of the cyclic walk of windows of \(S\) and its reversed walk. Distinctness and reversal avoidance imply that the two walks have disjoint edge sets, each of size \(m\). Their union is reversal-closed and balanced at every vertex, and contains exactly \(m\) reversal-pairs. At a symmetric triple, reversal swaps the first walk's in- and out-degrees, which are equal because it is closed. Thus the union has even out-degree (and even in-degree) at every symmetric triple.

Let \(F=B_k^*(3)\setminus B(S,4)\), and let \(r\) count its reversal-pairs. Write divergence for out-degree minus in-degree. In the full de Bruijn graph both degrees are \(k\). An edge \(abba\) deletes one outgoing edge at \(abb\) and one incoming edge at \(bba\); when \(a=b\), these deletions are at the same vertex. Thus in \(B_k^*(3)\) the divergence is \(+1\) at each \(aab\) with \(a\ne b\), \(-1\) at each \(abb\) with \(a\ne b\), and zero elsewhere. By balance of \(B(S,4)\), the divergence of \(F\) summed over \(P=\{aab:a\ne b\}\) is \(k(k-1)\).

Denote a reversal-pair's contribution to that sum by \(\Delta_P\). The only pairs with \(\Delta_P=2\) are \(\{aacc,ccaa\}\), \(a\ne c\): both tails must lie in \(P\), in which case neither head does. There are \(\binom{k}{2}\) such pairs. Every other pair contributes at most \(1\).

Each uniform triple \(aaa\) has odd out-degree \(k-1\) in \(B_k^*(3)\) and even out-degree in \(B(S,4)\), so at least one pair with an outgoing edge there is omitted. Each pair incident to a uniform triple has the form \(\{aaax,xaaa\}\), \(x\ne a\), and is incident to only one uniform triple. This pair contributes \(-1\) to the sum over \(P\): its only endpoint in \(P\) is the head \(aax\).

Consequently if \(u\ge k\) of the omitted pairs are incident to uniform triples and \(c\le \binom{k}{2}\) contribute \(2\), then
\[
k(k-1)\le 2c+(r-u-c)-u=r+c-2u\le r+\binom{k}{2}-2k.
\]
Hence \(r\ge\binom{k}{2}+2k=(k^2+3k)/2\). Subtracting from \(N\) yields the asserted bound.

## Verification
The universal bound uses the count of nonpalindromic words, balanced degrees of the cyclic walks, reversal-pair divergences and parity at uniform triples. No finite enumeration or external computation is required for this bound. For the two exact maxima, read each published `witness.txt` in [5, 6] as a cyclic word. The lengths are \(106\) and \(603\); all letters lie in the respective alphabets. No window equals its reversal, and the number of distinct canonical representatives \(\min(w_i,w_i^R)\) is \(106\) and \(603\), respectively. Uniqueness forces the least period to equal the displayed word length.

## Relationship to prior work
Theorem 2.22 of *New orientable sequences* gives \(m\le(k^4-2k^2)/2\) for even \(k\) at order four. The argument here additionally sums divergence over all \(k(k-1)\) left-semi-symmetric triples and bounds the contribution of each omitted reversal-pair, yielding the extra term \(-3k/2\). The construction update in [3] lists periods \(88\) and \(552\) for \(k=4\) and \(k=6\); the explicit witnesses in [5, 6] attain the new bounds \(106\) and \(603\).

## Limitations
The bound does not apply to sequences that only avoid reversal but allow repeated windows. The proof gives no general construction, and attainability is not claimed for arbitrary even \(k\).

## References
1. C. J. Mitchell and P. R. Wild, “New orientable sequences,” arXiv:2507.02526, first posted 3 July 2025; *Acta Informatica* 63 (2026), article 14. See Theorem 2.22 and the construction table.
2. A. Alhakim, C. J. Mitchell, J. Szmidt, and P. R. Wild, “Orientable sequences over non-binary alphabets,” arXiv:2407.14866, 2024.
3. C. J. Mitchell and P. R. Wild, “Constructing orientable and negative orientable sequences with asymptotically optimal period,” arXiv:2603.18646, first posted 19 March 2026. See Table 4 for small-parameter construction records.
4. C. J. Mitchell and P. R. Wild, “New upper bounds for the period of a negative orientable sequence,” arXiv:2602.04433, 2026. This studies the different condition involving the negative of the reversed tuple.
5. [“A 106-symbol quaternary orientable cycle of order four,” explicit witness](https://github.com/Resultary/2026/tree/main/2026/10/12/SCOPE-a-106-symbol-quaternary-orientable-cycle-of-order-four--341177c7af0a).
6. [“A six-symbol orientable cycle of order four and period 603,” explicit witness](https://github.com/Resultary/2026/tree/main/2026/10/13/SCOPE-a-six-symbol-orientable-cycle-of-order-four-and-period-603--7e0973a0f822).
