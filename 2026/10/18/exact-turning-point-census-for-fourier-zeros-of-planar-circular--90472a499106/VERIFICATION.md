---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Radial integration gives 2pi G_q(x)/x for G_q(x)=J_1(x)-qJ_1(qx), and area pi(1-q^2)>0 at zero. Put H(x)=xJ_1(x). Then H'=xJ_0 and H''=H'/x-H, so (H^2+H'^2)'=2H'^2/x, strictly increasing in the integrated sense on every positive interval. At a root H(x)=H(qx), this forces |J_0(x)|>q|J_0(qx)|. Consequently G_{q,x}=J_0(x)-q^2J_0(qx) is nonzero there and of the sign of J_0(x). At each J_0 gap endpoint, the same energy comparison gives |J_1(x)|>q|J_1(qx)|; alternating signs force one root per gap, and all simple crossings inside a gap have the same orientation, so there cannot be two. Below the first endpoint the integral has positive integrand almost everywhere. The implicit-function theorem gives analytic roots. The inner argument y=qx has derivative xJ_0(x)/G_{q,x}>0. Its left limit is zero and its right limit is j_{0,n}: the normalized integral G_q/(1-q) extends smoothly to q=1 with value xJ_0(x), and its local branch at j_{0,n} is j_{0,n}[1+(1-q)/2]+O((1-q)^2), entering the correct open gap and hence coinciding with its unique root. This is the decisive endpoint argument, without assuming the right endpoint is not a zero of the limiting function. At q=0 the local J_1 branch and qJ_1(qx)=xq^2/2+O(q^4) give exactly the even disk expansion. Since x_n'=y J_0(y)/G_{q,x}, y's increasing range crosses just j_{0,1},...,j_{0,n-1}. At each crossing y'=x and J_0'(y)=-J_1(y); this gives the stated nonzero curvature and sign (-1)^(n+m). In particular the n=1 derivative is strictly negative, and H is strictly monotone on the gap so the equation for X_{n,m} determines it uniquely. Replay: RESULT.md lines 58–145 and the above argument; python3 /workspace/review_evidence/bounded_checks.py uses Bessel series and bisection to reproduce q_{2,1}=0.315585469056578 and X_{2,1}=7.620203695958628. The provided SciPy script and recorded outputs were inspected, not rerun; the infinite-order result rests on the strict energy and implicit branch argument.

## originality

PASS

Classical Bessel interlacing and the optical disk and thin-ring profiles are antecedents. The gap census and turning count are mathematically covered by two later-dated all-dimensional records on specializing to d=2. That overlap must be credited, but it is not verified prior coverage relative to the frozen record, and the dated evidence here does not establish provenance or absolute priority. No inspected earlier result supplied the claimed joint gap and stationary-point classification with the endpoint expansions. The assessment concerns that classification, not the known diffraction profile.

## value

PASS

The scalar annular Fourier transform is a natural object. A full radial zero enumeration and exactly n-1 alternating nondegenerate turns resolve the meaningful question of whether dark-ring radii move monotonically as the hole grows: the first does, all higher ones have a prescribed number of reversals. The exact locations and endpoint corrections are useful beyond the known endpoint optical profiles; no Laplacian or complex-zero significance is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
