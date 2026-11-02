# Scientific review

## Correctness (C) — PASS

The local update can only stay or advance by one color, forcing binary stripe increments. For horizontal stripes, exactly three neighbors carry the next color precisely at a unit increment; this yields the complete edge shift at thresholds at most three and only constant words otherwise. For diagonal stripes, the Moore offset multiplicities give the exact predecessor-count identity \(2b_i+(b_i\oplus b_{i+1})+b_{i-2}b_{i-1}\). Its finite-type graph determines all traveling diagonal words and the four characteristic-polynomial regimes. The finite integer determinant checks agree with this direct derivation. The entropy is taken on **the invariant stripe wave subsystem**, not on the whole two-dimensional automaton. The axial finite-word formula and exact zeta function follow from a primitive three-state adjacency matrix.

## Originality (O) — PASS under documented priority risk

The relevant full-text sources were compared by their mathematical implications, not by title. Fisch, Gravner, and Griffeath already establish horizontal band-wave propagation up to the threshold three, and Urías et al. already give a general finite-automaton method for traveling configurations and topological entropy. Neither inspected source states the complete orientation comparison, the diagonal threshold-two quartic Perron entropy, the threshold-three golden-mean value, or the simultaneous exact axial orbit counts for this Moore rule. Sharipov et al. analyze different, reversible three-state brickwork rules and explicitly identify entropy as a desired dynamical diagnostic. Muñoz and Nuño (2026, arXiv:2610.37990; October 27 public posting) examine the very same three-color Moore rule and report typical attracting three-band waves, but their inspected model section, traveling-wave section, and parameter sweeps do not classify the whole (possibly nonattracting) infinite stripe-wave subshifts or compute their entropy. A general transducer algorithm is a significant broad precedent; specialized earlier calculations could still cover the new constants. The manuscript does not claim invention of the traveling-SFT method or the axial cutoff.

## Value (V) — PASS

The precise question is whether the same local threshold sustains exponentially many **rigidly moving** bands in distinct lattice orientations. The result proves a qualitative orientation obstruction at threshold one and two different positive entropy values at thresholds two and three, as well as a complete sharp cutoff and finite-orbit formula. This makes exact the wave-family diversity hidden by the familiar single-band propagation criterion. It provides an explicit 2D-to-SFT reduction and a natural finite-size census for the cyclic excitable-medium model, while carefully limiting the claims to stripe subsystems.

## Closest literature and limitations

Sharipov et al., arXiv:2503.16593 (full parsed HTML, especially models and outlook); Fisch, Gravner, Griffeath (1991; open PDF, band thresholds and model); Urías et al. (1996; author-uploaded full text, introduction and transducer construction); Muñoz and Nuño (2026, arXiv:2610.37990; full parsed HTML, model and observed traveling waves). General finite-state enumeration predates this calculation; no claim is made of novelty of that general approach. Finite checks of widths 3–8 cannot establish infinite entropy, and a relevant earlier application that was not indexed might supersede the explicit results. No independent expert evaluation was performed.

Self-review: passed. Independent audit: not yet performed.
