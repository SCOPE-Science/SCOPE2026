# Scientific review

## Correctness — PASS

The row recurrence realizes vertical translation by \(1+T\) on cyclic seed rows. The square-periodic subspace is the annihilator of \((1+t)^n-1\) in \(\mathbb F_2[t]/(t^n-1)\), with generator \((t^n-1)/\gcd(t^n-1,(1+t)^n-1)\) and dimension \(d_n\). Every cyclic code of dimension \(d\) has its first \(d\) consecutive coordinates as an information set: the shifted generator basis is lower triangular with ones on the diagonal, and cyclic symmetry covers any consecutive window. The rectangle's bottom row and successive right-edge coordinates give a triangular coordinate transformation of its \(w+h-1\) free data. Combining these proves rank \(\min(d_n,w+h-1)\), correct image and fiber counts, and the extension threshold even for rectangles exceeding the period. Frobenius factorization and Lucas parity establish the arithmetic bound with equality if and only if the odd part of \(n\) is a Mersenne number. Finite exact computations test examples independently; no finite experiment is used as an infinite proof.

## Originality — PASS under examined evidence

Miles–Ward (arXiv:1504.04973), Ledrappier example, previously obtain the Mersenne-period point count, so this component is explicitly attributed. Salo (arXiv:2603.16591v1) gives structural consequences of dense totally periodic points, not the sharp local rectangle restriction rank. Salo (arXiv:2504.11071) treats periodic point density in unishifts, not the all-\(n\) rank profile; Kari–Moutot (arXiv:1806.07107) concern low-complexity periodicity, not local extension counts. The closest published and database records examined do not state the jointly sharp \((n,w,h)\) profile, pattern fraction, or all-\(n\) arithmetic extremality. Database ranking alone does not prove novelty. Residual risks include historical cyclic-code information-set formulations, older algebraic \(\mathbb Z^2\)-actions, and works on multidimensional pattern extension not retrieved in this examination.

## Mathematical value — PASS

The exact image-size theorem answers a natural dynamical reconstruction question: what fraction of legal local patches can be imposed inside a finite-period torus, and at what precise perimeter does universal extension fail? It produces a complete three-parameter finite-index restriction profile, not only a periodic-point census. The Mersenne versus power-of-two dichotomy makes the obstruction concrete and gives explicit cofinal periods admitting every fixed patch, a quantitative refinement of periodic-density mechanisms. The polynomial gcd computes the threshold efficiently for any proposed period. Its scope is intentionally limited to the canonical Ledrappier shift; no stronger universality is asserted.

## Closest literature and limits

The Mersenne-period cardinality and the general cyclic-algebra method have precedents (Miles–Ward 2015). There may be uncatalogued equivalent cyclic-code formulations of the local information-set statement. No independence or historical-priority certification is claimed.

Self-review: passed. Independent audit: not yet performed.
