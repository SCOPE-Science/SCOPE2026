# The characteristic-five icosahedral mirrors are all secants of a finite conic

## Finding
For the classical fifteen-line icosahedral reflection arrangement, reduction at the unique prime over five turns the mirror lines into **the complete set of fifteen secants of a smooth six-point conic over \(\mathbb F_5\)**. Its reduced singular locus is exactly every rational point of \(\mathbb P^2(\mathbb F_5)\). There are six fivefold, ten triple and fifteen double intersection points. The radical singular-point ideal is the standard Frobenius determinantal ideal and has the Hilbert–Burch resolution below. The fifteen-line curve has \(\#D(\mathbb F_{5^n})=15\cdot5^n-44\) for all \(n\ge1\).

## Assumptions and scope
Put \(R_0=\mathbb Z[\varphi]\), \(\varphi^2-\varphi-1=0\), and \(\varphi^{-1}=\varphi-1\). This section fixes one standard orthogonal coordinate realization of the \(H_3\) mirror arrangement over \(R_0\): the 15 linear forms have normals the three coordinate vectors and the twelve vectors obtained by cyclic permutation of \((1,\epsilon\varphi,\eta\varphi^{-1})\), for \(\epsilon,\eta\in\{\pm1\}\). The prime \((5,\varphi-3)\) has residue field \(\mathbb F_5\). Our assertions concern its coefficientwise-reduced plane curve \(D\subset\mathbb P^2_{\mathbb F_5}\), its geometric incidence configuration, its **reduced** singular subscheme, and its point counts over extensions. They do not concern a stable reduction of an associated cover or the nonreduced Jacobian singular scheme.

## Proof
**1. Explicit specialization and the conic.** The polynomial \(\varphi^2-\varphi-1\) reduces to \((\varphi-3)^2\) modulo five, so the chosen prime sends \(\varphi\mapsto3\) and \(\varphi^{-1}\mapsto2\). The six points on \(Q:x^2+y^2+z^2=0\) over \(\mathbb F_5\) are exactly
\[
[1:0:2], [1:0:3], [1:2:0], [1:3:0], [0:1:2], [0:1:3].
\]
Indeed, \(-1=4\) is a square, \(Q\) is nonsingular (diagonal quadratic form of nonzero determinant), and every nonsingular conic over \(\mathbb F_5\) has \(5+1=6\) rational points. Pairing the two points on each coordinate line gives the three coordinate mirrors. Pairing points from different coordinate-line pairs produces the other twelve lines; normalization of their cross products gives precisely the twelve cyclic permutations of \((1,\pm3,\pm2)\), regarded as line coefficient triples. There are fifteen distinct cross products, hence every one of the fifteen specialized mirrors is a distinct secant and every conic secant occurs.

**2. Every rational plane point is singular.** A point of \(Q(\mathbb F_5)\) is on five distinct secants (one joining it to each other conic point). The remaining \(25\) rational plane points split into \(15\) exterior points, lying on two secants each, and \(10\) interior points, lying on three secants each. These follow from the standard tangent/secant classification for a nonsingular odd-order finite conic, or can be checked by the explicit six-point list. Thus every point of \(\mathbb P^2(\mathbb F_5)\) is incident with at least two distinct mirror lines, with multiplicity spectrum \(5^6,3^{10},2^{15}\). Conversely, intersection of any two distinct \(\mathbb F_5\)-rational lines is \(\mathbb F_5\)-rational; hence there are no additional geometric singular points. The pair count \(6\binom52+10\binom32+15\binom22=105=\binom{15}2\) independently confirms the exhaustive incidence classification.

**3. Scheme of reduced singular points.** For homogeneous coordinates \(x,y,z\) over \(k=\mathbb F_5\), the set of all \(k\)-rational points of the projective plane is cut out scheme-theoretically by the minors
\[
M_{xy}=x^5y-xy^5,\quad M_{xz}=x^5z-xz^5,\quad M_{yz}=y^5z-yz^5.
\]
Indeed, these say that \([x^5:y^5:z^5]=[x:y:z]\); projective Frobenius-fixed points are exactly \(\mathbb P^2(k)\). The ideal is reduced: on the chart \(x=1\), its equations are \(y^5-y\) and \(z^5-z\), with independent linear terms at each zero, and similarly on the other charts. It is saturated and has codimension two as the ideal of a finite reduced projective set. As the reduced singular locus equals this set, its saturated ideal \(I\) is exactly \((M_{xy},M_{xz},M_{yz})\). These are the maximal minors of the \(2\times3\) matrix with rows \((x,y,z)\) and \((x^5,y^5,z^5)\). The height-two Hilbert–Burch theorem yields a minimal graded resolution
\[
0\longrightarrow R(-7)\oplus R(-11)\longrightarrow R(-6)^3\longrightarrow I\longrightarrow0,
\]
with two explicit syzygies \(zM_{xy}-yM_{xz}+xM_{yz}=0\) and \(z^5M_{xy}-y^5M_{xz}+x^5M_{yz}=0\). Consequently \(H_{R/I}(t)=(1-3t^6+t^7+t^{11})/(1-t)^3\), and the length of the projective point set is \(31\). We make no assertion that the *unreduced* Jacobian singular scheme equals \(I\).

**4. Arithmetic of the reducible curve.** All fifteen lines and all their intersections are defined over \(\mathbb F_5\). Counting each line's \(5^n+1\) rational points and correcting multiple intersections gives
\[
\#D(\mathbb F_{5^n})=15(5^n+1)-\{6(5-1)+10(3-1)+15(2-1)\}=15\cdot5^n-44.
\]
Exponentiating the point-count generating series yields \(Z(D/\mathbb F_5,T)=(1-T)^{44}/(1-5T)^{15}\). The plane curve's arithmetic genus is \((15-1)(15-2)/2=91\), consistent with its ordinary multiple-point singularities and fifteen rational components.

## Verification
`verify_h3_five.py` uses exact modular arithmetic, independently enumerates the 31 rational projective points and the six nonsingular-conic points, constructs the fifteen normal-form mirrors and their fifteen cross-product secants, verifies equality and the \((6,10,15)\) incidence census, checks both Hilbert–Burch syzygies symbolically, and confirms the point-count formula for several extension degrees. Run `python verify_h3_five.py` with Python 3 and SymPy installed. The included `verify_output.txt` is the actual output of this executable. The finite enumeration is a complete finite certificate for the \(\mathbb F_5\) incidence facts; the Frobenius-minor identity, resolution and all-extension point count follow from the proofs above, not numerical extrapolation.

## Relationship to prior work
Hirzebruch's 1984 report lists the classical icosahedral arrangement as \(15\) lines with intersection counts \((t_2,t_3,t_5)=(15,10,6)\). Ehrenborg, Klivans and Reading (2015) discuss Coxeter arrangements in dimension three. Calvo (2022), Section 2 and its subsequent discussion of the invariant conic, studies this \(H_3\) configuration over \(\mathbb C\), describing its fifteen mirrors, thirty-one points and orthogonal quadratic invariant. None of these inspected accounts asserts the characteristic-five specialization into the complete \(\mathbb F_5\)-conic secant arrangement, or the resulting Frobenius-minor radical singular ideal. The general incidence and Hilbert–Burch facts are classical; the claimed specific contribution is their identification with the modular \(H_3\) arrangement. Priority outside the inspected material is not settled.

## Limitations
This is a specific coefficientwise reduction over the ramified prime above five, not a classification of reductions at every prime. The radical singular ideal is not asserted to equal the full nonreduced Jacobian ideal, and the ordinary-singular-curve zeta function is not a zeta function of a normalization or its Jacobian. The specialized incidence multiplicities coincide numerically with the classical arrangement; the arithmetic significance is the special alignment with the \(\mathbb F_5\)-conic and the entire finite projective plane. Independent validation has not been performed.

## References
- F. Hirzebruch, *Algebraic surfaces with extreme Chern numbers*, MPI/SFB 84-43 (1984), Section 3(f). https://archive.mpim-bonn.mpg.de/id/eprint/3531/1/preprint_1984_43.pdf
- R. Ehrenborg, C. Klivans and N. Reading, *Coxeter arrangements in three dimensions*, arXiv:1501.05991, originally submitted 2015-01-24. https://arxiv.org/abs/1501.05991
- S. Calvo, *The icosahedral line configuration and Waldschmidt constants*, arXiv:2209.01499v1 (2022), Sections 2 and 4. https://arxiv.org/pdf/2209.01499
- J. Baez, *Discriminant of the Icosahedral Group*, 2016-05-15. https://blogs.ams.org/visualinsight/2016/05/15/discriminant-of-the-icosahedral-group/
