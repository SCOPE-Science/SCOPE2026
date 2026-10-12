# A disjoint-repair availability dichotomy for binary closed-cube systematic codes

## Finding

For each integer \(r\ge2\), let \(d=r-1\), \(N=2^d\), and index coordinates of \(\mathbb F_2^N\) by the vertices of the binary cube \(Q_d\). Set \(S=I+A(Q_d)\) over \(\mathbb F_2\), and define the systematic code
\[
C_r=\{(x,Sx):x\in\mathbb F_2^N\}\subset\mathbb F_2^{2N}.
\]
Write \(x_v\) for a systematic coordinate and \(y_v\) for a parity coordinate. Let \(a(z)\) be the largest possible number of pairwise disjoint **linear recovery helper sets** for coordinate \(z\), with no restriction on the sizes of the sets; an associated recovery equality must hold for every codeword.

**Theorem.** For every \(r\ge2\) and every cube vertex \(v\),
\[
a(x_v)=1,\qquad
\begin{cases}
a(y_v)=1,&r\text{ odd},\\
2\le a(y_v)\le1+2^{r-3},&r\ge4\text{ even},\\
a(y_v)=2,&r=2.
\end{cases}
\]
The bound for even \(r\ge4\) is sharp at \(r=4\), when \(a(y_v)=3\) for every \(v\). Thus parity coordinates have more than one disjoint recovery route exactly for even \(r\), while systematic coordinates never do. At the first three sizes, \(r=2,3,4\), the localities \((\operatorname{loc}(x_v),\operatorname{loc}(y_v))\) are respectively \((2,1),(3,3),(4,3)\); these are exact finite assertions.

## Assumptions and scope

The binary cube has an edge between words differing in exactly one bit. The matrix \(S\) has a 1 on the diagonal and on each cube edge, and no other nonzero entries. The code is binary and the displayed systematic coordinate split is fixed; arbitrary code equivalences need not preserve that split. A helper set for \(z\) is a subset of the other \(2N-1\) coordinates from which \(z\) can be recovered as a binary linear combination for every codeword. Its cardinality is its repair size, and locality is the smallest repair size. Availability counts disjoint helper sets regardless of size and is finite. Every recovery set corresponds to a dual word containing the target; replacing it by the support of that dual word minus the target does not create intersections. Conversely every dual word gives a linear recovery set. No claims about non-linear repair costs, simultaneous erasures beyond these disjoint sets, or availability of larger even parameters are made.

## Proof

Set \(B=A(Q_d)\) and write \(B=\sum_{i=1}^d T_i\), where \(T_i\) flips cube coordinate \(i\). The \(T_i\) commute and \(T_i^2=I\). In characteristic two, \(B^2=dI\), whence
\[
S^2=(d+1\bmod2)I.
\]
The recursive matrix used in the originating construction has blocks \(S_1=\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)\) and \(S_d=\bigl(\begin{smallmatrix}I&S_{d-1}\\S_{d-1}&I\end{smallmatrix}\bigr)\). Its off-diagonal graph connects \((a,v)\) to \((1-a,v)\) and to \((1-a,v+b)\) for the \(d-1\) independent cube directions \(b\) of the previous graph. The \(d\) vectors \((1,0)\) and \((1,b)\) are linearly independent, so this graph is a hypercube under a linear vertex relabeling. Consequently the recursive matrix is simultaneously row-and-column permutation-conjugate to \(I+A(Q_d)\), and the displayed code is equivalent under separate synchronized coordinate permutations to the originating systematic construction, preserving information/parity classes and their repair invariants.

The dual code is precisely \(C_r^\perp=\{(St,t):t\in\mathbb F_2^N\}\), since \(S\) is symmetric. A repair equality is therefore indexed by a unique \(t\), and its helper support is the support of \((St,t)\) without the target.

If \(r\) is odd, then \(S^2=I\). Two dual words are orthogonal: \((St,t)\cdot(Su,u)=t\cdot(S^2+I)u=0\). Were two target-containing dual words to give disjoint helper sets, their supports would meet only at the target and their dot product would be 1, a contradiction. Every coordinate lies in some check \((Se_v,e_v)\), using the diagonal entry \(S_{vv}=1\); thus the availability is exactly one for both coordinate types.

If \(r\) is even, then \(S^2=0\). For a fixed systematic target \(x_v\), two disjoint recovery sets require their parity supports \(\operatorname{supp}(t)\), \(\operatorname{supp}(u)\) to be disjoint. Their systematic supports would intersect exactly in \(v\). But \((St)\cdot(Su)=t\cdot S^2u=0\), contradicting that single intersection. The check \((Se_v,e_v)\) contains \(x_v\), so \(a(x_v)=1\).

For a parity target \(y_v\), take \(t=e_v\) and \(u=Se_v\). Since \(S^2=0\), their check vectors are \((Se_v,e_v)\) and \((0,Se_v)\). Both contain \(y_v\), because \(S_{vv}=1\); their helper sets are disjoint, since the first has only systematic helpers and the second only parity helpers. Thus \(a(y_v)\ge2\).

