---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For every canonical four-spine tuple (a,b,c,d), a,d≥2,b,c≥1, sum N≤200 and (a,b,c,d) lex≤(d,c,b,a), the color transfer weights w_s(j;z)=z^j(Σ_{h≠j}z^h)^{s−1} give exact P_T(z)=ps4(X_T) using 4-state recurrence. Modulo 2^64 reduction commutes with operations; equality of full polynomials would force identical pairs of residues at z=2,3. The pinned verify.cpp enumerates every canonical tuple and uses equality-aware hash map (not hash-only testing), zero collisions and total 31,060,953 types. Independently implemented a different backward-transfer exact mod-2^64 C++17 exhaustive checker across N=6..200; all 31,060,953 canonical classes counted and no identical residue pairs per N. No claim beyond N≤200. Burnside formula total (62,117,055+4,851)/2=31,060,953 independently agrees.

## originality

PASS

Bingham et al. 2026 Conjecture 6.2 explicitly proposes ps4(X_T) separates all caterpillars; their Section 6 checked all caterpillars through 25 vertices and selective five-spine cases through 50. The complete four-spine N≤200 finite census with a two-residue deterministic separator is a strictly larger different finite domain not covered by inspected published checks. No claim of infinite separation.

## value

PASS

Substantial independently replayable 31-million-class finite extension of a recent explicit conjecture, on a natural fixed-spine family, with a compact deterministic modular fingerprint. Computer assistance does not make this meaningless; exact finite cutoff and corroborated full census are mathematically useful independent of an unfinished all-order conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
