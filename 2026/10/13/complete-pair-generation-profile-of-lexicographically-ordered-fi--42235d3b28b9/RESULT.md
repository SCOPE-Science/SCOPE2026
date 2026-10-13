# Complete pair-generation profile of lexicographically ordered first-order Reed–Muller codes

## Finding
For every integer \(m\ge2\) and \(n=2^m\), the standard binary truth-table ordering of the first-order Reed–Muller code \(C_m\) has the complete cyclic symbol-pair enumerator
\[
W_p(C_m;z)=1+4\sum_{j=1}^{n/2-1}z^{n/2+j}+3z^n.
\]
For integer \(0\le\alpha\le n\), the pair-generation profile is
\[
\gamma_m(\alpha)=\begin{cases}
0,&0\le\alpha\le n/2,\\
1+\min\{m,2+\lfloor\log_2(\alpha-n/2)\rfloor\},&n/2<\alpha\le n.
\end{cases}
\]
The graph joining distinct codewords whose cyclic pair distance is at most \(\alpha\) has \(2^{m+1-\gamma_m(\alpha)}\) connected components. It first becomes connected at \(\alpha=3n/4\). Its largest disconnected threshold is \(3n/4-1\), compared with \(n/2-1\) for the Hamming metric; the gap is \(n/4\).

## Assumptions and scope
Write each integer \(x\in\{0,1,\ldots,n-1\}\) as its \(m\)-bit vector \((x_0,\ldots,x_{m-1})\), with the least significant bit first. Let
\[
C_m=\big\{(f_{a,b}(0),f_{a,b}(1),\ldots,f_{a,b}(n-1)):\ a\in\mathbb F_2^m,\ b\in\mathbb F_2\big\},
\quad f_{a,b}(x)=b+\sum_{i=0}^{m-1}a_ix_i\pmod2.
\]
In the cyclic symbol-pair metric, \(\operatorname{wt}_p(c)\) is the number of indices \(x\) for which \((c_x,c_{x+1\bmod n})\ne(0,0)\). The graph on \(C_m\) has an edge when \(0<\operatorname{wt}_p(c-d)\le\alpha\). The order \(0,1,\ldots,n-1\) and the cyclic closing pair are essential; arbitrary coordinate permutations are outside this result. All thresholds stated here are integers.

## Proof
Let \(a\ne0\). The truth table of \(f_{a,b}\) is balanced, so it contains \(n/2\) ones. If \(T(a)\) is the number of cyclic transitions between zero and one, then
\[
\operatorname{wt}_p(f_{a,b})=n/2+T(a)/2.
\]
For \(0\le t\le m-2\), exactly \(2^{m-t-1}\) increments \(x\mapsto x+1\) have exactly \(t\) trailing one bits, so these increments toggle bits \(0,\ldots,t\). The transition \(2^{m-1}-1\mapsto2^{m-1}\) and the closing transition \(n-1\mapsto0\) both toggle all \(m\) bits. Introduce prefix parities \(p_t=\sum_{i=0}^{t}a_i\pmod2\). Consequently
\[
\frac{T(a)}2=\sum_{t=0}^{m-2}2^{m-t-2}p_t+p_{m-1}=:s(p).
\]
The transformation \(a\mapsto p\) is invertible and \(s(p)\) has coefficient multiset \(\{1,1,2,4,\ldots,2^{m-2}\}\). Therefore its generating polynomial, over all \(p\in\mathbb F_2^m\), equals
\[
(1+z)\prod_{j=0}^{m-2}(1+z^{2^j})=(1+z)\sum_{j=0}^{n/2-1}z^j
=1+2\sum_{j=1}^{n/2-1}z^j+z^{n/2}.
\]
The unique zero prefix-parity vector corresponds to \(a=0\). Every nonzero \(a\) has two affine constants \(b\), neither changing its pair weight. The zero and all-one words contribute respectively \(1\) and \(z^n\), giving the stated enumerator.

