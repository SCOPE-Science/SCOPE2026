# Scientific review: sharp negative-type thresholds of uniformly whiskered cliques

## Correctness — PASS

The domain is all integers \(n\ge3\), \(r\ge1\), with unweighted shortest-path metric. Every distance in the matrix is explicitly classified and the mean-zero decomposition accounts for all \(n(r+1)-1\) degrees of freedom: \(n(r-1)\) leaf contrasts, \(2(n-1)\) standard coordinates, and one constant-mode line. The central scalar function crosses zero once, and a strictly concave comparison proves that the standard determinant remains positive at this first crossing. All equality directions, the Hilbert Gram rank and the monotonic/asymptotic statements follow from these verified analytic steps. Direct graph-distance reconstruction and matrix diagonalization in `check_corona.py` passed 1180 supplementary assertions. The finite checks do not certify the infinite parameter range; the written analytic proof covers it.

## Originality — PASS, subject to historical priority

The precise shared object at one leaf per parent was inspected in Baskoro–Obata, *Determining Finite Connected Graphs Along the Quadratic Embedding Constants of Paths*, arXiv:1904.08059, §4.5 (first public 2019-04-17). Its theorem is about the \(p=1\) quadratic embedding constant, already known and explicitly excluded from the novelty claim. Choudhury–Nandi, arXiv:2306.15589, Theorem 1.7 and §4, covers the ordinary QEC of uniform star clusters; Ferdi–Baskoro–Obata–Santika, arXiv:2512.17258, §4.4 and Examples 5.1–5.3, covers corona QEC at the unpowered distance. Their formulas do not directly cover \(d^p\) for variable \(p\), whose distances two and three become independent nonlinear quantities \(2^p\) and \(3^p\). Sánchez, arXiv:1108.0451, §§2–3, supplies the general finite determinant method, without the present all-parameter crossing dominance. Robertson, arXiv:2309.16070, Theorem 1.2 and §4, supplies the negative-type embedding foundation and different graph examples. The closest accessible prior local mathematical record on clique coronas concerns the general-position polynomial, not powered-distance negative type. A separate earlier double-star threshold covers \(n=2\), which is deliberately excluded.

The new contribution is the exact powered-distance threshold for all \(n\ge3\), \(r\ge1\), its unique global critical load, strict parameter monotonicity, both boundary asymptotics, and the contrast with the known \(p=1\) QEC. Sources may use alternate terminology such as generalized roundness or hypermetric thresholds; undetected equivalent historical coverage remains a genuine risk, not an established absence.

## Mathematical value — PASS

This is a natural complete two-parameter classification of the first failure of Hilbert embeddability for uniformly pendant-extended cliques. The unmodified clique has arbitrarily large negative-type exponent, while adding one private leaf to every vertex creates a sharp finite bound. The classification identifies its entire critical equality space and affine-dimension loss, and proves strict deterioration as either the number of core vertices or the pendant multiplicity increases. The particularly motivated invariant separation is that the ordinary quadratic embedding constant remains fixed along growing clique cores, but their supremal negative-type exponent does not. Neither a general theorem downstream nor a new value of ordinary QEC is claimed.

## Limitations and literature risk

Weighted and nonuniform corona graphs are not classified. The two-vertex-core double-star family is not claimed. Independent mathematical examination is needed to exclude equivalent historical results under generalized roundness or related distance-kernel classifications. Numerical assertions test only a finite parameter grid.

Self-review: passed. Independent audit: not yet performed.
