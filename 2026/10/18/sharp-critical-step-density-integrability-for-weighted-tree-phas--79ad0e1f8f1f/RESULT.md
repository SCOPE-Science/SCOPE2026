# Sharp critical-step density integrability for weighted tree phase maps

## Finding
Let a tree have \(d+1\) vertices and \(d\ge1\) edges, with positive edge weights \(a_i\). Orient every edge from one color class of the tree's bipartition toward the other, write \(B\) for the oriented vertex-edge incidence matrix, \(K=B^{T}B\), \(A=\operatorname{diag}(a_1,\ldots,a_d)\), and \(\Lambda=\lambda_{\max}(A^{1/2}KA^{1/2})\). At the critical coupling \(h=1/\Lambda\), let
\[
F(z)=z+\Lambda^{-1}KA\sin z\pmod{2\pi},\qquad z\in\mathbb T^d.
\]
Let \(m\) be normalized Haar measure and \(\rho=d(F_*m)/dm\). Then \(F\) is a homeomorphism, is a smooth orientation-preserving local diffeomorphism except at the unique point \(p=(\pi,\ldots,\pi)\), and \(F_*m\ll m\). Its density obeys the **sharp dimension-dependent threshold**
\[
\rho\in L^q(m)\quad\Longleftrightarrow\quad 1\le q<1+\frac d2.
\]
There is moreover an exact spectral coefficient for its critical logarithmic divergence. Let \(\lambda_1,\ldots,\lambda_{d-1}\) be all eigenvalues other than \(\Lambda\) of \(A^{1/2}KA^{1/2}\); choose the \(\Lambda\)-eigenvector \(v\) of \(KA\) normalized by \(v^TAv=1\), and set
\[
c=\prod_{j=1}^{d-1}\left(1-\frac{\lambda_j}{\Lambda}\right),\qquad H=\frac c2\operatorname{diag}(a_1v_1^2,\ldots,a_dv_d^2).
\]
All \(v_i\ne0\), so \(H\) is positive definite. Put \(q_c=1+d/2\), and let \(U_{\epsilon,\delta}=\{z\in\mathbb T^d:\epsilon<\lVert z-p\rVert_2<\delta\}\) for \(0<\epsilon<\delta\) sufficiently small, using the ordinary Euclidean representative centered at \(p\). Then
\[
\int_{F(U_{\epsilon,\delta})}\rho^{q_c}\,dm
=\frac{|S^{d-1}|}{(2\pi)^d\sqrt{\det H}}\log\frac1\epsilon+O_{K,A,\delta}(1).
\]
Here \(|S^{d-1}|=2\pi^{d/2}/\Gamma(d/2)\); an empty product for \(d=1\) equals one. For the unit-weight three-vertex path, \(d=2\), \(K=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)\), the threshold is \(q<2\), \(H=I/6\), and the logarithmic coefficient is exactly \(3/\pi\).

## Assumptions and scope
The tree is finite and connected, all weights are strictly positive, and the sine acts coordinatewise. The displayed edge coordinates identify the quotient by common oscillator phase with \(\mathbb T^d\) by a unimodular change of coordinates, hence preserve normalized Haar measure. The top eigenvalue of \(A^{1/2}KA^{1/2}\) is simple and has a strictly positive eigenvector because the chosen bipartite edge orientation gives \(K_{ii}=2\) and \(K_{ij}\in\{0,1\}\), and the line graph of a tree is connected. No small-weight, path, or diagonal-dominance hypothesis is required. All \(L^q\) statements concern the one-step pushforward density, not an invariant density or a stationary law.

