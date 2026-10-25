---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

The Chebyshev commuting identity gives finite map u→(T_m(u),T_n(u)), and gcd(m,n)=1 forces K(T_m(u),T_n(u))=K(u) via degree divisibility; the affine coordinate ring is integral under monic rescaling, hence this is normalization and the plane polynomial irreducible. Critical roots a_{d,k}=(zeta^{k}+zeta^{-k})/2 for 1<=k<d have values (-1)^k and nonzero second derivative because characteristic does not divide 2mn. Equal-parity critical pairs give precisely delta ordinary nodes. Congruences make each a_{d,k} rational; b_{d,k}=zeta^k-zeta^-k satisfies Frobenius b^q=eps_d b, so the two local tangent slopes ±(n/m)b_m/b_n are fixed or exchanged with sign eta. Each node replaces two rational normalization points by one if split, and zero by one if nonsplit, correction −eta^r per node. Exponentiating counts derives affine zeta. Independent exact polynomial enumeration checked (q,m,n)=(5,2,3),(7,2,3),(11,2,3),(13,2,3),(31,3,4) giving 6,8,10,12,34 as predicted; finite checks do not prove all-field identity.

## originality

PASS

Freudenburg–Freudenburg establish the same Chebyshev curve as rational nodal normalization in characteristic zero; the geometric part is credited. The arithmetic finite-field Frobenius action and uniform affine zeta factor are not consequences of its characteristic-zero claims or the separately inspected smooth Kummer-type maximality literature. The 2014 finite-field Chebyshev chapter remains inaccessible, retained as a genuine priority risk rather than declared noncovering.

## value

PASS

Computing zeta functions of singular rational curves and distinguishing split/nonsplit nodes is a natural arithmetic-geometric exact invariant; the uniform sign-controlled formula for all coprime Chebyshev degrees and extension fields provides a reusable nodal Frobenius-gluing law. This is not just one finite-field table entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
