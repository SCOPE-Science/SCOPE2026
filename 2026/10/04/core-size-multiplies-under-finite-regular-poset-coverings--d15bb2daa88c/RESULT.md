# Core size multiplies under finite regular poset coverings

## Finding
Let \(B\) be a finite connected \(T_0\)-space, let \(G\) be a finite group, and let \(c\) be an admissible connected \(G\)-coloring of the Hasse diagram of \(B\). Barmak and Minian associate to \(c\) the regular covering \(p:E(c)\to B\) with points \((x,g)\) and lifted Hasse edges determined by the color of each base edge.

For this covering, beat points are preserved and reflected fiberwise. More precisely, \((x,g)\) is an up beat point exactly when \(x\) is an up beat point, and \((x,g)\) is a down beat point exactly when \(x\) is a down beat point. Therefore, if \(C\) is obtained from \(B\) by deleting beat points until a Stong core is reached, deleting the entire fiber over each deleted point gives a sequence of strong deformation retracts
\[
E(c)\searrow E(c|_C).
\]
The terminal space \(E(c|_C)\) has no beat points and hence is a core of \(E(c)\). In particular,
\[
|\mathrm{core}(E(c))|=|G|\,|\mathrm{core}(B)|.
\]

For the 13-point minimal finite model \(P\) of \(\mathbb{RP}^2\), the standard connected \(\mathbb Z/2\)-coloring gives its universal cover. Since \(P\) is already a core, the universal cover is a 26-point core. Its order complex is a closed triangulated surface with \(f\)-vector \((26,72,48)\) and Euler characteristic \(2\), hence is a triangulated \(S^2\). Thus the universal cover is weakly homotopy equivalent to \(S^2\), but it is not homotopy equivalent as a finite space to the unique 6-point minimal finite model of \(S^2\).

## Assumptions and scope
The theorem concerns finite regular coverings represented by admissible connected colorings by a finite group. This is the covering construction of Barmak and Minian. The core is the beat-point-free finite space obtained by successive Stong beat-point deletions, unique up to homeomorphism.

For the projective-plane application, use the 13-point height-two model with four minimal points \(a_1,\ldots,a_4\), six middle points \(b_{ij}\) indexed by edges of \(K_4\), and three maximal points indexed by the perfect matchings of \(K_4\). The relation \(a_i<b_{jk}\) holds exactly when \(i\in\{j,k\}\), and \(b_e<c_M\) holds exactly when \(e\notin M\). Its opposite gives the other 13-point minimal model. The statement for the opposite follows by reversing the order.

## Proof
Write \(x\prec y\) for a Hasse edge in \(B\). In the coloring construction, for every \(g\in G\) there is exactly one lifted Hasse edge from \((x,g)\) over \(x\prec y\), namely the edge ending at the uniquely determined lift of \(y\). Conversely, every Hasse edge in \(E(c)\) projects to a Hasse edge in \(B\). Hence the number of points immediately above \((x,g)\) equals the number immediately above \(x\), and the same holds below.

In a finite poset, an up beat point is exactly a point covered by one point, while a down beat point is exactly a point covering one point. The Hasse-degree correspondence therefore proves beat-point preservation and reflection.

Suppose \(x\) is a beat point of \(B\). Every point in the fiber \(p^{-1}(x)\) is then a beat point of the same type. Points in a common fiber are pairwise incomparable, so deleting one lift does not destroy the beat-point witness for any other lift in that fiber. By Stong's theorem, deleting the whole fiber is a sequence of strong deformation retracts. After that deletion the remaining Hasse diagram is exactly the coloring cover associated to the restriction of \(c\) to \(B-\{x\}\). Iterating along a beat-point reduction of \(B\) to a core \(C\) yields \(E(c)\searrow E(c|_C)\).

Because \(C\) has no beat points and beat points reflect from the cover to the base, \(E(c|_C)\) has no beat points. It is therefore a core of \(E(c)\). Its underlying set is \(C\times G\), which proves the cardinality formula.

