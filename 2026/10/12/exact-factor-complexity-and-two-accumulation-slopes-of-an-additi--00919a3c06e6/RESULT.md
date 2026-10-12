# Exact factor complexity and two accumulation slopes of an additive-power-free rich word

## Finding

Let \(\beta:\{0,1\}^*\to\{0,1\}^*\) be the length-five morphism
\[\beta(0)=00001,\qquad\beta(1)=01101,\]
and let \(B=\beta^\omega(0)\). This is the rich, additive-five-power-free infinite binary word constructed by Andrade and Mol [1]. Let \(p(n)\) count its distinct contiguous factors of length \(n\). Define, for every integer \(k\ge0\),
\[s_k=\frac{7\cdot5^k+1}{4},\qquad t_k=\frac{15\cdot5^k-3}{4}.\]
Then \(p(0)=1\), and for every integer \(n\ge1\),
\[\boxed{p(n)=2n+\sum_{k\ge0}\max\{0,\min(n-1,t_k)-s_k+1\}.}\]
Only finitely many summands are nonzero. Equivalently, for every \(n\ge1\),
\[p(n+1)-p(n)=\begin{cases}3,&s_k\le n\le t_k\text{ for some }k\ge0,\\2,&\text{otherwise}.\end{cases}\]
In particular, this canonical avoidability witness has two distinct asymptotic density slopes:
\[\boxed{\liminf_{n\to\infty}\frac{p(n)}n=\frac{16}{7},\qquad\limsup_{n\to\infty}\frac{p(n)}n=\frac83.}\]

## Assumptions and scope

A factor is a contiguous subword; factors are counted without multiplicity. The empty factor is counted once. The fixed point exists because \(\beta(0)\) starts with \(0\). Both image words contain both letters, so the fixed point is uniformly recurrent: in particular, every finite factor admits arbitrarily late occurrences and two-sided occurrence contexts. All assertions concern this particular fixed point, without claiming extremality among all rich or additive-power-free words.

## Proof

**1. Unique block recognition.** Every image block starts in \(0\), ends in \(1\), and has length five. The word `0000` occurs only at offset zero of \(\beta(0)\), and `11` occurs only at offset one of \(\beta(1)\); neither marker can cross a block boundary, since a boundary has the form `10`. Every length-eight factor contains at least one marker. Indeed, if a window starts at block offset zero, two, three or four, it includes a whole image block; if it starts at offset one, either its current block is \(\beta(1)\) and it contains `11`, or the next block's first four symbols contain `0000` or `11`. Thus every factor of length at least eight has a unique residue class modulo five for the start of each occurrence in the displayed image-block tiling.

**2. Bispecial desubstitution.** A factor is left-special if both binary left extensions occur, right-special if both right extensions occur, and bispecial if both hold. Consider any factor of length at least eight, so its block phase is fixed. It can begin at a left-special position only at block offset three: the preceding character is fixed at offsets zero, one, four, and at offset two the preceding character equals the factor's first character. Similarly, it can end at a right-special position only at block offset zero: all other offsets have a fixed next symbol, or the next symbol is determined by the final symbol. Therefore every bispecial factor of length at least eight has the unique form
\[\Phi(u)=01\,\beta(u)\,0\]
for a nonempty factor \(u\) of \(B\). Its length is \(5|u|+3\). For every context \(a u b\) in \(B\), the corresponding occurrence of \(\Phi(u)\) starts at block offset three of \(\beta(a)\) and ends at offset zero of \(\beta(b)\). The immediately preceding and succeeding symbols are precisely \(a\) and \(b\), because the offset-two symbol of \(\beta(a)\) equals \(a\), and the offset-one symbol of \(\beta(b)\) equals \(b\). Conversely, unique phase recognition shows all occurrence contexts of \(\Phi(u)\) arise this way. Hence the bilateral extension pairs of \(u\) and \(\Phi(u)\) coincide exactly: bispeciality and bilateral order are preserved in both directions.

**3. Finite seeds.** For a factor \(u\), put \(E(u)=\{(a,b):aub\text{ occurs in }B\}\), \(L(u)=\{a:(a,b)\in E(u)\}\), \(R(u)=\{b:(a,b)\in E(u)\}\) and \(j(u)=|E(u)|-|L(u)|-|R(u)|+1\). Any non-bispecial factor has \(j(u)=0\). The length-three factors of \(B\) are exactly `000`, `001`, `010`, `011`, `100`, `101`, `110`: the pattern `111` is impossible and the other seven appear in \(\beta^2(0)\). Every context of a factor of length at most seven has length at most nine, and hence lies in the image of three consecutive letters. Enumerating the seven displayed triples and the factor windows in their images yields the following *complete list of nonzero bilateral orders* at lengths zero through seven:

