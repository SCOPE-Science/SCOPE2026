# Independent mathematical audit

## correctness

PASS

Balancing the two environmental flows at each fixed integer j gives p_j, with p_0=0 and p_g=1 and unique stationary probabilities at the intermediate compositions. Conditioning on the same k cooperating co-players for both focal strategies gives gain r_L−1+Δ E[d_k], where d_k=(k+1)p_{k+1}−kp_k and k has the stipulated binomial law. Equal exponents give d_k as consecutive increments of t^(1+α)/g^α, strictly increasing by convexity. Differentiating the Bernstein average represents its derivative as a convex combination of strictly positive adjacent differences times (g−1)Δ, including both endpoints. For g=2 the difference is always 2(1−p_1)>0. For g=3 the three coefficients are u, 2v−u, 3−2v; expansion gives F as stated. Two simple interior roots with negative endpoint gains and the stated signs require concavity and an interior maximum. Since 0<u,v<1, F′(1)<0 is equivalent to 4v>3+u and implies F′(0)>0. The vertex and endpoint values then give the strict necessary and sufficient inequalities; the phase-line signs show both basins. In the witness, log 3>1 and 1−exp(−1/100)>1/101 give u<1/20, while log(3/2)<1/2 gives v>11/12. Thus F(0),F(1)<7/6 and F(1/2)>287/240>7/6, so both roots are simple and the inequalities persist under perturbation. Independent replay: python3 /workspace/independent_checks_oct19.py (game_check), direct focal-payoff averaging over four configurations and bisection gave roots 0.46517006461375 and 0.97198265014488. The supplied checker was read, not executed. The theorem is for the assumed annealed replicator, not a limiting theorem for finite hypergraph imitation.

## originality

PASS

The transition law is Wei et al.'s, the gain-polynomial machinery and generic unstable/stable root pair are Peña et al.'s, and cooperation promoted by environmental transitions in individually unfavorable games has qualitative antecedents. The supported distinct result is the model-specific sharp group-size/memory obstruction and the robust, parameter-explicit subunit-synergy three-person regime in a separately stipulated annealed replicator, not those general mechanisms.

## value

PASS

The group-size and memory question is natural in this environmental feedback model. A uniform no-memory exclusion and an exact minimal-size witness with both fixed games individually discouraging cooperation together separate the effect of making transitions state-dependent from the ordinary static rewards. The strict region has two basins with explicit boundaries, and is more informative than a numerical observation or a generic quadratic example. No finite-network, fixation, or empirical conclusion is warranted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
