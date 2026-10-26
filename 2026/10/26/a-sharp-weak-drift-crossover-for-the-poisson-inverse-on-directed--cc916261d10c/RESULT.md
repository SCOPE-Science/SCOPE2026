# A sharp weak-drift crossover for the Poisson inverse on directed cycles

## Finding
Let \(n\ge 3\), and consider the nearest-neighbor circulant Markov operator \(P_{n,\varepsilon}\) on \(\mathbb Z/n\mathbb Z\), with forward-step probability \(p=(1+\varepsilon)/2\) and backward-step probability \(q=(1-\varepsilon)/2\), where \(0\le\varepsilon\le1\). Let \(L_{n,\varepsilon}=I-P_{n,\varepsilon}\) and let \(G_{n,\varepsilon}=L_{n,\varepsilon}^{\dagger}\) be its Moore–Penrose inverse, acting as the inverse on the mean-zero functions and annihilating constants. Define the sharp endpoint Poisson stability constant
\[
 C_n(\varepsilon)=\|G_{n,\varepsilon}\|_{\ell^\infty\to\ell^\infty}
 =\|G_{n,\varepsilon}\|_{\ell^1\to\ell^1}.
\]

**Exact finite-size formula.** For \(0<\varepsilon\le1\), put \(r=q/p\) and
\[
 h_{n,\varepsilon}(k)
 =\frac{k-(n-1)/2}{n\varepsilon}
 +\frac{r^k}{\varepsilon(1-r^n)}
 -\frac{p}{n\varepsilon^2},\qquad 0\le k<n.
\]
For \(\varepsilon=0\), put
\[
 h_{n,0}(k)=\frac{n^2-1}{6n}-\frac{k(n-k)}{n}.
\]
Then \(h_{n,\varepsilon}(k)=(G_{n,\varepsilon})_{k,0}\) and
\[
 \boxed{C_n(\varepsilon)=\sum_{k=0}^{n-1}|h_{n,\varepsilon}(k)|.}
\]
Every sharp endpoint norm is attained by a sign function: for the row indexed by \(0\), use the sign of \(h_{n,\varepsilon}(-k)\). The indices where \(h_{n,\varepsilon}\) is negative form one consecutive interval, possibly with zeros at its boundary.

**Diffusive-to-directed crossover.** For \(\beta\ge0\), define \(g_0(x)=x^2-x+1/6\), \(0\le x\le1\), and, if \(\beta>0\), define
\[
 g_\beta(x)=\frac{x-1/2}{\beta}-\frac1{2\beta^2}
 +\frac{e^{-2\beta x}}{\beta(1-e^{-2\beta})},
 \qquad 0\le x\le1.
\]
Set \(\Phi(\beta)=\int_0^1|g_\beta(x)|\,dx\). For *every* sequence \(0\le\varepsilon_n\le1\) with \(n\varepsilon_n\to\beta<\infty\),
\[
 \boxed{\lim_{n\to\infty}\frac{C_n(\varepsilon_n)}{n^2}
 =\Phi(\beta).}
\]
The function \(g_\beta\) is strictly convex on \((0,1)\), continuous and periodic at the endpoints, has mean zero, and has exactly two zeros in \((0,1)\). Thus \(\Phi\) is also the explicitly integrable negative mass between those two zeros. Its limiting endpoint values are
\[
 \boxed{\Phi(0)=\frac{\sqrt3}{27},\qquad
 \left|\Phi(\beta)-\frac1{4\beta}\right|\le\frac1{\beta^2}
 \ \text{for all }\beta>0.}
\]
In the complementary regime \(n\varepsilon_n\to\infty\), with \(\varepsilon_n>0\),
\[
 \boxed{C_n(\varepsilon_n)\sim\frac{n}{4\varepsilon_n}.}
\]
In fact the finite bound
\[
 \left|C_n(\varepsilon)-\frac{n}{4\varepsilon}\right|
 \le \frac1{4n\varepsilon}+\frac{2p}{\varepsilon^2}
\]
holds for every \(n\ge3\) and \(0<\varepsilon\le1\). The result distinguishes the diffusive \(n^2\)-scale at vanishing drift from the directed \(n/\varepsilon\)-scale at stronger drift and identifies the sharp transition at \(\varepsilon\asymp n^{-1}\).

