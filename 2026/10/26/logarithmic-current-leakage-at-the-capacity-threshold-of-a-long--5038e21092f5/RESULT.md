# Logarithmic current leakage at the capacity threshold of a long-branch exclusion process

## Finding

Consider the stationary asymmetric simple exclusion process (ASEP) on a ring of \(L\geq3\) backbone vertices and one attached path of \(M\geq1\) extra vertices. The right/left backbone hopping rates are \(h_f>h_b>0\); the outward/inward branch rates are positive, with ratio \(q=h_t/h_r\). The number of particles is fixed. Write \(K\) for the number occupying the backbone, and \(J\) for the stationary signed current across one directed backbone bond (per bond, not summed over the ring).

**Theorem (critical logarithmic leakage).** Fix \(q>1\) and a sequence \(L,M\to\infty\) satisfying \(M/L\to\eta\in(0,\infty)\). At the capacity-matched filling \(N=M\), let \(c=\log q\). Then

\[
\mathbb E K=\frac{\log L-\log\log L+\log c}{c}+O_{q,\eta}(1),
\qquad \operatorname{Var}(K)=O_q(1),
\]

and

\[
J=\frac{h_f-h_b}{cL}\big(\log L-\log\log L+\log c+O_{q,\eta}(1)\big).
\]

In particular \(JL/\log L\to(h_f-h_b)/\log q\). The exact particle–hole identity

\[
J_{L,M}(N;q)=J_{L,M}(L+M-N;q^{-1})
\]

holds for every finite system at fixed backbone rates. Consequently, when \(0<q<1\), the corresponding capacity-matched threshold is \(N=L\) and the same formulas for the current and the number of *backbone holes* hold with \(c=|\log q|\).

## Assumptions and scope

The backbone forms a periodic simple cycle on \(L\geq3\) distinct vertices. A single linear branch with vertices at depths \(1,\ldots,M\) attaches to one backbone vertex (depth zero). On any occupied-to-vacant backbone edge, particles jump clockwise at \(h_f\) and counterclockwise at \(h_b\). On the branch they jump to greater depth at \(h_t\) and to lesser depth at \(h_r\); all four rates are strictly positive. No particle creation, annihilation, multiple occupancy or external reservoirs are included. Each finite fixed-particle-number chain is irreducible.

The branch-to-backbone rate ratio \(q\) is fixed independently of system size. The asymptotic is not asserted uniformly as \(q\to1\) or when \(M/L\) approaches zero or infinity. The exact finite-size identities below hold without the asymptotic size restriction.

## Proof

**1. Stationary counting and the critical ratio.** The known exact stationary law gives a configuration with occupied branch depths \(d_1,\ldots,d_s\) weight proportional to \(q^{d_1+\cdots+d_s}\); backbone positions carry weight one [1, Eq. (15)]. At \(N=M\), if exactly \(K=k\) particles are on the ring, exactly \(k\) branch sites are empty. Set \(a=q^{-1}\in(0,1)\). After dividing out the weight of the completely filled branch, the weight of this event is

\[
W_k=\binom Lk\sum_{1\le d_1<\cdots<d_k\le M}a^{d_1+\cdots+d_k}
=\binom Lk a^{k(k+1)/2}\begin{bmatrix}M\\k\end{bmatrix}_a,
\quad 0\le k\le\min(L,M).
\]

Here the Gaussian binomial is defined by \(\begin{bmatrix}M\\k\end{bmatrix}_a=\prod_{j=1}^{k}(1-a^{M-j+1})/(1-a^j)\). The equality follows by grouping strictly increasing integer depths; equivalently it follows inductively from the elementary-symmetric-function recurrence. Therefore the consecutive ratio is **exactly**

\[
R_k:=\frac{W_{k+1}}{W_k}=\frac{L-k}{k+1}\,a^{k+1}\frac{1-a^{M-k}}{1-a^{k+1}}.
\]

Every factor other than \(a^{k+1}\) is decreasing in \(k\), so \(R_{k+1}<aR_k\) whenever both ratios exist. Thus the critical occupancy law is strictly log-concave, with at most two adjacent modes.

**2. Mode location.** Let \(m\) be a mode chosen so that \(R_{m-1}\ge1\ge R_m\). Since \(M/L\to\eta>0\), evaluation of the displayed exact ratio at \(k=\lfloor (\log L)/(2c)\rfloor\) and at \(k=\lceil 2(\log L)/c\rceil\) shows \(m\asymp\log L\); these test indices are eventually much less than both \(L\) and \(M\). Uniformly for \(k\asymp\log L\),

\[
\log R_k=\log L-\log(k+1)-(k+1)c+o(1).
\]

Applying the two mode inequalities yields \(cm+\log m=\log L+O(1)\). Inverting this monotone equation gives

\[
m=\frac{\log L-\log\log L+\log c}{c}+O(1).
\]

