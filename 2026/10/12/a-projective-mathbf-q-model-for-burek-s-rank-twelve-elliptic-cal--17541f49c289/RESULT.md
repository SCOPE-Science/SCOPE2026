# A projective \(\mathbf Q\)-model for Burek's rank-twelve elliptic Calabi–Yau threefold

## Finding

Let \(B_{\mathbf Q}\) be the blow-up of the Hirzebruch surface \(\mathbb F_3\) at the Galois-stable reduced zero scheme of the homogeneous sextic \(UV(U^4-V^4)\) on its distinguished zero section, and let \(W_{\mathbf Q}\to B_{\mathbf Q}\) be the minimalized Weierstrass threefold in Burek's construction [1, equations (1.5) and (6.1)–(6.4)]. Resolve its two split transversal \(A_2\) curves by the projective crepant blow-ups of [1, Lemma 6.2], giving \(W_1\). Then **there exists a smooth projective crepant small resolution \(X_{\mathbf Q}\to W_1\) defined over \(\mathbf Q\)**. Consequently the composite \(X_{\mathbf Q}\to B_{\mathbf Q}\) is a flat elliptic fibration with a regular zero section; its geometric generic fiber has Mordell–Weil rank twelve.

More explicitly, let \(S_1,S_2,S_6,S'_1,S'_2,S'_6\) be the closures on \(W_1\) of the six section graphs given in [1, Appendix A, equation (A.6)], with \(u=2\) for unprimed and \(u=2i\) for primed sections, and let bars denote coefficientwise complex conjugation. The effective Weil divisor
\[
D=\sum_{j\in\{1,2,6\}}\bigl(S_j+\overline{S_j}+S'_j+\overline{S'_j}\bigr)
\]
is defined over \(\mathbf Q\). At the ninety-six geometric ordinary double points of \(W_1\), the absolute local divisor class \(\lvert[D]_p\rvert\), measured against either primitive generator of the local class group \(\mathbf Z\), equals **\(2\) at sixty-four points and \(4\) at thirty-two points**. Thus \(D\) is non-Cartier at every node. One projective small resolution is the relative construction
\[
X_{\mathbf Q}=\operatorname{Proj}_{W_1}\bigoplus_{m\ge0}\mathcal O_{W_1}(mD),
\]
where \(\mathcal O(mD)\) denotes the rank-one reflexive divisorial sheaf.

## Assumptions and scope

Everything is over the characteristic-zero field \(\mathbf Q\) unless a geometric point or its completed local ring is mentioned. The equations, base blow-ups, singularity classification, and twelve section formulas are exactly those of [1]; no unspecified member of a family is covered. The claimed rank twelve is **geometric**, over \(\mathbf C(v,t)\), and does not assert arithmetic Mordell–Weil rank twelve over \(\mathbf Q(v,t)\). The resolution is not claimed unique or identical, after complex base change, to one particular sequence of six blow-ups chosen in [1].

For the affine base chart define
\[
A(v)=v^8+14v^4+1,\quad B(v)=v(v^4-1),\quad C(v)=v^{12}-33v^8-33v^4+1,
\]
with \(a=481\), \(b=30\), \(c=-4879\). The twenty-four distinct roots of \(J(v)=a^3B(v)^4-b^4A(v)^3\), combined with four choices of \(t\) satisfying \(t^4=C(v)/c\), parameterize all ninety-six nodes by [1, Proposition 7.1]. Each has \(y=0\) and \(x=3a^2C(v)t^2/(cA(v))\).

## Proof

**Arithmetic descent of the ambient construction.** The Weierstrass coefficients are rational polynomials in \(v,t\). Its six base centers comprise a Galois-stable reduced closed subscheme of \(\mathbb F_{3,\mathbf Q}\), including the two conjugate points with \(v=\pm i\). Hence the base blow-up is defined over \(\mathbf Q\). The two singular \(A_2\) curves are the strict transforms of rational boundary sections. Their crepant resolutions are blow-ups of their intrinsically defined reduced singular-curve ideals; [1, Lemmas 6.1–6.2] verify the requisite split local charts and smoothness. Thus \(W_1\) exists projectively over \(\mathbf Q\), is smooth except for exactly ninety-six geometric nodes, and is Gorenstein with trivial dualizing sheaf.

**A rational Weil divisor.** Each of the six chosen section graphs is defined over \(\mathbf Q(i)\). Taking the sum of a graph and its Galois conjugate yields a Weil divisor invariant under \(\operatorname{Gal}(\mathbf Q(i)/\mathbf Q)\), hence a Weil divisor descended to \(\mathbf Q\). This proves that the displayed \(D\) is globally defined over \(\mathbf Q\). Some pairs coincide as divisors and therefore legitimately occur with multiplicity two. Away from the ninety-six nodes, \(W_1\) is smooth, so \(D\) is Cartier there.

**Local signs by two-dimensional tangent planes.** At a geometric node \(p\), the completed local ring is \(\overline{\mathbf Q}[[U,V,Z,T]]/(UV-ZT)\). Its local Weil class group is \(\mathbf Z\); the graph of any section passing through \(p\) is a smooth divisor with class one of the two primitive signs. Its tangent plane defines a line on the projectivized tangent quadric \(\mathbf P^1\times\mathbf P^1\). Two such graph planes correspond to the same sign precisely when they coincide or intersect only at the origin. Write each graph as \((x_j(v,t),y_j(v,t))\) and let \(M_j\) be its \(2\times2\) Jacobian in \((v,t)\) at \(p\). The graph planes intersect in the kernel of \(M_j-M_k\); thus the signs agree if \(M_j=M_k\) or \(\det(M_j-M_k)\ne0\), and disagree if this determinant vanishes with \(M_j\ne M_k\). This rule follows from the two rulings on the smooth tangent quadric and determines relative classes without choosing a global orientation.

