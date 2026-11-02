# Independent mathematical audit

## correctness

PASS

For star K_{1,m}, m>=2, conductance budget sum c_i w_i<=B, every pairwise leaf resistance is 1/w_i+1/w_j; the normalized x_i=(Delta w_i)^{-1} satisfy x_i+x_j<=1. Minimizing F=sum c_i/x_i splits into all x_i<=1/2 (unique all-half minimizer) and a single x_j>1/2. In the latter case all other x_i=1-x_j, and strict convexity of c_j/u+(C-c_j)/(1-u) gives its unique square-root optimum iff c_j>C/2. Thus Delta*=2C/B if max price<=sum others, otherwise (sqrt(a)+sqrt(C-a))^2/B; equality and the sharp <2 improvement factor follow. Independently minimized smooth normalized cost on five price families and sampled competitors; an earlier direct nonsmooth SLSQP formulation returned a suboptimal stationary numerical point, a solver limitation not counterevidence to the convex proof.

## originality

PASS

The contribution is an exact and unique heterogeneous-price minimax resistance-diameter design law on a star, with a sharp dominant-price transition, not the known path-resistance formula, convex feasibility, or general SDP solvability. Full relevant sections of Ghosh--Boyd--Saberi distinguish their optimized total pairwise resistance from maximum pairwise resistance, for which they describe an SDP without this explicit threshold. No reviewed Resultary hit covers the formula; less indexed minimax resource-allocation formulations remain possible.

## value

PASS

Choosing edge conductances to limit worst-case electrical resistance is a natural network-design objective. The exact all-price threshold and uniform-weights-versus-price-dominant optimizer classify all m>=2 cases and give a sharp approaching-two performance gap; they distinguish minimax from known total-resistance allocations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
