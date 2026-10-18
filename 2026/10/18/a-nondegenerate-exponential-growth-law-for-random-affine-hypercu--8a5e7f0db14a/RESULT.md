# A nondegenerate exponential-growth law for random affine hypercube sections

## Finding

For every integer \(n\ge3\), let \(Q_n=[-1,1]^n\). Draw an unoriented affine hyperplane from the Euclidean-motion-invariant measure, conditioned on intersecting \(Q_n\), and let \(V_n\) be the number of vertices of its generic section. Set \(\mu=\sqrt{2/\pi}\), let \(Z\) be a standard normal variable, and define for \(0\le x<\mu\)
\[
\Lambda(\lambda)=\mathbb E\log\cosh(\lambda |Z|),\qquad
I(x)=\sup_{\lambda\ge0}\{\lambda x-\Lambda(\lambda)\}.
\]
Extend continuously to \(I(\mu)=\log2\). If \(U\) is uniform on \([0,1]\), then
\[
\boxed{\frac{\log V_n}{n}\ \Longrightarrow\ Y=\log2-I(\mu U).}
\]
This is a nonconstant law supported on \([0,\log2]\). For \(0\le y\le\log2\), its exact distribution function is
\[
\boxed{\mathbb P(Y\le y)=1-\frac{I^{-1}(\log2-y)}{\mu}.}
\]
At the endpoints, the distribution has the sharp expansions
\[
\mathbb P(Y\le y)=\frac3\pi y^2+O(y^4)\quad(y\downarrow0),
\qquad
\mathbb P(Y>\log2-y)=\sqrt{\pi y}+O(y^{3/2})\quad(y\downarrow0).
\]
The exact mean, for all \(n\ge3\), is \(\mathbb E V_n=2^{n-1}\), an identity already covered by known mean-section results and not proposed as new. In contrast, the present limit proves
\[
\boxed{\frac{V_n}{2^{n-1}}\longrightarrow0\quad\text{in probability}.}
\]
Thus the exact expectation is sustained by increasingly rare exceptionally large sections, while typical sections have a random exponential rate. For orientation-independent relative offset \(U=1/2\), the limiting median log-growth rate is \(0.6064132549\ldots\), versus the mean-growth exponent \(\log2=0.6931471806\ldots\).

## Assumptions and scope

The invariant hyperplane measure is represented by \(d\sigma(u)\,dt\) with \(u\in S^{n-1}\) and signed offset \(t\in\mathbb R\), identifying \((u,t)\) with \((-u,-t)\); normalization after conditioning makes orientation density proportional to the width \(2\sum_i|u_i|\), and conditional on orientation the offset is uniform in \([-\sum_i|u_i|,\sum_i|u_i|]\). Intersections containing a cube vertex have measure zero and can be excluded. Logarithms are natural. The convergence is in distribution across dimensions, not a finite-\(n\) error bound; the endpoint expansions describe the limiting law.

## Proof

**1. Boolean graph reduction.** The generic section vertices correspond bijectively to cube edges crossed by the hyperplane. By symmetry replace the coordinate normal magnitudes by positive numbers \(w_i\), and take the signed offset nonnegative. Let \(S=\sum_iw_i\), \(t=uS\) with \(u\in[0,1]\). Denote by \(A_n\) the subset of Boolean vertices \(\varepsilon\in\{-1,1\}^n\) satisfying \(\sum_i w_i\varepsilon_i>t\). The number \(V_n\) equals the Boolean edge boundary \(|\partial A_n|\). For \(t>0\), antipodal symmetry gives \(0<|A_n|\le 2^{n-1}\). The cube edge-isoperimetric inequality and the degree bound imply
\[
|A_n|\log_2(2^n/|A_n|)\le |\partial A_n|\le n|A_n|,
\quad\text{and hence}\quad |A_n|\le V_n\le n|A_n|.
\]
For completeness, prove the lower inequality by induction on \(n\): split \(A_n\) into layers of cardinalities \(a,b\), use the induction bound on each layer, and note that the between-layer edge boundary has at least \(|a-b|\) edges. The remaining numerical inequality is \(H_2(p)+|2p-1|\ge1\), for \(p=a/(a+b)\), where \(H_2\) is binary entropy. It follows from concavity of \(H_2\) above the chords joining \((0,0)\), \((1/2,1)\), and \((1,0)\). Therefore \(n^{-1}\log V_n=n^{-1}\log|A_n|+O(\log n/n)\) uniformly over hyperplanes not through vertices.

