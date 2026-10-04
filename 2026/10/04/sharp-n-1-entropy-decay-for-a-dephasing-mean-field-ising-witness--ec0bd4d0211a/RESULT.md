# Sharp \(N^{-1}\) entropy decay for a dephasing mean-field Ising witness
## Finding
Consider the finite-dimensional mean-field Lindblad dynamics of Amini and Chalal with one-particle space \(\mathbb C^2\). Let \(X,Y,Z\) be the Pauli matrices and choose
\[
A=JZ\otimes Z,\qquad \widetilde H=0,\qquad L=\sqrt{\gamma}Z,
\]
with \(J\neq0\) and \(\gamma>0\). Start from the faithful product state
\[
m_0^{\otimes N},\qquad m_0=\frac{I+rX}2,\qquad 0<r<1.
\]
Writing \(r_t=r e^{-2\gamma t}\), the nonlinear mean-field solution is \(m_t=(I+r_tX)/2\). The exact \(N\)-body state is
\[
\rho_N(t)=U_N(t)m_t^{\otimes N}U_N(t)^\dagger,
\qquad
U_N(t)=\exp\!\left[-\frac{iJt}N\sum_{1\le i<j\le N} Z_iZ_j\right].
\]
For every integer \(N\ge1\) and every \(t\ge0\), its normalized Umegaki relative entropy from the mean-field product, using natural logarithms, is
\[
\mathfrak H_N(t):=\frac1N D\!\left(\rho_N(t)\middle\|m_t^{\otimes N}\right)
=r_t\operatorname{artanh}(r_t)\left[1-\cos\!\left(\frac{2Jt}N\right)^{N-1}\right].
\]
Consequently, for every fixed \(t>0\),
\[
\lim_{N\to\infty}N\mathfrak H_N(t)
=2r_t\operatorname{artanh}(r_t)J^2t^2>0.
\]
Thus the \(O(N^{-1})\) exponent in the general quantitative entropy estimate of arXiv:2605.06973v1 cannot be replaced, over the same model class, by a uniform \(o(N^{-1})\) rate. The obstruction persists with genuine local dissipation \(\gamma>0\).

The one-site marginal also has the closed form
\[
\rho_N^{(1)}(t)=\frac12\left[I+r_t\cos\!\left(\frac{2Jt}N\right)^{N-1}X\right],
\]
so
\[
\lim_{N\to\infty}N\left\|\rho_N^{(1)}(t)-m_t\right\|_1
=2r_tJ^2t^2.
\]

## Assumptions and scope
The interaction and scaling are exactly those of the cited mean-field Lindblad model: the \(N\)-body Hamiltonian contains \(N^{-1}\sum_{i<j}A_{ij}\), the initial state is exactly chaotic, and the one-body initial state is faithful. The jump \(L=\sqrt{\gamma}Z\) is a valid bounded local Lindblad operator. The result is a sharpness witness for the class-wide exponent. It does not claim a matching lower bound for arbitrary interactions, arbitrary initial states, or arbitrary dissipators, and it does not optimize the explicit constant in the upper bound.

## Proof
First, \(\operatorname{tr}(m_t Z)=0\). Hence the source paper's mean-field self-interaction is
\[
A^{m_t}=\operatorname{tr}_2[(I\otimes m_t)(JZ\otimes Z)]=0.
\]
The limiting nonlinear equation therefore reduces to pure local dephasing. Since
\[
\gamma(ZmZ-m)=-2\gamma\,\frac{rX}2
\]
on states of the form \(m=(I+rX)/2\), its solution is \(m_t=(I+r_tX)/2\) with \(r_t=r e^{-2\gamma t}\).

Second, every \(Z_i\) commutes with every pair operator \(Z_kZ_l\). The Hamiltonian commutator superoperator therefore commutes with all local dephasing superoperators. The exact many-body semigroup factors, giving
\[
\rho_N(t)=U_N(t)m_t^{\otimes N}U_N(t)^\dagger.
\]
For a fixed site \(i\), pair factors not incident to \(i\) commute with \(X_i\). Conjugating through each of the \(N-1\) incident pair rotations and taking the product expectation eliminates every term containing \(Y_i\) or a factor \(Z_j\), because \(\operatorname{tr}(m_tY)=\operatorname{tr}(m_tZ)=0\). Each neighbor contributes the factor \(\cos(2Jt/N)\). Thus
\[
\operatorname{tr}[\rho_N(t)X_i]
=r_t\cos\!\left(\frac{2Jt}N\right)^{N-1}.
\]
Permutation symmetry and the vanishing \(Y\)- and \(Z\)-components give the stated one-site marginal.

