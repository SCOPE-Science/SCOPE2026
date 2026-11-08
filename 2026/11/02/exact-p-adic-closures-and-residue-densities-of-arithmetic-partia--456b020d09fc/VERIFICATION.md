---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For integer-started D_p(x)=x ν_p(x)/p, valuation recurrence a→a−1+ν_p(a) implies finite orbit for a0<p and eventual periodic positive valuation cycle otherwise by previously published Emmons–Xiao Theorem 8. Across its least period ell, multiplier Λ=p^(-ell) product b_j is a positive p-adic unit, and x_(t+j+k ell)=z_j Λ^k. If Λ=1 finite; otherwise e=ord_p Λ for odd p, ord_4 Λ for p=2, c=ν_p(Λ^e−1), and LTE implies closure of Λ powers is disjoint union of e principal-unit cosets modulo p^c. Scaling by each z_j gives clopen balls z_jΛ^r+p^(b_j+c)Z_p. Distinct cycle/transient valuations guarantee disjointness, so Haar measure=eΣ_j p^(-b_j-c) and C_N=t+eΣ_j p^(N-b_j-c) at stated large N threshold. Independently computed small modular orbit counts including (p,x,N)=(2,16,11),(2,64,13),(3,729,10),(5,9765625,13) and compared to ball counts. Negative integers same valuation argument. These finite modular tests support but do not establish the infinite closure.

## originality

PASS

Emmons–Xiao establish eventual valuation periodicity and ordinary real orbit trichotomy, and later extend D_p to local fields with continuity and valuation discussion. The current theorem classifies closures of full integer-value orbits in Z_p, their disjoint balls, Haar measures and exact residue-class counts. The general principal-unit lifting lemma is standard and credited, but its application to each derivative valuation cycle produces an evaluated new orbit-geometric classification.

## value

PASS

Exact p-adic orbit closure and modular density are natural dynamical invariants, complementing already-known real growth/valuation periodicity. Positivity of Haar measure for every infinite integer orbit is a useful structural phenomenon; the result is neither a trivial valuation renaming nor merely a computed small table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
