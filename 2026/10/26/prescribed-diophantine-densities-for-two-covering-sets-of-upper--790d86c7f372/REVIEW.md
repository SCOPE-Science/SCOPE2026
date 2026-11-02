# Independent mathematical audit

## correctness

PASS

The density definition requires uniform numerator p coprime to all sufficiently large q, a constant C and v∈T with 1<=v<q. For prime q, each fixed v<q covers O(q^(1-s)) reduced numerator classes; Bertrand extends T(q)≫_s q^s from primes to all Q, giving δ(T)<=liminf_Q log T(Q)/log Q. For 0<t<1, stages n_k=floor(2^(tk)),d_k=floor(2^k/n_k) produce S_t of O(Q^t) counting growth and Dirichlet guarantees a v=md_k<q at every q in (2^k,2^(k+1)] with fractional error <=1/(n_k+1), so δ(S_t)=t. Endpoint cores S0=∅ and S1=N are handled separately. Alternating b_{j+1}=2^(b_j) full blocks E and O=N\E cover N, each with upper ordinary density one and liminf logarithmic count exponent zero at alternate endpoints. Then Aα=E∪Sα and Bβ=O∪Sβ have lower δ from the core and upper δ from the sparse endpoint count, achieving exactly all (α,β). Independent exact-q tests for t=1/2 and q<121 support finite boundaries, not asymptotic conclusions.

## originality

PASS

Qualified best-of-knowledge resolution of Sanford’s exact union/subadditivity question, sharpened to all covering pairs; proof openly uses known upper-counting bound, prescribed cores and alternating blocks, whose combination is elementary and may have appeared independently.

## value

PASS

Directly solves the open union question for the exact restricted Diophantine density proposed by Sanford 20 Oct 2026 and strengthens it to the entire [0,1]² pair spectrum under coverage with both upper ordinary densities 1. It identifies a maximal failure of subadditivity for a natural number-theoretic approximation invariant. Existing analytic ingredients do not make the resulting precise invariant worthless merely because the proof is short.

The dated certificate retains the supplied scientific assessment, sources and limitations.
