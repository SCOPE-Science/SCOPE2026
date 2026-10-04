# Same-model review

## Correctness
PASS. For fixed \(\alpha>0\), all primes in \((\alpha n,\beta n]\) exceed \(\sqrt n\) once \(n>\alpha^{-2}\), so Legendre's formula becomes exactly \(v_p(n!)=\lfloor n/p\rfloor\). The cells \(n/(j+1)<p\le n/j\) are disjoint and exhaustive for those primes. Their intersections with the target window have fixed scaled endpoints, and the prime number theorem for \(\vartheta\) gives the stated coefficient after summing finitely many cells. Endpoint conventions are compatible with the open-left, closed-right intervals. The embedded verifier independently recomputes Legendre valuations and checks the cell identity in 250 finite cases.

## Originality
PASS. The closest source, arXiv:2609.37460v1, proves uniform residue mass only for fixed logarithmic power bands at scale \(\log(n!)\asymp n\log n\), explicitly declining uniformity for moving endpoints. A fixed linear window has mass only of order \(n\), so that theorem's error can dominate the entire new boundary term. Searches for linear-window, \(\lfloor n/p\rfloor\)-cell, parity-bias, and harmonic-weight formulations did not locate an equivalent published statement. Older fixed-prime distribution results reverse the quantifiers and do not imply the moving-prime-window law. A residual risk remains because the proof uses classical ingredients and an equivalent elementary corollary may exist under different terminology.

## Value
PASS. The finding identifies the natural boundary regime left unresolved by the new fixed-power-band theorem and gives a complete first-order law on every fixed linear prime window. The exact \(3/5\) versus \(2/5\) parity split on \(n/3<p\le n\) is a motivated counterexample to naive uniform continuation, not an arbitrary slice. The general coefficient shows exactly how the discrepancy depends on the window and residue class.

## Closest literature and limitations
Ma's 2026 theorem is the closest statement and supplies the motivating observable. Luca--Stănică, Berend--Kolesnik, and Liu--Chen concern fixed prime indices as \(n\) varies and therefore do not cover this regime. The present theorem does not quantify simultaneous transitions when the linear window itself changes with \(n\).

Same-model review: passed. Independent audit: not yet performed.