## Assumptions and scope
The state space is the finite cyclic group \(\mathbb Z/n\mathbb Z\), with counting-measure \(\ell^1\) and \(\ell^\infty\) norms (no probability normalization). The kernel is real, not assumed symmetric. For \(\varepsilon=1\), the walk moves deterministically around the directed cycle; the zero-eigenvalue restriction remains invertible. All cyclic indices are taken modulo \(n\). The operator \(G_{n,\varepsilon}\) is defined by
\[
 L_{n,\varepsilon}G_{n,\varepsilon}
 =G_{n,\varepsilon}L_{n,\varepsilon}=I-J,
 \qquad G_{n,\varepsilon}\boldsymbol1=0,
\]
where \(J\) averages over all \(n\) coordinates. The limit parameter \(\beta\) is dimensionless and equals the limit of the graph size times the directional bias. No result is claimed for spatially inhomogeneous transition probabilities.

## Proof
**1. Finite inverse.** Circulant Fourier diagonalization shows that the only zero eigenvector of \(L_{n,\varepsilon}\) is constant. The matrix is normal, so its Moore–Penrose inverse is precisely the inverse on mean-zero vectors. It suffices to solve
\[
 L_{n,\varepsilon}h=\delta_0-n^{-1}\boldsymbol1,
 \qquad \sum_{k=0}^{n-1}h(k)=0.
\]
For \(\varepsilon>0\), write \(h(n)=h(0)\) and \(d_k=h(k)-h(k-1)\) for \(1\le k\le n\). Away from the source, the Poisson equation becomes \(p d_{k+1}-q d_k=1/n\), so
\[
 d_k=\frac1{n\varepsilon}-\frac{r^{k-1}}{p(1-r^n)}.
\]
This difference sequence sums to zero and satisfies the source equation \(q d_n-p d_1=1-1/n\). Summation of differences and normalization to mean zero gives exactly the asserted formula for \(h_{n,\varepsilon}\). At zero bias, substitution of the quadratic expression gives the same Poisson equation and normalization. Uniqueness on mean-zero vectors finishes the kernel derivation.

Every row of a circulant matrix is a permutation of the first column. The induced absolute row-sum and column-sum norms therefore coincide and equal \(\sum_k|h(k)|\). For a fixed row, choosing the input signs to agree with its entries attains this sum. Moreover, the first differences \(d_k\) are nondecreasing in \(k\) (strictly increasing for \(0<\varepsilon<1\)); this follows directly from the geometric term above, or from the constant second differences when \(\varepsilon=0\). Thus \(h(0),h(1),\ldots,h(n)\), with \(h(n)=h(0)\), is a convex sequence. Its largest value is at the endpoints and is positive by the mean-zero condition. Consequently its negative indices constitute one contiguous interval, with possible zero boundary values.

