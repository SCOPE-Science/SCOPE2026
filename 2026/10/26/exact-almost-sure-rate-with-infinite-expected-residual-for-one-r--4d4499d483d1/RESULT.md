# Exact almost-sure rate with infinite expected residual for one-row sketched GMRES(1)

## Finding
Let \(A\in\mathbb R^{2\times2}\) be real symmetric, invertible, and have distinct eigenvalues \(a,b\). Let the deterministic initial residual \(r_0\ne0\) have nonzero projection on *both* eigenspaces. At step \(k\ge1\), independently draw \(s_k\sim N(0,I_2)\), solve the one-dimensional **sketched** minimal-residual problem
\[\alpha_k\in\operatorname{argmin}_{t\in\mathbb R}|s_k^{\mathsf T}(r_{k-1}-t A r_{k-1})|,\qquad r_k=r_{k-1}-\alpha_k A r_{k-1}.\]
Then, almost surely, each minimum is unique, none of the iterates vanishes, and
\[\boxed{\lim_{k\to\infty}\frac1k\log\frac{\|r_k\|_2}{\|r_0\|_2}=\log\frac{|a-b|}{|a|+|b|}.}\]
For each integer \(k\ge1\) and real \(p\ge1\), \(\mathbb E\|r_k\|_2^p=+\infty\). If \(ab>0\), this gives exponential almost-sure residual convergence with exact factor \((\kappa-1)/(\kappa+1)\), where \(\kappa=\max(|a|,|b|)/\min(|a|,|b|)\). If \(ab<0\), the exponent equals zero; no stronger limit is claimed. The exceptional initial eigenvectors and scalar matrices terminate in one step.

## Assumptions and scope
All computations use exact real arithmetic and an independently regenerated, unnormalized Gaussian row at **every** iteration. The update is restarted sketched GMRES of degree one (search direction equal to the current residual), not a full-dimensional sketched Krylov method. The Euclidean residual is the true residual; the scalar absolute value above is the deliberately underdetermined **sketched** residual. For a consistent system \(Ax=f\), the residual convention is \(r=f-Ax\), giving \(x^+=x+\alpha r\). No assertion concerns floating-point safeguards, higher dimensions, nonsymmetric matrices, or other sketch distributions.

## Proof
Orthogonally diagonalize \(A\); Gaussian isotropy preserves the sketch law. Write \(A=\operatorname{diag}(a,b)\), \(r=(u,v)\), \(s=(X,Y)\). Except on an event of probability zero, the minimizing scalar is \(\alpha=(Xu+Yv)/(aXu+bYv)\). Direct expansion yields the **exact residual identity**
\[r^+=\frac{(b-a)uv}{aXu+bYv}(Y,-X).\tag{1}\]
When \(uv\ne0\), the updated vector is never zero and has both components nonzero with probability one. Conditional on any preceding residual, the direction of \(r^+\) modulo sign is the perpendicular to the freshly drawn isotropic sketch. Hence its angle \(\theta^+\) modulo \(\pi\) is uniform and independent of the past; the orientations after successive steps are independent uniform directions, although the logarithmic norm increments share adjacent sketches.

Put \(s/\|s\|=(\cos\phi,\sin\phi)\), \(r/\|r\|=(\cos\theta,\sin\theta)\). Formula (1) gives the norm multiplier
\[M(\theta,\phi)=\frac{|b-a|\,|\cos\theta\sin\theta|}{|a\cos\phi\cos\theta+b\sin\phi\sin\theta|}.\tag{2}\]
For \(k\ge2\), the two random angles used in (2) are individually uniform and independent, and successive log multipliers are one-dependent. Their absolute expectations are finite: logarithmic singularities of nontrivial linear trigonometric forms are integrable, and \(a,b\ne0\). Separate the even and odd multipliers into independent identically distributed subsequences and apply the strong law of large numbers to both.