For the upper bound, first note that when \(d\) is odd, \(S^2=0\) and \(\ker S=\operatorname{im}S\). Indeed, the block recursion \(S_d=\bigl(\begin{smallmatrix}I&S_{d-1}\\S_{d-1}&I\end{smallmatrix}\bigr)\) has rank at least \(N/2\), while nilpotence bounds it above by \(N/2\). Moreover \(\operatorname{im}S\) is self-orthogonal: \((St)\cdot(Su)=0\). Its nonzero words have even weight. For \(d\ge3\), distinct vertices of \(Q_d\) have distinct closed neighborhoods, so the columns of \(S\) are distinct; hence a word of weight two cannot lie in \(\ker S\). Consequently every nonzero word in \(\operatorname{im}S\) has weight at least four.

Suppose \(k\) checks \((St_i,t_i)\) contain \(y_v\) and have pairwise disjoint helper supports. Their parity supports pairwise intersect exactly in \(v\), so \(t_i\cdot t_j=1\) for \(i\ne j\). At most one \(t_i\) is in \(\ker S\): otherwise two such vectors belong to the self-orthogonal space \(\operatorname{im}S\) and have dot product zero. At least \(k-1\) vectors \(St_i\) are therefore nonzero, supported on disjoint systematic coordinate sets, each of size at least four. Thus \(4(k-1)\le N\) and \(k\le1+N/4=1+2^{r-3}\). When \(r=2\), \(N=2\), there are only two nonzero disjoint helpers available among the checks and the explicit pair above achieves availability two; the verifier enumerates all four code coordinates.

For \(r=4\), label the eight cube vertices by the bit masks \(0,\ldots,7\). The three check parameters \(t\), written as eight-bit support masks, are hexadecimal `c3`, `11`, and `09`. Their images under \(S\) are respectively `00`, `66`, and `99`. All three checks contain \(y_0\); their helper sets, in order, are
\[
\{y_1,y_6,y_7\},\qquad
\{y_4,x_1,x_2,x_5,x_6\},\qquad
\{y_3,x_0,x_3,x_4,x_7\}.
\]
They are pairwise disjoint, proving \(a(y_0)\ge3\), and the universal bound gives \(a(y_0)\le3\). Cube translations act transitively on the parity coordinates and preserve \(S\), so equality holds for all \(y_v\). Finally, the asserted localities at \(r=2,3,4\) follow by enumerating all nonzero dual checks as detailed in the standalone verifier.

## Verification

Run `python3 verify.py` using Python 3 and its standard library. It explicitly constructs \(S\) from cube Hamming adjacency, checks \(S^2=I\) or \(0\) as appropriate for \(r=2,3,4\), enumerates every nonzero dual word, and computes exact maximum disjoint check-support packing and minimum repair sizes for one systematic and one parity coordinate. Cube translations give the remaining coordinates. It independently verifies the three witnesses for \(r=4\), the image distance there, and the ordinary code distances for \(r=2,3,4,5\). The observed terminal line is `VERIFY_OK`. The general theorem is proved algebraically; finite computation alone does not establish its all-parameter clauses.

## Relationship to prior work

Kenjale and Garge, *Suslin-Rao Codes: the bridge between pure and applied* (first public on 2026-09-24, arXiv:2610.03746), introduced this particular systematic block construction and determined several code parameters. The matrix \(I+A(Q_d)\) also occurs in the substantially earlier reflexive-cube graph-code literature, notably Fish, Key, and Mwambene (2011). Neither the construction nor its alternating self-duality behavior is claimed as original. The theorem here classifies whether repeated disjoint single-symbol recovery is possible for the two systematic coordinate classes, gives an explicit even-parameter upper bound, and identifies the first nontrivial sharp three-repair instance. The published source examinations and remaining originality risk are stated in the accompanying review.

## Limitations

The numerical upper bound for even \(r\ge6\) need not be sharp; their exact parity availability is not determined here. The 2011 reflexive-cube article was available bibliographically and through its abstract, but not in full text during this examination; unrecognized earlier repair statements remain possible. The general result concerns linear reconstruction of a single target and unrestricted helper-set size; it does not assert locality-achieving availability or optimal fault tolerance against adversarial multiple erasures. No independent audit has been carried out.

## References

1. N. Kenjale and A. S. Garge, *Suslin-Rao Codes: the bridge between pure and applied*, arXiv:2610.03746 (first version submitted 2026-09-24), https://arxiv.org/abs/2610.03746 .
2. W. Fish, J. D. Key, and E. Mwambene, *Binary codes from designs from the reflexive n-cube*, Utilitas Mathematica **85** (2011), 235–246, https://combinatorialpress.com/um/vol85/ .
3. W. Fish, J. D. Key, and E. Mwambene, *Graphs, designs and codes related to the n-cube*, Discrete Mathematics **309** (2009), 3255–3269, https://doi.org/10.1016/j.disc.2008.09.024 .
