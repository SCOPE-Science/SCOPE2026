# Every finite stage of the internal forcing logic hierarchy is strict
## Finding

For \(n\ge1\), write
\[
L_n=
\operatorname{Log}^{\#}_{\subseteq}(\mathcal P(n))
\]
for the nonzero-state submodel logic introduced by Jockwich, Tarafder, and Venturi.

Their Lemma 6.13 proves the inclusions
\[
L_{n+1}\subseteq L_n.
\]
The inclusions are in fact all strict:
\[
\boxed{
L_{n+1}\subsetneq L_n
\qquad(n\ge1).
}
\]

The finite-frame obstruction behind strictness has an exact closed form.

Let
\[
G_n=
\bigl(
\mathcal P([n])\setminus\{\varnothing\},R
\bigr),
\qquad
A\,R\,B
\Longleftrightarrow
A\cap B\ne\varnothing.
\]
This is the co-consistency frame of the nonzero part of \(\mathcal P(n)\).

Among all generated subframes of all induced subframes of \(G_n\), the largest reflexive complete frame obtainable as a bounded-morphic image has exactly
\[
2^{n-1}
\]
worlds.

Equivalently, if a reflexive undirected graph is viewed with domination including the vertex itself, the maximum domatic number among all induced subgraphs of \(G_n\) is
\[
\boxed{2^{n-1}}.
\]

This number is attained already by \(G_n\) itself.

Consequently, if
\[
r_n=2^{n-1}+1,
\]
then the Jankov--Fine obstruction for \(K_{r_n}^{\mathrm r}\), after an explicit finite propositional coordinate coding, separates the adjacent logics:
\[
\sigma_n\in L_n\setminus L_{n+1}.
\]

Thus the finite hierarchy displayed in the source is not merely descending toward \(\mathsf{KTB}\); every adjacent finite stage is genuinely different.

## Assumptions and scope

The logic \(L_n\) is the source paper's translation-based nonzero-state submodel logic. Its models have a nonempty state set
\[
W\subseteq\mathcal P([n])^+
\]
and accessibility
\[
A\,R\,B
\Longleftrightarrow
A\cap B\ne\varnothing.
\]
For an atomic modal variable \(p\), a translation supplies a Boolean value \(v(p)\subseteq[n]\), and
\[
A\models p
\Longleftrightarrow
A\subseteq v(p).
\]

A bounded morphism is used in the standard modal-frame sense. For a map onto a reflexive complete frame, the back condition says exactly that every fiber is a dominating set in the source frame. Hence a bounded morphism onto \(K_r^{\mathrm r}\) is equivalent to a partition into \(r\) nonempty dominating sets.

The quantitative theorem ranges over arbitrary induced subframes and their generated subframes, because this is the exact frame condition entering the Jankov--Fine characterization used in the source.

The separating formula \(\sigma_n\) is not claimed to be size-optimal.

## Proof

### Step 1: complete bounded-morphic quotients are domatic partitions

Let \(H\) be a reflexive symmetric frame and let
\[
h:H\longrightarrow K_r^{\mathrm r}
\]
be surjective.

Because the target relation is universal, the forth condition is automatic. The back condition says that for every source world \(x\) and every target world \(j\), there is an \(H\)-successor \(y\) of \(x\) with
\[
h(y)=j.
\]
Thus every fiber
\[
h^{-1}(j)
\]
dominates \(H\).

Conversely, a partition of \(H\) into \(r\) nonempty dominating sets defines a bounded morphism onto \(K_r^{\mathrm r}\) by sending each block to its label.

So the largest reflexive complete bounded-morphic quotient of \(H\) has order equal to the domatic number of \(H\).

### Step 2: a \(2^{n-1}\)-block construction

Partition the full power set \(\mathcal P([n])\) into complementary pairs
\[
\{A,[n]\setminus A\}.
\]
There are exactly
\[
2^{n-1}
\]
such pairs.

After deleting the empty state, the pair
\[
\{\varnothing,[n]\}
\]
becomes the singleton block
\[
\{[n]\},
\]
and every other complementary pair remains a two-element block.

Every such block dominates \(G_n\). Indeed, let \(S\ne\varnothing\). For a complementary pair
\[
\{A,A^c\},
\]
choose \(s\in S\). Then \(s\) belongs to \(A\) or to \(A^c\), so \(S\) intersects at least one member of the block. The singleton \(\{[n]\}\) plainly dominates every state.

Hence
\[
G_n
\]
has a domatic partition with
\[
2^{n-1}
\]
blocks.

### Step 3: Hall upper bound for every induced subgraph

Let
\[
W\subseteq\mathcal P([n])\setminus\{\varnothing\}
\]
and suppose
\[
C_1,\ldots,C_r
\]
is a domatic partition of the induced frame on \(W\).

Call an unordered complementary pair
\[
\tau_A=\{A,A^c\}
\]
a **complement token**. There are \(2^{n-1}\) tokens.

Build a bipartite incidence graph from the blocks \(C_i\) to the complement tokens: connect \(C_i\) to \(\tau_A\) when \(C_i\) contains \(A\) or \(A^c\).

We verify Hall's condition.

Take any subcollection \(J\) of the domatic blocks. Let \(s\) be the number of singleton blocks in \(J\).

If
\[
C_i=\{A\}
\]
is a singleton dominating block, then
\[
A^c\notin W.
\]
Otherwise the state \(A^c\) would be disjoint from the only member \(A\) of \(C_i\), contradicting domination. Therefore the complement token containing \(A\) occurs nowhere else in \(W\). Distinct singleton blocks give distinct such private tokens.

The remaining
\[
|J|-s
\]
blocks each contain at least two vertices. Because the blocks are disjoint, together they contain at least
\[
2(|J|-s)
\]
distinct subsets. A complement token contains at most two subsets, so these nonsingleton blocks touch at least
\[
|J|-s
\]
additional tokens. None of those tokens is one of the private singleton tokens.

Thus every subcollection \(J\) touches at least
\[
s+(|J|-s)=|J|
\]
tokens.

By Hall's marriage theorem, the domatic blocks admit an injective assignment to complement tokens. Since there are only
\[
2^{n-1}
\]
tokens,
\[
r\le2^{n-1}.
\]

The same bound applies to every generated subframe of every induced subframe, because such a generated subframe is itself an induced frame on a subset of the vertices.

Together with Step 2,
\[
\max r=2^{n-1}.
\]

### Step 4: frame obstruction at stage \(n\)

Put
\[
r_n=2^{n-1}+1.
\]

By Step 3, no generated subframe of any induced subframe of \(G_n\) has
\[
K_{r_n}^{\mathrm r}
\]
as a bounded-morphic image.

The source paper's Jankov--Fine criterion therefore gives
\[
\chi_{K_{r_n}^{\mathrm r}}
\]
as frame-valid on every induced subframe of \(G_n\).

Any propositional substitution instance of a frame-valid modal formula is again frame-valid. Hence every propositional substitution instance of
\[
\chi_{K_{r_n}^{\mathrm r}}
\]
belongs to \(L_n\).

### Step 5: an explicit failure at stage \(n+1\)

Let
\[
X=[n+1].
\]
The complement-pair partition from Step 2 gives
\[
2^n
\]
dominating blocks of \(G_{n+1}\), hence a bounded morphism
\[
G_{n+1}\twoheadrightarrow K_{2^n}^{\mathrm r}.
\]

Since
\[
r_n=2^{n-1}+1\le2^n,
\]
merge some of those dominating blocks to obtain a partition into exactly \(r_n\) nonempty dominating blocks
\[
F_1,\ldots,F_{r_n}.
\]
This gives a bounded morphism
\[
h:G_{n+1}\twoheadrightarrow K_{r_n}^{\mathrm r}.
\]

It remains to realize the usual Jankov--Fine fiber valuation inside the source paper's restricted translation semantics.

Introduce coordinate variables
\[
q_1,\ldots,q_{n+1}
\]
and choose a translation with Boolean values
\[
v(q_i)=X\setminus\{i\}.
\]
Such Boolean values are realizable by parameter translations in the source semantics.

For each
\[
A\subseteq X,
\]
define the propositional formula
\[
\theta_A
=
\left(
\bigwedge_{i\in A}\neg q_i
\right)
\wedge
\left(
\bigwedge_{i\notin A}q_i
\right).
\]
At a nonempty state \(B\subseteq X\),
\[
B\models q_i
\Longleftrightarrow
B\subseteq X\setminus\{i\}
\Longleftrightarrow
i\notin B.
\]
Therefore
\[
B\models\theta_A
\Longleftrightarrow
B=A.
\]

For each bounded-morphism fiber \(F_j\), put
\[
\Theta_j=
\bigvee_{A\in F_j}\theta_A.
\]
Then \(\Theta_j\) defines exactly the fiber \(F_j\) on the full frame \(G_{n+1}\).

Let the label variables of the Jankov--Fine formula for \(K_{r_n}^{\mathrm r}\) be
\[
p_1,\ldots,p_{r_n}.
\]
Define
\[
\sigma_n
=
\chi_{K_{r_n}^{\mathrm r}}
[p_j:=\Theta_j]_{j=1}^{r_n}.
\]

By Step 4,
\[
\sigma_n\in L_n.
\]

On \(G_{n+1}\), under the coordinate translation above, the formulas \(\Theta_j\) reproduce exactly the standard fiber valuation witnessing the bounded morphism \(h\). The Jankov--Fine diagram is therefore true at a preimage of its root, so
\[
\sigma_n\notin L_{n+1}.
\]

Hence
\[
L_{n+1}\subsetneq L_n
\]
for every
\[
n\ge1.
\]

## Verification

The symbolic proof is complete for every \(n\).

The bundled checker independently performs three finite tests.

First, for
\[
1\le n\le8,
\]
it constructs the complement-pair partition of \(G_n\), verifies that it has exactly
\[
2^{n-1}
\]
blocks, and verifies directly that every block dominates every vertex.

Second, for
\[
n=1,2,3,
\]
it exhaustively enumerates every nonempty induced subgraph and every set partition of its vertices. It computes the exact domatic number of each induced subgraph and confirms that the largest value is
\[
1,2,4,
\]
respectively.

Third, for
\[
1\le n\le7,
\]
it checks the propositional coordinate coding:
\[
\theta_A
\]
holds at a nonempty state \(B\) exactly when
\[
A=B.
\]
It also constructs the complement-fiber bounded morphism and verifies the back condition for the relevant complete quotient sizes.

The computation corroborates the proof; the arbitrary-\(n\) upper bound is the Hall argument, not an extrapolation from enumeration.

## Relationship to prior work

Jockwich, Tarafder, and Venturi define the fixed-algebra submodel logics
\[
\operatorname{Log}^{\#}_{\subseteq}(B)
\]
and prove that Boolean subalgebra embeddings reverse inclusion of these logics. For finite complete Boolean algebras this gives the chain
\[
L_1\supseteq L_2\supseteq\cdots\supseteq\mathsf{KTB}.
\]

The paper explicitly describes this as a descending chain whose limit is \(\mathsf{KTB}\), but it does not state that every finite adjacent inclusion is strict.

The same paper introduces Jankov--Fine formulas as a method for finding extra principles at a fixed finite stage. Its worked example for \(n=2\) excludes a reflexive triangle using the absence of three pairwise-intersecting subsets. The present result replaces that one-stage obstruction by a uniform exact invariant:
\[
2^{n-1}
\]
is the maximum order of any reflexive complete bounded-morphic quotient obtainable anywhere inside the \(n\)-atom compatibility frame.

The strictness proof also addresses a feature specific to the translation semantics: arbitrary Jankov--Fine label valuations are not automatically atomic translations. The coordinate formulas \(\theta_A\) explicitly realize arbitrary finite fiber valuations as propositional combinations of translated atoms.

Targeted searches for strictness of the fixed-\(\mathcal P(n)\) hierarchy, domatic numbers of these compatibility frames, and complete bounded-morphic quotients did not locate the theorem above.

## Limitations

The theorem separates adjacent finite stages but does not axiomatize any individual \(L_n\).

The separating formula obtained from a Jankov--Fine formula and coordinate coding is finite but can be very large. No minimal-variable, minimal-depth, or minimal-length separator is claimed.

The exact domatic theorem uses the full finite Boolean power-set structure and its complement pairing. It is not asserted for arbitrary finite Boolean substructures presented without all complements.

The graph-theoretic invariant may have appeared under unrelated terminology in older domination or intersection-graph literature; no equivalent statement was located in the checked sources.

## References

[1] Santiago Jockwich, Sourav Tarafder, and Giorgio Venturi, “The Internal Modal Logic of Forcing,” arXiv:2607.25977, first posted 28 July 2026.

[2] Patrick Blackburn, Maarten de Rijke, and Yde Venema, *Modal Logic*, Cambridge Tracts in Theoretical Computer Science 53, Cambridge University Press, 2001.

[3] Teresa W. Haynes, Stephen T. Hedetniemi, and Peter J. Slater, *Fundamentals of Domination in Graphs*, Marcel Dekker, 1998.
