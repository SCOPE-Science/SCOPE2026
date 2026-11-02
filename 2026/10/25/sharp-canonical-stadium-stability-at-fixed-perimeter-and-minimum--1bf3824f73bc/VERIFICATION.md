---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For any planar convex support function h_K in H1, P=∫h, A=1/2∫(h²−h′²), width=h(theta)+h(theta+pi). Stadium support h_S=R+(L/2)|sin theta|, R=w/2 and L=(P−pi*w)/2, has curvature measure (h_S+h_S′′)=R dtheta+L(delta_0+delta_pi). Common perimeter cancels R∫f, common Steiner point cancels modes n=±1, and chosen minimal-width direction has f(0)+f(pi)=0, cancelling L atoms. Parseval yields exactly A(S)−A(K)=(pi/2)∑_{n≥2}(n²−1)(a_n²+b_n²). Weighted Cauchy–Schwarz yields supnorm f²≤(3/4)∑(n²−1)(a_n²+b_n²) since Σ_{n≥2}1/(n²−1)=3/4, proving the universal constant and rigidity. For each fixed R,L>0 finite q_N=∑_{n=2}^N cos(n(theta−phi_N))/(n²−1) has phi_N chosen to cancel even modes at the fixed minimum direction. For small enough amplitude its curvature density remains positive and the stadium width cusp keeps the exact minimum-width direction; at theta=phi_N the Cauchy–Schwarz kernel is attained, so ratio 2/pi Σ_{n=2}^N1/(n²−1) ↑3/(2pi). For P=pi w all widths are constant and every even Fourier mode of f vanishes, replacing kernel 3/4 by Σ_{odd n≥3}1/(n²−1)=1/4, with finite odd-harmonic smooth approximants. Independently solved even-mode root numerically and verified curvature and width on fine angle grid for N=4,16,64,128, with ratios 0.3342253805,0.4388463504,0.4675941621,0.4725105148. Numerics supplement analytic existence/sharpness, not replace them.

## originality

PASS

The classical area–perimeter–minimum-width bound A(K)≤Pw/2−pi*w²/4 with equality at the matching stadium appears explicitly in Ftouhi–Masiello–Paoli, Prop. 5.7, and is not novelty. A published earlier sharp constant-width Steiner-disk stability record (2026/9/20, via Resultary) gives the endpoint 1/(2pi) and is expressly treated as prior. Gao (2011) controls distance to a Steiner disk using a disk isoperimetric deficit, which does not vanish for a nondisk matched stadium, so it cannot imply a sharp vanishing surplus-based stadium bound for P>pi w. An (Oct 2026) studies support function inversion and planar Hausdorff reconstruction, but inspected results do not give the matched-stadium energy identity and fixed-pair sharp coefficient. Resultary cross-search on width and Fourier stability identified related constant-width cases but no covered varying-width result; unindexed stability sources remain a risk.

## value

PASS

This is a natural quantitative rigidity companion to the established stadium area extremum. Unlike a mere inequality re-expression, it exactly identifies the deficit as Fourier Sobolev energy, proves global Hausdorff stability to the shape matched in both P and minimum width, and finds a best coefficient simultaneously for every fixed nonconstant-width pair. The discontinuous sharp-constant transition at the constant-width boundary is an intrinsically motivated geometry phenomenon potentially useful in inverse support/shape stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
