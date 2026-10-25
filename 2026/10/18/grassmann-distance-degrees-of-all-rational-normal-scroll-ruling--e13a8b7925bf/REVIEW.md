# Independent mathematical audit

## correctness

PASS

For each n_i>=2, the ruling plane is the rank-d symmetric projector diag(v_i v_i^T/s_i) off roots of s_i. Genuine rank-d projection data Q_w assembled from normalized block vectors yield F_w(t)=sum_i g_i(t)^2/(q_i s_i(t))=R_w/L. All s_i are squarefree with no zeros +/-1; L is squarefree, and residues at its roots are generically nonzero. Thus the rational map P1->P1 has degree delta=deg L. The proof supplies a nondegenerate family of quadrics for generic critical simplicity, a codimension-two incidence exclusion of the rank(PQ)<d cut locus (g_i(t)=0 for some block) and nonramification at infinity; Riemann--Hurwitz leaves exactly 2delta-2 finite regular critical points. Generic nonvanishing resultants and irreducibility of the projection Grassmannian carry this count from special valid projectors to generic constrained data. Independently rebuilt rational trace, R, L and derivative H in SymPy for legal block vectors with multi-degrees (2,2),(2,3),(2,2,2): deltas (4,10,4), squarefree H degrees (6,18,6), no collisions with L or each g_i. Checked cyclotomic degree formula and S(2,m) boundary. Finite examples corroborate, not establish, all degrees.

## originality

PASS

Friedman--Hosten--Rosana Example 2.1/Theorem 2.2 in arXiv:2610.02018v2 already calculate the same curve’s ED degree 2delta-2 for unrestricted symmetric matrix data, a strong directly relevant prior. Their general Theorem 4.4 is a conditional equality criterion plus expected codimension heuristic, NOT a theorem guaranteeing GD=ED for every scroll ruling curve. This claim proves the additional constrained rank-d projector noncollision/cut-locus hypotheses, so only GD=ED specialization is treated as original, subject to a hidden immediate corollary risk.

## value

PASS

GD and ED optimize over different data spaces; equality is not automatic for Grassmann submodels and can be strict. A natural infinite family of ruling curves for all block degrees admits an exact constrained critical-count formula tied to cyclotomic poles. Proving genuine projector data achieve the ED number establishes a meaningful boundary of the general GD-vs-ED question, not an arbitrary numeric special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
