# Sharp comparison shattering thresholds for fixed-layer permutations

## Finding

For integers \(r\ge1\) and \(n\ge r+1\), let \(\mathcal L_{n,r}\) consist of all permutations of \([n]\) that are direct sums of exactly \(r+1\) nonempty decreasing consecutive layers. Regard each such permutation as a Boolean concept on position pairs \((i,j)\) with \(1\le i<j\le n\), with answer \(1\) exactly when the entry at position \(i\) is larger than the entry at position \(j\).

**Sharp saturation theorem.** For all these parameters,
\[
\operatorname{VCdim}(\mathcal L_{n,r})\le 2r,
\qquad
\operatorname{VCdim}(\mathcal L_{n,r})=2r
\ \Longleftrightarrow\ n\ge4r+1.
\]
The threshold is an if-and-only-if statement, not only a sufficient large-size bound.

**Exact three-layer classification.** For \(r=2\),
\[
\operatorname{VCdim}(\mathcal L_{n,2})=
\begin{cases}
0,&n=3,\\
\min\{4,\lfloor(n-1)/2\rfloor\},&n\ge4.
\end{cases}
\]
The first difference between static and adaptive shattering in this three-layer family occurs at \(n=6\):
\[
\operatorname{VCdim}(\mathcal L_{6,2})=2,
\qquad
\operatorname{Ldim}(\mathcal L_{6,2})=3.
\]
For \(n=3,4,5\) the two dimensions agree and equal \(0,1,2\), respectively.

**Uniform online bounds.** Write \(m=n-1\) and \(a=\lfloor m/r\rfloor\). Every admissible pair satisfies
\[
r\lfloor\log_2 a\rfloor
\le \operatorname{Ldim}(\mathcal L_{n,r})
\le\left\lfloor\log_2\binom{m}{r}\right\rfloor.
\]
In particular, for each fixed positive integer \(r\), as \(n\) increases,
\[
\operatorname{Ldim}(\mathcal L_{n,r})=r\log_2 n+O_r(1),
\]
while the VC dimension is eventually exactly \(2r\). Therefore the adaptive-minus-static gap is unbounded even with a fixed number of layers.

## Assumptions and scope

A layered permutation of length \(n\) is a direct sum of nonempty decreasing blocks: values decrease inside each block and every value in an earlier block is smaller than every value in a later block. The number of blocks is exactly \(r+1\); it is not merely bounded above by that number. Such a permutation is uniquely specified by its \(r\) distinct cut positions in \([m]\), where \(m=n-1\). Thus the number of hypotheses is \(\binom mr\).

Both dimensions use the full set of pairwise positional comparisons as queries; this is not the alternative permutation-pattern VC notion based on simultaneously realizing all orders on a chosen set of positions. Littlestone dimension means the maximum depth of a complete binary query tree such that each root-to-leaf answer sequence is realized by one hypothesis. Logarithms are base two.

## Proof

**1. Exact reduction to interval hitting.** Write \(C\subseteq[m]\) for the set of the \(r\) cut positions. For \(i<j\), the entries of the permutation at those positions form an inversion precisely when no cut occurs between them. Hence
\[
\mathbf1[\pi_C(i)>\pi_C(j)]
=1-\mathbf1[C\cap[i,j-1]\ne\varnothing].
\]
Every nonempty integer interval of \([m]\) arises uniquely as \([i,j-1]\). Uniformly reversing labels on queries changes neither VC nor Littlestone dimension. We may therefore work with the interval-hit class whose hypotheses are exactly the \(r\)-subsets \(C\) of \([m]\) and whose queries are all nonempty intervals \(I\subseteq[m]\), answered \(\mathbf1[C\cap I\ne\varnothing]\).

**2. A private-point lemma and the universal upper bound.** Suppose a family of \(t\) distinct query intervals \(I_1,\ldots,I_t\) is VC-shattered. For the trace that is positive only on \(I_s\), at least one selected cut belongs to \(I_s\) and no other queried interval. Thus each interval has a *private point* \(p_s\), and the \(t\) private points are distinct. Order them on the line. No point can belong to three of the queried intervals: if it belonged to intervals having private points \(p_a<p_b<p_c\), then either its location lies to the left of \(p_b\), forcing the interval containing \(p_c\) also to contain \(p_b\), or it lies to the right, forcing the interval containing \(p_a\) also to contain \(p_b\). Both contradict privacy; the equality case is also impossible. Consequently each cut hits at most two intervals. The all-positive trace uses exactly \(r\) cuts and can hit at most \(2r\) intervals. Therefore \(t\le2r\).

**3. Exact size threshold for saturation.** Suppose \(t=2r\) query intervals are shattered. Their private points give \(2r\) distinct positions with incidence count one. The all-negative trace requires \(r\) further positions, each with incidence count zero. For the all-positive trace, \(r\) selected positions must cover \(2r\) intervals, and each position meets at most two intervals; therefore each must meet *exactly* two. These yield \(r\) more positions, distinct from both the private points and the zero-incidence positions. Hence \(m\ge2r+r+r=4r\), or \(n\ge4r+1\).

Conversely, assume \(m\ge4r\). In each of \(r\) disjoint consecutive four-point blocks beginning at \(s\), select the two queries \([s,s+1]\) and \([s+1,s+2]\). Choosing one cut at positions \(s,s+1,s+2,s+3\) gives, respectively, query patterns \((1,0),(1,1),(0,1),(0,0)\). Choose exactly one cut in each block. The \(r\) blocks independently realize all \(4^r=2^{2r}\) answer strings on the \(2r\) queries, proving sharpness and the if-and-only-if threshold.

