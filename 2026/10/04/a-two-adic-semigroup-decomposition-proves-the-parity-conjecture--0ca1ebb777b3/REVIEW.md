# Same-model scientific review

## Correctness
PASS. The stabilization definition is reconstructed exactly: after subtracting the mandatory \(j\) copies of \(1^k\), eventual representability is membership in \(S_k=\langle n^k-1:n\ge2\rangle\). The identity
\[
(2m)^k-1=(m^k-1)+m^k(2^k-1)
\]
reduces all even-base generators to \(A_k=2^k-1\) plus even odd-base generators. This makes membership split exactly by parity as
\[
S_k=2T_k\sqcup(A_k+2T_k).
\]
The auxiliary \(T_k\) is numerical because it contains a coprime pair. The complete even/odd gap classification then gives the Frobenius and genus formulas and their parity consequences. The regression checker reproduces the source table for \(2\le k\le9\), but the infinite theorem does not depend on those computations.

## Originality
PASS. The current primary source, revised 31 March 2025, still states the parity assertion as Conjecture 10.4. The closest published semigroup result already identifies stable exceptions with gaps of \(\langle n^k-1\rangle\), but its indexed claim concerns a different modular-obstruction correction and does not state the new parity decomposition or transfer formulas. A separate published computation handles only \(k=10\). Exact and semantic searches for the conjecture, its semigroup formulation, and the stronger formulas found no general proof. A residual risk remains from unindexed numerical-semigroup work and from the unavailable full text of the closest published semigroup record.

## Value
PASS. This settles a named all-\(k\) conjecture with a short structural theorem, not a finite census. The same argument gives explicit transfer formulas for both the Frobenius number and genus, explaining why the observed parities persist and providing a reusable reduction for further work on the stable obstruction sets.

## Closest literature and limitations
The primary source is Brennan Benfield and Oliver Lippard, “Integers that are not the sum of positive powers,” arXiv:2404.08193. The closest later published results identify the obstruction sets with numerical-semigroup gaps and compute the \(k=10\) case. The present theorem does not settle the source's neighboring conjectures and does not compute \(F(T_k)\) or \(g(T_k)\) in closed form.

Same-model review: passed. Independent audit: not yet performed.
