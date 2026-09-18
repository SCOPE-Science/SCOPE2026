# Output-sensitive implementation of the q-ary three-length fix-free construction

## Result

Let \(q\ge 2\), let
\[
\lambda_1<\lambda_2<\lambda_3,\qquad \mu_1,\mu_2,\mu_3>0,
\]
and suppose
\[
\sum_{i=1}^3 \mu_i q^{-\lambda_i}\le \frac34.
\]
Write \(N_i=q^{\lambda_i}\). Gao and Shan proved that such data admit a deterministic \(q\)-ary fix-free code, and their direct implementation bound is
\[
O(N_2^2+N_3\lambda_3)
\]
operations in a unit-cost word-index convention.

The same construction can be implemented in
\[
\boxed{O(N_2\log N_2+\mu_3\lambda_3)}
\]
operations, with the same asymptotic working storage
\[
O(N_2+q^\beta+\mu_3)
\]
words in the overlap case
\[
\beta=2\lambda_2-\lambda_3>0.
\]
Thus the quadratic middle-layer scan and the exhaustive \(N_3\)-word final scan are both unnecessary. The final term is output-sensitive: it is proportional to the number of longest codewords actually requested, rather than to all \(q^{\lambda_3}\) possible longest words.

Two independent structural observations give the improvement.

## 1. Near-linear greedy interpolation

The fixed-cardinality interpolation theorem of Gao--Shan associates to each candidate \(x\) two indices \(i(x),j(x)\) and, for a current selected set \(S\), uses the increment
\[
\delta_S(x)
=(C_Se)_{j(x)}-(A_S^Te)_{i(x)}
-\mathbf 1_{\{i(x)=j(x)\}}.
\]
Let
\[
r_\ell(S)=|\{x\in S:i(x)=\ell\}|,\qquad
c_\ell(S)=|\{x\in S:j(x)=\ell\}|.
\]
Relative to the initial endpoint \(S=\varnothing\),
\[
\delta_S(x)
=b_x-r_{j(x)}(S)-c_{i(x)}(S),
\tag{1}
\]
where
\[
b_x=(C_0e)_{j(x)}-(A_0^Te)_{i(x)}
-\mathbf 1_{\{i(x)=j(x)\}}.
\]

Each greedy choice \(x=(i,j)\) therefore has only two effects on the remaining keys:

* every remaining candidate \(y\) with \(i(y)=j\) decreases by one;
* every remaining candidate \(y\) with \(j(y)=i\) decreases by one.

Gao--Shan's interpolation theorem assumes one of two one-sided uniqueness conditions. Under their condition \((U_c)\), for every label that occurs on both sides there is at most one candidate with that \(j\)-label. Partition the candidates into groups
\[
G_a=\{x:i(x)=a\}.
\]
The first update above is a uniform lazy decrement of the whole group \(G_j\). The second update affects at most one remaining candidate, by \((U_c)\). Maintain a binary heap inside every nonempty group and a second binary heap containing the current minimum of every group. A uniform group decrement updates one global key; the possible point decrement updates one local key; deleting the selected candidate updates one local minimum. Hence each greedy choice costs \(O(\log |D|)\), where \(D\) is the current interpolation packet.

Under \((U_r)\) the symmetric construction partitions by \(j\)-labels: one update is uniform on a group and the other affects at most one candidate. Therefore:

**Interpolation implementation lemma.**  
For every instance covered by the Gao--Shan fixed-cardinality interpolation theorem, its greedy chain on a packet \(D\) can be generated in
\[
O(|D|\log |D|)
\]
time and \(O(|D|)\) additional storage. If only the first \(m\) choices are required, the bound is \(O(|D|+m\log |D|)\).

The proof uses only the exact increment formula (1) and the one-sided uniqueness hypothesis already required for correctness of the interpolation theorem; it does not strengthen the coding-theoretic assumptions.

## 2. Direct generation of the longest layer

After the first two layers \(F=F_1\cup F_2\) have been selected, put \(r=\lambda_2\) and define
\[
P=X^r\setminus P_r(F),\qquad
S=X^r\setminus S_r(F),
\]
where \(P_r(F)\) and \(S_r(F)\) are the length-\(r\) prefix and suffix shadows. A length-\(\lambda_3\) word is admissible exactly when its first \(r\) symbols lie in \(P\) and its last \(r\) symbols lie in \(S\).

