# Exact fluctuation law for noncommuting two-projector randomized implicit Euler

## Finding
For an equiprobable, two-component randomized implicit Euler solver, the finite-step mean and the slow-mode variance are available in closed form. For a fast-eigenmode initial condition, the leading error is a *Gaussian fluctuation entirely in the other, slow eigendirection*. Its positive explicit variance proves sharpness of the root-mean-square temporal order one-half for every nonorthogonal, nonparallel pair of projector directions.

For \(0<c<1\) and \(T>0\), the limiting variance is
\[
V(c,T)=\frac{1-c^2}{4c}\left(e^{-2(1-c)T}-e^{-2(1+c)T}\right)>0.
\]

## Assumptions and scope
Take unit vectors \(u,v\in\mathbb R^2\) with \(u^{\mathsf T}v=c\in(0,1)\), and let \(P_u=uu^{\mathsf T}\), \(P_v=vv^{\mathsf T}\), and \(A=P_u+P_v\). Each independent equiprobable choice \(A_j\) equals \(2P_u\) or \(2P_v\), so \(\mathbb E A_j=A\). The exact differential equation is \(\dot U=-AU\), with initial condition \(U(0)=w_+=(u+v)/\sqrt{2(1+c)}\). Thus \(U(T)=e^{-(1+c)T}w_+\).

For step \(h>0\) the randomized implicit Euler update is \(U_{j+1}=(I+hA_{j+1})^{-1}U_j\), independently for all \(j\). The vector \(w_-=(u-v)/\sqrt{2(1-c)}\) is orthogonal to \(w_+\); \(A w_\pm=(1\pm c)w_\pm\). Expectations are over all independent random choices. No spatial discretization or additive forcing is assumed.

Define
\[
t=\frac{h}{1+2h},\quad m_\pm=1-t(1\pm c),\quad g=t\sqrt{1-c^2},\quad
H=\begin{pmatrix}m_+^2&g^2\\g^2&m_-^2\end{pmatrix}.
\]
The eigenvalues \(\varrho_+>\varrho_->0\) of \(H\) are explicitly
\[
\varrho_\pm=\frac{m_+^2+m_-^2\pm\sqrt{(m_+^2-m_-^2)^2+4g^4}}2.
\]

## Proof
**Resolvent reduction.** Each rank-one projector satisfies \(P^2=P\), so \((I+2hP)^{-1}=I-2hP/(1+2h)\). In the orthonormal basis \((w_+,w_-)\), the sampled operators are \(\begin{psmallmatrix}1+c&\xi\sqrt{1-c^2}\\\xi\sqrt{1-c^2}&1-c\end{psmallmatrix}\) for fair independent signs \(\xi\). Writing \(X_j=\langle U_j,w_+\rangle\) and \(Y_j=\langle U_j,w_-\rangle\), obtain the exact recurrences
\[
X_{j+1}=m_+X_j-\xi_{j+1}gY_j,\qquad
Y_{j+1}=m_-Y_j-\xi_{j+1}gX_j,
\]
with \(X_0=1\), \(Y_0=0\).

**Finite-time exact moments.** Conditioning on the previous step gives \(\mathbb E X_j=m_+^j\), \(\mathbb E Y_j=0\), \(\mathbb E(X_jY_j)=0\), and
\[
\binom{\mathbb E X_{j+1}^2}{\mathbb E Y_{j+1}^2}=H\binom{\mathbb E X_j^2}{\mathbb E Y_j^2}.
\]
Since \(H\) has strictly positive off-diagonal entries, its eigenvalues are distinct. They are positive because \(m_+m_--g^2=1-2t>0\). By the degree-two Cayley--Hamilton formula,
\[
\mathbb E Y_N^2=(H^N)_{21}
=g^2\frac{\varrho_+^N-\varrho_-^N}{\varrho_+-\varrho_-}
\]
for every integer \(N\ge1\), including \(N=1\).

