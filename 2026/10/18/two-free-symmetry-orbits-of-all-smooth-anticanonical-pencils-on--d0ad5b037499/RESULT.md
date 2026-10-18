# Two free symmetry orbits of all-smooth anticanonical pencils on the split quintic del Pezzo surface over \(\mathbf F_3\)

## Finding
Let \(S\) be the split degree-five del Pezzo surface over \(\mathbf F_3\). Precisely **240** two-dimensional \(\mathbf F_3\)-subspaces of \(H^0(S,-K_S)\) have all four rational members geometrically smooth. Under \(\operatorname{Aut}_{\mathbf F_3}(S)\cong S_5\), these pencils comprise **two free orbits of size 120**. Every one has geometrically reduced base scheme consisting of a **single closed point of degree five**, and none extends to a three-dimensional subspace all of whose thirteen rational members are smooth. The four elliptic-fiber rational-point counts distinguish the orbits: \((6,6,6,7)\) and \((5,6,7,7)\).

Representatives have generators \(F,G_A\) or \(F,G_B\), where, over \(\mathbf F_3\),
\[
\begin{aligned}
F&=X^2Z+XY^2-Y^2Z-YZ^2,\\
G_A&=X^2Y-XZ^2+Y^2Z-YZ^2,\\
G_B&=X^2Y-XZ^2-Y^2Z+YZ^2.
\end{aligned}
\]
The corresponding residual closed base points are represented on \(X=1\) by the distinct irreducible degree-five equations
\[
H_A(t)=t^5-t^4-t^3-t+1,\qquad H_B(t)=t^5-t^4-t^3+t^2+1.
\]
These are representatives of the two *pencil* orbits, not a classification of abstract genus-one curves.

## Assumptions and scope
Use the blow-up model \(S=\operatorname{Bl}_{P_1,P_2,P_3,P_4}\mathbf P^2_{\mathbf F_3}\), at the frame \(P_1=(1:0:0)\), \(P_2=(0:1:0)\), \(P_3=(0:0:1)\), \(P_4=(1:1:1)\). Here \(-K_S=3H-E_1-E_2-E_3-E_4\), \((-K_S)^2=5\), and \(h^0(S,-K_S)=6\). Smooth means geometrically smooth over the algebraic closure; an all-smooth pencil has four smooth \(\mathbf F_3\)-rational anticanonical divisors. All counts concern the *fixed embedded split surface*, not equations modulo an unstated equivalence; the two orbit counts explicitly use its full rational automorphism group.

## Proof
**Reduction to six coefficients.** Sections correspond exactly to ternary cubics passing through the four frame points. A basis is
\[
\begin{aligned}
B_1&=Y^2Z-YZ^2,&B_2&=XZ^2-YZ^2,&B_3&=XYZ-YZ^2,\\
B_4&=XY^2-YZ^2,&B_5&=X^2Z-YZ^2,&B_6&=X^2Y-YZ^2.
\end{aligned}
\]
For reproducibility encode \(\sum_{i=1}^6 a_iB_i\) by \(\sum_{i=1}^6 a_i3^{i-1}\), choosing the representative whose last nonzero coefficient is \(1\). The six-dimensional space has \((3^6-1)/2=364\) projective members and \({6\brack2}_3=11011\) projective pencils. A section on the blow-up is a smooth anticanonical curve if and only if its plane cubic is geometrically smooth: a singularity away from the centers remains singular; multiplicity at least two at a center introduces an exceptional component of the total anticanonical divisor; and a smooth cubic has smooth strict transform.

**Exhaustive geometric smoothness and pencil census.** For each of the 364 cubic forms \(f\), compute the homogeneous Jacobian ideal \((f,f_X,f_Y,f_Z)\) over \(\mathbf F_3\). It has no projective geometric zero exactly when the reduced Gröbner leading ideal contains a pure power of each of \(X,Y,Z\); equivalently its homogeneous quotient is Artinian. This gives exactly **132** smooth sections, distributed by their \(\mathbf F_3\)-point counts as \(12\) with five points, \(60\) with six, and \(60\) with seven. Independently, testing \(f=f_X=f_Y=f_Z=0\) over the extensions of degrees \(1,2,3\) returns the identical set of 132. The latter test is exhaustive for plane cubics: a geometrically irreducible singular cubic has a unique rational singular point; a line–conic decomposition has singular points of degree at most two; and a union of three conjugate lines has intersection points of degree at most three. Nonreduced cases are included. The accompanying independent program implements this check without Gröbner bases.

For each unordered independent pair of smooth projective forms, test the other two projective points in its span. Deduplicate the resulting four-element sets. Exactly **240** distinct pencils pass. Testing all nine affine coset points outside each such pencil shows none extends to a projective plane of thirteen smooth forms; every all-smooth net would necessarily contain one of the enumerated pencils.

