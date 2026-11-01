# Pentagon Hom complexes of polygonal prisms: circles and a divisibility jump

## Finding

For every integer \(n\ge3\), define the prism graph \(P_n=C_n\square K_2\). Let \(\operatorname{Hom}(P_n,C_5)\) denote the ordinary undirected graph-homomorphism complex, with its usual product-of-simplices cells. Set
\[
 W_n=\bigl\{w\in\mathbb Z: w\equiv n\pmod 2,\ 5|w|\le n\bigr\},\qquad
 W_n^\circ=\bigl\{w\in W_n:5|w|<n\bigr\}.
\]
Then the **complete homotopy type** is
\[
\boxed{\operatorname{Hom}(P_n,C_5)\simeq
 \left(\coprod_{w\in W_n^\circ} S^1\right)
 \amalg\left(\coprod^{20\mathbf1_{5\mid n}}\{\mathrm{pt}\}\right).}
\]
In particular the circle count is
\[
 b(n)=\begin{cases}
 1+2\left\lfloor\frac{n-1}{10}\right\rfloor,&n\text{ even},\\
 2\left\lfloor\frac{n+4}{10}\right\rfloor,&n\text{ odd},
 \end{cases}
\]
while twenty additional **isolated** vertices occur exactly when \(5\mid n\). The case \(n=3\) is empty. For instance, the cases \(n=4,5,7,10,15\) have types \(S^1\), twenty points, two circles, one circle together with twenty points, and two circles together with twenty points, respectively.

## Assumptions and scope

All graphs are finite, simple, undirected, and loopless. The vertices of \(C_5\) are integers modulo five, with adjacency for differences \(\pm1\). The source \(P_n\) has vertices \((i,a)\), with \(i\in\mathbb Z/n\mathbb Z\), \(a\in\{0,1\}\); adjacent vertices either differ by one horizontally within a layer or share the same \(i\) and differ in layer. The regular CW complex \(\operatorname{Hom}(G,H)\) has cells indexed by functions \(\eta:V(G)\to2^{V(H)}\setminus\{\varnothing\}\) with every pair of values on adjacent source vertices forming an edge of \(H\). In particular its vertices are graph homomorphisms and its edges change one source vertex's color.

For a graph homomorphism \(f:P_n\to C_5\), every oriented graph edge \(u\to v\) has a **signed color increment** \(\epsilon_f(u,v)\in\{-1,+1\}\), uniquely specified by \(f(v)-f(u)\equiv\epsilon_f(u,v)\pmod5\). This defines an orientation \(\vec P_{n,f}\) from color \(a\) to color \(a+1\); its horizontal winding is \(w(f)=\frac15\sum_{i=0}^{n-1}\epsilon_f((i,0),(i+1,0))\).

## Proof

**1. Square circulation and realizable winding.** On any four-cycle of the prism the oriented sum of four signed increments is a multiple of five lying between minus four and four. It is therefore zero **as an integer**. Adding these square identities over the annular strip shows that the horizontal signed sums on the two rims coincide. Each such sum is a multiple of five, has the parity of \(n\), and has absolute value at most \(n\). Hence \(w(f)\in W_n\).

Conversely choose any \(w\in W_n\) and a sequence \(s_i\in\{-1,+1\}\) summing to \(5w\). Starting with any \(a\in\mathbb Z/5\mathbb Z\), define \(f(i,0)=a+\sum_{j<i}s_j\pmod5\) and \(f(i,1)=f(i,0)+1\pmod5\). This is a well-defined prism homomorphism with winding \(w\). Thus exactly the integers in \(W_n\) are realized. In particular \(W_3\) is empty, so the asserted complex is empty at \(n=3\).

**2. Winding does not change under recoloring.** If one source vertex can be recolored while preserving its neighbors' colors, all its neighbors must have one common color: two distinct values in \(C_5\) have at most one common neighbor. The recoloring reverses the signs of all incident arrows. It changes neither the signed sum around a rim (or any other closed graph walk) nor \(w\). Consequently different windings are in different connected components of the Hom complex.

**3. Every nonextreme winding orientation is acyclic.** Let \(f\) have \(5|w(f)|<n\). If \(\vec P_{n,f}\) had a directed cycle \(\gamma\) of length \(L>0\), the signed sum around it would be \(L\). All square circulations are zero, so the signed sum around any closed walk equals \(5w(f)m\), where \(m\in\mathbb Z\) is its homological winding around the prism. At least \(n|m|\) horizontal edges are required by a walk with winding \(m\), and hence \(L\ge n|m|\). If \(m=0\), equality \(L=5w(f)m=0\) is impossible. If \(m\ne0\), we obtain \(L=5|w(f)||m|<n|m|\le L\), again impossible. Thus all these orientations have no directed cycles.

**4. Connectivity within each nonextreme winding.** Let \(f,g:P_n\to C_5\) have the same winding. The integral 1-cochain \((\epsilon_g-\epsilon_f)/2\) has zero circulation around all squares and both rims. Since the rim and square boundaries generate the cycle space of the filled prism annulus, there is an integer-valued vertex function \(h\) with \(\epsilon_g=\epsilon_f+2\,dh\). The coloring \(f+2h\pmod5\) and \(g\) have the same increments; adjust the additive constant of \(h\) (possible because two is invertible modulo five) to arrange \(g=f+2h\pmod5\).

