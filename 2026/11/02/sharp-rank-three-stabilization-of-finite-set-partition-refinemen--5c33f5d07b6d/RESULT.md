# Sharp rank-three stabilization of finite set-partition refinement lattices

## Finding

Let \(\Pi_n\) denote the finite lattice of all partitions of an \(n\)-element set, ordered by refinement (a finer partition is smaller). In first-order logic containing only equality and this binary order relation, for every pair of integers \(m,n\ge1\),

\[
\Pi_n\equiv_3\Pi_m \quad\Longleftrightarrow\quad \min(n,7)=\min(m,7).
\]

Thus precisely seven rank-three theories occur. The stable class begins at \(n=7\) and has a smallest representative with \(B_7=877\) elements, where \(B_n\) is the Bell number. This is sharp among these partition lattices. The result is for **quantifier rank**, not for a bound on the number of variables, and for the **pure order language**, not the language with meet and join operations.

## Assumptions and scope

For a partition \(x\), let \(b(x)\) be its number of blocks and set \(r(x)=n-b(x)\), \(c(x)=b(x)-1\). These are its rank and corank, satisfying \(r(x)+c(x)=n-1\). The bottom is the all-singleton partition, and the top is the one-block partition. Let \(x<y\) mean strict refinement, and \(x\parallel y\) incomparability. All partitions are ordinary set partitions, including both extrema. No probability, additional predicates, or lattice function symbols are assumed.

## Proof

**Step 1: a complete two-point extension table.** For distinct or equal partitions \(x,y\), describe the location of a possible third partition \(z\) relative to each of \(x,y\) using four symbols: \(E\) (equal), \(L\) (strictly below), \(G\) (strictly above), and \(I\) (incomparable). The pair \((u,v)\) means relation \(u\) of \(z\) to \(x\), and relation \(v\) of \(z\) to \(y\). The following table lists **all and only** realizable pairs, along with necessary and sufficient conditions:

* If \(x=y\), the always-available pair is \((E,E)\). Additionally \((L,L)\) occurs exactly when \(r(x)>0\), \((G,G)\) exactly when \(c(x)>0\), and \((I,I)\) exactly when both hold.
* If \(x<y\), \((E,L),(G,E)\) always occur. The other possibilities are \((L,L),(I,L)\) iff \(r(x)>0\); \((G,G),(G,I)\) iff \(c(y)>0\); \((G,L)\) iff \(r(y)-r(x)\ge2\); and \((I,I)\) iff \(r(x)>0\) and \(c(y)>0\). No other pair occurs.
* If \(x>y\), swap the two entries of the preceding row.
* If \(x\parallel y\), \((E,I),(I,E),(L,L),(G,G),(I,I)\) always occur. The four other possibilities are \((L,I)\) iff \(r(x)\ge2\), \((G,I)\) iff \(c(x)\ge2\), \((I,L)\) iff \(r(y)\ge2\), and \((I,G)\) iff \(c(y)\ge2\). No other pair occurs.

To prove sufficiency, remember that partitions are equivalence relations: an atom merges one pair of elements, and a coatom separates the ground set into two nonempty blocks. Every partition is the join of the atoms beneath it and the meet of the coatoms above it. Consequently, if \(x<y\), there is an atom below \(y\) but not below \(x\), and a coatom above \(x\) but not above \(y\); these give \((I,L)\) and \((G,I)\). An atom joining elements from distinct \(y\)-blocks is incomparable with both \(x\) and \(y\) whenever \(x\ne\bot\), giving \((I,I)\) under its two stated conditions. Standard strict intermediate elements give \((G,L)\). Existence of \((L,L)\) and \((G,G)\) follows by choosing an element strictly below \(x\) or above \(y\), respectively. Equality pairs are immediate.

