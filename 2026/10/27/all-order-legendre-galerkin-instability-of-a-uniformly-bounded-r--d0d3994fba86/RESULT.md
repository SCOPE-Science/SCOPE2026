# All-order Legendre–Galerkin instability of a uniformly bounded random Hamiltonian oscillator

## Finding
For a uniformly bounded family of conservative two-dimensional random linear Hamiltonian systems, **every** finite-order exact Legendre stochastic Galerkin (SG) truncation admits exponentially growing coefficient solutions. The explicit all-order lower certificate
\[
\alpha(\mathcal A_s(b))\ge \frac{bs}{4s^2-1}>0
\]
holds for every integer \(s\ge1\), although each parameter-frozen exact flow is uniformly bounded. With the same basis, evaluating stochastic products using the \(s\)-node Gauss–Legendre quadrature instead produces a coefficient flow that is uniformly bounded in both time and polynomial degree. The distinction is a single rank-one quadrature-boundary term.

## Assumptions and scope
Let \(\theta\sim\mathrm{Unif}[-1,1]\) be a random parameter fixed throughout time, and fix \(0<b<1\). Let
\[
J(\theta)=\theta\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
Q(\theta)=\begin{pmatrix}1+b\theta&0\\0&1-b\theta\end{pmatrix},
\qquad \dot x(t,\theta)=J(\theta)Q(\theta)x(t,\theta).
\]
For each parameter value, \(Q(\theta)\) is positive definite. Its energy \(H_\theta(x)=\tfrac12 x^{\mathsf T}Q(\theta)x\) is conserved, because \(J(\theta)\) is skew-symmetric. Thus \(\|x(t,\theta)\|_2\le\sqrt{(1+b)/(1-b)}\,\|x(0,\theta)\|_2\) for all \(t\in\mathbb R\), including the zero-frequency realization.

For an arbitrary integer \(s\ge1\), let \(\phi_j(\theta)=\sqrt{2j+1}\,P_j(\theta)\), \(0\le j<s\), be orthonormal with respect to \(\mathbb E[\cdot]\). Represent both state components by these polynomials and apply **exact** stochastic Galerkin projection. Let
\[
(T_s)_{ij}=\mathbb E[\theta\phi_i\phi_j],\quad
(U_s)_{ij}=\mathbb E[\theta^2\phi_i\phi_j],\quad
\mathcal A_s=\begin{pmatrix}0&-T_s+bU_s\\T_s+bU_s&0\end{pmatrix}.
\]
The spectral abscissa \(\alpha(A)\) is the maximum real part of its complex eigenvalues. The alternative \(s\)-node Gauss discretization means replacing the above exact expectations with the Gauss–Legendre quadrature rule of \(s\) nodes, without changing the polynomial basis or the time differential equation.

## Proof
The normalized Legendre recurrence is
\[
\theta\phi_j=a_{j+1}\phi_{j+1}+a_j\phi_{j-1},\quad
a_j=\frac{j}{\sqrt{4j^2-1}}\ (j\ge1),\qquad a_0=0.
\]
Consequently \(T_s\) is the symmetric tridiagonal Jacobi matrix with \((T_s)_{j,j+1}=a_{j+1}\). Squaring the recurrence before projection accounts for the one basis function that leaves and re-enters the truncated space, yielding the exact rank-one identity
\[
U_s=T_s^2+a_s^2 e_{s-1}e_{s-1}^{\mathsf T},\qquad
(U_s)_{jj}=a_j^2+a_{j+1}^2.
\]
Let \(D_s=\operatorname{diag}(1,-1,1,-1,\ldots)\). By parity, \(D_sT_sD_s=-T_s\) and \(D_sU_sD_s=U_s\). Put \(B_s=-T_s+bU_s\) and \(K_s=B_sD_s\); then \(T_s+bU_s=D_sB_sD_s\). Conjugation of \(\mathcal A_s\) by the orthogonal matrix \(\operatorname{diag}(I_s,D_s)\) gives
\[
\begin{pmatrix}0&K_s\\K_s&0\end{pmatrix},
\]
which is further orthogonally similar to \(\operatorname{diag}(K_s,-K_s)\). Hence its spectrum is symmetric under negation.

Since \(T_s\) has zero diagonal, a telescoping alternating sum gives
\[
\operatorname{tr}K_s
=b\sum_{j=0}^{s-1}(-1)^j(a_j^2+a_{j+1}^2)
=(-1)^{s-1}b a_s^2
=(-1)^{s-1}\frac{bs^2}{4s^2-1}.
\]
The sum of real parts of the \(s\) eigenvalues of \(K_s\) equals this nonzero real number. Thus one eigenvalue has \(|\operatorname{Re}\lambda|\ge |\operatorname{tr}K_s|/s\), and the sign-symmetric spectrum of \(\mathcal A_s\) proves
\[
\alpha(\mathcal A_s)\ge\frac{bs}{4s^2-1}>0.
\]
For instance, \(\alpha(\mathcal A_1)=b/3\) and \(\alpha(\mathcal A_2)=2b/15\) for \(0<b<1\). A positive real spectral part implies that the autonomous real coefficient ODE has at least one real initial state with exponentially unbounded evolution.

