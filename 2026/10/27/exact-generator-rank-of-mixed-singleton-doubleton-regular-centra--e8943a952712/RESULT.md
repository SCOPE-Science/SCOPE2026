# Exact generator rank of mixed singleton–doubleton regular centralizers

## Finding

For each integer \(b\ge1\), let \(X_b=\{0\}\sqcup\bigcup_{i=1}^b\{(i,0),(i,1)\}\), and let \(e\) fix \(0\) and send both points \((i,0),(i,1)\) to \((i,0)\). For the monoid of full transformations \(C_b=\{f:X_b\to X_b:fe=ef\}\), its **semigroup** rank is
\[
\operatorname{rank} C_b=\begin{cases}3,&b=1,\\4,&b=2,\\5,&b\ge3.\end{cases}
\]
Its cardinality is \((b+1)(2b+1)^b\). In the mixed case \(b\ge2\), at least three distinct kinds of nonunit are necessary, in addition to generators of the units.

## Assumptions and scope

Multiplication is from left to right. Rank counts the minimum size of a set whose **nonempty** words give every member of \(C_b\), including the identity; it is not image cardinality. If the empty word is allowed, the rank at \(b=1\) is instead 2. The other values are unchanged. Write \(B=\{0,1,\ldots,b\}\) for the index set of kernel blocks of \(e\); the section consists of \(0\) and the representatives \((i,0)\).

## Proof

**Normal form and units.** Commutation requires each source block to be mapped into a target block and its representative to the target representative; these two rules also suffice. A map is therefore described by an index map \(\sigma:B\to B\) and bits \(\varepsilon_i\) for \(i>0\) indicating whether the second point of block \(i\) maps to the second point of block \(\sigma(i)\). When \(\sigma(i)=0\), the bit must be 0. In a product of \((\sigma,\varepsilon)\) followed by \((\tau,\delta)\), the index map is \(\tau\circ\sigma\) and the positive-source bits are \(\varepsilon_i\delta_{\sigma(i)}\), with \(\delta_0=0\). There are \(b+1\) choices for the target of the singleton and \(2b+1\) choices for each positive block. A unit must be bijective, hence fixes the singleton and permutes the positive blocks with all bits one; these maps are all units. The unit group is \(S_b\).

**Generators.** For \(b=1\), take the identity as the unit generator. For \(b\ge2\), take the positive-index transposition \((1\ 2)\); for \(b\ge3\) also take \((1\ 2\ \cdots\ b)\). The cyclic conjugates of the transposition include the adjacent transpositions, and powers of the transposition give the identity. Thus these are semigroup generating sets of the units. Add the following nonunits with their displayed block actions and maximal permitted bits:

- \(t\) swaps indices 0 and 1 and fixes the others (the bit at source index 1 is zero, because that block maps to 0).
- \(z\) sends index 0 to 1 and fixes every positive index.
- If \(b\ge2\), \(c\) sends index 2 to 1 and fixes all other indices.

Conjugation by units relabels the positive indices. Write \(t_j,z_j\) for the relabeled maps and \(c_{j\to k}\) for the elementary positive collapse. Now \(z_jt_j\) fixes index 0 and sends index \(j\) to 0, and \(d_j=t_j^2\) fixes all indices and deletes just the bit at \(j\). The elementary positive collapses and positive permutations generate every map on the positive indices: for each target fibre of a given transformation, collapse its sources onto one chosen source in that fibre, then permute the distinct representatives onto the distinct targets. This also holds for \(b=1\), when the only such map is the identity. Any index map \(h\) fixing 0 is built with maximal allowable bits by first sending its zero-target positive indices to 0 using \(z_jt_j\), and then applying a transformation of the positive indices with the prescribed positive targets for the remaining indices.

