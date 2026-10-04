# Exact inverse branching for one-symbol duplication with transposition

## Finding
Let \(\Sigma_q\) be an alphabet of size \(q\ge2\). A **one-symbol duplication with transposition** is the specialization of duplication with transposition in which the duplicated block has length one: if \(x=abcd\) and \(|b|=1\), then the channel may output \(y=abcbd\). The copied symbol is inserted somewhere strictly to the right of its original occurrence; the intervening word \(c\) may be empty.

For a received word \(y\in\Sigma_q^{n+1}\), write \(r(y)\) for the number of maximal constant runs. For each symbol that occurs in \(y\), inspect its first run, and let \(s(y)\) be the number of symbols whose first run has length one. If \(P(y)\) denotes the set of distinct length-\(n\) parents of \(y\), then
\[
|P(y)|=r(y)-s(y).
\]
Hence
\[
\max_{y\in\Sigma_q^{n+1}} |P(y)|=
\begin{cases}
1,&n=1,\\
n-1,&n\ge2.
\end{cases}
\]
For every \(n\ge2\), any alternating word on two symbols of length \(n+1\) attains the maximum. For \(n\ge3\), equality holds exactly for two-symbol received words in which every run after the first run of each symbol is a singleton and each of those two first runs has length one or two.

The same local formula gives the global number of distinct parent-child edges from length \(n\) to length \(n+1\):
\[
|E_{q,n}|=q^n\bigl((q-1)n-q(q-2)\bigr)+q(q-2)(q-1)^n.
\]
In particular, for a binary alphabet, \(|E_{2,n}|=n2^n\).

## Assumptions and scope
The duplicated block has **exactly length one**, and there is exactly one duplication-with-transposition operation. Parent multiplicity counts distinct source words, not different operation locations that produce the same source. The alphabet is otherwise arbitrary and no complement, metric, or probabilistic structure is assumed.

## Proof
Fix a received word \(y=y_1\cdots y_{n+1}\). Reversing a one-symbol duplication with transposition means deleting one position \(j\) whose symbol already occurs at some earlier position: deleting \(y_j\) recovers a legal parent exactly when \(y_j=y_i\) for some \(i<j\). Thus a run can contribute a parent unless it is the first run of its symbol and has length one.

It remains to show that each contributing run gives exactly one distinct parent. If positions \(i<j\) are deleted from the same word, the resulting words are equal if and only if
\[
y_i=y_{i+1}=\cdots=y_j.
\]
Indeed, equality of the two deletion results forces equality of the shifted interval \(y_i,y_{i+1},\ldots,y_j\), and the converse is immediate. Therefore all legal deletion positions within one constant run yield the same parent, while positions in different runs yield different parents. This proves \(|P(y)|=r(y)-s(y)\).

For the maximum, let \(d(y)\) be the number of distinct symbols occurring in \(y\), and let \(t(y)\) be the number of symbols whose first run has length at least two. Since \(s(y)=d(y)-t(y)\),
\[
|P(y)|=r(y)-d(y)+t(y).
\]
Every one of the \(t(y)\) long first runs consumes at least one extra character beyond the one character needed for each run, so \(r(y)\le n+1-t(y)\). Hence
\[
|P(y)|\le n+1-d(y).
\]
If \(d(y)\ge2\), this is at most \(n-1\). If \(d(y)=1\), there is only one parent. For \(n\ge2\), an alternating two-symbol word has \(r(y)=n+1\) and \(s(y)=2\), so it has \(n-1\) parents. The equality characterization for \(n\ge3\) follows because equality in the bound requires exactly two used symbols and no excess length except possibly one extra character in each symbol's first run.

For the edge count, sum \(|P(y)|=r(y)-s(y)\) over all \(q^{n+1}\) received words. The total run count is
\[
\sum_y r(y)=q^{n+1}+n(q-1)q^n,
\]
because each word contributes one initial run plus one run boundary at every adjacent unequal pair. For a fixed symbol \(a\), the number of words whose first \(a\)-run is a singleton is
\[
(q-1)q^n-(q-2)(q-1)^n.
\]
This follows by summing over the location of the first \(a\), including the case in which it is the final symbol. Multiplying by \(q\) symbols and subtracting from the total run count simplifies to the displayed formula for \(|E_{q,n}|\).

## Verification
The accompanying `verify.py` independently generates the forward channel, reconstructs inverse parent sets by direct deletion, computes the run statistic, and checks the pointwise formula, maximum, extremizer characterization, and edge count exhaustively for all \(2\le q\le4\) and \(1\le n\le5\). It also checks the alternating sharpness witnesses and closed edge formula on a larger parameter grid. These computations corroborate the proof; they are not used as a substitute for the all-parameter argument.

## Relationship to prior work
Polyanskii and Vorobyev introduced the q-ary duplication-with-transposition graph, the parent/child terminology, roots as vertices of indegree zero, and studied the distance from a word to its root. Their main results concern asymptotic root distance for arbitrary duplicated blocks. The result here instead resolves the complete one-step inverse branching law for the atomic length-one specialization, including the worst-case inverse degree and the total number of distinct graph edges at each length.

Targeted searches under parent, preimage, indegree, one-symbol, run, and edge-count formulations did not locate an inspected source stating or implying the formula above. This negative evidence is not itself a proof of novelty; the residual possibility of an unindexed or differently phrased prior derivation remains.

## Limitations
No claim is made for duplicated blocks of length greater than one, multiple successive duplications, approximate/noisy transposition duplications, code size, or root-distance asymptotics. The equality characterization is stated only for \(n\ge3\); the small cases are covered by the maximum formula but have additional degenerate maximizers.

## References
1. N. Polyanskii and I. Vorobyev, “Duplication with transposition distance to the root for q-ary strings,” arXiv:2001.06242v1, first public version 2020-01-17; later published in the 2020 IEEE International Symposium on Information Theory, DOI 10.1109/ISIT44484.2020.9174324.
