# Exact graph-heat Lipschitz norms on cycles and a four-class short-time law

## Finding
Let \(C_n\) be the unweighted cycle with \(n\ge5\) vertices and graph distance, and let \(H_t=\exp(-tL_n)\) be its continuous-time heat semigroup for the **unnormalized** combinatorial Laplacian. Set \(k=\lfloor(n+2)/4\rfloor\). If \(p_t(j)=H_t(0,j)\), with vertices indexed modulo \(n\), then for every \(t\ge0\) the sharp Lipschitz-seminorm operator norm is
\[
\Lambda_n(t):=\|H_t\|_{\mathrm{Lip}\to\mathrm{Lip}}
=\sum_{j=0}^{n-1}|p_t(j)-p_t(k)|
=1-2\left[\left(2k+1-\frac n2\right)p_t(k)+\sum_{\operatorname{dist}(0,j)>k}p_t(j)\right].
\]
The finite Fourier formula
\[
p_t(j)=\frac1n\sum_{\ell=0}^{n-1}
\exp\!\left[-4t\sin^2\!\left(\frac{\pi\ell}{n}\right)\right]
\cos\!\left(\frac{2\pi\ell j}{n}\right)
\]
makes this a closed, finite expression at every time. One and the same \(1\)-Lipschitz potential (constructed below) attains this norm **for every** \(t\ge0\).

The sharp initial contraction defect obeys
\[
\boxed{\Lambda_n(t)=1-\frac{4k+2-n}{k!}\,t^k+O_n(t^{k+1})\quad(t\downarrow0),\qquad k=\left\lfloor\frac{n+2}{4}\right\rfloor.}
\]
In particular, \(4k+2-n\in\{1,2,3,4\}\); the first nonzero contraction derivative has order \(\lfloor(n+2)/4\rfloor\), which grows without bound with the cycle length. Nevertheless \(0<\Lambda_n(t)<1\) for every \(t>0\), and \(\Lambda_n\) is strictly decreasing on \([0,\infty)\).

## Assumptions and scope
Vertices are \(\mathbb Z/n\mathbb Z\) with edges between consecutive residues and unit graph-distance edge lengths. The generator is \((L_nf)(j)=2f(j)-f(j-1)-f(j+1)\), with jump rate \(1\) in **each** direction (total jump rate \(2\)). The real Lipschitz seminorm is \(\|f\|_{\mathrm{Lip}}=\max_j|f(j)-f(j+1)|\). It is a norm on functions modulo constants. The operator norm is taken on that quotient. No normalization by degree or probability is hidden in \(L_n\).

Here \(n\ge5\) is arbitrary and \(t\ge0\) is arbitrary. Constants in \(O_n(\cdot)\) may depend on the fixed cycle order. There is no assertion uniform in \(n\) as time tends to zero. The spectral expression, not any infinite-dimensional limit, defines the exact full-time value.

## Proof
**1. Edge-gradient duality.** For a periodic function put \(g_j=f(j)-f(j+1)\). Exactly the arrays satisfying \(|g_j|\le1\) and \(\sum_jg_j=0\) arise from \(1\)-Lipschitz functions. Translation invariance gives \((H_tf)(0)-(H_tf)(1)=\sum_jp_t(j)g_j\). Every output edge is a translated copy, whence
\[
\Lambda_n(t)=\max_{|g_j|\le1,\ \sum g_j=0}\sum_jp_t(j)g_j
=\min_{c\in\mathbb R}\sum_j|p_t(j)-c|.
\]
The second equality follows by the finite-dimensional duality between the quotient of \(\ell^1\) by constants and the mean-zero section of the \(\ell^\infty\) ball. Equivalently, the inequality \(\sum_jp_jg_j=\sum_j(p_j-c)g_j\le\sum_j|p_j-c|\) is sharp by assigning the signs of \(p_j-c\) and balancing the tied entries.

**2. Strict radial ordering for every positive time.** Write \(m=\lfloor n/2\rfloor\) and \(u_r(t)=p_t(r)=p_t(n-r)\), for \(0\le r\le m\). These equalities follow from reflection symmetry. Set \(q_r=u_r-u_{r+1}\) for \(0\le r<m\). For \(n\ge5\), the vector \(q\) solves a finite linear differential system with \(q(0)=(1,0,\ldots,0)\): its first equation is \(q'_0=-3q_0+q_1\), each interior equation is \(q'_r=q_{r-1}-2q_r+q_{r+1}\), and its last equation is \(q'_{m-1}=q_{m-2}-3q_{m-1}\) for even \(n\), or \(q'_{m-1}=q_{m-2}-2q_{m-1}\) for odd \(n\). For \(m=2\) there are just the first and last equations. The system matrix has nonnegative off-diagonal entries and is irreducible. Therefore \(q_r(t)>0\) for all \(r\) and \(t>0\), by positivity of its matrix exponential. Hence
\[
p_t(0)>p_t(1)>\cdots>p_t(\lfloor n/2\rfloor)>0\qquad(t>0).
\]

