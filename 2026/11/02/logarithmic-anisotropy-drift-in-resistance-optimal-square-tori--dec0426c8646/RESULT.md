# Logarithmic anisotropy drift in resistance-optimal square tori

## Finding
Let \(n\ge3\), \(P,Q,B>0\), and consider the simple toroidal grid \(G_n=C_n\square C_n\). Charge \(P\) per unit horizontal-edge conductance and \(Q\) per unit vertical-edge conductance. Every individual edge conductance is independently nonnegative, the total expenditure is \(B\), and the objective is the sum of all unordered pairwise effective resistances, which has the same minimizers as the trace of the Laplacian pseudoinverse.

There is exactly one globally optimal allocation. Every horizontal edge receives a common positive conductance \(x_n\), and every vertical edge receives a common positive conductance \(y_n\). Put \(t_n=x_n/y_n\), \(t_0=Q/P\), and define, for \(t>0\),
\[
C(t)=\frac1{12}+\frac{1}{2\pi\sqrt t}\left[\gamma+\log\frac{2}{\pi\sqrt{1+t}}-2\sum_{\ell=1}^{\infty}\log\bigl(1-e^{-2\pi\sqrt t\,\ell}\bigr)\right],
\]
\[
\kappa(t)=-4\pi t^{3/2}\left[\frac1{12}-\frac{\sqrt t}{2\pi(1+t)}-2\sum_{\ell=1}^{\infty}\frac{\ell}{e^{2\pi\sqrt t\,\ell}-1}\right].
\]
Here \(\gamma\) is Euler's constant; both series converge exponentially for fixed \(t>0\). For fixed \(P,Q,B\),
\[
\boxed{\ t_n=\frac QP+\frac{\kappa(Q/P)}{\log n}+o\!\left(\frac1{\log n}\right)\quad(n\to\infty).\ }
\]
Thus the limiting directional conductance ratio is the inverse price ratio, with a generally nonzero logarithmic finite-size correction.

With \(L_n\) the optimally weighted Laplacian, the sharp two-term trace expansion is
\[
\boxed{\ \operatorname{tr}(L_n^+)=\frac{n^4}{B}\left[\frac{\sqrt{PQ}}{\pi}\log n+2Q C(Q/P)+o(1)\right].\ }
\]
The sum of effective resistances over unordered vertex pairs is \(n^2\operatorname{tr}(L_n^+)\). If \(P=Q\), symmetry gives \(t_n=1\) exactly at every size. Relative to an allocation with identical horizontal and vertical conductances, the optimal resistance ratio tends to \(2\sqrt{PQ}/(P+Q)\).

## Assumptions and scope
The vertex set is \((\mathbb Z/n\mathbb Z)^2\), with undirected edges to the next vertex in each coordinate direction (one edge for each vertex and direction). For \(n\ge3\), these are \(2n^2\) distinct simple edges. Horizontal edges cost \(P>0\) each per unit conductance; vertical edges cost \(Q>0\). The admissible conductances are individually nonnegative and satisfy \(\sum_{e\in E_h}Pw_e+\sum_{e\in E_v}Qw_e=B\), \(B>0\). Disconnected allocations have infinite objective. For a connected allocation, \(\operatorname{tr}(L^+)\) is the sum of reciprocal nonzero Laplacian eigenvalues, and \(\sum_{u<v}R_{uv}=n^2\operatorname{tr}(L^+)\).

## Proof
**1. Unrestricted uniqueness and symmetry.** On the mean-zero vertex subspace, a connected weighted Laplacian is positive definite. The function \(X\mapsto\operatorname{tr}(X^{-1})\) is strictly convex there: in every nonzero symmetric direction \(D\), its second derivative is \(2\operatorname{tr}(X^{-1}DX^{-1}DX^{-1})>0\), since the trace equals \(\|(X^{-1/2}DX^{-1/2})X^{-1/2}\|_F^2\) before multiplying by 2. The map from conductances to the restricted Laplacian is injective: a zero-row-sum symmetric Laplacian is determined by its action on the mean-zero subspace, and in a simple graph each individual edge weight is the negative of a distinct off-diagonal entry. The feasible price simplex is compact, contains positive allocations, and as a connected sequence approaches disconnection the smallest eigenvalue on the mean-zero subspace tends to zero, so the trace inverse diverges. This proves existence and uniqueness. Translations act transitively within each of the two priced edge classes, so uniqueness forces the optimum to use two class weights. Neither can be zero because deleting a coordinate class disconnects the graph.

