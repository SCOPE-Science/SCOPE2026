# Sharp large-alphabet one-deletion lists for single-parity-check codes

## Finding

Fix integers \(n\ge2\) and a prime power \(q\ge n\). For any nonzero parity-check vector \(h=(h_1,\ldots,h_n)\in\mathbb F_q^n\), let
\[
C_h=\{x\in\mathbb F_q^n:\sum_{j=1}^{n}h_jx_j=0\}
\]
and let \(\Lambda(h)\) denote the maximum, over all received words \(y\in\mathbb F_q^{n-1}\), of the number of **distinct** words of \(C_h\) that produce \(y\) by deleting exactly one coordinate.

Let \(Z=\{j:h_j=0\}\) and \(z=|Z|\). For each \(j\in Z\), obtain \(u_j\in\mathbb F_q^{n-1}\) by deleting coordinate \(j\) from \(h\), and set
\[
W=\operatorname{span}_{\mathbb F_q}\{u_j:j\in Z\},
\]
with \(W=\{0\}\) when \(Z\) is empty. For every \(1\le i<n\) with \(h_i h_{i+1}\ne0\), form the merged vector
\[
b_i=(h_1,\ldots,h_{i-1},h_i+h_{i+1},h_{i+2},\ldots,h_n)
\in\mathbb F_q^{n-1}.
\]
Let
\[
g(h)=|\{i:1\le i<n,\ h_i h_{i+1}\ne0,\ b_i\notin W\}|.
\]
**Theorem.** For every such \(q,n,h\),
\[
\boxed{\Lambda(h)=1+(q-1)z+g(h).}
\]
Thus an exact worst-case one-deletion list size is computable using only ranks of matrices with at most \(n\) columns, in polynomial time.

In \(\mathbb F_5^4\), the check vectors \(h=(0,1,1,0)\) and \(h'=(0,1,4,0)\) have identical zero positions but different worst-case list sizes, \(\Lambda(h)=10\) and \(\Lambda(h')=9\). The distinction is whether the unique merged vector is in the span \(W\); it cannot be inferred from the zero/nonzero pattern alone.

## Assumptions and scope

The alphabet is the field \(\mathbb F_q\) with any prime-power cardinality \(q\ge n\), and the code is the codimension-one linear hyperplane specified by a **nonzero** check vector \(h\). The channel deletes exactly one coordinate, with no substitutions, and each distinct codeword is counted once even if several deletion positions give the same received word. No assumption is imposed on the number, positions, or values of nonzero entries of \(h\). The formula makes no claim for general \(q<n\).

## Proof

**1. Exact count from insertion positions.** Index insertion positions by \(j\in\{1,\ldots,n\}\). Given \(y=(y_1,\ldots,y_{n-1})\), let \(A_j(y)\subseteq\mathbb F_q\) be the possible inserted symbols that produce a codeword when placed at gap \(j\). If \(h_j\ne0\), the parity-check equation determines exactly one inserted symbol, so \(|A_j(y)|=1\). If \(h_j=0\), that equation reduces to \(u_j\cdot y=0\); in this case \(A_j(y)=\mathbb F_q\), otherwise \(A_j(y)=\varnothing\).

An insertion at gap \(i\) and an insertion at gap \(i+1\) give the same parent precisely when both insert the symbol \(y_i\). More generally, if two insertion descriptions at nonadjacent gaps give the same parent, all intervening gaps also describe that parent: the intervening symbols in \(y\) must equal the inserted symbol. Consequently, the equivalence classes of insertion descriptions are contiguous intervals of gaps. Counting their connected components in a path gives the exact identity
\[
|\{x\in C_h:y\preceq x\}|
=\sum_{j=1}^{n}|A_j(y)|
-\sum_{i=1}^{n-1}\mathbf1\{y_i\in A_i(y)\cap A_{i+1}(y)\}.
\tag{1}
\]
Here \(y\preceq x\) denotes deletion of exactly one symbol from \(x\).

**2. A maximizer activates every zero position.** At \(y=0\), all \(z\) zero-check gaps admit all \(q\) symbols, and every other gap admits just the zero symbol. The distinct parents are the zero word and \(q-1\) independent nonzero insertions at each zero-check gap. Therefore the maximum is at least \(1+(q-1)z\). If \(z\ge1\) and at least one zero-check gap fails \(u_j\cdot y=0\), at most \(q(z-1)+(n-z)\) insertion descriptions survive, and hence at most that many distinct parents survive. Since
\[
q(z-1)+(n-z)=1+(q-1)z+(n-q-1)<1+(q-1)z
\]
for \(q\ge n\), no maximizing \(y\) can have an inactive zero-check gap. If \(z=0\), the condition is vacuous.

