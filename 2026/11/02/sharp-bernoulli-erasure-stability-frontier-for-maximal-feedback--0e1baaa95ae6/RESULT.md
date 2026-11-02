# Sharp Bernoulli-erasure stability frontier for maximal-feedback EControl

## Finding

For the scalar objective \(f(x)=x^2/2\), consider EControl with exact gradients, feedback coefficient \(\eta=1\), fixed model step \(\gamma>0\), and an independently resampled erasure compressor \(\mathcal C_t(v)=B_tv\), where \(B_t\) is Bernoulli with success probability \(q\in(0,1]\). The complete three-state iteration is exponentially stable in mean square **if and only if**

\[
q>\frac23,\qquad 0<\gamma<\gamma_*(q),\qquad
\gamma_*(q)=\frac{2(6q-4)}{8-7q+\sqrt{(8-7q)^2+4(1-q)(6q-4)}}.
\]

Here *complete-state mean-square stability* means \(\mathbb E[x_t^2+e_t^2+h_t^2]\to0\) for every deterministic initial state, with a uniform geometric bound. When \(0<q<1\) and these inequalities fail, every nonzero deterministic initial state fails to converge even in the primal mean square \(\mathbb E[x_t^2]\). Outside the stable region the second-moment operator has spectral radius strictly greater than one, except at the positive-step boundary \(\gamma=\gamma_*(q)\), where it has spectral radius one. In particular, **if \(q\le2/3\), no positive step size yields primal mean-square convergence**, even with the gradient-consistent initialization \(e_0=0\) and \(h_0=x_0\ne0\).

At \(q=1\) the formula gives the ordinary gradient-descent boundary \(\gamma_*(1)=2\). At \(q=3/4\), the sharp threshold is \((\sqrt{129}-11)/2\approx0.178908\). Close to the critical erasure rate, \(\gamma_*(q)\sim(9/5)(q-2/3)\) as \(q\downarrow2/3\).

## Assumptions and scope

The objective is the deterministic, one-dimensional strongly convex quadratic \(f(x)=x^2/2\), and its gradient is evaluated exactly as \(g_t=x_t\). At every iteration, independently of all previous steps, a binary random variable \(B_t\) equals one with probability \(q\) and zero otherwise. The compressor satisfies \(\mathbb E|\mathcal C_t(v)-v|^2=(1-q)|v|^2\), so it is a contractive (generally biased) compressor with contraction parameter \(q\).

Starting from any deterministic \((x_0,e_0,h_0)\in\mathbb R^3\), define

\[
\begin{aligned}
\Delta_t&=B_t(e_t+x_t-h_t),\\
x_{t+1}&=x_t-\gamma(h_t+\Delta_t),\\
e_{t+1}&=e_t+x_t-h_t-\Delta_t,\\
h_{t+1}&=h_t+\Delta_t.
\end{aligned}
\]

This is the one-dimensional specialization of the EControl update with maximal feedback \(\eta=1\). The result concerns the exact-arithmetic, independent-erasure iteration. It does not assert instability for the feedback-regulated variant \(\eta<1\), or for deterministic Top-\(k\) sparsification.

## Proof

**1. Exact second-moment operator.** Write \(v_t=(x_t,e_t,h_t)^\mathsf T\). Conditional on an erasure or delivery, respectively, the update matrices are

\[
A_0=\begin{pmatrix}1&0&-\gamma\\1&1&-1\\0&0&1\end{pmatrix},\qquad
A_1=\begin{pmatrix}1-\gamma&-\gamma&0\\0&0&0\\1&1&0\end{pmatrix}.
\]

For a symmetric matrix \(S\), let \(\mathcal T_{q,\gamma}(S)=(1-q)A_0SA_0^\mathsf T+qA_1SA_1^\mathsf T\). The covariance \(S_t=\mathbb E[v_tv_t^\mathsf T]\) satisfies \(S_{t+1}=\mathcal T_{q,\gamma}(S_t)\). Represent this operator by a \(6\times6\) matrix \(M(q,\gamma)\) in the symmetric-entry coordinates \((S_{11},S_{12},S_{13},S_{22},S_{23},S_{33})\). Direct expansion gives the exact polynomial identity

