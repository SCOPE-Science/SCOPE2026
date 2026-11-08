# Independent mathematical audit

## correctness

PASS

On a path covering all vertices is equivalent to having visited both endpoints. After the first endpoint, expected optimal remaining cost equals L_N=H_N(0), independent of which endpoint. The one-target H_N(i)=sum_{j=i}^{N-1}(2-3^{-j}) and two-endpoint E_N(i) satisfy exact minimizing Bellman equations: H(i)=1+(3H(i+1)+H(i-1))/4 and E(i)=1+(3 min(E neighbors)+max(E neighbors))/4. Their strict monotonicities certify the offered-direction rules for arbitrary history-dependent control; finite expected absorption justifies stopping verification. For paths ≤5 vertices, each possible frontier freshness conflict is weakly compatible; at six vertices visit interval [1,2] with offers {1,3} gives a strict cost gap 4/3. Independent rational Bellman checks for all N≤40, including parity gap identity.

## originality

PASS

Compared exact statements, hypotheses and consequences against indexed published findings and primary literature, without treating unsuccessful searches as proof of priority.  Best-of-knowledge originality survives because the observed prior results do not entail the entire exact claim.

## value

PASS

This is the complete finite-order optimal-control solution of a natural path model, with an explicit sharp threshold exposing the failure of the intuitive unvisited-first heuristic. Both closed cover means and policy boundary are useful independent of general tree asymptotics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
