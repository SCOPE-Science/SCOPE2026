# Independent mathematical audit

## correctness

PASS

Reconstructed free 2-convex lattice norm using finite PSD design duality: ||vee_r |delta_{b_r}|||=max_{w in simplex} tr sqrt(sum w_r b_r b_r^T). Average by S_v using concavity, with no restriction to invariant test families. Johnson J(v,2) and complement Laplacians have zero and two nontrivial eigenspaces: E1 dim v-1, eigenvalues L1=v,L2=N-v; E2 dim v(v-3)/2, eigenvalues L1=2(v-1),L2=N-2(v-1). This yields U_b(x)=P sqrt(2b+(1-2b)x)+Q sqrt(cb+(1-cb)x), c=(v-4)/(v-3), P=sqrt(2(v-1)/(v-2)), Q=(v-3)sqrt(v/(v-2)), b=a². Strict scalar concavity gives beta_minus=(P+Q)/(2P+cQ) and beta_plus=(P/sqrt2+Q/sqrt(c))/(sqrt2 P+sqrt(c)Q) for v>=5, infinity for v=4; weighted Cauchy-Schwarz gives interior radical. Information matrix uniqueness by strict operator concavity on connected zero-sum space and off-diagonal recovery, and marginal sensitivity gives arbitrary disjoint-edge addition no-growth iff each a_e²<=beta_minus. Independent scipy scalar optimizations in 24 points v 4,5,6,8,15,60 across phases matched all piecewise branches. Formula is analytic for all v>=4, a>0; numeric tests not an infinite proof.

## originality

PASS

The general free p-convex lattice norm by Jardón-Sánchez et al and standard Johnson/Kneser graph eigenvalues and Kiefer optimal design are prior art. Their abstract general expressions do not state the mixed Johnson/Kneser two-threshold amplitude profile nor the simultaneous exact coordinatewise no-growth condition. A possible equivalent optimal-design theorem applied to this association scheme is an explicit residual priority risk.

## value

PASS

Determines the exact norm of a canonical competing graph-orbit operator for all amplitudes and graph orders, including a singular small case and an exact subfamily robust no-growth threshold. These are motivated phase boundaries for a natural association scheme rather than renaming a previously solved scalar example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