\[
\boxed{\det(I_6-M(q,\gamma))=\gamma q^2\left[(q-1)\gamma^2+(7q-8)\gamma+6q-4\right].}
\tag{1}
\]

An exact symbolic derivation and finite-step independent enumerations are supplied in `verify.py`.

**2. Instability from the determinant.** The linear operator \(\mathcal T_{q,\gamma}\) preserves the cone of positive-semidefinite matrices. Its spectral radius \(\rho\) is therefore a nonnegative real eigenvalue. When \(0<q\le2/3\), the bracket in (1) is strictly negative for every \(\gamma>0\); it is also negative for \(q>2/3\) once \(\gamma\) exceeds its unique positive root \(\gamma_*(q)\). In either case \(\det(I_6-M)<0\), which forces a real eigenvalue of \(M\) to exceed one (complex-conjugate eigenvalue pairs contribute positive factors to the determinant). Hence \(\rho>1\). At \(\gamma=\gamma_*(q)\), (1) gives an eigenvalue equal to one.

**3. Existence of a stable interval when \(q>2/3\).** At \(\gamma=0\), set \(y_t=h_t-x_t\). The primal coordinate \(x_t\) is constant and the internal pair \(u_t=(e_t,y_t)^\mathsf T\) evolves by

\[
F_0=\begin{pmatrix}1&-1\\0&1\end{pmatrix},\qquad
F_1=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
\]

For \(q>2/3\), the symmetric matrix

\[
P=\frac1{q(3q-2)}\begin{pmatrix}
2q^2&2q(q-1)\\2q(q-1)&2q^2-3q+2
\end{pmatrix}
\]

is positive definite: its leading diagonal entry is \(2q/(3q-2)>0\) and \(\det P=2q/(3q-2)^2>0\). Direct multiplication shows

\[
P-(1-q)F_0^\mathsf TPF_0-qF_1^\mathsf TPF_1=I_2.
\tag{2}
\]

Thus the internal pair is geometrically mean-square stable. Consequently the \(\gamma=0\) full covariance operator has a simple eigenvalue one (the conserved \(x^2\) direction), while all remaining eigenvalues lie strictly inside the unit disk: the internal covariance block contracts by (2), and the mixed \(x\)-internal block contracts by Cauchy–Schwarz. Differentiating the simple eigenvalue at zero gives \(-2\), since the conserved right state has \((x,e,h)=(1,0,1)\) and its first-step primal square is \((1-\gamma)^2\). Therefore \(\rho(M(q,\gamma))<1\) for all sufficiently small \(\gamma>0\).

The spectral radius is continuous in \(\gamma\). Because the covariance operator preserves the positive-semidefinite cone, its spectral radius is always itself a real eigenvalue. It cannot cross from less than one to at least one without first attaining the positive eigenvalue one. By (1), no such crossing is possible on \((0,\gamma_*(q))\). This proves stability throughout that interval. Equation (1) and Step 2 prove its sharpness. For \(q=1\), the compressor is the identity and the update reduces after at most two steps to standard scalar gradient descent, giving the same criterion \(0<\gamma<2\).

**4. Why this is a primal-error, not merely an auxiliary-state, obstruction.** For \(0<q<1\) and \(\gamma>0\), \(A_0-I\) is nilpotent with one Jordan block of length three. Its only proper nonzero invariant subspaces are \(\operatorname{span}\{(0,1,0)^\mathsf T\}\) and the plane \(\{h=0\}\). Both fail to be invariant under \(A_1\), because \(A_1(0,1,0)^\mathsf T=(-\gamma,0,1)^\mathsf T\). The matrices therefore have no common proper nonzero invariant subspace.

By the positive-cone Perron theorem, the adjoint moment operator has a nonzero positive-semidefinite eigenmatrix \(L\) at its spectral radius \(\rho\). The kernel of \(L\) is invariant under both \(A_0\) and \(A_1\), so irreducibility forces \(L\) to be strictly positive definite. Hence every nonzero deterministic initial state satisfies

