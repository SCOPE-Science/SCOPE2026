# Independent mathematical audit

## correctness

PASS

PASS. Reconstructed anchored-coordinate Lipschitz polytope for K_{p,q}, p>=2, q>=3, 2<=k<=q-1, equal exceptional star-edge lengths 1<=h<=3, anchor at an unaffected A-vertex. Fubini fixes ordinary A values of range R and B-interval L=2-R. The exceptional A variable z has section F_{r,k}(L,h)=int phi_1(z;L)^r phi_h(z;L)^k dz. Reflection gives 2 int_0^(1+L/2) min(v,L)^r min(v+h-1,L)^k dv; subtracting h=3 yields a positive finite binomial sum. The range pushforward moment integral int (L-s)_+^b d nu_{p-1}= (p-1)! b!/(p+b-2)! (2-s)^(p+b-2) also holds as a point-mass when p=2. Integrating recovers all finite-sum coefficients, V(1)=2^d p!q!/d!, V(3)/V(1)=1+2k/[p(q-k+1)], increasing deletion increments 2(q+1)/[p(q-k)(q-k+1)], and first nonzero endpoint deficit 2^k k(p-1)!(q-k)!/(p+q-k)! (3-h)^(p+q-k). Hence exactly C^(p+q-k-1) across h=3, not next order. Inspected verify_volume.py: Ehrhart finite differences are a distinct combinatorial consistency method in eight rational cases, never a universal proof. No evidence of a missing normalization; anchor coordinates, integer exponents, and k=0/1 comparison are explicit.

## originality

PASS

Best-of-knowledge PASS for the joint k>=2 volume polynomial and sharp smoothness loss; the graph-transport quotient, known single-edge perturbation, unweighted bipartite Ehrhart invariants and volume-product literature do not imply the interaction term. Mathematical equivalence with transportation-cost polars was considered, not treated as proof of novelty.

## value

PASS

PASS. The exact volume under physically natural simultaneous deletion/lengthening of a star in a complete bipartite graph quantifies a non-additive interaction, a sharp smoothness exponent that changes with the number of deleted edges, and an explicit endpoint volume gain. These are motivated quantitative invariants of graph metric/Lipschitz geometry beyond a routine one-edge substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
