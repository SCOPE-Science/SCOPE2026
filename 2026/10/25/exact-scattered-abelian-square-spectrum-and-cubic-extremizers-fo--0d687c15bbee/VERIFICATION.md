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

All zero-only squares are 0^(2h). Every other admissible square uses both ones on opposite halves, so the middle-zero run j obeys j>=|i-k| and j congruent to |i-k| mod 2; this proves the exact three-run count, including empty runs. The length-2h spectrum is a rectangle/diagonal lattice count using a clipped quadratic Q(t). Uniform O(n^2) sum/integral comparison reduces cubic growth to V(a,b,c)=integral integral (b-|x-y|)_+; strict balancing a=c and one-variable differentiation identify unique proportions 2:3:2 and maximum coefficient 2/147. Compactness proves only-if asymptotic rigidity. An independent brute-string enumerator agreed on every length and total for all 216 triples a,b,c<=5.

## originality

PASS

Fici–Mignosi–Shallit (2017) explicitly count contiguous abelian-square factors, including sparse-one constructions with quadratic factor counts, not distinct scattered subsequence strings. Fici–Puzynina (2022) surveys abelian repetitions and binomial/subsequence equivalence without supplying this fixed-source length spectrum or 2/147 cubic optimization; arbitrary alphabet-wide abelian-square enumeration by Richmond–Shallit also does not specialize to occurrence as subsequences of a fixed two-one word.

## value

PASS

Natural first nontrivial sparse-minority model where requiring both minority symbols forces an unexpectedly cubic family of distinct abelian-square subsequences. Exact length-by-length enumeration and a unique sharp maximizing run proportion answer a motivated extremal question, not merely a table of examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
