# Same-model review

## Correctness — PASS
The final claim was reconstructed from explicit coordinates. Positive barycentric coordinates certify that \(P\) is interior; the Cevian intersections and all distance/inradius formulas follow by direct coordinate geometry. `verify.py` uses exact rational enclosures whose validity is reduced to integer-power comparisons, and its strict upper bound for the defect is negative. The asymptotic family is derived symbolically from the same formulas. No finite random experiment is used to infer an infinite statement.

Risk: the counterexample does not determine the full valid exponent region. The proof is limited to negating the universal statement at \(k=21/10\) and, by continuity, a nearby geometric family at that exponent.

## Originality — PASS
The primary 2012 source was inspected at the Cevian definitions and Conjecture 3.9. Searches covered the exact inequality, \(k=2.1\), Cevian/pedal aliases, later citations, a published-findings database, and the prior local record. A 2018 pedal-triangle solution paper and a 2017 paper whose title announces a proof of a Liu conjecture were compared by objects and implications; neither contains or implies the present Cevian endpoint counterexample. The 2017 full text was specifically checked for Cevian notation.

Closest literature: Liu's source DOI 10.12816/0006135 states the conjecture; Huang DOI 10.1186/s13660-018-1661-7 solves different pedal-triangle conjectures; Yang et al. DOI 10.7153/jmi-11-34 proves a different point-distance parameter inequality. Residual risk remains that older or weakly indexed literature may contain an equivalent counterexample under different notation.

## Value — PASS
Refuting the exact proposed endpoint of a published conjecture is mathematically substantive. The counterexample is not merely numerical: an exact certificate verifies a concrete triangle, while the limiting computation exposes a robust slender-triangle obstruction that can guide a corrected formulation.

Same-model review: passed. Independent audit: not yet performed.
