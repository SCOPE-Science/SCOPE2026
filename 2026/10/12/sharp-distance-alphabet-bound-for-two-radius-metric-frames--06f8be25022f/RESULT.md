# Sharp distance-alphabet bound for two-radius metric frames

## Finding

For two thresholds \(0<a<b\), put \(k=\lfloor b/a\rfloor\) and let \(A,B\) be the putative open-ball relations at radii \(a,b\) on an arbitrary nonempty set \(W\). A representing metric on \(W\) exists if and only if both relations are reflexive and symmetric, \(A\subseteq B\), and \(A^k\subseteq B\). The latter condition means that a chain of \(k\) successive \(A\)-steps has its endpoints related by \(B\).

Among all such realizations, there is always one with no more than

\[
L(a,b)=\max\{3,\lfloor b/a\rfloor+1\}
\]

distinct **positive** distance values. The bound is universally sharp for every ratio \(b/a>1\), irrespective of the number of worlds. The threshold characterization alone is part of established metric-frame representation theory; the asserted new result is the sharp, cardinality-independent distance-alphabet bound and its obstruction examples.

## Assumptions and scope

All distances are ordinary finite nonnegative real numbers, obeying symmetry, identity of indiscernibles, and the triangle inequality. The inequalities in the two relational definitions are strict: \(d(x,y)<a\) and \(d(x,y)<b\). The set \(W\) can be finite or infinite. The integer \(k\) is at least one; in particular \(b=ka\) is allowed. Diagonal pairs are always present in the two relations. Composition \(A^k\) means exactly \(k\) compositional factors, with loops available to pad shorter chains. "Distance levels" counts positive values in the range of \(d\), not zero and not the number of edges.

## Proof

**Necessity of representability conditions.** Every open metric ball relation is reflexive and symmetric, and increasing radius gives \(A\subseteq B\). For any \(k\) successive \(A\)-steps, the triangle inequality makes the endpoint distance strictly smaller than \(ka\), which is at most \(b\); hence \(A^k\subseteq B\).

**Upper bound when \(k=1\).** Then \(a<b<2a\). Choose \(r\) strictly between \(b/2\) and \(a\), and \(s\) strictly between \(a\) and \(b\). Assign distance zero on the diagonal; for distinct vertices assign \(r\) to pairs in \(A\), \(s\) to pairs in \(B\setminus A\), and \(b\) to pairs outside \(B\). This assignment is symmetric and positive. Every nonzero distance is at least \(r\), whereas the largest is \(b<2r\), so *all* triangle inequalities hold. The prescribed strict thresholds are exact. At most the three positive numbers \(r,s,b\) are used.

**Upper bound when \(k\ge2\).** Choose \(r\) satisfying

\[
\max\{a/2,b/(k+1)\}<r<a.
\]

Such an \(r\) exists because \(ka\le b<(k+1)a\). In the complete undirected graph on \(W\), give each edge between distinct vertices the cost \(r\) if it belongs to \(A\), the cost \(kr\) if it belongs to \(B\setminus A\), and the cost \(b\) otherwise. Let \(d\) be the infimum of costs of finite paths between endpoints. Because all edge costs are at least \(r>0\), a direct edge exists with cost at most \(b\), and only finitely many distinct sums of these three positive edge costs lie at most \(b\), the infimum is attained, even when \(W\) is infinite. Thus \(d\) is a genuine metric.

The inequalities \(2r>a\), \(kr<b\) and \((k+1)r>b\) control shortcuts. A pair in \(A\) has distance exactly \(r\). A distinct pair in \(B\setminus A\) has a direct route of cost \(kr\); any cheaper path must use only \(A\)-edges, and must contain between \(2\) and \(k\) such edges. Therefore its distance belongs to \(\{2r,\ldots,kr\}\) and is strictly between \(a\) and \(b\). For a pair outside \(B\), an \(A\)-only route cannot use at most \(k\) edges (by \(A^k\subseteq B\)); any route using a \(B\setminus A\) edge plus another positive-cost edge costs at least \((k+1)r>b\); a route using an outside-\(B\) edge cannot beat \(b\). Hence this pair has distance exactly \(b\). The complete list of possible positive distances is contained in \(\{r,2r,\ldots,kr,b\}\), of size \(k+1\), with exact threshold relations.

