# The annealed metric law of spherical Voronoi interfaces

## Finding

Let \(n\geq2\) sites be independently uniformly distributed on the unit sphere \(S^2\). Form the geodesic nearest-site Voronoi tessellation, count each interface between two cells exactly once, and let \(L_n\) be the sum of the intrinsic lengths of all interfaces. There is an exact finite-sample length law:
\[
\mathbb E L_n=4\pi(n-1)\frac{\binom{2n-2}{n-1}}{4^{n-1}}.
\]
This includes \(\mathbb E L_2=2\pi\), \(\mathbb E L_3=3\pi\), and \(\mathbb E L_4=15\pi/4\). In the many-site regime,
\[
\mathbb E L_n=4\sqrt{\pi n}\left(1-\frac{5}{8n}+O(n^{-2})\right).
\]

The sharper statement concerns the **annealed length-weighted interface**. For an interface point \(z\) between sites \(X_i\) and \(X_j\), define its common cosine height \(c=\langle z,X_i\rangle=\langle z,X_j\rangle\), the transformed height \(U=(1+c)/2\), the squared chord between the two generating sites \(Q=\|X_i-X_j\|^2\), and \(V=Q/[16U(1-U)]\). Under the probability measure obtained by taking expected arclength and normalizing by \(\mathbb E L_n\), these variables have the exact representation
\[
U\sim\operatorname{Beta}\left(n-\frac12,\frac32\right),\quad
V\sim\operatorname{Beta}\left(1,\frac12\right),\quad U\ \text{and}\ V\ \text{independent},\quad Q=16U(1-U)V.
\]
In particular, for every integer \(k\geq0\),
\[
\mathbb E_{\mathrm{len}}[Q^k]
=\frac{16^k k!\,(n-\tfrac12)_k}{(n+1)_{2k}},
\]
where \((a)_k=\prod_{j=0}^{k-1}(a+j)\) denotes the rising factorial. As \(n\to\infty\),
\[
\frac{nQ}{16}\ \Longrightarrow\ \operatorname{Exp}(1),
\]
with convergence of every fixed positive integer moment.

## Assumptions and scope

The sphere has curvature one and ordinary surface-area measure \(\sigma\) with \(\sigma(S^2)=4\pi\). Sites \(X_1,\ldots,X_n\) are independent, identically distributed according to \(\sigma/(4\pi)\). Each closed Voronoi cell is
\[
C_i=\{z\in S^2:\langle z,X_i\rangle\geq\langle z,X_j\rangle\ \text{for every}\ j\}.
\]
Let \(B_{ij}=C_i\cap C_j\), and define \(L_n=\sum_{1\leq i<j\leq n}\mathcal H^1(B_{ij})\). For \(n\geq3\), triple-tie vertices have zero arclength almost surely; for \(n=2\), the sole interface is one entire great circle. Consequently this expression counts geometric interface length without multiplicity.

The notation \(\mathbb E_{\mathrm{len}}\) denotes a deterministic, **annealed**, length-biased law, not the law obtained by first choosing a random tessellation and then normalizing by that configuration's random total length. Formally, for every bounded Borel test function \(g\),
\[
\mathbb E_{\mathrm{len}}g(U,Q)=
\frac{\displaystyle\mathbb E\left[\sum_{i<j}\int_{B_{ij}}g\left(\frac{1+\langle z,X_i\rangle}{2},\|X_i-X_j\|^2\right)d\mathcal H^1(z)\right]}{\mathbb E L_n}.
\]
The law of \(V\) is the corresponding pushforward on the full-measure set \(U\in(0,1)\). All statements hold for every integer \(n\geq2\), without a generic-position restriction imposed on the sampling model.

## Proof

