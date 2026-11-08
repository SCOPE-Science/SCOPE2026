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

For arbitrary nonempty indexed binary v and circular sentinel-free BWT, each τ-image rotation starts at one of five lexicographically separated prefix classes 001/01/100/101/110; predecessor letters yield 1^z BWT(v)0^z1^o0^o. For η(0)=0,η(1)=01, the starts at block boundaries all lead with zero and preserve the infinite periodic lexical order of v; interior starts with one contribute 0^o, yielding BWT(η(v))=BWT(v)0^o. Periodic ties have equal predecessor letters. The literal intertwining ητ=ση with σ(0)=0010, σ(1)=1, τ counts z_n=(3^n+1)/2, o_n=(3^n−1)/2, and induction for U_n prove the explicit n>=2 run-string, n=0,1 exceptions and exactly 2n runs for n>=1. Independent direct rotation sorting tested both transport identities for all 510 nonempty binary v of length 1..8 and the Chacon entire BWT at n=0..5; infinite result relies on exact five-class lexicographic argument and induction.

## originality

PASS

Qualified best-of-knowledge PASS: Frosini et al prove general BWT-run asymptotics for morphic words rather than these universal last-column identities or the explicit entire Chacon run word; Currie et al study Chacon infinite-word extremality, not circular finite-iterate BWT. Search of mathematical records did not find an equivalent exact transform; uninspected specialist full texts may have equivalent transport identities.

## value

PASS

The two universal BWT transport identities are reusable structural relations across all binary input words. They explain and exactly classify the entire transformed string and linear-in-iterate run count of a canonical nonuniform substitution family, a natural string-compression invariant; not a mere finite-prefix census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
