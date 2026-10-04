# Dissociation polynomials of complete multipartite graphs and their coefficientwise extremizers
## Finding
For every connected complete multipartite graph \(G=K_{n_1,\ldots,n_r}\) with \(r\ge2\) and \(N=\sum_i n_i\), a vertex set is a dissociation set if and only if it has size at most two or is contained in a single part. Hence \[D_G(z)=\sum_{i=1}^r(1+z)^{n_i}-(r-1)+z^2\sum_{1\le i<j\le r}n_i n_j.\] Equivalently, \([z^k]D_G(z)\) equals \(1\), \(N\), and \(\binom{N}{2}\) for \(k=0,1,2\), and \(\sum_i\binom{n_i}{k}\) for \(k\ge3\). Among all complete \(r\)-partite graphs of order \(N\), the balanced Turan graph \(T_{N,r}\) uniquely minimizes and \(K_{N-r+1,1,\ldots,1}\) uniquely maximizes the polynomial coefficientwise; therefore they are also the unique minimizer and maximizer of \(D_G(z)\) for every real \(z>0\).

## Assumptions and scope
A dissociation set is a vertex set whose induced subgraph has maximum degree at most one. The dissociation polynomial is
\[
D_G(z)=\sum_{S\text{ dissociation}}z^{|S|}.
\]
Here \(G=K_{n_1,\ldots,n_r}\) is connected, so \(r\ge2\), each \(n_i\ge1\), and \(N=\sum_i n_i\).

## Proof
Every set of size at most two is dissociated. Let \(|S|\ge3\). If \(S\) meets two parts, choose \(x,y\in S\) from different parts and a third vertex \(w\in S\). If \(w\) lies with \(x\), then \(y\) has two neighbours in \(S\); if \(w\) lies with \(y\), then \(x\) has two; if \(w\) lies in a third part, then both do. Hence a dissociation set of size at least three lies in one part. Conversely, every subset of one part is independent and therefore dissociated.

Summing \((1+z)^{n_i}\) over the parts counts the empty set \(r\) times and misses exactly the cross-part pairs. Thus
\[
D_G(z)=\sum_{i=1}^r(1+z)^{n_i}-(r-1)+z^2\sum_{i<j}n_i n_j.
\]
Consequently all complete \(r\)-partite graphs of order \(N\) have the same coefficients in degrees zero, one, and two, while for \(k\ge3\),
\[
[z^k]D_G(z)=\sum_i\binom{n_i}{k}.
\]

For fixed \(N,r\), suppose two part sizes satisfy \(a\ge b+2\). Replacing them by \(a-1,b+1\) changes the degree-\(k\) sum by
\[
\binom{a}{k}+\binom{b}{k}-\binom{a-1}{k}-\binom{b+1}{k}
=\binom{a-1}{k-1}-\binom{b}{k-1}\ge0.
\]
Hence balancing weakly decreases every coefficient with \(k\ge3\), and repeated balancing reaches \(T_{N,r}\). At \(k=3\) every nontrivial balancing step is strict, so the balanced part multiset is the unique minimizer.

Conversely, if \(a\ge b\ge2\), replacing \(a,b\) by \(a+1,b-1\) increases every degree-\(k\) coefficient by
\[
\binom{a}{k-1}-\binom{b-1}{k-1}\ge0.
\]
Repeated concentration reaches \((N-r+1,1,\ldots,1)\), and the cubic coefficient increases strictly at every step. This gives the unique coefficientwise maximum. Since all coefficients are nonnegative and the first three are fixed, the same two graphs uniquely extremize \(D_G(z)\) for every \(z>0\).

## Verification
The included checker constructs each complete multipartite graph from part labels, enumerates every vertex subset, and tests induced degrees directly. It verifies the polynomial formula for every complete multipartite isomorphism type of orders two through ten. Separately it enumerates all part-size partitions through order twenty-five and verifies both coefficientwise extremal statements and cubic strictness.

## Relationship to prior work
Tu, Xiao, and Lang define the dissociation polynomial as a weighted counting object and prove an extremal theorem for cubic graphs. Their graph class is different from complete multipartite graphs, and their published statement does not give the formula or fixed-part-count extremizers above. Targeted semantic and exact searches for complete-multipartite, complete-bipartite, and Turan dissociation polynomials did not locate an equivalent result.

## Limitations
The extremal theorem fixes both \(N\) and \(r\), and the exact formula concerns complete multipartite graphs only. The finite computation is corroborative rather than a proof of the infinite statement. Search coverage cannot exclude differently phrased or non-indexed prior work.

## References
1. J. Tu, J. Xiao, R. Lang, “Counting the number of dissociation sets in cubic graphs,” AIMS Mathematics 8 (2023), 10021–10032, DOI 10.3934/math.2023507.
