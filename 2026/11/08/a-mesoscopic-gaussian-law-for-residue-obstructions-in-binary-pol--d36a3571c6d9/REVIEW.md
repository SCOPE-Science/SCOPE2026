# Independent mathematical audit

## correctness

PASS

For d≥2^16 set L=log_2 d, E=ceil L, B=floor(L-log_2 L-3). For P irreducible degree j≥2 and Q=2^j, conditional valuation probabilities are (1−Q^{-1})Q^{-e}. For e=1 the residue trace-one probability is Q/[2(Q−1)] by invertible unit multiplication in F_Q; for e≥2 the principal-unit action h↦h(1+P^{e−1}s) adds a surjective trace form and balances values. Consequently beta_P=1/(2Q)+1/(2Q^2); truncating valuations e≥E replaces beta_P by beta_{P,E}=beta_P−1/(2Q^E). For e<E the local bit is determined by f mod P^{2E}. Since S_B=Σ_{2≤j≤B}jI_j<2^{B+1} and 2^B≤d/(8L), the CRT modulus has degree 2ES_B<d; uniform monic degree-d polynomials therefore have EXACT independent truncated bits. Coupling true to truncated bits costs Σ_P Q^{−E}; comparing Bernoulli parameters adds 0.5Σ_P Q^{−E}. For E≥16, 1.5Σ_{j≥2}I_j2^{−Ej}≤6d^{−2}/(1−2^{1−E})<7d^{−2}. Irreducible counting I_j=2^j/j+O(2^{j/2}) gives mu_B,v_B=(log B)/2+O(1); the independent Bernoulli third centered moment sum is O(v_B), so Berry–Esseen plus TV yields the stated Kolmogorov bound. The absolutely convergent renormalized product supplies the positive constant C and relative O(B^−1) finite cutoff error. The asymptotic only concerns W_d, not positive orthogonal multiplicity. Independent finite arithmetic and exact tree recreation corroborated source premises and output constants; finite checks do not prove infinite statements.

## originality

PASS

The exact unconditional near-logarithmic prime-degree cutoff and 7d^{-2} total-variation control for all residue-trace bits, with its specific Bernoulli parameters and zero-event Euler constant, were not established by the inspected prior statements. Giraudin (2026) proves exactly the local residue distribution and reciprocity; those are cited inputs. Arratia–Barbour–Tavare (1993) treats factor multiplicity vectors and the 2005 study treats additive component functions; the present residue-bit J_P(f) depends on the cofactor modulo P and is not additive as a function of factorization (explicit P=T^2+T+1 example). A direct quantified CRT combination of the 2026 local theorem constitutes the surviving contribution, rather than a new general sieve principle. The same-record Resultary listing was excluded as a predecessor; additional published SCOPE cases cover only finite orthogonal multiplicity or extremal thresholds. Historical general-sieve priority risk and the inaccessible 1998 original are explicit.

## value

PASS

The differential-residue obstruction count is a natural and explicitly motivated statistic linked to the open pooling problem in the 2026 primary study. The result identifies an unconditional CRT-controlled regime containing a growing d/polylog(d)-scale number of small-prime residue bits, with an explicit uniform O(d^−2) joint approximation despite a global reciprocity constraint and with a sharp interpretable zero-survival exponent 1/2 and Euler constant. This is a useful precise boundary and benchmark for any future attempt at the full global law, beyond an arbitrary finite slice or textbook exercise. The local distribution, CRT, Berry–Esseen and harmonic summation are standard ingredients, credited as such; value attaches to the quantitatively complete combination for this specific non-additive residue observable, not to invention of a new general sieve or settlement of orthogonal multiplicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