**2. Unbiased Gaussian realization and correct conditioning.** Let \(G_i\) be independent standard Gaussians and put \(W_n=\sum_{i=1}^n|G_i|\). A Haar normal has the same distribution as \(G/\|G\|_2\). Under conditioned invariant hyperplane sampling, Gaussian directions have probability density tilted by \(W_n/\|G\|_2\); an independent relative offset \(U\) remains uniform on \([0,1]\). The strong law gives \(W_n/n\to\mu\) and \(\|G\|_2/\sqrt n\to1\); the tilt divided by \(\sqrt n\) tends to \(\mu\) almost surely and is bounded by one by Cauchy–Schwarz. Dominated convergence implies that its normalized density converges to one in \(L^1\), so the tilted and untilted Gaussian-direction distributions have total-variation distance tending to zero. It suffices to establish the claimed distributional limit for the untilted independent Gaussian weights and independent \(U\).

**3. A quenched weighted-Rademacher large deviation.** Conditional on fixed weights \(w_i=|G_i|\), a uniformly sampled Boolean sign vector has weighted sum \(S_n=\sum_i w_i\varepsilon_i\), with log-moment generating function \(n\Lambda_n(\lambda)=\sum_i\log\cosh(\lambda w_i)\). By the strong law, \(\Lambda_n(\lambda)\to\Lambda(\lambda)\) locally uniformly in \(\lambda\): the functions are equi-Lipschitz on each finite interval with random Lipschitz constant \(n^{-1}\sum_iw_i\to\mu\). Furthermore \(\Lambda'(\lambda)=\mathbb E[|Z|\tanh(\lambda|Z|)]\) increases strictly from zero to \(\mu\), and \(\Lambda''(\lambda)>0\). For each fixed \(a\in(0,\mu)\), Chernoff's inequality gives
\[
\limsup_{n\to\infty}\frac1n\log\mathbb P_\varepsilon(S_n/n>a)\le-I(a).
\]
For the reverse inequality, fix \(b\in(a,\mu)\) and tilt the conditional signs by the unique positive \(\lambda_b\) solving \(\Lambda'(\lambda_b)=b\). Under this tilted law the sum divided by \(n\) tends in probability to \(b\): its mean tends to \(b\), and its variance is at most \(n^{-2}\sum_iw_i^2\to0\). Restricting to \([b-\delta,b+\delta]\subset(a,\mu)\), and undoing the exponential tilt, yields the lower exponential bound \(\Lambda(\lambda_b)-\lambda_b(b+\delta)\). Let \(\delta\downarrow0\), then \(b\downarrow a\), to obtain the opposite inequality. Hence the quenched limit is exactly \(-I(a)\). As \(W_n/n\to\mu\), squeezing thresholds gives, for every fixed \(u\in(0,1)\),
\[
\frac1n\log\bigl(2^n\mathbb P_\varepsilon\{S_n>uW_n\}\bigr)
\longrightarrow\log2-I(\mu u).
\]
The quantity in parentheses equals \(|A_n|\). The uniform Boolean boundary comparison from step 1 transfers the logarithmic limit to \(V_n\). Coupling an independent uniform \(U\), ignoring its measure-zero endpoints, and reverting the asymptotically negligible width tilt completes the distributional convergence.

**4. Exact mean, endpoint expansions, and mean-typical separation.** Fix a normal vector with all coordinates nonzero. There are \(2^{n-1}\) cube edges parallel to coordinate \(i\); each is crossed for an offset interval of length \(2|u_i|\). Integrating the number of crossing edges over the full allowable offset interval of length \(2\sum_i|u_i|\) gives \(2^{n-1}\) regardless of orientation. This recovers the known exact mean.

Near zero, \(\Lambda(\lambda)=\lambda^2/2+O(\lambda^4)\), so \(I(x)=x^2/2+O(x^4)\) and \(\log2-Y=U^2/\pi+O(U^4)\). For large \(\lambda\), using \(\log\cosh z=z-\log2+\log(1+e^{-2z})\), the half-normal density at zero \(\mu\), and \(\int_0^\infty\log(1+e^{-s})\,ds=\pi^2/12\), obtain
\[
\Lambda(\lambda)=\mu\lambda-\log2+
\frac{\mu\pi^2}{24\lambda}+O(\lambda^{-3}).
\]
Legendre inversion then yields \(Y=\sqrt{\pi/3}\sqrt{1-U}+O((1-U)^{3/2})\) as \(U\uparrow1\). Inverting these two monotone endpoint relations gives the stated distribution tails. Since \(I(\mu u)>0\) for every \(u>0\), the limiting exponent satisfies \(Y<\log2\) almost surely, and consequently \(V_n/2^{n-1}\to0\) in probability.

## Verification

Run `python3 check_affine_cube.py` using the standard Python 3 library. The program tests the exact Boolean edge correspondence and isoperimetric comparisons, integrates the offset piecewise to reproduce the exact mean for random finite weights, numerically computes the rate function by deterministic quadrature, and tests its strict monotonicity and both endpoint constants. Expected diagnostic: `AFFINE_CUBE_RANDOM_EXPONENT_OK comparisons=155`. The finite checks are supportive only; in particular they do not certify the asymptotic large-deviation step, which is proved above.

## Relationship to prior work

Lonke's *On random sections of the cube* (arXiv:math/9812123) derives expectations and asymptotics for central random sections, not the noncentral invariant-plane exponential law. Swan's *Expected Number of Vertices of a Hypercube Slice* (2016, arXiv:1808.09482) proves the mean \(2^k\) for a uniformly translated \(k\)-dimensional section with arbitrary orientation distribution. Thus the exact mean in the present statement is explicitly **prior art**, and the new contribution is the nondegenerate logarithmic limit and its explicit distributional endpoint laws. Cho and Kim (arXiv:1512.07768) provide exact clipped-hypercube volume formulas, not random hyperplane edge-boundary growth laws. De Loera, Lopez-Campos and Torres (arXiv:2412.12419) treat maximal attainable vertex counts and gaps in finite-dimensional slice sequences, rather than the probabilistic scaling limit. Bárány and Domokos (arXiv:2310.18960) consider direction-independent mean polygon counts for three-dimensional polytopes. Distinct earlier work on central cube sections fixes the offset at zero, whereas the present motion-invariant model samples its full width and weights orientations appropriately. Broad combinatorial and large-deviation connections are acknowledged as possible historical overlap risks, not resolved priority claims.

## Limitations

Only axis-aligned equal-side Euclidean cubes and invariant affine codimension-one hyperplane sampling are treated. The proof gives weak convergence of logarithmic vertex numbers, not a convergence rate or a limit for normalized vertex counts without logarithms. The mean formula is known; the asymptotic random-growth law has received self-review only and needs independent mathematical and historical-priority review. The 2008 Calkin et al. probabilistic cube-cut study could be checked only through its indexed abstract, and a 1991 cube-slicing article by Chakerian and Logothetti was not available in inspectable full text. Related fixed-event probabilities may be useful for an independent derivation; priority cannot be ruled out.

## References

1. Y. Lonke, *On random sections of the cube*, initial public arXiv version 21 December 1998, arXiv:math/9812123.
2. Y. Cho and S. Kim, *Volume of Hypercubes Clipped by Hyperplanes and Combinatorial Identities*, initial public arXiv version 24 December 2015, arXiv:1512.07768 (revised version inspected).
3. H. Swan, *Expected Number of Vertices of a Hypercube Slice*, *American Mathematical Monthly* 123 (2016), 600–604; full open preprint arXiv:1808.09482.
4. J. A. De Loera, G. Lopez-Campos and A. J. Torres, *On the Number of Vertices in Hyperplane Cross-Sections of Convex Polytopes*, arXiv:2412.12419, full open version inspected.
5. I. Bárány and G. Domokos, *Same average in every direction*, *Bull. Math. Soc. Sci. Math. Roumanie* 67 (2024), 125–138, arXiv:2310.18960.
6. P. E. O'Neil, *Hyperplane cuts of an n-cube*, *Discrete Mathematics* 1 (1971), 193–195. Historical context concerning maximal cuts, abstract inspected.
7. G. D. Chakerian and D. Logothetti, *Cube Slices, Pictorial Triangles, and Probability*, *Mathematics Magazine* 64 (1991), 219–241; full text not inspected.
8. N. Calkin, K. James, J. B. Light, R. Myers, E. Riedl, and V. Thomas, *Cuts of the Hypercube* (2008); indexed abstract inspected, full text inaccessible.
