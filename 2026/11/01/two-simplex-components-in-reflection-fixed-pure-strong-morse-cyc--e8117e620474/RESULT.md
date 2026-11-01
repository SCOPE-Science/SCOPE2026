# Two simplex components in reflection-fixed pure strong Morse cycle complexes

## Finding
Let \(n\ge6\), let \(C_n\) be the cycle on \(\mathbb Z/n\mathbb Z\), and let
\(K_n=\mathcal{SM}_{\mathrm{pure}}(C_n)\) be the **pure strong discrete Morse matching complex** of Knudson and Owens--White. For \(a\in\mathbb Z/n\mathbb Z\), let the reflection \(s_a\) act on the underlying cycle by \(s_a(i)=a-i\). Then its **geometric**, not just homological, fixed-point space is a disjoint union of two simplices:
\[
\boxed{\ |K_n|^{\langle s_a\rangle}\cong_{\mathrm{PL}}\Delta^{d(n,a)}\sqcup\Delta^{d(n,a)},\quad
 d(n,a)=\begin{cases}
 m-2,&n=2m+1,\\
 m-2,&n=2m,\ a\equiv0\pmod2,\\
 m-3,&n=2m,\ a\equiv1\pmod2.
 \end{cases}\ }
\]
In particular, every reflection has a fixed space homotopy equivalent to \(S^0\), and its **reduced homological Lefschetz number** equals
\[
\boxed{\ \mathcal L_n(s_a)=\sum_{j\ge0}(-1)^j\operatorname{tr}\!\bigl((s_a)_*\mid\widetilde H_j(K_n;\mathbb Q)\bigr)=1.\ }
\]
The latter supplies exactly the reflection entries missing from the previously determined cyclic-rotation virtual character of this pure complex.

## Assumptions and scope
The vertices of \(K_n\) are the \(2n\) possible vertex--edge incidences of \(C_n\), written \((i,+)\) when edge \(e_i=\{i,i+1\}\) is matched to vertex \(i\), and \((i,-)\) when the same edge is matched to vertex \(i+1\). A face is any set of incidences contained in a maximal-cardinality strong discrete Morse matching obtained from a strict vertex filtration, with the simplicial downward closure taken as in the source definition. The pure complex must not be confused with the **full** strong-matching complex or the ordinary Chari--Joswig Morse complex. The group acts by relabeling both vertices and edges; \(s_a(i,\pm)=(a-i-1,\mp)\). The geometric realization uses the standard affine realization of an abstract finite simplicial complex.

For clarity \(\Delta^d\) denotes a closed \(d\)-simplex. The first two cases above are the odd-cycle reflection class and the even-cycle **vertex-axis** class, respectively. The last is the even-cycle **edge-axis** class. Only \(n\ge6\) is claimed.

## Proof
**1. All maximal facets.** Fix a strict vertex order and let \(g\) be its last vertex. Both neighbors of \(g\) already occur when \(g\) enters. Since the two neighbors are not adjacent in \(C_n\) for \(n\ge6\), its descending link is not a cone: \(g\) is critical and neither incident edge can be used as an incidence pair in this filtration. Consequently a matching contains at most \(n-2\) incidences. To attain this bound, precisely the two edges \(e_{g-1},e_g\) are unused. Removing \(g\) leaves the path whose successive vertices are
\[
 g+1,g+2,\ldots,g+n-1\quad(\text{mod }n).
\]
Every one of its \(n-2\) edges is matched to a different endpoint, leaving precisely one unmatched path vertex \(r\), its root. Leaf stripping forces the matched endpoint of each path edge to be the endpoint farther from \(r\). Therefore, reading the path edges in increasing cyclic order, every top facet has the incidence-sign word
\[
\underbrace{00}_{\text{edges incident to }g}\,\underbrace{+\cdots+}_{j\text{ entries}}\underbrace{-\cdots-}_{n-2-j\text{ entries}},\qquad 0\le j\le n-2,
\]
up to cyclic rotation. Conversely, choose any distinct \(g,r\), insert \(r\) first, grow the remaining path outward from \(r\) with each new vertex adjacent to exactly one earlier vertex, and insert \(g\) last. This realizes the prescribed root-directed incidence matching as a strong matching. Hence exactly the \(n(n-1)\) rooted-path facets \(F(g,r)\) occur. This also reconstructs the maximal-facet statement of Proposition 8.3 in the primary source.

**2. Orbit vertices in the fixed triangulation.** For a simplicial involution, fixed barycentric coordinates are equal on the two vertices of each swapped orbit. Thus its fixed polyhedron is PL-homeomorphic to the simplicial complex whose vertices are two-element incidence orbits contained in faces of \(K_n\), with a collection of orbit vertices forming a face precisely when their union is a face of \(K_n\). No incidence is individually fixed by \(s_a\): any fixed underlying edge has its endpoints interchanged and hence its two incidences swapped. An orbit consisting of both incidences of one edge is not a face and is discarded.

Conjugating by rotations reduces the calculation to \(s_0\) for odd \(n\), and to \(s_0,s_1\) for even \(n\). An incidence orbit uses a representative edge \(e_i\) from one half of the cycle and its mirror edge \(e_j\), where \(j=a-i-1\pmod n\). Write **type A** for the pair \(\{(i,-),(j,+)\}\), and **type B** for \(\{(i,+),(j,-)\}\). The complete list of *individually admissible* orbits is:

| Reflection | Representative index \(i\) for type A | Representative index \(i\) for type B | Mirrored edge index \(j\) |
| --- | --- | --- | --- |
| \(n=2m+1,\ s_0\) | \(0\le i\le m-2\) | \(1\le i\le m-1\) | \(2m-i\) |
| \(n=2m,\ s_0\) | \(0\le i\le m-2\) | \(1\le i\le m-1\) | \(2m-1-i\) |
| \(n=2m,\ s_1\) | \(1\le i\le m-2\) | \(2\le i\le m-1\) | \(2m-i\) |