**Exhaustive exact certificate.** Equations (7.2)–(7.3) and the table in Appendix B of [1] give the twenty-four \(\mathbf Q(i)\)-valued pairs \((v,\tau)\); the four values \(t=i^k\tau\), \(0\le k<4\), are distinct for each pair. The accompanying script expands each of the six section formulas from [1, (A.2)–(A.6)] and independently checks their Weierstrass identities. In \(\mathbf Q(i)\) it computes all section/node incidences and all corresponding \(2\times2\) Jacobians, including the six conjugate section graphs. It checks consistency of ruling signs for every pair of incident graphs, then sums their signs for the twelve graph terms in \(D\). The complete ninety-six-row certificate verifies exactly \(64\) absolute local classes equal to \(2\) and \(32\) equal to \(4\); none is zero. Reversing the reference ruling reverses every sign at that node but does not alter its absolute class. Since [1, Proposition 7.1] proves that the listed ninety-six points are **all** isolated nodes, this is exhaustive rather than a sample computation.

**Global projective small resolution.** In the completed ordinary-node local ring \(R=\overline{\mathbf Q}[[U,V,Z,T]]/(UV-ZT)\), the divisorial algebra of a primitive local class has relative Proj equal to one of the two standard smooth small resolutions, equivalently the blow-up of the corresponding rank-one ideal. For a nonzero multiple \(e\) of this class, its divisorial algebra is the \(\lvert e\rvert\)-th Veronese of the appropriate signed primitive algebra, up to a principal grading twist, so relative Proj remains that same small resolution. The algebra is finitely generated; completion is faithfully flat, so finite generation and the resulting smooth local model hold in algebraic neighborhoods. As \(D\) is Cartier elsewhere and has nonzero local class at every node, the global sheaf algebra is locally finitely generated, and its relative Proj is a projective morphism, isomorphic off the nodes and resolving each one by a single projective line. It creates no exceptional divisors, hence is crepant for this Gorenstein threefold. The entire graded algebra and its Proj are defined over \(\mathbf Q\); smoothness is checked geometrically and descends.

The zero section is disjoint from the nodes and hence unchanged. The resolution introduces no surface over a point of \(B_{\mathbf Q}\), so fibers remain pure one-dimensional; the smooth total space and smooth base give flatness by miracle flatness, as in [1, Proposition 7.4]. The generic elliptic curve is unchanged, and its geometric rank twelve is [1, Proposition 5.6]. Triviality of the canonical sheaf follows from crepantness and [1, equation (6.4)]; geometric Calabi–Yau vanishing follows from the birational smooth projective model in [1].

## Verification

Run `python verification/verify.py` from a directory containing the bundled `verification/certificate.json` and SymPy (tested with SymPy 1.13 or later). It performs exact rational/Gaussian arithmetic, proves the polynomial identities symbolically, checks all twenty-four distinct discriminant roots and ninety-six nodes, checks the six original section equations, verifies incidence and tangent-quadric ruling consistency, checks conjugation invariance of the absolute local classes, and compares every per-node row against `certificate.json`. Expected output ends with `VERIFY_OK`. The file `verification/certificate.json` records all local incidences, graph signs and classes; its signs use a temporary local reference and are not invariant individually.

## Relationship to prior work

Burek [1, Sections 6–7 and Appendices A–B] proves the complex geometric node classification and constructs projective crepant small resolutions by successively blowing up six section-image divisors over \(\mathbf C\). Section 1.1 expressly takes geometric statements over \(\mathbf C\) unless another field is specified. The tables in [1] establish incidence, not the local *signed* classes of Galois norms. The additional mathematical content here is that the single natural Galois-invariant sum of twelve section graphs has nonzero primitive-multiple class at **every** node, thereby supplying projectivity and descent simultaneously over \(\mathbf Q\). General gluing and relative-ampleness principles, such as [2], explain why projective small resolutions are not automatic, but do not perform this arithmetic computation for the present elliptic model.

## Limitations

The projective resolution is proved to exist, not classified among all possible small-resolution choices. Local class generators have only an unoriented meaning, so the signed values in the certificate are reference-dependent. The class counts and proof use the exact formulas and all ninety-six nodes of this particular model; no analogous statement is asserted for general elliptic Calabi–Yau threefolds. The arithmetic Mordell–Weil group over \(\mathbf Q(v,t)\) is not computed. A differently indexed prior arithmetic treatment could encode the same descent; no claim of priority or independent verification is made.

## References

[1] D. Burek, *An elliptic Calabi–Yau threefold of Mordell–Weil rank twelve*, arXiv:2610.01276v1 (first public 2026-10-01), especially Lemmas 6.1–6.2, Proposition 7.1, Lemmas 7.2–7.3, Proposition 7.4 and Appendices A–B. https://arxiv.org/abs/2610.01276

[2] D. Kaplan and T. Schedler, *Crepant resolutions of stratified varieties via gluing*, arXiv:2311.07539v4, especially the introduction and Section 3.3 on global projectivity. https://arxiv.org/abs/2311.07539
