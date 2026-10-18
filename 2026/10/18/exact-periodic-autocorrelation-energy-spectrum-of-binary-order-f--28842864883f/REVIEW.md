# Scientific review: periodic autocorrelation-energy spectrum

## Correctness — PASS

The finite domain is exactly the 2,048 cyclic binary de Bruijn sequences of order five. A unique 5-bit edge anchors each cycle. Every cyclic Euler tour defines one of the two incoming-to-outgoing edge matchings at each of 16 graph vertices, and conversely a matching whose successor permutation is one 32-cycle defines one Euler tour. Thus the 65,536-mask enumeration is exhaustive rather than a sample. Direct integer correlation sums reproduce the displayed full distribution of 47 values, with extremal counts 12 and four. An independent edge-avoiding Euler-tour depth-first enumeration returns precisely the same 2,048 words and the same histogram. Reversal/complementation orbit counts, exact mean and variance, and the divisible-by-32 lemma were checked. The energy is periodic, includes all nonzero shifts, and uses bipolar symbols.

## Originality — PASS, with limits

Spinsante--Andrenacci--Gambi (2011, doi:10.1186/1687-1499-2011-4) already exhaust all 2,048 cycles and publish RMS averages and peak-sidelobe threshold counts; no part of that earlier work is claimed as new. Table 3 supplies three aggregate RMS values and two threshold cardinalities, not the 47 exact **individual-energy** multiplicities or the sharp maximum-energy multiplicity and symmetry class. Our per-cycle normalized RMS equals \(\sqrt{E/31}/32\), so this is a substantive refinement in a precisely equivalent invariant. Fujisaki--Nabeshima (2011, doi:10.1587/nolta.2.400) address individual worst correlation values, and Spinsante--Warty--Gambi (2013, doi:10.1109/AERO.2013.6496833) display overlaid correlation traces, rather than an exact energy multiplicity table. Gabrić--Sawada (2018, arXiv:1803.09009) provide construction results, and Mandal--Gong (2020, doi:10.3934/amc.2020125) analyze filtered outputs. Searches for equivalent periodic-sidelobe energy and Fourier-fourth-moment enumerations did not uncover stronger published coverage. An unindexed exact tabulation remains possible; searches do not certify global priority.

## Mathematical value — PASS

Periodic total squared sidelobe energy is a natural rotation-invariant spectral-flatness statistic, complementary to the peak-correlation thresholds used when selecting shift-register/spreading sequences. The exact finite spectrum covers every order-five cycle rather than arbitrary slices. It resolves an unknown constrained full distribution, including the highest-energy orbit and nine missing attainable-grid values, and quantifies variance within a family for which only averages and peak thresholds were previously displayed. It is useful precisely because sequences with the same peak threshold can have very different accumulated sidelobe energy. The finite classification does not assert general-order behavior or physical-channel superiority.

## Independent review status

Self-review: passed. Independent audit: not yet performed.