The needed exact angular identities, for uniform \(\Theta,\Phi\in[0,2\pi)\), are
\[\mathbb E\log|\cos\Theta\sin\Theta|=-2\log 2,\]
\[\mathbb E_\Phi\log|a\cos\Phi\cos\theta+b\sin\Phi\sin\theta|=\tfrac12\log(a^2\cos^2\theta+b^2\sin^2\theta)-\log2,\]
\[\tfrac12\mathbb E_\Theta\log(a^2\cos^2\Theta+b^2\sin^2\Theta)=\log\frac{|a|+|b|}{2}.\]
All follow from \(\frac1{2\pi}\int_0^{2\pi}\log|c\cos t+d\sin t|\,dt=\log(\sqrt{c^2+d^2}/2)\), with the last identity alternatively obtained by factoring a complex linear polynomial on the unit circle. Substitution into \(\mathbb E\log M\) gives \(\log|b-a|-\log(|a|+|b|)\), as claimed. The initial logarithmic increment is finite almost surely and disappears after normalization by \(k\).

For the moment assertion, condition on any \(r=(u,v)\) with \(uv\ne0\). Decompose the new Gaussian sketch into independent standard-normal coordinates \(T,W\), parallel and perpendicular to \(Ar\). The denominator in (1) is \(\|Ar\|T\), whereas the perpendicular Gaussian coordinate contributes a nonzero \(W\)-term to the numerator \((Y,-X)\). Therefore \(\|r^+\|\ge C(r)|W/T|\) for some deterministic conditional constant \(C(r)>0\). Since \(\mathbb E|T|^{-p}=\infty\) for every \(p\ge1\), \(\mathbb E[\|r^+\|^p\mid r]=\infty\). The preceding nonzero-coordinate property permits iteration for every \(k\). When \(ab>0\), the rate is strictly negative; when \(ab<0\), \(|a-b|=|a|+|b|\). The classical deterministic optimal stationary Richardson worst-case rate on a definite two-point spectrum is \((\kappa-1)/(\kappa+1)\).

## Verification
Run the included standalone Python checker `verify.py` (Python 3, SymPy). It verifies the exact symbolic identity (1), orthogonality of the updated residual to the sketch, representative logarithmic angular integrals, large-sample pathwise exponents on positive, negative and indefinite spectra, and rational sketches approaching the singular denominator. The finite checks corroborate, but do not prove, the infinite-time and infinite-moment assertions. The latter are proved above using the strong law and a singular normal inverse moment.

## Relationship to prior work
Nakatsukasa and Tropp (2021) define and motivate sketched Krylov residual minimization under embedding-quality assumptions. Timsit, Grigori, and Balabanov (2023) analyze randomized Krylov projection quality, and Burke, Güttel, and Soodhalter (2023) analyze sketched GMRES with restarting and residual convergence bounds. Their studied embeddings or spaces are substantially more informative than the one-row, freshly resampled, deliberately undersketched setting analyzed here, and the inspected results do not give its exact pathwise exponent jointly with all positive-time moment divergence. General Gaussian regression inverse-moment observations explain an individual sketch's heavy tail, but alone do not determine the resampled iteration's almost-sure rate. The relationship to deterministic Richardson concerns equality of **rates**, not identity of the iterations.

## Limitations
This is a planar exactly computed model. Its zero exponent for indefinite spectra proves neither convergence nor divergence. It supplies no finite-precision recommendation: near-orthogonality of a sketch to the current matrix residual creates arbitrarily large intermediate errors. An equivalent formula might exist in specialized randomly projected iteration or random matrix-product literature not examined here. No independence, peer review, or external validation is claimed.

## References
1. Y. Nakatsukasa and J. A. Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, arXiv:2111.00113 (first public 2021-10-29).
2. E. Timsit, L. Grigori and O. Balabanov, *Randomized Orthogonal Projection Methods for Krylov Subspace Solvers*, arXiv:2302.07466 (first public 2023-02-15).
3. L. Burke, S. Güttel and K. M. Soodhalter, *GMRES with Randomized Sketching and Deflated Restarting*, arXiv:2311.14206 (first public 2023-11-23).