For \(\alpha\le n/2\), no nonzero word has sufficiently small pair weight. Otherwise put \(j=\alpha-n/2\ge1\). A selected nonconstant word corresponds to a prefix-parity vector \(p\) with \(0<s(p)\le j\), and either constant \(b\). The difference of the two words with the same \(a\) and opposite \(b\) is the constant-one codeword, so the selected span contains the constant direction. The positive coefficients defining \(s(p)\) imply that a coordinate \(p_t\) with coefficient greater than \(j\) must vanish in every selected vector. Conversely each unit vector corresponding to a coefficient at most \(j\) is selected. Hence the span of the prefix-parity vectors has dimension equal to the number of coefficients in \(\{1,1,2,4,\ldots,2^{m-2}\}\) not exceeding \(j\): precisely \(\min\{m,2+\lfloor\log_2j\rfloor\}\). Adding the independent affine-constant direction proves \(\gamma_m\).

The graph is a Cayley graph of the additive group \(C_m\), with generating set the nonzero codewords of pair weight at most \(\alpha\). Its components are exactly the cosets of their linear span, so their number is \(2^{m+1-\gamma_m(\alpha)}\). The highest coefficient in \(s(p)\) is \(2^{m-2}\); the graph therefore first becomes connected at \(\alpha=n/2+2^{m-2}=3n/4\). Finally, all nonconstant affine words have Hamming weight \(n/2\), and the two constants for each nonzero \(a\) already span \(C_m\). Thus the Hamming graph first becomes connected at \(n/2\). This proves both thresholds and their difference.

## Verification
Run the included standalone file with `python3 verify_rm_pair.py`. It exhaustively constructs all affine truth tables for \(2\le m\le8\), directly counts cyclic nonzero pair windows, recomputes the entire enumerator and uses binary Gaussian elimination to compute the low-weight span at every integer threshold. The independent finite checks return `VERIFY_OK`. The proof above, not the finite checks, establishes the results for every \(m\ge2\).

## Relationship to prior work
Singh and Singh (arXiv:2609.10989, first posted 10 September 2026) introduce cyclic symbol-pair generation profiles and disconnection thresholds in function-correcting data-protection codes. Their general graph perspective motivates evaluating these invariants explicitly on a classical indexed code family. Pan, Ling, Liu and Chen (DOI:10.1109/TIT.2024.3482726) determine minimum \(b\)-symbol distances of Reed–Muller codes; a minimum distance alone does not provide the complete weight enumerator or the intermediate ranks of the low-pair-weight span. Liang and Liu (DOI:10.1109/TIT.2024.3392744) study generalized pair weights and pair-equiweight code families, but their announced simplex construction is not the present naturally ordered affine truth-table family. These are differences of statements, not claims of exhaustive exclusion of all prior work.

## Limitations
The result depends on the specific truth-table coordinate order and cyclic wraparound; it is not a permutation-invariant statement about Reed–Muller codes. The original 2026 profile paper and the 2025 Reed–Muller \(b\)-symbol distance article could not be inspected completely, leaving a risk of an earlier unindexed exact-profile calculation. No general function-correcting redundancy optimum or independent external audit is claimed.

## References
1. Anamika Singh and Abhay Kumar Singh, *Data Protection in Function-Correcting Symbol-Pair Codes: Redundancy Bounds and Protection Profiles*, arXiv:2609.10989, first posted 2026-09-10. https://arxiv.org/abs/2609.10989
2. Xu Pan, San Ling, Hongwei Liu and Bocong Chen, *On the b-Symbol Distances of Matrix Product Codes, Constacyclic Codes, and Reed-Muller Codes*, IEEE Transactions on Information Theory 71 (2025), 287–296. https://doi.org/10.1109/TIT.2024.3482726
3. Yinghao Liang and Zihui Liu, *The Plotkin-Type Bound on the Generalized Symbol-Pair Weight and Symbol-Pair Equiweight Codes*, IEEE Transactions on Information Theory 70 (2024), 4990–5001. https://doi.org/10.1109/TIT.2024.3392744