Here the first two rows have \(m-1\) orbits in each type, and the last row has \(m-2\) orbits in each type. These ranges follow from the matching constraints and the two-consecutive-unused-edges condition in step 1: for \(s_0\), the disallowed first B orbit matches the fixed vertex \(0\) twice, and the disallowed final A orbit either matches the opposite fixed vertex twice (even case) or forces the central fixed edge to be a *single isolated* unused edge (odd case). For the edge-axis reflection \(s_1\), the two boundary orbits of the wrong type similarly force one of the fixed edges \(e_0,e_m\) to be an isolated unused edge. All other orbits in the listed ranges actually occur in top facets, as shown next.

**3. Each type is one full simplex, and the two types cannot mix.** The entire collection of type A orbits is contained in the rooted-path facet \(F(m,0)\) for either parity under \(s_0\), and in \(F(m,1)\) under \(s_1\). The entire collection of type B orbits is contained in \(F(0,m)\) under \(s_0\), and in \(F(1,m)\) under \(s_1\). Therefore each type generates a full simplex of the indicated dimension.

The two types cannot occur together in any face. If the representative edge index is the same, their union contains both incidences of that edge. Otherwise take representative indices \(i<j\) on the same half of the cycle. The corresponding four matched-edge signs, read cyclically across the pair and its reflected pair, alternate as \(+,-,+,-\) or \(-,+,-,+\) whenever the types differ. Every rooted-path facet from step 1, however, has all nonzero signs in a single cyclic \(+\)-block followed by one cyclic \(-\)-block, separated only by the one adjacent pair of unused edges. A fourfold alternating subsequence is impossible. Thus the orbit-fixed triangulation consists **exactly** of two disjoint full simplices, establishing the PL assertion.

**4. Homological consequence.** Each simplex is contractible, and the two components are disjoint, so \(\chi(|K_n|^{\langle s_a\rangle})=2\) and \(\widetilde\chi=1\). The simplicial Lefschetz formula after equivariant barycentric subdivision identifies this reduced fixed-point Euler characteristic with the alternating trace on reduced rational homology, giving \(\mathcal L_n(s_a)=1\). This is a statement about the **virtual** character, not about each separate graded representation.

## Verification
The accompanying self-contained `verify.py` independently builds maximal pure facets in two different ways: from all strict vertex filtrations for \(n=6,7,8\), and from rooted-path pairs. These constructions agree and give, respectively, \(30,42,56\) distinct maximal facets. The checker then directly builds reflected incidence orbits and all induced fixed-orbit facets for every odd/even reflection class and every \(6\le n\le64\); all \(89\) cases agree with the three exact index-range formulas in step 2. For \(6\le n\le18\) it also explicitly enumerates all nonempty fixed-orbit faces, finding \(1{,}988\) such faces across these cases and independently checking that each fixed Euler characteristic is \(2\). Run from the extracted package using `python verify.py`; the observed success line is `VERIFY_OK filtration_facets 128 reflection_cases 89 explicit_fixed_faces 1988`.

Finite checks support the theorem but do not replace the unrestricted combinatorial proof in steps 1--4. No separate independent validation is claimed.

## Relationship to prior work
Knudson and Owens--White, *Complexes of strong discrete Morse matchings* (arXiv:2609.06844v1, first publicly available September 6, 2026), define the pure strong complex, enumerate its maximal matchings (Proposition 8.3), and classify its ordinary homotopy type (Theorem 8.6). The full accessible text of Sections 3--4 and 8 was examined; those results do **not** identify the geometric reflection-fixed simplices or their PL dimensions. The underlying facet classification is explicitly prior art and is reconstructed in step 1 only to support the new fixed-space argument.

An earlier result, *The threefold rotation character of pure strong Morse matching complexes of cycles*, determines the cyclic-rotation virtual homology character of **the same pure object** but explicitly does not claim reflection action; its full result and limitations were checked. The result *Dihedral Euler characters of full strong Morse complexes of cycles* concerns the **full** \(\mathcal{SM}(C_n)\), not the pure subcomplex, and its reflection traces are generally different. Chari and Joswig's older *Discrete Morse Complexes* treats ordinary Morse matchings, another distinct construction. This note's novelty claim is the new geometric fixed-point classification for the **pure strong** construction, with its reflection Lefschetz corollary.

## Limitations
Only a single reflection subgroup is treated. The geometric fixed spaces for nontrivial rotations, graded integral/reflection representations, and an equivariant wedge decomposition of the ambient pure complex are not determined here. The two-simplex PL structure has no assertion of canonical equivariant deformation retractions in the ambient complex. Literature comparisons cannot rule out every unpublished or unindexed equivalent argument; independent validation has not been performed.

## References
1. K. P. Knudson and A. Owens--White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1, first public September 6, 2026, especially Definitions 3.2 and 4.2, Proposition 8.3, and Theorem 8.6. https://arxiv.org/abs/2609.06844
2. *The threefold rotation character of pure strong Morse matching complexes of cycles*, published-finding corpus published finding, October 11, 2026. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-threefold-rotation-character-of-pure-strong-morse-matching-c--0dacd6b82f58
3. *Dihedral Euler characters of full strong Morse complexes of cycles*, published-finding corpus published finding, October 11, 2026. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-dihedral-euler-characters-of-full-strong-morse-complexes-of-cycl--4819a9d67705
4. M. K. Chari and M. Joswig, *Discrete Morse Complexes*, arXiv:math/0011234v1 (November 28, 2000); later published in *Discrete Mathematics* 302 (2005), 39--51. https://arxiv.org/abs/math/0011234
