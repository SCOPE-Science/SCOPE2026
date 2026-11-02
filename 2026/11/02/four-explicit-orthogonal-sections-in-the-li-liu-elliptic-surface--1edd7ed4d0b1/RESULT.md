# Four explicit orthogonal sections in the Li–Liu elliptic surfaces

## Finding

Let \(g>1\). For the elliptic surfaces of Li and Liu with generic fiber
\[
E/\mathbb C(B):\quad y^2=x^3+(t^2+1)x+1,
\]
where \(B\) is the degree-two hyperelliptic cover specified below, choose the three distinct roots \(a_1,a_2,a_3\) of \(u^3+u+1=0\) and square roots \(b_i\in\mathbb C\) with \(b_i^2=a_i\). Then
\[
P_0=(0,1),\qquad P_i=(a_i,b_i t)\quad(1\le i\le3)
\]
are four explicit sections of the relatively minimal elliptic fibration \(X\to B\), and their geometric intersection and Mordell–Weil height matrices are
\[
P_i\cdot P_j=1\quad(i\ne j),\qquad
\bigl(\langle P_i,P_j\rangle\bigr)_{0\le i,j\le3}=2I_4.
\]
All six pairwise intersections take place **at the single point of the smooth fiber over the ramified point at infinity**, each transversely. All four sections are disjoint from the zero section. Consequently they span a free rank-four subgroup with the displayed orthogonal height lattice, for **every** allowed choice of branch parameters and every \(g>1\). Each is a smooth genus-\(g\) curve with self-intersection \(-1\).

There is a precise rational antecedent: on the same elliptic curve over \(\mathbb C(t)\), the four displayed points span an orthogonal lattice \(I_4\) of **index two** in the full Mordell–Weil lattice. The latter is the classical \(D_4^*\) lattice for a rational elliptic surface with fibers \(I_0^*+6I_1\). The abstract classification of that rational lattice is *prior work*; the explicit coordinates, common intersection locus after hyperelliptic base change, and orthogonal realization are the findings asserted here.

## Assumptions and scope

Work over \(\mathbb C\). Take \(g>1\) and pairwise distinct \(\lambda_1,\ldots,\lambda_{2g+1}\in\mathbb C\) that are neither zero nor roots of \(D(t)=4(t^2+1)^3+27\). Let \(B\) be the smooth projective normalization of
\[
w^2=\prod_{j=1}^{2g+1}(t-\lambda_j).
\]
It has genus \(g\), and \(t:B\to\mathbb P^1\) has degree two and is totally ramified at the unique point \(p_\infty\) above infinity. Let \(X\to B\) be the relatively minimal Jacobian elliptic surface with Weierstrass data \(a_4=t^2+1\), \(a_6=1\) and fundamental line bundle \(\mathcal O_B(p_\infty)\). Li and Liu establish that \(X\) has precisely twelve irreducible nodal fibers of type \(I_1\), is smooth at \(p_\infty\), and has \(\chi(\mathcal O_X)=1\) [1, §3.1; 2, §§2.2–2.3].

The three \(a_i\) are distinct because \(\operatorname{disc}(u^3+u+1)=-31\ne0\), and none is zero. Choose one square root \(b_i\) of each; all four slopes \(0,b_1,b_2,b_3\) are distinct. The result does not claim that the Mordell–Weil rank over \(\mathbb C(B)\) equals four, only that it is at least four.

## Proof

**1. Four algebraic sections.** For \(i\ge1\), the identity \(a_i^3+a_i+1=0\) gives
\[
(b_i t)^2=a_i t^2=a_i^3+(t^2+1)a_i+1.
\]
Thus \(P_i=(a_i,b_i t)\) lies on the generic elliptic curve. The point \(P_0=(0,1)\) is the section already displayed by Li and Liu. A rational point of the generic fiber extends uniquely to a section of the relatively minimal smooth elliptic surface; the explicit regular coordinates near infinity below also show extension there.

**2. Full intersection calculation.** At every finite value of \(t\), the four \(x\)-coordinates \(0,a_1,a_2,a_3\) are distinct. Consequently no distinct pair of the four sections meets over any finite base point, whether the fiber is smooth or nodal. All sections are disjoint from the zero section because they have finite Weierstrass coordinates on the affine base and, by the following local calculation, at infinity.

As \(t\) has a double pole at \(p_\infty\), one may choose a formal local uniformizer \(v\) with \(t=v^{-2}\) (over \(\mathbb C\) a local unit has a square root). In minimal Weierstrass coordinates \(X=v^2x\), \(Y=v^3y\), the equation becomes
\[
Y^2=X^3+(1+v^4)X+v^6.
\]
At \(v=0\) its fiber is the smooth curve \(Y^2=X^3+X\). Indeed, the derivative of its defining equation with respect to \(X\) at \((X,Y)=(0,0)\) is \(-1\). The four sections have local expansions
\[
P_0:\ (X,Y)=(0,v^3),\qquad
P_i:\ (X,Y)=(a_i v^2,b_i v).
\]
All pass through the same smooth point \((0,0)\) of this fiber; none meets the zero section. Since \(Y\) is a local coordinate along the fiber near that point, the difference between any two graph functions in \(Y\) vanishes to order exactly one in \(v\): the four first derivatives are \(0,b_1,b_2,b_3\), distinct. Hence every pair meets once, transversely, at \(p_\infty\), and nowhere else. Thus \(P_i\cdot P_j=1\) for \(i\ne j\), while \(P_i\cdot O=0\).

