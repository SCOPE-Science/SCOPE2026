# Independent audit — 2026-10-01

## Final claim

For the stated resonant symmetric doubly-confluent Heun system, the reduced equation has no Liouvillian solution and its differential Galois group over C(x) is SL(2,C).

## Disposition

**passed**

## Correctness — PASS

The scalar reduction was independently reconstructed: with a=2x+1/(2x)+1/x², the reduced equation is u''=(a²+a'+1)u with Q=4x²+5+4/x-1/(4x²)-1/x³+1/x⁴. The only finite pole of Q is order 4 at 0 and deg(den)-deg(num)=-2 at infinity. The Case-1 local choices give m in {1/2,3/2}, p in {2,-2}, t1 in {3/4,-7/4}, hence candidate degrees {1/4,-9/4,-3/4,-13/4}, none a nonnegative integer. Kovacic Cases 2 and 3 already fail their necessary pole-order gates; the repository's exact scripts reproduce the negative degree tables. Therefore no Liouvillian solution exists and the determinant-one second-order equation is in Kovacic Case 4, so its differential Galois group is SL(2,C). The numerical Stokes-loop trace is corroboration only and is not needed for the conclusion.

## Originality — PASS

Best-of-knowledge search found the general Kovacic algorithm and a broad 1992 application to Heun and confluent special-function families, but no source inspected stated or implied the exact SL(2,C) result for this rational parameter point. The 1992 paper remains a residual comparison risk because only its accessible abstract/bibliographic description, not a parameter-by-parameter full classification, was available in this run.

### Equivalent formulations

Equivalent formulations are absence of Liouvillian solutions for the reduced second-order equation, or full SL2 differential Galois group; no exact prior parameter match was located.

### Broader coverage

The general algorithms cover how to decide the point, but an algorithm is not itself a published answer for every rational parameter specialization.

### Exact database or table

There is no exact parameter table identified in the inspected sources.

### Claim versus prior implication

With no decisive prior implication located, originality passes best-of-knowledge, with the inaccessible/full-comparison risk explicitly retained.

## Scientific value — PASS

The parameter point is not presented as an arbitrary scan: it is a resonant symmetric boundary where the formal monodromy at the rank-1 irregular point is central, so a generic monodromy heuristic does not by itself decide reducibility. An exact no-Liouvillian/SL2 determination at that structurally delicate point is a motivated exact invariant and can serve as a boundary test for the doubly-confluent Heun family.

## Checked sources

- https://doi.org/10.1016/S0747-7171(86)80010-4
- https://doi.org/10.1007/BF01268661
- Resultary published-findings semantic search

## Residual risks and limitations

- The phrase in the package calling infinity an 'ordinary point of Q' is potentially confusing: Q grows quadratically and infinity is irregular for the differential equation. The Kovacic degree convention used in the actual elimination is nevertheless the correct relevant datum.
- A parameter-level theorem inside Duval-Loday-Richaud or another special-functions classification could subsume this point; the accessible material inspected in this run did not resolve that mapping.
- The scientific value is local to a distinguished parameter point rather than a family-wide classification.

The exact Kovacic elimination establishes the Galois-group conclusion; the numerical loop-monodromy value is corroborative only. A broad 1992 treatment of Heun-family Liouvillian solutions was identified, but no exact implication for this parameter point was located in the material inspected.
