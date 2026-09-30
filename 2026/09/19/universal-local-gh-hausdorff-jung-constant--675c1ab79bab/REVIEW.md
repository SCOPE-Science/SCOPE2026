# Review: universal local Hausdorff–Gromov–Hausdorff Jung constant

**Independent audit on 2026-09-29 UTC: correctness passed; provenance repaired.**

## Correctness

The scale optimization is correct. Rescaling distances by \(\delta/h\) sends the Hausdorff distance to \(\delta\), divides sectional curvature by the square of that factor, and multiplies the convexity radius. Thus the curvature parameter in Adams--Frick--Majhi--McBride becomes \(\kappa_+h^2/\delta^2\). The fixed choice \(\delta<\pi/[4(c_n+1)]\) makes the first branch of their lower-bound minimum active for all sufficiently small \(h\). Expanding the explicit sine quotient gives \(c_n-O(h^2)\), hence the uniform cubic lower error.

The sharpness conclusion is also correct, but the matching deleted-ball estimate was already proved in an earlier SCOPE record. Combining that earlier upper family with the present all-subset lower bound gives
\[
\mathcal C_M(h)=c_n+O(h^2).
\]

## Originality and provenance correction

The original review incorrectly stated that no SCOPE record contained the matching cubic deleted-ball asymptotic. In fact,
`2026/09/18/small-hole-gromov-hausdorff-cubic-asymptotic--a0d57fbb476f`
was first committed at 2026-09-18T13:52:44Z and already proved
\(d_{\mathrm{GH}}(M\setminus B_r(a),M)=c_nr+O(r^3)\).
The present record was first committed at 2026-09-19T01:53:04Z.

The distinct contribution that survives is the stronger quantifier: a scale-sensitive lower bound for every sufficiently dense compact subset, and therefore the universal local infimum. Current external searches did not locate that all-subset \(\kappa h^2\) formulation in the cited literature, but novelty is claimed only for this extension.

## Scientific value

High. The theorem turns a sharp example into a universal local converse bound and explains why ambient positive curvature disappears at first order. The earlier deleted-ball theorem supplies sharpness but is not re-claimed.

## Limitations

No optimal second-order coefficient or classification of extremizers is obtained. The result is for closed smooth manifolds of dimension at least two.
