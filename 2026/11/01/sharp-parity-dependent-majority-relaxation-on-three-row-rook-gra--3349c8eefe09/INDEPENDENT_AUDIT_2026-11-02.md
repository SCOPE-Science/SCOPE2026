# Independent mathematical audit

## correctness

PASS

PASS: The proof exactly reduces every labelled 3n-vertex state on K3□Kn (tie retention) to eight original column types and three row totals; the multinomial formula counts all labelled states with no duplication. I read scripts/verify_symbolic.py and both source SMT constraints and independently regenerated both complete unbounded QF_LIA counterexample formulas, byte lengths 79,340 (odd) and 94,484 (even), checked them through the installed libz3 interface and obtained UNSAT twice (≈0.66s and 3.24s). The formulas quantify arbitrary k≥1 and arbitrary integer type multiplicities; unlike finite samples, unsatisfiability with a sound integer solver proves F^5=F^3 for all odd n≥3 and F^6=F^4 for even n≥2. Parameterized three-type trajectories realize first-entry times 3 and 4 respectively, with separate exact n=2,4 counts. I checked the witnesses for several parameter values. Limits: solver soundness and encoding inspection, not a handwritten elimination proof.

## originality

PASS

PASS (best of knowledge): Goles–Olivos proves eventual period≤2 but no size-independent sharp first-entry bound; Kaaser–Mallmann-Trenn–Natale give general graph/module voting-time upper bounds, and Benjamini et al study general/unimodular/random networks. The two-row K2□Kn cousin is not the three-row eight-type dynamics. Direct implication search returned no source specifying parity-dependent sharp times 3/4 and all-layer multinomial profile census for K3□Kn.

## value

PASS

PASS: The fixed natural graph family K3□Kn grows unboundedly while its entire synchronous majority transient has an exact size-independent parity jump, and the polynomial-size frequency sum determines all first-entry and period layers. Uniform quantified dynamics plus sharp witnesses is substantially more informative than eventual period-two folklore or a tiny graph census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
