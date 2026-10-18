---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

The claim fixes the Yamaguchi--Tajima three-parameter qutrit unitary model, real r=(p-q)/(p+q) in (0,1), kappa=4(p-q)^2/(p+q), and weights G=kappa diag_block(W,h) with W=[[a,c],[c,b]] positive definite (D=ab-c^2>0) and h>0. From the source's exact inverse beta-QFI, the upper 2x2 real correction X must obey X>=0 and det X>=beta^2 r^2; conversely those are precisely the upper Hermitian PSD block conditions. Weighted trace AM-GM gives tr(W X)>=2 sqrt(det W * det X)>=2 beta r s for s=sqrt D, attained at X_beta=beta r s W^{-1}; the independent third constraint is kappa V33>=1-beta^2 r^2 and is simultaneously tight. Thus exact fixed-beta cost is a+b+h+2 beta r s-h beta^2 r^2. Its supremum on 0<=beta<1 occurs at beta*=s/(hr) when s<hr and at beta->1^- when s>=hr, giving the stated two formulas. A single V feasible for ALL beta must satisfy det X>=r^2 and kappa V33>=1; both bounds are simultaneously attained by X*=r s W^{-1}, kappa V33=1, whose 2x2 determinant of the Hermitian slack equals r^2(1-beta^2)>=0 and whose third slack is beta^2 r^2>=0. This proves exact Holevo=a+b+h+2rs, with strictly positive gap hr^2 in boundary branch and s(2hr-s)/h in interior branch. At s=hr, both formulas match; at s>0, h>0, 0<r<1 no degeneracy. Read verifier file to check which assertions it actually tests; analytically checked the matrix conditions and both branches, not merely its dense beta grid.

## originality

PASS

Best-of-knowledge PASS for an entire four-dimensional positive-definite block-weight cone and exact piecewise optimizer. The September 2026 originating paper evaluates only isotropic weight; the earlier MLD theory is general framework, not this exact qutrit phase diagram.

## value

PASS

The natural block-compatible weight family is the largest simple cone respecting the source qutrit split, not an arbitrary numerical slice: it exhibits a global strict MLD/Holevo separation, a sharp optimizer regime boundary s=hr, and exact tradeoffs among weights including correlations c. It upgrades a single isotropic witness to a complete solvable family and clarifies which beta-bound dominates, of use in multiparameter quantum estimation. No claim for fully general coupled 3x3 weights or finite-copy implementability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
