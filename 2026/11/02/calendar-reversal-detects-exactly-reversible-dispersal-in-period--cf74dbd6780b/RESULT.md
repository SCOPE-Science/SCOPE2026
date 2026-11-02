# Calendar reversal detects exactly reversible dispersal in periodic patch populations

## Finding

**Theorem (complete reversal criterion and finite witness bound).** Let \(n\ge2\) and let \(P\) be any irreducible, nonnegative, column-stochastic \(n\times n\) matrix. In a linear patch-population model the seasonal update is \(x_{t+1}=PD_t x_t\), where each \(D_t\) is an arbitrary positive diagonal habitat-growth matrix. For a calendar of length \(k\), define the forward and time-reversed period matrices
\[
F_k=PD_k\cdots PD_2PD_1,\qquad R_k=PD_1PD_2\cdots PD_k.
\]
The following are equivalent:

1. \(P\) obeys detailed balance: there exists \(\pi_i>0\) with \(P_{ij}\pi_j=P_{ji}\pi_i\) for every pair of habitats.
2. For **every** \(k\ge1\) and **every** positive diagonal calendar, \(F_k\) and \(R_k\) have identical full characteristic polynomials (not merely equal growth factors).
3. For every integer \(k\) with \(3\le k\le n\), and every positive diagonal calendar of length \(k\), the asymptotic period multipliers obey \(\rho(F_k)=\rho(R_k)\).

For \(n=2\), statement 3 is vacuous and every irreducible stochastic \(P\) satisfies detailed balance. For every \(P\), irrespective of reversibility, calendars of length at most two are always isospectral under reversal. Both thresholds are sharp: three habitats and three distinct seasonal matrices suffice for strict reversal sensitivity.

A fully positive three-habitat example is
\[
P=\begin{pmatrix}\tfrac12&\tfrac25&\tfrac1{10}\\
\tfrac1{10}&\tfrac12&\tfrac25\\
\tfrac25&\tfrac1{10}&\tfrac12\end{pmatrix},\qquad
D_1=\operatorname{diag}(3,1,1),\quad D_2=\operatorname{diag}(1,3,1),\quad D_3=\operatorname{diag}(1,1,3).
\]
For \(F_3=PD_3PD_2PD_1\) and \(R_3=PD_1PD_2PD_3\), exact arithmetic gives
\[
\operatorname{tr}(F_3)=\tfrac{329}{100},\quad
\operatorname{tr}(R_3)=\tfrac{91}{20},\quad
\min_i(R_3^2\mathbf1)_i-\max_i(F_3^2\mathbf1)_i
=\tfrac{10651}{10000}>0.
\]
Consequently \(\rho(R_3)>\rho(F_3)\) with no numerical approximation involved. The period-root inequality is equivalent to a strict inequality between per-season asymptotic growth factors \(\rho(R_3)^{1/3}\) and \(\rho(F_3)^{1/3}\).

**Persistence can also reverse, not just growth speed.** Multiply every displayed seasonal growth profile by the same factor \(c=17/27\). The resulting full period multipliers are \(c^3F_3\) and \(c^3R_3\). The same exact row sums certify
\[
\frac{188454769957001}{193710244500000}<1<
\frac{201309232327951}{193710244500000},
\]
which are, respectively, an upper bound on \(\rho(c^3F_3)^2\) and a lower bound on \(\rho(c^3R_3)^2\). Thus the same three habitat-growth profiles, only temporally reversed, give exponential decline in one ordering and exponential growth in the other. This is a statement about the deterministic model's zero-population stability, not an empirical population forecast.

## Assumptions and scope

All vectors use the column convention: \(P_{ij}\) is the fraction leaving habitat \(j\) and arriving in habitat \(i\), and \(\sum_iP_{ij}=1\). Irreducibility permits zero migration entries but requires every habitat to be reachable from every other. Each season's growth factors are strictly positive, but they need not be bounded above by one or distinct. The same \(P\) acts every season, after growth. The comparison reverses the entire cyclic list of seasonal growth profiles while keeping migration fixed. This is a deterministic, density-independent population model; no claims are made about stochastic environments, finite-time totals, nonlinear feedbacks, variable migration, or empirical persistence probabilities.

## Proof

