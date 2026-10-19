# Quenched fluctuations and a stationary Gaussian slow mode for two-state random metastable Markov cocycles

## Finding

Consider two metastable states with independently redrawn positive transition-rate pairs. The random invariant probability of the left state has an **exact finite-leakage variance and lag covariance**, a rigidity criterion for the absence of environmental fluctuations, and a Gaussian stationary slow-time limit. These statistics quantify a feature not determined by the averaging limit alone: random fluctuations of the invariant *weight itself*, as opposed to fluctuations of a single particle following that invariant law.

**Theorem.** Let \((L_n,R_n)_{n\in\mathbb Z}\) be independent and identically distributed copies of a real random vector satisfying \(0<c\le L_n,R_n\le C<\infty\). The two coordinates of each vector may be dependent. Fix \(0<\varepsilon<1/(2C)\) and define the random row-stochastic matrix

\[
P_n^{\varepsilon}=\begin{pmatrix}1-\varepsilon L_n&\varepsilon L_n\\ \varepsilon R_n&1-\varepsilon R_n\end{pmatrix}.
\]

Let \((X_n^\varepsilon,1-X_n^\varepsilon)\) be its unique stationary pullback random invariant probability vector, indexed so that \((X_{n+1}^\varepsilon,1-X_{n+1}^\varepsilon)=(X_n^\varepsilon,1-X_n^\varepsilon)P_n^\varepsilon\).

Write \(B=L+R\), \(m=\mathbb E B\), \(\theta=\mathbb E R/m\), and \(\sigma^2=\operatorname{Var}(R-\theta B)\), using a generic one-step environment pair. Then, for **every** permissible \(\varepsilon\),

\[
\boxed{\mathbb EX_n^\varepsilon=\theta,\qquad
\operatorname{Var}(X_n^\varepsilon)=
\frac{\varepsilon\sigma^2}{2m-\varepsilon\mathbb E B^2},\qquad
\operatorname{Cov}(X_n^\varepsilon,X_{n+k}^\varepsilon)
=(1-\varepsilon m)^k\operatorname{Var}(X_n^\varepsilon)}
\quad(k\in\mathbb N_0).
\]

The invariant weight is nonrandom at some (equivalently, every) permissible leakage level **if and only if** \(R/(L+R)\) is almost surely constant; equivalently \(\sigma^2=0\). Otherwise its standard deviation has precise order \(\sqrt\varepsilon\), whereas its correlation-memory length has order \(1/\varepsilon\).

For any fixed real times \(t_1,\ldots,t_d\), the vector

\[
\left(\frac{X_{\lfloor t_j/\varepsilon\rfloor}^\varepsilon-\theta}{\sqrt\varepsilon}\right)_{j=1}^{d}
\]

converges in law as \(\varepsilon\downarrow0\) to a centered Gaussian vector with covariance

\[
\boxed{\operatorname{Cov}(Z_s,Z_t)=\frac{\sigma^2}{2m}
\exp(-m|t-s|).}
\]

This is the finite-dimensional distribution law of the stationary Ornstein–Uhlenbeck diffusion \(dZ_t=-mZ_t\,dt+\sigma\,dW_t\). If \(\sigma^2=0\) this is the identically zero process. No path-space weak convergence is asserted.

**Nontrivial exact example.** If the environment independently takes the two pairs \((L,R)=(1,2)\) and \((3,1)\), each with probability \(1/2\), then \(m=7/2\), \(\theta=3/7\), \(\sigma^2=25/49\), and

\[
\boxed{\operatorname{Var}(X_n^\varepsilon)=
\frac{50\varepsilon}{49(14-25\varepsilon)},\qquad
\varepsilon^{-1}\operatorname{Var}(X_n^\varepsilon)\longrightarrow\frac{25}{343}.}
\]

The constant-rate environment \((L,R)=(2,3/2)\) has the same averaged rates and the same invariant mean \(3/7\), but its quenched invariant weight is deterministic. Thus the averaging limit cannot determine the fluctuation strength.

## Assumptions and scope

