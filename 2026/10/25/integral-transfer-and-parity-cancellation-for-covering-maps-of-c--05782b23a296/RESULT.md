# Integral transfer and parity cancellation for covering maps of cycle Hom complexes

## Finding
Fix integers \(m\ge4\), \(n\ge5\), and \(k,\ell\ge1\). The reductions of vertex labels induce graph coverings \(q:C_{kn}\to C_n\) and \(p:C_{\ell m}\to C_m\), hence a continuous map on ordinary (undirected) Lovász--Babson--Kozlov Hom complexes
\[
\Phi_{k,\ell}(\eta)(j)=q(\eta(j\bmod m)).
\]
Put \(d(t)=1\) for even \(t\) and \(d(t)=2\) for odd \(t\). The map on the integral first homology of each source circle component is multiplication by
\[
D(k,n)=\frac{k\,d(kn)}{d(n)}
=\begin{cases}k/2,&n\text{ odd and }k\text{ even},\\k,&\text{otherwise}.\end{cases}
\]
In particular, a two-sheeted cover of an odd cycle induces a *primitive* first-homology map, rather than multiplication by two. The complete kernel and cokernel of \(\Phi_{k,\ell*}\) are determined in the proof below.

## Assumptions and scope
Write \(C_t\) for the simple undirected cycle with vertex set \(\mathbb Z/t\mathbb Z\) and edges between successive residues. An element of \(\operatorname{Hom}(C_m,C_t)\) is a multihomomorphism \(\eta\) assigning each source vertex a nonempty subset of target vertices such that any two values at adjacent source vertices are completely adjacent. Its cells are products of simplices. Throughout, \(m\ge4\) and \(t\ge5\), so a cell is a cube with coordinate sets of cardinality at most two.

For an ordinary homomorphism \(f:C_m\to C_t\), choose increments \(\epsilon_j\in\{-1,+1\}\) such that \(f(j+1)-f(j)\equiv\epsilon_j\pmod t\). Its winding is \(w=\sum_j\epsilon_j/t\in\mathbb Z\). Noncontractible components occur exactly for admissible \(w\) satisfying \(|tw|<m\) and \(tw\equiv m\pmod2\); for odd \(t\) there is one circle component for each \(w\), whereas for even \(t\) there are two, indexed by the parity of \(f(0)\). Equality \(|tw|=m\) instead produces isolated maps, contributing no first homology. The component classification is the prior theorem of Čukić--Kozlov. For an empty Hom complex, all statements about circle generators and first homology are vacuous.

## Proof
**1. Canonical evaluation degree.** Fix the vertex \(0\) of the source and define the continuous evaluation \(E_t:|\operatorname{Hom}(C_m,C_t)|\to|C_t|\) cellwise. On a cell, each coordinate value is a singleton or an unordered pair \(\{a-1,a+1\}\). The unique length-two geodesic joining that pair in \(|C_t|\) exists for \(t\ge5\); evaluating the coordinate at vertex zero on that arc gives a continuous cellular extension of ordinary vertex evaluation. It is compatible across cell faces.

For a circle component \(Y\), Fujii--Iwamasa--Kimura--Nozaki--Suzuki construct a contractible cubical universal cover, with deck translations \(a_v\mapsto a_v+t'\) simultaneously on every source coordinate, where \(t'=t/\gcd(t,2)\); the covered target label at vertex \(v\) is \(f(v)+2a_v\pmod t\). Their explicit deck construction is a covering of each noncontractible component, and its deck generator is the positive generator of \(\pi_1(Y)\). Since \(E_t\) changes the lifted target label by \(2t'\), it has degree \(2t'/t=d(t)\), with positive sign for the positive deck generator. Thus a preferred generator \(e_Y\in H_1(Y;\mathbb Z)\) satisfies \(E_{t*}(e_Y)=d(t)[C_t]\). This normalization is independent of winding and target-color parity.

**2. Functoriality and the exact coefficient.** Let \(Y\) be a source circle component. The composition \(\Phi_{k,\ell}\) evaluates at the zero vertex of \(C_{\ell m}\) as \(q\circ E_{kn}\), up to the canonical linear realization of the cycle coverings. In particular the evaluation diagram commutes as a continuous map. On the fundamental class of the geometric cycle, \(|q|_*\) multiplies degree by \(k\). Write \(\Phi_{k,\ell*}(e_Y)=a e_Z\), with \(Z\) the target component, once it is known to be a circle. Applying evaluation gives \(a\,d(n)=k\,d(kn)\); therefore \(a=D(k,n)\), a positive integer. As this degree is nonzero, the target component cannot be contractible. Note that \(\ell\) does not appear, because the source covering fixes its distinguished vertex zero.

