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

PASS: Over Watson–Crick four-letter alphabet, the reverse-complement involution on 256 four-mers has 136 orbits including 16 fixed words. Imposing all self/cross prefix–suffix nonoverlap lengths 1..3 and pairwise aligned Hamming distance≥2 leaves 56 individually valid orbits (12 singleton,44 doubleton). Their exact compatibility graph has 420 edges; RC-closed codebooks biject to its weighted cliques. The strictly decreasing exclusion/inclusion recursion F(S)=F(S\{v})+z^{s(v)}F((S\{v})∩N(v)) gives H(z)=(1,12,88,288,584,760,688,424,160,32), total 3037 and maximum 9 with 32 maximizers; the complement-preserving relabeling group has order 8 and acts in four full orbits, 24/8 structural split. Independent code rebuilt the graph and exact clique polynomial (1318 memo states), matching all ten coefficients. Source direct-word backtracker additionally verifies orbit classes. The finite exhaustive recursion proves exactly length 4, not arbitrary lengths.

## originality

PASS

PASS (qualified): Blackburn 2013/2015 determines general non-overlapping code bounds without Watson–Crick closure or aligned Hamming≥2; King 2003 studies constant-GC DNA codes with Hamming separation from reverse complements, a materially different condition from closure (including allowed self-RC fixed words); Mir et al 2013 investigate longer barcodes. No inspected full primary results determine this exact restricted weighted-clique spectrum; specialist four-mer enumerations remain residual priority risks.

## value

PASS

PASS: A natural DNA barcode/synchronizing-code design conflict combines Watson–Crick reversal symmetry, strict frame nonoverlap and single-substitution detection. The complete four-mer cardinality polynomial and symmetries give an exact small-block feasibility benchmark and all optimal codebooks; the finite scope is inherent and mathematically motivated rather than an arbitrary isolated integer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
