# Three-round orbit recovery for finite partition lattices

## Finding

Let \(n\ge 1\). Write \(\Pi_n\) for the set of all partitions of \([n]=\{1,\dots,n\}\), with the **full strict refinement relation** \(R(\pi,\sigma)\), meaning \(\pi\ne\sigma\) and every block of \(\pi\) is contained in some block of \(\sigma\). Begin with one common vertex colour and apply synchronous one-dimensional **bidirectional counting colour refinement**: each new colour records the preceding colour and the multisets, with multiplicity, of preceding colours among strict predecessors and strict successors.

**Theorem.** After at most **three** refinement rounds, two partitions have the same colour if and only if their multisets of block sizes coincide. Thus these colours are precisely the orbits of the symmetric-group action on \(\Pi_n\), and also the orbits of the full order-automorphism group. The stable partition has exactly \(p(n)\) classes, one for each integer partition of \(n\). A class of type \(\lambda=(1^{m_1}\cdots n^{m_n})\), with \(\sum_{r=1}^n r m_r=n\), has size

\[
\frac{n!}{\prod_{r=1}^{n}(r!)^{m_r}\,m_r!}.
\]

In particular, the number of rounds is bounded independently of \(n\), although the lattice contains \(B_n\) vertices, where \(B_n\) is the Bell number.

## Assumptions and scope

The lattice is supplied as a relational structure with **one directed binary predicate for all strictly comparable ordered pairs**, not merely its Hasse (cover) graph. Predecessors and successors are counted separately. No vertices are precoloured or individualized. Colours from each round are canonically compared through their refinement signatures; refinement never merges previously distinct colours. The result applies to every finite \(n\ge 1\), including the one-vertex case. It is an **intra-structure orbit-recovery theorem**, not an identification theorem against arbitrary other finite structures.

## Proof

**Step 1: identify block counts.** Let \(\pi\) have \(k\) blocks. A coarsening of \(\pi\) is exactly a partition of its \(k\)-element set of blocks. Hence \(\pi\) has precisely \(B_k-1\) strict successors. Since the Bell numbers are strictly increasing for positive arguments, the first-round colour determines \(k\). In particular, for \(n\ge2\) the partitions having \(n-1\) blocks (one doubleton and otherwise singletons) constitute a first-round class, denoted \(T_2\).

**Step 2: identify one-large-block classes.** For each integer \(r\) with \(3\le r\le n\), let \(T_r\) consist of the partitions with precisely one block of size \(r\) and all remaining blocks singletons. Fix \(\pi\) with \(k=n-r+1\) blocks of sizes \(s_1,\dots,s_k\). Its number of strict predecessors belonging to \(T_2\) equals

\[
A(\pi)=\sum_{i=1}^{k}\binom{s_i}{2}.
\]

Put \(e_i=s_i-1\ge0\). Then \(\sum_i e_i=r-1\), and

\[
2A(\pi)=\sum_i(e_i^2+e_i)\le(r-1)^2+(r-1)=r(r-1).
\]

For \(r\ge3\), equality holds exactly when only one \(e_i\) is positive, equivalently \(\pi\in T_r\). The value of \(k\) is already known at round one, and \(T_2\) is already a single colour class. Consequently the second-round colour identifies membership in each \(T_r\), for every \(3\le r\le n\), separately from all other types. The class \(T_2\) is already recognized. Each \(T_r\) remains a single colour class because relabelings of \([n]\) act transitively on it and preserve the refinement process.

**Step 3: recover every block size.** Let \(\pi\) have blocks of sizes \(s_1,\dots,s_k\). At round three, for each \(2\le r\le n\), the colour records the number \(N_r(\pi)\) of strict predecessors in the second-round class \(T_r\). Such a predecessor corresponds to choosing an \(r\)-subset wholly inside one block of \(\pi\). The sole possible non-strict choice is \(\pi\) itself when \(\pi\in T_r\). Therefore

\[
N_r(\pi)=\sum_{i=1}^{k}\binom{s_i}{r}-\mathbf 1_{\{\pi\in T_r\}}.
\]

The correction indicator is already determined by the second-round colour. It follows that round three recovers every binomial moment

