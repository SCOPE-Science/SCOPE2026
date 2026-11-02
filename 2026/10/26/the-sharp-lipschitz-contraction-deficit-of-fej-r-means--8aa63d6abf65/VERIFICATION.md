---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Every periodic W^{1,infinity} derivative has mean zero and any bounded mean-zero function has a periodic Lipschitz primitive; commuting derivative with convolution reduces induced Lip seminorm to L∞–L¹ duality modulo constants. A median c of the nonconstant Fejér kernel minimizes absolute deviation; its zero-measure level sets yield an attained derivative sign(F_n-c). For odd n=2m+1, sign(F_n-1/n)=sign(sin((m+1)t)sin(mt)), which flips under t→t+pi, so c=1/n is median. Kernel F2/F3 give the exact cases. For asymptotics n F_n(t) converges weakly in distribution by joint torus Fourier-character equidistribution to H=sin²U/sin²V with independent U,V uniform, whose unique median is 1. Median convergence plus bounded truncation n(1-L_n)=2 E min(nF_n,c_n)-c_n avoids invalid unbounded dominated convergence. Integrating the two-angle triangle gives E min(H,1)=1/2+2/pi², yielding 4/pi². Fresh independent high-resolution midpoint quadrature verifies L2,L3, odd n median and n=200 limit approximation 0.405300 versus 0.405285, but unbounded n uses the rigorous proof.

## originality

PASS

The Fejér kernel, L∞ duality to L¹ distance from constants and general Markov contraction theory are established classical tools. The assessed quantitative contribution is the exact sharp periodic Lipschitz seminorm, odd n explicit extremal signs and precise leading 4/pi² deficit coefficient. Inspected Gaubert–Qu treats a different Hopf oscillation seminorm, Mishra–Sonavane discusses approximation errors for conjugate means and Kravitz–Steinerberger derivative smoothing in l2, not this exact operator norm. A classical textbook or unindexed Fejér median calculation may nevertheless exist.

## value

PASS

This sharp first-order contraction coefficient answers a natural stability question for classical Fejér summability on periodic Lipschitz functions, including exact extremizers and asymptotic rate. It is not merely another approximate-identity convergence estimate or unmotivated numeric constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
