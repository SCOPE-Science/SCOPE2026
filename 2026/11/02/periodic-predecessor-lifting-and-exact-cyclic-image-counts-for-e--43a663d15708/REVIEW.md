# Scientific review

## Correctness — PASS
Rule 126 is independently verified directly from its neighborhood table. The XOR boundary construction proves the necessary and sufficient even-parity criterion for a length-\(n\) predecessor, including degenerate rings. Forced boundary bits between target zero-runs give the exact run-length parity obstruction; the integrability of every even-weight boundary word constructs a predecessor. For failed cases the forced odd-parity pattern repeats to even parity exactly on even period multiples. A four-state finite-type adjacency matrix proves the `010`-avoidance count; a cyclic rooted-block generating function and its parity-signed counterpart prove the exact obstruction count. Their algebra yields the rational generating function and asymptotic. The standalone independently coded checker returned `VERIFY_OK` after complete input/output enumeration for \(n\le18\), and independent signed-class enumeration for \(n\le15\). Finite checks support but do not replace the general proof.

## Originality — PASS (with historical risk)
The earlier Rule-126 literature explicitly knows the forbidden word `010`, has de Bruijn diagrams, and tabulates periodic basins. OEIS A269173 knows the bitwise local XOR/OR identity, so it is excluded from the priority claim. Actual published-finding corpus searches for Rule 126's periodic images, gap-parity obstructions, exact counting sequences and equivalent expressions found no statement of this periodic-lifting and image-enumeration theorem. Inspected public sources did not show the all-length parity criterion and exact rational count; however, the McIntosh monograph's full text was not accessible, and an unindexed earlier proof cannot be excluded. A 2010 journal date is not used as an invented first-public day: the verified public arXiv posting is 2012-12-01.

## Value — PASS
The distinction between a locally permissible image and a same-period reachable state is a natural issue in symbolic cellular automata and finite-period inverse dynamics. The result provides a sharp parity obstruction, a minimal period-doubling remedy, an infinite obstruction family, and an exact all-length image census plus entropy-growth asymptotics. This is stronger and conceptually more informative than a finite table or a restatement of the known `010` exclusion.

## Closest literature and scientific limits
Martínez et al. (2010; arXiv:1212.0124v1), in particular Sections 2.2–2.3, give Rule-126 periodic basins through length 18 and de Bruijn machinery, and attribute the `010` Garden-of-Eden factor to McIntosh (2009). OEIS A269173 gives the local bitwise formula. The present statement excludes both already-known ingredients from its novelty claim. The full text of the McIntosh monograph was unavailable for inspection, so some historical overlap remains possible; the present theorem concerns one synchronous step on indexed binary rings only.

Self-review: passed. Independent audit: not yet performed.