The environment is two-sided, i.i.d. across discrete time, bounded and uniformly strictly positive. Dependence between \(L_n\) and \(R_n\) at one time is allowed. The matrix cocycle is the **finite-state induced Markov model** used in the metastability framework of González-Tokman and Peters; this theorem does **not** assert the same \(\sqrt\varepsilon\) Gaussian fluctuation law for the invariant densities of their underlying interval maps. The law of \((L,R)\) is fixed as \(\varepsilon\) varies. The row-vector normalization, temporal indices, and stationary rather than deterministic initial law are essential.

## Proof

**Existence and recurrence.** Matrix multiplication of the left mass gives the scalar affine recursion

\[
X_{n+1}^\varepsilon=(1-\varepsilon B_n)X_n^\varepsilon+\varepsilon R_n.
\]

Because \(2c\le B_n\le2C\) and \(0<\varepsilon<1/(2C)\), every affine coefficient lies strictly between zero and \(1-2c\varepsilon\). The map preserves \([0,1]\), and products contract uniformly. The pullback limit therefore gives a unique stationary solution measurable with respect to \((L_j,R_j)_{j<n}\); it is independent of the time-\(n\) environment.

**Centered equation.** Set \(Y_n^\varepsilon=X_n^\varepsilon-\theta\) and \(\eta_n=R_n-\theta B_n\). Since \(\mathbb E\eta_n=0\),

\[
Y_{n+1}^\varepsilon=(1-\varepsilon B_n)Y_n^\varepsilon+\varepsilon\eta_n.
\]

Taking expectations and using independence of the current environment gives \(\mathbb EY_n^\varepsilon=0\). For \(v_\varepsilon=\mathbb E(Y_n^\varepsilon)^2\), the mixed term vanishes because \(\mathbb EY_n^\varepsilon=0\), even though \(B_n\) and \(\eta_n\) can be correlated. Thus

\[
v_\varepsilon=\bigl(1-2\varepsilon m+\varepsilon^2\mathbb EB^2\bigr)v_\varepsilon+\varepsilon^2\sigma^2.
\]

Solving gives the stated exact variance. Conditioning on the entire environment through time \(n-1\) gives \(\mathbb E[Y_{n+1}^\varepsilon\mid\mathcal F_n]=(1-\varepsilon m)Y_n^\varepsilon\), where \(\mathcal F_n=\sigma((L_j,R_j):j<n)\). Iteration and stationarity yield the exact covariance for every \(k\ge0\). The strictly positive denominator also proves the zero-variance rigidity criterion.

**Replacing multiplicative noise by a deterministic drift.** Put \(a_\varepsilon=1-\varepsilon m\) and let \(U_n^\varepsilon\) be the unique stationary solution of

\[
U_{n+1}^\varepsilon=a_\varepsilon U_n^\varepsilon+\varepsilon\eta_n,
\qquad U_n^\varepsilon=\varepsilon\sum_{j\ge1}a_\varepsilon^{j-1}\eta_{n-j}.
\]

For the difference \(D_n^\varepsilon=Y_n^\varepsilon-U_n^\varepsilon\) the **exact** recursion is

\[
D_{n+1}^\varepsilon=a_\varepsilon D_n^\varepsilon-\varepsilon(B_n-m)Y_n^\varepsilon.
\]

Current environments are independent of the past; the cross term has expectation zero. Hence the stationary second moment satisfies

\[
\mathbb E(D_n^\varepsilon)^2
=\frac{\varepsilon^2\operatorname{Var}(B)\,v_\varepsilon}
{1-a_\varepsilon^2}=O(\varepsilon^2).
\]

The square-integrable normalized difference \(D_n^\varepsilon/\sqrt\varepsilon\) therefore vanishes in \(L^2\), uniformly over integer \(n\) by stationarity. This step treats the possible same-time correlation between the incoming random rates and the noise without assuming independence between \(B_n\) and \(\eta_n\).

**Gaussian slow-time limit.** The vector of \(U_{\lfloor t_j/\varepsilon\rfloor}^\varepsilon/\sqrt\varepsilon\) is a linear array of independent centered, bounded \(\eta_n\)'s, with each coefficient at most \(\sqrt\varepsilon\). For any finite linear combination, its total squared coefficient is bounded and has a limit; the Lindeberg condition follows since individual terms tend uniformly to zero. Its covariance is exactly

