# Parity-split Gaussian bandwidth on circular ladders

## Finding

Let \(P_n=C_n\square K_2\) be the circular ladder (prism graph) with \(n\ge20\) rim positions and \(2n\) vertices, equipped with unweighted shortest-path distance \(d\). For \(t>0\) put
\[
K_n(t)_{uv}=\exp(-t\,d(u,v)^2).
\]
For every \(n\ge20\), there is a unique \(t_n>1\) such that, **within \(t\ge1\)**, \(K_n(t)\) is positive semidefinite exactly for \(t\ge t_n\), and positive definite exactly for \(t>t_n\). Every \(t\ge t_n\) is admissible, even without restricting \(t\ge1\), so \(t_n\) is also the last-failure parameter
\[
\tau_n=\sup\{t>0:K_n(t)\text{ has a negative eigenvalue}\}.
\]
At \(t_n\), the nullity is one for even \(n\) and two for odd \(n\).

The asymptotic limiting threshold is not zero. Let \(t_*\in(1,6/5)\) be the unique root of the absolutely convergent alternating Gaussian series
\[
F(t)=1-3e^{-t}+4\sum_{r=2}^{\infty}(-1)^r e^{-tr^2}.
\]
Set
\[
g_r(t)=e^{-tr^2}-e^{-t(r+1)^2},\quad
Q(t)=-\sum_{r=1}^{\infty}(-1)^r r^2g_r(t),\quad
c_*={\pi^2Q(t_*)\over F'(t_*)}.
\]
Then \(F'(t_*)>0\), \(Q(t_*)>0\), and as \(n\to\infty\),
\[
\begin{aligned}
t_n&=t_*+O(e^{-n^2/4}) &&\text{if }n\text{ is even},\\
t_n&=t_*-{c_*\over n^2}+O(n^{-4}) &&\text{if }n\text{ is odd}.
\end{aligned}
\]
Numerically, \(t_*\approx1.03788405470569\) and \(c_*\approx3.35455140586851\). These decimals are for orientation, not part of the exact definitions.

## Assumptions and scope

The vertex set is \(\mathbb Z/n\mathbb Z\times\{0,1\}\). The graph has horizontal edges along each cyclic layer and one rung between the two layers at each position. Thus, for \(r=\min(|i-j|,n-|i-j|)\),
\[
d((i,a),(j,b))=r+|a-b|.
\]
No weights, rescaling of the graph distance, or continuum-cylinder limit is assumed. The theorem is proved for each integer \(n\ge20\). It does not claim that no isolated positive-semidefinite intervals occur below \(t=1\); none are needed to determine the last-failure threshold.

## Proof

**1. Exact block spectrum.** Put \(a_r=e^{-tr^2}\), \(b_r=e^{-t(r+1)^2}\), \(g_r=a_r-b_r\), and \(h_r=a_r+b_r\). The Gaussian matrix has block form \(\left(\begin{smallmatrix}A&B\\B&A\end{smallmatrix}\right)\), where \(A\) and \(B\) are circulants with first rows \(a_{d_n(0,j)}\) and \(b_{d_n(0,j)}\), respectively. Symmetric and antisymmetric layer vectors diagonalize it into the two circulants \(A+B\) and \(A-B\). Write \(n=2m+1\) or \(n=2m\). The real trigonometric eigenvalue functions are, respectively,
\[
\begin{aligned}
L_{n,\pm}(\theta)&=w_0^{\pm}+2\sum_{r=1}^{m}w_r^{\pm}\cos(r\theta) &&(n=2m+1),\\
L_{n,\pm}(\theta)&=w_0^{\pm}+2\sum_{r=1}^{m-1}w_r^{\pm}\cos(r\theta)+w_m^{\pm}\cos(m\theta) &&(n=2m),
\end{aligned}
\]
where \(w_r^-=g_r\), \(w_r^+=h_r\), and sampled frequencies are \(\theta=2\pi k/n\). In the even case \(\cos(m\theta)=(-1)^k\).

**2. Uniform positivity and mode ordering for \(t\ge1\).** The symmetric-layer eigenvalues are strictly positive, since
\[
L_{n,+}(\theta)\ge1-2\sum_{r\ge1}(e^{-r^2}+e^{-(r+1)^2})
\ge1-2\left({e^{-1}\over1-e^{-3}}+{e^{-4}\over1-e^{-5}}\right)>0.
\]
The last inequality follows, for example, from \(e^{-1}<3/8\), \(e^{-3}<1/20\), \(e^{-4}<1/50\), and \(e^{-5}<1/100\). To order the antisymmetric modes, note that \(g_1\ge e^{-t}(1-e^{-3})\), while
\[
\sum_{r\ge2}r^2g_r\le e^{-t}\sum_{r\ge2}r^2e^{-(r^2-1)}
\le e^{-t}\sum_{r\ge2}r^2(1/20)^{r-1}<0.225e^{-t}<g_1.
\]
The elementary inequality \(|\sin(r\theta)|\le r\sin\theta\) for \(0<\theta<\pi\) now shows \(\partial_\theta L_{n,-}(\theta)<0\) in that interval. Consequently its least sampled eigenvalue is
\[
F_n(t)=L_{n,-}(\theta_n,t),\qquad
\theta_n=\begin{cases}\pi,&n\text{ even},\\\pi-\pi/n,&n\text{ odd}.\end{cases}
\]
For odd \(n\) the two conjugate frequencies realizing this minimum are distinct, while for even \(n\) there is only one.

**3. Strict increase of the least eigenvalue.** Differentiating \(g_0\) gives \(e^{-t}\), while \(g_1'=-e^{-t}+4e^{-4t}<0\) for \(t\ge1\); also \(\cos\theta_n<0\). All remaining derivative contributions obey
\[
F_n'(t)\ge e^{-t}-2\sum_{r\ge2}\bigl(r^2e^{-tr^2}+(r+1)^2e^{-t(r+1)^2}\bigr)>\tfrac12e^{-t}.
\]
Indeed, with \(y=1/20\), the sum divided by \(e^{-t}\) is at most
\[
\sum_{r\ge2}r^2y^{r-1}+\sum_{r\ge3}r^2y^{r-1}<1/4,
\]
using \(r^2-1\ge3(r-1)\) and \(e^{-3}<y\). This also passes to the infinite series \(F\), so \(F'(t)>0\) for \(t\ge1\).

**4. Existence and exact last-failure characterization.** The alternating series gives \(F(1)\le1-3e^{-1}+4e^{-4}< -0.028\). For \(n\ge20\), the error between \(F_n(1)\) and \(F(1)\) is bounded by
\[
\left({\pi\over n}\right)^2\sum_{r\ge1}r^2g_r(1)
+2\sum_{r\ge\lfloor n/2\rfloor}e^{-r^2}
<0.012.
\]
Here one uses \(|\cos(r(\pi-\delta))-(-1)^r|\le r^2\delta^2/2\), the bound of Step 2, and the Gaussian tail from \(r\ge10\). Hence \(F_n(1)<0\). Since \(\lim_{t\to\infty}F_n(t)=1\) and \(F_n\) is strictly increasing for \(t\ge1\), it has a unique root \(t_n>1\). Step 2 proves that the Gaussian matrix is positive semidefinite in that range precisely at and above this root, strictly positive above it, and has the asserted endpoint nullities. Because it is positive definite for all \(t>t_n\) and negative on the nonempty interval \([1,t_n)\), its last-failure supremum is exactly \(t_n\), irrespective of behavior for \(t<1\).

**5. Even/odd asymptotics.** Define the infinite trigonometric series
\[
L_{\infty,-}(\theta,t)=g_0(t)+2\sum_{r=1}^{\infty}g_r(t)\cos(r\theta).
\]
It and all fixed-order \(\theta,t\) derivatives converge absolutely and uniformly on compact subsets of \(t\ge1\). At \(\theta=\pi\) it equals \(F(t)\). The alternating identity in the statement follows by shifting the second Gaussian series in \(g_r\). Also
\[
\tfrac12\partial_\theta^2L_{\infty,-}(\pi,t)=Q(t)>0
\]
by Step 2. In the even case the finite/infinite difference at \(\pi\) is \(O(e^{-n^2/4})\), uniformly near \(t_*\); the inverse-function estimate from \(F'(t_*)>0\) gives the claimed even asymptotic. In the odd case the nearest sampled angle is \(\pi-\pi/n\), and Taylor expansion with Gaussian-tail control gives, uniformly near \(t_*\),
\[
F_n(t)=F(t)+{\pi^2Q(t)\over n^2}+O(n^{-4}).
\]
Implicit expansion about \(F(t_*)=0\) yields \(t_n=t_*-\pi^2Q(t_*)/[F'(t_*)n^2]+O(n^{-4})\), proving the odd asymptotic. The strict inequalities in Steps 2–3 show that no competing Fourier band can change this threshold.

## Verification

Run the accompanying standalone `check_prism.py` with Python 3. It independently constructs the distance-kernel matrix for representative even and odd prism orders, compares Fourier eigenpairs against direct multiplication, brackets the unique critical zeros, tests the signs immediately to either side, and checks convergence of the even and odd asymptotic quantities. Its numerical computations support, but do not replace, the analytic inequalities above.

## Relationship to prior work

Sánchez (2011) develops general supremal negative-type methods for finite metric spaces, not a bandwidth classification for squared-distance Gaussian kernels on prisms. Feragen–Lauze–Hauberg (2014) explain why geodesic Gaussian positivity for every bandwidth fails broadly in curved settings, but do not determine finite-prism last-failure cutoffs or parity corrections. Atik–Mondal–Parveen (2022) analyze the ordinary distance matrix spectrum of multilayer prism graphs; entrywise exponentiation of squared graph distance is not determined by that distance-matrix spectrum. Known discrete-cycle Gaussian cutoffs and wheel-graph cutoffs apply to different vertex sets and do not control the antisymmetric rung modes responsible for \(t_*\).

## Limitations

The exact classification of admissible \(t<1\) is not asserted. No sharp finite-order formula in elementary functions is claimed, and no uniform limit is claimed for other families of cylindrical width or rung weights. The decimals and finite checks are approximate. A wider equivalence hidden in older circulant-covariance or graph-kernel literature cannot be excluded by the bounded literature review; independent verification has not been performed.

## References

1. Stephen Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451, publicly posted 2011-08-02; https://arxiv.org/abs/1108.0451.
2. Aasa Feragen, François Lauze, and Søren Hauberg, *Geodesic Exponential Kernels: When Curvature and Linearity Conflict*, arXiv:1411.0296, publicly posted 2014-11-02; https://arxiv.org/abs/1411.0296.
3. Fouzul Atik, Priti Prasanna Mondal, and Firdoshi Parveen, *On the distance spectra of m-generation n-prism graph*, AKCE International Journal of Graphs and Combinatorics 19 (2022), 276–281, DOI:10.1080/09728600.2022.2137443.
