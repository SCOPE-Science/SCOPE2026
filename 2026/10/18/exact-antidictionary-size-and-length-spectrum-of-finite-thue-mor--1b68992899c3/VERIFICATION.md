---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Reconstructed the exact domain T_m=phi^m(0), m>=3, contiguous rather than scattered/cyclic factors. For R=2^(m-2), distinct parity-recognizable R+1 windows give all 3R infinite factors (p(R+1)=3R), while length R+2 has 3R-1 finite versus 3R+4 infinite factors, exactly five new minimal absent boundary factors. The published infinite bispecial classification and checked substitution of context pairs yield two forbidden triples and four minimal absent extensions at each 3*2^j+2. A putative longer minimal absent word would force two occurrences of a unique R+1 interior. Independent direct substring enumeration (different code from package verifier) for all m=3..9 reproduced 4m-5 and full spectra, including m=9 count 31, lengths 3:2; 5/8/14/26/50/98:4 each; 130:5. The infinite theorem follows from the proof and cited bispecial result, not finite enumeration.

## originality

PASS

Best-of-knowledge originality restricted to the evaluated finite dyadic antidictionary count, complete missing-length spectrum and five endpoint factors; the infinite bispecial families and finite CDAWG structure belong to Radoszewski–Rytter, and general minimal-absent-word extraction is pre-existing. Read their primary theorem and factor-graph descriptions and compared their mathematical implications. The exact closed dyadic count and endpoint spectrum were not located as a stated/derived invariant; full CDAWG descriptions might still make them a straightforward corollary, an explicit priority risk.

## value

PASS

Minimal absent factors form a natural succinct description of an automatic word language; determining every length and the exact logarithmic number for ALL dyadic finite iterates is a meaningful complete invariant, distinguishing substitution-forbidden internal factors from the five truncation-boundary missing factors. It is not merely generic algorithm execution or arbitrary isolated computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