\[
\mathbb E[v_t^\mathsf TLv_t]=\rho^t v_0^\mathsf TLv_0.
\tag{3}
\]

At the boundary, (3) prevents full-state decay; beyond it, it forces exponential full-state growth. Meanwhile

\[
\mathbb E[x_{t+1}^2]=(1-q)\mathbb E[(x_t-\gamma h_t)^2]+q\mathbb E[((1-\gamma)x_t-\gamma e_t)^2].
\tag{4}
\]

If \(\mathbb E[x_t^2]\to0\), both square terms in (4) vanish and therefore \(\mathbb E[h_t^2],\mathbb E[e_t^2]\to0\), contradicting (3) when \(\rho\ge1\). If \(\rho>1\), bounded primal second moments would also force bounded auxiliary second moments through (4), again contradicting (3). Thus outside the stable range, for every nonzero initial state and \(0<q<1\), the primal error does not decay in mean square, and for \(\rho>1\) its second moment has unbounded limsup.

## Verification

The supplementary `verify.py` reconstructs both update matrices, builds the \(6\times6\) second-moment map from its defining action, factors (1) symbolically, verifies (2) and \(\det P\) exactly, and compares the matrix recurrence with independent enumeration of every erasure path for four rational parameter pairs over horizons zero through six (28 full covariance identities). It also evaluates numerical spectral radii on either side of the theoretical boundary, checks the positive-root identity, and checks the uncompressed endpoint. Run `python verify.py` with Python 3, SymPy and NumPy installed. These finite checks corroborate, but do not replace, Steps 2–4.

## Relationship to prior work

Gao, Islamov and Stich introduced EControl, including a feedback coefficient \(\eta\) and the same three-state algorithm; their Appendix C documents initialization-sensitive divergence at \(\eta=1\) with Top-1 compression in a different multidimensional example. Their general convergence guarantees use regulated feedback and do not state the exact independent-erasure critical probability or step-size curve above. Earlier EF21 work uses a different stored-gradient mechanism. A subsequent analysis by Thomsen, Taylor and Dieuleveut studies error-feedback performance, including an empirically optimal EControl feedback choice \(\eta=0\), but does not give the Bernoulli maximal-feedback boundary (1)–(4).

A separate scalar Bernoulli result for *classical* error-feedback sparsification gives a sharp geometric-delay step restriction \(0<s<2q/(2-q)\). It is not this three-state EControl recurrence; neither its model nor its stated restriction implies the present \(q>2/3\) impossibility for arbitrarily small positive steps. The general theory of positive linear maps and quadratic Lyapunov functions is standard. The assessed claim is the exact algorithm-specific stability phase diagram and the all-initial-state primal obstruction, not a new general method for linear random-system stability.

## Limitations

The result assumes a scalar exact-gradient quadratic, independent Bernoulli erasures, maximal feedback \(\eta=1\), and a constant positive step size. It is not a sufficient or necessary guarantee for general nonlinear objectives, multicomponent data, correlated erasures, other compressors, or reduced feedback. The strict positivity of \(q\) and \(\gamma\) is essential. For \(q=1\), the sharp condition is a uniform-all-initial-states stability statement; exceptional initial states can trivially vanish even outside that interval. The proof is an analytic mean-square result and does not assert almost-sure divergence. Publication priority against additional specialized literature is not independently certified.

## References

1. Y. Gao, R. Islamov, S. Stich, *EControl: Fast Distributed Optimization with Compression and Error Control*, arXiv:2311.05645, first posted 2023-11-06, Algorithm 2 and Appendix C. https://arxiv.org/abs/2311.05645
2. P. Richtárik, I. Sokolov, I. Fatkhullin, *EF21: A New, Simpler, Theoretically Better, and Practically Faster Error Feedback*, arXiv:2106.05203, 2021. https://arxiv.org/abs/2106.05203
3. B. Thomsen, A. Taylor, A. Dieuleveut, *A Tight Theory of Error Feedback Algorithms in Distributed Optimization*, arXiv:2605.31594, 2026, §§3–4. https://arxiv.org/abs/2605.31594