\[
\operatorname{Cov}\left(
\frac{U_n^\varepsilon}{\sqrt\varepsilon},
\frac{U_{n+k}^\varepsilon}{\sqrt\varepsilon}\right)
=\frac{\varepsilon\sigma^2}{1-a_\varepsilon^2}a_\varepsilon^{|k|}.
\]

For \(n=\lfloor s/\varepsilon\rfloor\), \(k=|\lfloor t/\varepsilon\rfloor-\lfloor s/\varepsilon\rfloor|\), this converges to \(\sigma^2e^{-m|s-t|}/(2m)\). The Cramér–Wold and Lindeberg–Feller theorems identify the limiting finite-dimensional Gaussian laws. Since finitely many \(D_n^\varepsilon/\sqrt\varepsilon\) vanish in \(L^2\), the same conclusion holds for the actual invariant weights. The covariance is that of the uniquely stationary Ornstein–Uhlenbeck process. This completes the proof.

## Verification

A standalone Python 3 program, `verify.py`, uses exact rational arithmetic for three finitely supported environment laws and three admissible leakage parameters per law. It checks the one-step matrix recurrence, zero-mean centered innovation, closed mean/variance identities, covariance recursion, and the deterministic-coefficient comparison. Its floating-point tail additionally checks convergence of the covariance kernel at shrinking \(\varepsilon\). The analytical arguments above, not any finite computation, prove the all-parameter moment identities and Gaussian finite-dimensional limit. Run `python3 verify.py` in a directory containing that file.

## Relationship to prior work

González-Tokman and Peters, *Averaging for random metastable systems*, arXiv:2406.09672, Section 1.1 and Remark 5.3, introduce this two-state random Markov cocycle and give its **exact pullback product representation**, along with a deterministic zero-leakage limit for the invariant vector. The transition model and product formula are prior work. The present result extracts an exact nonzero-leakage covariance structure, a rigid no-fluctuation criterion, and a stationary Gaussian second-order scaling law; these do not follow from merely knowing the averaged limit. The published exact product formula makes the computation possible and bounds the originality claim to these evaluated fluctuation consequences.

The same authors' *Jumping for diffusion in random metastable systems*, arXiv:2505.22996, studies jump processes and central-limit diffusion coefficients for **particle observables** of metastable interval systems (Sections 1, 5 and 6). That is a different random variable and limiting procedure from the random invariant probability vector under repeated i.i.d. environments. Dolgopyat and Wright, arXiv:1011.5330, study deterministic interval-map observables and Markov approximations, not this quenched invariant-vector Gaussian law. Standard random-affine-recursion and weighted-array limit theory supply proof techniques, which are not claimed as new.

## Limitations

The theorem only covers i.i.d., uniformly positive bounded rate pairs and a fixed driving law; neither temporally correlated forcing nor rates changing with leakage are addressed. The limit asserted is **finite-dimensional convergence**; a functional tightness argument would be needed for a path-space theorem. The OU law concerns random invariant **weights of the two-state Markov cocycle**, not the positions of individual Markov particles and not the original interval-map invariant density. The exact covariance formula is analytically derivable from the known pullback representation, so the contribution is the explicit evaluated model-specific second-order law and its rigorous Gaussian slow-time interpretation; independently checking earlier generalized random-affine diffusion approximations remains relevant to priority.

## References

1. C. González-Tokman and J. Peters, *Averaging for random metastable systems*, arXiv:2406.09672, first public version 2024-06-14; especially Section 1.1, Remark 5.3, equations (13)–(14). https://arxiv.org/abs/2406.09672
2. C. González-Tokman and J. Peters, *Jumping for diffusion in random metastable systems*, arXiv:2505.22996, 2025; Sections 1, 5 and 6. https://arxiv.org/abs/2505.22996
3. D. Dolgopyat and P. Wright, *The diffusion coefficient for piecewise expanding maps of the interval with metastable states*, arXiv:1011.5330, 2010; relevant deterministic antecedent. https://arxiv.org/abs/1011.5330
