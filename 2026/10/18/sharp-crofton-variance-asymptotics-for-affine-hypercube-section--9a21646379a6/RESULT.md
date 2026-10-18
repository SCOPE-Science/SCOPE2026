# Sharp Crofton variance asymptotics for affine hypercube section vertices

## Finding
Let \(Q_n=[-1,1]^n\), with integer \(n\ge 3\). Choose an unoriented affine hyperplane by the Euclidean-motion-invariant measure on all such hyperplanes, conditioned on intersection with \(Q_n\). Denote the number of vertices of the section by \(V_n\). Then
\[
\mathbb E V_n=2^{n-1},\qquad
\lim_{n\to\infty}\frac{\operatorname{Var}(V_n)}{4^n\sqrt n}
=\frac1{2\sqrt2\,\pi}.
\]
In addition, \(V_n/2^{n-1}\to0\) in probability. The exact expectation is known from Swan's general k-flat result and is included as normalization; the asymptotic variance constant and corresponding typical-to-mean separation are the present findings.

## Assumptions and scope
The hyperplanes are not constrained to pass through the center. Parametrize a hyperplane by a unit normal \(u\in\mathbb S^{n-1}\) (with antipodal identification) and an offset \(s\), and use invariant density \(d\sigma(u)\,ds\) before conditioning on \(|s|\le\sum_i|u_i|\). As a result, normals under the conditioned law are *width-biased*, not uniform on the sphere. Almost surely no cube vertex lies on the sampled hyperplane, so the section vertices correspond bijectively to cut cube edges.

Set \(\mu=\mathbb E|G_1|=\sqrt{2/\pi}\) for independent standard Gaussians \(G_1,\dots,G_n\), and put \(L(G)=\sum_i|G_i|\). For every nonnegative degree-zero function of the normal and offset, the conditioned invariant average is
\[
\mathbb E_{\mathrm{aff}}F
=\frac1{2n\mu}\mathbb E_G\int_{-L(G)}^{L(G)}F(G,t)\,dt.
\]
The identity follows on writing \(G=Ru\): the extra radial factor in each offset integral cancels that in its normalizer.

## Proof
**1. Edge-interval representation.** There are \(M_n=n2^{n-1}\) cube edges. For an edge \(e\) along coordinate \(i\), with fixed signs \(\epsilon_j\in\{-1,1\}\) for \(j\ne i\), define
\[
I_e(G)=\Bigl[\sum_{j\ne i}\epsilon_jG_j-|G_i|,\;
\sum_{j\ne i}\epsilon_jG_j+|G_i|\Bigr].
\]
For almost all \((G,t)\), the section-vertex count is \(V(G,t)=\sum_e\mathbf1_{I_e(G)}(t)\). Integrating one interval and using symmetry yields
\[
\mathbb E V_n=\frac{M_n\,2\mu}{2n\mu}=2^{n-1}.
\]
For two independently chosen uniform cube edges \(E,F\), write \(\ell(E,F,G)=|I_E(G)\cap I_F(G)|\). Squaring the preceding indicator sum proves the exact identity
\[
\mathbb E V_n^2=\frac{M_n^2}{2n\mu}\,
\mathbb E_{E,F,G}\ell(E,F,G).
\tag{1}
\]

**2. Negligibility of same-coordinate pairs.** The edges \(E,F\) have the same free-coordinate direction with probability \(1/n\). Their overlap is bounded by \(2|G_i|\), of mean \(2\mu\), so their contribution to \(\sqrt n\,\mathbb E\ell\) is at most \(2\mu/\sqrt n\), which vanishes.

**3. Overlap of different directions.** Conditional on different directions \(i\ne j\), the two half-lengths are independent \(A=|G_i|\) and \(B=|G_j|\). The difference of interval centers is distributed as
\[
D=Z+\sigma A+\tau B,\qquad
Z\mid H\sim N(0,4H),\qquad
H\sim\operatorname{Bin}(n-2,1/2),
\]
where \(\sigma,\tau\) are independent symmetric signs, independent of \(A,B,H,Z\). Indeed, each of the remaining \(n-2\) endpoint signs differs with probability \(1/2\), contributing an independent \(\pm2G_k\). Let
\[
K_{a,b}(x)=\big|[-a,a]\cap[x-b,x+b]\big|.
\]
By Fubini, for all \(a,b\ge0\),
\[
\int_{\mathbb R}K_{a,b}(x)\,dx=4ab.
\tag{2}
\]
On the event \(H\ge n/4\), the density of \(Z\) is bounded by \((2\pi n)^{-1/2}\), and for each fixed \(x\) and fixed \(a,b\) its density at \(x-\sigma a-\tau b\), multiplied by \(\sqrt n\), converges in probability to \(1/\sqrt{4\pi}\), since \(H/n\to1/2\). The bound and (2) provide the integrable dominating envelope \(4AB/\sqrt{2\pi}\). On \(H<n/4\), the probability is exponentially small, while \(K_{A,B}\le2A\); hence the contribution after multiplication by \(\sqrt n\) also vanishes. Dominated convergence therefore gives
\[
\lim_{n\to\infty}\sqrt n\,
\mathbb E\bigl[\ell(E,F,G)\mid i\ne j\bigr]
=\frac{4\mathbb E A\,\mathbb E B}{\sqrt{4\pi}}
=\frac{2\mu^2}{\sqrt\pi}.
\tag{3}
\]
Combining (1) with (3), the same-coordinate estimate, and \(M_n=n2^{n-1}\), obtains
\[
\lim_{n\to\infty}
\frac{\mathbb E V_n^2}{4^n\sqrt n}
=\frac1{8\mu}\frac{2\mu^2}{\sqrt\pi}
=\frac1{2\sqrt2\,\pi}.
\]
Finally, \((\mathbb E V_n)^2/(4^n\sqrt n)=1/(4\sqrt n)\to0\), proving the stated variance limit.

