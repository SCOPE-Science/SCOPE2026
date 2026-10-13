# Zero forcing polynomial and minimum rank of generalized-quaternion cyclic graphs

## Finding

Let \(Q_{4n}=\langle a,b\mid a^{2n}=1,\ b^2=a^n,\ bab^{-1}=a^{-1}\rangle\) with \(n\ge2\), and let \(\Gamma(Q_{4n})\) be the full cyclic graph on all \(4n\) elements, where distinct vertices are adjacent exactly when they generate a cyclic subgroup. Then \(\Gamma(Q_{4n})\cong K_2\vee(K_{2n-2}\dot\cup nK_2)\) and \[\mathcal Z(\Gamma(Q_{4n});u)=u^{3n-2}\left((u+2)^{n+1}(u+2n-2)-2^{n+1}(2n-2)\right).\] Consequently \(Z(\Gamma(Q_{4n}))=M(\Gamma(Q_{4n}))=3n-1\) and \(\operatorname{mr}(\Gamma(Q_{4n}))=n+1\) over real symmetric graph-pattern matrices. The minimum zero forcing sets are exactly the complements of a transversal choosing one vertex from every one of the \(n+2\) canonical clique classes except one, so there are \(2^{n+1}n^2\) minimum sets.

## Assumptions and scope

The full cyclic graph \(\Gamma(G)\) has vertex set \(G\), with distinct \(x,y\) adjacent exactly when \(\langle x,y\rangle\) is cyclic. For zero forcing, \(\mathcal Z(G;u)=\sum_k z(G;k)u^k\). Real symmetric maximum nullity and minimum rank are denoted \(M(G)\) and \(\operatorname{mr}(G)\).

## Proof

Ma, Wei, and Zhong prove for the generalized quaternion presentation above that
\[
\operatorname{Cyc}(Q_{4n})=\{1,a^n\}.
\]
These two vertices are universal in the full cyclic graph. The remaining \(2n-2\) rotations form a clique. The \(2n\) elements outside \(\langle a\rangle\) split into \(n\) inverse pairs \(\{a^ib,a^{i+n}b\}\), each inducing \(K_2\), with no other cyclic adjacencies. Hence
\[
\Gamma(Q_{4n})\cong K_2\vee(K_{2n-2}\dot\cup nK_2).
\]

This gives \(n+2\) true-twin clique classes: one universal class of size \(2\), one rotation class of size \(2n-2\), and \(n\) classes of size \(2\). A zero forcing set cannot leave two white vertices in one true-twin class.

Conversely, suppose at most one vertex per class is white. If the universal class is fully blue, any peripheral class containing a white vertex can force that vertex from a blue mate. If the universal class has one white vertex and some peripheral class is fully blue, a blue vertex in that peripheral class first forces the universal white vertex; all remaining peripheral whites then force. The unique stalled type profile therefore has one white representative in every class.

A clique class of size \(w\) contributes
\[
u^w+w u^{w-1}=u^{w-1}(u+w)
\]
to the at-most-one-white product. Subtracting the unique stalled all-class profile yields
\[
\mathcal Z(\Gamma(Q_{4n});u)
=
u^{3n-2}\left((u+2)^{n+1}(u+2n-2)-2^{n+1}(2n-2)\right).
\]
The constant term inside the parentheses cancels and the linear coefficient is \(2^{n+1}n^2\), giving
\[
Z=3n-1.
\]
A minimum set leaves \(n+1\) white vertices, exactly one in every class except one, proving the stated classification and count.

For minimum rank, use \(\mathbb R^{n+1}\) with basis \(e_0,\ldots,e_n\). Assign \(e_0\) to the rotation class, \(e_i\) to the \(i\)-th outside pair, and \(e_0+\cdots+e_n\) to both universal vertices. The Gram matrix has exactly the required off-diagonal pattern and rank \(n+1\). Thus \(\operatorname{mr}\le n+1\). Since \(M(G)\le Z(G)\),
\[
\operatorname{mr}=4n-M\ge4n-Z=n+1,
\]
so equality holds and \(M=Z=3n-1\).

## Verification

The accompanying `verify.py` constructs \(Q_{4n}\) directly from its multiplication law. It generates \(\langle x,y\rangle\) for each tested pair and independently tests whether that subgroup is cyclic. For \(n=2,3,4,5\), the direct graph is checked edge-for-edge against the stated decomposition. For \(n=2,3,4\), every vertex subset is exhaustively tested and the complete polynomial is reproduced. The Gram witness is checked entry-by-entry and row-reduced exactly over the rationals. For every \(2\le n\le10\), all type profiles with at most one white representative per class are tested, with exactly the all-class profile failing.

Exact replay output:

```text
Q_8: N=8, Z=5, min_sets=32, polynomial={5: 32, 6: 24, 7: 8, 8: 1}, witness_rank=3
Q_12: N=12, Z=8, min_sets=144, polynomial={8: 144, 9: 128, 10: 56, 11: 12, 12: 1}, witness_rank=4
Q_16: N=16, Z=11, min_sets=512, polynomial={11: 512, 12: 560, 13: 320, 14: 100, 15: 16, 16: 1}, witness_rank=5
Q_20: N=20, predicted_Z=14, min_sets=1600, witness_rank=6
PROFILE_CLASSIFICATION_OK
VERIFY_OK
```

The finite checks corroborate but do not replace the symbolic proof.

## Relationship to prior work

Abdollahi and Mohammadi Hassanabadi introduced the cyclicizer/noncyclic-graph framework; their article lists Primary MSC \(20D60\). Ma, Wei, and Zhong introduced the full cyclic graph and in Section 5 determine the generalized-quaternion cyclicizer and neighborhoods used above. They study degree, planarity, Eulerian, and Hamiltonian properties rather than zero forcing or graph minimum rank.

Boyer and collaborators introduced the zero forcing polynomial and its general counting framework. Targeted searches under cyclic graph, generalized quaternion, dicyclic, zero forcing, zero forcing polynomial, maximum nullity, and minimum rank did not locate the polynomial, minimum-set classification, or rank formula above.

## Limitations

The theorem is for the full cyclic graph on all elements of \(Q_{4n}\), not the deleted cyclic graph and not the complementary noncyclic graph. The graph decomposition itself is prior work. No extension to arbitrary generalized dicyclic groups with noncyclic abelian kernel is asserted. Minimum rank is over real symmetric graph-pattern matrices.

## References

1. A. Abdollahi and A. Mohammadi Hassanabadi, “Noncyclic Graph of a Group,” *Communications in Algebra* 35 (2007), 2057–2081. DOI: 10.1080/00927870701302081. Published online 11 June 2007.
2. X. L. Ma, H. Q. Wei, and G. Zhong, “The Cyclic Graph of a Finite Group,” *Algebra* 2013, Article 107265. DOI: 10.1155/2013/107265. First published 16 April 2013.
3. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” arXiv:1801.08910; *Discrete Applied Mathematics* 258 (2019), 35–48.
4. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