Because \(0<r_t<1\),
\[
\log m_t=\alpha_t I+\beta_tX,
\qquad
\beta_t=\frac12\log\frac{1+r_t}{1-r_t}=\operatorname{artanh}(r_t),
\]
for an irrelevant scalar \(\alpha_t\). Unitary invariance gives
\[
\operatorname{tr}[\rho_N(t)\log\rho_N(t)]
=\operatorname{tr}[m_t^{\otimes N}\log m_t^{\otimes N}].
\]
Also
\[
\log(m_t^{\otimes N})=N\alpha_t I+\beta_t\sum_{i=1}^N X_i.
\]
Subtracting the two terms in the Umegaki divergence and using the exact one-site expectation yields
\[
D\!\left(\rho_N(t)\middle\|m_t^{\otimes N}\right)
=N r_t\beta_t\left[1-\cos\!\left(\frac{2Jt}N\right)^{N-1}\right],
\]
which proves the finite-\(N\) identity.

Finally, for fixed \(t\),
\[
\cos\!\left(\frac{2Jt}N\right)^{N-1}
=1-\frac{2J^2t^2}N+O(N^{-2}),
\]
so multiplication by \(N\) gives the positive entropy limit. The trace-norm limit follows from the exact one-site formula because a matrix \(aX/2\) has trace norm \(|a|\).

## Verification
The accompanying `verify.py` independently enumerates computational-basis phase differences for \(2\le N\le10\) and checks the closed one-site expectation against the direct sum for several parameter choices. It then checks the relative-entropy identity through \(\log m_t=\alpha_tI+\operatorname{artanh}(r_t)X\), and numerically verifies convergence of \(N\mathfrak H_N(t)\) and the rescaled one-site trace distance to their analytic limits. These computations corroborate the algebraic proof; finite enumeration is not used as a proof for arbitrary \(N\).

## Relationship to prior work
Amini and Chalal prove an explicit \(O(N^{-1})\) upper bound for normalized quantum relative entropy in the general mean-field Lindblad model, but their theorem and discussion do not establish optimality of that exponent. The present result supplies an exact dissipative witness inside their hypotheses.

The Hamiltonian is, up to an additive scalar and normalization, the standard one-axis-twisting Hamiltonian. Exact collective-spin expectation formulas of cosine-power type are classical in that literature; for example, Zhong, Liu, Ma, and Wang derive such expectations for coherent pure initial states. That known identity is not claimed as new. The new claim is the exact Umegaki-divergence formula for the faithful mixed product under the mean-field scaling, its compatibility with nonzero local dephasing, and the resulting sharpness obstruction for the 2026 entropy theorem.

Carollo and Lesanovsky prove validity of mean-field theory for time-dependent open infinite-range systems and provide finite-size bounds, but the inspected abstract does not state this normalized-relative-entropy identity or an \(N^{-1}\) lower-bound witness. Classical sharp propagation-of-chaos results for interacting diffusions, such as Lacker and Le Flem, concern different stochastic systems and different marginal rates.

## Limitations
The exact factorization uses a commuting dephasing jump and a diagonal Ising interaction; it should not be read as a solution of the general dissipative problem. The result proves sharpness of the exponent over the theorem's model class, not sharpness of the theorem's prefactor. Literature search cannot exclude an equivalent observation hidden under different terminology, and the cosine-power spin expectation itself is known from one-axis-twisting theory.

## References
1. N. H. Amini and S. Chalal, *Quantitative propagation of chaos for Lindblad dynamics*, arXiv:2605.06973v1 (first public 2026-05-07).
2. W. Zhong, J. Liu, J. Ma, and X. Wang, *Quantum Fisher information and spin squeezing in one-axis twisting model*, arXiv:1309.4842v2.
3. F. Carollo and I. Lesanovsky, *Applicability of mean-field theory for time-dependent open quantum systems with infinite-range interactions*, arXiv:2403.17163; Phys. Rev. Lett. 133, 150401 (2024).
4. D. Lacker and L. Le Flem, *Sharp uniform-in-time propagation of chaos*, arXiv:2205.12047.