**4. Separation of typical and expected complexity.** In the Gaussian representation the law of \(G\) is tilted by \(L(G)/(n\mu)\), and conditional on it, \(t=U L(G)\) with independent \(U\sim\operatorname{Unif}[-1,1]\). For any fixed \(\delta\in(0,1)\), outside an event whose tilted probability tends to zero, we have
\[
L(G)\ge n\mu/2,\quad\sum_iG_i^2\le2n,\quad
\max_i|G_i|\le\delta\mu n/4.
\]
This follows from ordinary Gaussian concentration and Cauchy–Schwarz for the width tilt, because \(\mathbb E[L(G)^2]/(n\mu)^2\) remains bounded. If also \(|U|\ge\delta\), an edge in direction \(i\) can be cut only when a signed sum of the other Gaussian coordinates has magnitude at least \(\delta\mu n/4\). Conditional on \(G\), the subgaussian Rademacher tail inequality bounds the fraction of cut edges in any one direction by
\[
2\exp(-\delta^2\mu^2 n/64).
\]
There are \(n\) directions; hence on the stated event,
\[
\frac{V_n}{2^{n-1}}\le
2n\exp(-\delta^2\mu^2 n/64).
\]
Since \(\Pr(|U|<\delta)=\delta\), for every fixed positive threshold the limiting exceedance probability is at most \(\delta\). Letting \(\delta\downarrow0\) proves \(V_n/2^{n-1}\to0\) in probability.

## Verification
The included standalone file `checks/verify.py` implements two independently sampled checks. Direct width-biased Gaussian hyperplane simulation reproduces the known finite-dimensional expectation for dimensions three through five. Separate independent interval-overlap simulation tests the exact second-moment representation in dimensions eight through 512 and approaches the sharp asymptotic constant. A deterministic seed and explicit tolerances are supplied. The numerical tests are supplementary; the proof above establishes the infinite-dimensional claims.

## Relationship to prior work
Swan proved the mean count \(2^{n-1}\) (indeed the more general \(2^k\) for affine \(k\)-flats through the cube under the stated conditional translation measure). That mean is not new. Lonke's random-cube-section results instead sample *central linear* sections using Haar Grassmannian measure; conditioning the affine law on offset zero changes the distribution, and its formulas do not imply the variance stated here. Brandenburg and Meroni study the **finite-dimensional combinatorial census** of cube slices through dimension six; an all-dimensional asymptotic variance is not a finite census consequence. Birkemeyer, Brose, Brandenburg, and Prün (2026) study face-lattice reconstruction and combinatorial slicing inequalities; their full accessible text contains no random-plane expectation or variance theorem. Related published comparisons involving Haar central sections have a different sampling law.

## Limitations
The result applies to the cube and to Euclidean-motion-invariant *affine* hyperplane sampling conditioned on intersection. It does not claim the same variance under Haar-uniform central section sampling, uniformly sampled offsets without the requisite width-biased orientation, arbitrary parallelepipeds, or other face dimensions. The limit is not an exact finite-dimensional variance formula. Literature comparison supports originality to the extent of the sources read; older or unindexed equivalent results remain a residual risk. Independent external validation has not been performed.

## References
1. H. Swan, “Expected Number of Vertices of a Hypercube Slice,” *American Mathematical Monthly* **123** (2016), 600–604; arXiv:1808.09482, https://arxiv.org/html/1808.09482v1.
2. Y. Lonke, “On random sections of the cube,” arXiv:math/9812123 (1998), https://arxiv.org/html/math/9812123v1.
3. M.-C. Brandenburg and C. Meroni, “Combinatorics of slices of cubes,” arXiv:2510.09265 (2025), https://arxiv.org/abs/2510.09265.
4. A. Birkemeyer, A. E. Brose, M.-C. Brandenburg, and N. Prün, “Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices,” arXiv:2609.16195, first public September 14, 2026, https://arxiv.org/abs/2609.16195.
