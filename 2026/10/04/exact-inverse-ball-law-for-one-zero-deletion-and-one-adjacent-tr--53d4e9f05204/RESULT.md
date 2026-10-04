# Exact inverse-ball law for one zero-deletion and one adjacent transposition
## Finding
For a binary received word \(y\in\{0,1\}^{n-1}\), write its zero-gap representation uniquely as
\[
y=0^{v_0}1\,0^{v_1}1\cdots 1\,0^{v_w},
\]
and put \(m=w+1\), \(p=|\{i:v_i>0\}|\), and \(e\) equal to the number of positive endpoint gaps among \(v_0,v_w\) (counted once when \(m=1\)). Let \(P_n(y)\) be the set of binary length-\(n\) source words that can produce \(y\) by exactly one deletion of a zero and at most one adjacent transposition of unequal bits, with the transposition allowed before or after the deletion. Then
\[
|P_n(y)|=m+(2m-3)p-(m-2)e.
\]
Consequently, for every \(n\ge2\),
\[
\max_y |P_n(y)|=\left\lfloor\frac{n^2}2\right\rfloor-n+2.
\]
For even \(n\ge4\), the unique maximizing received word is \((10)^{n/2-1}1\). For odd \(n\ge5\), the maximizing received words are exactly those that start and end in \(1\), contain no \(00\), and contain exactly one occurrence of \(11\); there are \((n-1)/2\) of them. At \(n=2\), the unique maximizer is \(1\); at \(n=3\), the maximizers are \(01,10,11\).

## Assumptions and scope
The alphabet is binary. A zero-deletion deletes one symbol \(0\). An adjacent transposition exchanges an unequal adjacent pair, so it is either \(01\mapsto10\) or \(10\mapsto01\). The received word has length \(n-1\), so exactly one zero-deletion has occurred; zero or one adjacent transposition may also occur. The statement concerns the uncoded inverse error ball, not the list size of a particular code.

## Proof
Use the standard zero-gap map \(\phi\), which sends a word to its vector \(v=(v_0,\ldots,v_w)\) of zero-run lengths between successive ones and at the two ends. A zero-deletion subtracts one unit from one coordinate. Swapping an unequal adjacent pair moves one zero across one neighboring one, hence transfers one unit between adjacent coordinates of \(v\).

Reverse the channel from a fixed received vector \(v\). Restoring the deleted zero inserts one unit in some coordinate \(j\). If there is no transposition, this gives the \(m\) distinct parents \(v+e_j\).

Now orient a possible transfer from donor coordinate \(a\) to an adjacent coordinate \(b\). If the restored zero is inserted at the donor, the net vector is \(v+e_b\), already counted among the no-transposition parents. For every other insertion coordinate \(j
e a\), the source vector is
\[
v+e_j-e_a+e_b,
\]
and this is feasible exactly when \(v_a>0\). Thus a positive donor contributes \((m-1)\deg(a)\) transfer constructions before duplicate removal.

Different donors cannot collide, because the unique negative coordinate in the increment vector identifies the donor. For an interior donor, its two transfer directions have exactly one collision: inserting at the right neighbor while transferring left and inserting at the left neighbor while transferring right both give increment \(e_{a-1}+e_{a+1}-e_a\). There are no other collisions. Hence
\[
|P_n(y)|=m+(m-1)\sum_{a:v_a>0}\deg(a)-|\{a:v_a>0:\ a\text{ is interior}\}|.
\]
If \(p\) coordinates are positive and \(e\) positive coordinates are endpoints, then
\[
\sum_{a:v_a>0}\deg(a)=2p-e,
\qquad
|\{a:v_a>0:\ a\text{ is interior}\}|=p-e,
\]
which simplifies to the stated pointwise formula.

It remains to maximize it subject to \(\sum_i v_i=n-m\). For fixed \(m\), the formula is maximized by making as many coordinates positive as possible and placing positivity in interior coordinates before endpoints. Thus
\[
p=\min(n-m,m),\qquad e=\max(0,p-(m-2)).
\]
Substitution gives three elementary quadratic regimes. If \(m\le n/2\), the maximum is \(2m^2-4m+4\), increasing with \(m\). In the odd middle case \(m=(n+1)/2\), it is \(2m^2-5m+5\). For \(m\ge\lceil(n+2)/2\rceil\), it is
\[
-2m^2+(2n+4)m-3n,
\]
whose maximum on that regime is attained at its smallest allowed \(m\). Comparing the neighboring regimes yields \(\lfloor n^2/2\rfloor-n+2\). Equality conditions give the stated extremizers: for even \(n\), every interior gap is \(1\) and both endpoint gaps are \(0\); for odd \(n\), exactly one interior gap is \(0\), all other interior gaps are \(1\), and both endpoint gaps are \(0\). The cases \(n=2,3\) are immediate from the pointwise formula.

## Verification
The accompanying verifier implements the channel directly on binary strings, allowing the adjacent swap before or after the zero-deletion, and independently evaluates the zero-gap formula. For every received word through \(n=10\), it checks equality between the directly enumerated inverse ball and the formula, checks the exact worst-case value and all extremizers, and separately optimizes the support-form formula through \(n=200\). The finite checks corroborate the proof; they are not used to infer the universal statement.

## Relationship to prior work
Wang, Vu, and Tan introduced and analyzed codes for the asymmetric Damerau--Levenshtein setting with zero-deletions and adjacent transpositions. Their zero-gap representation records zero-deletions as coordinate decrements and adjacent transpositions as unit transfers, and their later expanded treatment studies list-decodable codes. The exact uncoded inverse degree above is a different invariant: it fixes a received word and counts all length-\(n\) parents.

Ye and Ge later derived forward error-ball lower bounds and asymptotic upper bounds on code size for deletions and asymmetric transpositions. Those forward-ball and code-size results do not determine the exact inverse received-word degree or its extremizers.

## Limitations
The theorem is for binary words, exactly one zero-deletion, and at most one adjacent transposition. It does not give inverse-ball formulas for multiple deletions, multiple transpositions, or nonbinary alphabets. The literature comparison cannot exclude an unindexed, unpublished, or differently phrased prior derivation of the same inverse-ball enumeration.

## References
1. Z. Wang, T. T. N. Vu, and V. Y. F. Tan, “Codes for the Asymmetric Damerau--Levenshtein Distance,” IEEE Information Theory Workshop, 2022, DOI: 10.1109/ITW54588.2022.9965921.
2. Z. Wang, T. T. N. Vu, and V. Y. F. Tan, “Codes for Correcting Asymmetric Adjacent Transpositions and Deletions,” arXiv:2301.11680.
3. C. Ye and G. Ge, “On the Maximum Size of Codes Under the Damerau-Levenshtein Metric,” arXiv:2507.04806.
