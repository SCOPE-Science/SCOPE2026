# The \(D_4^*\) section lattice and a 24-cell of higher-genus \((-1)\)-curves

## Finding
For every integer \(g\ge2\), the Li--Liu elliptic surface described below contains a canonical (by descent) rank-four Mordell--Weil subgroup with height lattice \(2D_4^*\), where \(2D_4^*\) denotes the standard \(D_4^*\) lattice with its bilinear form multiplied by two. The subgroup has precisely 24 height-two nonzero elements. Their sections are distinct smooth genus-\(g\) curves of self-intersection \(-1\), disjoint from the zero section. For any one of these 24 curves, exactly \(8,6,8,1\) of the other 23 meet it with intersection numbers \(0,1,2,3\), respectively. The inherited height pairing has determinant \(4\). In particular, the full Mordell--Weil group has rank at least four.

## Assumptions and scope
Work over \(\mathbb C\). Fix an integer \(g\ge2\) and distinct \(\lambda_1,\ldots,\lambda_{2g+1}\in\mathbb C\) outside the zero set of \(4(t^2+1)^3+27\) and outside \(\{0\}\). Let \(B\) be the smooth projective curve with function field \(\mathbb C(t,w)\), \(w^2=\prod_i(t-\lambda_i)\), and let \(f:B\to\mathbb P^1\) be its degree-two map. It has genus \(g\) and is ramified at infinity. Let \(X\to B\) be the smooth relatively minimal Jacobian elliptic surface with generic fiber
\[
y^2=x^3+(t^2+1)x+1.
\]
This is the explicit construction in Li--Liu, Section 2.2. Denote its zero section by \(O\), its Mordell--Weil group by \(\operatorname{MW}(X/B)\), and the geometric intersection of sections by \(P\cdot Q\). Let \(S\to\mathbb P^1\) denote the relatively minimal Jacobian elliptic surface with the same equation over \(\mathbb C(t)\). The inherited subgroup means the image of \(E(\mathbb C(t))\hookrightarrow E(\mathbb C(B))\). We do not claim it is the full Mordell--Weil group.

