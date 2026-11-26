# Independent mathematical audit

## correctness

PASS

For the repaired finding, the epoch convention Z_k=(x_{2k},x_{2k-1}) and unreset momentum give P=[[1/5,7],[-1/20,-1/2]], Q=[[1/5,1/40],[-14,-1/2]]. Their common characteristic polynomial is s^2+3s/10+1/4 with simple roots of modulus 1/2. Exact independent reconstruction gives leading principal minors 58833/800 and 1643697/2560000 for (P^T P+Q^T Q)/2-(49/2)I. Positivity and independence give the one-step bound for every state, iterated by the tower property for any deterministic start. The Euclidean norm is of the full two-iterate state; the certificate does not assert almost-sure divergence. Replay: python3 /workspace/reproductions/independent_checks.py 3.

## originality

PASS

Only the simultaneous spectral factor 1/2 and uniform quantitative conditional norm bound at the specified rational witness survives. Neither the qualitative phenomenon nor the deterministic phase diagram is retained as a contribution. The available prior claims do not give the all-state conditional gain in this setting.

## value

PASS

The retained witness separates rapid asymptotic frozen stability from immediate large conditional average expansion, uniformly over every input direction in the natural two-coordinate state. At the same gradient budget and momentum coefficients, even the best direction cannot avoid the one-epoch expected norm penalty. That is stronger than merely identifying one divergent example or a moment-operator instability, and is useful for stress-testing order-dependent momentum rules. The result does not suggest that individual component stability also holds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