It follows that a maximizing \(y\) belongs to the orthogonal complement \(W^\perp\). For these \(y\), every adjacent pair of gaps with at least one zero-check coefficient is a duplicate pair in (1). There are \(n-1-e\) such pairs, where
\[
e=|\{i:1\le i<n,\ h_i h_{i+1}\ne0\}|.
\]
For an adjacent pair with both check coefficients nonzero, the shared insertion letter \(y_i\) is permitted exactly when the corresponding merged-check equation \(b_i\cdot y=0\) holds. Hence (1) reduces exactly to
\[
|\{x\in C_h:y\preceq x\}|
=1+(q-1)z+|\{i:h_i h_{i+1}\ne0,\ b_i\cdot y\ne0\}|.
\tag{2}
\]

**3. Simultaneous avoidance achieves every unforced gain.** For \(y\in W^\perp\), a vector \(b_i\in W\) has \(b_i\cdot y=0\) identically. Each \(b_i\notin W\), on the other hand, induces a nonzero linear functional on \(W^\perp\). Its kernel contains exactly a fraction \(1/q\) of that finite vector space. There are \(g(h)\le n-1<q\) such proper hyperplanes. Their union cannot cover \(W^\perp\), since the sum of their cardinalities is strictly less than \(|W^\perp|\). Choosing \(y\) outside their union makes all \(g(h)\) unforced terms in (2) contribute one, and no other term can contribute. The theorem follows. \(\square\)

For the explicit example \(h=(0,1,1,0)\) over \(\mathbb F_5\), \(y=(1,4,1)\) attains \(10\). For \(h'=(0,1,4,0)\), the received zero word attains \(9\). The alphabet hypothesis cannot simply be dropped: for \(q=2\), \(n=4\), and \(h=(1,1,1,1)\), the displayed rank expression equals \(4\) but the actual maximum is \(3\).

## Verification

Run `python3 verify.py` from this directory. The file uses standard-library Python only. It directly constructs sets of distinct parents and compares their maximum cardinalities with a separately computed matrix-rank expression. Across \(\mathbb F_3\), \(\mathbb F_4\), \(\mathbb F_5\), and \(\mathbb F_7\), it checks \(1{,}574\) nonzero check vectors and \(131{,}395\) received-word cases, including all nonzero checks at the tested lengths through \(4\) except the sampled \(\mathbb F_7\) length-\(4\) setting. It also validates both length-\(4\) examples and the stated small-alphabet boundary. The expected final line is `HYPERPLANE_LIST_VERIFY_OK`; the exact output is in `verification_output.txt`.

These are finite tests. The full domain \(q\ge n\), including arbitrarily large prime powers, is established by the proof and not by enumeration.

## Relationship to prior work

Verma, Hollanti, and Tajeddine derive rate and fixed-list insdel bounds for general linear codes. Their Theorem 7, Corollary 8, and Remark 9, which exhibits a specially patterned binary single-check code, are the closest explicit comparisons. Those statements do not give a coefficient-dependent exact worst-case deletion-list formula for every parity-check hyperplane over \(\mathbb F_q\) when \(q\ge n\). The present finding focuses on that different exact extremal invariant, not on improving their general rate bound.

Cullina and Kiyavash analyze deletion-channel degree counts and asymptotic bounds on sizes of deletion-correcting codes for general alphabets. Their channel counting framework does not identify this hyperplane-constrained inverse-degree maximum. The known unstructured one-insertion-ball cardinality cannot imply the coefficient-sensitive formula for an intersecting linear code on its own.

## Limitations

The theorem concerns one exact deletion and one parity check; it does not determine list sizes for multiple deletions or arbitrary higher-codimension linear codes. The bound \(q\ge n\) is sufficient, not proved necessary for particular check vectors. A small-alphabet counterexample rules out unrestricted extension of this rank expression. Equivalence to a differently phrased result in older synchronization or finite-field coding literature remains a priority risk; independent validation has not been performed.

## References

1. N. Verma, C. Hollanti, and R. Tajeddine, *A Generalized Half-Singleton Bound for List Decoding of Insertion/Deletion Errors*, arXiv:2610.23270v1 (first public submission 2026-10-16). https://arxiv.org/abs/2610.23270
2. D. Cullina and N. Kiyavash, *An Improvement to Levenshtein's Upper Bound on the Cardinality of Deletion Correcting Codes*, arXiv:1302.6562v2 (2013). https://arxiv.org/abs/1302.6562
