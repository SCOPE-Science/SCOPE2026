# Six Frobenius spectra of singular parameters in binary elliptic pencils

## Finding

Let \(S=\mathbf P^1_{\mathbf F_2}\times\mathbf P^1_{\mathbf F_2}\), and consider two-dimensional subspaces \(W\subset H^0(S,\mathcal O_S(2,2))\) such that all three nonzero rational members of \(W\) cut out geometrically smooth curves. Let \(\Delta_{\mathrm{red}}(W)\subset\mathbf P^1_{\mathbf F_2}\) denote the **reduced support** of the parameters where the corresponding geometric fibre is singular. Record the degrees over \(\mathbf F_2\) of the closed points of this finite support as an unordered multiset.

Exactly the following six spectra occur, with the indicated numbers of literal coefficient-coordinate pencils:

| Frobenius closed-point degrees of singular parameters | Pencils | Ambient automorphism orbits |
|---|---:|---:|
| \((2,8)\) | 72 | 1 |
| \((3)\) | 192 | 4 |
| \((3,4,5)\) | 72 | 1 |
| \((3,6)\) | 108 | 2 |
| \((4,8)\) | 216 | 3 |
| \((12)\) | 144 | 2 |
| **Total** | **804** | **13** |

In particular, every singular geometric fibre lies over an extension of degree at least \(2\), and the *number of distinct geometric singular-fibre parameters* is exactly one of \(3,9,10,12\). All four values occur. This counts distinct geometric parameter values, **not** multiplicities of the Weierstrass discriminant, not singular points within a fibre, and not Kodaira fibre types.

## Assumptions and scope

All calculations take place over \(\mathbf F_2\). A pencil is an actual two-dimensional vector subspace of the nine-dimensional section space, not an ordered basis or a quotient by projective automorphisms. A smooth member means smooth over the algebraic closure; its genus is \((2-1)(2-1)=1\). The full rational automorphism group of the split quadric has order \(72\) and is \((\operatorname{PGL}_2(\mathbf F_2)\times\operatorname{PGL}_2(\mathbf F_2))\rtimes C_2\). Changing the pencil basis acts on its parameter line by \(\operatorname{PGL}_2(\mathbf F_2)\) and does not change Frobenius degrees.

The property studied is the singular-fibre *parameter locus* of the entire geometric pencil. All three rational fibres are smooth by hypothesis; singular fibres, if any, occur over non-rational parameter values. This is distinct from the Frobenius splitting of the pencil's common base scheme in \(S\).

## Proof

Use the ordered section basis \(X_0^{2-i}X_1^iY_0^{2-j}Y_1^j\), indexed by \(3i+j\) for \(0\le i,j\le2\). Represent a binary section by its nine-bit integer mask; a pencil is the unordered triple of masks \(\{a,b,a\oplus b\}\) for independent nonzero sections \(a,b\).

**Completeness of the smooth-form test.** On each of the four standard affine charts, any bidegree-\((2,2)\) form can be written \(F(x,y)=\sum_{0\le i,j\le2}c_{ij}x^iy^j\). In characteristic two, \(F_x\) is a polynomial in \(y\) alone of degree at most two, and \(F_y\) is a polynomial in \(x\) alone of degree at most two. If neither derivative vanishes identically, any simultaneous root has both coordinates in \(\mathbf F_4\). If one derivative vanishes identically, the other fixes one coordinate over at most \(\mathbf F_4\), while \(F=0\) fixes the second over a further extension of degree at most two, so the coordinates lie in \(\mathbf F_{16}\). If both vanish identically, the form is a square on the chart and every point of its nonempty zero locus is singular; a point may be chosen over \(\mathbf F_{16}\). Thus a geometric singularity exists if and only if the simultaneous equations \(F=F_x=F_y=0\) have a solution on one of the four charts over \(\mathbf F_{16}\). Exhaustively testing all \(511\) nonzero binary masks leaves \(144\) smooth sections.

There are exactly \(804\) unordered triples \(\{a,b,a\oplus b\}\) lying entirely in that \(144\)-element set. Since the evaluation map from sections to their values on the \(3\times3\) rational grid is a linear isomorphism, the complete ambient automorphism group acts by row permutations, column permutations, and transposition. The explicit \(72\)-element action gives exactly \(13\) orbits, with sizes ten times \(72\), twice \(36\), and once \(12\). `enumerate_pencils.py` independently constructs these data from finite-field evaluation, with all masks and orbit representatives in `pencil_catalogue.json`.

