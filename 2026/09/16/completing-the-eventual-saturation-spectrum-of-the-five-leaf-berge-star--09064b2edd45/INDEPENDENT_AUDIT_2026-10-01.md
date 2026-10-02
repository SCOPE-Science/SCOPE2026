# Independent audit — 2026-10-01

## Finding

**Disposition: passed.** The final claim was reassessed on correctness, originality, and scientific value.

## Correctness — PASS

The proof's finite residual reduction and padding logic were reconstructed. Independently of the package verifier, all 40 stored seed hypergraphs were checked from the actual seeds.json: edge counts/deficits are consistent, every vertex link has Berge matching rank at most four, and every missing triple creates rank five at some incident vertex. A separate exhaustive edge-branching implementation reproduced zero saturated witnesses for (n,d)=(6,3),(7,3),(8,3),(9,3),(8,4), with positive controls (6,4) and (9,5) agreeing. Together with the inspected Bushaw et al. lower interval/local lemmas and the K5/lantern padding arithmetic, these establish the four nonzero-residue rows for all sufficiently large n.

## Originality — PASS

Bushaw et al. explicitly state the exact five-leaf spectrum under the divisibility condition 5|n and leave only constantly many top values in general. The audited exclusions and seed constructions close the nonzero residue classes; no inspected stronger extremal/saturation source or published-record search implied those rows.

### Equivalent formulations

The nonzero-residue deficit table is not an equivalent restatement of the divisible-order result.

### Broader coverage

No stronger inspected theorem was found that implies the missing deficit exclusions and all required positive constructions.

### Exact database or table

The new finite classifications are not copied from a known table identified in the search.

### Claim versus prior implication

The final nonzero-residue rows require both exclusions and constructions beyond the cited prior implications.

### Sources inspected

- The Saturation Spectrum of Berge Stars — https://arxiv.org/abs/2502.17686: STRONG_PRIOR_BUT_NOT_COVERING_NONZERO_RESIDUES. The exact five-leaf spectrum is stated for 5 dividing n, while the general result leaves constantly many top values.
- Nearly-Regular Hypergraphs and Saturation of Berge Stars — https://doi.org/10.37236/8363: INPUT_NOT_COVERING. It supplies the minimum edge count, not the entire eventual spectrum.
- Turan numbers for hypergraph star forests — https://arxiv.org/abs/2001.05631: NOT_COVERING_SPECTRUM. It constrains extremal edge counts but does not provide the full saturation spectrum or the nonzero-residue deficit exclusions.

## Scientific value — PASS

Completing the four missing residue classes is a natural exact classification problem left by a recent saturation-spectrum theorem. The result combines genuine finite obstructions with constructive coverage of every remaining upper-range deficit, rather than an arbitrary census slice.

## Limitations and residual risks

The classification is eventual and does not determine the least threshold N. It uses prior eventual lower-interval results plus explicit finite exclusions and seed/padding constructions for the upper range.
