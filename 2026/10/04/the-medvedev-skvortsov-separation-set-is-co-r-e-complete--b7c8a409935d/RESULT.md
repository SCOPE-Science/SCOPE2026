# The Medvedev–Skvortsov separation set is co-r.e.-complete
## Finding

Let
\[
\mathrm{Sep}
=
\{\varphi:
\varphi\in\mathrm{ML}
\text{ and }
\varphi\notin\mathrm{Skvo}\},
\]
where \(\mathrm{ML}\) is Medvedev logic and \(\mathrm{Skvo}\) is Skvortsov logic.

Then
\[
\boxed{
\mathrm{Sep}\text{ is }\Pi^0_1\text{-complete under computable many-one reductions.}
}
\]

Equivalently, the set of formulas that witness the proper inclusion
\[
\mathrm{Skvo}\subsetneq\mathrm{ML}
\]
is co-r.e.-complete.

The hardness already holds on the canonical formulas produced by the tiling construction of Almeida and Knudstorp.

The key uniform device is a fixed finite strongly aperiodic Wang tileset \(A\). For an arbitrary finite Wang tileset \(W\), take the coordinatewise product
\[
W\otimes A.
\]
This product tiles the plane exactly when \(W\) does, but it can never tile periodically. Therefore every positive ordinary-tiling instance is converted uniformly into an aperiodic instance, and the source's canonical formula for that product lies in \(\mathrm{ML}\setminus\mathrm{Skvo}\).

## Assumptions and scope

The definitions of Medvedev logic, Skvortsov logic, Wang tilings, the tiling poset \(P_W\), the closed domain \(D_W\), and the canonical formula
\[
\alpha(P_W,D_W)
\]
are those of Almeida–Knudstorp.

The source proves the two semantic correspondences
\[
\alpha(P_W,D_W)\notin\mathrm{ML}
\quad\Longleftrightarrow\quad
W\text{ tiles periodically},
\]
and
\[
\alpha(P_W,D_W)\notin\mathrm{Skvo}
\quad\Longleftrightarrow\quad
W\text{ tiles the plane}.
\]

The construction of \(P_W,D_W\), and hence of the canonical formula, is effective in the finite tileset \(W\).

A finite strongly aperiodic Wang tileset means a finite tileset that tiles the plane but has no periodic tiling. Such tilesets are classical; one may fix, once and for all, the 11-tile Jeandel–Rao set.

Completeness is with respect to computable many-one reductions between standard effective codings of finite tilesets and propositional formulas.

No claim is made about polynomial-time complexity, formula-size optimality, or the complexity of deciding membership in the difference for restricted syntactic fragments.

## Proof

### Upper bound

Almeida–Knudstorp explicitly use the fact that refutability in \(\mathrm{ML}\) is recursively enumerable. Therefore theoremhood in \(\mathrm{ML}\) is co-r.e., equivalently a \(\Pi^0_1\) set of formula codes.

The same paper recalls Skvortsov's theorem that \(\mathrm{Skvo}\) is recursively axiomatizable. Hence theoremhood in \(\mathrm{Skvo}\) is r.e., so non-theoremhood in \(\mathrm{Skvo}\) is co-r.e.

Consequently
\[
\mathrm{Sep}
=
\mathrm{ML}\cap
(\mathrm{Form}\setminus\mathrm{Skvo})
\]
is an intersection of two co-r.e. sets. Thus
\[
\mathrm{Sep}\in\Pi^0_1.
\]

### A uniform aperiodicization of Wang tileability

Fix a finite strongly aperiodic Wang tileset
\[
A.
\]

For a finite Wang tileset \(W\), define
\[
W\otimes A
\]
as follows. A tile of the product is a pair
\[
(w,a)\in W\times A.
\]
Each of its four edge colors is the ordered pair consisting of the corresponding edge color of \(w\) and the corresponding edge color of \(a\).

A tiling by \(W\otimes A\) projects coordinatewise to a \(W\)-tiling and an \(A\)-tiling.

Conversely, if
\[
\tau_W:\mathbb Z^2\to W
\]
and
\[
\tau_A:\mathbb Z^2\to A
\]
are tilings, then
\[
z\longmapsto
(\tau_W(z),\tau_A(z))
\]
is a tiling by \(W\otimes A\).

Because \(A\) has at least one tiling,
\[
W\otimes A\text{ tiles}
\quad\Longleftrightarrow\quad
W\text{ tiles}.
\]

Moreover \(W\otimes A\) has no periodic tiling. If it had a periodic tiling, projection to the second coordinate would give a periodic \(A\)-tiling, contradicting strong aperiodicity.

Thus the computable map
\[
W\longmapsto W\otimes A
\]
takes arbitrary ordinary-tiling instances to tilesets that are either non-tiling or aperiodic, while preserving ordinary tileability exactly.

### Reduction to the logical separation set