For the projective-plane model \(P\), Barmak and Minian explicitly give a connected \(\mathbb Z/2\)-coloring corresponding to the universal cover. Cianci and Ottina prove that every 13-point finite model of \(\mathbb{RP}^2\) is one of two opposite models and that such a model has no beat points. Thus the core formula gives 26 points for the universal cover and shows that it is itself a core.

The accompanying verifier reconstructs the model above and finds a non-coboundary admissible \(\mathbb Z/2\)-coloring. The base order complex has \(f\)-vector \((13,36,24)\), every simplicial edge lies in two triangles, every vertex link is a cycle, and its Euler characteristic is \(1\). The lifted order complex has \(f\)-vector \((26,72,48)\), the same local closed-surface condition, and Euler characteristic \(2\). It is connected, so the classification of closed surfaces identifies it with \(S^2\).

Finally, Barmak and Minian prove that the unique cardinality-minimal finite model of \(S^2\) has six points. The 26-point universal cover and the 6-point model are both beat-point-free. Stong's core classification says that homotopy-equivalent finite \(T_0\)-spaces have homeomorphic cores. Since the two cores have different cardinalities, they are not homotopy equivalent as finite spaces, even though both have weak homotopy type \(S^2\).

## Verification
Run `python3 artifacts/verify.py`. The script independently reconstructs the 13-point poset, solves the admissibility equations over \(\mathbf F_2\), selects a non-coboundary coloring, constructs the connected double cover, checks Hasse-degree preservation, confirms that both base and cover have no beat points, computes both order-complex \(f\)-vectors, and verifies that each simplicial edge belongs to two triangles and every vertex link is a cycle. The supplied output ends in `VERIFY_OK`.

The general core-scaling theorem is symbolic and does not depend on the finite computation; the computation certifies the concrete projective-plane application.

## Relationship to prior work
Barmak and Minian's coloring paper supplies the covering construction and, in Example 3.7, explicitly identifies a connected \(\mathbb Z/2\)-coloring of the 13-point projective-plane model with its universal cover. That universal-cover construction is prior work and is not claimed here as new. Their paper states the beat-point criterion in the preliminaries but does not state that beat points lift and reflect under the coloring cover, does not identify the universal cover in Example 3.7 as a core, and does not give the core-cardinality multiplication formula.

Cianci and Ottina establish the 13-point lower bound and classify the two opposite minimal projective-plane models; their proof also records that a 13-point model has no beat points. Barmak and Minian establish that the unique minimal finite sphere model has \(2n+2\) points, hence six points for \(S^2\). Combining these results with the fiberwise beat-point lemma yields the new structural conclusion about cores under regular covers and the 26-point universal-cover corollary.

Targeted searches for regular finite-poset coverings together with beat points, cores, and core cardinality did not locate a published statement of the fiberwise beat-point equivalence or the core-size formula. The closest database result concerned an unrelated simplicial \(\mathbb{RP}^2\) torsion census, not finite-space covering cores.

## Limitations
The theorem is stated for finite regular coverings in the explicit group-coloring framework. No claim is made here about arbitrary nonregular finite coverings, infinite-sheeted coverings, or a functorial choice of core independent of a chosen beat-point deletion sequence.

The 26-point projective-plane universal cover is shown to be a core and to have weak type \(S^2\); this does not assert that 26 is extremal among all beat-point-free finite models with weak type \(S^2\). The distinction proved is specifically between finite-space homotopy type and weak homotopy type.

## References
1. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156v1, 2006; J. Homotopy Relat. Struct. 2 (2007), 127--140.
2. J. A. Barmak, *Algebraic Topology of Finite Topological Spaces and Applications*, Lecture Notes in Mathematics 2032, Springer, 2011.
3. J. A. Barmak and E. G. Minian, *G-colorings of posets, coverings and presentations of the fundamental group*, arXiv:1212.6442v1, 2012.
4. N. Cianci and M. Ottina, *Poset splitting and minimality of finite models*, arXiv:1512.06088v1, 2015.
5. R. E. Stong, *Finite topological spaces*, Trans. Amer. Math. Soc. 123 (1966), 325--340.
