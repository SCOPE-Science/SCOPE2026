# Sharp four-state positivity frontier for fourth-order Padé steps on directed Markov cycles

## Finding

For every integer \(n\ge 2\), let \(P_n\) be the cyclic permutation matrix defined by \(P_ne_j=e_{j+1\pmod n}\), where subscripts are understood modulo \(n\), and let \(Q_n=P_n-I_n\). The continuous-time Markov semigroup \(e^{hQ_n}\) is strictly entrywise positive for every \(h>0\). Let the fourth-order diagonal Padé (equivalently, two-stage Gauss–Legendre Runge–Kutta) end-step approximation be
\[
T_n(h)=r(hQ_n),\qquad r(z)=\frac{12+6z+z^2}{12-6z+z^2},\qquad h\ge0.
\]

**Theorem (sharp cycle positivity classification).** The matrix \(T_n(h)\) has every column sum equal to one for every \(n\ge2\) and \(h\ge0\). For \(n=2,3\), it is entrywise nonnegative for all \(h\ge0\), and strictly entrywise positive for \(h>0\). For \(n=4\), let \(h_*\) denote the unique positive root of
\[
F(h)=h^4-24h^2-72h-72.
\]
Then \(6.135<h_*<6.136\), more precisely \(h_*=6.13572028261049\ldots\), and
\[
\boxed{\quad T_4(h)\ge0\text{ entrywise if and only if }0\le h\le h_*.\quad}
\]
It is strictly entrywise positive for \(0<h<h_*\). At \(h=h_*\), exactly the four cyclic first-neighbor entries vanish, while all other entries remain positive. For every \(h>h_*\), exactly those four first-neighbor entries are negative.

More generally, writing the unique circulant decomposition \(T_n(h)=\sum_{j=0}^{n-1}c_{n,j}(h)P_n^j\), for every fixed \(n\ge2\) one has the **sharp all-dimension large-step law**
\[
\boxed{\quad c_{n,j}(h)=\mathbf1_{\{j=0\}}+\frac{6(2j-n+1)}{nh}+O_n(h^{-2})\quad(h\to\infty).\quad}
\]
In particular, \(\lim_{h\to\infty}h c_{n,1}(h)=6(3-n)/n<0\) for every \(n\ge4\). Thus **four states are the minimum number within the directed cycle family for which a sufficiently large Padé step destroys Markov positivity**, and this happens despite exact conservation of probability mass. For \(n\ge4\) the theorem makes no claim that all sufficiently small steps preserve positivity; that property can fail at higher dimensions.

## Assumptions and scope

Everything is over exact real arithmetic. The integer \(n\) is at least two; the directed cycle has uniform positive transition rate one and one outgoing edge per state; \(h\) is the dimensionless step length. For physical transition rate \(\lambda>0\), replace \(h\) throughout by \(\lambda h\). The generator acts on **column** probability vectors, so its columns sum to zero. Entrywise \(T\ge0\) means all matrix entries are nonnegative, distinct from spectral or semigroup positivity. The assertion about four states is a minimality statement **within this particular cyclic family**, not among arbitrary generators or arbitrary integrators.

The exact semigroup is positive because
\[
e^{hQ_n}=e^{-h}\sum_{k=0}^{\infty}\frac{h^k}{k!}P_n^k,
\]
and every cyclic residue class appears with strictly positive weight for \(h>0\).

## Proof

**Well-definedness and mass conservation.** The denominator of \(r\) is \(12-6z+z^2\), with zeros \(3\pm i\sqrt3\). The eigenvalues of \(Q_n\) are \(\omega-1\), with \(\omega^n=1\), and lie in the closed left half-plane. Thus the denominator matrix is invertible for all \(h\ge0\). Since \(\mathbf1^T Q_n=0\) and \(r(0)=1\), we have \(\mathbf1^T T_n(h)=\mathbf1^T\). Moreover, \(P_n\) commutes with the numerator and denominator of \(T_n\), so \(T_n\) is circulant.

