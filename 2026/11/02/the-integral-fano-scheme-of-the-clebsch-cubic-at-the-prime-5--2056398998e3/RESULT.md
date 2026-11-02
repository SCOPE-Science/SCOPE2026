# The integral Fano scheme of the Clebsch cubic at the prime \(5\)

## Finding

Let \(R=\mathbb Z_{(5)}\), and let \(\mathscr X\subset\mathbb P^4_R\) be the Clebsch cubic surface
\[
\mathscr X:\quad \sum_{i=0}^4X_i=\sum_{i=0}^4X_i^3=0.
\]
Write \(\mathscr F=\operatorname{Hilb}^{t+1}(\mathscr X/R)\) for the relative Hilbert scheme of lines, equivalently the zero scheme in \(\operatorname{Gr}(2,4)_R\) of the cubic section of \(\operatorname{Sym}^3\mathcal S^*\). Then there is an isomorphism of finite flat \(R\)-schemes
\[
\boxed{\displaystyle
\mathscr F\simeq
\coprod_{15}\operatorname{Spec}R\ \sqcup\
\coprod_6\operatorname{Spec}\bigl(R[T]/(T^2+T-1)\bigr).}
\]
In characteristic zero, the corresponding geometric lines consist of fifteen rational lines and six pairs defined over \(\mathbb Q(\sqrt5)\). The characteristic-five fiber has precisely twenty-one \(\mathbb F_5\)-rational supports: fifteen reduced points and six curvilinear points of length two. Each doubled support corresponds to a line through the unique ordinary node of the special cubic. Thus the full special-fiber Fano scheme has length \(27\), not \(21\).

There is a natural \(K_6\) incidence refinement. Regard the six lines through the node as the six vertices. Every one of the fifteen remaining lines meets exactly two vertex lines, and the resulting unordered pairs are all fifteen edges of \(K_6\). In particular, each node-line meets precisely five of the fifteen remaining lines.

## Assumptions and scope

The statement is over \(R=\mathbb Z_{(5)}\); base changes to \(\mathbb Q\), its algebraic closure, \(\mathbb F_5\), and its algebraic closure are allowed. The special fiber is singular, so the usual twenty-seven *distinct* lines theorem for a smooth cubic does not apply to that fiber. The decomposition concerns the intrinsic Hilbert scheme, including its nilpotents, rather than only its closed points. The generic quadratic algebra is the field \(\mathbb Q(\sqrt5)\); the extension is tamely ramified at \(5\), and \(T^2+T-1=(T-2)^2\) over \(\mathbb F_5\).

## Proof

**The fifteen sections.** Choose an omitted index \(i\) among five indices and partition the other four into two unordered pairs \(\{j,k\}\) and \(\{\ell,m\}\). The line
\[
X_i=0,\qquad X_j=-X_k,\qquad X_\ell=-X_m
\]
lies on \(\mathscr X\), giving exactly \(5\cdot3=15\) sections over \(R\).

**The six quadratic branches.** Put \(A=R[T]/(T^2+T-1)\). In the order of coordinates \(0,1,2,3,4\), the two vectors
\[
u=(1,0,-1,-T,T),\qquad v=(0,1,T,-T,-1)
\]
span a projective line in \(\mathbb P^4_A\). They satisfy \(\sum u_i=\sum v_i=0\), and, using \(T^2=1-T\), they satisfy all four polarizations
\[
\sum u_i^3=\sum u_i^2v_i=\sum u_iv_i^2=\sum v_i^3=0.
\]
Consequently they define an \(A\)-valued Fano point. All their coordinate permutations give, on the generic fiber, the classical twelve non-matching lines of the Clebsch cubic. Equivalently, a representative is the span of \((1,\zeta,\zeta^2,\zeta^3,\zeta^4)\) and \((1,\zeta^{-1},\zeta^{-2},\zeta^{-3},\zeta^{-4})\), with \(\zeta\) a primitive fifth root of unity and \(T=\zeta+\zeta^{-1}\). The twelve lines form six conjugate pairs. The stabilizer of the unordered pair is the order-twenty affine group on five points, so coordinate permutations yield six distinct \(A\)-families. The generic geometric fiber consists exactly of these twelve lines and the fifteen matching lines, by the classical twenty-seven-line theorem.

**The special cubic and its six node-lines.** Set \(k=\overline{\mathbb F}_5\). The singular points of \(\mathscr X_k\) satisfy \(X_i^2=X_j^2\) for all indices, hence every coordinate is a common scalar times a sign. Since the five signs sum to zero in characteristic five only when all signs agree, the unique singular point is
\[
P=[1:1:1:1:1].
\]
Its quadratic tangent cone is the nondegenerate form induced by \(\sum X_i^2\) on the three-dimensional space \(\ker(\sum X_i)/\langle P\rangle\), so \(P\) is an ordinary node. A line through \(P\) with a second spanning vector \(w\) is contained in the cubic exactly when
\[
\sum w_i=\sum w_i^2=\sum w_i^3=0.
\]
Modulo the freedom \(w\mapsto aw+bP\), the equations of degrees two and three define a plane conic and cubic, intersecting in six points. All six are represented by permutations of \((0,1,2,3,4)\); there are six modulo affine changes of the five residues. They are transverse because a linear combination of their gradients could vanish on the sum-zero hyperplane only if a polynomial \(aT+bT^2-c\) vanished at all five residues. Such a polynomial must vanish identically. Bézout gives exactly these six geometric node-lines.