\[
b_r(\pi)=\sum_{i=1}^{k}\binom{s_i}{r},\qquad 2\le r\le n.
\]

If \(m_s\) is the number of blocks of size \(s\), then \(b_r=\sum_{s=r}^{n}\binom{s}{r}m_s\). This upper-triangular system, with diagonal entries one, has the explicit inverse recursion

\[
m_n=b_n,\qquad m_r=b_r-\sum_{s=r+1}^n\binom{s}{r}m_s\quad(r=n-1,\dots,2),
\qquad m_1=n-\sum_{s=2}^n s\,m_s.
\]

Hence the third-round colour uniquely determines the entire block-size multiset. For \(n=1\) the claim is immediate; for \(n=2\) the first-round colours already distinguish the two partitions.

**Step 4: equality with automorphism orbits and counting.** The symmetric group \(S_n\) acts on the partition lattice by permuting \([n]\); this action is transitive on partitions with identical block-size multisets. Every refinement round is invariant under all such automorphisms, so it cannot split a common block-size type. Step 3 proves that it cannot join distinct types. Each class is therefore exactly a symmetric-group orbit. Since every symmetric-group permutation is an order automorphism, and every order automorphism preserves these refinement colours, the full order-automorphism orbits coincide with them. There is one class per integer partition of \(n\), giving \(p(n)\). Selecting disjoint unlabelled blocks of the prescribed sizes yields the displayed multinomial class-size formula. No further refinement can split any class, proving stability.

## Verification

Two independent finite corroboration procedures are included. `check_partition_lattice.py` explicitly generates all elements and all ordered strict refinement pairs, implements the stated synchronous bidirectional colour refinement, and compares the round-three partition with actual block-size types for \(1\le n\le8\). This checks 5,295 vertex instances over the eight lattices, including the 4,140-vertex lattice \(\Pi_8\); every comparison passed. `check_moments.py` independently enumerates integer-partition types for \(1\le n\le30\), verifies the triangular binomial-moment reconstruction, and checks the unique atom-count extremum at each permissible block count; all cases passed.

From a directory containing the four accompanying checker and output files, run `python3 check_partition_lattice.py 8` and `python3 check_moments.py`. Exact outputs are supplied in `check_output8.txt` and `moments_output.txt`. These **finite tests are corroboration, not the proof of the all-size theorem**; Steps 1–4 establish the infinite quantifiers.

## Relationship to prior work

The classification of set partitions by block-size type and the action of symmetric groups on the partition lattice are classical and explicitly discussed by Ehrenborg and Readdy [1] and Ehrenborg and Hedmark [2]. They are **not** new components of the theorem. Those works investigate Möbius functions, homology, and type-restricted filters, rather than recovery of types via a bounded number of counting-refinement steps. Arvind, Köbler, Rattan, and Verbitsky [3] formalize refinability as equality of colour classes and automorphism orbits, in the ordinary graph setting, and study general structural implications; their results do not give the present constant-round partition-lattice statement. The new assertion here is the uniform three-round recovery from the **entire strict order relation** via Bell counts, unique atomic extrema, and binomial inversion.

## Limitations

No optimality claim is made for three rounds; some of the checks stabilize sooner. The argument depends on giving refinement access to **all strict order pairs**; it does not prove the same bound for a cover graph. Equality with automorphism orbits does not imply identification among all finite posets by two-variable counting logic. A complete priority survey of every specialized treatment is not available; an earlier equivalent statement cannot be ruled out by these comparisons. The theorem uses the classical orbit partition, not a novel automorphism-group classification.

## References

1. Richard Ehrenborg and Margaret Readdy, *The Möbius function of partitions with restricted block size*, arXiv:1009.3976 (public e-print dated 2010-09-21), https://arxiv.org/abs/1009.3976 .
2. Richard Ehrenborg and Dustin Hedmark, *Filters in the partition lattice*, arXiv:1606.01443 (2016), https://arxiv.org/abs/1606.01443 .
3. V. Arvind, Johannes Köbler, Gaurav Rattan and Oleg Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (2015), https://arxiv.org/abs/1502.01255 .
