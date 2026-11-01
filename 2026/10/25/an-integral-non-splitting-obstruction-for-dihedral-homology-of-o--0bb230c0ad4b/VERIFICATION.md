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

For n>k>2 every q-subset except the n complements of consecutive k-arcs is a possible facet of the cut complex, and the lower (q-2)-skeleton agrees with the full simplex skeleton. Bayer et al. Theorem 27 establishes shellability, hence vanishing H~_(q-2). The pair long exact sequence yields the canonical surjection from the skeleton top homology, naturally wedge^q of augmentation lattice U_n, onto the oriented missing-face permutation lattice. The reflection s(i)=k-1-i fixes the representative omitted face, acts there by epsilon_q=(-1)^((q-1)/2). For odd n and even k, its unique fixed vertex v lies in missing facet F; R=F\{v} is reflection-invariant and every other extension of R is by an s-paired vertex of B. Any invariant mod2 cycle lifting the F-coordinate 1 would have boundary coefficient 1 at R, contradiction. Therefore no mod2 D_n-section; an integral section would reduce to one. Independent finite parity cases n=7,9,11 are consistent but the full statement follows from the invariant-face argument.

## originality

PASS

Best-of-knowledge integral and mod-two extension nonsplitting is not implied by the prior complete rational D_n character. Prior dihedral virtual-character theorem gives rational decomposition (where finite-group modules are semisimple), not the failure of an integral equivariant section exhibited here.

## value

PASS

The nonzero extension class is motivated by the already determined rational dihedral homology representation: it detects exactly the integral/modular phenomenon invisible to that character, for an infinite natural odd-cycle/even-cut parameter family. A short parity obstruction supplies structural insight beyond table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
