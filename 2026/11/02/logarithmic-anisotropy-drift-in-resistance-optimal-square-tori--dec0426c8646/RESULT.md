# Logarithmic anisotropy drift in resistance-optimal square tori

## Finding
Let \(n\ge3\), \(P,Q,B>0\), and consider the simple toroidal grid \(G_n=C_n\square C_n\). Charge \(P\) per unit horizontal-edge conductance and \(Q\) per unit vertical-edge conductance. Every individual edge conductance is independently nonnegative, the total expenditure is \(B\), and the objective is the sum of all pairwise effective resistances (equivalently the trace of the Laplacian pseudoinverse).

There is exactly one globally optimal allocation. Every horizontal edge receives a common positive conductance \(x_n\), and every vertical edge receives a common positive conductance \(y_n\). Put \(t_n=x_n/y_n\), \(t_0=Q/P\), and define, for \(t>0\),
\[
C(t)=\frac1{12}+\frac{1}{2\pi\sqrt t}\left[\gamma+\log\frac{2}{\pi\sqrt{1+t}}-2\sum_{\ell=1}^{\infty}\log\bigl(1-e^{-2\pi\sqrt t\,\ell}\bigr)\right],
\]
\[
\kappa(t)=-4\pi t^{3/2}\left[\frac1{12}-\frac{\sqrt t}{2\pi(1+t)}-2\sum_{\ell=1}^{\infty}\frac{\ell}{e^{2\pi\sqrt t\,\ell}-1}\right].
\]
Here \(\gamma\) is Euler's constant; both displayed series converge exponentially for each fixed \(t>0\). Then
\[
\boxed{\ t_n=\frac QP+\frac{\kappa(Q/P)}{\log n}+o\!\left(\frac1{\log n}\right)\quad(n\to\infty).\ }
\]
Thus the limiting directional conductance ratio is the inverse price ratio, with an explicit, generally nonzero, *logarithmically slow finite-size drift*.

With \(L_n\) the optimally weighted Laplacian, its pseudoinverse has the sharp two-term trace asymptotic
\[
\boxed{\ \operatorname{tr}(L_n^+)=\frac{n^4}{B}\left[\frac{\sqrt{PQ}}{\pi}\log n+2Q C(Q/P)+o(1)\right].\ }
\]
The sum of effective resistances over unordered vertex pairs is \(n^2\operatorname{tr}(L_n^+)\). For \(P=Q\), symmetry gives \(t_n=1\) exactly at every size. Relative to an allocation with identical horizontal and vertical conductances, the leading optimal resistance ratio tends to \(2\sqrt{PQ}/(P+Q)\).

## Assumptions and scope
The vertex set is \((\mathbb Z/n\mathbb Z)^2\), with undirected edges to the next vertex in each coordinate direction (one edge for each vertex and direction). For \(n\ge3\), these are \(2n^2\) distinct simple edges. Horizontal edges cost \(P>0\) each per unit conductance; vertical edges cost \(Q>0\). The admissible conductances are individually nonnegative and satisfy \(\sum_{e\in E_h}Pw_e+\sum_{e\in E_v}Qw_e=B\), \(B>0\). Disconnected allocations have infinite objective. Write \(\operatorname{tr}(L^+)\) for the sum of reciprocal nonzero Laplacian eigenvalues. The convention is \(R_{\rm tot}=\sum_{u<v}R_{uv}=n^2\operatorname{tr}(L^+)\), because the number of vertices is \(n^2\).

## Proof
**1. Unrestricted uniqueness and symmetry.** On the mean-zero vertex subspace, a connected weighted Laplacian is positive definite. The function \(X\mapsto\operatorname{tr}(X^{-1})\) is strictly convex on positive-definite matrices: in every nonzero symmetric direction \(D\), its second derivative is \(2\operatorname{tr}(X^{-1}DX^{-1}DX^{-1})>0\). The map from conductances to the restricted Laplacian is injective for a simple graph (individual edge weights occur as the negatives of its off-diagonal entries, and a zero-row-sum matrix is determined by its action on the mean-zero subspace). Therefore the objective is strictly convex on connected allocations. The feasible price simplex is compact, and the trace diverges as a connected sequence approaches disconnection, so a unique minimizer exists. Translations and reflections act transitively on each of the two priced edge classes. Uniqueness forces two uniform class weights \(x_n,y_n\). Neither can be zero, since deleting an entire coordinate class disconnects the graph.

