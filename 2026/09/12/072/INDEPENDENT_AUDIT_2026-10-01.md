# Independent mathematical audit — SCOPE-20260912-072

Disposition: **passed**.

## Correctness
**PASS** — Independent reconstruction verifies the normal form r=1/4+(t-1/4)/x-3/(16x²), Kovacic case-1 candidate degrees t-1, t-1/2, -t-1/2, -t (none nonnegative integral for transcendental t), the symmetric-square pole and infinity obstructions, and the rational Lax obstruction. At x=0 the pole equation involves integer pole order versus ad_K eigenvalues 0,0,+/-1/2; at other finite points differentiation dominates. A polynomial Lax matrix is forced to degree 0 and then the equations -b/2=0 and bt-1=0 conflict. Thus the normalized classical group is SL2 and the non-isomonodromic Zariski-dense PPV group is full SL2.

## Originality
**PASS** — The classical differential Galois groups of confluent hypergeometric equations are well developed (Mitschi summarizes prior Katz/Gabber coverage), and Arreche supplies a general PPV algorithm. However, the inspected primary material and Resultary search did not locate the exact generic-parameter Kummer PPV classification with this explicit rational Schlesinger obstruction. The final claim is narrower than the general algorithms but is not a verbatim corollary without the parameter-specific calculation.

### Equivalent formulations
The exact final statement can be phrased as classical SL2 plus failure of a rational t-flatness equation.

### Broader coverage
No inspected source stated the exact t-family's PPV differential equations and non-isomonodromy verdict.

### Exact database or table search
This only supplements, and does not replace, implication comparison.

### Claim versus prior implication
A parameter-specific exact calculation remains necessary.

## Value
**PASS** — Kummer's equation is a canonical special-function family. Determining its generic PPV group and proving non-isomonodromy is a natural exact invariant with direct reuse in differential-Galois and deformation questions, not an arbitrary parameter slice.

## Source inspections
- **Arreche, Computing the differential Galois group of a one-parameter family of second order linear differential equations** (arXiv:1208.2226): full arXiv HTML introduction and SL2 subgroup classification passages Assessment: General algorithm is prior; no exact Kummer parameter-family output was located. Evidence: Arreche treats arbitrary rational r1,r2 in C(x,t) and distinguishes full versus constant Zariski-dense SL2.
- **Mitschi, Differential Galois groups of confluent generalized hypergeometric equations: an approach using Stokes multipliers** (Pacific J. Math. 176 (1996), 365-405): indexed full-text introduction plus PDF visual inspection of title/introduction context and representative theorem page Assessment: Classical confluent-hypergeometric Galois theory is prior and strong; this does not by itself give the parameterized t-flatness calculation. Evidence: The introduction states that differential Galois groups of irreducible confluent hypergeometric equations had been determined by Katz and Gabber.
- **Resultary semantic search** (Resultary local research index): top hits for Kummer PPV full SL2/non-isomonodromy Assessment: The exact Kummer record was the direct hit; adjacent hits concerned different equations. Evidence: No earlier equivalent Kummer PPV SCOPE record was returned.

## Residual risks
- Classical Kummer differential Galois groups are heavily studied; the PASS on originality is specifically for the parameterized full-vs-constant conclusion with the displayed rational Lax obstruction.
- The original companion-system GL2 determinant bookkeeping was not rederived as a separate theorem; the audited core claim is the normalized SL2 PPV classification.
