# Orientation-Invariant Quantifier-Rank Profile of Finite Cycles

## Finding

For every integer \(q\ge1\) and all \(m,n\ge3\), let \(C_m,C_n\) be undirected cycle graphs and let \(D_m,D_n\) be directed cycles whose only nontrivial relation is the immediate-successor relation \(S\). Then \(D_m\equiv_q D_n\) if and only if \(C_m\equiv_q C_n\). Equivalently, all sizes at least three are equivalent at rank one; at rank two the only exceptional size is three; and for \(q\ge3\),
\[
D_m\equiv_q D_n\quad\Longleftrightarrow\quad m=n\ \text{or}\ m,n\ge 2^{q-1}+3.
\]

## Assumptions and scope

For \(n\ge3\), write \(C_n=(\mathbb Z/n\mathbb Z,E)\), where \(E(i,j)\) holds exactly when \(j-i\equiv1\) or \(-1\pmod n\). Write \(D_n=(\mathbb Z/n\mathbb Z,S)\), where \(S(i,j)\) holds exactly when \(j-i\equiv1\pmod n\). These are relational structures: the language has a binary relation, not a unary function symbol. The notation \(A\equiv_q B\) means that \(A\) and \(B\) satisfy the same first-order sentences of quantifier rank at most \(q\), equivalently that Duplicator wins the \(q\)-round Ehrenfeucht–Fraïssé game.

## Proof

First, on every \(D_n\) with \(n\ge3\), undirected adjacency is quantifier-free definable by
\[
E(x,y)\ \longleftrightarrow\ S(x,y)\lor S(y,x).
\]
Thus any rank-\(q\) sentence distinguishing two undirected cycles translates, without increasing quantifier rank, to a sentence distinguishing the corresponding directed cycles. In particular, directed-cycle equivalence implies undirected-cycle equivalence.

At rank one, every cycle of size at least three is nonempty and loopless, so all \(D_n\) with \(n\ge3\) agree. At rank two, \(D_3\) is distinguished from every \(D_n\) with \(n\ge4\) by
\[
\forall x\forall y\bigl(x\ne y\to(S(x,y)\lor S(y,x))\bigr).
\]
Any two directed cycles of sizes at least four are rank-two equivalent: after the first choice, the second choice is either the same vertex, its successor, its predecessor, or a vertex adjacent in neither direction; each response type is available in every cycle of size at least four.

For \(q\ge3\), Brown and Hoshino prove that the exact cutoff for undirected cycles is \(g(q)=2^{q-1}+3\): distinct cycle sizes below this cutoff are distinguishable at rank at most \(q\), while all sizes at least the cutoff are rank-\(q\) equivalent. Translating their distinguishing sentences by \(E(x,y)\mapsto S(x,y)\lor S(y,x)\) gives the same lower bound for directed cycles.

For the upper bound in the directed language, use the cycle-cut and gap-splitting strategy from their cycle proof. After the first move, cut each cycle at the selected vertex and represent it as a consistently oriented path whose two endpoints are copies of that selected vertex. In the remaining \(q-1\) rounds, the endpointed-path strategy matches each short gap exactly and keeps each longer gap above the stage-dependent threshold. The strategy can be chosen to preserve the linear order of selected points: a response to a point in a gap is chosen in the corresponding gap, with short distances copied exactly. Therefore it preserves every directed successor edge, which is precisely a gap of length one, as well as the undirected adjacency relation. The published sufficient bound for this path strategy is met when both cycle sizes are at least \(2^{q-1}+3\). Hence Duplicator wins on \(D_m,D_n\) whenever \(m,n\ge g(q)\). Combined with the lower bound and the direct rank-one and rank-two cases, this proves the stated equivalence of the size partitions.

## Verification

The cited cycle theorem gives \(g(2)=4\) and \(g(q)=2^{q-1}+3\) for \(q\ge3\). The rank-two boundary was checked directly using the displayed sentence and the four possible second-move types. The orientation-sensitive upper bound uses the order-preserving version of the published gap strategy; finite game checks were used only as a sanity check and are not part of the proof.

## Relationship to prior work

Jason I. Brown and Richard Hoshino, “The Ehrenfeucht–Fraïssé Game for Paths and Cycles,” *Ars Combinatoria* 83 (2007), 193–212, give the complete rank-threshold classification for undirected paths and cycles, including the cycle cutoff used here. Their published language has symmetric graph adjacency, not a directed successor relation. The new comparison is that the same size-equivalence partition survives the oriented relational expansion. Work on quantifier-depth bounds for finite abelian groups uses a different group language and does not state this successor-cycle classification.

## Limitations

The statement is restricted to cycles of size at least three and to the binary relational successor language. It does not apply to a unary function symbol for successor, where terms can iterate the function without adding quantifier rank. The lower-bound transfer is immediate from quantifier-free definability; the upper-bound transfer depends on using an order-preserving gap strategy after cutting the cycle.

## References

1. J. I. Brown and R. Hoshino, “The Ehrenfeucht–Fraïssé Game for Paths and Cycles,” *Ars Combinatoria* 83 (2007), 193–212. Published 30 April 2007; full text available from Combinatorial Press.
2. W. Gomaa, “Descriptive Complexity of Finite Abelian Groups,” *International Journal of Algebra and Computation* 20(8) (2010), 1087–1116. DOI: 10.1142/S0218196710006047.
