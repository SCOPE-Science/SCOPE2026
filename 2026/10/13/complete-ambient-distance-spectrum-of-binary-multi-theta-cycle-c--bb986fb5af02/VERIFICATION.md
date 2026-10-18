---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The incidence-kernel cycle code of r internally disjoint length-ell paths has block-constant bits and even block parity, dimension r-1 and minimum distance 2ell (r even >=4, ell>=2). Given ambient block weights w_i, minimize sum min(w_i,ell-w_i), adding the smallest majority-flip penalty exactly when all blocks are non-tied and preferred block-parity is odd. This yields the displayed even-ell and odd-ell U_t/B polynomial identities by parity-pairing in every deviation class. For even ell=2s all-tie words alone reach radius rs (count C(2s,s)^r and 2^(r-1) nearest codewords); for odd ell=2s+1 the odd-parity zero-deviation words alone reach rs+1 (count 2^(r-1) C(2s+1,s)^r and r nearest codewords). The strict comparison uses r>=4; there is no unjustified inference from small r. An independently implemented brute min-distance count matched every ambient vector for (r,ell)=(4,2),(4,3),(4,4),(6,2), including deep-hole multiplicities; this is finite corroboration, not an infinite proof.

## originality

PASS

The matching multi-theta code in Barbosa–Marquezino–La Guardia Section 3.2 supplies the construction, dimensions, minimum distances and four examples, but the material read does not supply an ambient coset-leader distance polynomial or nearest-codeword tie counts. Solé–Zaslavsky establish covering-radius relationships for general graph cycle codes (abstract read); a general radius bound does not automatically imply every ambient shell and extremal multiplicity. Ribeiro–Cardell concerns ordinary weight enumerators of single-parity-check product codes, mathematically different from distances of all ambient words to repeated whole-block even-parity codes. Best-of-knowledge originality PASS, with important risk from the unavailable 1993 full text and other possible coset-spectrum aliases.

## value

PASS

The natural ambient distance distribution and deep-hole tie multiplicities control nearest-neighbor decoding and coset geometry of a concrete graph-cycle code introduced in the source literature. A complete closed form for all shell coefficients at all equal path lengths is a motivated exact invariant, not the already known code parameters or a routine rewriting of its codeword weight enumerator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
