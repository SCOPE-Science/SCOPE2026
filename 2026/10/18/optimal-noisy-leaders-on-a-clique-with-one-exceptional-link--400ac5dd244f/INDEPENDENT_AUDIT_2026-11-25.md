# Independent mathematical audit

## correctness

PASS

The positive-definite grounded matrix is the grounded unit clique B plus (w-1)bb^T, b=e1-e2. With v_i=c on leaders and a otherwise, the inverse of B is diag(v)+vv^T/[q(a-c)], since 1-sum(v)=q(a-c)>0. Its trace depends only on q. A second update gives J=J_clique+(1-w)s/[1-(1-w)r] with r=b^TB^-1b and s=||B^-1b||^2. The cases j=0,2 give 2a or 2c for r and 2a^2 or 2c^2 for s; the mixed case follows by squaring ce1-ae2-v/q. In particular r<=2/n<1 so the weakening denominators are positive. Under weakening j=2 has strictly smaller r,s than its competitors; q=1 excludes that count, gives equal r for j=0,1, and wins at j=0 by smaller s. Reinforcement maximizes s/(1+ur), u=w-1>0. Its j=1 versus j=2 numerator has positive constant and linear coefficients: the latter is 2c[a(a-c)(1+1/q)+a^2 n/q^2], establishing strict dominance whenever both counts are feasible. The j=1 versus j=0 numerator is exactly D+uH, with a positive denominator. The feasible endpoint counts give the stated q=1, n-1, n and interior cases, ties included, while w=1 gives full symmetry. Independently computed inverse traces via principal minors divided by determinant for all ten K5 three-leader sets at each of 11/10, 27/22 and 2. In order of j=0,1,2 the traces at equality are 49/60, 49/60, 212/255; the unique minimizing counts on the two test sides are 0 and 1 respectively.

## originality

PASS

The common noisy-consensus objective, resistance criteria and matrix updates are standard. The supported distinct contribution is the exact all-budget placement and tie rule for a clique with one continuously varied link. The strongest located papers or distinct catalogue records do not provide that optimizer classification.

## value

PASS

A single weighted link is a natural symmetry-breaking case in otherwise exchangeable finite-gain consensus. The theorem solves design rather than just evaluating a placement: it proves a budget-dependent change under weakening and a sharp switch with a tie under reinforcement. The K5 witness demonstrates that choosing by endpoint status alone, without the weight, is inadequate even in this minimal perturbation setting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
