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

The singleton counterexample was checked directly against the source definition. On \(M=\{u\}\), all maps are automatically Lipschitz. With \(\tau_n=u\) for all \(n\), \(f_1(u)=1\), and \(f_n(u)=0\) for \(n\ge2\), the analysis vector is \(e_1\), the synthesis map on \(\ell^1\) is bounded by \(\|u\|\), and the frame map is the identity. Its range is exactly \(\operatorname{span}\{u\}\).

For the replacement theorem, reconstruction gives \(M\subseteq\operatorname{Ran}(\theta_\tau)\). Linearity gives the lower inclusion. For finite \(p\), coordinate truncations converge in \(\ell^p\); bounded synthesis carries them to finite linear combinations of atoms, giving the upper inclusion. Taking closures yields equality of the two closed spans.

No finite experiment, numerical approximation, or unproved classification is used. No claim is made that the synthesis range is closed in general.