**2. Scalar reduction and convex coordinate.** Put \(a_j=4\sin^2(\pi j/n)\) for \(0\le j<n\). Fourier characters diagonalize the class-weighted Laplacian, whose eigenvalues are \(x a_j+y a_k\). For \(t=x/y>0\) the budget implies \(y=B/[n^2(Pt+Q)]\) and \(x=ty\). Define
\[
S_n(t)=\sum_{(j,k)\ne(0,0)}\frac1{t a_j+a_k},\qquad
F_n(t)=\frac{Pt+Q}{n^2}S_n(t),
\]
where indices range from 0 to \(n-1\). Then \(\operatorname{tr}(L^+)=n^4 F_n(t)/B\). The fraction of budget spent horizontally is \(u(t)=Pt/(Pt+Q)\), strictly increasing in \(t\). As a function of \(u\), the trace is strictly convex by Step 1, because \(x=Bu/(Pn^2)\), \(y=B(1-u)/(Qn^2)\) is a nonconstant affine line of connected allocations for \(0<u<1\). The unique optimum is therefore characterized by \(F_n'(t)=0\), equivalently
\[
P S_n(t)=(Pt+Q)\sum_{(j,k)\ne(0,0)}\frac{a_j}{(t a_j+a_k)^2}.
\]

**3. Finite-cycle resolvent and its constant.** For \(z>0\), put \(\alpha=\operatorname{arsinh}(z/2)\). Then \(z^2+a_k=2(\cosh(2\alpha)-\cos(2\pi k/n))\). In the Poisson-kernel expansion of \(\sinh(2\alpha)/(\cosh(2\alpha)-\cos\theta)\), averaging over \(\theta=2\pi k/n\) retains only multiples of \(n\), giving \(1+2\sum_{m\ge1}e^{-2n\alpha m}=\coth(n\alpha)\). Thus
\[
\sum_{k=0}^{n-1}\frac1{z^2+a_k}=\frac{n}{z\sqrt{z^2+4}}\coth\!\left(n\operatorname{arsinh}(z/2)\right).
\]
Taking the constant term after subtracting \(z^{-2}\) at \(z=0\) gives \(\sum_{k=1}^{n-1}a_k^{-1}=(n^2-1)/12\). With \(\theta_j=\pi j/n\) and \(h_t(\theta)=[4\sqrt t\sin\theta\sqrt{1+t\sin^2\theta}]^{-1}\), the resolvent applied to the rows \(j\ne0\) gives exactly
\[
\frac{S_n(t)}{n^2}=\frac{n^2-1}{12n^2}+\frac1n\sum_{j=1}^{n-1}h_t(\theta_j)\coth\!\left(n\operatorname{arsinh}(\sqrt t\sin\theta_j)\right).
\]
Write \(A(t)=1/(2\pi\sqrt t)\) and split \(\coth=1+(\coth-1)\). For the first part, subtract \((4\sqrt t)^{-1}(1/\theta+1/(\pi-\theta))\) from \(h_t(\theta)\); the remainder extends smoothly to both endpoints, including its first two \(t\)-derivatives on any compact positive interval. The normalized discrete sum of the singular terms is \(A(t)H_{n-1}\). The remaining sum converges to the integral of the remainder divided by \(\pi\), uniformly with those derivatives. Indeed the antiderivative
\[
\int\frac{d\theta}{\sin\theta\sqrt{1+t\sin^2\theta}}=-\operatorname{artanh}\!\left(\frac{\cos\theta}{\sqrt{1+t\sin^2\theta}}\right)
\]
gives, upon truncating at \(\epsilon\) and \(\pi-\epsilon\) and subtracting the two singular integrals, the remainder integral divided by \(\pi\) as \(A(t)\log(2/[\pi\sqrt{1+t}])\). This part of the sum is therefore \(A(t)[\log n+\gamma+\log(2/[\pi\sqrt{1+t}])]+o(1)\).

For the \(\coth-1\) part, fix a compact interval \(K\subset(0,\infty)\) and write \(m=\min(j,n-j)\). The quantity \(\sin\theta_j\) is comparable to \(m/n\). The argument \(n\operatorname{arsinh}(\sqrt t\sin\theta_j)\) is at least \(c_K m\) and its first two \(t\)-derivatives are \(O_K(m)\). The prefactor \(h_t(\theta_j)/n\) and its first two \(t\)-derivatives are \(O_K(1/m)\). Since \(\coth w-1\) and its first two derivatives decay exponentially as \(w\to\infty\), the summand and its first two \(t\)-derivatives are dominated by a summable bound of the form \(C_K(1+m)^2e^{-c_K m}/m\), changing constants if necessary. At fixed \(m\), one endpoint contributes \(A(t)[\coth(\pi\sqrt t\,m)-1]/(2m)\) in the limit, uniformly with two derivatives; the two endpoints together give twice that. The central index, when there is only one term at distance \(n/2\), vanishes by the same bound. Expanding \(\coth w-1=2\sum_{\ell\ge1}e^{-2\ell w}\) gives
\[
\sum_{m\ge1}\frac{\coth(\pi\sqrt t\,m)-1}{m}=-2\sum_{\ell\ge1}\log(1-e^{-2\pi\sqrt t\,\ell}).
\]
Consequently,
\[
\frac{S_n(t)}{n^2}=A(t)\log n+C(t)+o(1)
\]
in \(C^2(K)\) for every such compact interval \(K\).

**4. Localization and drift of the optimizer.** Let \(g(t)=(Pt+Q)A(t)=(P\sqrt t+Q/\sqrt t)/(2\pi)\) and \(H(t)=(Pt+Q)C(t)\). The unique minimum of \(g\) is at \(t_0=Q/P\). Choose any fixed \(a<t_0<b\) with \(a>0\). The expansion at the three fixed points gives \(F_n(a)>F_n(t_0)\) and \(F_n(b)>F_n(t_0)\) for large \(n\). Convexity in \(u\) now traps the minimizer in \((a,b)\): if it were at or to the left of \(a\), convexity between that minimizer and \(u(t_0)\) would give \(F_n(a)\le F_n(t_0)\), a contradiction, and the right-hand argument is the same. Because the bracket is arbitrary, \(t_n\to t_0\), and one fixed bracket also supplies the compact interval on which to differentiate the expansion.

Stationarity gives \((\log n)g'(t_n)=-H'(t_n)+o(1)\). In particular \(t_n-t_0=O(1/\log n)\), since \(g'(t_0)=0\) and \(g''(t_0)=P/(4\pi t_0^{3/2})>0\). It follows that
\[
(t_n-t_0)\log n\longrightarrow -\frac{H'(t_0)}{g''(t_0)}=-4\pi t_0^{3/2}\bigl[C(t_0)+2t_0 C'(t_0)\bigr].
\]
In \(C+2tC'\), the derivative of the factor \(A(t)\) cancels the corresponding nondifferentiated term. Differentiating the bracket defining \(C\) thus gives the displayed \(\kappa\); its square bracket tends to \(1/12\) as \(t\to\infty\), so it is not identically zero. The equal-price case also has exact coordinate-swap symmetry. Finally \((g(t_n)-g(t_0))\log n=o(1)\) by the quadratic Taylor estimate and the rate just obtained, while \(H(t_n)\to H(t_0)=2QC(t_0)\). This proves the trace formula. The allocation \(t=1\) has leading coefficient \(g(1)=(P+Q)/(2\pi)\), proving the ratio statement.

## Verification
The accompanying standard-library program `verify.py` checks finite cases. It reconstructs the Laplacian and computes an exact rational trace inverse on small tori to compare to the Fourier formula. It also checks the finite-cycle resolvent, the fixed-anisotropy constant and selected optimizer drifts numerically. The package records a replay of `python3 verify.py` with `VERIFY_OK 100 checks; exact traces, Fourier-resolvent identity, finite-size constant, optimized drift`. Those checks are corroboration only; the optimizer localization and uniform differentiable expansion are justified by the proof above.

## Relationship to prior work
Ghosh, Boyd and Saberi develop the general convex conductance-allocation framework, uniqueness and symmetry reductions. Rossi, Frasca and Fagnani obtain the two-dimensional leading logarithm for the unweighted toroidal average resistance. Cserti develops lattice Green-function formulas for fixed networks. Izmailian and Huang derive theta-function asymptotics for fixed anisotropic periodic networks, for resistance between two maximally separated nodes rather than the trace inverse; the parity-restricted periodic sum in their equations (30)–(32) is not the zero-mode-deleted full sum used here. Their asymptotic method is related to the endpoint analysis above. The fixed-\(t\) Green-function constant by itself is not asserted to be new. The specific contribution is the explicit fixed-price optimizer drift and the corresponding two-term optimized trace, obtained over individually adjustable conductances.

## Limitations
Prices and budget are fixed as \(n\to\infty\). The proof does not address varying prices, rectangular side lengths, open boundaries, discrete edge-selection budgets, or other objectives. Full historical priority against the literature on finite lattice Green functions and network design is not established.

## References
1. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66. DOI: 10.1137/050645452. https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf
2. W. S. Rossi, P. Frasca and F. Fagnani, *Average resistance of toroidal graphs*, SIAM Journal on Control and Optimization 53 (2015), 2541–2557. https://arxiv.org/abs/1309.2172
3. J. Cserti, *Application of the lattice Green's function for calculating the resistance of an infinite network of resistors*, Am. J. Phys. 68 (2000), 896–906. https://arxiv.org/abs/cond-mat/9909120
4. N. Sh. Izmailian and M.-C. Huang, *Asymptotic expansion for the resistance between two maximally separated nodes on an M×N resistor network*, Phys. Rev. E 82 (2010), 011125. https://arxiv.org/abs/1005.1434
