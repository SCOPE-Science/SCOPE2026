# Scientific review: Möbius-ladder proper conflict-free colorings

## Correctness — PASS

The graph model is a two-row strip with a row-swapped closing edge. The local three-color argument excludes swapped successive columns and direction changes, forcing a three-step column orbit incompatible with that closure. Proper two-colorings of cubic graphs also fail the unique-neighbor-color condition. A concrete family of four-color words provides the reverse inequality at every length. For the enumeration, the transfer states encode exactly two adjacent columns, and their transitions test both properness and the two open-neighborhood singleton conditions. Row exchange commutes with the transfer and splits its 84 states into two explicit 42-dimensional integer matrices. Their full characteristic polynomials were recomputed by an integer algorithm, yielding the formal trace generating function and the closed twist correction. The package's `verify.py` passed independently reconstructed graph checks, full characteristic-polynomial comparisons, and finite-width consistency tests. No finite experiment is used as a substitute for the all-length arguments.

Risk and scope: the characteristic-polynomial identities are substantial finite algebra; reproducibility depends on running the included executable certificate and the explicit state definition, not on an unseen table. The graph definitions, small-order boundary, fixed named colors, and formal omission of degenerate one- and two-column walks are stated explicitly.

## Originality — PASS, with residual historical-priority risk

Lu, Ying, and Song (arXiv:2608.29375v1, public August 29, 2026) prove proper conflict-free four-choosability for subcubic graphs. That is stronger as a general *upper bound*, but does not determine whether three colors suffice on Möbius ladders and does not count optimal colorings. The accessible complete preprint of Caro, Petruševski, and Škrekovski (arXiv:2203.01088v1, March 2022) discusses general bounds, basic classes, and sparse graphs; the inspected body does not give a Möbius-ladder statement or a twisted-transfer trace. The original planar-coloring introduction (Fabrici, Lužar, Rindošová, Soták, arXiv:2202.02570v1) treats a distinct family-level upper-bound problem. Existing exact proper conflict-free prism counts concern **straight** gluing, while Möbius gluing requires an anti-invariant row-swap trace. This comparison evaluates implications, not simply titles or parameter names.

Targeted comparisons against published mathematical records, equivalent terminology, graph tables and direct primary-paper searches found no covering Möbius enumerator or lower-bound theorem. This is best-knowledge originality, not a claim of exhaustive historical priority. The full text of the 2026 list-coloring paper was inaccessible, although its publicly stated theorems were read. No negative whole-document claim is made about that manuscript.

## Mathematical value — PASS

A Möbius ladder is a canonical infinite family of cubic graphs, and the tension between local neighborhood-color constraints and global twisted closure is mathematically natural. The result determines the exact minimum palette and the **entire named-optimal-coloring count at every length** by an explicit rational generating function; it also identifies a simple spectral correction between twisted and straight gluing. The correction can be zero at a nontrivial width despite an infinite-family obstruction to three colors, providing a structural distinction invisible to the general four-choosability bound. This is an exact classification with a reusable involutive-transfer mechanism rather than a routine case of a known general upper bound.

## Remaining limitations

The count uses labelled vertices and a named palette; no quotient by automorphisms or all-palette chromatic polynomial is claimed. A full independent audit and definitive bibliographic priority assessment have not been performed.

Self-review: passed. Independent audit: not yet performed.
