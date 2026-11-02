---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: Examined exact overlapping occurrence definition, including a=b=c=0 and empty boundary factors. For zero-only MUS only a unique largest positive zero-run works. Every minimal unique factor with one 1 has exactly one distinguishing left or right flank; exclude it when its zero-only maximal proper subfactor is already unique. Every two-1 MUS must equal 1 0^b 1 and requires a,c>=b. This exhausts all possible substrings; the disjoint cases yield the four-factor iff and the four rational generating functions via weak-composition case splits. Coefficient singularity extraction yields 1/3 and 2/3 limiting proportions. Independent complete occurrence-count enumeration for 0<=a+b+c<=23 checked exact MUS sets, equality cases, and each generating-function coefficient; this finite corroboration does not establish the all-length exhaustion.

## originality

PASS

PASS with explicit historical risk: Ilie–Smyth (2011) introduce MUSs and repeat duality, not visibly the fixed-Hamming-weight enumeration; its full text remained inaccessible. Mieno et al. (MFCS 2016) Lemmas 7–8 yield a coarser run-count bound and longest-run subcase, but do not imply the sharp weight-two spectrum. A sliding-window algorithm treats varying windows, not this census. The exact all-length GF classification appears distinct on available full-text comparison; no unsupported absolute priority claim.

## value

PASS

PASS: Weight-two binary words are a canonical sparse-marker model with arbitrarily long zero runs. Four explicit factor patterns give a length-independent sharp bound and complete distribution of local exact-uniqueness complexity; the one-third extremal density is a natural sharp asymptotic. This is not merely implementing a generic MUS finder or a tiny finite observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