**3. The height matrix.** The Shioda height pairing on an elliptic surface with section gives, for nonzero distinct \(P,Q\),
\[
\langle P,Q\rangle
=\chi(\mathcal O_X)+(P\cdot O)+(Q\cdot O)-(P\cdot Q)
-\sum_v\operatorname{contr}_v(P,Q),
\]
and
\[
\langle P,P\rangle
=2\chi(\mathcal O_X)+2(P\cdot O)
-\sum_v\operatorname{contr}_v(P).
\]
Here the correction terms vanish because all twelve singular fibers are irreducible type \(I_1\). With \(\chi=1\) and the intersections from Step 2, the matrix is exactly \(2I_4\). This is positive definite, proving independent infinite-order sections. Since a section is isomorphic to \(B\) and its self-intersection is \(-\chi(\mathcal O_X)=-1\), each provides a smooth genus-\(g\) \((-1)\)-curve.

**4. Exact index on the rational antecedent.** Over \(\mathbb P^1_t\), consider the same Weierstrass equation with fundamental line bundle \(\mathcal O_{\mathbb P^1}(1)\). At \(s=1/t=0\), substitute \(x=s^{-2}X\) and \(y=s^{-3}Y\) to obtain
\[
Y^2=X^3+s^2(1+s^2)X+s^6.
\]
The invariant \(c_4\) has order two and the minimal discriminant \(\Delta\) order six at \(s=0\). Thus this fiber is type \(I_0^*\). The degree-six squarefree polynomial \(D(t)\) gives six type-\(I_1\) fibers elsewhere. This is a rational elliptic surface with reducible-fiber root lattice \(D_4\). By Oguiso–Shioda's classical table [3, Main Theorem, row 9], its torsion is zero, its Mordell–Weil rank is four, and the height lattice is \(D_4^*\) with discriminant \(1/4\).

The degree-two map \(B\to\mathbb P^1\) multiplies canonical heights by two. Step 3 therefore gives the four points on the rational antecedent height matrix \(I_4\), of discriminant one. The index of their span in the rank-four lattice \(D_4^*\) is
\[
\sqrt{\frac{1}{1/4}}=2.
\]
This uses the older lattice classification only for the last structural identification; the formulae and incidence of the four actual sections follow independently from Steps 1–3. \(\square\)

## Verification

The standalone file `verify.py` uses exact SymPy polynomial arithmetic to check the cubic and sextic discriminants, the three additional section equations, the minimal local equation at the ramified infinity point, its smoothness, and the rational-at-infinity \((\operatorname{ord}c_4,\operatorname{ord}\Delta)=(2,6)\) computation. It also checks the two claimed Gram determinants using the intersection and height formulas. Run with `python verify.py` in an environment with SymPy installed; the completed run printed `VERIFY_OK`.

The script does not certify the general Kodaira–Néron extension theorem, Shioda's height formula, the old Oguiso–Shioda classification, or the geometric interpretation of local intersection multiplicity. Those are justified mathematically above and by the cited sources, rather than extrapolated from finite experimentation.

## Relationship to prior work

Li and Liu [1,2] introduced these higher-genus elliptic surfaces, verified the twelve nodal fibers and Euler characteristic, and exhibited the single non-torsion section \((0,1)\). Their two inspected versions do not display the three sections \((a_i,b_i t)\), their full intersection pattern, or this explicit orthogonal height matrix. The existence of a rank-four subgroup after degree-two base change can alternatively be inferred *abstractly* from the prior Oguiso–Shioda classification [3] of the rational antecedent: that abstract rank bound is not asserted to be new. The new contribution is the exact **coordinate-level** realization, transversality at the unique smooth infinity fiber for all hyperelliptic bases, and the explicit index-two orthogonal frame on the rational model. No claim of universal historical priority is made.

## Limitations

The argument works over \(\mathbb C\), with the squarefree, discriminant-avoiding hyperelliptic covers specified above. It does not compute the complete Mordell–Weil group over \(\mathbb C(B)\), prove that its rank is exactly four, or classify enhanced-rank specializations. The index-two statement concerns only the rational antecedent over \(\mathbb C(t)\). The published general Mordell–Weil-lattice theory is essential to that index statement, not independently reproved. Historical-priority review and independent mathematical audit remain outstanding.

## References

[1] S. Li and J. Liu, *Examples of infinitely many \((-1)\)-curves with higher genus on elliptic surfaces*, arXiv:2605.27926v1 (publicly submitted 2026-05-27), https://arxiv.org/html/2605.27926v1, construction and proof.

[2] S. Li and J. Liu, same work, arXiv:2605.27926v2 (2026-08-26), https://arxiv.org/html/2605.27926v2, §§2.2–2.3.

[3] K. Oguiso and T. Shioda, *The Mordell–Weil lattice of a rational elliptic surface*, Comment. Math. Univ. St. Paul. **40** (1991), 83–99, https://doi.org/10.14992/00009974, Main Theorem Table row 9 and §3.