**Two and three states.** In the representation \(T_n=\sum_jc_{n,j}P_n^j\), direct reduction modulo \(P_n^n=I_n\) yields
\[
(c_{2,0},c_{2,1})=\frac{(h^2+3,\ 3h)}{h^2+3h+3}
\]
and
\[
(c_{3,0},c_{3,1},c_{3,2})=
\left(
\frac{h^2-2h+4}{h^2+2h+4},
\frac{8h}{(h+2)(h^2+2h+4)},
\frac{4h^2}{(h+2)(h^2+2h+4)}
\right).
\]
The denominators are positive for \(h\ge0\) and \(h^2-2h+4=(h-1)^2+3>0\), proving the claims for these dimensions.

**Four states.** Define the positive denominator
\[
D(h)=2(h^2+3h+3)(h^4+6h^3+18h^2+36h+36).
\]
Reducing the Padé rational function modulo \(P_4^4=I_4\) gives the exact coefficients
\[
\begin{aligned}
c_{4,0}(h)&=\frac{2h^6+9h^5+6h^4+72h^2+216h+216}{D(h)},\\
c_{4,1}(h)&=\frac{-3h(h^4-24h^2-72h-72)}{D(h)},\\
c_{4,2}(h)&=\frac{3h^2(h^3+12h^2+36h+36)}{D(h)},\\
c_{4,3}(h)&=\frac{9h^3(h+2)^2}{D(h)}.
\end{aligned}
\]
All four are real and sum to one. For \(h>0\), the coefficients other than \(c_{4,1}\) are strictly positive. The polynomial \(F(h)=h^4-24h^2-72h-72\) has exactly one positive root: its nonzero coefficient signs have one variation, while \(F(0)<0\) and \(F(h)\to\infty\). Exact rational substitution gives \(F(6.135)<0<F(6.136)\). Consequently \(c_{4,1}\) changes once from positive to negative, exactly at \(h_*\). Circulant symmetry means its four copies are precisely the first-neighbor positions; all other entries stay strictly positive for every positive step. This proves the full four-state positivity interval, including both endpoints.

**Large-step law in all dimensions.** Set \(U_n=n^{-1}\sum_{j=0}^{n-1}P_n^j\). On its complementary invariant subspace, \(Q_n\) is invertible. The explicit group inverse is
\[
G_n=\sum_{j=0}^{n-1}\frac{2j-n+1}{2n}P_n^j,
\qquad Q_nG_n=G_nQ_n=I_n-U_n,\quad G_nU_n=0.
\]
Indeed, for \(j\ge1\), the coefficient of \(P_n^j\) in \((P_n-I_n)G_n\) equals \(-1/n\), while the coefficient of \(I_n\) equals \((n-1)/n\), and the sum of coefficients of \(G_n\) vanishes. Hence \(G_n\) is exactly the inverse of \(Q_n\) on the zero-sum subspace and zero on the stationary subspace.

For nonzero \(z\) tending to infinity,
\[
r(z)=1+\frac{12}{z}+O(z^{-2}).
\]
Because a cyclic permutation is unitarily diagonalizable, applying this expansion on its finitely many nonstationary Fourier modes and applying \(r(0)=1\) on the stationary mode gives the matrix expansion
\[
T_n(h)=I_n+\frac{12}{h}G_n+O_n(h^{-2})
\]
in any matrix norm. Reading off the coefficient of each \(P_n^j\) proves the stated formula. At \(j=1\), its coefficient is \(6(3-n)/n\), which is strictly negative for \(n\ge4\). Every such directed cycle therefore has a negative first-neighbor Padé transition entry for all sufficiently large \(h\), even while \(e^{hQ_n}\) is positive. Combined with unconditional positivity for \(n=2,3\), this establishes minimality within the cycle family.

## Verification

