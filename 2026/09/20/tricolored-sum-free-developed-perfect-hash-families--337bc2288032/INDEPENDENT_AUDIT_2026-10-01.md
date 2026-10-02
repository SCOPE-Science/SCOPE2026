---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

Diagonally translation-developed three-row perfect hash families over a finite abelian group \(G\) are in exact correspondence with tri-colored sum-free sets in \(G\); consequently their maximum column count is \(|G|M_3(G)\), with the stated fixed-characteristic asymptotic transfer and the verified \(81\)-symbol specialization.

## Correctness — PASS

Normalizing each free diagonal-translation orbit to first coordinate zero gives one seed pair. From a tri-colored sum-free seed, equality of two rows for a pair of columns forces equal seed indices, while any unseparated triple produces an off-diagonal zero-sum equation; hence the developed array is a perfect hash family. Conversely, translation closure turns any repeated seed coordinate or any off-diagonal zero-sum relation into three distinct columns with no separating row, so a developed perfect hash family yields a tri-colored sum-free set. This proves the exact bijection and factor \(|G|\). The finite-field corollary was independently replayed from the actual verifier: the twenty fourth powers in the displayed model of \(\mathbb F_{81}\) have no nontrivial zero-sum triple, and the developed family therefore has \(1620\) columns. The exponential-order consequence is then a direct transfer of published tri-colored sum-free upper and lower growth bounds.

**Checked sources.** assigned RESULT.md at frozen tree a3a73ffadb2a075c1f0b531c04d4e30402ea8b52; artifacts/verify_f81_phf.py blob b0348cd7ea97c9094753ce0656a65c0206a3a5a7; Walker--Colbourn 2007; Shangguan--Ge 2016; Blasiak et al. 2017 tri-colored sum-free bound

**Residual risks.** The exact correspondence could occur under group-developed triple-system or induced-matching terminology not retrieved by the searches.

## Originality — PASS

Walker--Colbourn's progression-free developed construction is a strict special seed, and Shangguan--Ge connect perfect hash families to additive/hypergraph extremal objects, but the inspected statements do not identify arbitrary unions of full diagonal translation orbits with tri-colored sum-free sets or give the resulting exact structured capacity.

### Equivalent formulations

The progression-free construction is recovered by a special diagonal tri-colored seed, whereas the audited theorem classifies every developed orbit family.

### Broader coverage

The additive-combinatorics theorems determine the seed capacity after the new correspondence; they do not themselves identify the perfect-hash subclass.

### Exact database or table

A parameter table cannot imply the exact structural bijection or asymptotic exponent of the developed class; the finite \(81\)-symbol comparison is secondary to the theorem.

### Claim versus prior implication

Neither prior implication mechanically yields the converse classification of all diagonally developed three-row families.

**Checked sources.** https://doi.org/10.1515/JMC.2007.008; https://doi.org/10.1137/15M103827X; https://doi.org/10.19086/da.1245; Resultary semantic search

**Residual risks.** The full Walker--Colbourn article was not read line by line; terminology-equivalent group-developed folklore remains possible.

## Value — PASS

The result exactly classifies a natural symmetry-restricted perfect-hash class rather than merely giving another construction. It transfers a well-motivated additive-combinatorics capacity to perfect hashing and explains a genuine exponent loss caused by diagonal translation symmetry.

**Checked sources.** Walker--Colbourn perfect-hash constructions; Shangguan--Ge additive/hypergraph framework; tri-colored sum-free growth literature

**Residual risks.** The finite \(81\)-symbol example is illustrative; the structural correspondence carries the value judgment.

## Limitations

- The correspondence is specific to three rows, strength three, and simultaneous diagonal translation.
- The asymptotic exponent concerns only the developed subclass, not unrestricted perfect hash families.
- The \(81\)-symbol construction is not claimed to be the current global record.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
