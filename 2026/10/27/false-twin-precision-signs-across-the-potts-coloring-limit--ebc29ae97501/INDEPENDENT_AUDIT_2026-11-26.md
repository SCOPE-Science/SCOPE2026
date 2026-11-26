# Independent mathematical audit

## correctness

PASS

The covariance has full affine support: the all-zero indicator and each coordinate indicator occur, using full support at w>0 or a proper (q−1)-coloring with one vertex recolored to color 1 at w=0. Conditioning on the full colors off the twins makes the twin indicators iid Bernoulli(p). Removing the linear projection onto the observed indicators leaves diagonal S+R and off-diagonal R, with S=E[p(1−p)]>0 and R the squared projection residual. At w=0 the proper (q−1)-coloring supplies a conditioning assignment with color 1 and at least one other color available at the twins. Inverting this Schur block gives −R/[S(S+2R)]; this also works with no conditioning coordinates, using projection onto constants. At positive w the two same-indicator assignments differ in denominators by (w−1)(w^(d−1)−1), nonzero exactly in the range needed for strictness when d≥2; the d≤1 and w=1 cases are affine. At w=0 a clique gives an affine indicator formula because its d colors are distinct. With q≥max(3,|V|), two extendable proper assignments avoiding color 1, one injective and the other identifying a nonedge in N, give different p at identical indicators, proving the converse. No converse is asserted for all smaller admissible palettes. The reported 588 exact cases supplement the general proof; the supplied script was inspected, not executed.

## originality

PASS

The full false-twin sign and zero classification across the Potts-to-coloring limit is distinct from the inspected cycle special case, generic residual algebra, and coloring influence results. Only the graph- and palette-specific result, not the general Schur-complement identity, is credited.

## value

PASS

The theorem gives an exact structural criterion for absence versus presence of a linear partial association even though the two vertices are independent given the full other spins. It exhibits a genuine change in the precision zero pattern at the proper-coloring limit, not a rephrasing of graphical separation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