For incomparable \(x,y\), their meet and join give \((L,L),(G,G)\). A nontrivial element strictly below \(x\) but not below \(y\) exists exactly when \(r(x)\ge2\): one takes an atom beneath \(x\) absent from \(y\). Its dual gives the coatom above \(x\) incomparable with \(y\) exactly when \(c(x)\ge2\). Symmetry handles the other two asymmetric patterns. Finally, two incomparable non-top equivalence relations must separate some same unordered pair of ground elements (if their joined-pair relations covered all pairs, transitivity would force one relation to be universal). Merging such a pair defines an atom incomparable with both, giving \((I,I)\). Necessity of all conditions follows from ranks and extremality. This completes the table for every \(n\ge1\), including the small cases.

**Step 2: pointed two-round profiles stabilize at clipped ranks.** Assume \(n\ge7\) and define
\[
\tau(x)=\bigl(\min(r(x),3),\min(c(x),3)\bigr).
\]
After selecting \(x\), one more selection \(y\) leaves one round. The available final adjacency/equality patterns are precisely the table in Step 1. If \(y<x\), the table depends only on whether \(y\) is bottom, whether the gap from \(y\) to \(x\) is one or at least two, and whether \(x\) is top. All possible combinations depend only on the clipped value \(\min(r(x),3)\): rank one has only the bottom at gap one; rank two adds the bottom at gap two and a nonbottom predecessor at gap one; rank at least three additionally permits a nonbottom element at gap at least two. There are no further signatures from larger gaps. The case \(y>x\) is dual and depends only on \(\min(c(x),3)\).

If \(y=x\), the row of Step 1 depends only on extremality. If \(y\parallel x\), the table depends only on whether the rank or corank of each selected element is at least two. For **every** non-extremal \(x\) when \(n\ge7\), incomparable \(y\) exist in each of the three types: atom (rank one), coatom (corank one), and middle (rank and corank at least two). For an atom, merge a pair separated by \(x\); for a coatom, separate a pair joined by \(x\); for a middle element of rank two, if \(r(x)=1\) choose a triple away from the pair defining \(x\), if \(r(x)=2\) choose any distinct rank-two partition, and if \(r(x)\ge3\) merge a triple containing elements from different \(x\)-blocks. The last construction works since \(x\) is not top; rank two ensures the chosen middle partition is not below or above \(x\). Hence every incomparable-row signature is likewise determined by \(\tau(x)\). Both directions of a second move are covered by the same analysis.

Therefore a pointed partition lattice with two remaining moves has a game type determined by \(\tau(x)\), independently of block sizes and independently of \(n\ge7\).

**Step 3: three-round equivalence of all large lattices.** In each \(\Pi_n\) for \(n\ge7\), every rank \(r\in\{0,\dots,n-1\}\) occurs and \(c=n-1-r\), so the set of \(\tau\)-values is exactly
\[
\{(0,3),(1,3),(2,3),(3,3),(3,2),(3,1),(3,0)\}.
\]
In the first move of a three-round Ehrenfeucht–Fraïssé game between any \(\Pi_m,\Pi_n\) with \(m,n\ge7\), match the selected partition to one with the same \(\tau\). Step 2 gives a matching response to every second move with identical third-move extension sets; Step 1 gives a response to the third move preserving every equality and refinement fact among the three chosen elements. Thus Duplicator wins, proving \(\Pi_m\equiv_3\Pi_n\).

**Step 4: the cutoff is exact.** For a free variable \(x\), define \(L_1(x)\) to assert existence of a strict predecessor, \(L_2(x)\) a strict chain of length two below \(x\), and \(L_3(x)\) the rank-at-least-three property
\[
L_3(x):=\exists y\bigl[(\exists z\ z<y)\land(\exists w\ y<w<x)\bigr].
\]
Each has quantifier rank at most two (the internal strict-chain variables are within one more quantifier under \(\exists y\)). Define \(U_1,U_2,U_3\) dually by reversing order. Then for each \(t=2,\dots,7\) there is a sentence of quantifier rank at most three, true exactly in those \(\Pi_n\) with \(n\ge t\): respectively
\[
\begin{aligned}
t=2:&\quad \exists x\,L_1(x),\\
t=3:&\quad \exists x\,L_2(x),\\
t=4:&\quad \exists x\,L_3(x),\\
t=5:&\quad \exists x\,[L_2(x)\land U_2(x)],\\
t=6:&\quad \exists x\,[L_3(x)\land U_2(x)],\\
t=7:&\quad \exists x\,[L_3(x)\land U_3(x)].
\end{aligned}
\]
Indeed such a partition exists iff the rank-plus-corank requirement is at most \(n-1\). For each distinct truncated parameter, a threshold sentence separates the smaller and larger members. Finally \(|\Pi_7|=B_7=877\), while all smaller parameter values have different three-round theories. This proves both directions and sharpness.

