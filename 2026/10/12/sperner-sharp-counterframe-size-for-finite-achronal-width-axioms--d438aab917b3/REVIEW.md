# Review

## Correctness
The source's frame correspondence turns failure of \(U_n\) at a world \(x\) into \(n+1\) successors whose future sets are pairwise incomparable under inclusion. In a transitive frame, every future of a successor of \(x\) is again a successor of \(x\). Achronicity also forces the \(n+1\) offending successors themselves to be pairwise inaccessible, so none lies in another's future. The future sets are therefore an antichain of subsets of the remaining successors of \(x\). Sperner's theorem gives the exact lower bound on the number of those remaining worlds. The matching construction takes \(n+1\) central-layer subsets of a \(q_n\)-element set and realizes them as future sets; its only two-step paths are explicitly closed, so it is an irreflexive transitive frame.

The inverse-central-binomial asymptotic is standard: \(\binom{q}{\lfloor q/2\rfloor}=\Theta(2^q/\sqrt q)\), and solving for the least threshold \(q\) gives \(q_n=\log_2 n+\tfrac12\log_2\log_2 n+O(1)\).

## Originality
Candidate-specific semantic-database searches used the queries “finite achronal width modal logic strict partial order minimal counterframe Sperner central binomial,” “KU_n strict partial order countermodel minimum size future sets antichain,” and “modal logic achronal set upper cones Sperner theorem counterframe.” They returned adjacent modal-logic and finite-poset findings, but no equivalent minimum-size theorem.

The cumulative current and preceding owned ledgers were searched for achronal width, strict-order counterframes, Sperner thresholds, \(U_n\), and central-binomial minima. No matching result was found. The inspected Goldblatt--Hodkinson paper gives the achronal-width correspondence but does not state the Sperner-sharp finite counterframe minimum.

The residual originality risk is uncatalogued folklore: once the relational characterization is combined with transitivity, the Sperner argument is short.

## Value
The result identifies the exact finite obstruction size for every member of a natural modal axiom hierarchy on strict-order semantics. It shows that forcing \(n+1\) mutually non-nested futures costs only an additional inverse-central-binomial number of worlds and quantifies that overhead as \(\log_2 n+\tfrac12\log_2\log_2 n+O(1)\). This is stronger than a generic finite-model bound because it is exact and attained by an explicit family.

## Closest literature and limitations
The closest source is Goldblatt and Hodkinson's finite-achronal-width paper; Sperner's theorem supplies the extremal set-theoretic ingredient. The proof does not extend unchanged to arbitrary nontransitive frames, and no claim is made about minimum countermodels for arbitrary formulas over the resulting logics.

Self-review: passed. Independent audit: not yet performed.
