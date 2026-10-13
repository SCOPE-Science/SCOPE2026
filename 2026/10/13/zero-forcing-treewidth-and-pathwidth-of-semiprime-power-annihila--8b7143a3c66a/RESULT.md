# Zero forcing, treewidth, and pathwidth of semiprime-power annihilating-ideal graphs

## Finding

Let \(p\ne q\) be primes and \(a\ge2\). For the annihilating-ideal graph \(G=\operatorname{AG}(\mathbb Z/(p^a q)\mathbb Z)\), one has \[Z(G)=\operatorname{tw}(G)=\operatorname{pw}(G)=a-1.\] A minimum zero forcing set is the family of ideals \((p),(p^2),\ldots,(p^{a-1})\). Moreover, the \(a\) disjoint connected branch sets \(\{(p^i),(p^{a-i}q)\}\), for \(1\le i\le a\), form a \(K_a\)-minor certificate, so the lower bound is structural rather than computational. For the boundary \(a=1\), \(\operatorname{AG}(\mathbb Z/(pq)\mathbb Z)=K_2\) and all three parameters equal \(1\).

Thus the exponent of the repeated prime is recovered exactly from any one of the three graph parameters:
\[
a=Z(G)+1=\operatorname{tw}(G)+1=\operatorname{pw}(G)+1
\]
for \(a\ge2\).

## Assumptions and scope

Let \(p\ne q\) be primes and let
\[
R=\mathbb Z/(p^a q)\mathbb Z,
\qquad a\ge2.
\]
The annihilating-ideal graph \(\operatorname{AG}(R)\) has as vertices the nonzero annihilating ideals, with distinct ideals adjacent exactly when their product is zero. Because \(R\) is Artinian, every nonzero proper ideal is a vertex. For \(1\le i\le a\) and \(0\le j\le a-1\), write
\[
A_i=(p^i),\qquad B_j=(p^j q).
\]
These are exactly the \(2a\) nonzero proper ideals.

## Proof

In \(\mathbb Z/(p^a q)\mathbb Z\), an ideal is represented by a divisor of \(p^a q\), and
\[
(d)(e)=(0)\quad\Longleftrightarrow\quad p^a q\mid de.
\]
Therefore
\[
A_iA_k\ne(0),
\]
\[
A_iB_j=(0)\quad\Longleftrightarrow\quad i+j\ge a,
\]
and
\[
B_jB_k=(0)\quad\Longleftrightarrow\quad j+k\ge a.
\tag{1}
\]

Consider
\[
S=\{A_1,A_2,\ldots,A_{a-1}\}.
\]
Starting with \(S\) blue, \(A_1\) has exactly one white neighbor, namely \(B_{a-1}\). Continuing gives
\[
A_i\longrightarrow B_{a-i}\qquad(1\le i\le a-1).
\tag{2}
\]
After these forces all \(B_1,\ldots,B_{a-1}\) are blue. The blue vertex \(B_1\) then has exactly one white neighbor, \(A_a\), and after \(B_1\longrightarrow A_a\), the vertex \(A_a\) has exactly one remaining white neighbor, \(B_0\). Hence \(S\) is zero forcing and
\[
Z(G)\le a-1.
\tag{3}
\]

For the lower bound, define
\[
C_i=\{A_i,B_{a-i}\},\qquad1\le i\le a.
\]
Each \(C_i\) is connected. The branch sets are pairwise disjoint. If \(i<j\), then
\[
j+(a-i)\ge a,
\]
so \(A_j\) is adjacent to \(B_{a-i}\). Thus every pair of branch sets is adjacent, and contracting them gives a \(K_a\)-minor. Therefore
\[
\operatorname{tw}(G)\ge a-1.
\tag{4}
\]

For every graph,
\[
\operatorname{tw}(G)\le\operatorname{pw}(G)\le Z(G).
\tag{5}
\]
Combining (3), (4), and (5) gives
\[
Z(G)=\operatorname{tw}(G)=\operatorname{pw}(G)=a-1.
\]