**Finiteness and length.** A line avoiding \(P\) lies in the smooth locus of the cubic. By adjunction its normal bundle within the cubic has degree \(-1\), hence is \(\mathcal O_{\mathbb P^1}(-1)\), giving zero Hilbert-scheme tangent space. The lines through \(P\) have just been shown finite. Consequently every geometric special-fiber Fano component is zero-dimensional. The Fano scheme is the zero locus of a rank-four bundle section on the four-dimensional smooth relative Grassmannian. It is therefore a relative zero-dimensional local complete intersection over \(R\), Cohen–Macaulay with no vertical components and finite flat. Its degree equals the generic twenty-seven-line count; independently, with \(x,y\) the Chern roots of \(\mathcal S^*\),
\[
\int_{\operatorname{Gr}(2,4)}c_4(\operatorname{Sym}^3\mathcal S^*)
=\int 9xy(2x+y)(x+2y)
=45-18=27.
\]
The fifteen matching sections avoid \(P\) and so give fifteen reduced supports.

**The doubled local points.** For a node-line \(\langle P,w\rangle\), vary its two spanning vectors by \(a,b\), respectively. Let \(L_1(c)=\sum w_ic_i\) and \(L_2(c)=\sum w_i^2c_i\). The first-order cubic-containment equations on the four-dimensional tangent space of the Grassmannian are
\[
L_1(a)=0,\qquad L_2(a)+2L_1(b)=0,\qquad L_2(b)=0.
\]
Both forms are independent on \(\ker(\sum X_i)/\langle P,w\rangle\), by the same five-root polynomial argument. The equations have rank three, leaving a one-dimensional tangent space. Thus each of the six local Artin rings has length at least two. The fifteen other supports and the global length \(27\) force the six local lengths to be *exactly two*. Every length-two local algebra over the perfect residue field with one tangent direction is isomorphic to \(k[\varepsilon]/(\varepsilon^2)\).

**The integral isomorphism.** The fifteen sections and six quadratic families give a finite morphism from the proposed disjoint union to \(\mathscr F\). Their special supports are pairwise distinct: the fifteen sections avoid \(P\), while the six quadratic families reduce to the six node-lines. In the displayed chart for the representative quadratic family, the Plücker minor \(p_{01}=1\) and normalized coordinate \(p_{02}/p_{01}=T\). At the prime \(5\), the element \(T-2\) is nonzero and square-zero in \(A/5A\); hence this Plücker coordinate generates the entire dual-number local algebra. The induced map on each special local ring is therefore a surjection between two length-two rings, hence an isomorphism. It is also an isomorphism at the fifteen reduced supports. Nakayama's lemma for finite free \(R\)-modules upgrades the special-fiber isomorphism to the asserted isomorphism over \(R\).

**The incidence graph.** Each node-line represented by a permutation \(w\) meets exactly five of the matching lines: for each choice of omitted coordinate, the other four residues pair uniquely into two opposite pairs around the omitted residue. By the \(S_5\)-symmetry, each matching line meets exactly two node-lines. Conversely, any two distinct node-lines span a plane; the plane section of the cubic contains them and has a unique third residual line. Since the tangent quadratic cone at \(P\) has just the two specified line directions in that plane, this residual line avoids \(P\) and hence is one of the fifteen matching lines. This establishes the complete \(K_6\) incidence identification.

## Verification

The accompanying standalone Python 3 checker `verify_clebsch.py` carries out independent exact computations: all \(806\) projective lines in \(\mathbb P^3(\mathbb F_5)\), the \(21\) rational line supports on the special cubic, the fifteen-plus-six partition, the complete \(K_6\) incidence structure, the Grassmannian Chern number \(27\), and the quadratic coefficient-ring identities for the displayed \(A\)-family. It reduces all twelve generic permutation lines to six distinct special supports and tests that their normalized Plücker coordinates detect the nonzero nilpotent. Its finite-field enumeration is corroboration; the proof above establishes geometric completeness and scheme length independently.

Run with `python3 verify_clebsch.py`. Both exact-check success markers are printed upon completion.

## Relationship to prior work

The classical Clebsch line configuration (fifteen matching lines plus twelve fifth-root lines) and the known singularity of the Clebsch cubic in characteristic five are not claimed as discoveries. Vikulova's 2024 preprint explicitly notes that the Clebsch cubic is singular at \(P\) in characteristic five and studies automorphism groups of *smooth* cubic surfaces. The six node-lines are also obtainable as components of the characteristic-five Bring complete intersection \(V(e_1,e_2,e_3)\); their individual existence is not the new assertion. The contribution here is the **complete integral relative Hilbert scheme**, including the six ramified quadratic branches, their exact dual-number special local rings, and the canonical complete-graph incidence with the fifteen other lines. Generic rationality of the 27 smooth-fiber lines does not itself determine the flat integral special fiber or its infinitesimal structures.

## Limitations

The result is localized at the prime five, not a uniform analysis of every bad prime of an arbitrary integral cubic model. It does not determine the deformation theory of all nodal cubic surfaces, or the integral Fano scheme for non-Clebsch models. The six node-line supports and the classical generic lines have substantial antecedents; the originality assessment is confined to the exact integral decomposition and incidence refinement. Independent external verification and priority review have not been performed.

## References

1. A. V. Vikulova, *The most symmetric smooth cubic surface*, first public arXiv submission 13 July 2024, arXiv:2407.09997, https://arxiv.org/abs/2407.09997, especially Introduction and §§3–4.
2. V. L. Dolgachev and A. Duncan, *Automorphisms of cubic surfaces in positive characteristic*, reference on smooth cubic surfaces cited in Vikulova (2019); smoothness hypotheses do not cover the singular characteristic-five fiber.
3. Classical Clebsch cubic line equations and 27-line configuration, illustrated in the University of California, Irvine mathematical surface gallery: https://www.math.uci.edu/~vmm/Surface/clebsch_cubic/clebsch_cubic.html.