For a finite tileset \(U\), write
\[
\alpha_U
=
\alpha(P_U,D_U)
\]
for the canonical formula of Almeida–Knudstorp.

Their Medvedev correspondence gives
\[
\alpha_U\notin\mathrm{ML}
\quad\Longleftrightarrow\quad
U\text{ tiles periodically}.
\]

Their Skvortsov correspondence gives
\[
\alpha_U\notin\mathrm{Skvo}
\quad\Longleftrightarrow\quad
U\text{ tiles the plane}.
\]

Set
\[
U=W\otimes A.
\]

Since \(U\) never tiles periodically,
\[
\alpha_U\in\mathrm{ML}
\]
for every \(W\).

Also,
\[
\alpha_U\notin\mathrm{Skvo}
\quad\Longleftrightarrow\quad
U\text{ tiles}
\quad\Longleftrightarrow\quad
W\text{ tiles}.
\]

Therefore
\[
\boxed{
W\text{ tiles the plane}
\quad\Longleftrightarrow\quad
\alpha_{W\otimes A}\in\mathrm{Sep}.
}
\]

The map
\[
W\longmapsto\alpha_{W\otimes A}
\]
is computable.

Berger's ordinary Wang tileability problem is \(\Pi^0_1\)-complete. Hence
\[
\mathrm{Sep}
\]
is \(\Pi^0_1\)-hard.

Together with the upper bound,
\[
\mathrm{Sep}
\]
is \(\Pi^0_1\)-complete.

## Verification

The proof has three independently checkable components.

First, the primary source states that \(\mathrm{ML}\)-refutability is recursively enumerable and recalls recursive axiomatizability of \(\mathrm{Skvo}\). This gives the \(\Pi^0_1\) upper bound.

Second, the product-tileset construction is verified directly from the edge-matching definition. Projection of a product tiling gives both coordinate tilings, and coordinatewise pairing of two tilings gives a product tiling. Periodicity is preserved by projection, so a strongly aperiodic second factor forbids periodic product tilings.

Third, the primary source's Theorems 2.16 and 2.19, together with its periodic and ordinary tiling equivalences proved in Sections 4 and 5, identify non-membership of the canonical formula with periodic and ordinary tileability, respectively.

Substituting the product tileset into these two equivalences yields the reduction exactly.

No finite experiment is used to infer an infinite tiling fact or an arithmetical-hierarchy classification.

## Relationship to prior work

Almeida–Knudstorp prove that \(\mathrm{ML}\) and \(\mathrm{Skvo}\) are undecidable and that
\[
\mathrm{Skvo}\subsetneq\mathrm{ML}.
\]
Their Corollary 5.7 obtains one separator from any fixed aperiodic tileset. The paper does not classify the complexity of the entire difference
\[
\mathrm{ML}\setminus\mathrm{Skvo}.
\]

Pawlowski independently proves that theoremhood in \(\mathrm{ML}\) is \(\Pi^0_1\)-complete. That result concerns all Medvedev-valid formulas; it does not determine the complexity of those formulas that additionally fail in \(\mathrm{Skvo}\).

The present theorem uses a fixed strongly aperiodic factor to turn every ordinary tileability instance into an aperiodic one. This upgrades the source's existence-of-a-separator argument to a uniform completeness reduction for the full separation set.

Jeandel–Rao provide a convenient fixed strongly aperiodic factor: an 11-tile Wang set that tiles the plane but admits no periodic tiling.

Targeted searches for the Medvedev–Skvortsov difference together with co-r.e. completeness, \(\Pi^0_1\)-completeness, aperiodicization, and product Wang tiles did not locate this classification.

## Limitations

The reduction establishes computability-theoretic completeness, not a useful finite-time complexity bound.

The theorem uses the full propositional languages of \(\mathrm{ML}\) and \(\mathrm{Skvo}\). It does not show that the separation remains \(\Pi^0_1\)-complete in a fixed-variable or other restricted fragment.

The aperiodic product construction is elementary and classical in spirit. The scientific content claimed here is the exact application of that uniform aperiodicization to the two different canonical-formula correspondences, thereby classifying the logical difference.

The result does not classify the complementary difference, which is empty because
\[
\mathrm{Skvo}\subseteq\mathrm{ML}.
\]

## References

[1] Rodrigo Nicolau Almeida and Søren Brinck Knudstorp, “Medvedev logic is undecidable,” arXiv:2609.13359, first posted 11 September 2026.

[2] Paweł Pawlowski, “Medvedev Logic is Not Decidable. It is \(\Pi^0_1\)-complete. Who Would Have Guessed?,” arXiv:2609.11576, first posted 10 September 2026.

[3] Emmanuel Jeandel and Michaël Rao, “An Aperiodic Set of 11 Wang Tiles,” arXiv:1506.06492, first posted 22 June 2015; *Advances in Combinatorics* (2021), Article 1.

[4] Robert Berger, “The Undecidability of the Domino Problem,” *Memoirs of the American Mathematical Society* 66 (1966).
