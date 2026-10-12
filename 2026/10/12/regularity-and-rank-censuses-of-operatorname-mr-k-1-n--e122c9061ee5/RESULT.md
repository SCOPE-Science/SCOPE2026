# Regularity and rank censuses of \(\operatorname{MR}(K_{1,n})\)

## Finding

**Theorem.** For every integer \(n\ge3\), let \(S_n=K_{1,n}\) have center \(0\), leaves \(1,\ldots,n\), and simplices the empty set, single vertices, and edges \(\{0,i\}\). Define \(M_n=\operatorname{MR}(S_n)\) to be the monoid of all partial maps \(f:S_n\rightharpoonup S_n\) for which the full inverse image of each singleton or edge is empty, a singleton, or an edge. The rank of \(f\) is \(\rho(f)=|\operatorname{im}f|\). An element is *regular* if there is \(g\in M_n\) with \(fgf=f\), where multiplication is partial-map composition.

Writing \((a)_k=a(a-1)\cdots(a-k+1)\), \((a)_0=1\), define the rank enumerators \(R_n(z)=\sum_{f\in M_n}z^{\rho(f)}\), \(Q_n(z)=\sum_{f\in M_n\setminus\operatorname{Reg}(M_n)}z^{\rho(f)}\), and \(E_n(z)=\sum_{f\in M_n,\ f^2=f}z^{\rho(f)}\). Then

\[
\begin{aligned}
R_n(z)&=1+(2n+1)z+2n^2z^2\\
&\quad+\sum_{k=1}^n\binom nk\big((n+1)_k+k(n)_k\big)z^k
+\sum_{j=2}^n\binom nj(n)_jz^{j+1},\\
Q_n(z)&=\sum_{k=2}^n\binom nk\,k(n)_{k-1}z^k,\\
E_n(z)&=(1+z)^{n+1}+nz(1+z)^{n-1}+nz.
\end{aligned}
\]

In particular, \(M_n\) is nonregular, its nonregular elements are precisely those \(f\) satisfying

\[
\rho(f)\ge2,\qquad 0\notin\operatorname{im}f,\qquad 0\in\operatorname{dom}f,\qquad f^{-1}(f(0))=\{0\},
\]

and the idempotent count is

\[
|\{f\in M_n:f^2=f\}|=2^{n+1}+n2^{n-1}+n.
\]

For \(n=3,4,5\), the triples (total elements, nonregular elements, idempotents) are respectively \((185,36,31)\), \((1278,288,68)\), and \((10857,2500,149)\).

## Assumptions and scope

The condition concerns **inverse images of all faces**, rather than ordinary graph endomorphisms preserving edges forward. An undefined input never belongs to a fiber. The zero element of the monoid is the everywhere undefined map. The parameter \(n\ge3\) starts at the first genuinely branching star not isomorphic to a path. The displayed polynomial identity also holds at \(n=2\), but that boundary is not needed for the result.

## Proof

**Fiber decomposition.** Let \(H=\operatorname{im}f\). If \(0\notin H\), then the image vertices are pairwise nonadjacent leaves. Every fiber is a singleton or an edge, and distinct edge fibers cannot coexist because two edges of a star intersect at its center. Consequently either all fibers are singletons, or one fiber is an edge \(\{0,i\}\) and all remaining fibers are singletons of leaves distinct from \(i\). For fixed \(H\) with \(|H|=k\), the all-singleton case has \((n+1)_k\) maps; the one-double-fiber case has \(k n(n-1)_{k-1}=k(n)_k\) maps. Choosing \(H\) gives the first summation in \(R_n\).

If \(H=\{0\}\), the unique nonempty fiber can be any of the \(n+1\) vertices or any of the \(n\) edges, giving \(2n+1\) maps. If \(H\) contains \(0\) and exactly one leaf, the union of the two nonempty fibers is the inverse image of their edge, and must be an edge with two singleton fibers. There are \(2n\) orientations of a source edge and \(n\) choices of target leaf, giving \(2n^2\) maps. If \(H\) contains \(0\) and \(j\ge2\) leaves, all fibers are singletons. The preimage of \(0\) must be the source center (otherwise two distinct target leaves would need the same source center as their preimage), and the \(j\) remaining preimages are distinct source leaves. Thus there are \(\binom nj(n)_j\) maps. With the empty map, these cases prove \(R_n(z)\).

**Regularity obstruction.** For arbitrary partial transformations, \(fgf=f\) is equivalent to the requirement that for every \(y\in H\), \(g(y)\) is defined and lies in the fiber \(f^{-1}(y)\). Indeed this condition implies equality on the domain of \(f\), while both sides are undefined outside that domain. If \(H\) consists of \(k\ge2\) target leaves and the source center is a singleton fiber, any such \(g\) must map one of those target leaves to the source center and a second target leaf to some source leaf. The inverse image under \(g\) of the source edge between those two outputs then contains two distinct target leaves. Since no two target leaves form an edge, \(g\notin M_n\). Therefore \(f\) is nonregular.

