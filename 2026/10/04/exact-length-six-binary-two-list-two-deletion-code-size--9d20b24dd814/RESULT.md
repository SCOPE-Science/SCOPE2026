# Exact length-six binary two-list two-deletion code size
## Finding
Let \(A_{2,2}^{\mathrm{del}}(6)\) be the largest cardinality of a set \(C\subseteq\{0,1\}^6\) for which every \(y\in\{0,1\}^4\) is a subsequence of at most two members of \(C\). Then
\[
A_{2,2}^{\mathrm{del}}(6)=7.
\]
One optimal code is
\[
C=\{000000,000001,011100,100110,101111,110001,111111\}.
\]

## Assumptions and scope
A word \(y\in\{0,1\}^4\) is a two-deletion output of \(x\in\{0,1\}^6\) when \(y\) is obtained by deleting exactly two coordinates of \(x\). The list-size-two condition means that, for every received word \(y\), at most two codewords contain \(y\) as a subsequence. This is Definition 2.1 of Lin's \(t\)-list-decodable \(k\)-deletion code specialized to \(n=6\), \(k=2\), and \(t=2\).

## Proof
The displayed seven-word set gives the lower bound. Direct exact enumeration of its two-deletion outputs shows that no length-four word is produced by more than two codewords.

For the upper bound, define a nonnegative weight \(w\) on length-four binary words by
\[
egin{aligned}
w(0000)&=w(1111)=\frac35,\qquad
w(0001)=w(0111)=w(1000)=w(1110)=\frac25,\\
w(0011)&=w(1100)=\frac15,
\end{aligned}
\]
and let all other length-four words have weight \(0\). For every \(x\in\{0,1\}^6\), let \(D_2(x)\) be the set of distinct length-four subsequences obtainable from \(x\) by two deletions. Exact enumeration of all \(64\) words verifies
\[
1\le \sum_{y\in D_2(x)} w(y)+\frac25\,\mathbf 1_{x\in\{000000,111111\}}.
\]
The certificate is finite and exact; `certificate.tsv` lists every ambient word and its rational left-hand side, while `verify.py` regenerates the inequality from first principles using rational arithmetic.

Now let \(C\) be any binary two-list two-deletion code of length six. Summing the preceding inequality over \(x\in C\), every received word \(y\) contributes at most twice because its list size is at most two. The two endpoint corrections contribute at most \(4/5\). Therefore
\[
|C|\le 2\sum_{y\in\{0,1\}^4}w(y)+\frac45
=2\cdot\frac{16}5+\frac45
=\frac{36}5<8.
\]
Since \(|C|\) is an integer, \(|C|\le7\). Together with the explicit witness, this proves the claim.

## Verification
Run `python3 verify.py`. It checks all \(64\) length-six words, verifies the exact pointwise weighted inequality with `Fraction` arithmetic, confirms \(\sum_y w(y)=16/5\), obtains the global upper bound \(36/5\), and independently checks that the seven-word witness has received-word multiplicity at most two. The expected terminal marker is `VERIFY_OK`.

## Relationship to prior work
Lin introduced the \((k,t)\)-deletion hypergraph and proved asymptotic lower bounds for binary \(t\)-list-decodable \(k\)-deletion codes. His full text defines the same list-decoding condition used here and discusses \(k=t=2\) only asymptotically; it does not give the exact finite optimum at \(n=6\). Guruswami and Håstad previously constructed asymptotically large binary two-deletion codes with list size two, again without an exact small-length table. The present result is a finite extremal benchmark for the newly emphasized \((2,2)\)-deletion hypergraph and is certified by a short rational packing argument rather than by a solver transcript.

## Limitations
The claim is only for binary length six, exactly two deletions, and list size two. It does not determine the optimum for other lengths, larger deletion counts, or larger lists. The originality search found no matching exact value, but absence from searched databases is not a proof that the parameter has never appeared in unindexed literature.

## References
1. Andrew D. Lin, *Lower Bounds for all List-Decodable Deletion Codes*, arXiv:2609.26650v1, first submitted 2026-09-22.
2. Venkatesan Guruswami and Johan Håstad, *Explicit two-deletion codes with redundancy matching the existential bound*, arXiv:2007.10592v1; later IEEE Transactions on Information Theory.
3. Noga Alon, Gabriela Bourla, Ben Graham, Xiaoyu He, and Noah Kravitz, *Logarithmically Larger Deletion Codes of All Distances*, IEEE Transactions on Information Theory 70(1), 2024.