**2. Finite weak-drift limit.** Let \(\varepsilon_n\ge0\) satisfy \(n\varepsilon_n\to\beta\). For the Fourier index \(m\ne0\), represented by \(|m|\le n/2\), the eigenvalue of the cyclic generator is
\[
 \lambda_{m,n}=1-\cos(2\pi m/n)
 -i\varepsilon_n\sin(2\pi m/n).
\]
For each fixed nonzero integer \(m\),
\[
 n^2\lambda_{m,n}\longrightarrow2\pi^2m^2-2\pi i\beta m.
\]
The elementary inequality \(1-\cos(2\pi m/n)\ge8m^2/n^2\) for \(|m|\le n/2\) gives the uniform domination
\[
 \left|(n^2\lambda_{m,n})^{-1}\right|\le(8m^2)^{-1}.
\]
Dominated convergence in the absolutely summable Fourier series implies, *uniformly over cyclic sample points*,
\[
 \frac{h_{n,\varepsilon_n}(k)}n-g_\beta(k/n)\longrightarrow0.
\]
Indeed the limiting Fourier multiplier inverts the periodic differential operator \(-\tfrac12\partial_x^2-\beta\partial_x\) on mean-zero functions. The displayed formula for \(g_\beta\) is its unique mean-zero Green kernel: away from \(x=0\) it satisfies \(-\tfrac12g_\beta''-\beta g_\beta'=-1\), it is periodic in value, and its derivative has jump \(-2\) at the source. At \(\beta=0\), direct integration yields the polynomial formula. Uniform kernel convergence and ordinary Riemann summation imply the claimed limit for \(C_n/n^2\).

**3. Shape and normalization of the crossover.** For \(\beta>0\),
\[
 g_\beta''(x)=\frac{4\beta e^{-2\beta x}}{1-e^{-2\beta}}>0,
 \qquad \int_0^1g_\beta(x)\,dx=0,
 \qquad g_\beta(0)=g_\beta(1).
\]
For \(\beta=0\), the second derivative is \(2\) and the same endpoint and mean identities hold. Strict convexity implies the endpoints are positive and the interior minimum negative. Hence exactly two interior zero crossings exist, and \(\Phi\) equals twice the opposite of the integral between them. Integration of \(x^2-x+1/6\) between its roots \((1\pm1/\sqrt3)/2\) gives \(\Phi(0)=\sqrt3/27\). For \(\beta>0\), subtract \((x-1/2)/\beta\) from \(g_\beta\). The remaining constant has absolute integral \(1/(2\beta^2)\), and the positive exponential has integral \(1/(2\beta^2)\). The reverse triangle inequality therefore yields
\[
 \left|\Phi(\beta)-\frac1{\beta}\int_0^1|x-1/2|\,dx\right|\le\beta^{-2},
\]
which is the advertised bound.

**4. Strong-drift limit.** Split the exact finite kernel into the centered linear term \((k-(n-1)/2)/(n\varepsilon)\) and the remaining two terms. The absolute sum of the geometric term is \(p/\varepsilon^2\); that of the constant term is also \(p/\varepsilon^2\), because \(1-r=\varepsilon/p\). The absolute sum of the centered linear term differs from \(n/(4\varepsilon)\) by at most \(1/(4n\varepsilon)\), establishing the finite bound. Dividing that bound by \(n/(4\varepsilon)\) proves the stated strong-drift asymptotic whenever \(n\varepsilon_n\to\infty\).

## Verification
A standalone standard-library Python checker (`check.py`) computes exact rational Green columns both from the claimed closed formula and by separately implemented Gaussian elimination of \(L+J\). It checks the zero-mean normalization, the source and off-source Poisson equations, and the position of the maximum across multiple sizes and biases. It additionally compares finite normalized endpoint norms with the continuum integral by numerical Riemann sums and tests the strong-drift scaling. The finite checks are diagnostic; the universal statements follow from the mathematical arguments above.

## Relationship to prior work
Beveridge's *A Hitting Time Formula for the Discrete Green's Function* (arXiv:1505.06989, initially public 26 May 2015) gives a general hitting-time representation of the Green operator for strongly connected digraphs, and explicitly treats the **symmetric** cycle as an example. That representation and the symmetric-cycle Green kernel are prior results, not claimed here. In particular, the formula for \(h_{n,0}\) is included as a normalization reference only. The added statement is the sharp operator-norm crossover under directional bias, with its explicit periodic advection–diffusion limit, sign extremizers and two complementary scaling regimes. The general prior hitting-time identity alone does not quantify that endpoint transition.

Other related work on drift–diffusion limits supplies the underlying continuum interpretation; a weak limit for the walk itself is not an equality for the induced supremum norm of its centered Poisson inverse. The specific sharp norm comparison and continuum absolute-Green profile were not located in the inspected primary work or targeted searches. Absence from those searches is not a proof of historical uniqueness.

## Limitations
Historical priority is provisional. The fixed-parameter finite Green kernel is elementary and may also be expressed using pre-existing hitting-time formulas; originality is asserted only for the combined sharp endpoint crossover and sign-profile classification. The result is confined to spatially homogeneous nearest-neighbor cycles and does not give finite-size optimizing threshold indices as an independent closed floor formula. No independent audit has been performed.

## References
- Andrew Beveridge, *A Hitting Time Formula for the Discrete Green's Function*, arXiv:1505.06989v1, publicly submitted 2015-05-26; especially the directed-graph result and the symmetric-cycle computation in Section 4. https://arxiv.org/html/1505.06989v1