Conversely, if the image is contained in target leaves and has at least two vertices but the source center is not a singleton fiber, choose a transversal of all fibers entirely among source leaves: this is possible when the center is absent, or when it lies in the unique double fiber. Let \(g\) be the resulting partial inverse, defined precisely on \(H\). Its outputs are distinct source leaves, so every target face has under \(g\) an empty or singleton preimage; hence \(g\in M_n\) and \(fgf=f\). For a singleton image a one-point section suffices. When the image contains the target center and at least one target leaf, the preceding fiber classification shows that \(f\) is a bijection between two star subgraphs (a source edge in the two-point case, a centered star when there are at least three image vertices). Its inverse on \(H\) is continuous, so again \(fgf=f\). This proves the claimed if-and-only-if regularity criterion.

For a nonregular map of rank \(k\), necessarily \(2\le k\le n\). Choose its \(k\)-element leaf image \(H\) in \(\binom nk\) ways, choose which of the \(k\) image leaves receives the source center, and inject the other \(k-1\) image labels into distinct source leaves in \((n)_{k-1}\) ways. These are all such maps, giving \(Q_n(z)\).

**Idempotents.** A partial map satisfies \(f^2=f\) if and only if it fixes every point in its image. With a \(k\)-element image made entirely of leaves, the leaf image points must map to themselves and the only extra domain element permitted is the source center, which may be undefined or map to any one of the \(k\) image leaves. This yields \(k+1\) maps per leaf image. The center-only image yields \(n+1\) idempotents (its fixed center and optionally one additional source leaf). With center and \(j\ge1\) image leaves, only the partial identity on the image works, giving \(\binom nj\) idempotents. Including the empty map and summing,

\[
\begin{aligned}
E_n(z)&=\sum_{k=0}^{n}\binom nk(k+1)z^k+(n+1)z+z\sum_{j=1}^{n}\binom njz^j\\
&=(1+z)^{n+1}+nz(1+z)^{n-1}+nz.
\end{aligned}
\]

Setting \(z=1\) proves the idempotent total.

## Verification

The included `verify.py` independently enumerates all partial maps on \(n+1\) vertices for \(2\le n\le5\). It tests each vertex and edge preimage against the definition, computes rank and idempotence directly, and compares the resulting polynomials with the formulas. It also constructs a regularity witness for every predicted regular map and checks \(fgf=f\). For \(n=2,3\), a separate exhaustive search over *all pairs* of continuous maps confirms that a witness exists exactly when the criterion predicts. The output is `VERIFY_OK` with counts for all cases. These finite tests do not certify the infinite-parameter theorem; the case decomposition and proof above do.

## Relationship to prior work

Margolis and Rhodes, arXiv:2609.39370v2, define \(\operatorname{MR}(\Gamma)\), characterize its singular and injective pieces (Section 3.4), describe regular \(\mathcal J\)-classes (Section 4), and give explicit orders for strict continuous monoids on paths and cycles (Section 8). The star family is not enumerated there. The present statement is a rank-by-rank *full monoid* census, a concrete obstruction to regularity, and an idempotent census, rather than a restatement of their general Green-relation correspondence.

Dimitrova, Fernandes, and Koppitz (arXiv:2410.21084v1) study partial graph endomorphism monoids on stars. Their maps impose **forward** edge preservation (possibly weak or strong), unlike the inverse-face condition here. For example, the partial map sending the source center to one target leaf and a source leaf to a different target leaf is in the present monoid but not a forward edge endomorphism. Conversely, a partial map collapsing three source vertices to the center is a weak endomorphism but not continuous here. Thus their enumerations do not directly give these formulas. The general degree-two transformation-semigroup framework predates the 2026 work.

## Limitations

This concerns finite stars with at least three leaves, not arbitrary trees or the Krohn–Rhodes complexity of their monoids. It does not classify all Green classes individually or produce a monoid presentation. A literature search cannot establish absolute historical priority; an older equivalent enumeration under another definition remains possible. The finite computational checks are illustrative, not a replacement for the general proof.

## References

- S. Margolis and J. Rhodes, *The Margolis–Rhodes Monoid of Continuous Functions on a Graph*, arXiv:2609.39370v2 (2026), especially Sections 1, 3.4, 4, 7, 8. https://arxiv.org/html/2609.39370v2
- I. Dimitrova, V. H. Fernandes, and J. Koppitz, *Presentations for Monoids of Partial Endomorphisms of a Star Graph*, arXiv:2410.21084v1 (2024), Sections 1–2. https://arxiv.org/html/2410.21084v1
- S. Margolis and J. Rhodes, *Degree 2 Transformation Semigroups as Continuous Maps on Graphs: Foundations and Structure*, arXiv:2005.02606 (2020). https://arxiv.org/abs/2005.02606
