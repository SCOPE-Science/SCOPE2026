# Exact weight-two binary one-deletion code capacity

## Finding

For every integer \(n\ge 2\), let \(W_{n,2}\) be the set of length-\(n\) binary words containing exactly two ones. For each word \(w\), write \(D(w)\) for the **set of distinct** length-\(n-1\) words obtained by deleting exactly one symbol of \(w\), at an unknown position. Define \(A_{\mathrm{del},2}(n)\) as the largest cardinality of a subset \(C\subseteq W_{n,2}\) such that \(D(u)\cap D(v)=\varnothing\) for distinct \(u,v\in C\). Then

\[
A_{\mathrm{del},2}(n)=\left\lfloor\frac{3n-2}{4}\right\rfloor\qquad(n\ge2).
\]

This gives the exact one-deletion capacity of the first nontrivial constant-weight binary source, including an explicit optimal construction at every blocklength.

## Assumptions and scope

The channel deletes **exactly one** symbol. Deletion position is not reported to the receiver. Every transmitted codeword has exactly two ones; the output may have one or two ones. Repeated outcomes from deleting distinct positions of one word count only once. There is no restriction on where the two ones lie, apart from the common codeword length. All indices in the proof start at one. The theorem includes the short boundary case \(n=2\), where the unique permitted word is `11`.

## Proof

Fix \(n\ge2\) and put \(m=n-1\). Represent any word having its two ones in positions \(i<j\) by the pair

\[
(a,b)=(i,j-1),\qquad 1\le a\le b\le m.
\]

The two possible deletions of a one yield length-\(m\) words of weight one whose unique one is at position \(a\) or \(b\). If \(a=b\), call the codeword a **loop**; its two ones are adjacent, and it has only one distinct weight-one deletion output. If \(a<b\), call it an **edge**; it has two distinct weight-one outputs, labeled \(a\) and \(b\).

Let \(C\) be any one-deletion-correcting code, with \(t\) loops and \(e\) edges. Because the weight-one output sets of different codewords are disjoint, and because there are precisely \(m\) possible weight-one length-\(m\) words,

\[
t+2e\le m.\tag{1}
\]

Two loops with consecutive labels \(t_0\) and \(t_0+1\) share a weight-two descendant: the word with ones at positions \(t_0,t_0+1\) of the length-\(m\) output, obtained by deleting a zero after the first loop or before the second loop. Hence loop labels form a subset of \(\{1,\ldots,m\}\) containing no two consecutive integers. Therefore

\[
t\le\left\lceil\frac m2\right\rceil.\tag{2}
\]

Equations (1) and (2) imply

\[
|C|=t+e\le \left\lfloor\frac{m+t}{2}\right\rfloor
\le\left\lfloor\frac{m+\lceil m/2\rceil}{2}\right\rfloor
=\left\lfloor\frac{3n-2}{4}\right\rfloor.\tag{3}
\]

For equality, select all loops labeled \(t_0=1,3,5,\ldots\le m\), meaning codewords whose ones occupy \((t_0,t_0+1)\). In addition select every edge labeled

\[
(a,b)=(4k+2,4k+4),\qquad k\ge0,\quad4k+4\le m,
\]

meaning codewords whose ones occupy \((4k+2,4k+5)\). There are \(\lceil m/2\rceil\) loops and \(\lfloor m/4\rfloor\) edges. Their total size is

\[
\left\lceil\frac m2\right\rceil+\left\lfloor\frac m4\right\rfloor
=\left\lfloor\frac{3n-2}{4}\right\rfloor,\tag{4}
\]

as one checks in the four cases \(m\bmod4\).

It remains to check that **all** deletion descendants are disjoint, not only the weight-one descendants. The selected loops have weight-one outputs only at odd positions. The selected edges have weight-one outputs at the even positions \(4k+2\) and \(4k+4\); these labels never repeat. Thus the weight-one descendants are disjoint.

A word represented by \((a,b)\) has weight-two descendants obtained by deleting a zero. Such descendants, represented by their two one-positions in the length-\(m\) output, lie among

\[
(a-1,b)\ \ (a>1),\qquad (a,b)\ \ (a<b),\qquad
(a,b+1)\ \ (b<m).
\tag{5}
\]

A loop \((t_0,t_0)\) has only the adjacent-pair outputs \((t_0-1,t_0)\) (if available) and \((t_0,t_0+1)\) (if available). For odd \(t_0\), these sets are disjoint across the loops: the first coordinate of a resulting adjacent pair is one of \(t_0-1,t_0\), and each possible first coordinate belongs to only one selected loop.

For an edge \((a,b)=(4k+2,4k+4)\), (5) yields possible pairs \((a-1,a+2)\), \((a,a+2)\), and \((a,a+3)\), with unavailable boundary pairs omitted. Their coordinate gaps are two or three, so none can collide with a loop descendant, whose coordinate gap is one. Finally, for different edge indices \(k\), the first coordinates lie in the disjoint two-element sets \(\{4k+1,4k+2\}\). Hence no two selected edges have the same weight-two descendant. All deletion balls are therefore pairwise disjoint. Equation (4) attains (3), proving the theorem.

## Verification

Run `python3 check.py` using Python 3.8 or later. The script generates the proposed code and checks all of its exact deletion outputs at every length \(2\le n\le80\). It also performs an exhaustive maximum-clique search over the compatibility graph of **all** weight-two words at each length \(2\le n\le9\). Both checks passed. These finite tests corroborate the proof but are not used to infer the infinite theorem.

## Relationship to prior work

The deletion-correction criterion is standard; see Chee, Ge and Ling. Cullina, Kulkarni and Kiyavash introduce deletion graphs induced on fixed Hamming-weight layers and determine optimal **colorings** of those layers; their theorem gives the chromatic number, which is not the maximum independent-set cardinality computed here. Kulkarni and Kiyavash give a general constrained-source hypergraph optimization formulation and upper bounds, illustrated by run-length-limited sources; that formulation does not itself evaluate the weight-two maximum or produce the construction above. The present result gives an exact value and explicit witnesses for this natural sparse layer.

## Limitations

The result concerns a fixed binary weight of exactly two and exactly one deletion. It does not determine optimal mixed-weight codes, higher-weight layers, or two-or-more-deletion correction. The literature comparison covers the inspected publications and database records; absence of a located equivalent prior theorem is not a proof that no earlier unpublished or unindexed derivation exists. Independent mathematical audit has not been performed.

## References

Chee, Y. M., Ge, G., and Ling, A. C. H., *Spectrum of Sizes for Perfect Deletion-Correcting Codes*, SIAM Journal on Discrete Mathematics **24** (2010), 33–55, DOI 10.1137/090751311; publicly released 2010-02-05.

Cullina, D., Kulkarni, A. A., and Kiyavash, N., *Two Approaches to the Construction of Deletion Correcting Codes: Weight Partitioning and Optimal Colorings*, arXiv:1211.4056v1 (2012), especially Sections II–IV and Theorem 5.

Kulkarni, A. A., and Kiyavash, N., *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128v1 (2012), especially Section V on constrained sources.