## Proof
**1. Global injectivity.** The matrix \(K\) is positive definite because incidence columns of a tree are independent. The spectral definition of \(\Lambda\) yields \(K^{-1}-\Lambda^{-1}A\succeq0\). Write \(h=1/\Lambda\) and \(f(t)=t+\sin t\). For any distinct lifts \(x,y\in\mathbb R^d\),
\[
\begin{aligned}
(x-y)^T K^{-1}(F(x)-F(y))
&=(x-y)^T(K^{-1}-hA)(x-y)\\
&\quad+h\sum_i a_i(x_i-y_i)(f(x_i)-f(y_i))>0,
\end{aligned}
\]
where this formula uses the unreduced lift. The strict inequality holds because \(f'(t)=1+\cos t\ge0\), with isolated zeroes, so \(f\) is strictly increasing. Thus the lift is injective. If two torus classes had the same image, translating one lift by an appropriate \(2\pi\mathbb Z^d\) vector (the lift is equivariant) would contradict injectivity. The continuous injective self-map of the compact connected torus is surjective by invariance of domain; hence it is a homeomorphism.

**2. The unique singularity.** Its derivative is \(DF(z)=I+hKA\operatorname{diag}(\cos z_i)\). Multiplication on the left by positive-definite \(K^{-1}\) gives
\[
K^{-1}DF(z)=(K^{-1}-hA)+hA\operatorname{diag}(1+\cos z_i)\succeq0.
\]
The first summand has a one-dimensional kernel spanned by \(v\), since \(\Lambda\) is a simple top eigenvalue. The second summand annihilates \(v\) only when \(1+\cos z_i=0\) for every \(i\), because each \(v_i\ne0\). Therefore \(DF\) is invertible away from \(p\), positive orientation there, and of corank exactly one at \(p\).

**3. The critical quadratic determinant.** Put \(z=p+x\), and \(L=I-hKA\). The Taylor expansion gives
\[
DF(p+x)=L+\frac h2 KA\operatorname{diag}(x_i^2)+O(\lVert x\rVert^4).
\]
With \(v^TAv=1\), the left null vector of \(L\) is \(Av\), and the product of its nonzero eigenvalues is \(c\); thus \(\operatorname{adj}(L)=c\,v(Av)^T\). Differentiating the determinant at \(L\) gives
\[
\begin{aligned}
\det DF(p+x)
&=\operatorname{tr}\!\left(\operatorname{adj}(L)\frac h2 KA\operatorname{diag}(x_i^2)\right)+O(\lVert x\rVert^4)\\
&=\frac c2\sum_i a_iv_i^2x_i^2+O(\lVert x\rVert^4)
=x^THx+O(\lVert x\rVert^4).
\end{aligned}
\]
The second equality follows from \((Av)^TKA=\Lambda(Av)^T\). Since \(H\succ0\), there exist positive constants \(c_-,c_+\) with \(c_-\lVert x\rVert^2\le\det DF(p+x)\le c_+\lVert x\rVert^2\) for small \(x\).

**4. Density and its sharp norm.** Outside \(p\), the homeomorphism is a diffeomorphism. Its inverse change-of-variables formula gives \(\rho(F(x))=[\det DF(x)]^{-1}\) for \(x\ne p\). A singleton and its image are null; applying this formula on an increasing exhaustion of the punctured torus proves \(F_*m\ll m\), with no singular atom. For every \(q\ge1\),
\[
\int\rho(y)^q\,dm(y)=\frac1{(2\pi)^d}\int_{\mathbb T^d}\bigl(\det DF(x)\bigr)^{1-q}\,dx.
\]
All integrals away from \(p\) are finite. Near \(p\) the integrand is comparable to \(\lVert x\rVert^{2(1-q)}\); its radial integral converges exactly when \(d+2(1-q)>0\). This proves both sides of the sharp threshold, not merely a sufficient estimate.

**5. Logarithmic coefficient.** For \(q_c=1+d/2\), polar coordinates \(x=r\omega\) give
\[
\bigl(\det DF(p+r\omega)\bigr)^{-d/2}
=r^{-d}(\omega^TH\omega)^{-d/2}\bigl(1+O(r^2)\bigr),
\]
uniformly on the sphere. Radial integration on \(\epsilon<r<\delta\) therefore yields a logarithmic main term and a bounded remainder. The elementary ellipsoidal Gaussian integral gives
\[
\int_{S^{d-1}}(\omega^TH\omega)^{-d/2}\,d\sigma(\omega)=\frac{|S^{d-1}|}{\sqrt{\det H}},
\]
which proves the stated coefficient. The three-vertex-path value follows from \(\Lambda=3\), the other eigenvalue \(1\), \(v=(1,1)/\sqrt2\), and \(c=2/3\).

## Verification
Run the embedded standalone script `verify.py` with Python, NumPy and SymPy: `python verify.py`. It verifies the exact two-edge Jacobian identity and Hessian coefficient symbolically, checks the \(3/\pi\) critical constant, and tests the determinant's predicted quadratic asymptotic on positive-weight trees with \(1,2,3,4,5,8\) edges, including nontrivial weights. It also verifies the anisotropic circle integral numerically. The program reported 488 successful checks. Only the proof above justifies all dimensions and all positive weights.

## Relationship to prior work
Buescu, D'Aniello and Oliveira (arXiv:2610.10993v1), Sections 2–5, establish the sine-tree quotient-gradient structure and a Morse–Smale criterion for strictly smaller coupling, explicitly noting loss of diffeomorphicity at equality. They do not analyze the pushforward of Haar measure or its critical \(L^q\) behavior. Their earlier three-clock papers (arXiv:2502.15371v1 and arXiv:2503.13230v1) concern Lyapunov functions and attracting basins in the diffeomorphism regime. The underlying change-of-variables and quadratic-singularity integral are classical; the contribution here is their combination with an **exact all-positive-weight tree determinant coefficient**, sharp dimension-dependent integrability threshold, and spectral logarithmic constant at the critical network step. Prior treatments of critical map injectivity or cubic inverse modulus alone do not supply these volume-distortion statements.

## Limitations
The statement concerns the single critical update and its one-step pushforward of Haar, not invariant densities, ergodic statistics, long-time iterated distortion or the full phase space before quotienting. The full-support top eigenvector is essential to a unique isolated Jacobian zero; sign-changing edge laws, disconnected graphs, general cyclic networks, or degenerate top eigenspaces can have different thresholds. The calculation uses Euclidean edge-angle Haar coordinates, which are canonical up to torus automorphism but not arbitrary non-unimodular ambient rescalings. Literature priority beyond the inspected papers and mathematical-record searches has not been independently settled.

## References
1. Jorge Buescu, Emma D'Aniello, and Henrique M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1 (first publicly posted 2026-10-07), https://arxiv.org/pdf/2610.10993; especially Sections 2–5.
2. Jorge Buescu, Emma D'Aniello, and Henrique M. Oliveira, *A Lyapunov function for a Synchronisation diffeomorphism of three clocks*, arXiv:2502.15371v1 (2025), https://arxiv.org/pdf/2502.15371.
3. Jorge Buescu and Henrique M. Oliveira, *Lyapunov functions for Morse–Smale synchronisation diffeomorphisms*, arXiv:2503.13230v1 (2025), https://arxiv.org/pdf/2503.13230.
4. The standard inverse-function theorem, change-of-variables theorem, invariance of domain and Perron–Frobenius theorem are used in their classical finite-dimensional forms.
