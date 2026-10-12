# Review of the exact two-qutrit damping boundary

**Correctness (C): PASS.** Exact multiplication of the source's six matrices gives the diagonal Kraus sum, yielding the sharp equal-rate cutoff \(t\le(\log2)/2\). Exact marginal identities and a \(9\times9\) partial-transpose spectral decomposition establish the trace defect and PPT invariance for the entire claimed parameter range. The rational examples are replayed by `verify.py`. The result distinguishes complex continuation of a CP but trace-increasing map from a physical CPTP channel.

**Originality (O): PASS, with residual risks.** The source displays the six Kraus matrices and reports separable/PPT-to-NPT birth but does not identify the trace-preserving cutoff or quantify the false trace-norm signal. The usual PPT-preservation theorem does imply the qualitative noncreation statement; it does not supply the exact cutoff, trace defect, or source-specific quantitative expression. The 2014 Ali comment addresses a **different** 2012 dynamics, the Ali--Huang 2014 sudden birth occurs between reservoirs, and the 2020 correlated-dephasing study treats a different noise mechanism. An unindexed derivation in a later comment or the inaccessible full 2014 article remains a possibility.

**Value (V): PASS.** This sharp boundary concerns the full named finite-temperature family and the central reported effect in a cited two-qutrit study: the supposed generation of distillable entanglement from initially separable or bound-entangled states. It provides the exact probability-conservation obstruction and a quantitative mechanism for a spurious entanglement diagnostic, not merely a small numerical discrepancy. It does not claim a new general PPT theorem or extend the criticism to globally coupled reservoirs.

**Scientific limitations.** The published plots' implementation is unavailable, so no claim is made to reproduce those plotted values. The complex continuation is CP but not TP beyond the cutoff; physically renormalizing this output leaves a PPT state. No independent audit has occurred.

Self-review: passed. Independent audit: not yet performed.
