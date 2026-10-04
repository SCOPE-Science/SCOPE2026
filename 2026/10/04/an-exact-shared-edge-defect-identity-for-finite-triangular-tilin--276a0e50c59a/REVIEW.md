# Same-model scientific review

## Correctness
**PASS.** The claim has a complete finite combinatorial proof. Euler counting gives
\[
t+2=v_{\mathrm{bd}}+2v_{\mathrm{int}}-v_{\mathrm{int}}^*.
\]
The stretch decomposition, with size-\(2\) stretches retained, gives
\[
3t-v_{\mathrm{bd}}=2q+3v_{\mathrm{int}}^*-2E.
\]
Eliminating \(t\) yields the stated identity. The proof explicitly accounts for boundary vertices, interior subdividing vertices, and every stretch size, and no finite experiment is used as evidence for an infinite or universal claim.

## Originality
**PASS.** The closest source is Kupavskii–Pach–Tardos, arXiv:1711.04504, whose Theorem 6 proves only that a finite triangular tiling of a convex \(k\)-gon with \(k\ge4\) has at least one shared full side. Its proof assumes there are no such sides, so size-\(2\) stretches are absent. The present claim retains those stretches and obtains an exact count and the sharp bound \(q\ge k-3\). Targeted searches using the source terminology and the alternative terminology T-junction, hanging node, and non-edge-to-edge triangulation did not locate the same identity or a stronger theorem. Two closely related papers were also inspected and did not cover it.

Residual originality risk remains because search cannot exclude an unindexed or differently worded prior occurrence.

## Value
**PASS.** This is not only a restatement of the existence theorem: it supplies the exact defect
\[
q-(v_{\mathrm{bd}}-3)=3\bigl(v_{\mathrm{int}}-v_{\mathrm{int}}^*\bigr)+E,
\]
so every additional full shared side beyond the sharp boundary minimum is explained by concrete combinatorial nonconformity. It sharpens \(q\ge1\) to \(q\ge k-3\), is attained for every \(k\), and gives equality conditions.

## Closest literature and limitations
The closest literature is *Tilings with noncongruent triangles* (arXiv:1711.04504), followed by arXiv:1712.03118 and arXiv:1711.08903. The result here is restricted to finite tilings of convex planar polygons by nondegenerate triangles; infinite tilings and nonconvex regions are outside its scope.

Same-model review: passed. Independent audit: not yet performed.