**Sharpness when \(k=1\).** On three points take \(A\) to consist of the diagonal and just one off-diagonal unordered edge, and take \(B\) to additionally contain just one of the other two unordered edges. The remaining pair is outside \(B\). Every representing metric must give the three pairs distances in the disjoint ranges \((0,a)\), \([a,b)\), and \([b,\infty)\), respectively. Thus three positive distance values are unavoidable. The construction above realizes this example.

**Sharpness when \(k\ge2\).** Take \(W=\{x_0,\ldots,x_{k+1}\}\) with \(A\) the reflexive adjacency relation of the path in this order and \(B=A^k\). It is a realizable pair by the upper construction. For any representing metric, each consecutive edge has length strictly below \(a\), while \(d(x_0,x_{k+1})\ge b\ge ka\) because these endpoints are not \(B\)-related. For every \(1\le i\le k\), the direct prefix path gives \(d(x_0,x_i)<ia\), and the reverse triangle inequality via the terminal suffix gives

\[
d(x_0,x_i)>b-(k+1-i)a\ge(i-1)a.
\]

Thus the distances \(d(x_0,x_i)\) for \(i=1,\ldots,k\) occupy \(k\) pairwise disjoint open intervals \(((i-1)a,ia)\). The additional terminal distance \(d(x_0,x_{k+1})\ge b\ge ka\) is different from all of them. Hence every representation uses at least \(k+1\) distinct positive values. Together with the constructions, this proves the sharp universal formula.

## Verification

The accompanying standalone `reproduce.py` enumerates all symmetric, reflexive nested pairs on at most four labelled vertices satisfying \(A^k\subseteq B\) for nine threshold ratios; these comprise 5,042 admissible instances. The checker independently constructs and tests all metric triangles, both strict threshold relations and the distance-alphabet bound, using finite shortest paths. It also checks the proposed path witnesses for \(2\le k\le9\) and the three-point witness for \(k=1\). Run `python3 reproduce.py` using Python 3 standard library only. The computational experiment is finite and does not replace the general proof, including the infinite-carrier case.

## Relationship to prior work

Harding and Shapirovsky (2026), Lemma 4.2 and its appendix, and Kutz (2007), Theorem 4.4, establish broader qualitative metric-frame representability under suitable relational axioms. The two-radius representability criterion follows from these ideas and is expressly **not** asserted as novel. The contribution here is the exact optimum on the number of distinct positive distances needed simultaneously to represent both strict radius relations, uniformly in carrier cardinality, together with sharp path examples. The relevant full-text representation arguments inspected do not state this optimum. Exhaustive bibliographic coverage is not claimed.

## Limitations

The bound is for *two* strict radius modalities and unrestricted real metrics, not for three or more thresholds, prescribed topology, Euclidean embedding, ultrametrics, integer metrics, or fixing a pre-existing metric. It is a universal maximum of the minimum possible alphabet size; individual frames can require fewer distances. This is a self-review, not independent validation. Earlier equivalent quantitative formulations under different terminology remain a plausible originality risk.

## References

1. J. Harding and I. Shapirovsky, *On Modal Logics of Connectedness in Metric Spaces* (2026), arXiv:2606.31880, DOI: 10.4204/EPTCS.447.27, especially Lemma 4.2 and Appendix.
2. O. Kutz, *Notes on Logics of Metric Spaces*, Studia Logica 85 (2007), 75–104, DOI: 10.1007/s11225-007-9023-3, especially Theorem 4.4.
3. O. Kutz, F. Wolter, H. Sturm, N.-Y. Suzuki, M. Zakharyaschev, *Logics of Metric Spaces*, ACM Transactions on Computational Logic 4 (2003), 260–294, DOI: 10.1145/635499.635504.
