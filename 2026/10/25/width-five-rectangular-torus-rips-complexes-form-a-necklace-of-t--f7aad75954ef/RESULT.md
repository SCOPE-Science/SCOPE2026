# Width-five rectangular torus Rips complexes form a necklace of two-spheres

## Finding
For every integer \(n\ge7\), let \(G_n=C_5\square C_n\) carry its graph shortest-path metric. The inclusive radius-two Vietoris--Rips complex satisfies
\[
X_n=\operatorname{VR}_{\le2}(G_n)\simeq S^1\vee\bigvee^n S^2.
\]
Explicitly, \(20n\) elementary simplicial collapses take \(X_n\) onto a cyclic necklace of \(n\) two-sphere complexes, each isomorphic to \(\operatorname{Ind}(C_{10})\). In particular its positive-degree integral homology is \(H_1(X_n;\mathbb Z)\cong\mathbb Z\), \(H_2(X_n;\mathbb Z)\cong\mathbb Z^n\), with all other reduced integral homology zero. The nonempty face vector indexed by cardinality one through five is \((5n,30n,55n,35n,6n)\).

## Assumptions and scope
The vertex set is \(\mathbb Z/5\mathbb Z\times\mathbb Z/n\mathbb Z\). Distances are the sum of cyclic distances \(d_5(a,b)+d_n(j,k)\). Faces are nonempty finite vertex sets of pairwise distance at most two. Let \(S_j\) be the full induced subcomplex on columns \(j,j+1\), and put \(U_n=\bigcup_j S_j\). The condition \(n\ge7\) excludes short cyclic wraparound and ensures uniqueness of the middle column for a pair of columns at distance two.

## Proof
**Outside-slab face classification.** A face not contained in two consecutive columns has vertices in columns \(j-1\) and \(j+1\) at cyclic distance two. Those endpoints must share the same first coordinate \(a\), since their total distance is at most two. Denote their pair by \(B_{j,a}=\{(a,j-1),(a,j+1)\}\). Any additional vertex must be in the unique intervening column \(j\) and have first coordinate \(a-1\), \(a\), or \(a+1\). Conversely all such vertices are mutually compatible in the width-five cycle, whose diameter is two. Thus every face outside \(U_n\) is uniquely of the form
\[
B_{j,a}\cup T,\qquad T\subseteq\{(a-1,j),(a,j),(a+1,j)\}.
\]
A second endpoint pair cannot occur in such a face: an endpoint column contains only the original endpoint, and the other allowable vertices lie in the middle column. The middle column is unique for \(n\ge7\). Hence these sets partition all faces outside the slabs into \(5n\) disjoint eight-face families.

**Explicit collapses.** For each \((j,a)\), put \(v=(a,j)\), \(p=(a-1,j)\), and \(q=(a+1,j)\). Process \(T=\{p,q\},\{p\},\{q\},\varnothing\) in that order. At each step delete the codimension-one pair
\[
\bigl(B_{j,a}\cup T,\ B_{j,a}\cup T\cup\{v\}\bigr).
\]
The first member is free: all alternative cofaces strictly extending \(T\) have been removed at earlier steps; the only remaining coface is the displayed second member. There are no coface interactions across different endpoint pairs by uniqueness of the outside-slab classification. The four pairs for each of \(5n\) endpoint pairs remove all \(40n\) outside-slab faces, yielding \(X_n\searrow U_n\) in exactly \(20n\) elementary collapses.

**Topology of each slab.** Each five-vertex column is a complete graph in the radius-two graph because the diameter of \(C_5\) is two. Between neighboring columns, the only forbidden pairs have first coordinates at cyclic distance two. The forbidden-pair graph on the ten vertices is a single ten-cycle: each vertex has two forbidden neighbors in the opposite column, and steps by two generate all five first coordinates. Therefore each \(S_j\) is the independence complex of \(C_{10}\). The standard three-periodic independence-complex calculation for cycles gives \(\operatorname{Ind}(C_{10})\simeq S^2\); equivalently, use the elementary deletion-and-link recurrence for cycles and paths. The slab has nonempty face vector \((10,35,50,25,2)\).

**Cyclic gluing.** Only successive slabs intersect, and \(S_j\cap S_{j+1}\) is the full simplex on the five vertices of column \(j+1\), hence a contractible four-simplex. Non-successive slabs and all triple intersections are empty. Gluing the first \(n-1\) slabs along their single contractible overlaps gives a wedge of \(n-1\) two-spheres. The final slab meets the existing union in two disjoint contractible simplices, adding one further two-sphere and one independent loop to the homotopy pushout. Thus \(U_n\simeq S^1\vee\bigvee^n S^2\), and so does \(X_n\). This establishes integral homology, not merely field ranks.

**Face vector.** The \(n\) slabs contribute \(n(10,35,50,25,2)\); their \(n\) adjacent intersections contribute \(n(5,10,10,5,1)\) for subtraction. The outside-slab face families contribute \(5n(0,1,3,3,1)\). Adding gives \((5n,30n,55n,35n,6n)\), with Euler characteristic \(n\), consistent with the homotopy equivalence.

## Verification
Run `python3 artifacts/verify.py 11` using only the Python standard library. The verifier independently generates all pairwise-distance cliques, checks the face-vector formula, confirms each two-column forbidden-pair graph is connected and 2-regular on ten vertices, checks every slab overlap, and tests each of the \(20n\) proposed elementary collapses against **all** remaining cofaces. The completed package contains its successful execution output for every \(7\le n\le11\). These finite checks complement rather than replace the uniform proof.

## Relationship to prior work
Adams et al. [1] compute the scale-two complex of the *square* \(5\times5\) torus (nine two-spheres) and study square grids, but that fixed-square result does not determine the rectangular family \(5\times n\) for \(n\ge7\). The published width-four rectangular result [2] concerns \(C_4\square C_n\) and yields \(S^1\vee\bigvee^nS^3\); its analogous local slab is the boundary of a four-cross-polytope, whereas the width-five slab here is \(\operatorname{Ind}(C_{10})\simeq S^2\), so the new homological dimension and local classification are not implied by replacing a parameter in that theorem. Adamaszek [3] studies clique complexes of powers of individual cycle graphs; the cycle computation supports the local input but does not supply the rectangular cyclic gluing.

## Limitations
The statement assumes \(n\ge7\), the intrinsic graph metric, and inclusive threshold two. It makes no claim about shorter rectangles, other Rips radii, or wider grids. No independent external audit has been performed. A logically equivalent unindexed prior statement remains a bibliographic risk.

## References
[1] H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng, J. Sterling, *Vietoris--Rips complexes of torus grids*, arXiv:2502.07134 (first posted 2025-02-10), especially the \(5\times5\) square case and Sections 5--6. https://arxiv.org/abs/2502.07134

[2] *A thin toroidal grid has scale-two Rips type \(S^1\vee\bigvee^n S^3\)*, publicly available `RESULT.md`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-thin-toroidal-grid-has-scale-two-rips-type-s-1-vee-bigvee-ns-3--a2c9f7beb39c

[3] M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (first posted 2011-04-03), the cycle-power homotopy calculations. https://arxiv.org/abs/1104.0433
