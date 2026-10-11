# Independent mathematical audit

## correctness

PASS

For every nonterminal cleanup pass the candidate set strictly shrinks and the terminal set has size \(K\), so pass sizes are bounded by \(N,N-1,\ldots,K\). For \(K=1\), the maintained threshold lower-bound invariant forces reset to the unique active coordinate when it is encountered, so cleanup starts from a singleton. For \(K\ge2\), the stated rational recurrence has positive decreasing threshold increments and orders the prefix values so that exactly one prefix entry is removed per pass before the final \(K\)-element terminal pass. Independent exact-rational replay on boundary and interior \(N,K\) pairs reproduced the claimed pass-size sequence and count. The finite bundled verifier is corroborative, not the universal proof.

## originality

PASS

The final support-sensitive complexity statement is not stated in Condat or the later weighted dynamic-threshold paper. Condat gives the removal-loop invariant and quadratic worst case, while Liu–Xie–Yang analyze reset/removal dynamics, construct quadratic families, and prove a gap condition for long bounded-deletion phases. Neither source gives the sharp final-support-conditioned maximum \(\sum_{s=K}^{N}s\), the singleton-support collapse, or equality for every \(2\le K\le N\).

## value

PASS

The exact support-conditioned maximum is a natural algorithmic complexity invariant: it refines a known quadratic worst case, exposes a genuine \(K=1\) structural discontinuity, and supplies sharp examples for every final support size rather than a single adversary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