**Reversibility implies all-length isospectrality.** By detailed balance, \(Q=\operatorname{diag}(\sqrt{\pi_1},\ldots,\sqrt{\pi_n})\) symmetrizes migration: \(S=Q^{-1}PQ\) is real symmetric. Since every \(D_t\) commutes with \(Q\), the period matrices are respectively similar to \(SD_k\cdots SD_1\) and \(SD_1\cdots SD_k\). Taking the transpose of the first produces \(D_1S\cdots D_kS\), which is a cyclic rotation of the second product. The characteristic polynomial is invariant under transposition and under cyclic rotation of a square-matrix product: \(\det(zI-AB)=\det(zI-BA)\), including for singular factors. Therefore the characteristic polynomials are equal for every \(k\) and calendar. This proves 1 implies 2; 2 implies 3 is immediate.

**Growth invariance for at most \(n\) seasons forces reversibility.** Fix an arbitrary simple directed cycle of positive migration edges with distinct sites \(i_1,\ldots,i_k\), \(3\le k\le n\), written as \(i_1\to i_2\to\cdots\to i_k\to i_1\). For each season \(j\) take \(D_j(\varepsilon)=E_{i_j}+\varepsilon(I-E_{i_j})\), where \(E_i=e_ie_i^{\mathsf T}\) and \(0<\varepsilon<1\). These are admissible strictly positive diagonal matrices. At \(\varepsilon=0\), each entire period product has rank at most one, and its trace—and hence its only potentially nonzero eigenvalue—is the product around the corresponding oriented cycle:
\[
\rho(F_k(0))=\prod_{j=1}^k P_{i_{j+1},i_j},\qquad
\rho(R_k(0))=\prod_{j=1}^k P_{i_j,i_{j+1}},
\quad i_{k+1}=i_1.
\]
The first product is positive by the definition of the directed cycle. Spectral radius is continuous in matrix entries; hence condition 3, valid for every \(\varepsilon>0\), gives equality of these two cycle products. In particular every edge in any directed simple cycle has its reversed edge present. Irreducibility ensures every positive edge lies on a simple directed cycle (complete that edge with a simple return path). Thus the support of \(P\) is symmetric. Cycles of length one or two are automatically balanced, and the same limit argument balances all simple longer cycles. Every closed walk decomposes into simple cycles, so all forward and reverse products around closed walks agree.

Choose a root habitat \(r\). For any habitat \(i\), choose a positive-edge path from \(r\) to \(i\) and define the positive weight \(w_i/w_r\) as the product of forward edge probabilities divided by the product of reverse edge probabilities along that path. Symmetric support and cycle balance make the ratio independent of the path. Along every edge \(j\to i\), this construction gives \(w_i/w_j=P_{ij}/P_{ji}\). Normalize \(\pi_i=w_i/\sum_h w_h\) to obtain \(P_{ij}\pi_j=P_{ji}\pi_i\). This proves 3 implies 1 without assuming all entries positive or that \(P\) is nonsingular.

**Sharpness and strict witness.** For \(k=1\) the calendars are identical; for \(k=2\) the products are a cyclic rotation of two factors and always have the same characteristic polynomial. Any two-state irreducible Markov matrix is reversible because its stationary flux across the unique inter-habitat edge must balance. Hence at least three seasons and three habitats are required.

For the displayed \(3\times3\) example, the directed cycle probabilities are \((1/10)^3\) versus \((2/5)^3\), so detailed balance fails even though the migration matrix is strictly positive and doubly stochastic. Direct rational multiplication yields
\[
F_3^2\mathbf1=\begin{pmatrix}689659/62500\\7339579/500000\\7807529/500000\end{pmatrix},\qquad
R_3^2\mathbf1=\begin{pmatrix}14338799/500000\\8340079/500000\\5840221/250000\end{pmatrix}.
\]
The largest entry of the first vector is \(7807529/500000\); the smallest of the second is \(8340079/500000\). Their difference is \(10651/10000\). For every nonnegative square matrix \(M\), the elementary positive-vector spectral-radius bounds give \(\min_i(M\mathbf1)_i\le\rho(M)\le\max_i(M\mathbf1)_i\), without requiring primitivity. Apply these bounds to \(M=F_3^2\) and \(M=R_3^2\). The displayed strict separation yields \(\rho(R_3)^2>\rho(F_3)^2\), hence the desired strict result. Scaling each of the three diagonal growth matrices by \(17/27\) multiplies each period matrix by \(c^3\), so the squared-period spectral bounds multiply by \(c^6\). Direct multiplication of the already displayed rational row sums by \(c^6\) gives the two precise fractions in the finding and proves opposite sides of the persistence threshold.