**3. Identification of target circle sectors.** The ordinary source coloring has winding \(w\), and precomposing with \(p\) repeats its integer edge-step list exactly \(\ell\) times. Postcomposing with \(q\) preserves each signed unit step. Hence the target winding is \(k\ell w\). If \(n\) is even, target and source both have even target length and \(f(0)\bmod2\) is preserved. If \(n\) is odd, the target has only one circle sector for any admissible winding, so the two parity-labeled source components merge when \(k\) is even. The target winding automatically satisfies \(|n k\ell w|<\ell m\) and parity congruence.

**4. Integral Smith classification.** Partition the source circle generators by their target sector \(Z\). Every sector in the image receives at least one generator, and each such generator maps to \(D(k,n)e_Z\). Different target sectors have disjoint supports. Consequently, for each hit target sector, the restriction of the homology map is a row of identical coefficients \((D,\ldots,D)\), whose Smith normal form consists of the single factor \(D\) and zero columns. If \(s\) of the \(T\) target circle sectors are hit, then
\[
\ker(\Phi_{k,\ell*})\cong\mathbb Z^{b_1(\operatorname{Hom}(C_m,C_{kn}))-s},\qquad
\operatorname{coker}(\Phi_{k,\ell*})\cong
(\mathbb Z/D\mathbb Z)^s\oplus\mathbb Z^{T-s}.
\]
The convention \(\mathbb Z/1\mathbb Z=0\) is used. Isolated map components do not contribute to this statement. These formulas are integral and require no rationalization.

For example, with \(m=4\), \(n=5\), \(k=2\), and \(\ell=1\), the map \(H_1(\operatorname{Hom}(C_4,C_{10});\mathbb Z)\to H_1(\operatorname{Hom}(C_4,C_5);\mathbb Z)\) is represented, in the canonical positive bases, by \((1\ \ 1)\): it is surjective with rank-one kernel. For \(m=4,n=6,k=2,\ell=1\), the analogous map from target 12 to target 6 is \(\operatorname{diag}(2,2)\), with cokernel \((\mathbb Z/2\mathbb Z)^2\). Both assertions include the distinctions between target parity sectors.

## Verification
The accompanying `cover_hom_verifier.py` enumerates all homomorphisms in six independently selected small examples, builds their exact reconfiguration edges, constructs explicit closed paths by cycling a path from a coloring to its two-step target rotation, and checks the source and projected target evaluation winding numbers. Its assertions recover the predicted coefficients in the odd/even parity branches. The all-parameter proof is the universal-cover and evaluation argument above, not interpolation from finite examples.

## Relationship to prior work
Čukić and Kozlov (2004) classified the homotopy components of \(\operatorname{Hom}(C_m,C_t)\), including winding-index circles and isolated maps. Fujii and collaborators (2024) generalized the circle-or-point classification to any connected source and built an explicit cubical universal covering, providing the essential deck-normalization input. Dochtermann's treatment of Hom complexes states the general covariant/contravariant functoriality. These results supply the premises, but none of the inspected statements gives the induced **integral** map, the target-parity cancellation, or the Smith groups for varying cycle coverings. The proof here makes those functorial integer invariants explicit.

## Limitations
The result treats canonical, orientation-preserving cyclic coverings and first integral homology. Orientation-reversing coverings change the sign of the displayed coefficient. It does not classify arbitrary graph homomorphisms between target graphs, higher homology, or maps on fundamental-group representations beyond their abelianized degree. Whether an earlier source computes exactly the same functorial Smith groups without matching terminology remains a publication-priority risk; no independent audit has been performed.

## References
1. S. Fujii, Y. Iwamasa, K. Kimura, Y. Nozaki, A. Suzuki, *Homotopy types of Hom complexes of graph homomorphisms whose codomains are cycles*, arXiv:2408.04802, first public 2024-08-09, https://arxiv.org/abs/2408.04802 .
2. S. Čukić and D. Kozlov, *The homotopy type of complexes of graph homomorphisms between cycles*, arXiv:math/0408015, https://arxiv.org/abs/math/0408015 .
3. A. Dochtermann, *Hom complexes and homotopy theory in the category of graphs*, European Journal of Combinatorics 30 (2009), 490--509, https://doi.org/10.1016/j.ejc.2008.04.009 .