**3. Location of the minimizing median.** For \(k=\lfloor(n+2)/4\rfloor\), exactly \(2k-1\) vertices are strictly closer than \(k\) to the origin and \(n-(2k+1)\) are strictly farther. Both numbers are at most \(n/2\). Thus \(p_t(k)\) is a median of the multiset \(\{p_t(j):0\le j<n\}\). Inserting that median into step 1 proves the first equality. Splitting the absolute-value sum into closer, equal-distance and farther terms and using \(\sum_jp_t(j)=1\) gives the displayed formula without absolute values.

**4. A time-independent sharp potential.** Let \(d_j=\operatorname{dist}(0,j)\), and prescribe an oriented edge-gradient array
\[
g_j=\begin{cases}
1,&d_j<k,\\
(n-4k)/2,&d_j=k,\\
-1,&d_j>k.
\end{cases}
\]
Since \(n-4k\in\{-2,-1,0,1\}\), all its coordinates lie in \([-1,1]\). Its sum is
\((2k-1)+(n-4k)-[n-(2k+1)]=0\). Integrating \(g_j=f(j)-f(j+1)\) cyclically gives a real potential \(f\) with \(\|f\|_{\mathrm{Lip}}=1\). The same \(f\) attains the duality maximum for every \(t>0\), because the strict radial ordering never changes. The claim at \(t=0\) follows directly.

**5. Exact initial defect and strict contraction.** The exponential power series and minimal path length show that for every fixed \(n\ge5\), \(p_t(k)=t^k/k!+O_n(t^{k+1})\); the shortest walk to vertex \(k\) is unique, and all probabilities at graph distance greater than \(k\) are \(O_n(t^{k+1})\). Substitution into step 3 yields
\(1-\Lambda_n(t)=(4k+2-n)t^k/k!+O_n(t^{k+1})\).
For any \(t>0\), all heat probabilities are positive, so the displayed median formula gives \(\Lambda_n(t)<1\), while the nonconstant eigenmodes imply \(\Lambda_n(t)>0\). The semigroup inequality \(\Lambda_n(t+s)\le\Lambda_n(t)\Lambda_n(s)\), combined with \(0<\Lambda_n(s)<1\), proves strict decrease for every \(s>0\). This also gives the stated all-time conclusion.

## Verification
The standalone script `verify.py` constructs the combinatorial Laplacian, obtains heat kernels by matrix exponentials, and separately maximizes edge differences over the exact graph-Lipschitz polytope via linear programming. It also recomputes the initial coefficient with exact symbolic powers of the generator. Its recorded check completed: 60 independent linear-program comparisons, 15 exact Taylor coefficients for cycle orders \(3\) to \(17\) (including boundary diagnostics), and 288 radial inequalities. The theorem only claims cycle orders \(n\ge5\); the smaller orders are checker controls. Floating-point tests are diagnostics, not substitutes for steps 1–5.

Reproduce by running `python verify.py` with NumPy, SciPy and SymPy installed. No external data files are needed.

## Relationship to prior work
Ollivier's 2007 treatment introduces transport curvature and the equivalence between Wasserstein contraction and Lipschitz operator bounds; Veysseire's 2012 theorem extends continuous-time curvature contraction, and Cloez's 2012 study develops sharp Wasserstein decay for one-dimensional jump-diffusions. Jost–Liu's 2011 graph-curvature analysis concerns local transport and curvature estimates for nearest-neighbor chains. These supply the transport viewpoint, but their inspected statements do not compute the complete time-dependent sharp Lipschitz norm on every finite cycle or the residue-class order of its first nonzero contraction term.

The generic fact that cyclic gradient arrays have zero sum is not asserted to be new. The new conclusion is the explicit heat-kernel **median index independent of time**, the **single simultaneous extremizer**, and the complete **four-class high-order short-time law** for arbitrarily long cycles. A related calculation of Fejér convolution on the continuous circle uses a median formula for a different kernel; neither that formula nor known special small-cycle heat calculations imply the finite-cycle heat profile for all \(n\ge5\).

## Limitations
The result concerns finite **unweighted** cycles, the unit graph-distance Lipschitz seminorm, and the combinatorial (not normalized) heat generator. It does not address directed walks, conductance-weighted cycles, arbitrary circulant jump generators, or uniform-in-dimension short-time asymptotics. The originality assessment is subject to possible unindexed, equivalent optimal-transport calculations. No claim of independent external validation is made.

## References
- Yann Ollivier, *Ricci curvature of Markov chains on metric spaces*, first posted 2007-01-30, arXiv:math/0701886.
- Jürgen Jost and Shiping Liu, *Ollivier's Ricci curvature, local clustering and curvature dimension inequalities on graphs*, first posted 2011-03-21, arXiv:1103.4037.
- Laurent Veysseire, *Coarse Ricci curvature for continuous-time Markov processes*, first posted 2012-02-02, arXiv:1202.0420.
- Bertrand Cloez, *Wasserstein decay of one dimensional jump-diffusions*, first posted 2012-02-06, arXiv:1202.1259.
