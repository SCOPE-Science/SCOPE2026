# Independent mathematical audit

## correctness

PASS

For every d>=3, q_i>=2, c_i>0, the energy-normalized gradient projection is symmetric idempotent. Starting from the zero-sum edge dipole, the product heat kernel integrates to a strictly positive h_i. Counting its signed gradients: coordinate i contributes 2(q_i-1)/q_i, and each j!=i contributes 2(q_j-1)sqrt(c_i*c_j)/(q_i*c_i+q_j*c_j), with monotone heat-kernel differences justifying absolute values. Thus row and column norms equal max_i R_i. Pairwise AM-GM proves R_i<=F_i; a maximizing row requires q_i*c_i=q_j*c_j for all j, so the maximizing ratios are unique up to scale. The explicit F_i-F_j formula is positive for q_i<q_j; equal conductances likewise favor smallest alphabet. This is universal analytic reasoning, not inferred from four finite matrix tests.

## originality

PASS

The two-factor rook-graph formula is acknowledged as covered and excluded. Kassel–Wu gives the transfer-current projection, Jiang–Lim–Yao–Ye the general Hodge framework, and Hibino–Lee–Obata the spectral context. None of their inspected statements evaluates arbitrary mixed d>=3 row-sum norms, proves the pairwise absolute flow formula or uniquely optimizes all positive c_i. Prior equivalence remains possible in uninspected electrical-resistance literature.

## value

PASS

For a canonical multiattribute product-of-cliques comparison graph, the exact worst coordinatewise sensitivity of energy-normalized least-squares gradient recovery is an important operator invariant. The fact that all higher-dimensional edge responses split pairwise, with a unique jointly worst rate balance and a precise smallest-alphabet sensitivity rule, is a nontrivial structural and optimization result rather than a renaming of d=2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