## Verification

The accompanying standalone `verify_partition_rank3.py` enumerates all set partitions using restricted-growth sequences and stores pair-equivalence relations as integers. It compares the exact third-move extension masks against the symbolic table for all **813,297** ordered pairs across the cases \(n=1,\dots,7\); it additionally checks 50,000 deterministically sampled pairs for \(n=8\). It computes the full three-round theory by enumerating second- and third-move signatures, reducing the first move only by genuine ground-set permutation orbits (block-size multisets). It recovers seven pairwise different classes through \(n=8\), with identical signatures at \(n=7,8\). The enumeration provides finite corroboration of Step 1 and the cutoff; Step 3 is the independent proof for unbounded \(n\).

Run `python3 verify_partition_rank3.py` from the directory containing the standalone script; compare with `verification_output.txt`. No external packages or data files are used.

## Relationship to prior work

Pittel, *Where the Typical Set Partitions Meet and Join* (2000), studies the same finite refinement lattices, but its theorems give asymptotic random meet/join properties, not first-order equivalence at fixed quantifier rank. Weil, *On the logical definability of certain graph and poset languages* (2006), concerns definability of graph/poset languages via compositional structure, rather than individual set-partition refinement lattices. Ellerman, *The Logic of Partitions* (2009), develops propositional partition logic and lattice operations, rather than pure-order finite model theory. Contreras-Mantilla and Sinclair, *The model theory of metric lattices: pseudofinite partition lattices* (2025), develops metric/continuous model theory on partition lattices: its pseudofinite framework is not a uniform rank-three equivalence in pure discrete first-order logic. Balbiani and Tinchev, *Definability Over the Class of all Partitions* (2006), concerns modal/first-order definability; only its accessible abstract was examined, so an implicit implication in its inaccessible full text cannot be excluded.

Other adjacent finite powerset inclusion-poset and linear-subspace inclusion-poset classifications have rank-three cutoff six, but are not statements about the nonmodular set-partition lattice. In particular, neither follows from the other merely by changing terminology; the third-move extension table and optimal cutoff differ.

## Limitations

No claim is made about rank four or higher, about a richer signature containing lattice operations or constants, or about all geometric lattices. The standalone finite checks do not prove any unbounded assertion. The paper by Balbiani and Tinchev could not be fully inspected; historical priority is not asserted to be exhaustive. Mathematical validation by an independent party has not been performed.

## References

1. Boris Pittel, *Where the Typical Set Partitions Meet and Join*, Electronic Journal of Combinatorics **7** (2000), R5; https://doi.org/10.37236/1483 (first public date documented 2000-01-15).
2. Pascal Weil, *On the logical definability of certain graph and poset languages*, arXiv:cs/0609048 (submitted 2006-09-11); https://arxiv.org/abs/cs/0609048.
3. Philippe Balbiani and Tinko Tinchev, *Definability Over the Class of all Partitions*, Journal of Logic and Computation **16** (2006), 541–557; https://doi.org/10.1093/logcom/exl024.
4. David Ellerman, *The Logic of Partitions: Introduction to the Dual of the Logic of Subsets*, arXiv:0902.1950 (2009); https://arxiv.org/abs/0902.1950.
5. José Contreras-Mantilla and Thomas Sinclair, *The model theory of metric lattices: pseudofinite partition lattices*, arXiv:2507.10932 (2025); https://arxiv.org/abs/2507.10932.
