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

# Verification and limits

The radial expansion follows from \(\sqrt{\delta/\tan\delta}=1-\delta^2/6-\delta^4/40+O(\delta^6)\) and \(\sec(u/n)=1+u^2/(2n^2)+5u^4/(24n^4)+O(n^{-6})\), uniformly on \(|u|\le\pi/2\). The exact moment coefficients reduce to integrals of the rational polynomials \((3x^2-1)^3/24^3\), \(3(3x^2-1)^2(25x^4-10x^2-3)/(24^2\cdot1920)\), and \((3x^2-1)^4/24^4\) over \([-1,1]\). The included script evaluates these integrals with exact rational arithmetic and asserts the values \(1/15120\), \(13/1209600\), and \(1/120960\).

For \(g(r)=rJ_1(j_{1,1}r)/j_{1,1}\), the derivative identities give \(g'(1)=g''(1)=J_0(j_{1,1})\), \(g'''(1)=-j_{1,1}^2J_0(j_{1,1})\), and \(g''''(1)=-2j_{1,1}^2J_0(j_{1,1})\). The exact area identity cancels \(\int(h_n+h_n^2/2)\), leaving the cubic and quartic moments. The Fourier-harmonic tail is factorially small at bounded frequency. The nearest-zero theorem and derivative estimate from arXiv:2609.10517v1 imply that the root displacement is \(O(n^{-6})\), so replacing the derivative by \(2\pi J_0(j_{1,1})/j_{1,1}\) contributes only \(O(n^{-10})\).

The script verifies algebraic integrations, not the full infinite-dimensional Fourier-zero localization. No independent audit or independent validation has been performed.
