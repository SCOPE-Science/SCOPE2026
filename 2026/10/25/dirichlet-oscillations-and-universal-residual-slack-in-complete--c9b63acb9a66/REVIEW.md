# Independent mathematical audit

## correctness

PASS

Reconstructed polar inequalities M_A-m_B<=1 and M_B-m_A<=1, giving R_A+R_B<=2. In the anchored chart x_{a0}=0, the centered-to-H Gram determinant is 1/n, so intrinsic Jacobian 1/sqrt(n). The anchored A-span distribution has cumulative p*r^(p-1) and density p(p-1)*r^(p-2); for span r each B coordinate independently ranges over an interval of length 2-r. The beta integral gives anchored volume 2^(n-1)*p!*q!/(n-1)! and the intrinsic formula. R_A/2~Beta(p-1,q+1); independently R_B/(2-R_A)~Beta(q-1,2); stick-breaking gives all three Dirichlet coordinates and the Beta slack tail. Independent gamma variables with total shape n yield the CLT/Gamma joint limit, with exact p/n centering, and the p=1 volume boundary is computed separately. Finite hull, Ehrhart, and sampling diagnostics from inspected checker.py corroborate but are not the proof.

## originality

PASS

This identifies a specific continuous uniform-volume law inside the polar complete-bipartite Lipschitz body; the checked close originals establish graph polar duality, lattice/facet data and primal h* data, not the joint Dirichlet law and universal slack. The volume normalization may be known independently. The priority conclusion is best-of-knowledge and allows an equivalent order-statistic presentation.

## value

PASS

Oscillation budgets are a canonical metric observable of graph Lipschitz potentials. The universal slack law and exactly anticorrelated Gaussian limit are natural, usable distributional invariants of every complete bipartite graph; they are not determined by the known primal face counts. The normalization also distinguishes balanced and star partitions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
