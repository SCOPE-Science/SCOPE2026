# Leaf-color normal form and sharp star extremality for bounded morphisms to a fan

## Finding

For a nonempty finite rooted tree \(T\) with the reflexive ancestor order, and a reflexive fan \(F_k\) with one bottom and \(k\ge2\) labeled incomparable maxima, write \(N_k(T)\) for the number of bounded morphisms \(T\to F_k\), including constant maps. The structural claims are a bijection describing the individual maps and a sharp shape characterization at fixed leaf count:

- **Leaf-color bijection.** A leaf coloring by the \(k\) maxima extends to a bounded morphism exactly when the colors in each descendant subtree form either a singleton or the full palette. The extension is unique: a vertex maps to its subtree's unique color in the first case and to the bottom in the second.
- **Sharp star extremality.** If \(T\) has \(\ell\) leaves and \(k\ge3\), then \(k\le N_k(T)\le k+k!S(\ell,k)\), where \(S\) denotes a Stirling number of the second kind and is zero when \(\ell<k\). If \(\ell\ge k\), the upper bound is attained exactly when suppressing every unary vertex leaves the rooted star with \(\ell\) leaves. If \(\ell<k\), all maps are constant; if \(k=2\), all tree shapes with a fixed \(\ell\) have \(N_2(T)=2^\ell\).

The specialized recurrence, degree threshold and profile examples below are consequences, not separate claims of novelty for bounded-morphism counting.

## Assumptions and scope

The accessibility relation on \(T\) is the reflexive transitive ancestor order, not the parent-edge relation. Denote the descendant subtree of \(x\), including \(x\), by \(T_x\). For \(F_k\) the only strict comparisons are \(0<i\) for \(i=1,\ldots,k\). A map \(f\) is bounded when \(f(T_x)=\{y\in F_k:f(x)\le y\}\) for every \(x\); the two inclusions are the forth and back conditions. The shapes are unordered, but the counts distinguish functions on the actual vertices and the labels of the target maxima. Suppression of unary vertices includes removal of any unary stem above the first branch.

## Proof

**Leaf-color bijection.** Leaves necessarily map to maxima, because their successor sets are singletons. If a vertex maps to a maximal color, all descendant leaves have that color. If it maps to \(0\), back supplies some vertex below it mapping to each maximal color; below each such vertex is a leaf mapping to the same color. Thus the leaf set below any vertex has a singleton or full palette, determining its value. Conversely, under this palette condition, the specified extension satisfies forth because descendant palettes are nested under inclusion. At a top-valued vertex back is witnessed by the vertex itself, and at a bottom-valued vertex all tops are witnessed by leaves and the bottom by the vertex itself. This proves the bijection.

**Sharp extremality.** At the root the coloring is monochromatic or onto. There are \(k\) monochromatic colorings and \(k!S(\ell,k)\) onto colorings of the leaves, giving the upper bound. Removing a unary vertex does not change validity of a coloring, since its palette test duplicates that of its child. In the reduced star every proper subtree contains one leaf, so all globally onto colorings pass the local tests. If the reduced tree is not a star and \(\ell\ge k\ge3\), some proper child subtree of a branching vertex contains \(s\ge2\) leaves and has \(t=\ell-s\ge1\) leaves outside. Choose \(h=\max(2,k-t)\); then \(2\le h\le\min(s,k-1)\) and \(1\le k-h\le t\). Color the inside leaves onto an \(h\)-color set and the outside leaves onto the remaining \(k-h\) colors. This globally onto coloring fails the local test at the chosen subtree, proving strictness. If \(\ell<k\), onto colorings are impossible. If \(k=2\), every nonempty palette already has size one or two, so all \(2^\ell\) leaf colorings are valid.

## Counting consequences and examples

For a leaf, \(N_k=k\). For an internal vertex with \(d\) child subtrees \(T_i\), the specialization of the general subtree recurrence in [1] is
\[
N_k(T)=k+\prod_{i=1}^d N_k(T_i)-k^d+k!S(d,k).
\]
Indeed the three terms by type of coloring are \(k\) monochromatic at the root, \(\prod_iN_k(T_i)-k^d\) assignments having a full-palette child, and \(k!S(d,k)\) assignments all of whose child subtrees are monochromatic but collectively use all colors. In the general inclusion–exclusion formula of [1], the empty excluded-child set contributes \(\prod_iN_k(T_i)\); a nonempty excluded set of size \(j\) forces each child into one of \(k-j\) tops. Its summed contribution over all nonempty sets is \(k!S(d,k)-k^d\). Adding the \(k\) constant maps to the surjective count gives the same recurrence.

Writing \(\Delta\) for maximum child count, the excess \(N_k(T)-k\) is positive exactly when \(2\le k\le\Delta\): in the recurrence positivity comes from either a positive excess in a child or \(d\ge k\). Thus the largest index \(k\) with positive excess identifies \(\Delta\) if \(\Delta\ge2\); if there is none, \(\Delta\le1\). The \(k=2\) entry determines the leaf count. If there is exactly one ternary vertex and all other vertices have at most two children, it contributes excess 6 at \(k=3\), and each of its \(b\) binary ancestors multiplies the excess by 3, while unary ancestors leave it unchanged. This gives \(N_3(T)=3+6\cdot3^b\). Full-binary shapes with \(\ell\) leaves all have profile \(N_2=2^\ell\), \(N_k=k\) for \(k\ge3\); there are distinct such shapes for every \(\ell\ge4\), for example root splits of sizes \(\lfloor\ell/2\rfloor,\lceil\ell/2\rceil\) versus \(1,\ell-1\). For four leaves the sum of \(d-1\) over internal vertices is three. Up to unary vertices, the possibilities have all binary vertices, one ternary and one binary vertex, or one quaternary vertex. The middle case has zero or one binary ancestor of the ternary vertex. Thus the possible three-fan counts are \(3,9,21,39\).

## Verification

The supplied `verify.py` enumerates all vertex maps into fans with two to four maxima for increasingly labeled rooted trees on at most six vertices. It tests forth and back directly using descendant sets, and compares with separate leaf-color and recurrence counts. Every rooted shape of at most six vertices has an increasingly labeled representative. It also checks the degree threshold, upper-bound equality criterion, unique ternary-vertex formula and a four-leaf full-binary collision. The recorded output is in `verification_output.json`. These finite comparisons corroborate the arguments but do not prove the universal claims.

## Relationship to existing results and limitations

The general exact counting theorem [1] already covers surjective counts to the star \(F_k\) and hence all counts here, by adding the \(k\) constant maps. The contribution of the structural results is to describe the maps themselves by local palette constraints and use those constraints to determine exactly when all globally onto colorings are allowed. The two-fork correspondence [2] uses the same maximal-color idea for two colors and a product source. It does not give the \(k\ge3\) local obstruction and star equality for arbitrary rooted trees. The one-relation forth/back conditions are standard [3]. No publication priority is claimed. None of the assertions is about immediate parent-edge accessibility, quotients by automorphisms, or unordered target colors.

## References

1. [*Exact bounded-morphism counting between arbitrary finite rooted tree frames*](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-exact-bounded-morphism-counting-between-arbitrary-finite-rooted--e532142d4dde/RESULT.md), Finding and subtree recurrence.
2. [*P-morphisms onto the two-fork are exactly Boolean colorings*](https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-p-morphisms-onto-the-two-fork-are-exactly-boolean-colorings--93b119282552/RESULT.md), Finding.
3. U. Endriss, *Modal Logics of Ordered Trees*, revised thesis, §3.5, Definition 3.20, 2003. https://staff.science.uva.nl/u.endriss/pubs/files/otl.pdf
