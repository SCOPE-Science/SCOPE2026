# Independent mathematical audit

## correctness

PASS

The only bi-infinite zero-cost paths use the A and B loops: no zero-cost edge enters C. Nonpositive potential thus forces every maximizing invariant measure onto the two fixed points. For positive epsilon the transfer matrix is positive. Eliminating C near lambda=1 gives the first-order perturbation on A,B with entries [1,1;1,0], whose roots are phi and -1/phi. Equivalently the characteristic expansion in the frozen proof gives those two simple roots and the remaining eigenvalue is O(epsilon). The Perron pressure is phi epsilon+O(epsilon^2), and the slow Markov eigenvalue is the ratio of the two transfer eigenvalues, 1-sqrt(5) epsilon+O(epsilon^2). The left and right Perron equations normalized at A give B/A ratios 1/phi+O(epsilon) and left C=O(epsilon), right C=1+O(epsilon). Their products give the claimed weights; nonconstant finite cylinders have vanishing probability. For the kinetic statement, the Markov chain traced on D={A,B} has kernel K_DD+K_DC(1-K_CC)^(-1)K_CD, from summing the geometric excursions. Its off-diagonals are epsilon/phi and phi epsilon to first order, so its powers on the scaled clock converge to exp(sQ). In the stationary original chain at most O(1) visits to C are expected up to time floor(s/epsilon); the number of deleted time steps is tight. On a deterministic window of L steps about each sampling index the trace chain jumps with probability O(L epsilon). This transfers finite-dimensional convergence back to the projected original chain by bounding the delay by L and then sending L to infinity. In the two-symbol case mixing with both loops forces both cross edges; equal diagonal transfer entries give equal left-right Perron products at every positive temperature. Any limiting measure is maximizing by the finite-state entropy bound in the variational principle, and thus is the equal mixture. One symbol cannot support two different fixed points.

## originality

PASS

The exact golden weights and three-symbol/two-fixed-ground-state setting have a primary-literature precedent, and general locally constant selection and irrational examples are known. The supported distinct claim is a nearest-neighbor realization in the sharp minimum alphabet together with the explicit scaled two-state dynamics for this realization. The strongest inspected sources do not establish that class boundary and kinetic statement.

## value

PASS

The motivating finite-range selection problem and the earlier nonlocally constant golden example make the minimal realization a natural question. A three-state construction together with a universal two-state obstruction identifies a sharp structural boundary for two fixed phases, not just an irrational number found by calculation. The explicit kinetic scale and rates also show how the asymmetric mass arises dynamically in this minimal model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
