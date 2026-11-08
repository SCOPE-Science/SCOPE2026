---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For even k, RC orbit counts (2^k+2^(k/2))/2 give 3,10,36 at k=2,4,6. Explicit witnesses cover the first two bounds. The 5 high-potential and 5 RC-low-potential states produce a 0..3 nonnegative six-mer cost constant on RC classes. An independent enumeration of all 64 six-mers verified eight fixed words, sum 18 of fixed-word weights, and total 41 when counting all 36 RC classes once. Telescoping along any linear word yields total cost at most L+2 for L six-mer windows, forcing L>=39. Independently evaluated the explicit 44-bit word and found all 36 classes among its 39 windows, with precisely three classes appearing twice and zero weights on those repeats. This is a universal lower bound plus exact witness, not inference from brute-force search over all strings.

## originality

PASS

The exact claim is not established as a corollary or table entry in the inspected relevant material; foundational objects, algorithms and covered subclaims are separately credited. This is a qualified best-of-knowledge comparison, not absolute priority certification.

## value

PASS

A compact nonnegative potential certificate resolves the first binary even-order deficit for a basic de Bruijn/reverse-complement covering problem. The precise value 44 and three-window obstruction are natural length and symmetry invariants, useful independently of the established general polynomial algorithm; the displayed dual proof explains why orbit counting fails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
