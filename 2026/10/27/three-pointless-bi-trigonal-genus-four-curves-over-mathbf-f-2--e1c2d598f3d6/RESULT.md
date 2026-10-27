# Three pointless bi-trigonal genus-four curves over \(\mathbf F_2\)

## Finding
Among all geometrically smooth curves of bidegree \((3,3)\) in the split quadric \(Q=\mathbf P^1_{\mathbf F_2}\times\mathbf P^1_{\mathbf F_2}\) having no \(\mathbf F_2\)-rational point, there are exactly **three** \(\mathbf F_2\)-isomorphism classes. There are exactly 84 defining nonzero bihomogeneous sections, partitioned into orbits of sizes 24, 24, and 36 under the order-72 group of \(\mathbf F_2\)-automorphisms of \(Q\). The respective geometric curve automorphism groups over \(\mathbf F_2\) have orders 3, 3, and 2.

Representatives, expressed by four-digit hexadecimal coefficient masks, and their point-count fingerprints are:

| Mask | Number of equations in orbit | Rational automorphisms | \(\#C(\mathbf F_2),\#C(\mathbf F_4),\#C(\mathbf F_8),\#C(\mathbf F_{16})\) |
| --- | ---: | ---: | --- |
| `b0bd` | 24 | 3 | \((0,2,18,18)\) |
| `b0db` | 24 | 3 | \((0,0,18,12)\) |
| `b1cb` | 36 | 2 | \((0,2,21,26)\) |

## Assumptions and scope
Work over \(k=\mathbf F_2\), and use coordinates \(([S:T],[U:V])\) on \(Q\). A coefficient mask \(m\in\{0,\ldots,65535\}\) encodes
\[
F_m=\sum_{i,j=0}^{3}\epsilon_{4i+j} S^{3-i}T^i U^{3-j}V^j,\qquad \epsilon_r\in\mathbf F_2,
\]
with \(\epsilon_r\) the binary digit in position \(r\). In code, monomials and masks are literal machine notation. A 'pointless curve' means \(F_m(P)\neq0\) at all nine points \(P\in Q(\mathbf F_2)\). A 'smooth curve' means geometric smoothness over \(\overline{\mathbf F}_2\), not merely smoothness at rational points. The classification is for smooth curves on the **split** quadric, not all abstract genus-four curves over \(\mathbf F_2\). These models are nonhyperelliptic canonical curves of genus four with two rational degree-three maps.

## Proof
**1. Exhaustion of point-free equations.** In degree three, evaluation of homogeneous binary cubics at the three points of \(\mathbf P^1(\mathbf F_2)\) has rank three: the evaluations of \(S^3\), \(T^3\), and \(S^2T\) (or any suitable interpolating basis) span all functions on this three-point set. Their tensor products give a rank-nine evaluation map
\[
H^0(Q,\mathcal O_Q(3,3))\longrightarrow \mathbf F_2^{Q(\mathbf F_2)}=\mathbf F_2^9.
\]
The source has dimension 16. The requirement that all nine values equal 1 therefore has exactly \(2^{16-9}=128\) solutions, none zero. The script `proof_checker.py` generates this affine fibre directly and verifies its cardinality.

**2. Geometric smoothness is decidable by four unit-ideal computations.** Cover \(Q\) by the four standard affine charts, using the two local affine parameters \(x,y\). Write \(f\) for the dehomogenization of \(F_m\). At a geometric point of a smooth surface, the hypersurface \(f=0\) is singular precisely if \(f=f_x=f_y=0\). Such a geometric point exists exactly when the affine ideal \((f,f_x,f_y)\) is proper in \(\mathbf F_2[x,y]\), equivalently (by the algebraic Nullstellensatz) when its reduced Gröbner basis is not the unit ideal. All 128 candidates are tested exactly in all four charts over \(\mathbf F_2\), producing precisely **84** for which all four ideals are the unit ideal; the other 44 have a geometric singularity. This is an exhaustive algebraic proof, not an inference from low-degree point tests. The independent finite-field C implementation detects singular points of all 44 rejected masks over degrees at most six and independently reproduces the same 84 accepted masks; its bounded search is corroborating rather than the logical certificate of smoothness.

**3. Complete orbit enumeration.** \(\operatorname{Aut}_k(Q)=(\operatorname{PGL}_2(k)\times\operatorname{PGL}_2(k))\rtimes C_2\) has order \(6\cdot6\cdot2=72\). The changes \((S,T)\mapsto(S+T,T)\) and \((S,T)\mapsto(T,S)\), their analogues on \((U,V)\), and factor interchange generate this full group. Expanding their actions on the sixteen monomials over \(\mathbf F_2\) gives five exact 16-bit linear transformations. Breadth-first generation on the entire 84-element admissible set yields three orbits, represented by `b0bd`, `b0db`, and `b1cb`, with cardinalities 24, 24, and 36. The three sizes sum to 84; the stabilizer orders by orbit-stabilizer are 3, 3, and 2.

**4. Curve isomorphisms and genus.** Adjunction on \(\mathbf P^1\times\mathbf P^1\) gives \(2g-2=(3,3)\cdot(1,1)=6\), so \(g=4\). The adjunction canonical series is \(\mathcal O_C(1,1)\) and embeds each smooth \((3,3)\) curve in \(\mathbf P^3\), since it is a complete intersection of a smooth quadric and a cubic. Its containing quadric is unique: the degree-two part of the ideal is one-dimensional. Every isomorphism of such genus-four curves respects their canonical embeddings, hence carries the unique containing quadric to the unique containing quadric and is induced by an automorphism of the split quadric. Thus the three computed ambient orbits are precisely the three abstract \(k\)-isomorphism classes; the stabilizer orders are the abstract \(k\)-automorphism-group orders.

**5. Arithmetic witnesses.** Enumerating the \((2^r+1)^2\) points of the split quadric over \(\mathbf F_{2^r}\) for \(r=1,2,3,4\), and evaluating the representative forms by exact finite-field arithmetic, gives the four extension-point counts tabulated above. The three distinct sequences independently separate the isomorphism classes.

## Verification
Run `python3 proof_checker.py` with SymPy installed. It recomputes all 128 point-free forms, verifies geometric smoothness by four exact Gröbner bases for each, constructs projective-group orbits, and verifies the three point-count vectors. Independently compile `cc -O2 independent_check.c -o independent_check` and run `./independent_check > masks.txt`; compare `masks.txt` byte-for-byte with `smooth_masks.txt`. The C checker searches for singularities through extension degree six and must yield exactly 84 surviving masks; its 84 masks agree with the algebraically certified set. The degree-six bound in C does not replace the unbounded geometric correctness of the Gröbner calculation. The original source was run, compared with the independent implementation, and the final embedded scripts are supplied for reproducibility.

## Relationship to prior work
Faber and Grantham (arXiv:2005.07054; first publicly posted May 14, 2020) describe smooth canonical genus-four curves on split quadrics and investigate maximum rational-point counts at fixed gonality. Their structural characterization of the two-ruling case is used here; their stated extremal rational-point results neither give the present zero-point count nor classify the three point-free isomorphism classes. Faber, Grantham and Howe (arXiv:2207.14307, first posted July 28, 2022) study excessive gonality; their main classification is a different problem. Howe, Lauter and Top (arXiv:math/0403178) establish existence of pointless genus-four curves; existence does not imply this complete classification of the two-ruling locus.

## Limitations
The classification applies only to the split-canonical-quadric, bidegree-\((3,3)\) locus over \(\mathbf F_2\); it says nothing about genus-four curves on nonsplit quadrics, quadric cones, or hyperelliptic genus-four curves. The calculations classify equations and ordinary \(\mathbf F_2\)-isomorphisms, not twists over all extensions or their full geometric automorphism groups. Published computational databases could contain equivalent information not found in the inspected prose: originality is provisionally assessed and not independently audited.

## References
1. X. Faber and J. Grantham, *Binary Curves of Small Fixed Genus and Gonality with Many Rational Points*, arXiv:2005.07054 (2020), especially the genus-four canonical-quadric discussion.
2. X. Faber, J. Grantham and E. W. Howe, *On the Maximum Gonality of a Curve over a Finite Field*, arXiv:2207.14307 (2022).
3. E. W. Howe, K. E. Lauter and J. Top, *Pointless Curves of Genus Three and Four*, arXiv:math/0403178 (2004).
