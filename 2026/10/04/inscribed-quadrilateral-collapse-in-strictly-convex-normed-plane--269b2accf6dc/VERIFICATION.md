---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof in `RESULT.md` has three independently checkable steps.

First, for a nonzero horizontal translation of a planar convex body, common boundary points occur exactly at ordinates where the horizontal section width equals the translation length. The width is concave. If a horizontal level met it in more than two ordinates, concavity would force a constant interval; on such an interval the left and right boundary functions would both be affine, creating boundary line segments. Strict convexity excludes this. Therefore two distinct translates of a strictly convex planar boundary meet in at most two points.

Second, an admissible zero-sum unit quadruple gives two unit pairs with the same sum. The translate lemma makes those unordered pairs identical, except for the repeated-point case, where strict convexity of the midpoint gives the same conclusion. Thus every admissible quadruple is \(x,-x,y,-y\) after relabelling, and its energy is
\[
8+2\|x+y\|^2+2\|x-y\|^2.
\]
Taking the supremum gives \(J_{\mathrm{in}}(X)=8+8C'_{\mathrm{NJ}}(X)\).

Third, Ciesielski--Płuciennik Theorem 2 at \(n=2\) yields
\[
C'_{\mathrm{NJ}}(\ell_p^2)=
\begin{cases}
2^{2/p-1},&1<p\le2,\\
2^{1-2/p},&2\le p<\infty.
\end{cases}
\]
The two non-strict endpoints are checked directly by four unit vertices with all six mutual distances equal to \(2\), together with the universal upper bound \(24\).

A deterministic constrained numerical stress test, not used in the proof, used twenty starting points for each of \(p=3/2,3,4\). Its largest values agreed with the closed form to within \(10^{-12}\) or better.

Limits: no independent audit has been performed. The planar chord-uniqueness step fails as a general mechanism in higher dimension, and no claim is made for \(\ell_p^d\) with \(d\ge3\).
