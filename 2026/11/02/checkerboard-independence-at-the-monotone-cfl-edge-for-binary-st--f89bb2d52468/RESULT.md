# Checkerboard independence at the monotone CFL edge for binary stochastic heat rounding

## Finding

**Theorem (stationary checkerboard law and two-cell continuation).** Fix an integer \(m\ge2\). At the \(m\) interior sites of the one-dimensional heat difference grid, keep both boundary values equal to \(1/2\). Use the complete-step, independently rounded forward-Euler update defined below on the binary lattice \(\{0,1\}^m\). For every \(0<h\le1/2\), the resulting chain has a unique invariant law \(\pi_{m,h}\), reached geometrically in a weighted Wasserstein metric from every initial law. Every one-site marginal of this law is the fair Bernoulli distribution.

Its stationary off-diagonal covariances satisfy the sharp dichotomy
\[
\operatorname{Cov}_{\pi_{m,h}}(X_i,X_j)=
\begin{cases}
>0,&0<h<1/2,\\
0,&h=1/2\text{ and }i-j\text{ is odd},\\
>0,&h=1/2\text{ and }i-j\text{ is even},
\end{cases}\qquad i\ne j.
\]
In fact, the endpoint statement is stronger than pairwise decorrelation: at \(h=1/2\) the **entire odd-indexed subconfiguration and entire even-indexed subconfiguration are independent** under \(\pi_{m,1/2}\). Coordinates within one parity class need not be independent; for \(m=3\), \(\operatorname{Cov}(X_1,X_3)=1/16\) at this endpoint.

When \(m=2\), the binary update remains well-defined on the larger interval \(0<h<2/3\). Throughout this interval it has a unique invariant law and
\[
\operatorname{Cov}(X_1,X_2)=\frac{1-2h}{2(4-5h)}.
\]
Thus its covariance is positive below \(1/2\), zero exactly at \(1/2\), and negative above \(1/2\), even though the deterministic two-cell Euler map is spectrally stable for every \(0<h<2/3\). In particular, \(\lim_{h\downarrow0}\operatorname{Cov}(X_1,X_2)=1/8\).

## Assumptions and scope

Use \(h=\Delta t/(\Delta x)^2\) as the nondimensional Euler diffusion number, not physical time. At step \(k\), the interior state \(X^k=(X_1^k,\ldots,X_m^k)\) takes values in \(\{0,1\}^m\). Set \(X_0^k=X_{m+1}^k=1/2\) (these fixed boundary values are *never* rounded). Form
\[
p_i^k=(1-2h)X_i^k+h(X_{i-1}^k+X_{i+1}^k),\quad 1\le i\le m.
\]
Conditional on \(X^k\), produce the \(m\) new coordinates **independently** with \(X_i^{k+1}\sim\operatorname{Bernoulli}(p_i^k)\). Equivalently, apply unbiased stochastic rounding to the adjacent binary lattice values \(0\) and \(1\) once, after computing the full Euler update exactly. This is an intentionally coarse fixed-lattice quantizer, **not** IEEE floating-point stochastic rounding at every arithmetic operation.

For all \(m\ge2\) and \(0<h\le1/2\), convexity ensures \(0\le p_i^k\le1\) in every state. For \(m=2\), the boundary contributions allow this for all \(0<h\le2/3\); the strict upper bound is used to ensure uniqueness of the invariant law. No assertion of a binary update is made for arbitrary larger grids with \(h>1/2\).

## Proof

**1. Contraction and centered means.** Put \(s_i=2X_i-1\in\{-1,1\}\) at interior sites and \(s_0=s_{m+1}=0\). Write \(A_m\) for the path-adjacency matrix and \(B=(1-2h)I_m+hA_m\). Conditional independence and unbiased rounding yield
\[
\mathbb E[s^{k+1}\mid s^k]=B s^k.
\]
For \(0<h\le1/2\), \(B\) is entrywise nonnegative. The vector \(w_i=\sin(\pi i/(m+1))\) has strictly positive entries and satisfies
\[
Bw=\rho w,\qquad \rho=1-2h+2h\cos\bigl(\pi/(m+1)\bigr)\in(0,1).
\]
Couple two copies of the chain by using the same independent uniform random numbers for corresponding site-roundings. In this coupling, the chance of a site mismatch after one step is exactly the absolute difference of the corresponding Bernoulli parameters, hence is at most the corresponding component of \(B|X-Y|\). Therefore
\[
\mathbb E\sum_iw_i|X_i^{k+1}-Y_i^{k+1}|
\le\rho\sum_iw_i|X_i^k-Y_i^k|.
\]
Since the state space is finite, this contraction gives a unique stationary law and geometric convergence of laws. Its centered mean satisfies \(\bar s=B\bar s\) and therefore vanishes. Thus \(\mathbb E X_i=1/2\) and \(\operatorname{Var}(X_i)=1/4\) for every site, at stationarity.

**2. A positive-noise covariance series.** Let \(C=\mathbb E_{\pi}[ss^{\mathsf T}]\), so \(C_{ii}=1\). The site roundings are conditionally independent. Consequently \(C=BCB+D\), where \(D\) is diagonal, with
\[
D_{ii}=\mathbb E_{\pi}\!\left[\operatorname{Var}(s_i^{k+1}\mid s^k)\right]
=\mathbb E_{\pi}[1-(Bs^k)_i^2]\ge0.
\]
As \(\rho(B)<1\), iterating the identity gives an absolutely convergent series
\[
C=\sum_{r=0}^{\infty}B^rD(B^r)^{\mathsf T}.
\]
At the left boundary \(p_1^k\in[h/2,1-h/2]\), so \(D_{11}=\mathbb E[4p_1^k(1-p_1^k)]>0\) for every \(0<h\le1/2\). For \(0<h<1/2\), the matrix \(B\) has positive diagonal and positive neighboring entries. For any distinct \(i,j\), some common step count \(r\) has \((B^r)_{i1}(B^r)_{j1}>0\), by paths from vertex \(1\) padded using positive self-loops. The corresponding term of the series is strictly positive; every term is nonnegative. Thus \(C_{ij}>0\).

