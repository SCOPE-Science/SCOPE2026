# Independent mathematical audit

## correctness

PASS

With signed incidence matrix B and independent fair edge signs z, Q=||Bz||^2/4. Its expectation is |E|/2 and 2(Q-EQ) has one quadratic monomial for each unordered incident edge pair. In a simple host distinct pairs give orthogonal monomials, so the variance is one fourth the wedge count. In the cube an edge sign must occur with even multiplicity: the only surviving triples consist of three distinct monomials forming a triangle on the line graph. The six orderings all have coefficient +1 for three edges at one vertex and -1 for a host triangle, because in the latter case each edge has one incidence sign at each of its endpoints. This gives the third central moment exactly, with no connectedness assumption. For the histogram on a nonempty host of positive common degree, nonadjacent degrees are independent; a shared edge distributes its sole win across the pair and the remaining d-1 signs per vertex are independent. This gives pair covariance -1/4 times the product of the two binomial mass differences, which equal 2(2r-d)p_r/d and 2(2s-d)p_s/d. Combining nd such ordered terms with n same-vertex terms and whitening subtracts the orthogonal constant and binomial-linear directions from the identity; d=1 gives the zero projection. The dispersion formulas also hold on an empty graph, where whitening is not defined. Independent orientation enumeration checked the triangle and claw (opposite cubic signs), a matching, the prism and K_{3,3}, including regular histogram ranks and every covariance entry for the tested regular hosts (python3 /workspace/review-checks.py, orientation section).

## originality

PASS

The supported distinct result is the exact signed star-versus-triangle identity for the cubic dispersion moment on arbitrary fixed simple hosts and its use to recover triangle counts that second-order regular score data cannot distinguish. First and second moments use classical sign orthogonality and are not asserted to be new general moment methods. The histogram half has a direct published tournament precursor and its extension to regular graphs follows routinely from the already published pair calculation and independence of nonadjacent vertices; it is not credited as standalone originality. The close prior angular-width result recovers triangles from a different random observable and does not yield this identity.

## value

PASS

The centered squared score is a natural measure of dispersion of random orientation data. The exact cubic dependence recovers a host subgraph count from the statistic once degrees are known, even for disconnected simple hosts; regular hosts such as the triangular prism and K_{3,3} have entire second-order histograms indistinguishable in the covariance sense but distinct third dispersions. This supplies a concrete information threshold, not just a generic chaos expansion or a finite table. It does not identify the entire orientation-score law or remove the need for known degrees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
