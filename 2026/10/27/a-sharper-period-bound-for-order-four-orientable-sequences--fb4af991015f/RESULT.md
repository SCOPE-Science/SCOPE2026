# A sharper period bound for order-four orientable sequences

## Finding
For every even integer \(k\ge4\), every \(k\)-ary orientable sequence of order \(4\) with period \(m\) satisfies

\[
 m\le \frac{k^4-2k^2-3k}{2}.
\]

The previously published even-alphabet bound is \(m\le (k^4-2k^2)/2\). The new bound improves it by \(3k/2\); in particular, at \(k=4\) it lowers the upper bound from \(112\) to \(106\).

## Assumptions and scope
Let the alphabet be \(\mathbb Z_k\), with even \(k\ge4\). An order-four orientable sequence is periodic and has no length-four factor equal to the reversal of any length-four factor, including itself. Its period is \(m\). The result is an upper bound only; it does not assert attainability.

## Proof
Use the order-three de Bruijn digraph whose vertices are triples and whose directed edges are length-four words. Delete every edge labelled by a symmetric length-four word, obtaining \(B_k^*(3)\). A symmetric length-four word has the form \(abba\), so \(B_k^*(3)\) has \(k^4-k^2\) edges, or
\[
N=\frac{k^4-k^2}{2}
\]
reversal-pairs of edges.

For an orientable sequence \(S\), let \(B(S,4)\) consist of the edges labelled by factors of \(S\) and of its reversal. It is closed under edge reversal, has \(2m\) distinct edges, and is Eulerian. Thus it contains exactly \(m\) reversal-pairs. Moreover, every symmetric triple vertex has even in-degree and out-degree in \(B(S,4)\): reversing a circuit swaps in- and out-degrees, and a symmetric vertex is fixed by reversal.

Let \(F=B_k^*(3)\setminus B(S,4)\), and let \(r\) be its number of reversal-pairs. The divergence of a vertex means out-degree minus in-degree. In \(B_k^*(3)\), a vertex \(aab\) with \(a\ne b\) has divergence \(+1\), and a vertex \(abb\) with \(a\ne b\) has divergence \(-1\); all other triples have divergence zero. Since \(B(S,4)\) is Eulerian, the sum of divergences of \(F\) over
\[
P=\{aab:a\ne b\}
\]
is exactly \(|P|=k(k-1)\).

For a reversal-pair, let \(\Delta_P\) be its contribution to that sum. The only pairs with \(\Delta_P=2\) are \(\{aacc,ccaa\}\), where \(a\ne c\): both tails lie in \(P\), while neither head does. There are at most \(\binom{k}{2}\) such pairs. Every other pair not involving a uniform triple contributes at most \(1\) to the sum.

A uniform triple \(aaa\) has out-degree \(k-1\) in \(B_k^*(3)\), which is odd because \(k\) is even. Its out-degree in \(B(S,4)\) must be even, so at least one omitted edge-pair must contain an outgoing edge from each uniform triple. These require at least \(k\) distinct pairs: a non-symmetric length-four edge-pair cannot contain two uniform triple tails. Each such pair has the form \(\{aaax,xaaa\}\) with \(x\ne a\), and contributes \(-1\) to the divergence sum over \(P\), because its only endpoint in \(P\) is the head \(aax\).

If \(u\ge k\) is the number of omitted pairs involving uniform triples and \(c\le\binom{k}{2}\) is the number of special pairs with contribution \(2\), then
\[
k(k-1)\le 2c+(r-u-c)-u=r+c-2u\le r+\binom{k}{2}-2k.
\]
Hence \(r\ge\binom{k}{2}+2k=(k^2+3k)/2\). Subtracting these omitted pairs from the \(N\) available pairs gives
\[
m=N-r\le\frac{k^4-k^2}{2}-\frac{k^2+3k}{2}
=\frac{k^4-2k^2-3k}{2},
\]
as claimed.

## Verification
The proof uses only the edge count, the divergence of each triple type, reversal-pair accounting, and the even-degree condition at symmetric vertices. The key bound is the contribution inequality \(\Delta_P\le1\) for every nonuniform pair except \(\{aacc,ccaa\}\). No finite enumeration or external computation is needed. The right-hand side is an integer for even \(k\).

## Relationship to prior work
Theorem 2.22 of *New orientable sequences* gives \(m\le(k^4-2k^2)/2\) for even \(k\) at order four. Its proof counts local degree restrictions. The present argument additionally sums divergence over all \(k(k-1)\) left-semi-symmetric triple vertices and bounds the contribution of each omitted reversal-pair, yielding the extra term \(-3k/2\). The 2026 construction update still lists period \(88\) for \(k=4\), so the new upper bound \(106\) narrows, but does not close, the known gap.

## Limitations
The bound is not claimed optimal. For \(k=4\), a known construction has period \(88\), leaving a gap of \(18\). The argument does not construct sequences and does not resolve the maximum period for any even alphabet size.

## References
1. C. J. Mitchell and P. R. Wild, “New orientable sequences,” arXiv:2507.02526, first posted 3 July 2025; *Acta Informatica* 63 (2026), article 14. See Theorem 2.22 and the construction table.
2. A. Alhakim, C. J. Mitchell, J. Szmidt, and P. R. Wild, “Orientable sequences over non-binary alphabets,” arXiv:2407.14866, 2024.
3. C. J. Mitchell and P. R. Wild, “Constructing orientable and negative orientable sequences with asymptotically optimal period,” arXiv:2603.18646, first posted 19 March 2026; updated 14 August 2026. See Table 4 for current small-parameter construction records.
4. C. J. Mitchell and P. R. Wild, “New upper bounds for the period of a negative orientable sequence,” arXiv:2602.04433, 2026. This studies a different condition involving the negative of the reversed tuple.