**4. Full three-layer VC formula.** Put \(r=2\). The upper bound four is already proved. Shattering one query requires at least three cut positions: one privately in its interval and two outside to realize the zero trace. Shattering two queries requires two private positions and two zero-incidence positions, hence at least four positions. Shattering three requires three private positions and two zero-incidence positions; the all-positive trace also needs a further position lying in at least two intervals, hence at least six positions. Shattering four requires at least eight positions by step 3. Conversely, matching lower witnesses exist on three, four, six and eight positions, respectively:

- One query on three positions: \([1,1]\).
- Two queries on four positions: \([1,1]\), \([2,2]\).
- Three queries on six positions: \([1,1]\), \([2,3]\), \([3,4]\).
- Four queries on eight positions: the two four-point blocks from step 3.

The claimed formula follows by embedding witnesses into larger chains. For the three-query witness, the eight patterns \(000,001,010,011,100,101,110,111\) are realized by the cut pairs \((5,6),(4,5),(2,5),(2,3),(1,5),(1,4),(1,2),(1,3)\), respectively. The four-query witness is verified blockwise in step 3.

**5. First adaptive separation.** For three layers and \(n=3,4,5\), the numbers of hypotheses are \(1,3,6\). Their cardinality upper bounds on Littlestone dimension are \(0,1,2\), matching the VC values from step 4. At \(n=6\), there are ten hypotheses and the VC dimension is two. A complete depth-three interval-hit query tree is specified in `three_layer_first_gap_tree.json`; it has eight pairwise distinct cut-pair witnesses, checked one path at a time by `verify_layered_comparisons.py`. This proves Littlestone dimension at least three. Its upper bound is \(\lfloor\log_2 10\rfloor=3\). Negating the interval-hit answers gives the corresponding comparison tree for the layered permutations.

For clarity, the witness tree begins with query \([1,1]\). The zero branch asks \([1,2]\) and the one branch asks \([2,3]\). The four depth-two nodes ask, in the resulting lexicographic answer order, \([1,3]\), \([3,3]\), \([2,4]\), \([2,2]\). Their final witnesses are recorded explicitly in the accompanying JSON certificate.

**6. General online growth.** Partition \([m]\) into \(r\) consecutive blocks each of length at least \(a=\lfloor m/r\rfloor\). Restrict to hypotheses selecting exactly one cut in each block, and in each block restrict that cut to a specified length-\(a\) subblock. Interval queries confined to one subblock act as ordinary threshold tests on the corresponding cut. By balanced binary splitting, the selected position in each subblock supports a shattered adaptive tree of depth \(\lfloor\log_2 a\rfloor\). Concatenating these trees over the independent blocks gives depth \(r\lfloor\log_2 a\rfloor\). Conversely, every shattered tree of depth \(d\) needs at least \(2^d\) different hypotheses, whereas there are exactly \(\binom mr\). This proves the displayed bounds and the fixed-\(r\) asymptotic relation.

## Verification

Run `python verify_layered_comparisons.py` and `python verify_permutation_direct.py` with Python 3 and no external packages. The first checker evaluates 21,878 direct permutation-comparison equalities, exhaustively computes VC and Littlestone dimensions for two-cut interval-hit classes on two through nine cut positions, replays the eight distinct depth-three terminal witnesses and checks the sharp \(2r\)-query gadgets for one through five cuts. The second checker independently generates three-layer permutations by positive compositions and recomputes the VC dimension at orders three through nine and Littlestone dimension through order six. Both programs completed successfully. Their finite computations are supplementary; the all-parameter statements follow from the proofs above.

## Relationship to prior work

Layered permutations and their fixed numbers of layers are standard objects. Kabela, Kráľ, Noel and Pierron study their pattern densities and structural properties, including three-layer patterns. The inspected main theorems and conclusion address packing-density maximizers, not the Boolean pairwise-comparison concept class or its shattering dimensions. Guingona, Kolesnikov, Nierwinski and Soucy develop exact VC and Littlestone dimensions for zero sets of nontrivial linear combinations of independent functions, a different concept family. Their equality-of-dimensions theorem does not cover this class, whose adaptive/static difference is unbounded.

The standard VC result for unions of a fixed number of intervals describes point-membership queries on interval unions; the present problem is the **dual-type incidence language** of choosing a fixed number of points and asking interval-intersection questions. A bounded VC dimension is consistent with generic closure arguments, but the exact finite saturation boundary \(m=4r\), the full three-layer VC formula and the depth-three first-gap certificate require the above interval-incidence analysis. They are not claimed to settle arbitrary pattern-avoiding permutation classes, and a definitive historical-priority survey has not been completed.

## Limitations

The exact Littlestone dimension for every order and every fixed number of layers is not determined; only the sharp first three-layer gap, the certified small values and the stated universal bounds and asymptotic are proved. The result concerns comparison queries by *positions* and exactly \(r+1\) layers. Alternative query languages, unrestricted layered permutations and other permutation-pattern classes are outside the theorem. The review is not independent validation. Prior work under alternative terminology for dual interval range spaces remains a literature risk.

## References

1. A. Kabela, D. Kráľ, J. A. Noel and T. Pierron, *Density maximizers of layered permutations*, arXiv:2110.01723, first submitted 2021-10-04. https://arxiv.org/abs/2110.01723
2. V. Guingona, A. Kolesnikov, J. Nierwinski and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805, first submitted 2021-09-10. https://arxiv.org/abs/2109.04805
3. R. Raz, *VC-dimension of sets of permutations*, Combinatorica 20 (2000), 241–255, DOI 10.1007/s004930070023. This uses a different, nonbinary permutation VC notion. https://doi.org/10.1007/s004930070023
