---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Independent reconstruction: with odd p and (s,h)=(a+b,a−b), a^e+b^e=(s^e+h^e)/2 by Frobenius, so for fixed s nonzero collision fibers are multiplicative orbits of H={ζ:ζ^e=1} of cardinality g. Two-dimensional additive-character orthogonality yields ||Tf||_{L⁴(prob)}⁴=∑|R_f(s,y)|², no residual q factor. The exact pairwise variance identity g∑|z|²−|∑z|²=∑_{unordered pairs}|z_i−z_j|² gives ||Tf||⁴=gS²−(g−1)∑|f|⁴−orbit_deficit, and scalar Cauchy ∑|f|⁴≥S²/q gives sharp g−(g−1)/q with constant f equality. Equality iff nonzero f has constant positive modulus and phase-product invariance along H orbits. Euclidean gcd for gcd(p^k+1,p^m−1) gives g=2 when m/d odd, p^d+1 when m/d even; when g=2 phase conditions automatic. For g>2, Fourier-in-x of real infinitesimal phase relations forces any nonzero character β to satisfy trace(βζy)=±trace(βy) for all y, impossible unless ζ=±1 because union of two proper F_p subspaces cannot exhaust F. Thus real solution space is constants and projective compact phase group is finite; quadratic trace(αt^(p^d+1)) supplies nonlinear finite members. Independently constructed F₉ using α²=−1 over F₃: exponents e=4,10,28 give respective g=4,2,4, collision cardinalities (9 singleton+18 quadruple), (9 singleton+36 pairs), (9 singleton+18 quadruple) and exact constant-amplitude norms 11/3,17/9,11/3, as predicted. These finite counts corroborate, not prove, universal theorem.

## originality

PASS

Best-of-knowledge sharp L²→L⁴ Gold-graph operator fourth moment, exact orbit deficit and projective phase rank dichotomy are not in the inspected earlier odd-characteristic planarity results or recent other-surface sharp-extension theorem. Binary Gold graph results are in characteristic 2 and do not imply these p-odd midpoint/orbit formulas. The older planarity arithmetic is expressly not claimed new. Residual unknown equivalent additive-energy coding-theory formulations remain possible.

## value

PASS

A sharp weighted Fourier extension constant, exact nonnegative deficit and topological dichotomy of all optimizer phases solve a natural restriction/equality problem across complete arithmetic subfamilies. The nonplanar finite-vs-torus jump and nonlinear optimizers go beyond a routine gcd count or normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
