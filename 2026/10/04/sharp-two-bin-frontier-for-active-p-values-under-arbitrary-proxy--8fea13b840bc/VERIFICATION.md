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

The proof is analytic. For each rejection level \(s<1\), arbitrary dependence of the proxy bin on the true p-value is absorbed into the decreasing envelope

\[
g_s(p)=\max\{h_1\mathbf{1}\{p\le s/b_1\},h_2\mathbf{1}\{p\le s/b_2\}\}.
\]

Super-uniformity of \(P\) implies \(\mathbb E[g_s(P)]\le\int_0^1g_s(p)\,dp\), and the integral equals \(h_1\min(1,s/b_1)+(h_2-h_1)\min(1,s/b_2)\). The three threshold regions yield the stated necessary-and-sufficient coefficient inequality. Necessity is witnessed by \(P\sim\mathrm{Unif}(0,1)\) and a proxy label that chooses the maximizing bin on the two rejection intervals at one sufficiently small \(s\).

`verify.py` uses exact rational arithmetic to check the boundary example \((h_1,h_2,b_1,b_2)=(1/5,4/5,1/2,1)\), the contradiction \(\beta\ge4/5\) versus \(\beta\le3/5\) for the prior split-tail sufficient conditions, and the piecewise envelope on rational test grids. It also checks a finite set of rational parameter tuples as corroboration. Finite checks are not treated as a proof of the universal theorem.

Limit: no computation here certifies novelty, a result for more than two bins, or any multiple-testing guarantee beyond ordinary use of a valid p-value.
