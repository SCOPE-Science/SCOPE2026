# Independent audit — 2026/09/16/002

**Date:** 2026-09-29  
**Disposition:** **REPAIRED**  
**Audited tree:** `19007d3fb15df556e6c2f2b1afd217c1d8dec916` at repository commit `253a0fe5d0217455660a277f9adb940030e567ad`

## Correctness

**PASS** — The quotient description gives exactly L+1 endpoint classes R_j and L endpoint classes C_i, with L(L+1) interval edges. The resulting graph is connected; hence b1=E-V+1=L(L-1). Removing R_0 leaves exactly L components, removing C_i leaves two, removing R_j for j>=1 leaves the graph connected, and an interior point of an R_0-C_i bridge creates two components while an interior point of an edge in an L-fold bundle does not. Therefore the punctured-component maximum is L and distinct L are non-homeomorphic.

## Originality

**PASS_WITH_CAUTION** — The July 2026 Obermeyer–Winter preprint supplies the quotient model but the inspected public descriptions do not state these elementary graph invariants. The calculation is a plausible useful corollary, but the filed “first invariant computation” priority wording was stronger than the evidence supports and is removed.

## Value

**PASS** — Although elementary once Proposition 5.1 is decoded, recovering L from the topology of each finite-stage spectrum is a concrete structural lemma relevant to comparing finite stages and constraining any future analysis of the inverse-limit diagonal spectra.

## Literature/evidence checked

- [Obermeyer–Winter, A C*-diagonal in the Jiang-Su algebra via entangled matrix cones](https://arxiv.org/abs/2607.03129): Source of the finite-stage quotient X_L and the inverse-limit diagonal construction.
- [Barlak–Raum, Cartan subalgebras in dimension drop algebras](https://arxiv.org/abs/1712.01957): Background on spectra of Cartan subalgebras in dimension-drop algebras.

## Limitations of this audit

Main-branch tree and blob guards were checked before staging and matched the assignment. Literature search is claim-specific and is not a proof of absolute priority. GitHub was read only; no repository writes were made. No inaccessible source is claimed as read.
