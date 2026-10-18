# Research assessment: clamped quadratic Greville coefficient recovery

## Correctness — PASS
Cox–de Boor recursion yields the stated boundary and interior tridiagonal rows. Alternating-sign diagonal conjugation turns the collocation matrix into a strictly diagonally dominant nonsingular M-matrix. The row-sum system is solved exactly by the characteristic roots \(3\pm2\sqrt2\), with boundary equations fixing its amplitude. Strict convexity of the row profile localizes all sharp positions. Separate Toeplitz and limit arguments justify the claimed persistent boundary excess. Finite arithmetic checks independently reconstruct the actual B-spline evaluations and all tested inverse entries. Risks: none identified in the claimed algebraic domain; independent proof inspection remains outstanding.

## Originality — PASS within examined evidence
The closest fully inspected source, Novaković–Singer–Singer (2010, arXiv:1004.4014), treats degree-two cardinal matrices with simple knots: symmetric Toeplitz arrays and spectral condition numbers, not the clamped repeated-endpoint matrix and exact \(\ell^\infty\) coefficient norm. De Boor (1975) and Marsden (1983) concern Greville spline interpolation more broadly; only their abstracts and contextual descriptions were accessible, so an implicit equivalent formula in them remains a significant priority risk. A mathematical-record semantic search for equivalent clamped-boundary norm formulas returned no direct implication; absence of a hit is not a uniqueness proof.

## Value — PASS
The coefficient extraction map is a natural stability invariant of Greville spline reconstruction. The theorem supplies a complete sharp bound for all mesh lengths, exact extremal rows and data, a strict finite-size law, and a boundary penalty that survives grid refinement. This distinguishes clamped and pure-cardinal constructions, which share the same interior collocation stencil but have different limiting stability. This is more informative than a generic boundedness estimate; it does not assert a downstream approximation theorem.

## Limitations and priority
The result is restricted to quadratic open uniform knots and coefficient norms. Marsden's 1983 directly relevant interpolation paper was available only at abstract level; an institutional full-text attempt was not completed. Historic equivalence is not excluded. 

Self-review: passed. Independent audit: not yet performed.
