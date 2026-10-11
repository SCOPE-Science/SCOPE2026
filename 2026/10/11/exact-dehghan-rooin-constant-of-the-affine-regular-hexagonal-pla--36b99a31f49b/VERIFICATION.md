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

The proof was checked from the exact unit-sphere formulation of the Dehghan–Rooin constant. The norm identity \(N(s,t)=\operatorname{rng}(0,s,t)\) turns unit vectors into range-one triples modulo common-coordinate shifts. Simultaneous coordinate permutations give the full dihedral symmetry needed to normalize one triple, and exchange of the two vectors replaces \(q\) by \(q^{-1}\), so \(0<q\le1\) is sufficient.

The six relative permutations were checked against the four proof cases: identity, reversal, a paired transposition type, and a paired cycle type. The transposition and cycle bounds both reduce to \(\sqrt q(2-q)\); the identity and reversal cases are at most \(1\). The exact polynomial certificate
\[
\frac{32}{27}-q(2-q)^2=\frac{(8-3q)(3q-2)^2}{27}\ge0
\]
holds for \(0<q\le1\), with equality only at \(q=2/3\).

For the displayed vectors \(u=(0,1)\), \(v=(1,2/3)\), and \(a=\sqrt{2/3}\), direct exact evaluation gives
\[
N(u-v)=4/3,\qquad N(a u-a^{-1}v)=\sqrt{3/2},
\]
so the squared quotient is exactly \(32/27\).

The companion `verify_exact.py` replays these finite exact checks with rational arithmetic. It does not certify the infinite optimization by enumeration; that step is supplied by the monotonicity and case analysis in the proof. No claim is made about all maximizers or other polygonal norms.
