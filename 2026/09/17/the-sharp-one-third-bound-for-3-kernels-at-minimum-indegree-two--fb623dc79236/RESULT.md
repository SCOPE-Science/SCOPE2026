# The sharp one-third bound for 3-kernels at minimum indegree two

## Claim and definitions

Let `c_{δ,q}` be the least constant such that every finite simple digraph of minimum in-degree at least `δ` has a `q`-kernel of size at most `c_{δ,q}|V(D)|`, where a `q`-kernel is an independent set from which every vertex is reachable by a directed path of length at most `q`.

**Theorem.** Every finite simple digraph `D` with minimum in-degree at least 2 has a 3-kernel of size at most `|V(D)|/3`. Consequently, `c_{2,3}=1/3`.

The lower bound is witnessed by the bidirected triangle.

## Proof outline

Apply Algorithm 1 of Boyer--Burnham--Cerna--Hartke--Hollars--Jeffries--Miyasaki--Timofeyev with parameters `ell=1, k=2`. It yields a partition `V(D)=R ⊔ A ⊔ B` with:

1. `D[R]` acyclic;
2. `2|R| <= |B|`;
3. every `a in A` having at most one out-neighbor in `A`;
4. every `b in B` at directed distance at most one from `R`; and
5. no arc from `R` to the final set `A`.

Let `X={x in A : N_B^-(x)=empty}` and `C_x={x} ∪ N_A^-(x)`. For each `x in X`, minimum in-degree at least two and the absence of arcs `R -> A` imply `|C_x| >= 3`. Each `a in A` belongs to at most two of the sets `C_x`: possibly `C_a`, and at most one additional `C_x` through the unique possible `A`-outneighbor of `a`.

Construct an incidence multigraph `F` whose vertices are the sets `C_x`. An element appearing in two sets becomes an edge joining those two vertices; an element appearing in exactly one set becomes a private token at the corresponding vertex. Orient each edge according to the underlying arc `a -> x`. Every vertex then has outdegree at most one, so the underlying multigraph is a pseudoforest.

Use the following covering lemma.

**Pseudoforest covering lemma.** If `F` is a pseudoforest, parallel edges allowed and loops forbidden, with `p(v)` private tokens at each vertex and `d_F(v)+p(v) >= 3` for every vertex, then all vertices can be covered by at most

`(|E(F)| + sum_v p(v))/3`

objects, where an edge covers its two endpoints and a private token covers its one endpoint.

The proof reduces the bound to

`3 nu(F) >= 3|V(F)| - |E(F)| - sum_v max(0,3-d_F(v))`,

verified componentwise: cycles are the leafless base case, and deleting a leaf together with its neighbor decreases the right side by at most three.

Translating the cover back gives a hitting set `P subset A` meeting every `C_x` with `|P| <= |A|/3`. Delete redundant elements until `P` is inclusion-minimal. Then `D[P]` is acyclic: a directed cycle in `P` would make every cycle vertex redundant because the outdegree-one structure means its possible hits are already hit by neighboring cycle vertices.

Since there are no arcs from `R` to `P`, `D[R ∪ P]` is acyclic. Moreover every vertex of `D` is reached from `R ∪ P` within two steps: vertices of `B` are reached from `R` in at most one step; vertices of `A\X` have an in-neighbor in `B`; and vertices of `X` are hit by `P`. Thus `R ∪ P` is a 2-prekernel. Boyer et al.'s Lemma 4.2 converts it to a contained 3-kernel `Q`.

Finally,

`|Q| <= |R| + |P| <= |R| + |A|/3 <= (|R|+|A|+|B|)/3 = |V(D)|/3`,

using `2|R| <= |B|`.

The bidirected triangle has minimum in-degree two and every 3-kernel has size at least one, so equality follows.

## Reproducibility

`artifacts/verify.py` exhaustively checks every loopless simple digraph with minimum in-degree at least two on 3, 4 and 5 vertices, totaling 1, 256 and 161051 digraphs respectively. It also checks the structural partial-functional-digraph hitting lemma for all orders through 7, including 823543 maps at order 7.

These computations are checks only; the proof is non-computational.

## Prior work and scope

The primary anchor is Boyer et al., *Small q-kernels in digraphs with minimum in-degree delta*, arXiv:2606.16971 (2026). That paper conjectures `c_{δ,q}=1/(δ+1)` for all `δ>=1, q>=3`, reduces the issue to `q=3`, and identifies `δ=2` as the first case to check. Its general bound gives only `c_{2,3} <= 1/2`.

Penev, Stein and Trujillo-Negrete, *Small q-kernels in digraphs*, arXiv:2608.00825 (2026), studies different q-kernel questions and does not appear to cover these minimum-in-degree constants.

To the best of the same-model review's searches during the run, no equivalent or stronger theorem covering `c_{2,3}=1/3` was found.

## Limitations

The originality assessment is qualified. A recent unindexed manuscript, private draft, or newer unindexed revision of the primary work could still supply prior coverage. No independent review is claimed.
