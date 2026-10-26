# Sharp quadratic revival and strict relaxation inequalities for random-transposition quantum shuffles

## Finding

Let \(n\ge3\), let \(C=\binom n2\), and let \(H=C^{-1}\sum_{\tau}R_\tau\) be the normalized transposition-class Hamiltonian acting in the left-regular representation on \(\ell^2(S_n)\). Starting at the identity permutation and combining coherent coupling \(\alpha\ge0\) with dissipative random-transposition rate \(\gamma>0\), let \(p_{\alpha,\gamma}(\cdot,t)\) denote the measured diagonal distribution at a finite observation time \(t\ge0\), and let \(u\) be the uniform measure on \(S_n\). Write \(D_2(p,u)=\sum_g(p(g)-1/n!)^2\).

**Theorem.** The least positive projective period of \(U(s)=e^{-isH}\) equals
\[
T_n=\begin{cases}2\pi,&n=3,\\6\pi,&n=4,\\2\pi\binom n2,&n\ge5.\end{cases}
\]
In particular the period of the normalized transposition walk grows quadratically, not exponentially. For every finite \(t\ge0\),
\[
D_2(p_{\alpha,\gamma}(\cdot,t),u)\le D_2(p_{0,\gamma}(\cdot,t),u),
\]
with equality **if and only if** \(\alpha t\in T_n\mathbb Z\). At every other coherent phase, the inequality is strict. At any resonance, writing \(s=\alpha t=kT_n+\delta\), the squared-distance improvement has the sharp local expansion \(K_n(\gamma,t)\delta^2+O(\delta^4)\) with the strictly positive, explicit coefficient given below.

For a partition \(\lambda\vdash n\), let \(d_\lambda\) be its irreducible dimension and \(c_\lambda=\sum_{(i,j)\in\lambda}(j-i)\) its content sum, using row and column numbering starting at one. Define \(r_\lambda=c_\lambda/C\), \(Q_s(g)=|\langle g|U(s)|e\rangle|^2\), and
\[
\kappa_\lambda(s)=\frac1{d_\lambda}\sum_{g\in S_n}Q_s(g)\chi_\lambda(g).
\]
The full quantitative deficit is
\[
\boxed{\ D_2(p_{0,\gamma},u)-D_2(p_{\alpha,\gamma},u)
=\frac1{n!}\sum_{\lambda\ne(n)}d_\lambda^2e^{-2\gamma(1-r_\lambda)t}\bigl(1-\kappa_\lambda(\alpha t)^2\bigr).\ }
\]
Here \(\kappa_\lambda\in[-1,1]\), and
\[
K_n(\gamma,t)=\frac{2}{Cn!}\sum_{\lambda\ne(n)}d_\lambda^2(1-r_\lambda)e^{-2\gamma(1-r_\lambda)t}>0.
\]
All statements use finite \(t\) and no finite-size approximation.

## Assumptions and scope

Each \(R_\tau\) is the unitary left-regular action of a transposition on \(\ell^2(S_n)\); the transpositions are sampled uniformly, without an identity-hold step. The density matrix obeys the finite-dimensional Lindblad equation
\[
\frac{d\rho}{dt}=-i\alpha[H,\rho]+\gamma\left(\frac1C\sum_\tau R_\tau\rho R_\tau^\dagger-\rho\right),\qquad\rho(0)=|e\rangle\langle e|.
\]
The probability \(p_{\alpha,\gamma}(g,t)=\langle g|\rho(t)|g\rangle\) is measured in the permutation basis. All rates and times are in the normalized generator's units. The inequality compares squared counting-measure \(\ell^2\) distances, **not** the total variation distance. The theorem excludes \(n=2\), whose group has nontrivial center and additional translated point-mass revivals.

## Proof

**1. Factorization and Fourier deficit.** Since \(H\) is central in the group algebra, it commutes with every \(R_\tau\), hence its commutator superoperator commutes with the dissipator. Evolving the initial diagonal density matrix with the dissipator alone yields the continuous-time random-transposition law \(p_{0,\gamma}(t)=e^{\gamma t(H-I)}\delta_e\). The measured coherent-dissipative law therefore factorizes as
\[
p_{\alpha,\gamma}(\cdot,t)=Q_{\alpha t}*p_{0,\gamma}(\cdot,t).
\]
Both factors are central class functions. Fourier transform in the irreducible representation indexed by \(\lambda\) sends \(p_{0,\gamma}\) to \(e^{-\gamma(1-r_\lambda)t}I_{d_\lambda}\) and sends \(Q_s\) to \(\kappa_\lambda(s)I_{d_\lambda}\). Characters of \(S_n\) are real. Plancherel, with the trivial mode removed, gives the displayed deficit formula. The normalized character average satisfies \(|\kappa_\lambda|\le1\) because \(Q_s\) is a probability distribution and \(|\chi_\lambda(g)|\le d_\lambda\). Thus every summand in the deficit is nonnegative.

