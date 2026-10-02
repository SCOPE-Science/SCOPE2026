---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

Let m=a+1 and c=b+1. A primitive divisor s of p^(kc)-1 divides B=σ_k(p^b), has ord_s(p)=kc and s>c; divisibility forces s|m, hence m≥kc+1. A primitive divisor r of 2^(km)-1 (apart from the sole km=6 exception, immediately incompatible with m≥kc+1) divides A=σ_k(2^a), satisfies r>m>c, and therefore must equal p. Thus m|p-1; since s|m, p≡1 mod s, contradicting ord_s(p)=kc≥4. The finite verifier's 42,112 cases and zero hits corroborate but do not prove the infinite theorem.

## originality

PASS

No located source states uniform nonexistence of k-harmonic numbers 2^a p^b for all k≥2. Standard summaries report only weaker congruence restrictions. The primary 1998 paper remained inaccessible despite OA searching; the authorized Oxford fallback returned a transport/request error, so that source is a named residual risk rather than novelty evidence.

## value

PASS

Uniformly eliminating every even two-prime-support candidate for all k≥2 is a natural structural advance over congruence filters and materially narrows the search for proper power-harmonic numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
