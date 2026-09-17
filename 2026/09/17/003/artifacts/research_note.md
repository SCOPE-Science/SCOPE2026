# SCOPE research note: the first unresolved minimum-indegree 3-kernel case

## Main theorem

Let `c_{delta,q}` be the least constant such that every finite simple digraph of minimum in-degree `delta` has a `q`-kernel of size at most `c_{delta,q}|V(D)|`, where a `q`-kernel is an independent set from which every vertex is reachable by a directed path of length at most `q`.

**Theorem.** Every digraph `D` with minimum in-degree at least 2 has a 3-kernel of size at most `|V(D)|/3`. Consequently `c_{2,3}=1/3`.

The lower bound is witnessed by the bidirected triangle.

## Auxiliary covering lemma

Let `F` be an undirected pseudoforest (parallel edges are allowed, loops are not). At each vertex `v`, let there be `p(v)` private tokens incident only with `v`, and suppose

`d_F(v) + p(v) >= 3` for every `v`.

Then one can choose at most

`(|E(F)| + sum_v p(v))/3`

objects, each object being either an edge of `F` (covering its two endpoints) or a private token (covering its one endpoint), so that every vertex of `F` is covered.

### Proof

Put `ell(d)=max(0,3-d)` and

`g(F)=3|V(F)|-|E(F)|-sum_v ell(d_F(v))`.

We claim `3 nu(F) >= g(F)`, where `nu(F)` is the matching number. It is enough to prove this componentwise.

For an isolated vertex, `g=0`. If a connected component has no leaf and has at least two vertices, pseudoforest sparsity gives `|E|<=|V|`, while minimum degree at least 2 gives `2|E|>=2|V|`; hence equality holds and every degree is 2. The component is a cycle (a 2-cycle from parallel edges is allowed). Thus `g=|V|` and `3 floor(|V|/2) >= |V|`.

Otherwise choose a leaf `x` with neighbor `y`, and delete `x,y`, obtaining a (possibly disconnected) pseudoforest `F'`. Let `d=d_F(y)`. If `m_z` is the multiplicity of edges from `y` to a remaining neighbor `z`, then deleting `y` changes `ell(d_F(z))` by at most `m_z`; hence, with `A <= sum_z m_z=d-1`,

`g(F)-g(F') = 4-d-ell(d)+A <= 3`.

By induction, a matching of `F'` together with `xy` has size at least `g(F)/3`. This proves the claim.

For each nonisolated component, a maximum matching can be extended to an edge cover using at most `|V|-nu(F)` edges; each isolated vertex can instead be covered by one private token (it has at least three). Therefore a cover exists with at most

`|V|-nu(F) <= (|E(F)|+sum_v ell(d_F(v)))/3 <= (|E(F)|+sum_v p(v))/3`.

## Proof of the theorem

Use Algorithm 1 of Boyer--Burnham--Cerna--Hartke--Hollars--Jeffries--Miyasaki--Timofeyev with parameters `ell=1, k=2`. It produces a partition

`V(D)=R disjoint_union A disjoint_union B`

with these properties:

1. `D[R]` is acyclic.
2. `2|R| <= |B|`.
3. Every vertex of `A` has at most one out-neighbor in `A`.
4. Every vertex of `B` is at directed distance at most 1 from `R`.
5. No arc goes from `R` to the final set `A` (such an out-neighbor would have been deleted from `A` when its tail entered `R`).

Let

`X={x in A : N_B^-(x)=empty}`.

For `x in X`, minimum in-degree at least 2 and property 5 imply that all in-neighbors of `x` lie in `A`; hence `d_A^-(x)>=2`. Define

`C_x={x} union N_A^-(x)`.

Then `|C_x|>=3`.

Each `a in A` belongs to at most two of the sets `C_x`: it can belong to `C_a` (only if `a in X`) and, because `d_A^+(a)<=1`, to at most one further `C_x` via an arc `a->x`.

Build an incidence multigraph `F` whose vertices are the sets `C_x` (`x in X`). An element `a in A` appearing in two `C_x`'s becomes an edge between those two vertices; an element appearing in exactly one becomes a private token. Elements appearing in none are ignored. Every edge of `F` is naturally oriented from `C_a` to `C_y` when `a->y`; therefore every vertex of this oriented incidence graph has out-degree at most one. Hence the underlying multigraph `F` is a pseudoforest. At each `C_x`, incident edges plus private tokens are exactly the elements of `C_x`, so their number is at least 3.

By the covering lemma there is a hitting set `P subseteq A` meeting every `C_x` with

`|P| <= |A|/3`.

Delete redundant elements until `P` is inclusion-minimal. Then `D[P]` is acyclic. Indeed, if `P` contained a directed cycle `p_1->...->p_t->p_1`, the final-set bound `d_A^+<=1` implies that `p_i` can hit only `C_{p_i}` (if `p_i in X`) and `C_{p_{i+1}}` (if `p_{i+1} in X`). The former is also hit by `p_{i-1}` and the latter by `p_{i+1}`, contradicting inclusion-minimality after deleting `p_i`.

There are no arcs from `R` to `P subseteq A`; hence `D[R union P]` is acyclic. Moreover:

- `R` is reached in 0 steps;
- every `b in B` is reached from `R` in at most 1 step;
- every `a in A\X` has an in-neighbor in `B`, hence is reached from `R` in at most 2 steps;
- every `x in X` is hit by `P`, so either `x in P` or some `p in P` has `p->x`, hence `x` is reached from `P` in at most 1 step.

Thus `R union P` is a 2-prekernel. Lemma 4.2 of Boyer et al. converts it to a 3-kernel `Q subseteq R union P`. Finally,

`|V(D)|=|R|+|A|+|B| >= 3|R|+|A|`,

so

`|Q| <= |R|+|P| <= |R|+|A|/3 <= |V(D)|/3`.

The bidirected triangle has minimum in-degree 2 and every 3-kernel has size at least 1, yielding `c_{2,3}>=1/3`; hence equality.

## Computational checks

The accompanying Python script exhaustively verifies:

- the theorem for every simple digraph with minimum in-degree at least 2 on 3, 4, and 5 vertices (1, 256, and 161051 digraphs respectively under an incoming-neighborhood encoding), and
- the key functional-digraph hitting-set lemma for every loopless partial functional digraph on at most 7 vertices (up to 823543 maps at n=7).

These computations are checks only; the proof above is non-computational.

## Literature anchors

- G. Boyer et al., *Small q-kernels in digraphs with minimum in-degree delta*, arXiv:2606.16971 (2026). Their Conjecture 7.1 predicts `c_{delta,q}=1/(delta+1)` for all `delta>=1, q>=3`, and explicitly identifies `delta=2` as the first place to check. The paper's current arXiv record is v1.
- I. Penev, M. Stein, A. Trujillo-Negrete, *Small q-kernels in digraphs*, arXiv:2608.00825 (2026), studies different Spiro questions (cycle/girth, strong connectivity, bipartite cases), not the minimum-in-degree constants.