To realize a map with \(\sigma(0)=a>0\), work first with maximal allowed bits. If there is a positive \(j\) with \(\sigma(j)=a\), first apply \(z_j\), then apply the zero-fixing map whose positive-index targets are the specified ones. If there is no such \(j\) but there is a positive \(j\) with \(\sigma(j)=0\), first apply \(t_j\); the next, zero-fixing map takes \(j\) to \(a\) and all other positive indices to their specified targets. The bit lost in the swap was destined for 0. If no positive index maps to 0 or \(a\), some distinct positive \(j,k\) share a target since only \(b-1\) targets remain. Apply \(c_{j\to k}t_j\), then the zero-fixing map taking \(j\) to \(a\) and every other positive index to its specified target. The collapse vacates \(j\) before the swap, so no original positive-source bit is lost there. Finally, for any of these maximal-bit maps, precompose with the chosen \(d_j\) to delete those bits required to be zero. This proves the upper bounds.

**Lower bounds.** A product of full maps of a finite set can be bijective only if each factor is bijective. Thus a semigroup generating set must generate the units using only units: at least one for \(b=1\) (the unique identity), one for \(b=2\), and two for \(b\ge3\) (where \(S_b\) is nonabelian). To produce \(t\), the index maps in the word must all be permutations of \(B\), with at least one moving 0. Such a factor is a nonunit sending a positive index to 0. To produce \(z\), all original positive indices must remain distinct and positive and all corresponding bits must survive throughout the word. Indeed neither a merged index nor a lost bit can be restored. Just before each factor these indices exhaust the set of positive indices; each factor must therefore permute that set with bits one. At least one factor sends 0 to a positive index, a nonunit of a different kind from the one required for \(t\). These two required nonunits apply also at \(b=1\). For \(b\ge2\), consider any word for \(c\) at the first factor merging two originally distinct positive indices. All original positive-source bits survive, so just before the first merger those index trajectories exhaust the positive set, and the merging factor maps the whole positive set into itself noninjectively. It cannot be either of the two previous kinds. This gives the three lower bounds, and shows why the empty-word convention changes only \(b=1\).

## Verification

Run `python3 verify.py` using the accompanying bounded checker. It computes closure starting from the proposed generators, **not** from an inserted identity. For \(b=1,2\), it separately enumerates all point maps and filters directly by commutation. In particular all pairs fail at \(b=1\), and \(\{t,z\}\) produces exactly the five nonunits. For \(b=2\) the checker tests all 2,628 choices of two nonunits with the nonidentity unit. For \(b=3,4\) it checks the commutation of the generators and the size of the generated subsemigroup against the cardinality formula. The sizes for \(b=1,2,3,4\) are respectively 6, 75, 1,372, and 32,805. These finite tests corroborate the proof; they are not a proof for unbounded \(b\).

## Relationship to existing work

Araújo, Bentz, Mitchell, and Schneider identify idempotent centralizers with partition-and-section preserving transformations and pose the general regular-case rank problem in Problem 5.3. Their Theorem 1.1 for all partition-preserving maps concerns a larger monoid: commutation also constrains the section. Dolinka and East treat idempotent generation for a uniform partition, not the full mixed centralizer. The indexed *Rank spectra of centralizers of finite transformation retractions* treats the same general centralizer object but counts its elements by the cardinalities of their images, not the minimum sizes of generating sets. The cardinality and normal form here are supporting structure, not originality claims. The contribution is the mixed-type generator rank and the separate necessary nonunit mechanisms, not the vacuous-unit convention at \(b=1\) on its own.

## Limitations

The generator-rank formula is for precisely one singleton and \(b\) doubletons. It does not solve the general regular centralizer rank problem or claim publication priority over the full earlier centralizer literature.

## References

1. J. Araújo, W. Bentz, J. D. Mitchell, and C. Schneider, *The rank of the semigroup of transformations stabilising a partition of a finite set*, https://arxiv.org/abs/1404.1598, especially Theorem 1.1 and §5.
2. I. Dolinka and J. East, *Idempotent generation in the endomorphism monoid of a uniform partition*, https://arxiv.org/abs/1407.3312.
3. J. Araújo and J. Konieczny, *Semigroups of transformations preserving an equivalence relation and a cross-section*, Communications in Algebra 32 (2004), 1917–1935.
4. J. André, J. Araújo, and J. Konieczny, *Regular centralizers of idempotent transformations*, Semigroup Forum 82 (2011), 307–318.
5. *Rank spectra of centralizers of finite transformation retractions*, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-rank-spectra-of-centralizers-of-finite-transformation-retraction--cabfb16a59f1.