**2. Exact scalar reduction.** Let \(a_j=4\sin^2(\pi j/n)\), \(0\le j<n\). Fourier characters diagonalize the weighted Laplacian, with nonzero eigenvalues \(x_na_j+y_na_k\), \((j,k)\ne(0,0)\). Setting \(t=x_n/y_n\) and enforcing the budget gives
\[
y_n=\frac{B}{n^2(Pt+Q)},\qquad x_n=\frac{Bt}{n^2(Pt+Q)}.
\]
Define \(S_n(t)=\sum_{(j,k)\ne(0,0)}(ta_j+a_k)^{-1}\). Then \(\operatorname{tr}(L^+)=n^2(Pt+Q)S_n(t)/B\). The positive minimizing \(t=t_n\) is uniquely characterized by
\[
P S_n(t)=(Pt+Q)\sum_{(j,k)\ne(0,0)}\frac{a_j}{(ta_j+a_k)^2}.
\]
This equation is exact for every \(n\ge3\), not an asymptotic surrogate.

**3. Finite-cycle resolvent and its constant.** Put \(\theta_j=\pi j/n\) and \(h_t(\theta)=\bigl[4\sqrt t\sin\theta\sqrt{1+t\sin^2\theta}\bigr]^{-1}\). The cycle-resolvent identity, obtained by differentiating the standard Chebyshev eigenvalue product, is
\[
\sum_{k=0}^{n-1}\frac1{z^2+a_k}=\frac{n}{z\sqrt{z^2+4}}\coth\!\left(n\operatorname{arsinh}(z/2)\right)\quad(z>0).
\]
Since \(\sum_{k=1}^{n-1}1/a_k=(n^2-1)/12\), it follows exactly that
\[
\frac{S_n(t)}{n^2}=\frac{n^2-1}{12n^2}+\frac1n\sum_{j=1}^{n-1}h_t(\theta_j)\coth\!\left(n\operatorname{arsinh}(\sqrt t\sin\theta_j)\right).
\]
Write \(A(t)=1/(2\pi\sqrt t)\) and split \(\coth=1+(\coth-1)\). For the first sum, subtract the endpoint singularities:
\[
h_t(\theta)-\frac1{4\sqrt t}\left(\frac1\theta+\frac1{\pi-\theta}\right).
\]
The difference extends smoothly to the closed interval, with smooth dependence on \(t\) on any compact subset of \((0,\infty)\). Using \(H_{n-1}=\log n+\gamma+o(1)\) and the antiderivative
\[
\int\frac{d\theta}{\sin\theta\sqrt{1+t\sin^2\theta}}=-\operatorname{artanh}\!\left(\frac{\cos\theta}{\sqrt{1+t\sin^2\theta}}\right),
\]
its normalized sum equals
\[
A(t)\left[\log n+\gamma+\log\frac2{\pi\sqrt{1+t}}\right]+o(1).
\]
For the remainder, only the two endpoint layers contribute: fixed distance \(j\) from either endpoint gives \(A(t)[\coth(\pi\sqrt t\,j)-1]/j\). Exponential bounds on \(\coth(u)-1\) make the passage to the infinite boundary sum uniform with its first two \(t\)-derivatives. The identity
\[
\sum_{j\ge1}\frac{\coth(\pi\sqrt t\,j)-1}{j}=-2\sum_{\ell\ge1}\log(1-e^{-2\pi\sqrt t\,\ell})
\]
then yields, in \(C^2\) uniformly over compact positive \(t\)-intervals,
\[
\boxed{\ \frac{S_n(t)}{n^2}=A(t)\log n+C(t)+o(1).\ }
\]
In particular, this is stronger than a pointwise leading-log estimate.