**Step 1: coarea and the empty-cap event.** For a fixed unordered pair \(i<j\), put \(F_{ij}(z)=\langle z,X_i-X_j\rangle\). Its zero set is the bisector great circle, and on that zero set the intrinsic gradient has norm \(\|\nabla_{S^2}F_{ij}\|=\|X_i-X_j\|\). The coarea formula therefore gives, with harmless removal of the arclength-null triple ties,
\[
\int_{B_{ij}}h(z,X_i,X_j)\,d\mathcal H^1(z)
=\int_{S^2}\delta(F_{ij}(z))\,\|X_i-X_j\|\,
\mathbf1\{\langle z,X_k\rangle\leq\langle z,X_i\rangle\ \forall k\ne i,j\}
\,h(z,X_i,X_j)\,d\sigma(z).
\]
The Dirac notation can be justified by replacing \(\delta\) by a symmetric approximate identity; almost-sure transversality and bounded test functions permit passage to the limit on the compact sphere. Rotational invariance allows fixing \(z\) at the north pole in its expectation.

**Step 2: the exact unnormalized pair law.** Write the two site heights relative to \(z\) as \(c_i,c_j\), each uniform on \([-1,1]\), and their independent azimuths as \(\psi_i,\psi_j\). On the coarea constraint \(c_i=c_j=c\), the relative azimuth \(\Delta=(\psi_i-\psi_j)\bmod2\pi\) is uniform on \([0,2\pi)\). The chord length is
\[
\|X_i-X_j\|=2\sqrt{1-c^2}\sin(\Delta/2).
\]
Each of the other \(n-2\) sites lies no closer to \(z\) than the pair with probability \(((1+c)/2)^{n-2}\), independently. The sphere's surface factor \(4\pi\), the joint height density \(1/4\), and the relative-azimuth density \(1/(2\pi)\) cancel the factor two in the gradient. Hence the unnormalized expected length measure associated with one pair has **exact density**
\[
\sqrt{1-c^2}\sin(\Delta/2)
\left(\frac{1+c}{2}\right)^{n-2}
\,dc\,d\Delta,
\qquad -1<c<1,\quad0<\Delta<2\pi.
\]
This is an identity for expected arclength, rather than a statement about the distribution at a uniformly chosen random tessellation.

**Step 3: beta factorization and total length.** Substitution \(u=(1+c)/2\) gives the factor \(4u^{n-3/2}(1-u)^{1/2}du\); the angular factor integrates to \(\int_0^{2\pi}\sin(\Delta/2)d\Delta=4\). Thus the expected length of one labelled interface is \(16B(n-\tfrac12,\tfrac32)\), and
\[
\mathbb E L_n=16\binom n2B\left(n-\frac12,\frac32\right).
\]
For integer \(n\), the gamma-function identity \(\Gamma(n-\tfrac12)=\sqrt\pi\,(2n-2)!/[4^{n-1}(n-1)!]\) simplifies this expression to the finite-sample formula in the finding. The centered-binomial-coefficient expansion
\[
\frac{\binom{2m}{m}}{4^m}=
\frac1{\sqrt{\pi m}}\left(1-\frac1{8m}+O(m^{-2})\right)
\]
with \(m=n-1\) gives the stated two-term perimeter asymptotic.

For the joint law, let \(Z=\cos(\Delta/2)\). The normalized angular density proportional to \(\sin(\Delta/2)d\Delta\) pushes forward to the uniform law on \([-1,1]\). It is independent of \(U\), which has beta parameters \((n-\tfrac12,\tfrac32)\) by the radial factor above. Since \(V=\sin^2(\Delta/2)=1-Z^2\), its distribution is \(\operatorname{Beta}(1,\tfrac12)\); the squared chord is \(Q=16U(1-U)V\). This proves the full joint claim.