## Verification

Run \(\texttt{python3 verify.py}\) from the directory containing this manuscript and the supplied standalone Python script. The script uses only the standard library's exact \(\texttt{fractions.Fraction}\) and checks column stochasticity, positivity, the exact rational forward/reverse characteristic polynomials, the two squared-matrix row-sum vectors, the strict spectral-gap bound, the directional cycle imbalance, all two-season orders in the witness, and several symmetric-migration calendar reversals. For further cross-checking, the exact characteristic polynomials are
\[
\det(zI-F_3)=z^3-\tfrac{329}{100}z^2-\tfrac{1118287}{1000000}z-\tfrac{59319}{1000000},
\]
\[
\det(zI-R_3)=z^3-\tfrac{91}{20}z^2-\tfrac{888967}{1000000}z-\tfrac{59319}{1000000}.
\]
The general all-dimensional equivalence and minimality are established by the proof above, not by finite sampling.

## Relationship to prior work

Mertens, Yearsley, van den Bosch and Gilligan (2006) develop transient analyses for periodic demographic matrices and distinguish cyclic permutations, which retain asymptotic growth, from general noncyclic reorderings, which need not. Their full article addresses population-size sensitivity and its timing, not a detailed-balance criterion characterizing the special case where **every** time-reversed calendar has the same spectrum. Schreiber (2010) studies metapopulation growth from products of a constant dispersal matrix and temporally varying diagonal habitat fitness, including temporal autocorrelation and dispersal-rate effects, without deriving this calendar-reversal characterization. Schreiber and Li (2010 preprint; 2011 journal article), particularly their Theorem 2 and Appendix 1, use diagonal symmetrizability to study evolutionary stability for period-two environmental fitness and dispersal-rate changes. Their positive-matrix and symmetrization arguments are closely relevant, but their stated results do not supply the all-period reversal equivalence or the finite witness bound. The classical Kolmogorov cycle criterion is acknowledged as the pre-existing final bridge between directional cycle products and detailed balance; that cycle criterion is **not** claimed as a new theorem here.

The result sharpens the known distinction between cyclic and noncyclic environmental reorderings in a specific ecological matrix class: a noncyclic **reversal** is harmless for all choices of local growth precisely when the migration network has no circulation. Two-habitat seasonal reversal symmetry is a special case of the reversible direction; the all-dimensional converse, finite-testing bound and three-habitat strict counterexample are distinct statements.

## Limitations

The theorem quantifies universal invariance, not invariance for any fixed observed calendar; particular nonreversible matrices may have reversed calendars with equal growth. The construction in the converse is a limiting argument using increasingly habitat-concentrated but strictly positive seasons; the exact example instead uses moderate factors of 3 and 1. The result concerns asymptotic period eigenvalues (and, under detailed balance, the entire spectrum), not transient population sizes, species interactions, or real-world habitat viability. The mathematical proof has been reviewed within this package, but no independent audit or historical priority certification has been performed.

## References

- Mertens, S. K., Yearsley, J. M., van den Bosch, F., and Gilligan, C. A. (2006). *Transient population dynamics in periodic matrix models: Methodology and effects of cyclic permutations*. Ecology 87, 2338–2348. First public date 2006-09-01. DOI: https://doi.org/10.1890/0012-9658(2006)87[2338:TPDIPM]2.0.CO;2. Full text: https://api.unil.ch/iris/server/api/core/bitstreams/39f4a4a0-30ec-490e-8314-846a5f9f412b/content.
- Schreiber, S. J. (2010). *Interactive effects of temporal correlations, spatial heterogeneity and dispersal on population persistence*. Proceedings of the Royal Society B 277, 1907–1914. First online 2010-02-17. DOI: https://doi.org/10.1098/rspb.2009.2006.
- Schreiber, S. J., and Li, C.-K. (2011). *Evolution of unconditional dispersal in periodic environments*. Journal of Biological Dynamics 5, 120–134. Preprint first public 2010-07-29, arXiv:1007.5267. DOI: https://doi.org/10.1080/17513758.2010.525667.
- Kolmogorov's cycle criterion for finite-state reversible Markov chains (classical standard result); a direct derivation of the needed direction is provided in the proof.
