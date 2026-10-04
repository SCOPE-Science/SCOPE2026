# Review

## Correctness

PASS. Because the BML modal preorder contains the finite chain order, it is automatically a total preorder. Its mutual-accessibility classes must be intervals: if two endpoints of a chain interval are equivalent, transitivity together with the included chain edges makes every point between them equivalent as well. Conversely, every contiguous block partition defines a preorder containing the chain.

The adjacent cut/tie choices therefore give exactly \(2^{n-1}\) relations. If \(\ell(d)\) is the least point in \(d\)'s modal-equivalence block, then \(d\sqsubseteq e\) holds exactly when \(\ell(d)\le e\). Substituting this into the primary source's bounded-modal clause gives the suffix beginning at \(\max(\ell(d),\rho(\gamma))\). Exhaustive replay through six scopes agrees exactly.

## Originality

PASS. The primary 2026 BML paper gives the general preorder/stability definition and bounded-modal semantics but does not study finite chain scope structures. Searches of the published-finding database and public literature did not locate a BML chain census, adjacent-cut normal form, or suffix semantics theorem.

The order-theoretic statement that total preorders decompose into ordered equivalence classes is standard and is not claimed as new. The new claim is the precise BML specialization: stability over a fixed chain forces interval classes, gives exactly \(2^{n-1}\) BML modal structures, and collapses every bounded-modal successor set to one suffix.

## Value

PASS. BML is motivated by explicit dependencies between lexical scopes in multi-stage programs, and linearly nested scopes are a canonical special case. The theorem turns the modal component of every finite chain instance from an arbitrary binary relation into an exact \(n-1\)-bit object. It also makes every bounded-modal accessibility query a single suffix threshold, providing a natural normal form for finite chain experiments and implementations.

## Closest literature and limitations

Murase--Maniwa (2026), Definition 2.1 and the Kripke semantic clause in Definition 4.1, are the direct source. General order theory supplies the background terminology of total preorders and equivalence classes.

The theorem does not extend the \(2^{n-1}\) count to non-chain scope orders and does not establish a decision-complexity theorem.

Same-model review: passed. Independent audit: not yet performed.