This inversion can be checked by substitution; the derivative of \(ct+\log t\) is at least \(c\), so bounded residuals imply bounded root displacement.

**3. Uniform concentration.** By \(R_{k+1}<aR_k\) and the mode inequalities, for integers \(j\ge1\) within the support,

\[
\frac{W_{m+j}}{W_m}\le a^{j(j-1)/2},
\qquad
\frac{W_{m-j}}{W_m}\le a^{j(j-1)/2}.
\]

The normalizer is at least \(W_m\). Hence \(\mathbb E|K-m|^r\le2\sum_{j\ge1}j^r a^{j(j-1)/2}<\infty\) uniformly in \(L,M\) for each fixed \(r>0\). In particular \(\mathbb E K=m+O_q(1)\), \(\operatorname{Var}K=O_q(1)\), and \(\mathbb E K^2=O_q((\log L)^2)\).

**4. Exact current and asymptotics.** Conditional on \(K=k\), every \(k\)-subset of ring sites is equally likely. A specified ordered bond is occupied then vacant with probability \(k(L-k)/(L(L-1))\). The opposite orientation has the same probability. Thus

\[
J=(h_f-h_b)\frac{\mathbb E[K(L-K)]}{L(L-1)}
=\frac{h_f-h_b}{L}\big(\mathbb E K+O_q((\log L)^2/L)\big).
\]

Substituting the first three steps proves the claimed leakage expansion.

**5. Particle–hole duality.** Complement every occupation variable. The product stationary weight transforms, up to a configuration-independent factor, from \(q^{\sum_{\mathrm{occupied\ branch}}d}\) to \((q^{-1})^{\sum_{\mathrm{occupied\ branch}}d}\), while \(N\) becomes \(L+M-N\). On any periodic ring configuration, the number of occupied–vacant bonds equals the number of vacant–occupied bonds. Therefore the signed current, which equals \((h_f-h_b)\) times either bond probability under the translation-invariant stationary law, is unchanged by the complement. The stated exact identity follows; the \(0<q<1\) threshold is its direct image.

## Verification

The standalone `verify.py` independently enumerates canonical weights from elementary symmetric polynomials, compares them against the exact Gaussian-binomial ratio, constructs the complete finite-state Markov generator for two small graphs and checks stationarity and current, tests particle–hole reciprocity, and checks the logarithmic/logarithm-of-logarithm centering for five sizes at four fixed biases. Executing the script with Python, NumPy and SciPy produced `PASS: 86 independent deterministic assertions`.

The proof of the infinite-size result is the ratio-and-concentration argument above; finite computations are corroboration only. The error term is bounded, not explicitly optimized. The finite-state tests do not prove any infinite-volume statement.

## Relationship to prior work

Ishiguro and Ando [1] establish the exact canonical stationary weight and current formula for a single long branch [1, Eqs. (15), (31)–(42)], and plot a nearly blocked region. The formulas, the model and the qualitative branch trapping are prior art. The finding here is the **sharp critical-size leakage** \(\log L/L\), its \(-\log\log L\) correction, bounded occupancy fluctuations, and the exact reciprocal-bias boundary relation. These are not stated in [1].

Sarkar and Gupta [2] develop product-weight stationary states and transport analysis for a *random comb with many disordered branches*, including saddle-point descriptions of typical occupancies. Their Appendix B also treats stationary weights with a single branch. Those facts are not claimed as new; the specific capacity-matched long-branch \(L\)-dependent asymptotic is a different limit than the random-comb thermodynamic regime considered there. Ishiguro and Sato [3] prove the general transition-decomposition construction of exact stationary ASEP measures; it does not explicitly evaluate this boundary-layer current asymptotic.

## Limitations

Independent priority assessment has not been performed. Other analyses of canonical inhomogeneous exclusion ensembles might imply the asymptotic after an unrecognized reduction. The theorem concerns stationary mean current, not temporal fluctuations, relaxation or spectral gaps. It assumes a single length-\(M\) branch, homogeneous ring rates and fixed nonunit branch bias. It does not cover random trees, junction disorder, a bias tending to one with size, or nonequilibrium open boundaries.

## References

[1] Y. Ishiguro and Y. Ando, *Asymmetric simple exclusion process with tree-like network branches*, arXiv:2603.09694v1 (first posted 2026-03-10), https://arxiv.org/abs/2603.09694.

[2] M. Sarkar and S. Gupta, *Asymmetric simple exclusion process on a random comb: Transport properties in the stationary state*, arXiv:2502.11931 (first posted 2025-02-17), https://arxiv.org/abs/2502.11931.

[3] Y. Ishiguro and J. Sato, *Exact steady states in the asymmetric simple exclusion process beyond one dimension*, arXiv:2403.01934v1 (first posted 2024-03-04), https://arxiv.org/abs/2403.01934.
