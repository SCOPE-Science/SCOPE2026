# The all-petals flower need not be finite
## Finding

In v2 of Fernández-Duque's *Fine Selection for Intuitionistic Modal Logic*, the construction used in the proof of Proposition 12.3 need not be finite as written.

The proposition takes
\[
n=\max\{\operatorname{dpt}_A(w),2|\Sigma|+1\},
\]
lets
\[
\mathcal G
\]
be the set of all \(n\)-petals over a bud \(w\), up to isomorphism, and sets
\[
A'=A\sqcup_w\mathcal G.
\]

There are choices satisfying all hypotheses for which
\[
|\mathcal G|=\infty.
\]

More explicitly, take the one-atom closed set
\[
\Sigma=\{p_\bullet\},
\]
where \(p_\bullet\) is the distinguished atom used in the paper's generated canonical structure. One can choose a \(\Sigma\)-region \(r\) whose canonical bud contains a reflexive canonical point
\[
\Psi\mathrel{R_c}\Psi.
\]
Choose a finite set \(C\subseteq\widehat r\) of \(\Sigma\)-representatives containing \(\Psi\), and let \(A\) consist of one reflexive modal cluster, with one world mapped to each element of \(C\), equipped with the identity intuitionistic relation.

Then \(A\) is a stable canonical \(\Sigma\)-tree, every world of its modal cluster is a bud, and
\[
\operatorname{dpt}_A(w)=0.
\]
Because
\[
|\Sigma|=1,
\]
the parameter in Proposition 12.3 is
\[
n=3.
\]

For every integer
\[
m\ge1,
\]
let \(B_m\) be an \(m\)-point reflexive modal cluster and map every point of \(B_m\) to \(\Psi\). Each \(B_m\) is a canonical \(\Sigma\)-tree. It lies in the same region as \(w\), can be grafted onto \(w\), and has
\[
\operatorname{hgt}(B_m)=
\operatorname{wdt}(B_m)=0.
\]
Hence every \(B_m\) is a \(3\)-petal over \(w\).

The structures
\[
B_1,B_2,B_3,\ldots
\]
are pairwise nonisomorphic because their underlying sets have different cardinalities. Therefore the family of all \(3\)-petals over \(w\), even modulo ordinary isomorphism, is infinite.

Definition 8.2 defines simultaneous grafting
\[
A\sqcup_w\mathcal B
\]
only when \(\mathcal B\) is a finite set of canonical sprouts. Thus the displayed assignment
\[
A'=A\sqcup_w\mathcal G
\]
in the proof of Proposition 12.3 does not, by itself, define a finite canonical tree in this example.

This identifies a finiteness gap in that construction. It does **not** show that Proposition 12.3 is false, that no finite flower can be selected, or that \(\mathsf{IK4}\) lacks the finite model property.

## Assumptions and scope

The terminology is exactly that of arXiv:2609.27078v2.

A \(\Sigma\)-sprout is finite and tree-like. Its height counts strict modal chains, and its width counts incomparable immediate modal successors. A canonical \(\Sigma\)-tree is a canonical sprout whose \(\Sigma\)-restriction is completely labelled and has every modal defect resolved.

A bud \(w\) requires the image of its full modal cluster to be a set of \(\Sigma\)-representatives of the canonical bud of \(\rho(w)\), together with a condition excluding a strict modal predecessor in the same region.

An \(n\)-petal over \(w\) is a canonical \(\Sigma\)-tree \(B\) satisfying
\[
\rho(B)=\rho(w),
\]
graftability onto \(w\), width at most \(n\), height at most \(n+1\), and an additional condition only when the height is exactly \(n+1\).

The counterexample concerns ordinary isomorphism types of canonical sprouts. It exploits multiplicity inside one reflexive modal cluster. The paper's width and height parameters do not count that multiplicity.

## Proof

We first produce the canonical data needed for the example.

Take
\[
\Sigma=\{p_\bullet\}.
\]
This is finite and closed under subformulas and respects the standing convention in the source that \(p_\bullet\in\Sigma\).

Consider a one-world reflexive \(\mathsf{IK4}\) model in which \(p_\bullet\) is false, and let \(\Theta\) be the prime theory of its unique world. The modal loop makes the singleton reflexive \(\Sigma\)-sprout map homomorphically to \(\Theta\).

Apply the source's Finality Proposition 6.2 to this singleton sprout and the preorder used to define regions. We obtain a \(\Sigma\)-region \(r\) whose full Final cluster contains a point to which the reflexive singleton maps.

We now choose a reflexive point in the canonical bud \(\widehat r\).

If \(r\) is a singleton, its unique point is the reflexive point supplied by the singleton homomorphism. If \(r\) contains at least two points, Lemma 6.5 shows that every canonical bud point \(\Psi\in\widehat r\) satisfies
\[
\Psi\mathrel{R_c}\Psi.
\]

Because \(\Sigma\) is finite, there are only finitely many \(\Sigma\)-restrictions of canonical labels. Choose one member of \(\widehat r\) for each restriction realized there, choosing the reflexive \(\Psi\) as the representative of its restriction. Call the resulting finite set \(C\).

For distinct elements of \(C\), Lemma 6.5 gives modal accessibility in both directions, and the same lemma gives modal reflexivity when \(r\) is non-singleton. In the singleton case reflexivity was already arranged. Hence one may form a finite reflexive modal cluster \(A\) with one world for each member of \(C\), mapped homomorphically onto \(C\).

The restriction \(A\upharpoonright\Sigma\) is completely labelled. Since \(\Sigma\) contains only the atom \(p_\bullet\), it contains no modal formula capable of generating a modal defect and no implication or box formula capable of generating an intuitionistic defect. Thus \(A\) is a canonical \(\Sigma\)-tree.