**4. Optimization and logarithmic correction.** The minimizers \(t_n\) remain in a common compact subset of \((0,\infty)\): the zero-frequency rows give the lower bounds \(S_n(t)\ge(n^2-1)/(12t)\) and \(S_n(t)\ge(n^2-1)/12\). The leading normalized objective \((Pt+Q)A(t)=\bigl(P\sqrt t+Q/\sqrt t\bigr)/(2\pi)\) has its unique minimum at \(t_0=Q/P\). Uniform convergence on the compact set proves \(t_n\to t_0\). Differentiate the uniform \(C^2\) expansion and use the exact stationarity condition to obtain
\[
(t_n-t_0)\log n\longrightarrow-\frac{P C(t_0)+2Q C'(t_0)}{P/(4\pi t_0^{3/2})}.
\]
Differentiating the exponentially convergent defining series for \(C\), and using \(Q=Pt_0\), simplifies this limit to \(\kappa(t_0)\), exactly as displayed in the finding. Inserting \(t_n=t_0+O(1/\log n)\) into the objective gives the two-term minimum trace formula. A same-conductance allocation uses \(x=y=B/[n^2(P+Q)]\), whose leading coefficient is \((P+Q)/(2\pi)\); comparison produces the stated sharp efficiency ratio.

## Verification
The standalone standard-library program `verify.py` reconstructs the full weighted Laplacian on small tori, computes its trace inverse using exact rational Gaussian elimination, and compares it with the Fourier spectrum; it also checks the finite-cycle resolvent, the explicit Green-function constant, and the finite-size optimizer drift. Run `python3 verify.py`. In the package replay, the program printed `VERIFY_OK 100 checks; exact traces, Fourier-resolvent identity, finite-size constant, optimized drift`. These finite checks corroborate, but do not replace, the all-size analytic arguments above.

## Relationship to prior work
Ghosh, Boyd and Saberi, *Minimizing Effective Resistance of a Graph* (2008; conference version 2006), develop unrestricted convex conductance allocation, uniqueness and symmetry reductions (especially Sections 4–5), but the inspected complete text treats trees, wheels and barbells rather than the square-torus anisotropic price model. Rossi, Frasca and Fagnani, *Average resistance of toroidal graphs* (arXiv:1309.2172, first public 2013-09-09; 2015 journal version), give unweighted toroidal average-resistance asymptotics, including the two-dimensional leading logarithm; their full arXiv text considers unit resistances and does not derive the priced anisotropic optimizer or its logarithmic finite-size correction. Cserti (arXiv:cond-mat/9909120, first public 1999-09-08) develops lattice Green-function formulas for fixed networks, primarily infinite grids, not this finite-price optimization. Classical lattice Green-function and theta/eta-function results may contain the fixed-\(t\) constant \(C(t)\) in equivalent form; that constant alone is not presented as a novel independent claim. The new result is the global finite-size optimal design together with its explicit first \(1/\log n\) allocation correction and optimal resistance expansion.

## Limitations
Prices \(P,Q\) must be fixed positive numbers as \(n\to\infty\). The proof does not address prices changing with \(n\), rectangular side lengths, open boundaries, discrete edge-selection budgets, or different objectives. The result has not undergone independent mathematical validation. Full priority against all historical lattice Green-function and network-design literature is not established; equivalent specialized results may exist. No claim that the fixed-\(t\) Green-function constant alone is new is made.

## References
1. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66. DOI: 10.1137/050645452. Full text: https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf . Earlier conference version: MTNS, July 2006.
2. W. S. Rossi, P. Frasca and F. Fagnani, *Average resistance of toroidal graphs*, arXiv:1309.2172 (first submitted 2013-09-09), SIAM Journal on Control and Optimization 53 (2015), 2541–2557. https://arxiv.org/abs/1309.2172 .
3. J. Cserti, *Application of the lattice Green's function for calculating the resistance of infinite networks of resistors*, arXiv:cond-mat/9909120 (first submitted 1999-09-08), American Journal of Physics 68 (2000), 896–906. https://arxiv.org/html/cond-mat/9909120v4 .
