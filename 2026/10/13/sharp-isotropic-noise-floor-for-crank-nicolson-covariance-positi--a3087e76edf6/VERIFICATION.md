---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The direct matrix trapezoidal step with x=ha,y=hb in (0,1) has P11+=(r P11+h nu)/(1+x), P22+=(ell P22+h nu)/(1+y), P12+=z P12, r=1-x,ell=1-y,z=(2-x-y)/(2+x+y). Rank-one trace-tau inputs generate the PSD trace slice, so convexity reduces universal PSD to determinant F_s(t)=s^2+s[rt+ell(1-t)]-E t(1-t)>=0, s=h nu/tau, E=k-r ell=2(x-y)^2(x+y)/(2+x+y)^2>0 and k=z^2(1+x)(1+y). Completing the square yields s*=E/(r+ell+2 sqrt(k)), t*=1/2-s*(r-ell)/(2E) strictly in (0,1), F_s*(t)=E(t-t*)^2. F_s increases strictly in s>=0 pointwise; thus the threshold is necessary and sufficient, equality orientation unique, below it fails even for rank-one inputs. Taylor E=0.5(a-b)^2(a+b)h^3+O(h^4) gives nu*=tau h^2(a-b)^2(a+b)/8+O(h^3). Independent exact Fraction replay at (x,y)=(1/4,4/5) reproduced s*=42/1159, t*=74/209, unforced determinant -847/111630. No extrapolation from this witness.

## originality

PASS

Best-of-knowledge PASS: Dieci–Eirola already proved a general loss of positive definiteness in direct high-order Lyapunov/Riccati integrators; Gillis–Diehl introduce a modified positivity-preserving discretization. Neither inspected work states an exact smallest isotropic input diffusion restoring one direct CN step over fixed-trace PSD covariances. This quantitative Schur-multiplier rescue is separated from known impossibility and from changing integrators.

## value

PASS

The fixed total variance is a natural physical normalization of additive covariance forcing. The exact minimal isotropic noise and worst rank-one direction quantify an integrator positivity defect despite nonnegative scalar damping; the h² scaling helps distinguish structural versus numerical safety. Not claimed for repeated steps or arbitrary matrix drift.

The dated certificate retains the supplied scientific assessment, sources and limitations.
