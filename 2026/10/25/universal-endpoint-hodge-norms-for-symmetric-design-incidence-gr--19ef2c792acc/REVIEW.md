# Scientific review: symmetric-design incidence projection norms

## Correctness

**PASS.** The incidence equations are explicitly solved using the symmetric-design identity \(MM^{\mathsf T}=(k-\lambda)I+\lambda J\). All seven edge types have independently checkable multiplicities and voltage differences. The assumptions give a strict sign for each class, so the absolute-sum formula is exact. The complementary projection is obtained from the diagonal effective resistance rather than by assuming that the two projections have equal norms. A standalone exact-rational grounded-Laplacian calculation recomputes every edge column on four nontrivial designs (\(346\) columns total). The proof applies to every existing design in the stated parameter range; the finite tests are corroboration, not an infinite proof.

## Originality

**PASS, with residual bibliographic risk.** The closest inspected operator-theory source is Dilworth–Kutzarova–Ostrovskii, arXiv:2305.12582, whose targeted sections treat Hamming graphs and discrete tori rather than symmetric-design incidence graphs. Shramchenko–Shramchenko, arXiv:2312.03937, gives incidence-matrix spectral tools but no identified absolute-current endpoint norm theorem. General electrical localization bounds do not determine the rational equalities here. The symmetric-design formula is not obtained merely by specializing the known formulas for projective-plane incidence graphs, crown graphs, or general \(3\)-designs: the central range has \(\lambda\ge2\), \(\lambda\le k-2\), and includes a \(2\)-\((11,5,2)\) design that cannot be a \(3\)-design (its required triple multiplicity would be \(2/3\)). The possibility of an equivalent result in specialized graph-resistance literature cannot be eliminated by searching.

## Mathematical value

**PASS.** The incidence graphs of symmetric \(2\)-designs form a natural, potentially non-flag-transitive class of bipartite distance-regular graphs. Exact endpoint projection norms are legitimate Banach operator invariants and measure total absolute electrical-current response; neither their values nor constancy of every column follows from the effective-resistance diagonal alone. A complete parameter-only classification covers biplanes, point–hyperplane designs, their complements and nonisomorphic designs with the same parameters, while resolving the ordering of the two complementary norms. The exact self-contained result remains useful without any claim of optimality among nonorthogonal projections.

## Closest literature and limitations

- Dilworth, Kutzarova and Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582: motivating projection theory, different enumerated graph families.
- Shramchenko and Shramchenko, *Mutual incidence matrix of two balanced incomplete block designs*, arXiv:2312.03937: matrix spectra, no matching absolute-current statement in the inspected material.
- Bailey, *On the metric dimension of incidence graphs*, arXiv:1707.02899: same graph objects but a distinct invariant.
- Schild, Rao and Srivastava, *Localization of Electrical Flows*, arXiv:1708.01632: general bounds rather than the exact rational formulas.

The formulas are for real, unweighted graphs and canonical Euclidean-orthogonal projections; the existence of designs with arbitrary formally admissible parameters is not claimed. Residual bibliographic uncertainty and lack of independent mathematical review remain.

Self-review: passed. Independent audit: not yet performed.
