# Sharp Markovian simplex and single-onset transition for finite-field Weyl mixtures

## Finding

Let \(q=p^r\ge3\) be any prime power and let \(\mathbb F_q\) be its finite field. Consider all \(q+1\) maximal commuting Weyl directions in the two-dimensional finite phase space. Mix the corresponding equal-rate pinching semigroups with a fixed probability vector \(x=(x_1,\ldots,x_{q+1})\). The resulting dynamics has a **complete, sharp CP-divisibility classification**, including its simplex boundary and, when CP-divisibility fails only later, the exact unique onset time.

For positive weights set
\[
 a_j=\frac{1-x_j}{x_j},\qquad A=\sum_{j=1}^{q+1}a_j,\qquad m=\max_j a_j.
\]
Then the mixture is CP-divisible at every finite time if and only if
\[
 \boxed{A\ge q m.}
\]
If \(A<qm\), let \(k\) be an index with \(a_k=m\). There is a unique \(y_*\in(0,1)\) solving
\[
 \boxed{\sum_{j\ne k}\frac{a_j(1+m y_*)}{1+a_jy_*}=(q-1)m.}
\]
The evolution is CP-divisible on its initial interval \([0,t_*]\), where \(t_*=c^{-1}\log(1/y_*)\); at every later time there is a strictly negative canonical decoherence rate. All other rates are at least the rate in direction \(k\). In particular, there can be no recovery to CP-divisibility after onset.

On the boundary of the mixing simplex, support size one gives the original CP-divisible semigroup; every support size between two and \(q\) instead produces a negative canonical decoherence rate at **every** positive time. Thus the entire simplex is classified without excluding its faces.

## Assumptions and scope

A prime power \(q=p^r\ge3\), a common rate \(c>0\), and nonnegative real coefficients \(x_j\) with \(\sum_jx_j=1\) are fixed. The Hilbert space has orthonormal computational basis \(\{|z\rangle:z\in\mathbb F_q\}\). Write \(\chi(z)=\exp(2\pi i\,\operatorname{Tr}_{\mathbb F_q/\mathbb F_p}(z)/p)\). Define the finite-field Weyl operators by
\[
 W_{a,b}|z\rangle=\chi(bz)|z+a\rangle,\qquad (a,b)\in\mathbb F_q^2.
\]
Choose the \(q+1\) one-dimensional \(\mathbb F_q\)-linear subspaces \(L_j\) of \(\mathbb F_q^2\); they partition its nonzero elements. Their Weyl operators commute up to phases, and their adjoint actions commute exactly. For every direction define a pinching channel and a Markovian semigroup:
\[
 T_j(\rho)=\frac1q\sum_{u\in L_j}W_u\rho W_u^\dagger,\qquad
 \Phi_j(t)=e^{-ct}\operatorname{Id}+(1-e^{-ct})T_j.
\]
The family under study is \(\Lambda_x(t)=\sum_jx_j\Phi_j(t)\) for \(t\ge0\). CP-divisibility means that for each \(t\ge s\ge0\) there is a completely positive trace-preserving \(V(t,s)\) with \(\Lambda_x(t)=V(t,s)\Lambda_x(s)\). This is a statement about intermediate maps, not about whether the mixture is a time-homogeneous semigroup.

Every eigenvalue of \(\Lambda_x(t)\) is strictly positive at every finite time: on the nonidentity Weyl operators with indices in \(L_j\), it is \(\lambda_j(t)=x_j+(1-x_j)e^{-ct}\). Consequently the time-local generator exists and is unique for all finite times, even when some weights vanish.

## Proof

**1. Spectral reduction.** The trace pairing \(\operatorname{Tr}_{\mathbb F_q/\mathbb F_p}\) is nondegenerate. The sum of the associated additive character over a one-dimensional field line vanishes unless the tested Weyl label lies in its symplectic orthogonal. In dimension two, each line is its own symplectic orthogonal. Therefore \(T_j(W_v)=W_v\) if \(v\in L_j\) and \(T_j(W_v)=0\) for nonzero \(v\notin L_j\). This proves the preceding expression for \(\lambda_j\), and with \(y=e^{-ct}\) yields
\[
 \frac{\dot\lambda_j(t)}{\lambda_j(t)}=-g_j(t),\qquad
 g_j(t)=\frac{c(1-x_j)y}{x_j+(1-x_j)y}.
\]

