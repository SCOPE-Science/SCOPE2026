# Independent mathematical audit

## correctness

PASS

With constant mass w_e=rho_e*length_e on each edge and the orthogonal edge basis q0=1-7x/2+5x^2/2, q1=-3x/2+5x^2/2, b=4x(1-x), exact local integration gives nodal Gram H=(3D-A)/24, bubble norm 8/15, inverse 8 sum 3^-j T^j D^-1 strictly positive on a connected graph, and vertex row normalization sum d_u(H^-1)_vu=12. Since integral |q_i|=79/300, each vertex evaluation kernel has L1 norm strictly below 12*79/300=79/25; the interior kernel identity plus explicit two-region shape-function envelope is also strictly below. On Q_d, radial random-walk moments bound sum_edges min(a_u,a_w)<=6/d, yielding norm >=79/25-158/(25d), proving optimal unattained constant. Because K integrates to 1, the maximal negative excursion for 0<=f<=1 equals (norm-1)/2 and tends to 27/25. Independent rational Gram/integral and single-edge kernel checks corroborated the proof. Strict finite-graph supremum and hypercube limiting sharpness have separate arguments.

## originality

PASS

Classical interval spline stability, discrete quadrature spline projections, and 2D triangulation counterexamples are strong antecedents. The inspected relevant primary work does not give this exact 79/25 constant for quadratic continuous metric-graph spaces, nor its hypercube limiting sharpness or 27/25 positivity defect. This is a qualified O pass with specialist finite-element literature risk.

## value

PASS

The sharp uniform max-norm and positivity-defect constants for edgewise-quadratic orthogonal projection on arbitrary weighted finite metric graphs address stability of a natural finite-element/spline projection under unrestricted branching and degrees. An explicit extremizing topology sequence supplies genuine optimality beyond textbook interval estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
