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

## Reproduction
Execute `python3 CHECK.py` using Python 3.9 or later, with no third-party packages. The script recomputes the polynomial's exact eight vertex values, a rational interval for \(\pi\), all \(88\) strict positive principal-minor certificates for odd \(3\le q\le23\), and all \(39\) strict negative fixed-vector certificates for odd \(25\le q\le101\). It also checks \(\pi^2<10\), the rational tail inequality at \(q=103\), and the same cutoff for a uniformly strictly positive constant-mixture kernel, which supports the analytic proof for every larger odd base.

## Proof obligation and bounds
The interval engine represents real numbers by integer endpoints scaled by \(10^{35}\) and rounds every multiplication and division outward. The alternating arctangent and cosine remainder signs give enclosing intervals, not floating-point approximations. Leading principal minors are evaluated by exact Laplace recursion with interval operations; Sylvester's criterion then converts their certified signs into positive definiteness. The infinite-base conclusion uses the separately proved coordinate Lipschitz bound and is not inferred from a finite list.

## Scope of checking
The checker establishes the finite strict inequalities and arithmetic constants for the explicit example. It does not prove that \(25\) is minimal among arbitrary one-variable constructions, inspect unpublished papers, or constitute independent validation. No numerical timeout or missing test is treated as mathematical evidence.
