# Arithmetic splitting fingerprints of trigonal genus-five curves over \(\mathbf F_2\)

## Finding

Let \(C\) be a geometrically integral plane quintic over \(\mathbf F_2\) whose only singularity is an ordinary node or cusp. Its smooth normalization \(\widetilde C\) has genus \(5\). The projection from the singular point induces the unique degree-three morphism \(\pi:\widetilde C\to\mathbf P^1\). For its three rational target points, record the unordered splitting triple of the corresponding *geometric degree-three fibre divisors*.

The five symbols are **I3**, an irreducible cubic (no rational geometric point); **LQ**, a rational simple point plus a conjugate quadratic pair; **L3**, a triple rational point; **L2L**, a double and a different simple rational point; and **LLL**, three distinct rational points. For computational encoding these are indexed respectively \(0,1,2,3,4\).

**Exactly 34 of the 35 unordered splitting triples occur.** The unique unrealized triple is **(LLL,LLL,LLL)**. The exhaustive fixed-center census consists of **67,608** normalized quintic equations; the refined singularity-by-splitting table has exactly **75 nonempty cells**. The full 75-cell table and one explicit representative of each of the 34 triple types are `hurwitz_profile_table.csv` and `hurwitz_witnesses.csv`.

For the three singularity types, the exact counts grouped by \(r\), the number of rational base points with nonreduced geometric fibre, are:

| Singularity type | \(r=0\) | \(r=1\) | \(r=2\) | \(r=3\) | Total |
|---|---:|---:|---:|---:|---:|
| Ordinary split node | 2712 | 12276 | 16464 | 5388 | 36840 |
| Ordinary nonsplit node | 3736 | 5400 | 2784 | 464 | 12384 |
| Ordinary cusp | 5568 | 8016 | 4128 | 672 | 18384 |
| Total | 12016 | 25692 | 23376 | 6524 | 67608 |

Under the seven rational choices of the singular point, the ambient coefficient census is \(7\) times larger, namely **473,256** equations. Dividing the fixed-center enumeration by the order \(24\) of the point-stabilizer in \(\operatorname{PGL}_3(\mathbf F_2)\) recovers the previously published stack count **2817**; this existing total is a calibration, **not** asserted to be new.

## Assumptions and scope

All fields, points, and singularities are geometric unless the word rational is used. A fibre is taken as the divisor on the normalization, *not* the set of rational points on the singular plane curve. The source class contains exactly those ordinary one-singularity plane quintics of arithmetic genus six whose normalizations have genus five. In coefficient normalization, the singular point is \([0:0:1]\), the coefficients of \(Z^5\), \(XZ^4\), and \(YZ^4\) are zero, and the other \(18\) coefficients vary independently over \(\mathbf F_2\).

## Proof

**Local type and geometry.** In affine coordinates \(Z=1\) the first nonzero local terms have degree \(2\). A nondegenerate binary quadratic with cross term \(1\) is an ordinary node; it is nonsplit over \(\mathbf F_2\) precisely when its \(X^2\) and \(Y^2\) coefficients both equal \(1\). A square quadratic tangent cone with nonzero transverse cubic term is an ordinary cusp. All other local structures are excluded.

**Geometric integrality and uniqueness.** The arithmetic genus of a plane quintic is \(6\); a node or cusp has \(\delta=1\). A second geometric singular closed point of degree \(n\) contributes at least \(n\) to the genus defect. Thus a second singular closed point would have degree at most \(5\); the exact Jacobian test enumerates **all** such points over fields \(\mathbf F_{2^n}\) for \(1\le n\le5\). Reducibility over \(\mathbf F_2\) requires a degree-one or degree-two factor of a degree-five form; exhaustive product enumeration or independent polynomial divisibility excludes these. A geometrically reducible but rationally irreducible degree-five plane curve would be a union of five conjugate lines, hence has additional singular intersections at closed points of degree at most five, also excluded. The remaining curves are geometrically integral, nonsingular away from the chosen node/cusp, and their normalizations have genus \(5\). The uniqueness of the degree-three pencil for nonhyperelliptic genus-five trigonal curves is standard and explicitly used in the primary sources.

