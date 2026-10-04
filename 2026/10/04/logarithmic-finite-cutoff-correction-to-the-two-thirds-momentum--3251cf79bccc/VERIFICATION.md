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

The analytic argument uses the exact published quotient \(G(k)\) and two exact algebraic factorizations of the equations \(G(k)=3\) and \(G(k)=-3/2\). The critical steps are: (1) the fixed broad-band roots \(\cos(kd)=-1/2\); (2) the even-center identity \(\lvert\tan(kd/2)\rvert=\sqrt3/(k\ell)\), which gives a total central-hole contribution of order \(1/n\); (3) the two odd-center half-angle equations, whose edge difference gives the paired narrow-band contribution of order \(1/n\); and (4) harmonic summation over phase periods.

`verify.py` is a standard-library replay. It evaluates the original quotient, checks both factorization identities at independent values, locates the four continuous-band pieces by bisection in complete high-energy periods, and verifies convergence of
\[
n\left(\frac{4\pi}{3d}-|S\cap P_n|\right)
\]
to \(4/(\sqrt3\pi\ell)\) for several \(d\) and \(\ell\). It also checks a cumulative harmonic-corrected residual. Its successful output is `VERIFY_OK`.

The numerical replay is not used as a proof for infinitely many periods. The proof of the all-
\(K\) statement is the exact factorization plus Taylor expansion and the harmonic-series asymptotic. The \(O(1)\) constant is not computed, and no claim is made about energy-measure density, the general Kagome lattice, or the detailed low-energy spectrum.