At \(h=1/2\), \(B=A_m/2\) has zero diagonal. A length-\(r\) path from a vertex \(a\) can end only at a vertex of parity \(a+r\). Therefore each summand vanishes at \((i,j)\) when \(i-j\) is odd. If \(i-j\) is even, paths from vertex \(1\) to \(i\) and \(j\) exist at a common sufficiently large length of the correct parity (one may pad a path by two-step backtracking). Since \(D_{11}>0\), the corresponding summand is strictly positive. This proves the stated pair-covariance dichotomy, using \(\operatorname{Cov}(X_i,X_j)=C_{ij}/4\).

**3. Independence of the two parity blocks.** At \(h=1/2\), all conditional update probabilities at odd sites depend only on the previous even sites, and vice versa. Since every output uses independent rounding, the two-step transition kernel factors as
\[
P^2((a,b),(a',b'))=Q_{\rm odd}(a,a')\,Q_{\rm even}(b,b'),
\]
where \(a\) and \(b\) denote odd- and even-indexed bit configurations. Each marginal of the unique invariant law is invariant for its corresponding factor. Their product is then invariant for \(P^2\). The same coupling bound, now with factor \(\rho^2<1\), makes the invariant law of \(P^2\) unique. Hence this product is the original invariant law. For \(m=3\), at \(h=1/2\) the conditional spin means at sites \(1\) and \(3\) both equal \(s_2/2\), giving \(\mathbb E[s_1s_3]=1/4\) and \(\operatorname{Cov}(X_1,X_3)=1/16\).

**4. The sharp two-site extension.** For \(m=2\), all four Bernoulli parameters lie strictly inside \((0,1)\) whenever \(0<h<2/3\); every transition probability is then positive, so the chain has one invariant law. The centered mean matrix is \(B=\begin{psmallmatrix}1-2h&h\\h&1-2h\end{psmallmatrix}\), whose eigenvalues \(1-h\) and \(1-3h\) lie strictly inside the unit disk on this entire interval. Therefore both centered stationary means are zero. Let \(q=\mathbb E[s_1s_2]\) at stationarity. Conditional independence yields
\[
q=2h(1-2h)+\bigl((1-2h)^2+h^2\bigr)q.
\]
Solving gives \(q=2(1-2h)/(4-5h)\), and dividing by four gives the asserted covariance. The denominator remains positive throughout \(0<h<2/3\), so every sign and endpoint limit follows directly. At \(h=2/3\) the chain has a period-two recurrent class, which is deliberately excluded from the uniqueness assertion.

## Verification

The accompanying `verify.py` constructs the complete finite-state transition matrices using exact rational arithmetic, solves exactly for stationary distributions, and checks all pair signs, mean identities, full parity-factorization at the endpoint, the two-site formula, and the three-site within-parity covariance for \(m=2,3,4\) at several rational step values. Run `python verify.py` after installing `sympy` according to `requirements.txt`. This is a finite reproducibility check; the proof for every integer \(m\ge2\) and real admissible \(h\) is the coupling, covariance-series, and two-step kernel argument above.

## Relationship to prior work

Croci and Giles (arXiv:2010.16225; first preprint October 30, 2020) analyze floating-point rounding errors in finite-difference heat solvers and establish global error estimates for stochastic versus nearest rounding. Their numerical representation and questions differ from this fixed binary-lattice stationary law. Their observations about mean-independent fresh rounding errors do not imply independence of the *stationary rounded solution*.

Gastner (arXiv:1502.02883) maps a synchronous noisy voter model on a **periodic** chain to a constrained Ising model and derives correlations. The present heat-rounding chain has finite Dirichlet reservoirs held at \(1/2\), a self-retention term below the endpoint, a unique stationary law, and a specific checkerboard factorization at the endpoint. The finite-graph voter duality analyzed by Ben-Ari, Panzo, Speegle and VandenBerg (arXiv:2004.10187) concerns a different absorbing voter process and quasi-stationarity on complete bipartite graphs. General voter and finite-state Markov methods are natural background mechanisms; the claimed scope is this exact numerical discretization and its stationary structure, not the originality of those mechanisms.

## Limitations

This is an idealized, exactly computed Euler step followed by one independently sampled **binary fixed-grid** rounding per site. It is not a theorem about IEEE fp16/bfloat16 rounding, finite-precision evaluation of stencil sums, general source terms, nonconstant boundary data, other graph Laplacians, or multidimensional grids. The full parity-block independence statement is established only at \(h=1/2\); outside that point, the assertion is about covariance signs. Correlated random-number streams can destroy the conditional-independence step of the proof. General sampling/rounding policies and an independent priority audit have not been assessed.

## References

1. M. Croci and M. B. Giles, *Effects of round-to-nearest and stochastic rounding in the numerical solution of the heat equation in low precision*, arXiv:2010.16225, first submitted 2020-10-30. https://arxiv.org/abs/2010.16225
2. M. T. Gastner, *The Ising chain constrained to an even or odd number of positive spins*, arXiv:1502.02883, first submitted 2015-02-10. https://arxiv.org/abs/1502.02883
3. I. Ben-Ari, H. Panzo, P. Speegle and R. O. VandenBerg, *Quasi-Stationary Distributions for the Voter Model on Complete Bipartite Graphs*, arXiv:2004.10187, first submitted 2020-04-21. https://arxiv.org/abs/2004.10187