Fix \(f\) and direct each graph edge \(u\to v\) when \(\epsilon_f(u,v)=1\). The admissible integer heights are precisely those \(h\) obeying \(h(v)\le h(u)\le h(v)+1\) on each such edge. The coordinatewise minimum of two admissible heights is admissible. Let \(p\le q\) be distinct admissible heights, and let \(S=\{v:p(v)<q(v)\}\). At a vertex \(v\in S\), any incoming arrow \(u\to v\) of the *current coloring* \(f+2p\) forces \(u\in S\): otherwise the edge would violate admissibility for \(q\) after raising \(v\). If no vertex of \(S\) were a source in the current oriented graph, following incoming arrows inside finite \(S\) would produce a directed cycle. The orientation of \(f+2p\) is acyclic by Step 3; hence some source \(v\in S\) exists. Replacing \(p(v)\) by \(p(v)+1\) remains admissible and changes exactly one color by two modulo five. Repeating reaches \(q\) in finitely many recolorings. Any two admissible heights can be joined through their coordinatewise minimum. Therefore all homomorphisms with a fixed nonextreme \(w\) belong to exactly one connected component.

**5. The extreme windings are twenty isolated vertices.** If \(5|w|=n\), all horizontal steps on both rims must have the same sign \(\operatorname{sgn}(w)\). Each square identity then makes all vertical signed steps equal. For either rim sign there are exactly five initial rim colors and two vertical signs: ten homomorphisms. Both possible rim signs exist exactly if \(5\mid n\), giving twenty. At each of their vertices, the two horizontal neighbors have different colors, so no single-vertex recoloring is possible. Each is an isolated point of \(\operatorname{Hom}(P_n,C_5)\).

**6. Identify the homotopy types.** Fujii, Iwamasa, Kimura, Nozaki and Suzuki [1, Theorem 5.1] prove that, for a connected source mapping to a cycle target other than \(C_4\), the Hom component of \(f\) is homotopy equivalent to \(S^1\) if \(\vec P_{n,f}\) has no directed cycle, and is contractible otherwise. The nonextreme components of Step 4 satisfy its first alternative by Step 3, so each is a circle. Step 5 already proves the extreme components are actual isolated points. Counting allowed parity values of \(w\) strictly inside \(5|w|<n\) gives the stated formulas for \(b(n)\).

## Verification

The standalone standard-library verifier `artifacts/verify_prism_hom.py` exhaustively enumerates graph homomorphisms for \(3\le n\le10\), builds every permissible single-vertex recoloring, computes their connected components by an independent union-find procedure, and calculates Euler characteristics by enumerating the compatible product-cube faces using independent-set polynomials. It verifies the winding labels, the predicted number of components in every winding class, Euler characteristic zero for each nonextreme component, and ten singleton components for each extreme sign.

For \(n=3,4,5,6,7,8,9,10\), the full homomorphism counts are respectively \(0,190,20,1410,560,11070,8280,89550\). The checker reports `PRISM_C5_COMPONENTS_AND_CUBICAL_EULER_VERIFIED`. Finite computations are corroboration, **not** a replacement for the all-parameter proof above or the cited published theorem identifying the circle type.

## Relationship to prior work

Čukić and Kozlov [2] classify Hom complexes **between two cycles**, including winding and rigid terminal cases. The source here is a prism with two cycles connected by an entire matching; the new all-parameter formula counts its actual components and identifies a twenty-point divisibility transition not covered by the cycle-source classification. Wrochna [3] establishes a general algorithm for graph-homomorphism reconfiguration into square-free target graphs, but no formula for all prism sizes is stated in the inspected material. Fujii et al. [1] and Matsushita [4] establish the broad possible homotopy types for cycle and square-free codomains; the present result applies those structural theorems and supplies the previously unspecified explicit prism component classification.

The target \(C_5\), the source prism \(C_n\square K_2\), and the Hom functor must be distinguished from prism cut, Čech, matching, or Vietoris–Rips complexes. A topological statement about one of those different constructions does not imply the classification here.

## Limitations

The theorem is for the ordinary undirected target \(C_5\) and the polygonal-prism source \(C_n\square K_2\) only, with \(n\ge3\). It does not classify maps to other odd cycles, the equivariant action of prism symmetries, or the attaching maps of a chosen polyhedral model. Circle equivalence relies on the independently published theorem [1], whereas the component count and rigidity statement have a self-contained proof. The bibliographic comparison rules out implications from the inspected sources but cannot exclude a synonymous, unindexed earlier calculation; there has been no independent expert audit.

## References

[1] Soichiro Fujii, Yuni Iwamasa, Kei Kimura, Yuta Nozaki and Akira Suzuki, *Homotopy types of Hom complexes of graph homomorphisms whose codomains are cycles*, arXiv:2408.04802 (first submitted 2024-08-09), especially Definition 2.2 and Theorem 5.1. https://arxiv.org/abs/2408.04802

[2] Sonja Lj. Čukić and Dmitry N. Kozlov, *The homotopy type of complexes of graph homomorphisms between cycles*, arXiv:math/0408015 (2004 preprint), Theorem 6.1. https://arxiv.org/abs/math/0408015

[3] Marcin Wrochna, *Homomorphism reconfiguration via homotopy*, arXiv:1408.2812 (2014 preprint), especially the introduction and reconfiguration algorithm. https://arxiv.org/abs/1408.2812

[4] Takahiro Matsushita, *Hom complexes of graphs whose codomains are square-free*, arXiv:2412.19144 (2024 preprint), especially Theorem 1.2. https://arxiv.org/abs/2412.19144
