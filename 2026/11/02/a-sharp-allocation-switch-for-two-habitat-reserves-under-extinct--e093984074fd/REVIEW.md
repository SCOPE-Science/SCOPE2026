# Scientific review: two-reserve area-allocation switch

## Correctness — PASS

The result explicitly specifies all four states, the absorbing state, the starting state, and the positive-rate domain. Three first-step equations give an exact rational absorption-time formula, which reduces algebraically to a convex quadratic in \(z=x(A-x)\). The image of the feasible area interval and the exact endpoint difference prove *all* global equality cases; derivative signs prove coexistence of two distinct local-maximizer geometries. The package verifier forms the transient generator independently and passes 73,158 exact-rational assertions. Finite checks support, but do not replace, the universal proof.

## Originality — PASS within inspected evidence; residual historical risk

The earliest anchor is Etienne–Heesterbeek (2000), which establishes an area-and-number reserve-design framework but, in the accessible abstract, adjusts the number and common size of patches rather than the present fixed-two-site unequal split. Full text was unavailable and its exact mathematical coverage remains a risk. Hernández-Suárez et al. (1999) was read as a full primary article; its patch-count model assumes identical patches and optimizes neither heterogeneous area allocation nor the critical split switch. Day and Possingham (1995) already treat patch-area heterogeneity with 2-to-the-number-of-patches *discrete-time* transition matrices; the author-uploaded public text was read for its model, two-patch matrices and unequal-area scenarios. It does not identify an exact continuous-time all-allocation area switch, but its framework is an important ancestor. Etienne (2000) also treats heterogeneous patch sizes and rescue using a mean-field Levins-type model. Ovaskainen (2002), Frank–Wissel (2002), and Etienne–Heesterbeek (2001) provide related persistence criteria, but inaccessible full manuscripts limit negative coverage claims.

A previous mathematical treatment of the same four-state chain optimizes recolonization *alone* under fixed local extinction rates. It supplies a useful baseline but not the claimed jointly area-dependent optimization; substituting a variable area changes both rate families and yields an optimality reversal that its fixed-rate optimizer does not cover. The claim is therefore assessed as a distinct area-coupled design theorem, not as a new Markov-chain technique or universal conservation law. Earlier equivalent theorems could still exist.

## Value — PASS

The fixed-total-area reserve-design problem is motivated by a longstanding fragmentation and habitat-persistence question. Its exact threshold is structurally informative: increasing rescue effectiveness produces a discontinuous switch between maximally unequal and balanced designs, with coexisting local maxima near the transition. The result classifies all admissible continuous area splits and supplies exact switching costs, rather than reporting a tuned numerical optimum. It is a benchmark for the stated stylized ecological assumptions, not field advice.

## Sources and scientific limits

- Etienne & Heesterbeek (2000), DOI 10.1006/jtbi.1999.1060: published abstract and metadata inspected; full text not available.
- Hernández-Suárez, Marquet & Velasco-Hernández (1999), DOI 10.1006/bulm.1998.0084: full lawful open-access paper read, including model and stochastic absorption-time argument.
- Ovaskainen (2002), PMID 12384046: abstract inspected, full text not available.
- Frank & Wissel (2002), DOI 10.1086/338991: abstract inspected, full text not available.
- Etienne & Heesterbeek (2001), DOI 10.1086/321986: abstract inspected, full text not available.
- Day & Possingham (1995), DOI 10.1006/tpbi.1995.1034: author-uploaded online full-text passages on model, two-patch matrices, and heterogeneous landscape scenarios were read.
- Etienne (2000), DOI 10.1006/bulm.2000.0186: abstract inspected, full text unavailable.

Self-review: passed. Independent audit: not yet performed.
