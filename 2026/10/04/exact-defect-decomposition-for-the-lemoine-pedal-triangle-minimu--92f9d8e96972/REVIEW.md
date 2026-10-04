# Same-model review

## Correctness
PASS. The claim follows from three elementary identities: the centroid sum-of-squares identity for \(XYZ\), Pythagorean splitting relative to the perpendicular feet from its centroid, and completion of squares for the sum of squared signed distances to the three sidelines. The Lemoine barycentrics \(a^2:b^2:c^2\) give distances \(2\Delta a/S,2\Delta b/S,2\Delta c/S\), and the weighted normal equilibrium \(a n_a+b n_b+c n_c=0\) cancels the linear term. Equality forces both centroid displacement and all three tangential offsets to vanish, hence exactly the Lemoine pedal triangle. A deterministic coordinate replay is supplementary and agrees with the identity.

## Originality
PASS, with explicit historical risk. The optimizer itself is classical and is not claimed as new. The inspected 2007 source states that optimizer but displays \(4\Delta^2/S\), inconsistent with its own subsequent factor-three relation and with the equilateral test; the corrected value is \(12\Delta^2/S\). Targeted searches for the Lemoine pedal triangle, sum-of-squared-side minimization, symmedian least squares, and exact defect decompositions did not locate the two-term identity. The 2016 least-squares paper is adjacent, but only its metadata and abstract were available in the inspected lawful sources, so equivalent full-text coverage remains a residual risk.

## Value
PASS. The identity upgrades a qualitative optimizer theorem to an exact stability certificate: every unit of excess is assigned either to motion of the centroid away from the Lemoine point or to nonpedality of the three chosen side points. It also identifies and repairs a concrete factor-three constant error in an accessible statement of the classical result. Both features are reusable in quantitative triangle-geometry arguments.

Closest literature and limitations are recorded in `AUDIT.json` and `RESULT.md`. The result is confined to the Euclidean quadratic objective and does not assert exhaustive historical novelty.

Same-model review: passed. Independent audit: not yet performed.
