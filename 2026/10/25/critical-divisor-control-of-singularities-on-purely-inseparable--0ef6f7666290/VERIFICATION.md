---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The polynomial is integral because f squarefree of degree p is not a pth power in k(t); z^p-f is irreducible over k(t). The map onto P1 is finite purely inseparable degree p. Jacobian criterion, F_z=0, and Euler homogeneous identity in characteristic p reduce singularity to vanishing coefficient differential dh on affine charts. At critical point the local value f0 is nonzero (simple roots prevent df=0 at f=0), and its first nonconstant term order m>=2 is <=p-1 because f is degree p, is not a pth power (otherwise multiple root), and derivative degree <=p-2. Since gcd(m,p)=1 an mth-root formal coordinate substitution absorbs the higher unit and yields v^p=u^m; normalization via u=s^p,v=s^m proves semigroup and gap count. Transition of f across P1 charts has degree p, whose derivative cross term vanishes in characteristic p; df is nonzero section O(p-2), so sum critical vanishing multiplicities m-1=p-2 and deltas sum plane arithmetic genus (p-1)(p-2)/2. A unibranch integral curve with zero normalization genus has normalization P1. Independently checked char5 polynomial expansion h(2+u)=3+u²+u^5 and infinity 1+s³+s⁴; semigroup gaps give 2+4=6. These finite checks do not prove all p.

## originality

PASS

Best-of-knowledge PASS for the global critical-divisor distribution, not the classical local monomial cusp semigroup formula alone. Fong–Maccan 2024 Example 3.13 explicitly studies the same z^(p^r)=f squarefree curve and its fixed points/multiple-fiber application, but the relevant inspected full primary text does not give the local critical-order semigroup list. Brion 2024 Theorems 1–2 gives equivariant local covers and total arithmetic-genus/Hurwitz relation, not this explicit pointwise critical divisor formula in the inspected introduction and theorems. Standard singularity classifications can give individual monomial branch types, so an uninspected local paper or other algebraic geometry source might imply the result after specialization. No blanket uniqueness claim.

## value

PASS

The exact singularity profile of a natural purely inseparable family used in elliptic surface constructions is determined by a computable divisor on P1; the theorem locates every singular point, its analytic type, value semigroup and delta, not just the total arithmetic genus. The p=5 example exhibits two distinct cusps on one curve. This natural finite-prime family invariant is structurally useful even though individual branch formulas are textbook.

The dated certificate retains the supplied scientific assessment, sources and limitations.