**Full symmetry and orbit certificate.** Linear coordinate changes preserving the four frame points give an \(S_4\) subgroup. Adjoin the quadratic Cremona involution \((X:Y:Z)\mapsto(YZ:XZ:XY)\), which lifts to an automorphism of the blow-up and acts on the cubic sections as \(f(X,Y,Z)\mapsto f(YZ,XZ,XY)/(XYZ)\). The resulting projective transformations on the six-dimensional section space form a group of order \(120\). The ten \((-1)\)-curves on \(S\) have Petersen incidence graph, whose automorphism group is \(S_5\), bounding the surface-automorphism group by \(120\); hence the generated group is the full one. Its exact action on the 240 pencils gives two orbits of 120, with minimum coefficient-code quadruples \((110,250,357,467)\) and \((110,251,358,465)\). Both stabilizers are trivial. Direct evaluation of the four projective cubics at all thirteen points of \(\mathbf P^2(\mathbf F_3)\) gives the two claimed point-count multisets, invariant within each orbit.

**Geometrically reduced degree-five base schemes.** For the two representative pairs, the gradients are linearly independent at all four fixed frame points: otherwise one of the four rational members would be singular there. Thus the common plane intersection contributes exactly one to Bézout's degree nine at each fixed point, leaving residual intersection degree five. On \(X=1\), elimination of \(Z\) gives, respectively,
\[
\operatorname{Res}_Z(F(1,Y,Z),G_A(1,Y,Z))=Y(Y-1)H_A(Y),
\]
\[
\operatorname{Res}_Z(F(1,Y,Z),G_B(1,Y,Z))=Y(Y-1)H_B(Y).
\]
Their lexicographic Gröbner bases also include \(Z-Y^6+Y^5-Y\) and \(Z+Y^6+Y^4+Y^3-Y\), respectively. The quintics are irreducible over \(\mathbf F_3\) by exact factorization (alternatively, their gcd with both \(t^3-t\) and \(t^9-t\) is one, which suffices in degree five). Hence each residual scheme consists of five distinct Frobenius-conjugate geometric points, and carries no multiplicity. By the two-orbit result, this holds for every qualifying pencil.

## Verification
From this document's accompanying files, run `python src/pencil_census.py`, `python src/orbit_and_base.py`, and `python src/independent_census.py` (Python 3 and SymPy required for the first two). `data/census.json` lists all 132 smooth coefficient codes and all 240 qualifying pencils, and `data/orbits.json` records the two 120-element orbits and the generating six-dimensional transformations. The first program recomputes the entire 364-member Jacobian/11011-pencil census and checks absence of all-smooth nets. The second independently regenerates the complete 120-element automorphism action, tests both quintic eliminants and frame transversality, and checks all four-member point spectra. The third regenerates the smoothness and pencil census using explicit finite extension fields rather than Gröbner bases. These are finite exhaustive proofs supported by the algebraic reduction above, not experimental extrapolations.

## Relationship to prior work
Asgarli–Ghioca investigate pencils all of whose rational hypersurface members are smooth; their 2022 preprint gives general existence results and examples for hypersurfaces, not the sharp classification of anticanonical pencils on a fixed degree-five del Pezzo surface over \(\mathbf F_3\). Their earlier Bertini-type paper instead concerns common transverse hyperplane sections. Candelas–de la Ossa–van Geemen–van Straten discuss the degree-five del Pezzo surface, its \(S_5\) symmetry, and a genus-six Wiman pencil; this does not imply the arithmetic enumeration of anticanonical genus-one pencils here. The result is a fixed-field, fixed-surface classification rather than a new general Bertini theorem.

## Limitations
The numerical classification is restricted to the split quintic del Pezzo surface over \(\mathbf F_3\), and to its four rational members per pencil. Smoothness is not claimed for every geometrically parametrized member of a pencil. The base schemes are geometrically reduced, but their degree-five points need not be conjugate across the two different orbit representatives. The result is not an independent audit of the computational implementations, and an unindexed earlier classification remains a possible priority risk.

## References
1. S. Asgarli and D. Ghioca, *Smoothness in Pencils of Hypersurfaces over Finite Fields*, arXiv:2203.07169v1 (14 March 2022), especially Introduction and Sections 2–3; published in Bull. Aust. Math. Soc. 107 (2023), 85–94.
2. S. Asgarli and D. Ghioca, *A Bertini Type Theorem for Pencils over Finite Fields*, arXiv:2004.03479, Finite Fields Appl. 77 (2022), Article 101936.
3. P. Candelas, X. de la Ossa, B. van Geemen and D. van Straten, *Lines on the Dwork Pencil of Quintic Threefolds*, arXiv:1206.4961 (2012), Sections 3 and 6 on the quintic del Pezzo and its automorphisms.