When \(a=1\), the only nonzero proper ideals are \((p)\) and \((q)\), whose product is zero. Thus the graph is \(K_2\), and all three parameters equal \(1\).

## Verification

The accompanying `verify.py` was read from its packaged path before replay. For every \(2\le a\le30\), it checks the chronological forcing sequence (2) and all pairwise adjacencies of the \(a\) explicit branch sets in the \(K_a\)-minor certificate. For \(2\le a\le8\), it exhaustively enumerates every vertex subset until the exact zero forcing number is reached and obtains \(a-1\) in every case.

It also constructs the annihilating-ideal graph directly from divisor ideals and ideal-product divisibility for \(\mathbb Z/12\mathbb Z\), \(\mathbb Z/80\mathbb Z\), \(\mathbb Z/1215\mathbb Z\), and \(\mathbb Z/875\mathbb Z\), and verifies complete agreement with the abstract adjacency rules.

Exact replay output:

```text
symbolic forcing and K_a-minor certificates: a=2..30 OK
a=2: exact Z=1, minimum_sets=2
a=3: exact Z=2, minimum_sets=6
a=4: exact Z=3, minimum_sets=23
a=5: exact Z=4, minimum_sets=63
a=6: exact Z=5, minimum_sets=207
a=7: exact Z=6, minimum_sets=559
a=8: exact Z=7, minimum_sets=1774
Z/12Z: direct ideal-product graph has 4 vertices and matches the abstract graph
Z/80Z: direct ideal-product graph has 8 vertices and matches the abstract graph
Z/1215Z: direct ideal-product graph has 10 vertices and matches the abstract graph
Z/875Z: direct ideal-product graph has 6 vertices and matches the abstract graph
a=1 boundary: K2 with Z=1
VERIFY_OK
```

The finite checks corroborate the proof; the arbitrary-\(a\) result rests on the symbolic forcing sequence and complete-minor certificate.

## Relationship to prior work

Behboodi and Rakeei introduced the annihilating-ideal graph and proved that for Artinian rings every nonzero proper ideal is a vertex. Their paper lists \(13A15\) first in its Mathematics Subject Classification.

Nikandish, Maimani, and Izanloo study \(\operatorname{AG}(\mathbb Z_n)\) directly, including the divisor-ideal description, vertex counts, and weak perfectness. The inspected full text contains no occurrences of “zero forcing,” “treewidth,” or “pathwidth.”

Barioli and coauthors establish general relationships among treewidth, pathwidth, and zero forcing. Those inequalities are prior background; the new content here is the semiprime-power ideal decomposition together with the explicit minimum forcing process and matching \(K_a\)-minor certificate.

Targeted searches under annihilating-ideal, divisor-ideal, zero-forcing, treewidth, pathwidth, and semiprime-power formulations did not locate this exact equality.

## Limitations

The theorem concerns the standard annihilating-ideal graph and moduli with exactly two distinct prime divisors, one occurring to exponent \(a\) and the other to exponent \(1\). It does not classify all minimum zero forcing sets. No minimum-rank or maximum-nullity equality is claimed. The graph depends on \(a\), but not on the numerical values of \(p\) and \(q\).

## References

1. M. Behboodi and Z. Rakeei, “The Annihilating-Ideal Graph of Commutative Rings I,” arXiv:0808.3187, first submitted 23 August 2008.
2. R. Nikandish, H. R. Maimani, and H. Izanloo, “The annihilating-ideal graph of \(\mathbb Z_n\) is weakly perfect,” *Contributions to Discrete Mathematics* 11 (2016), 16–21. DOI: 10.11575/cdm.v11i1.62406.
3. F. Barioli, W. Barrett, S. M. Fallat, H. T. Hall, L. Hogben, B. Shader, P. van den Driessche, and H. van der Holst, “Parameters Related to Tree-Width, Zero Forcing, and Maximum Nullity of a Graph,” *Journal of Graph Theory* 72 (2013), 146–177. DOI: 10.1002/jgt.21637.
4. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