**Step 4: all moments and the limit.** Independence and the beta moment formula yield
\[
\mathbb E_{\mathrm{len}}[Q^k]
=16^k\frac{(n-\tfrac12)_k(\tfrac32)_k}{(n+1)_{2k}}
\frac{(1)_k}{(\tfrac32)_k},
\]
which reduces to the asserted expression. The variable \(T_n=n(1-U)\) converges in law and all fixed moments to a \(\Gamma(\tfrac32,1)\) variable \(G\), while \(U\to1\) in probability. The independent \(V\) remains beta distributed. The beta-gamma multiplication identity implies \(GV\sim\Gamma(1,1)=\operatorname{Exp}(1)\), because \(G\sim\Gamma(1+\tfrac12,1)\) and \(V\sim\operatorname{Beta}(1,\tfrac12)\) are independent. Consequently \(nQ/16=U T_n V\Rightarrow GV\), and the exact moment formula above gives convergence of every fixed moment directly.

## Verification

The companion self-contained `verify.py` uses two distinct checks. It evaluates the beta integral and the central-binomial closed form independently in floating-point arithmetic while confirming the rational chord-moment identities exactly with `fractions.Fraction`. It also reconstructs random realized Voronoi diagrams by intersecting pair-bisector great circles with all required spherical halfspaces. Exact trigonometric interval integration returns each realization's total arclength, arclength-weighted transformed height, and arclength-weighted generator chord square. Deterministically seeded sampling for several site counts agrees with the theoretical values within stated tolerances. Execute with `python3 verify.py`; success prints `ALL_EXACT_MOMENT_AND_GEOMETRIC_CHECKS_PASSED`. The finite simulations are independent consistency checks and are not used as proofs of the infinite-sample assertions.

## Relationship to prior work

Hug and Reichenbacher's 2017 study of random tessellations in spherical space establishes geometric and stochastic models and the asymptotic shape behavior of spherical Poisson–Voronoi cells; its focus is a Poisson input and large-cell deviations, not the finite-binomial arclength-weighted two-generator law here. Kabluchko and Thäle's 2019 preprint (journal version 2021) develops the binomial spherical Voronoi model and exactly identifies its **face-number** distributions using beta-prime polytopes. Its enumerative duality does not determine the **metric lengths** of interfaces or the distances between the two generating sites under arclength weighting. Classical work by Miles on sphere tessellations and Muche on Euclidean Poisson–Voronoi edges is relevant historical background; full original inspection of Miles's 1971 paper was not possible, leaving a specific priority risk. The present claim does not assert that the Voronoi construction, coarea principle, or beta-gamma identity is itself new.

## Limitations

The probability law is annealed and length weighted: it is not a quenched law conditional on a site configuration, nor a distribution of the length of a uniformly selected combinatorial edge. It applies only to independent **uniform** sites on the unit two-sphere, not to other input laws or higher dimensions. The theorem does not describe interface lengths individually, area statistics, variance of total length, or error bounds for convergence to the exponential limit. Historical priority awaits examination of inaccessible older primary literature, and no independent mathematical audit has been performed.

## References

1. D. Hug and A. Reichenbacher, *Geometric inequalities, stability results and Kendall's problem in spherical space*, arXiv:1709.06522, publicly posted 19 September 2017, especially the original sections on spherical Poisson–Voronoi tessellations: https://arxiv.org/abs/1709.06522.
2. Z. Kabluchko and C. Thäle, *The Typical Cell of a Voronoi Tessellation on the Sphere*, arXiv:1911.07221, first posted 17 November 2019; *Discrete & Computational Geometry* **66** (2021), 1330–1350, doi:10.1007/s00454-021-00315-2: https://link.springer.com/article/10.1007/s00454-021-00315-2.
3. R. E. Miles, *Random points, sets and tessellations on the surface of a sphere*, *Sankhyā*, Series A **33** (1971), 145–174: https://www.jstor.org/stable/25049720. Cited as a plausible historical comparison, not claimed to have been read in full.
4. L. Muche, *The Poisson–Voronoi tessellation: relationships for edges*, *Advances in Applied Probability* **37** (2005), 279–296. A Euclidean homogeneous-Poisson model, not the spherical finite-binomial model.