| Length | Factor | Bilateral order |
|---:|:---:|---:|
| 0 | empty | +1 |
| 1 | `0` | +1 |
| 3 | `000` | −1 |
| 3 | `010` | +1 |
| 3 | `101` | −1 |

Every other factor in this finite range has bilateral order zero. The displayed seven-triple enumeration is directly reproducible by the attached checker. In conjunction with Step 2, every nonzero bilateral order at length at least eight is an iterate of \(\Phi\) from a positive-length seed. Since \(|\Phi(u)|=5|u|+3\), the total bilateral-order sum at length \(m\ge0\) is \(1\) for \(m=0\), is \(+1\) at
\[m=\frac{7\cdot5^k-3}{4}\quad(k\ge0),\]
is \(-1\) at
\[m=\frac{15\cdot5^k-3}{4}\quad(k\ge0),\]
and is zero otherwise.

**4. Factor-complexity recurrence.** Each factor of length \(m+2\) has a unique central length-\(m\) factor, so \(p(m+2)=\sum_{|u|=m}|E(u)|\). Likewise, \(p(m+1)=\sum_{|u|=m}|L(u)|=\sum_{|u|=m}|R(u)|\), and \(p(m)=\sum_{|u|=m}1\). Therefore for every \(m\ge0\),
\[p(m+2)-2p(m+1)+p(m)=\sum_{|u|=m}j(u).\]
With \(p(0)=1\) and \(p(1)=2\), integration of the bilateral-order sequence from Step 3 gives \(p(n+1)-p(n)=3\) precisely on the disjoint integer intervals \([s_k,t_k]\), and \(2\) elsewhere for \(n\ge1\). Summing the first differences yields the boxed formula.

**5. Asymptotic oscillation.** Each interval \([s_k,t_k]\) has exactly \(2\cdot5^k\) integers. At \(n=s_k\), the excess \(p(n)-2n\) is precisely \((5^k-1)/2\), so \(p(s_k)/s_k\to 16/7\). At \(n=t_k+1\), the excess is \((5^{k+1}-1)/2\), so \(p(t_k+1)/(t_k+1)\to 8/3\). Within each high interval, the excess-to-length ratio increases, since its numerator increments by one and is smaller than the denominator. Between consecutive high intervals, that ratio decreases since its numerator is constant. The two sequences of endpoints therefore attain the global lower and upper accumulation limits.

## Verification

Run `python3 verify.py` using only Python's standard library. It independently enumerates all seven length-three source contexts, checks the block markers and finite bilateral-order seeds, and compares the closed formula with sliding-window factor sets for every \(1\le n\le260\) in the \(78125\)-symbol prefix \(\beta^7(0)\). It additionally recomputes nonzero bilateral orders at six lengths through \(93\). Successful output: `VERIFY_OK blocks=7 contexts=7 base=0..7 factors=1..260 bispecial_lengths=8,13,18,43,68,93 prefix=78125`. The all-length conclusion is derived from the explicit desubstitution proof, not extrapolated from these finite checks.

## Relationship to prior work

Andrade and Mol [1] introduced the exact morphism and proved that its fixed point is rich and avoids additive fifth powers. Their August 2024 first preprint and February 2025 revision were compared; the exact factor-complexity formula, bilateral-order classification and two distinct normalized accumulation slopes are not among their stated results. Shallit and Shur [2] study connections between factor complexity and power avoidance for other named infinite words, motivating the invariant, but predate this specific 2024 construction. General effective algorithms for automatic or morphic words may compute complexity; algorithmic computability alone does not imply the explicit interval formula or its derived oscillations. No equivalent result was identified in the searched mathematical literature or indexed research records, subject to residual indexing and priority risk.

## Limitations

The theorem concerns ordinary contiguous factor complexity, not abelian complexity or scattered subsequence complexity. It does not claim that either accumulation slope is optimal over all rich words satisfying additive-power restrictions. The external 2024 richness and power-freeness claims are cited solely to motivate the object; the exact complexity proof uses only the displayed morphism. Independent validation and external priority review remain outstanding.

## References

[1] J. Andrade and L. Mol, *Avoiding abelian and additive powers in rich words*, arXiv:2408.15390v1 (first public August 27, 2024), https://arxiv.org/html/2408.15390v1 ; revised arXiv:2408.15390v2, https://arxiv.org/pdf/2408.15390 .

[2] J. Shallit and A. M. Shur, *Subword complexity and power avoidance*, arXiv:1801.05376v1 (January 16, 2018), https://arxiv.org/pdf/1801.05376 .