### Nonoverlap case: \(\lambda_3\ge 2r\)

Every admissible word is uniquely
\[
u z v,\qquad
u\in P,\quad
v\in S,\quad
z\in X^{\lambda_3-2r}.
\]
Consequently the admissible words can be generated directly from this Cartesian product and enumeration can stop after \(\mu_3\) outputs.

### Overlap case: \(r<\lambda_3<2r\)

Put
\[
\beta=2r-\lambda_3.
\]
For each \(a\in X^\beta\), form
\[
P_a=\{u\in P:\operatorname{suff}_\beta(u)=a\},
\qquad
S_a=\{v\in S:\operatorname{pref}_\beta(v)=a\}.
\]
Then the admissible longest words are in bijection with
\[
\bigsqcup_{a\in X^\beta} P_a\times S_a.
\tag{2}
\]
Indeed, a pair \((u,v)\) with the common \(\beta\)-symbol overlap determines exactly one length-\(\lambda_3\) word, and every admissible word gives exactly one such pair.

For the Gao--Shan construction, \(F_1\) is the natural-order initial interval at length \(\lambda_1\), while \(F_2\) consists entirely of length-\(\lambda_2\) words. With a bit vector for \(F_2\), membership in \(P\) and \(S\) is tested in constant time from the length-\(\lambda_1\) prefix/suffix index and the length-\(\lambda_2\) word index. Thus all lists in (2) are built by one pass over \(X^{\lambda_2}\), using \(O(N_2+q^\beta)\) storage. Traversing the Cartesian products stops immediately after \(\mu_3\) words have been produced. Writing those words explicitly costs \(O(\mu_3\lambda_3)\), which is unavoidable up to constants for symbol-by-symbol output.

## Complexity consequence

In the overlap regimes, the only quadratic term in the direct implementation described by Gao--Shan comes from rescanning a remaining interpolation packet to minimize the current increment at every greedy step. The grouped priority structure above replaces this by \(O(N_2\log N_2)\) worst-case work. The direct longest-layer generator replaces the exhaustive \(O(N_3\lambda_3)\) scan by \(O(N_2+\mu_3\lambda_3)\).

The reverse-order middle-layer regimes and the nonoverlap regime require no more work than this bound. Hence, in the same unit-cost numerical-index convention,
\[
\boxed{
T=O(N_2\log N_2+\mu_3\lambda_3).
}
\]
If codewords are kept only as numerical indices, the explicit-output term can be written \(O(\mu_3)\); the displayed bound charges for materializing all \(\lambda_3\) symbols.

## Verification

The accompanying script checks two independent parts of the argument:

1. structured one-sided-uniqueness updates against naïve recomputation of all greedy increments on deterministic finite test families; and
2. the direct overlap/nonoverlap longest-layer enumeration against exhaustive enumeration on small binary and ternary fix-free examples.

These finite checks support the implementation identities; the general complexity statement follows from the proofs above.

## Scientific scope and limitations

This result improves the implementation complexity of the Gao--Shan deterministic three-length construction. It does not prove the \(3/4\) conjecture for four or more lengths, does not improve the \(3/4\) Kraft threshold, and does not claim a lower bound showing that \(O(N_2\log N_2)\) is necessary for producing only one prescribed middle-layer cardinality.

The priority-queue idea is a standard data-structural technique. The substantive claim is the structural observation that Gao--Shan's one-sided uniqueness hypothesis makes every greedy score update a combination of one group-wide lazy decrement and at most one point decrement, together with the output-sensitive shadow-product enumeration of the final layer.

## References

1. W. Gao and Z. Shan, *The 3/4 Conjecture for q-Ary Fix-Free Codes With at Most Three Distinct Codeword Lengths*, arXiv:2609.18237, 2026. https://arxiv.org/abs/2609.18237
2. S. Congero and K. Zeger, *The 3/4 Conjecture for Fix-Free Codes With at Most Three Distinct Codeword Lengths*, IEEE Transactions on Information Theory 69(3), 1452--1485, 2023. DOI: 10.1109/TIT.2022.3218212.
