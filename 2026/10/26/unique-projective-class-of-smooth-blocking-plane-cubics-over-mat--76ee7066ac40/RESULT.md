# Unique projective class of smooth blocking plane cubics over \(\mathbf F_3\)

## Finding

Let \(C\subset\mathbf P^2_{\mathbf F_3}\) be a geometrically smooth plane cubic. Say that \(C\) is **blocking** when every line defined over \(\mathbf F_3\) contains an \(\mathbf F_3\)-rational point of \(C\). Then **every such blocking cubic is projectively equivalent over \(\mathbf F_3\)** to
\[
C_0:\quad Y^2Z-X^3-X^2Z+XZ^2=0.
\]
There are precisely \(936\) such projective cubic equations up to nonzero scalar multiplication, forming one orbit of \(\operatorname{PGL}_3(\mathbf F_3)\). Equivalently, there are \(1872\) nonzero cubic coefficient vectors representing them. The rational projective automorphism group of the embedded curve has order \(6\).

Every smooth blocking cubic has exactly six rational points. Its thirteen rational lines meet the rational point set in one, two, or three points with respective frequencies \(6,3,4\). This is a **classification of embedded plane cubics**, not an assertion about every elliptic curve of the same point count or every genus-one embedding.

## Assumptions and scope

All curves are projective hypersurfaces over the field \(\mathbf F_3\), with geometric smoothness meaning smoothness after extension to an algebraic closure. A cubic equation is counted up to multiplication by either of the two nonzero scalars only in the projective-equation count; the coefficient-vector count distinguishes both. Projective equivalence is by \(\operatorname{PGL}_3(\mathbf F_3)\), not by geometric automorphisms or abstract curve isomorphisms. Only degree-three plane curves over this specific field are classified.

## Proof

**(1) Exhaustive finite parameter space.** The \(10\) degree-three monomials \(X^aY^bZ^c\) with \(a+b+c=3\) form a basis of the ternary cubic equations. Hence there are exactly \(3^{10}-1=59048\) nonzero equations. The projective plane and its dual each have \(13\) rational points. Enumerating each equation on all thirteen points, then requiring a zero on each of the thirteen rational lines, produces exactly \(9880\) blocking coefficient vectors. This part is independent of smoothness.

**(2) Geometric smoothness without an unjustified field cutoff.** For a plane cubic over \(\mathbf F_3\), geometric singularity can be detected over \(\mathbf F_9\) or \(\mathbf F_{27}\). To see why, a geometrically integral singular cubic has arithmetic genus one, so the sum of the local geometric delta-invariants is at most one; the unique possible singular geometric point is consequently Frobenius-fixed. For a geometrically reducible cubic, its components over the algebraic closure have degrees \(1+2\) or \(1+1+1\), or include a repeated line. In the first case, component intersection points have closed-point degrees at most two by Bézout, while pairwise intersections in the second case occur over extensions of degree at most three because the component lines have Galois orbits of length at most three. Repeated components have geometric singular points already over an extension of degree at most three. Thus every singular cubic has a singular point with residue degree one, two, or three.

The first exact checker constructs \(\mathbf F_9=\mathbf F_3[t]/(t^2+1)\) and \(\mathbf F_{27}=\mathbf F_3[t]/(t^3-t-1)\), evaluates the equation and all three first derivatives at all projective points over both fields, and retains the coefficient vectors for which no common zero occurs. The resulting subset consists of **exactly \(1872\)** blocking vectors, all having six rational points. The second checker independently obtains the same number by Gröbner-basis tests on the three projective charts, directly over the algebraic closure (via the unit-ideal criterion).

**(3) Projective orbit.** For each of the \(1872\) vectors, scale the first nonzero coefficient to one. This gives \(936\) distinct projective equations. The transformations swapping \(X,Y\), swapping \(Y,Z\), replacing \(X\) by \(X+Y\), and replacing \(X\) by \(-X\) generate \(\operatorname{GL}_3(\mathbf F_3)\), by elementary Gaussian elimination and coordinate permutations. Exact substitution of these generators into the ten monomials, followed by orbit traversal, puts all \(936\) projective equations in **one orbit**. Since
\[
|\operatorname{PGL}_3(\mathbf F_3)|
=\frac{(3^3-1)(3^3-3)(3^3-3^2)}{3-1}=5616,
\]
the projective stabilizer has order \(5616/936=6\). The displayed representative belongs to this orbit and is tested to be smooth and blocking.

**(4) Incidence refinement.** Let \(t_j\) denote the number of rational lines containing exactly \(j\) rational points of a smooth blocking cubic. Smoothness and Bézout preclude four collinear rational points, and blocking precludes zero intersections. The census gives six points; hence
\[
t_1+t_2+t_3=13,\quad
 t_1+2t_2+3t_3=6\cdot4=24,\quad
 t_2+3t_3=\binom 62=15.
\]
Solving yields \((t_1,t_2,t_3)=(6,3,4)\).

## Verification

Run `python blocking_cubic_classify.py` with Python 3 and NumPy; it exhausts the entire coefficient space, tests smoothness over both extension fields, and calculates the full projective orbit. Run `python blocking_cubic_groebner.py` with Python 3 and SymPy for an independent geometric-smoothness test. Their exact expected outputs appear in `enumeration_output.txt` and `groebner_output.txt`. Both programs were run using their included code. All computations are exact integer/finite-field operations; no randomized steps or heuristic singularity tests are used.

## Relationship to prior work

Asgarli, Ghioca, and Yip prove nonexistence of irreducible blocking plane cubics for field sizes at least five and give an existence example for the exceptional field of size three (arXiv:2208.13299, Theorem 1.3 and Example 3.5). Thus **existence and the sharp field-size boundary are prior results**. Their discussion does not give the complete arithmetic projective orbit classification or the coefficients-to-orbit census above. The same authors' arithmetic-statistics paper (arXiv:2211.08523) computes blocking densities for sufficiently high degrees and studies asymptotic smoothness, not this degree-three classification. Finite-geometric classifications of blocking point sets concern subsets of the rational projective plane; they are not automatically classifications of the defining smooth cubic equations.

## Limitations

The result is finite and specific to \(\mathbf F_3\); it makes no claim about larger finite fields, moduli over extensions, or all elliptic curves having six rational points. The full projective-orbit count is computational, with complete enumerators supplied rather than a closed-form moduli argument. Prior finite-geometry tables or full small-field elliptic-curve catalogues may encode equivalent information implicitly; publication priority is not independently certified. Although the displayed cubic is known to be geometrically smooth, the two programs should be rerun in an independently controlled environment before external reliance.

## References

1. S. Asgarli, D. Ghioca, C. H. Yip, *Plane curves giving rise to blocking sets over finite fields*, arXiv:2208.13299 (first public version 2022-08-28), especially Theorem 1.3 and Example 3.5; *Designs, Codes and Cryptography* **91** (2023), 3643–3669.
2. S. Asgarli, D. Ghioca, C. H. Yip, *Most plane curves over finite fields are not blocking*, arXiv:2211.08523 (first public version 2022-11-15), Sections 1, 2, 5, 7; *J. Combin. Theory Ser. A* **204** (2024), 105871.
3. K. Coolsaet, A. Botteldoorn, V. Fack, *Classification of minimal blocking sets in small Desarguesian projective planes*, *Journal of Combinatorial Designs* **30** (2022), 561–580, DOI:10.1002/jcd.21842 (blocking point-set context, not a cubic-equation classification).
