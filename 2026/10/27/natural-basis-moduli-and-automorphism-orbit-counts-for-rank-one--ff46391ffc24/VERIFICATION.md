---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In a natural basis the form B is diagonal with both entries nonzero by nondegeneracy. A basis up to separately rescaling and reordering is an unordered pair of transverse orthogonal lines; orthogonal complementation on nonisotropic lines is a fixed-point-free involution. Rescaling u rescales B, changing its determinant by a square and leaving B(u,u)=0 invariant. An automorphism has Tu=cu and B(Tx,Ty)=cB(x,y). If B(u,u)≠0 then c=1 and T is ±1 on the orthogonal line while fixing u. If B(u,u)=0, choose an isotropic v with B(u,v)=1 by subtracting B(v,v)u/2 from a suitably normalized mate. The same equations force Tv=v, and all nonzero c are allowed. There are at most two exceptional isotropic lines over an infinite field, giving infinitude; dimension one has only one basis class under scaling. Over an odd finite field the isotropic line count is 1+χ(-Δ), giving N. In the hyperbolic coordinates L_t=K(u+tv), complementation sends t to -t and the automorphism sends t to t/c, proving transitivity. For nonisotropic u, the reflection fixes the coordinate pair. Any other fixed pair must be swapped; orthogonality of u+tv and u-tv requires t²=B(u,u)/B(v,v), and such lines are nonisotropic because their norm is 2B(u,u)≠0. Two roots give one pair exactly when χ(Δ)=1. Burnside gives the claimed O and the fixed-point count, including the small fields.

## originality

PASS

The exact Aut(E)-orbit census and its fixed-pair refinement are the supported distinct content of the joint theorem. The automorphism types are already known, the form and orthogonal-pair description use established machinery, and a distinct indexed record explicitly contains the same moduli description and N(E). Do not award separate novelty for those components. No inspected statement supplies the extra involution fixed-pair count and O(E) across both generator types. The available survey comparison supports the relevance of the finite-group example, not novelty of its algebra or automorphisms.

## value

PASS

The equivalence by scaling and reordering is the one singled out by the survey. Computing how many of those bases remain inequivalent after intrinsic symmetry answers a further natural classification question, which knowing the group and the total number of bases does not settle. For example, a hyperbolic form over F7 gives three basis classes for either generator type, while an isotropic generator leaves one automorphism orbit and a nonisotropic one leaves two. The count distinguishes a concrete effect of the distinguished derived line, rather than tabulating illustrative prime-field examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
