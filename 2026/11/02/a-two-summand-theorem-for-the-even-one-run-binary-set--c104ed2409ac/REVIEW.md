# Scientific review

**Correctness — PASS.** The proof constructs digitwise binary-addition transitions between eight possible states, tracking parity of the open one-runs and carry. The determinized automaton paired with the residue and position-parity tracker has exactly ten reachable states, whose transitions are displayed in the proof. Every reachable state accepts exactly when its residue is zero, which proves the statement for unbounded input lengths. The standalone checker recomputes this complete finite certificate without assuming its conclusion and separately tests all targets below 16384. Boundaries at zero, nonzero carry, and closing odd one-runs are included.

**Originality — PASS within inspected sources.** Rampersad–Wiebe's Theorem 20 describes the relevant zero-one sequence, not the sumset of its support. Bell–Hare–Shallit provide generic algorithms for additive bases of automatic sets, and discuss other sets explicitly, but do not give this particular exact order-two equality. Chen–Wang's binary criterion uses parity of the total zero count rather than even lengths of one-runs. The exact sumset and sharp order were compared against relevant research search records, alternate descriptions and published work. A possible unindexed prior implementation of the general algorithms remains a genuine risk; priority is not certified.

**Value — PASS.** The result determines a natural exact additive invariant of a recently characterized automatic number-theoretic set: its twofold sumset is precisely one full congruence class lattice, despite the underlying support being sparse. The statement gives a sharp additive-basis order on the scaled support rather than mere decidability, eventual basis status or finite computational evidence. The ten-state certificate gives a reusable method for binary carry-constrained additive questions.

**Scientific limits.** Two summands may include zero; uniqueness, representation counts and the generalized one-run divisibility family are not determined. The priority comparison does not replace independent verification or a complete historical bibliography.

Self-review: passed. Independent audit: not yet performed.
