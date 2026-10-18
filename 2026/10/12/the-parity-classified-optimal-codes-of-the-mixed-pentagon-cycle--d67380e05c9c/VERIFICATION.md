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

Column sections of a strong-product independent set have cardinalities zero, one, or two. Each nonadjacent two-set in C5 has union of closed neighborhoods all five symbols and forces both adjacent columns empty. If D and E are doubled and empty columns then D±1⊆E; hence |I|=n+|D|−|E|≤n. Cyclic ±2 singleton constructions achieve n for every n≥6 (for odd n use a five-cycle plus two-step backtracks). Equality implies |D|=|E| and D+1=D−1=E, i.e. D+2=D. If D empty all columns are singleton and their symbols trace a closed ±2 walk; if D nonempty then n is even and D is exactly one parity class, the other empty. Each occupied double section has five freely chosen C5 nonadjacent pairs. The all-length labeled count follows by choosing a0 (5), k positive signs satisfying 2k≡n(mod5), plus 2·5^(n/2) even-n codes. Independently reconstructed cyclic column-state transfer enumeration from the actual graph and got alpha n and counts 350,70,1600,360 for n=6,7,8,9; finite tests support but do not replace the equality proof. C5 spectrum gives the even/odd asymptotic growth as submitted.

## originality

PASS

PASS best-of-knowledge for equality CLASSIFICATION and exact count, not novelty of alpha=n. Read full Hales 1973 (all ten pages) and Korže–Vesel 2012 nearby graph-product result; they establish independence-number bounds and constructions, not enumerate every maximizing labeled set. Sonnemann–Krafft 1974 and Vesel 1998 are plausible prior independence-number sources, their inaccessible bodies are recorded as genuine bibliographic risks. A numerical alpha formula alone does not imply equality-case structure or number of max codebooks.

## value

PASS

Counting every optimal codebook in a canonical zero-error confusability product is a substantive complete classification for a natural infinite graph family. The two structurally different extremizer mechanisms and parity split n-even ~5^(n/2) versus n-odd ~2^n supply mathematically meaningful design diversity, without asserting new Shannon capacity or arbitrary-product results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