Run `python artifacts/verify_cycle_pade.py` with the SymPy version described by `requirements.txt`. The script verifies the exact symbolic coefficients for \(n=2,3,4\), circulant symmetry and mass conservation, the exact positive-root count and rational bracket, the group-inverse identity for \(2\le n\le14\), direct symbolic large-step limits for \(2\le n\le6\), and selected rational step lengths on the four-cycle. It reports `CHECKS_PASSED 118`. The proof above, not the finite computational sample, establishes the quantification over every dimension and every real step length. The verifier itself is complete and self-contained modulo its declared SymPy dependency.

One useful consequence for the four-cycle is that a scaling-and-squaring implementation \(T_4(h/2^s)^{2^s}\) preserves nonnegativity and mass when \(s\) is a nonnegative integer with \(h/2^s\le h_*\), since products of nonnegative column-stochastic matrices retain those properties. This is a sufficient design condition; no necessity assertion is made for the squared method.

## Relationship to prior work

Blanes, Kopylov and Seydaoğlu (2024) investigate efficient scaling and squaring with classical and diagonal Padé approximants to matrix exponentials; the inspected preprint's computational cost, Lie-group preservation, and error analysis do not derive an entrywise positivity threshold for a finite cyclic Markov generator. It motivates studying what Padé structure preserves beyond algebraic invariants.

Zappavigna, Colaneri, Kirkland and Shorten (2012) already show that diagonal Padé maps need not preserve positivity, even at arbitrarily small steps, using a nilpotent nonnegative shift and a related Hurwitz Metzler construction. Neither that obstruction nor the known general zero absolute-monotonicity radius directly supplies the exact four-state **conservative irreducible cycle** horizon or the critical-large-step group-inverse sign law proved here. A separate previously published result on an eight-state pure-birth Markov generator proves a sharp small-step dimension barrier and a different stochasticity window; it does not imply this four-cycle large-step classification.

Itkin and Kazbek (2026) discuss eventual positivity of rational maps when the large-argument value \(r(\infty)\) falls in specified strict ranges. The inspected abstract covers \(0\le r(\infty)<1\) and \(r(\infty)<0\); the present diagonal Padé case has the boundary value \(r(\infty)=1\). Full-text comparison with that recent preprint could not be completed, so potential specialized overlap remains a publication-priority risk.

## Limitations

This is a theorem about the diagonal \([2/2]\) Padé map at the end of a linear fourth-order Gauss–Legendre step and the uniform directed cycle generators only. It does not prove positivity of internal Runge–Kutta stages, unconditional positivity for arbitrary finite Markov generators, an all-step positivity interval for every dimension greater than four, accuracy superiority, numerical roundoff behavior, or sharp scaling-and-squaring cost. At odd \(n\), the large-step leading coefficient for one opposite-cycle index can vanish, so the displayed first-order asymptotic alone does not determine that entry's eventual sign. The number \(h_*\) is exact as an algebraic root; its decimal expansion is informational only. Scientific peer review and independent validation have not been performed.

## References

1. Sergio Blanes, Nikita Kopylov, Muaz Seydaoğlu, *Efficient scaling and squaring method for the matrix exponential*, arXiv:2404.12789, first submitted 2024-04-19. https://arxiv.org/abs/2404.12789
2. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, *Essentially Negative News About Positive Systems*, Linear Algebra and its Applications 436 (2012), 3425–3442. https://doi.org/10.1016/j.laa.2011.12.021 ; full text https://www.hamilton.ie/skirkland/pade_paper_final_end.pdf
3. *Eight-state barrier for Markov positivity of the [2/2] Padé map*, previously published research record, 2026-09-20. https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab
4. Andrey Itkin, Rakhymzhan Kazbek, *Diagonal Frog meets ADI: trading matrix exponentials for rational maps in the Fokker--Planck equation*, arXiv:2608.22703, first submitted 2026-08-24. https://arxiv.org/abs/2608.22703