For the \(s\)-point Gauss–Legendre rule, triple products with one \(\theta\) are integrated exactly; the discrete multiplication-by-\(\theta\) operator is still \(T_s\). Its eigenvalues are the distinct Gaussian nodes \(\tau_1,\ldots,\tau_s\in(-1,1)\). The quadrature evaluation of the \(\theta^2\) product is precisely \(\widetilde U_s=T_s^2\), not \(U_s\). After an orthogonal eigenbasis transformation of \(T_s\), the quadrature-based generator becomes the direct sum, over \(\tau_j\), of the original \(2\times2\) matrices
\[
\tau_j\begin{pmatrix}0&-(1-b\tau_j)\\1+b\tau_j&0\end{pmatrix}.
\]
Each such block conserves the positive quadratic energy with weights \(1+b\tau_j\) and \(1-b\tau_j\). Uniform positive-definiteness proves that its propagator and hence the full orthogonally conjugated coefficient propagator have Euclidean norm at most \(\sqrt{(1+b)/(1-b)}\), for all \(s\ge1\) and \(t\in\mathbb R\). This also proves that the rank-one correction is the only difference between the exact and Gaussian-product matrices.

## Verification
The theorem is proved analytically for **all** \(s\ge1\); finite checks are not treated as an all-order argument. The accompanying standard-library script `verify.py` uses exact fractions in the equivalent unnormalized Legendre basis, checks the three-term recurrence, parity identities, alternating trace, rank-one boundary identity, and the two-dimensional test over \(1\le s\le50\). Run `python3 verify.py` from the directory containing the script. Its expected terminal marker is `VERIFY_OK`.

## Relationship to prior work
Pulch and Sète (2023) explain why naive stochastic Galerkin projection of an original parameter-dependent port-Hamiltonian representation need not preserve its product structure and motivate prior transformations. The present example gives an explicit all-polynomial-orders instability bound for the untransformed generator plus a same-order Gauss-collocation contrast. Pulch and Augustin (2017) previously demonstrated instability of Galerkin projections of stable uncertain systems, without the stated all-order conservative planar certificate. Manfredi, De Zutter and Vande Ginste (2018) derive approximate factorization between Galerkin and Gaussian collocation, but their matrix relation does not itself establish this spectral sign law. Pasini and Sahai (2013) establish long-time inadequacy of finite chaos representations for an uncertain harmonic oscillator; long-time approximation error does not imply the present positive spectral abscissa or the exact quadrature stability distinction.

## Limitations
The uncertainty is a **time-independent** random parameter, not stochastic temporal forcing. This is an existential instability statement for coefficient initial data, not instability of every Galerkin solution. It addresses exact projection and a specific Gaussian quadrature replacement of the same degree; it does not show that exact finite-time polynomial-chaos approximations fail as the degree grows. The positive abscissa lower bound decays with \(s\). It does not provide a general instability criterion for all Hamiltonian families, distributions or structure-preserving transformed Galerkin schemes. Unindexed literature, particularly older stochastic oscillator and Galerkin stability papers for which only abstracts were accessible, might contain a more specific equivalent statement.

## References
1. R. Pulch and O. Sète, *Stochastic Galerkin method and port-Hamiltonian form for linear first-order ordinary differential equations*, arXiv:2308.07087v1 (2023), https://arxiv.org/abs/2308.07087.
2. R. Pulch and V. Augustin, *Stability preservation in stochastic Galerkin projections of dynamical systems*, arXiv:1708.00958 (2017), https://arxiv.org/abs/1708.00958.
3. P. Manfredi, D. De Zutter and D. Vande Ginste, *On the relationship between the stochastic Galerkin method and the pseudo-spectral collocation method for linear differential algebraic equations*, Journal of Engineering Mathematics 108 (2018), https://doi.org/10.1007/s10665-017-9909-7.
4. J. M. Pasini and T. Sahai, *Polynomial chaos based uncertainty quantification in Hamiltonian, multi-time scale, and chaotic systems*, arXiv:1307.0065 (2013), https://arxiv.org/abs/1307.0065.
5. R. Pulch, *Stability-preserving model order reduction for linear stochastic Galerkin systems*, https://doi.org/10.1186/s13362-019-0067-6 (2019).