**Fibre test.** Restrict the quintic equation to each of the \(3\) rational lines through \([0:0:1]\). Removing the compulsory order-two contribution at that point gives a homogeneous binary cubic, which represents the full geometric pullback divisor on \(\widetilde C\), including the limiting branch or branches at the singular center. Squarefree and repeated linear factors, and the residual irreducible quadratic/cubic, distinguish I3/LQ/L3/L2L/LLL. Relabelling the three rational lines under \(\operatorname{PGL}_2(\mathbf F_2)\) permutes the triple but leaves its sorted multiset invariant.

**Exhaustion.** There are exactly \(2^{18}\) coefficient vectors with fixed singular center. A direct finite-field Jacobian and factorization sweep produces **67,608** valid equations. The 75 coefficient cell counts in `hurwitz_profile_table.csv` sum to 67,608, and grouping by unordered triple produces the 34 nonzero rows in `hurwitz_witnesses.csv`. All 34 witnesses satisfy the geometric tests. The missing all-LLL triple would imply nine rational points on a smooth genus-five trigonal curve, which is also forbidden by the previously known genus-five rational-point bound over \(\mathbf F_2\); the exhaustive search independently establishes its absence in this plane-quintic model.

## Verification

The executable `source_checker.c` uses direct finite-field arithmetic plus exact polynomial divisibility. The structurally separate `independent_checker.py` enumerates all degree-(1,4) and degree-(2,3) factor products and uses binary linear algebra for Jacobian vanishing on closed points. Both return the same 67,608 valid forms, matching distributions by singularity type and rational-point counts. The Python checker independently computes the full 75-cell fibre divisor table and the 34 witness records; the C checker separately computes a coarser fibre rational-point distribution, which agrees with aggregation of the 75-cell results. Source code is included in full; reference outputs are `source_checker_output.txt` and `independent_checker_output.txt`.

To reproduce with a C99 compiler and Python 3: `cc -O3 -std=c99 source_checker.c -o source_checker && ./source_checker` and `python3 independent_checker.py`. All calculations use exact \(\mathbf F_2\) and binary-extension-field operations; no random searches or floating-point comparisons enter the mathematical decisions.

## Relationship to prior work

Wennink (2017 preprint, 2020 journal) computes the weighted count of genus-five trigonal curves and explains nodal/cuspidal plane-quintic presentations. Dragutinović (2022 preprint, 2024 journal) computes all binary genus-five curves with explicit equations and rational-point counts, including the **known** maximum of eight rational points and the **known** global curve counts. Those totals are not new. The finer splitting of all three rational fibres, together with the singularity-conditioned 75-cell enumeration and rational ramification-incidence histograms, is not tabulated in the inspected papers; it is a further natural arithmetic invariant of the uniquely determined trigonal map. The complete published curve database allows some of these figures to be *computed in principle*, a specific residual novelty limitation.

## Limitations

The 67,608 count enumerates embedded **plane equations with a fixed singular center**, not abstract isomorphism classes. The 75 rows do not enumerate inequivalent morphisms or identify Galois monodromy groups. The five-type profile records only rational base fibres and does not determine the entire branch divisor. Source/database coverage and publication priority require independent expert review. There is no independent validation beyond the separate arithmetic algorithms reported here.

## References

1. T. Wennink, *Counting the number of trigonal curves of genus 5 over finite fields*, 2017 preprint, arXiv:1701.00375; published *Geometriae Dedicata* (2020), https://doi.org/10.1007/s10711-019-00508-3 .
2. D. Dragutinović, *Computing binary curves of genus five*, arXiv:2202.07809 (first public 2022), published *Journal of Pure and Applied Algebra* (2024), https://research-portal.uu.nl/ws/files/221402791/1-s2.0-S0022404923002049-main.pdf .
