# Review of the six-cycle positivity boundary

**Correctness (PASS).** The exact completed Gauss map has scalar multiplier \(f(x)=(x^2-6x+12)/(x^2+6x+12)>0\) for nonnegative \(x\). Its \(C_5\) and \(C_6\) distance classes are explicitly reconstructed by rational matrix algebra. At six vertices, all distance classes except nearest neighbors have positive numerators, while the nearest-neighbor quartic has one positive root by Descartes' rule. For each larger cycle, the cycle-resistance pseudoinverse and high-step rational spectral expansion force a negative nearest-neighbor coefficient. A standalone symbolic checker passed; no finite sample is mistaken for the general proof.

**Originality (PASS, subject to remaining literature risk).** The closest known general sources concern RK positivity radii (Horváth 2004/2005), Padé counterexamples on broader positive systems (Zappavigna et al. 2012), invariant-polyhedron conditions (Horváth et al. 2014), and an eight-state *small-step* obstruction (2026). Earlier short-cycle unconditional cases follow known complete-multipartite/strongly-regular graph results and are baseline only. The new statement is the first exact failing cycle \(C_6\), its sharp step polynomial and the complete classification of which unweighted cycle sizes remain positive for all steps. The searched sources do not imply the sharp polynomial; specialized work not reached by the searches remains a risk.

**Value (PASS).** Cycles are a basic periodic-grid semidiscretization; their exact critical size distinguishes spectral stability from positivity of a standard fourth-order A-stable time step. The six-node exact boundary is a usable positive-cone benchmark, while the effective-resistance formula explains why any longer periodic lattice eventually loses positivity. This is a natural infinite-family structural cutoff, not a graph chosen only for a numerical test.

**Limits.** No exact step cutoff is claimed for the cycles of length seven or greater. No assertions concern arbitrary weighted cycles, internal stage sign or numerical roundoff. The self-review cannot replace independent assessment.

Self-review: passed. Independent audit: not yet performed.