**Moment estimates.** Fix \(T>0\) and take \(h=T/N\). The resolvents are nonexpansive, so \(\mathbb E X_j^2\le1\). Iterating the second-moment recursion yields \(\mathbb E Y_j^2\le jg^2\le C_T h\) for \(j\le N\). Moreover, if \(\Delta X_j=X_j-m_+^j\), martingale orthogonality in the explicit recursion implies
\[
\mathbb E(\Delta X_j)^2
=g^2\sum_{i=0}^{j-1}m_+^{2(j-1-i)}\mathbb E Y_i^2
\le C_T h^2.
\]
Both constants may depend on \(c,T\), but not on \(N\). The deterministic mean satisfies \(m_+^N=e^{-(1+c)T}+O(h)\), because \(t=h+O(h^2)\).

**Limit distribution.** Introduce the deterministic-weight Rademacher sum
\[
\widetilde Y_N=-g\sum_{j=0}^{N-1}\xi_{j+1}
 m_-^{N-1-j}m_+^j.
\]
Replacing \(X_j\) by \(m_+^j\) in the exact expression for \(Y_N\) has mean-square error at most \(g^2\sum_{j=0}^{N-1}\mathbb E(\Delta X_j)^2=O(h^3)\). Thus \((Y_N-\widetilde Y_N)/\sqrt h\to0\) in \(L^2\). Every summand of \(\widetilde Y_N/\sqrt h\) is \(O(\sqrt h)\), and its total variance converges by a Riemann sum to
\[
(1-c^2)\int_0^T e^{-2(1-c)(T-s)}e^{-2(1+c)s}\,ds
=V(c,T).
\]
The independent triangular-array Lindeberg theorem therefore gives \(\widetilde Y_N/\sqrt h\Rightarrow\mathcal N(0,V(c,T))\). The above fast-mode moment estimate and deterministic bias give \((X_N-e^{-(1+c)T})/\sqrt h\to0\) in \(L^2\). Joint convergence follows by Slutsky's theorem.

Finally \(h^{-1}\mathbb E Y_N^2\to V(c,T)\) from the same moment estimates, and the mean-square fast-mode contribution divided by \(h\) tends to zero. The constant is strictly positive for all \(0<c<1\), \(T>0\), establishing sharpness of the root-mean-square one-half convergence rate.

## Verification
The supplied standalone standard-library program at `verification/check.py` checks the exact resolvent identity, enumerates all sign sequences through seven steps for nine distinct rational parameter pairs, tests five moment identities at every step, and checks the limiting squared-error coefficient at 45 numerical parameter/refinement combinations. Run `python verification/check.py` from the extracted package root. These finite checks corroborate the formulas; the all-parameter assertion and the central limit theorem are supplied by the proof above.

## Relationship to prior work
Eisenmann and Stillfjord formulate the randomized implicit operator splitting framework and prove a general strong temporal error estimate of order at least one-half (2022 preprint; 2024 journal publication). Their displayed convergence bounds do not yield the exact finite-step two-mode covariance, the one-direction Gaussian limit, or the positive parameter-dependent sharp constant established here. The familiar rank-one resolvent identity, martingale orthogonality, Cayley--Hamilton identity and triangular-array normal limit are standard proof ingredients, not claimed as novel. Berg, Cohen and Dujardin examine Lie--Trotter numerical splitting for a *stochastic differential equation* with random dispersion, a distinct source of randomness and an unrelated flow.

## Limitations
The result is for homogeneous real two-dimensional linear dynamics, equiprobable independent component sampling, positive nonorthogonal and nonparallel overlap, constant steps, and initialization in the fast eigenmode. It does not assert a Gaussian limit for arbitrary initial conditions, nonlinear problems, other sampling laws, arbitrary spatial discretizations or joint dependence across steps. The original scheme's general strong-rate bound remains a separate result. The literature comparison cannot rule out equivalent formulas buried in specialized random-product literature; independent publication-priority review remains necessary.

## References
1. M. Eisenmann and T. Stillfjord, *A randomized operator splitting scheme inspired by stochastic optimization methods*, arXiv:2210.05375v1 (first public 11 October 2022), https://arxiv.org/html/2210.05375v1; *Numerische Mathematik* **156** (2024), 435–461, https://doi.org/10.1007/s00211-024-01396-w.
2. A. Berg, D. Cohen, and G. Dujardin, *Lie–Trotter splitting for the nonlinear stochastic Manakov system*, arXiv:2010.15679 (2020), https://arxiv.org/abs/2010.15679.
3. The triangular-array Lindeberg–Feller central limit theorem and the Cayley–Hamilton identity are used in their standard forms.
