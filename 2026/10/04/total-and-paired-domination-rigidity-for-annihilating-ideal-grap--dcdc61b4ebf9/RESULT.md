# Total and paired domination rigidity for annihilating-ideal graphs of products of fields

## Finding

Let \(R\cong\prod_{i=1}^{r}F_i\) be a direct product of \(r\ge2\) fields, and let \(\mathbb{AG}(R)\) be its annihilating-ideal graph. Then \[\gamma_t(\mathbb{AG}(R))=r.\] Moreover, the unique minimum total dominating set is the set of the \(r\) coordinate minimal ideals \(E_i=0\times\cdots\times F_i\times\cdots\times0\). For paired domination, \[\gamma_{\mathrm{pr}}(\mathbb{AG}(R))=\begin{cases}r,&r\text{ even},\\ r+1,&r\text{ odd}.\end{cases}\] If \(r\) is even, the coordinate minimal ideals form the unique minimum paired dominating set. If \(r\) is odd, every minimum paired dominating set consists of all coordinate minimal ideals together with exactly one additional nonzero proper coordinate ideal having support size at least two; hence there are exactly \(2^r-r-2\) minimum paired dominating sets.

Thus the total-domination core is rigid: it is forced to be the family of coordinate minimal ideals. Paired domination adds exactly a parity correction, and in odd rank every minimum paired set is classified.

## Assumptions and scope

Let
\[
R\cong F_1\times\cdots\times F_r,\qquad r\ge2,
\]
where each \(F_i\) is a field. The annihilating-ideal graph \(\mathbb{AG}(R)\) has as vertices the nonzero ideals with nonzero annihilator, with distinct ideals adjacent exactly when their product is zero.

For a nonempty proper subset \(A\subset[r]\), write
\[
I_A=\prod_{i=1}^r J_i,\qquad
J_i=\begin{cases}F_i,&i\in A,\\0,&i\notin A.\end{cases}
\]
Every nonzero proper ideal of \(R\) is uniquely of this form, and
\[
I_A I_B=0\iff A\cap B=\varnothing.\tag{1}
\]
Hence \(\mathbb{AG}(R)\) is the strong Boolean graph on the nonempty proper subsets of \([r]\).

## Proof

For each \(i\in[r]\), let \(C_i=[r]\setminus\{i\}\). By (1), a nonempty proper support \(B\) is disjoint from \(C_i\) if and only if \(B=\{i\}\). Thus \(I_{C_i}\) has the unique neighbor
\[
E_i:=I_{\{i\}}.\tag{2}
\]
Every total dominating set must therefore contain all \(E_i\), so
\[
\gamma_t(\mathbb{AG}(R))\ge r.
\]
The vertices \(E_1,\ldots,E_r\) form a clique. Every nonempty proper support omits some index \(i\), hence is adjacent to \(E_i\). Therefore
\[
D_0=\{E_1,\ldots,E_r\}
\]
is total dominating and
\[
\gamma_t(\mathbb{AG}(R))=r.
\]
The forcing in (2) also makes \(D_0\) the unique minimum total dominating set.

Every paired dominating set is total dominating, because the perfect matching gives each selected vertex a selected neighbor. Hence every paired dominating set contains \(D_0\).

If \(r\) is even, the clique on \(D_0\) has a perfect matching. Thus
\[
\gamma_{\mathrm{pr}}(\mathbb{AG}(R))=r,
\]
and \(D_0\) is the unique minimum paired set.

Suppose \(r\) is odd. A paired dominating set has even size, so its size is at least \(r+1\). Let \(A\subset[r]\) be any nonempty proper subset with \(|A|\ge2\), and choose \(j\notin A\). Then
\[
D_A=D_0\cup\{I_A\}
\]
has size \(r+1\). Match \(I_A\) with \(E_j\); the remaining \(r-1\) singleton vertices form a complete graph of even order, so they can be perfectly matched. Hence \(D_A\) is paired dominating.

Conversely, a minimum paired dominating set in odd rank has size \(r+1\) and already contains all \(r\) singleton supports, so its unique extra vertex must have support size between \(2\) and \(r-1\). There are
\[
(2^r-2)-r=2^r-r-2
\]
such supports, yielding the stated count.

## Verification

The accompanying `verify.py` constructs the support-disjointness graph directly. For \(2\le r\le5\), it checks every co-singleton's unique neighbor, exhaustively enumerates all total dominating sets of size \(r\), and exhaustively enumerates all paired dominating sets at the claimed minimum size.

Exact output:

```text
r=2 vertices=2 total_min_count=1 gamma_t=2 paired_min_count=1 gamma_pr=2
r=3 vertices=6 total_min_count=1 gamma_t=3 paired_min_count=3 gamma_pr=4
r=4 vertices=14 total_min_count=1 gamma_t=4 paired_min_count=1 gamma_pr=4
r=5 vertices=30 total_min_count=1 gamma_t=5 paired_min_count=25 gamma_pr=6
VERIFY_OK
```

These finite checks are corroborative only. The arbitrary-rank theorem follows from the unique-neighbor argument and explicit matching construction above.

## Relationship to prior work

Behboodi and Rakeei introduced the annihilating-ideal graph and established its basic structure. Visweswaran and Parejiya later studied independence-number classifications for the same graph in a source whose primary subject classification is commutative algebra.

Guo, Wu, and Yu identify direct products of fields with the strong-Boolean case of the annihilating-ideal graph under their stated clique hypothesis. A later Boolean-graph survey records standard structural data for strong Boolean graphs, including degree, clique number, diameter, automorphism group, spectra, and algebraic characterizations.

The inspected sources do not state the total-domination forcing phenomenon above, the paired-domination parity formula, or the classification and count of all minimum paired dominating sets. Exact searches using “strong Boolean graph,” “annihilating-ideal graph,” “total domination,” and “paired domination” did not locate a covering theorem.

## Limitations

The theorem concerns direct products of fields, not arbitrary reduced rings. General reduced rings may yield nontrivial blow-ups of strong Boolean graphs, and blow-up multiplicities can change domination parameters.

The graph does not recover the field cardinalities; only the number of direct factors enters this result.

The verification covers small ranks only and does not substitute for the symbolic proof.

## References

1. M. Behboodi and Z. Rakeei, “The Annihilating-Ideal Graph of Commutative Rings I,” arXiv:0808.3187; *Journal of Algebra and Its Applications* 10 (2011), 727–739. DOI: 10.1142/S0219498811004896.
2. S. Visweswaran and J. Parejiya, “Annihilating-ideal graphs with independence number at most four,” *Cogent Mathematics* 3 (2016), Article 1155858. DOI: 10.1080/23311835.2016.1155858.
3. J. Guo, T. Wu, and H. Yu, “On Rings Whose Annihilating-Ideal Graphs Are Blow-Ups of a Class of Boolean Graphs,” *Journal of the Korean Mathematical Society* 54 (2017), 847–865. DOI: 10.4134/JKMS.j160283.
