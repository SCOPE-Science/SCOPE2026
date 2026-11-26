# Independent mathematical audit

## correctness

PASS

The four cyclic server states retain service on a scored rally; summing non-scoring faults gives (8,4,2,1)/15. From deuce the difference chain absorbs almost surely (two same-side scored points in a fixed direction have positive probability, uniformly over states). I independently solved the rally-level deuce equations, obtaining (30/43,45/86,13/43,41/86) at zero difference, and evaluated targets 2 through 21 by eliminating the four cyclic rally equations at each score; all match (replay independent_checks.py 2). For the infinite identity, right multiplication checks the printed Green-row difference. Its A-next-point and deuce weights give (1−y)H and (11x−32y+10)H/43. All monotone histories inside the square of scores ≤n−1 are nonterminal; summing the first weight on the A-winning edge telescopes, and the deuce corner gets the second weight. For m=n−1, symmetry and (5−2x−2y+xy)H=1 yield f_n=(75c_m,m+11c_{m−1,m−1})/86. The diagonal constant term is ((5+z)^2−16z)^(−1/2), so c_j,j=5^(−j−1)P_j(3/5); this also covers n=2. For the asymptotic, cos(θ/2)=2/√5, sin(θ/2)=1/√5; the weighted adjacent cosines have coefficients 260/√5 and −20/√5, i.e. amplitude 20√34 and phase shift arctan(1/13). The fixed-angle error after common scaling is O(1/n). A rational θ/π would make 6/5 a rational algebraic integer, so the phases are dense and give the stated sharp positive and negative limits. This proves both signs infinitely often, not strict alternation at consecutive targets. The conclusion uses only the stated uncapped, fair independent-rally doubles model.

## originality

PASS

The underlying model, general finite matrix calculation, and opposite signs for targets 11 and 15 are established. The independent overlap review supports the distinct target-uniform Legendre reduction and sharp infinite oscillation, not those earlier results or the classical polynomial identities.

## value

PASS

A natural symmetric limit of the actual gameplay model already exhibits a puzzle at common targets. The exact identity exposes orthogonal-polynomial structure, explains why either first-serve sign keeps recurring, and gives the sharp magnitude; this is more than recomputing the two well-known targets and does not exaggerate the practical size of the effect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
