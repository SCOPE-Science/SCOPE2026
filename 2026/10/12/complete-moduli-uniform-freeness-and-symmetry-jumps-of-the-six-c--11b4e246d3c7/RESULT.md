# Complete moduli, uniform freeness, and symmetry jumps of the six-chord conic arrangements

## Finding

**Theorem.** Let \(\mathcal A\subset\mathbb P^2_{\mathbb C}\) be a reduced union of exactly six distinct lines and one smooth conic. Suppose its entire singular set comprises precisely three ordinary double points and four ordinary quadruple points (all with distinct branch tangents). Then, up to a projective change of coordinates, \(\mathcal A\) has equation
\[
f_\lambda=xyz(x-y)(x-z)(y-z)\bigl(xy-\lambda xz+(\lambda-1)yz\bigr)=0,
\qquad \lambda\in\mathbb C\setminus\{0,1\}.
\]
Two such equations represent projectively equivalent unlabelled arrangements exactly when their parameters differ by an anharmonic transformation:
\[
\lambda\longmapsto \lambda,\quad1-\lambda,\quad \frac1\lambda,\quad
\frac1{1-\lambda},\quad\frac{\lambda}{\lambda-1},\quad
\frac{\lambda-1}{\lambda}.
\]
The quotient parameter
\[
j(\lambda)=256\frac{(1-\lambda+\lambda^2)^3}{\lambda^2(1-\lambda)^2}
\]
identifies its coarse projective moduli space with \(\mathbb A^1_{\mathbb C}\). **Every** member is a free degree-eight curve with \(\operatorname{mdr}(f_\lambda)=2\) and free exponents \((2,5)\). Its full projective stabilizer is
\[
\operatorname{Aut}_{\mathbb P^2}(\mathcal A_\lambda)\cong
\begin{cases}
C_2\times C_2,&j(\lambda)\notin\{0,1728\},\\
D_4,&j(\lambda)=1728,\\
A_4,&j(\lambda)=0.
\end{cases}
\]
The harmonic locus is \(\lambda\in\{-1,1/2,2\}\); the equianharmonic locus is \(\lambda^2-\lambda+1=0\). These are the only stabilizer jumps.

## Assumptions and scope

All curves, points, projective equivalences, stabilizers and singularity calculations are over the algebraically closed field \(\mathbb C\), in characteristic zero. “Ordinary quadruple” means a reduced local germ with four smooth branches and four pairwise distinct tangent directions; the same convention applies to nodes. No freeness hypothesis is imposed on the initial arrangement. The source classification uses the weak singularity count \((1,6;3,0,4)\); this theorem concerns **all** its complex realizations, not merely a previously exhibited example. The degree-eight curve has one conic component, and its remaining six irreducible components are lines.

## Proof

**1. Intrinsic recovery of the conic points.** Let \(q\) denote the number of ordinary quadruple points lying on the unique conic, and let \(n\) be the number of nodes lying on it. At a quadruple point of the total curve on the conic there are exactly three transverse line branches; at a node on the conic there is one transverse line branch. Bézout's theorem applied to the six lines gives \(3q+n=2\cdot6=12\). Since \(0\le q\le4\) and \(0\le n\le3\), either \((q,n)=(4,0)\) or \((3,3)\). The second is impossible. Indeed, its one quadruple point away from the conic would be the concurrence of four of the lines. Outside that concurrence, a triple intersection of lines must contain **both** remaining lines, hence can occur at most once (they meet at one point). But the three quadruple points on the conic would each require a distinct triple intersection of lines. Therefore all four quadruple points lie on the conic, and all three nodes lie off it.

**2. Forcing the complete quadrangle.** At each of the four marked conic points, three of the six distinct lines pass through it. This gives twelve line–point incidences. A line meets the smooth conic in at most two distinct points; since there are six lines, all six meet precisely two marked points each. No two lines can connect the same pair. Consequently the six lines are **all** the chords joining the four marked points pairwise, which are in general position because no line meets the conic in three distinct points. Their remaining intersections are the three diagonal points of a complete quadrangle; they are distinct ordinary nodes off the conic. Each chord meets the conic transversely at both endpoints, so all four points are ordinary quadruple points. This also proves the converse: every smooth conic through four projectively general points, together with the six joining chords, has exactly the required weak singularity count.

**3. Explicit moduli and equivalence.** There is a unique projective coordinate frame sending the four **ordered** marked points to \([1:0:0],[0:1:0],[0:0:1],[1:1:1]\). Their six chords then have product \(L=xyz(x-y)(x-z)(y-z)\). A homogeneous quadratic vanishing at the first three points is \(a xy+b xz+c yz\); it passes through the fourth precisely when \(a+b+c=0\). Its symmetric matrix has determinant \(abc/4\), so it is smooth exactly when \(abc\neq0\). After scalar normalization \(a=1\), write \(b=-\lambda\), \(c=\lambda-1\); smoothness is precisely \(\lambda\neq0,1\). The restriction of projective equivalences to the unique conic is the Möbius action on its four marked points. Their unordered cross-ratio is represented by \(\lambda\), and permutations yield exactly the six anharmonic values displayed above. Conversely every such permutation of the four conic points lifts, through the quadratic Veronese embedding, to a projectivity of the plane sending its six chords and conic to the corresponding arrangement. The familiar anharmonic invariant \(j\) separates these finite orbits and assumes every finite complex value. Thus it provides precisely the coarse affine moduli parameter, including the special stabilizer strata.

