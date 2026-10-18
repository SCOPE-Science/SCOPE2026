---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For B={|x|^p+|y|^q<=1} with 2<p<q, all Euclidean pullback norms arise from positive-definite quadratic forms Q and have squared distortion M(Q)/m(Q) on the Luxemburg sphere. Coordinate sign averages eliminate off-diagonal terms without worsening the two-sided quadratic comparison. For diagonal Q=diag(a,b) and t=|x|^p, the squared Hilbert norm is F(t)=a t^{2/p}+b(1-t)^{2/q}, strictly concave; its minimum is min(a,b) at an axis. Normalize this to one: a,b>=1, so any nonidentity diagonal form has strictly larger interior maximum than F_{1,1}. For Q=[[1,c],[c,1]] after sign average, nonzero c is excluded because opposite sign pairs at the unique interior maximum t_* produce a squared norm exceeding M_{p,q}, while axis minimum remains <=1. f(t)=t^{2/p}+(1-t)^{2/q} is strictly concave with derivative going from +infinity to -infinity; its unique stationary point is the displayed critical root. Independent p=4,q=6 scalar solve gives t_*=0.61977620919 and M=1.51171647247, consistent with the source and not used in the proof. Boundary p=2 and finite p<2 are explicitly excluded.

## originality

PASS

The precise coordinatewise mixed-power Luxemburg ball is asymmetric under coordinate swapping when p!=q, unlike nearby l_p/l_q norm blends. Original Musielak–Orlicz literature defines this unit ball but does not settle its Euclidean Banach–Mazur best ellipse; the superquadratic strict-concavity global classification is not implied by the identified boundary or different-norm results.

## value

PASS

The exact Hilbert distortion and unique best ellipse of a canonical coordinate-variable-exponent norm gives an independently useful geometric invariant across a natural nontrivial continuum, beyond routine scalar substitution into an existing theorem. The proven symmetry and strict uniqueness distinguish coordinatewise anisotropic norms from exchangeable power blends.

The dated certificate retains the supplied scientific assessment, sources and limitations.
