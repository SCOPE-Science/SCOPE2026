# Review of the dicyclic commutative-closure result

## Correctness
PASS. The normal form \(a^k b^e\) and relation \(ba=a^{-1}b\) identify exactly the reachable group products for fixed Parikh counts. The proof classifies all right quotients, including the zero-\(b\) axis and the transition at \(r=m-1\), and supplies a separation argument for all classes. The arithmetic count is \((m-1)+2m+4(m-1)+4=7m-1\). The standalone verifier exercises independent group-product enumeration for \(2\le m\le10\) and tests canonical classes and distinguishability. The finite tests do not certify the infinite formula.

## Originality
PASS, subject to residual research risks. Hoffmann (2020, arXiv:2004.11772) gives a general automaton construction and a nonsharp upper bound for commutative closures of group languages, not the dicyclic family exact state complexity. Hoffmann (2020, arXiv:2008.05420) addresses shuffle expressions; Hoffmann (2021, arXiv:2111.13523) addresses product-form minimal automata. The prior dihedral identity closure cannot supply the dicyclic computation because \(b^2=a^m\) changes both the Parikh language and its right quotients. Exact prior coverage cannot be excluded absolutely; the 2013 foundational article was compared at the abstract level only and was not used to infer noncoverage of its full text.

## Mathematical value
PASS. The new exact family and its quotient classification show how a nontrivial central group extension generates a length threshold in commutative-closure state complexity. The result is not a finite parameter table: the proof handles every \(m\ge2\), quantifies the blow-up relative to the group language, and produces an explicit minimal-state representation that is much smaller than the general operation bound.

## Closest literature and limitations
The closest reviewed work is Hoffmann's *State Complexity Bounds for the Commutative Closure of Group Languages*, arXiv:2004.11772. The result is for the standard positive-generator alphabet only; no claim is made for arbitrary presentations or generating sets. The search cannot establish publication uniqueness, and the finite verification cannot replace the uniform proof. Independent external review has not occurred.

Self-review: passed. Independent audit: not yet performed.