**2. Canonical rates and complete positivity.** The unique generator can be expressed in the Weyl adjoint basis as
\[
 \mathcal L_t(\rho)=\sum_{u\ne0}\gamma_u(t)\big(W_u\rho W_u^\dagger-\rho\big).
\]
All \(q-1\) Weyl labels \(u\in L_k\setminus\{0\}\) have the same real rate \(\gamma_k\). Character Fourier inversion, using
\[
 \sum_{v\in L_j\setminus\{0\}}\chi([u,v])=
 \begin{cases}q-1,&u\in L_j,\\-1,&u\notin L_j,\end{cases}
\]
where \([u,v]\) is the field-valued symplectic pairing, gives
\[
 \boxed{\gamma_k(t)=\frac1{q^2}\left[\sum_{j\ne k}g_j(t)-(q-1)g_k(t)\right].}
\]
The displayed Weyl operators form an orthogonal traceless operator basis, so a nonnegative set of coefficients is a GKLS generator and implies CP-divisibility by integration. Conversely, if some \(\gamma_u(t_0)<0\), take the Choi state of \(\operatorname{Id}+h\mathcal L_{t_0}+O(h^2)\); its expectation along the Bell-vector direction indexed by \(u\ne0\) is \(h\gamma_u(t_0)+O(h^2)<0\) for small \(h>0\). Thus CP-divisibility is equivalent to all these rates being nonnegative at every time.

**3. Interior sharp criterion.** If all \(x_j>0\), put \(a_j=(1-x_j)/x_j\) and define \(\phi_y(a)=a/(1+ay)\). We obtain
\[
 \gamma_k(t)=\frac{cy}{q^2}\left[\sum_{j=1}^{q+1}\phi_y(a_j)-q\phi_y(a_k)\right].
\]
Because \(\phi_y\) is increasing, the least rate always occurs at an index where \(a_k=m\). For every \(a_j\le m\),
\[
 \phi_y(a_j)=\frac{a_j}{1+a_jy}\ge\frac{a_j}{m}\,\phi_y(m).
\]
Hence \(A\ge qm\) implies every rate is nonnegative at every time. If \(A<qm\), the coefficient of \(cy/q^2\) in the smallest rate tends to \(A-qm<0\) as \(y\downarrow0\), establishing necessity. This proves the sharp if-and-only-if criterion.

**4. Single-onset theorem.** Suppose \(A<qm\). Divide the expression for the smallest rate by its positive factor \(cy\phi_y(m)/q^2\). The remaining sign is the sign of
\[
 F(y)=\sum_{j\ne k}\frac{a_j(1+my)}{1+a_jy}-(q-1)m.
\]
Here \(F(0)=A-qm<0\), while \(F(1)>0\), as can also be seen from \(\gamma_k(0)=cx_k/q>0\). Moreover
\[
 F'(y)=\sum_{j\ne k}\frac{a_j(m-a_j)}{(1+a_jy)^2}>0.
\]
The inequality is strict because \(A<qm\) forces at least one of the other positive \(a_j\) to be strictly smaller than \(m\). Thus exactly one \(y_*\in(0,1)\) solves \(F(y_*)=0\). Since \(y=e^{-ct}\) decreases in time, the smallest rate stays positive before \(t_*\), is zero at \(t_*\), and is strictly negative afterward. The remaining rates dominate it. This gives the asserted full time classification.

**5. Faces of the simplex.** If exactly one weight is nonzero, the mixture is that semigroup. Otherwise let the support contain \(r\) indices, \(2\le r\le q\), and choose an index \(k\) whose weight is zero. For all \(t>0\) every positive-weight \(j\) has \(g_j(t)<c(1-x_j)\), while each zero-weight direction has \(g_j(t)=c\). Since the number of zero weights is \(q+1-r\),
\[
 q^2\gamma_k(t)=\sum_{x_j>0}g_j(t)-(r-1)c
 < c\sum_{x_j>0}(1-x_j)-(r-1)c=0.
\]
Thus every nontrivial proper face is CP-indivisible at each positive time, while every vertex is CP-divisible.

**6. Critical asymptotics.** For interior points exactly on the sharp boundary \(A=qm\), expand \(\phi_y(a)=a-a^2y+O(y^2)\):
\[
 \gamma_k(t)=\frac c{q^2}\left(qm^2-\sum_j a_j^2\right)e^{-2ct}+O(e^{-3ct}).
\]
The coefficient is strictly positive because all \(a_j>0\), not all equal, and \(\sum_j a_j=qm\); indeed \(\sum_j a_j^2<m\sum_j a_j\). In contrast, at points with \(A>qm\) the least rate has leading term \(c(A-qm)e^{-ct}/q^2\). The equal-weight point has \(a_j=q\), so lies strictly in the CP-divisible region.