**4. Uniform Jacobian syzygy.** Put \(S=x+y+z\), \(E=x\partial_x+y\partial_y+z\partial_z\), and \(D=x^2\partial_x+y^2\partial_y+z^2\partial_z\). The six-chord product satisfies \(D(L)=3SL\). For \(Q=xy-\lambda xz+(\lambda-1)yz\), the coefficient identity \(1-\lambda+(\lambda-1)=0\) gives \(D(Q)=SQ\), hence \(D(f_\lambda)=4Sf_\lambda\) and \(E(f_\lambda)=8f_\lambda\). Therefore \((2D-SE)f_\lambda=0\), an exact degree-two Jacobian relation with coefficient triple
\[
\bigl(x(x-y-z),\ y(y-x-z),\ z(z-x-y)\bigr).
\]
There is no nonzero degree-one Jacobian relation: exponentiating such a homogeneous linear derivation would produce a nontrivial positive-dimensional projective subgroup preserving this reduced curve. But the singularity type forces the group to permute its four projective-frame quadruple points, hence its projective stabilizer injects into the finite group \(S_4\). A linear derivation acting trivially projectively is a scalar multiple of \(E\), and its action on a degree-eight equation cannot vanish unless the scalar is zero. A constant-coefficient relation would, after multiplication by any linear form, give a forbidden linear relation. Thus \(\operatorname{mdr}(f_\lambda)=2\) for **all** admissible complex parameters.

Each ordinary node has Tjurina number \(1\), and each ordinary quadruple point has Tjurina number \((4-1)^2=9\); hence \(\tau(f_\lambda)=3+4\cdot9=39\). The standard free-curve numerical criterion with degree \(8\) and \(r=2\le(8-1)/2\) reads \((8-1)^2-2(8-2-1)=49-10=39\). Thus every member is free with exponents \((2,5)\).

**5. Full automorphism groups.** The four ordinary quadruple points are intrinsic, and lie on the unique conic. A projectivity preserving the arrangement must permute them, giving an injection of its stabilizer into \(S_4\). Every Möbius symmetry of the four-point subset of the conic extends uniquely under its quadratic Veronese embedding to a projectivity of the plane; it preserves every chord, so these are all stabilizer elements. The permutation homomorphism \(S_4\to S_3\) for the anharmonic action has Klein-four kernel. For six distinct anharmonic values, the stabilizer is the kernel \(V_4\); for three values (the harmonic parameters \(-1,1/2,2\)), the full preimage of an order-two subgroup is \(D_4\); for two values (roots of \(\lambda^2-\lambda+1\)), the preimage of an order-three subgroup is \(A_4\). These cases exhaust all possible collisions among the six values.

## Verification

The self-contained `verify.py` uses only the Python standard library and carries out exact polynomial arithmetic in \(\mathbb Z[x,y,z,\lambda]\). Run it using `python3 verify.py`. It verifies the identities \(D(L)=3SL\), \(D(Q)=SQ\), \(E(f)=8f\), and the entire quadratic syzygy coefficient by coefficient. It independently enumerates all pairwise six-line intersections as four triple-line points and three double-line points; evaluating the conic at an admissible rational parameter separates the types. Rational examples confirm the six-value generic orbit, three-value harmonic orbit and the invariance of \(j\). The mathematical argument above, rather than finite specialization, establishes the universal complex statement, the absence of degree-one syzygies, and the equianharmonic case.

## Relationship to prior work

Pokora (arXiv:2312.13052v1, Section 3, six-line case) established an explicit **harmonic** example with singularity counts \((3,0,4)\) and freeness; the present theorem does not claim that example or the numerical freeness criterion as novel. Janasz–Pokora (arXiv:2512.24707v2, Remark 3.5 and Example 4.5) repeated its specific model and established broader numerical constraints for maximal ordinary arrangements, but did not classify the full projective family or prove that every realization is free. The complete-quadrangle construction and cross-ratio/anharmonic identities are standard classical projective geometry. The contribution here is the forcing of **all** such weak-combinatorial realizations into that family, a universal freeness proof, and the associated complete projective-moduli and symmetry stratification. A separate earlier geometric study established the order-eight stabilizer of Pokora's single harmonic member; this isolated special case is included and expressly not claimed anew.

## Limitations

The theorem is over \(\mathbb C\) in characteristic zero, with smooth irreducible conic and the exact specified singularity count. It does not classify degenerate conics, collisions of the four points, other weak combinatorics, or integral/arithmetic forms. The six-value orbit and affine \(j\)-parameter are classical mathematics, not new modular invariants. No independent mathematical audit has been performed. Historical classification material, notably M. Neusel's 1992 thesis on line-and-conic configurations with tree resolutions, was not available in full text; its possible overlap is a bibliographic limitation, and searches alone do not establish novelty.

## References

- P. Pokora, *Freeness of arrangements of lines and a conic with ordinary quasi-homogeneous singularities*, first public version, arXiv:2312.13052v1, 20 December 2023, especially Theorem 1.3 and Section 3 (six-line example). https://arxiv.org/html/2312.13052v1
- W. Janasz and P. Pokora, *On \(\mathcal M\)-arrangements of conics and lines with ordinary singularities*, arXiv:2512.24707v2, especially Remark 3.5 and Example 4.5 (later comparison). https://arxiv.org/html/2512.24707v2
- E. W. Weisstein, *Complete Quadrangle*, MathWorld, standard terminology and geometry. https://mathworld.wolfram.com/CompleteQuadrangle.html
- M. Neusel, *Konfigurationen von Geraden und einer Quadrik mit Baumauflösung – ein Bilderbuch*, Göttingen doctoral thesis, 1992 (cited by Pokora; original full text not inspected).
