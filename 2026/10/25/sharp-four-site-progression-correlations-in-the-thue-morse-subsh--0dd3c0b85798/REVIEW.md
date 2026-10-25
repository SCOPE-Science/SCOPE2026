# Scientific review: sharp four-site Thue–Morse progression correlations

## Correctness — PASS

The correlation is an invariant-measure expectation on the uniquely ergodic binary substitution subshift. Its even/odd decomposition has been independently reconstructed from \(t_{2j}=t_j\) and \(t_{2j+1}=-t_j\). The two-point base \(\eta_2(1)=-1/3\) and the four-site base \(C(1)=1/3\) follow directly. Eight explicit renormalization rows close on the stated family; each output is a signed average of two parent entries, so every coordinate remains in \([-1/3,1/3]\). The equality characterization is not inferred from finite lag sampling: the six reachable saturation types are completely enumerated by a closed transition table, and their first coordinate is saturated only along repeated doubling from lag one. The actual standalone `verify.py` reproduces the finite transition certificate exactly and checks 10,000 further rational lag values. It also conducts 35 independent finite-block comparisons, which are corroborative only.

## Originality — PASS under inspected sources

The four-point renormalization is established by Ong (arXiv:2209.11162, Proposition 2.6), and its arbitrary-order generalization by Baake and Coons (arXiv:2209.07102, Proposition 4.1 and Corollary 4.5). Both papers explicitly make the underlying coefficients computable. The inspected sections do not give the global sharp bound and **if-and-only-if dyadic extremizer classification on the four-term arithmetic-progression slice**, which is the only claimed incremental contribution. Baake, Gähler and Grimm (arXiv:1201.1423) supply the earlier Thue–Morse dynamical setting. The result is not an assertion that four-point correlations, their recurrence, or the ambient subshift are new. A prior unlocated specialization or implicit equivalence remains possible; historical priority has not been independently audited.

## Mathematical value — PASS

The first odd-order balanced correlation vanishes, making a four-site observable a natural next-order temporal diagnostic. The equal-spacing restriction is not an arbitrary parameter substitution: it probes exact arithmetic resonances across dyadic observation scales. A sharp global upper bound alone would not identify those resonances; the complete equality classification establishes that only powers of two maximize absolute dependence. The six-state saturation mechanism provides a structural dynamical explanation rather than a numerical table of selected lags.

## Literature comparison and limitations

Relevant inspected open full texts: Baake–Gähler–Grimm (2012), classical Thue–Morse system and two-point spectra; Baake–Coons (2022), all-order recursion and corner determination; Ong (2022), four-point recurrence and correlation visualizations. The new theorem may be derivable from those recursions after nontrivial additional analysis. It does not address general non-equally-spaced quadruples or other substitutions. Remaining originality risk: inaccessible or unindexed explicit specializations of the classical recurrence. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