For each orbit representative choose generators \(a,b\) and write \(F_t=F_a+tF_b\), with the fibre at infinity equal to \(F_b\). On each affine chart form the ideal
\[
I_c=\bigl(F_t,\partial_xF_t,\partial_yF_t\bigr)\subset\mathbf F_2[x,y,t].
\]
Its elimination ideal \(I_c\cap\mathbf F_2[t]\) is principal; a lexicographic Gröbner basis computes its monic generator. The zero set of the generator is exactly the parameter values admitting a geometric singular point on that chart: the projection is a finite set because at least the three rational fibres are smooth, so its Zariski closure introduces no extra parameter. Taking the union of the four chart zero sets is equivalent to collecting all distinct irreducible factors of the four elimination generators. The smooth fibre at infinity contributes none. Each irreducible factor of degree \(d\) produces one Frobenius orbit of \(d\) distinct geometric singular-fibre parameters.

The thirteen elimination calculations and their factor polynomials appear in `singular_spectra.json`. A separate calculation by two iterated Sylvester resultants, reducing coefficients modulo two at each stage, reproduces the same union of irreducible factors for every representative. This second calculation is independently implemented alongside the Gröbner calculation in `singular_parameters.py`; it is a cross-check and not a substitute for the ideal-elimination proof.

For illustration, the representative masks \((98,141,239)\) have singular-parameter equation \(t^3+t^2+1=0\), irreducible over \(\mathbf F_2\). The representative \((99,188,223)\) has the irreducible degree-twelve equation
\[
t^{12}+t^9+t^8+t^5+t^4+t^3+1=0.
\]
The representative \((99,284,383)\) has three irreducible factors, of degrees \(3,4,5\), explicitly recorded in the package. All thirteen representatives and their orbit weights yield the table in the Finding section. Frobenius degrees remain invariant under every rational surface automorphism and rational change of parameter, proving the assertion for every one of the \(804\) pencils.

## Verification

With Python 3 and SymPy installed, run these commands in a directory containing the packaged sources:

```sh
python3 enumerate_pencils.py > enumerate_pencils_output.txt
python3 singular_parameters.py > singular_parameters_output.txt
```

The first program builds the independent \(\mathbf F_{16}\) chart test, \(144\)-element smooth-form list, all \(804\) pencils, and the complete \(72\)-element automorphism action. The second checks all thirteen orbit representatives by both Gröbner elimination and iterated resultants, asserts exact agreement of irreducible factor sets, and weights their Frobenius degree patterns by orbit sizes. Exact expected output transcripts are included in `enumerate_pencils_output.txt` and `singular_parameters_output.txt`. Both programs were executed from these standalone package paths. All coefficients, searches and comparisons are exact finite algebra, with no heuristic numerical approximations.

## Relationship to prior work

Hamada and Hayano (2020) identify the bidegree-\((2,2)\) elliptic pencil on the quadric as a fundamental genus-one Lefschetz pencil over the complex numbers. Asgarli and Ghioca (2022) examine pencils with all rational members smooth over finite fields, in a hypersurface framework. Neither inspected manuscript states the binary-quadric singular-parameter Frobenius spectra calculated here.

Existing finite-field classifications already determine the \(804\) qualifying pencils, their thirteen ambient orbits, and the Frobenius structures of their **base schemes**. These underlying counts are used solely as verified structural inputs and are **not** newly claimed. The new result instead concerns the different arithmetic invariant of *singular values in the parameter line*, obtained through fresh elimination calculations. Lang's work on characteristic-two rational elliptic surfaces develops geometric singular-fibre configurations and arithmetic-discriminant methods, but the inspected text does not give this complete \(\mathbf F_2\) thirteen-orbit parameter-degree census. Earlier unindexed arithmetic surface tables could still overlap; this priority uncertainty is not resolved by a database search alone.

## Limitations

This is a classification for the split quadric over \(\mathbf F_2\) only. It determines reduced Frobenius support of singular parameters, not multiplicities, local Kodaira types, discriminant divisors, fields of definition of singular points, or the full Mordell–Weil groups. The computation is exhaustive over a finite coefficient domain; it does not assert a uniform classification over all fields. There has been no independent external scientific audit.

## References

1. Noriyuki Hamada and Kenta Hayano, *Classification of genus-1 holomorphic Lefschetz pencils*, arXiv:2008.02925, first public version 2020-08-07; *Turkish Journal of Mathematics* 45 (2021), 1079–1119.
2. Shamil Asgarli and Dragos Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169, first public version 2022-03-14; *Bulletin of the Australian Mathematical Society* 107 (2023), 85–94.
3. William E. Lang, *Extremal rational elliptic surfaces in characteristic \(p\). II: Surfaces with three or fewer singular fibres*, *Arkiv för Matematik* 32 (1994), 423–448, DOI:10.1007/BF02559579.
4. William E. Lang, *Configurations of singular fibres on rational elliptic surfaces in characteristic two*, *Communications in Algebra* 28 (2000), 5813–5836, DOI:10.1080/00927870008827190. Bibliographic metadata accessed; full text not inspected.