## Proof
**1. The rational ancestor has a \(D_4\) reducible fiber.** Its affine discriminant is
\[
\Delta=-16\bigl(4(t^2+1)^3+27\bigr).
\]
The polynomial \(D(t)=4(t^2+1)^3+27\) has six simple roots: \(D'(t)=24t(t^2+1)^2\), but \(D(0)=31\), and \(D(\pm i)=27\). These are six Kodaira \(I_1\) fibers. At infinity put \(s=1/t\), \(X=s^2x\), \(Y=s^3y\); the minimal local Weierstrass form becomes
\[
Y^2=X^3+(s^2+s^4)X+s^6.
\]
Here the local vanishing orders of \(c_4,c_6,\Delta\) are \(2,6,6\), respectively, with \(s^{-6}\Delta\) a unit. The Kodaira--Tate classification therefore gives a single \(I_0^*\) fiber (five components), with root lattice \(D_4\). The fundamental line bundle over \(\mathbb P^1\) has degree one; the surface has \(\chi(\mathcal O_S)=1\), and its canonical bundle is negative on the base. By the classification of elliptic surfaces with section, \(S\) is rational; hence \(\rho(S)=10\) and \(\operatorname{NS}(S)\) is unimodular.

**2. The complete ancestor Mordell--Weil lattice.** Shioda--Tate gives
\[
\operatorname{rank}E(\mathbb C(t))=10-2-(5-1)=4.
\]
For a nonzero section \(P\), Shioda's height formula and the \(I_0^*\) correction table give
\[
\langle P,P\rangle_S=2+2(P\cdot O)-\operatorname{contr}_{\infty}(P)\ge1,
\]
because \(P\cdot O\ge0\) and the correction of a section at an \(I_0^*\) fiber is at most one. Thus no nonzero section is torsion. The Oguiso--Shioda classification, or the primitive \(D_4\subset E_8\) embedding and dual-lattice description of the Mordell--Weil pairing, identifies the complete rank-four height lattice with \(D_4^*\). Equivalently, its determinant is \(1/4\), and its minimum squared norm is one. The minimum vectors are the eight \(\pm e_i\) and the sixteen \((\pm1/2,\pm1/2,\pm1/2,\pm1/2)\), in the standard Euclidean model of \(D_4^*\).

**3. Ramified base change scales height by two.** The extension \(\mathbb C(t)\subset\mathbb C(B)\) has degree two, so the map on rational points is injective. The six nodal fibers split into twelve \(I_1\) fibers, as the finite branch points avoid the discriminant. At the branch point at infinity, quadratic ramification changes the \(I_0^*\) fiber to a smooth fiber after minimalization (the corresponding exponent-two base-change case in the Kodaira table). Consequently, \(X\to B\) has twelve \(I_1\) fibers, no reducible fibers, and \(\chi(\mathcal O_X)=1\). The canonical height pairing on points coming from \(\mathbb C(t)\) multiplies by the extension degree two. Therefore the inherited lattice is \(2D_4^*\), of determinant \(2^4/4=4\), and all its 24 minimum nonzero elements have height two.

**4. Incidence of the 24 genus-\(g\) curves.** Every section of \(X\) is isomorphic to \(B\), hence smooth of genus \(g\), and has self-intersection \(-\chi(\mathcal O_X)=-1\). Since all singular fibers are irreducible, Shioda's height formula for a nonzero section \(P\) is \(\langle P,P\rangle_X=2+2(P\cdot O)\). Thus any inherited minimum section has \(P\cdot O=0\). For two distinct such sections \(P,Q\), the bilinear formula reduces to
\[
P\cdot Q=1-\langle P,Q\rangle_X=1-2(v_P\cdot v_Q),
\]
where \(v_P,v_Q\) are the corresponding unit vectors in \(D_4^*\). Fix one unit vector. Among the other 23, exactly eight have Euclidean inner product \(1/2\), six have inner product \(0\), eight have inner product \(-1/2\), and one is its negative and has inner product \(-1\). Hence intersection numbers \(0,1,2,3\) occur with multiplicities \(8,6,8,1\), respectively, proving the claim.

## Verification
The accompanying standalone `verify.py` checks the sextic discriminant and its square-freeness, the order-six discriminant at infinity, the rank arithmetic, the determinant of a \(D_4\) Cartan matrix, all 24 minimum dual vectors, their 23-neighbor intersection multisets, and the scaled height-lattice determinant. Run `python verify.py` with Python and SymPy installed. These computations verify exact polynomial and finite-lattice steps; the geometric statements about fibers, Mordell--Weil lattices, and height functoriality use the cited theorems rather than finite experimentation.

## Relationship to prior work
Li and Liu construct the hyperelliptic-base elliptic surface and exhibit one non-torsion section, proving the existence of infinitely many genus-\(g\) \((-1)\)-curves. Their text does not identify a complete inherited rank-four Mordell--Weil lattice or a 24-curve intersection configuration. The results of Oguiso--Shioda and Schütt--Shioda classify rational elliptic-surface Mordell--Weil lattices and ramified base change; they provide the classical machinery for identifying the rational ancestor, but do not state this genus-\(g\) curve configuration on the Li--Liu family. The extra geometric assertion is the identified 24-element minimum shell and its uniform intersection numbers on the base-changed surfaces.

## Limitations
This theorem determines the subgroup descended from the rational ancestor, not the full Mordell--Weil group after base change. In particular it does not assert that no other height-two sections exist, that the full Mordell--Weil rank equals four, or that the listed 24 curves exhaust any curve-theoretic classification. Its proof relies on standard Kodaira fiber and Mordell--Weil lattice classifications; the novelty of applying those theories to this explicit 2026 construction is subject to normal literature-priority uncertainty.

## References
S. Li and J. Liu, *Examples of infinitely many \((-1)\)-curves with higher genus on elliptic surfaces*, arXiv:2605.27926v1 (27 May 2026), revised v2 (26 Aug 2026), Sections 2.2--2.3. M. Schütt and T. Shioda, *Elliptic Surfaces*, arXiv:0907.0298v3, Sections 5 and 11, especially the ramified-base-change table and the Mordell--Weil height/correction formulas. K. Oguiso and T. Shioda, *The Mordell-Weil lattice of a rational elliptic surface*, Comment. Math. Univ. St. Pauli **40** (1991), 83--99, the root-\(D_4\) case.
