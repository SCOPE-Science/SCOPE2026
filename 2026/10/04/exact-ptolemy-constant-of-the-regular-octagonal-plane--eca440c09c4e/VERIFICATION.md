---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Euclidean E dominates N. By symmetry, on a>=b>=0 with t=b/a the ratio N/E has one decreasing branch and one increasing branch, so its global minimum occurs at t=sqrt(2)-1 and equals c=cos(pi/8). Hence cE<=N<=E. Hilbert Ptolemy then gives C_Pt<=c^{-2}=4-2sqrt(2). With s=sqrt(2)-1, x=(-1,s), y=(s,-1), z=(-2,-2) have N(x)=N(y)=1, N(x-y)=2, N(z)=2sqrt(2), and N(x-z)=N(z-y)=1+sqrt(2), yielding ratio exactly 4-2sqrt(2). The upper and lower bounds therefore match globally.

## originality

PASS

Zuo's 2012 exact criteria do not cover this branch-transition extremum, and Zuo's 2018 Example 1 explicitly leaves the endpoint lambda=1/sqrt(2) unresolved for the max{ell_infty,lambda ell_1} family. Komuro--Saito--Tanaka use exactly the regular-octagonal norm for a James-constant problem, not Ptolemy. Resultary found the audited theorem as the exact direct match. A published SCOPE Euclidean-distortion formula for the containing Lorentz-predual family gives the same squared comparison factor at the octagon, but it supplies only the upper-bound ingredient and does not imply the sharp Ptolemy lower witness.

## value

PASS

The regular octagonal plane is a classical highly symmetric Banach plane, and the inspected closest family theorem explicitly leaves this exact endpoint unresolved. Closing that endpoint with a sharp comparison and explicit extremizer is a natural exact-invariant result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