Equip \(A\) with the identity intuitionistic relation. It is pointwise pivotal, and stability is vacuous because there are no intuitionistic defects. Hence \(A\) is stable.

Pick the world \(w\in A\) mapped to \(\Psi\). The full modal cluster of \(w\) maps exactly to \(C\), which is a set of \(\Sigma\)-representatives of \(\widehat r\), and there is no strict modal predecessor of \(w\). Thus \(w\) is a bud.

The modal cluster of \(A\) has no strict modal edges. Therefore
\[
\operatorname{dpt}_A(w)=0
\]
and Proposition 12.3 sets
\[
n=\max\{0,2\cdot1+1\}=3.
\]

Now fix
\[
m\ge1.
\]
Let \(B_m\) have \(m\) worlds with the complete reflexive modal relation, and map every world to \(\Psi\). Since
\[
\Psi\mathrel{R_c}\Psi,
\]
this is a canonical homomorphism.

Again, the \(\Sigma\)-labels are complete and no modal defect can occur, so \(B_m\) is a canonical \(\Sigma\)-tree.

Every point of \(B_m\) maps into \(r\), hence
\[
\rho(B_m)=r=\rho(w).
\]
A root of \(B_m\) maps to \(\Psi\), and
\[
h_A(w)=\Psi\mathrel{R_c}\Psi=h_{B_m}(r_m),
\]
so \(B_m\) is graftable onto \(w\).

There are no strict modal edges in \(B_m\). Hence
\[
\operatorname{hgt}(B_m)=0
\qquad\text{and}\qquad
\operatorname{wdt}(B_m)=0.
\]
The tall-petal clause is irrelevant. Therefore \(B_m\) is a \(3\)-petal.

Finally,
\[
m\ne k
\quad\Longrightarrow\quad
B_m\not\cong B_k
\]
because isomorphisms preserve cardinality.

Thus the set of all \(3\)-petals over \(w\) up to ordinary isomorphism contains
\[
\{B_m:m\ge1\},
\]
and is infinite.

Definition 8.2 explicitly extends grafting to a family \(\mathcal B\) only when \(\mathcal B\) is finite. Therefore Proposition 12.3's simultaneous all-petals graft is not licensed by that definition in the example above, and it does not establish finiteness of the purported flower.

## Verification

The current primary source is arXiv:2609.27078v2, dated 29 September 2026. Its version note says that several earlier inaccuracies were corrected, including the missing definition of \(\Sigma\)-trees, a reversed order relation in admissibility, and an ordinal correction.

The following load-bearing points were checked directly in the full PDF.

Definition 3.4 makes sprouts finite and defines height and width from strict modal structure rather than cluster cardinality.

Definition 7.1 allows canonical sprouts to map homomorphically into the canonical model; the map need not be injective.

Definition 8.2 defines \(A\sqcup_w B\) for one sprout and extends the notation to a set of sprouts only under an explicit finiteness hypothesis.

Definition 8.4 defines buds using sets of \(\Sigma\)-representatives.

Definition 12.1 bounds only petal height and width.

Proposition 12.3 sets \(\mathcal G\) equal to all \(n\)-petals over \(w\), up to isomorphism, and immediately forms \(A\sqcup_w\mathcal G\), without an intervening finiteness or quotient lemma.

Theorem 14.2 later applies Kruskal to trees whose modal clusters are labelled by the **set** of labels appearing in a cluster. That well-quasiorder argument can ignore multiplicities under its simulation notion, but it does not identify ordinary isomorphism types of clusters of different finite cardinalities.

The explicit family \(B_m\) exploits exactly this difference.

## Relationship to prior work

Fernández-Duque's paper gives a new model-theoretic Fine-selection proof of the finite model property for Fischer Servi-style \(\mathsf{IK4}\). The construction in Proposition 12.3 is load-bearing: Lemma 15.3 invokes a flower in the internal-resolution case, and the final finite-model argument iterates that defect-resolution machinery.

The source's current version already records several corrected inaccuracies, but its version note does not mention the all-petals finiteness issue.

A separate 2026 paper by Girlando, Kuznets, Marin, and Straßburger gives a constructive decision procedure producing finite countermodels for \(\mathsf{IS4}\) and \(\mathsf{IK4}\). That independent result supports the finite model property itself but does not supply the missing finiteness argument for this particular flower construction.

Targeted searches for Proposition 12.3, petals, flowers, bounded height and width, modal-cluster multiplicity, and finiteness of the all-petals family did not locate a published correction or equivalent diagnosis.

## Limitations

The finding targets the **construction in the proof** of Proposition 12.3, not the proposition's mathematical statement.

It does not prove that a finite subfamily of petals cannot suffice. In particular, a repair may be possible by quotienting cluster multiplicities, selecting reduced petals, or showing that Lemma 12.2 needs only finitely many simulation types rather than all ordinary isomorphism types.

It does not challenge the independently established finite model property of \(\mathsf{IK4}\).

It also does not assert that any later preprint version will retain the gap; the source is an early preprint whose author explicitly anticipates updates.

## References

[1] David Fernández-Duque, “Fine Selection for Intuitionistic Modal Logic,” arXiv:2609.27078v2, first posted 22 September 2026, v2 posted 29 September 2026.

[2] Marianna Girlando, Roman Kuznets, Sonia Marin, and Lutz Straßburger, “A decision procedure for intuitionistic modal logic IS4 (and IK4),” arXiv:2609.24922, first posted 21 September 2026.