**2. Exact equality.** At every finite \(t\), all weights \(d_\lambda^2e^{-2\gamma(1-r_\lambda)t}\) are strictly positive. Equality requires \(|\kappa_\lambda(s)|=1\) for every nontrivial \(\lambda\), while \(\kappa_{(n)}(s)=1\). Applying Plancherel directly to \(Q_s\) then yields
\[
\sum_{g\in S_n}Q_s(g)^2=\frac1{n!}\sum_{\lambda\vdash n}d_\lambda^2\kappa_\lambda(s)^2=1.
\]
A probability vector has squared norm one only if it is a point mass. Since \(Q_s\) is conjugacy invariant, its atom must lie in the center of \(S_n\), which is trivial for \(n\ge3\). Thus \(Q_s=\delta_e\). Equivalently \(U(s)|e\rangle\) is a phase multiple of \(|e\rangle\). Because \(U(s)\) is a group-convolution operator, this is equivalent to \(U(s)\) being scalar on the whole regular representation. The converse is immediate. Hence equality occurs exactly at the projective revivals of \(U\).

**3. Least period.** The transposition class sum acts on the irreducible \(\lambda\) as the integer content sum \(c_\lambda\); this follows by summing the Jucys--Murphy operators in a Young seminormal basis, where each contributes the content of its newly inserted cell. As \(c_{(n)}=C\), scalarity requires and is equivalent to
\[
\frac{s}{2\pi C}(C-c_\lambda)\in\mathbb Z\quad\hbox{for all }\lambda\vdash n.
\]
Therefore the minimal positive scalar period is \(2\pi C/g_n\), where \(g_n=\gcd_{\lambda\ne(n)}(C-c_\lambda)\). For \(n=3\) the content sums are \(3,0,-3\), so \(g_3=3\). For \(n=4\) they are \(6,2,0,-2,-6\), so \(g_4=2\). For \(n\ge5\), partitions \((n-1,1)\), \((n-2,2)\), and \((n-3,2,1)\) have gaps \(n\), \(2(n-1)\), and \(3(n-1)\). Their gcd is one, so \(g_n=1\). This proves the stated sharp period for all \(n\ge3\). The trivial mode implies \(U(T_n)=I\), not merely a scalar phase, in these cases.

**4. Sharp quadratic onset.** For small \(\delta\), \(U(\delta)=I-i\delta H+O(\delta^2)\). Since each off-diagonal transposition matrix entry of \(H\) is \(1/C\),
\[
Q_\delta=(1-\delta^2/C)\delta_e+(\delta^2/C)\mu_2+O(\delta^4),
\]
where \(\mu_2\) is the uniform transposition measure. Each component \(Q_\delta(g)\) is even and analytic in \(\delta\), since \(H\) is real symmetric; hence the stated fourth-order remainder is valid. The character transform is \(\kappa_\lambda(\delta)=1-(\delta^2/C)(1-r_\lambda)+O(\delta^4)\). Squaring and substituting in the deficit yields the formula for \(K_n\). At least the \((n-1,1)\) mode has \(r_\lambda<1\), so the coefficient is strictly positive. Periodicity reduces expansions about any integer multiple of \(T_n\) to this calculation.

## Verification

The accompanying `verify.py` independently enumerates partitions and hook dimensions for \(2\le n\le18\), checks all content gcds and the identity \(\sum_{\lambda\vdash n}d_\lambda^2=n!\), and constructs the full left-regular Hamiltonians for \(n=3,4\). It diagonalizes the classical and coherent generators, confirms exact revival and strict/non-strict squared-distance comparisons at prescribed phases, and compares the quadratic coefficient with direct matrix evolution. It reports `PASS 127 finite checks`. These finite tests corroborate but do not replace the all-size representation-theoretic proof.

## Relationship to prior work

He, Hutsalyuk, Mussardo and Stampiggi (arXiv:2609.13387v1) establish the normalized symmetric-group quantum-stochastic model, commuting-factorization/convolution law, and a nonstrict total-variation comparison; Appendix B discusses rational spectral recurrence through character/dimension arithmetic. These are antecedents, not claimed here. For the transposition case, the exact **least** scalar recurrence time is quadratic with two small-size exceptions; in particular, the general LCM/GCD-based period expression in that appendix is not needed and need not be minimal for this special class. The source does not give the squared-distance strictness/equality classification or its positive local curvature. Gerhardt and Watrous (arXiv:quant-ph/0305182v1, Proposition 7) previously establish periodicity for integral class spectra of unnormalized Cayley quantum walks; this directly supplies a known recurrence *upper bound*. It does not identify the least period in the normalized transposition family nor the exact equality times in the dissipative measured law. General convolution contraction and classical character-content integrality are established tools; the asserted contribution is their sharp coupled classification in this natural model.

## Limitations

This theorem fixes the transposition class for both coherent and dissipative terms, starts at a permutation basis vector, and considers finite times. It does not classify strictness in total variation, generic unequal-rate or noncentral Hamiltonians, other conjugacy classes, initial coherent superpositions, or asymptotic mixing-time speedup. The formula is elementary once the central Fourier representation is available; it does not establish literature-wide priority. Finite computations do not establish priority or replace the all-size proof.

## References

1. F. He, A. Hutsalyuk, G. Mussardo and A. Stampiggi, *Quantum Stochastic Walks on the Permutation Group*, arXiv:2609.13387v1 (first public 2026-09-11), especially Section 5, Eq. (68)--(74) and Appendix B. https://arxiv.org/html/2609.13387v1
2. H. Gerhardt and J. Watrous, *Continuous-time quantum walks on the symmetric group*, arXiv:quant-ph/0305182v1 (2003), especially Proposition 7. https://arxiv.org/abs/quant-ph/0305182
3. P. Diaconis and M. Shahshahani, *Generating a random permutation with random transpositions*, Z. Wahrscheinlichkeitstheorie verw. Gebiete 57 (1981), 159--179 (classical transposition background).
