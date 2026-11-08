# Independent mathematical audit

## correctness

PASS

In a directed subgraph of a simple cycle the only non-backtracking directed circuits are the two oriented Hamiltonian cycles. If neither survives, SCCs are components of the fully-bidirectional edge subgraph; exhaustive independent reachability checks on every 64+256+1024 arc configuration for n=3..5 confirmed this. Independently oriented forward/backward arc sets give Pr(0<->j)=(p^j+p^{n-j}-p^n)^2. Full SCC connectivity is 2p^n-p^(2n)+n(1-p)^2*p^(2n-2); if the only bad edge does not destroy both directed arcs, an orientation is complete, hence the correction counts exactly both-missing edges. With n(1-p)->lambda finite, independent marked Bernoulli arcs converge to two Poisson point processes and, when each has at least one mark, cyclic gaps are finite-dimensional Dirichlet spacings; tightness yields ranked l1 convergence. When n(1-p)->infty and p->1, rare long bidirectional runs yield the Gumbel law using factorial moments, with one-vertex error negligible since -log(p^2)->0. Endpoint p=0,1 and lambda=0 are compatible. Finite checks are not convergence proofs.

## originality

PASS

General bidirected percolation in Liu–Rolla–Shi concerns infinite transitive graphs, while this exact finite-circle model has a distinct Hamiltonian single-orientation atom and a Poisson-to-Gumbel complete SCC crossover. Undirected Bernoulli spacings and longest-run extremes are classical inputs; novelty is assessed for the explicit directed model and whole crossover, with possible classical directed-ring reliability formulation retained as risk.

## value

PASS

A natural one-dimensional directed percolation model exhibits a qualitatively different single-macroscopic-SCC event from undirected cuts. Its exact connectivity polynomial and complete ranked mass partition, followed by microscopic Gumbel extremes, form a useful connected finite-size/crossover classification rather than routine parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