**7. An exact qutrit example.** In dimension \(q=3\) use weights \((1/10,3/10,3/10,3/10)\). Then \(a=(9,7/3,7/3,7/3)\), so \(A=16<27=3m\). The onset equation reduces to \(7(1+9y)/(1+7y/3)=18\), with the unique solution \(y_*=11/21\). Hence \(t_*=c^{-1}\log(21/11)\). This explicit delayed transition is neither a boundary-face effect nor a stationary semigroup.

## Verification

The accompanying standalone standard-library Python program `verify.py` independently constructs phase-space lines and finite-field trace characters for dimensions \(q=3,4,5,7\). In the \(q=4\) case it uses \(\mathbb F_4=\mathbb F_2[z]/(z^2+z+1)\), not arithmetic modulo four. The program obtains every canonical rate by direct Fourier summation over all \(q^2-1\) nonidentity Weyl labels and compares it against the closed formula. It additionally checks all signs implied by the sharp criterion, the unique-onset bisection, and boundary-support classification using seeded random weights and multiple times. It passed 182400 direct finite-field character comparisons. These are finite numerical corroborations; the proof establishes the all-prime-power statement independently of the tests.

Reproduce with `python3 verify.py` using Python 3.9 or later; no third-party packages are required. The example's exact transition and the equality-case asymptotic are derived symbolically above and do not depend on numerical tests.

## Relationship to prior work

Xu and Jagadish [1], particularly Section V.B, Eq. (30), and Appendix F, derive the qutrit four-way Weyl decay-rate formula and show examples of uniform-weight CP-divisibility, a neighborhood of it, and sufficiently nonuniform non-Markovianity. They also establish sparse-support eternal non-Markovianity. Those expressions are a starting point, not claimed as new. The present finding evaluates the exact necessary-and-sufficient weight region, proves a one-time irreversible CP-divisibility transition outside it, includes every simplex face, and establishes the finite-field result for every prime-power dimension \(q\ge3\). It uses a specific common-rate, field-line model, not arbitrary Weyl maps.

Jagadish, Srikanth, and Petruccione [2] comprehensively analyze the **qubit** three-Pauli semigroup simplex; the qubit classification is prior art, not claimed here. Siudzińska and Chruściński [3] establish general spectral and memory-kernel formulas for generalized Pauli channels, but their results do not assert the present closed mixing-weight boundary and one-onset theorem. Li, Xu, Wang, and Zheng [4] characterize when generalized Pauli channels are time-homogeneous semigroups and their convex decompositions; their stationary spectral condition concerns a different property from CP-divisibility of the present non-semigroup mixture. These comparisons identify the new implication rather than only a title or dimension difference.

## Limitations

The classification assumes a complete symplectic line spread over a finite field, a **common** exponential decay constant, and time-independent mixing weights; it does not extend without additional argument to unequal rates, non-field Weyl spreads, non-invertible channels at finite times, or arbitrary Weyl noise. CP-divisibility and CP-indivisibility concern the Rivas–Huelga–Plenio definition, not all possible information-backflow witnesses. The source's prior qutrit rate calculation is credited; the novelty claim is the evaluated sharp simplex criterion, unique onset, and full prime-power classification. Undiscovered equivalent treatments or implicit consequences of general channel criteria remain possible and have not been ruled out by exhaustive indexing. No independent external verification has occurred.

## References

[1] Wen Xu and Vinayak Jagadish, *Convexity and non-Markovianity of Weyl Maps*, arXiv:2605.23852v1 (first public posting 2026-05-22), Section V.B, Eq. (30), Appendix F; https://arxiv.org/abs/2605.23852.

[2] Vinayak Jagadish, R. Srikanth, and Francesco Petruccione, *Convex Combinations of Pauli Semigroups: Geometry, Measure and an Application*, arXiv:1910.04114; Physical Review A **101**, 062304 (2020), https://arxiv.org/abs/1910.04114.

[3] Katarzyna Siudzińska and Dariusz Chruściński, *Memory kernel approach to generalized Pauli channels: Markovian, semi-Markov, and beyond*, arXiv:1706.10041; Physical Review A **96**, 022129 (2017), https://arxiv.org/abs/1706.10041.

[4] Mao-Sheng Li, Wen Xu, Yan-Ling Wang, and Zhu-Jun Zheng, *Beyond the mixture of generalized Pauli dephasing channels*, arXiv:2309.04903 (2023), https://arxiv.org/abs/2309.04903.
