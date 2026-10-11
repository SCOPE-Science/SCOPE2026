# Exact covariance and typical-rate gap for random planar Minkowski symmetrization

## Finding

Let \(K\subset\mathbb R^2\) be an arbitrary compact convex body with nonempty interior. Starting from \(K_0=K\), construct \(K_t=\frac12(K_{t-1}+\mathcal R_{\Theta_t}K_{t-1})\) for integers \(t\ge1\), where \(\mathcal R_{\Theta}\) is reflection in the line through the origin at angle \(\Theta\), and the \(\Theta_t\) are independent uniform angles in \([0,\pi)\). All random statements refer to this law of reflection axes.

Let \(P=P(K)\), \(r=P/(2\pi)\), and \(D_t=\pi r^2-\operatorname{Area}(K_t)\). Write the support function of \(K\) as
\[
h(\phi)=r+\sum_{m\ge1}\bigl(a_m\cos(m\phi)+b_m\sin(m\phi)\bigr),
\qquad
w_m=\frac\pi2(m^2-1)(a_m^2+b_m^2)\quad(m\ge2).
\]
The nonnegative weights have \(\sum_{m\ge2}w_m=D_0<\infty\). Put \(Q=\sum_{m\ge2}w_m^2\). For all integers \(0\le s\le t\),
\[
\boxed{\mathbb E D_t=2^{-t}D_0},\qquad
\boxed{\operatorname{Cov}(D_s,D_t)=2^{-(t-s)}\bigl[(3/8)^s-4^{-s}\bigr]Q}.
\]
In particular, for every \(t\ge1\),
\[
\boxed{\operatorname{Var}(D_t)=\bigl[(3/8)^t-4^{-t}\bigr]Q
\ \le\ \bigl[(3/8)^t-4^{-t}\bigr]D_0^2.}
\]
For \(D_0>0\), equality in the upper bound holds if and only if the support function, modulo its constant and translational first harmonic, has precisely one nonzero Fourier frequency of order at least \(2\). Noncircular equality cases exist for every frequency; they include the convex bodies with \(h(\phi)=r+\epsilon\cos(m\phi)\) when \(r>0\) and \(0<|\epsilon|\le r/(m^2-1)\). The translated disks, for which \(D_0=0\), give zero on both sides.
For every noncircular single-frequency equality case, the entire finite-time law is \(D_t/D_0\overset d=\prod_{j=1}^tB_j\), where the \(B_j\) are independent arcsine variables with distribution \(\operatorname{Beta}(1/2,1/2)\).

For every noncircular \(K\), the squared coefficient of variation obeys the exact identity
\[
\frac{\operatorname{Var}(D_t)}{(\mathbb E D_t)^2}
=\left[(3/2)^t-1\right]\frac{Q}{D_0^2},
\qquad t\ge1.
\]
Nevertheless the mean-normalized deficit vanishes almost surely:
\[
\boxed{2^tD_t\longrightarrow0\quad\text{almost surely as }t\to\infty.}
\]
Thus the positive mean \(\mathbb E(2^tD_t)=D_0\) is not representative of typical realizations, and the nonnegative martingale \((2^tD_t)\) is not uniformly integrable when \(D_0>0\).

## Assumptions and scope

The body need not be smooth, strictly convex, origin-symmetric, or finitely Fourier-supported. Perimeter means Euclidean boundary length, area means two-dimensional Lebesgue measure, and support functions are evaluated at outer unit normals \((\cos\phi,\sin\phi)\). Every \(K_t\) has perimeter \(P\) because reflection preserves the mean support value and Minkowski addition adds support functions. Translation affects only the first Fourier frequency and leaves the deficit and all claims invariant. The area and Fourier formulas are valid for nonsmooth bodies by standard support-function approximation in \(W^{1,2}\), or equivalently by the planar convex-body area identity in its weak form. There is no assertion about Steiner rather than Minkowski symmetrization, nonuniform reflection laws, or dimensions greater than two.

## Proof

**Step 1: the geometric area identity.** A planar support function is Lipschitz on the circle. Its weak derivative is square-integrable, and the planar support-function area identity gives
\[
\operatorname{Area}(K)=\frac12\int_0^{2\pi}\bigl(h(\phi)^2-h'(\phi)^2\bigr)\,d\phi.
\]
For smooth strictly convex support functions this follows from \(x(\phi)=h(\phi)n(\phi)+h'(\phi)\tau(\phi)\) and the signed-area integral. For general convex bodies one can mollify the support function by averaging rotations, adding a small disk if needed, and pass to the limit using convergence of support functions and their weak derivatives in \(W^{1,2}\); alternatively the identity is obtained by integration by parts against the curvature measure \(h+h''\). Fourier Parseval yields
\[
\pi r^2-\operatorname{Area}(K)=\frac\pi2\sum_{m\ge2}(m^2-1)(a_m^2+b_m^2)=\sum_{m\ge2}w_m.
\]
The first Fourier frequency cancels exactly. Every term is nonnegative, and the series is finite. The identity holds independently for every \(K_t\).

**Step 2: mode-by-mode reflected projection.** For a fixed \(m\ge2\), write the real harmonic as \(c_m\cos(m\phi-\alpha_m)\). Reflection in the axis \(\Theta\) sends the support function to \(h(2\Theta-\phi)\); taking the arithmetic mean projects this harmonic onto the one-dimensional reflection-invariant subspace at angle \(\Theta\). Its squared amplitude becomes \(c_m^2\cos^2(m\Theta-\alpha_m)\). Once projected at \(\Theta_{j-1}\), the next projection multiplies its squared amplitude by \(\cos^2(m(\Theta_j-\Theta_{j-1}))\). Thus, for each \(m\ge2\), the contribution at time \(t\ge1\) equals
\[
W_{m,t}=w_m\cos^2(m\Theta_1-\alpha_m)
\prod_{j=2}^t\cos^2(m(\Theta_j-\Theta_{j-1})),
\qquad D_t=\sum_{m\ge2}W_{m,t}.
\]
This representation is valid even for infinitely many nonzero modes because all contributions are nonnegative and sum to the finite geometric deficit.

**Step 3: exact second moments.** The transformation from the independent axis angles to their successive differences modulo \(\pi\) is a Haar-measure-preserving bijection on the angle torus. Consequently the difference variables, including the first angle, are independent and each uniform modulo \(\pi\). For every integer \(m\ge1\) and real \(\alpha\), uniform angular integration gives
\[
\mathbb E\cos^2(mU-\alpha)=\tfrac12,
\qquad \mathbb E\cos^4(mU-\alpha)=\tfrac38.
\]
If \(m\ne\ell\), orthogonality of distinct integer trigonometric frequencies gives
\[
\mathbb E\bigl[\cos^2(mU-\alpha)\cos^2(\ell U-\beta)\bigr]=\tfrac14.
\]
Multiplying independent factors therefore yields
\[
\mathbb E W_{m,t}=2^{-t}w_m,
\quad
\mathbb E W_{m,t}^2=(3/8)^t w_m^2,
\quad
\mathbb E[W_{m,t}W_{\ell,t}]=4^{-t}w_mw_\ell\ (m\ne\ell).
\]
Summation and Tonelli's theorem give the mean and variance formulas without requiring finite Fourier support. Indeed, \(\sum_m w_m<\infty\) guarantees absolute control of every first and second moment.

**Step 4: temporal covariance and rigidity.** Conditioned on all axes through time \(s\), the next uniform axis multiplies the conditional expectation of every existing squared Fourier amplitude by \(1/2\). Hence \(\mathbb E[D_t\mid\mathcal F_s]=2^{-(t-s)}D_s\). Applying the defining covariance identity proves the two-time formula. For \(D_0>0\), \(Q\le D_0^2\) is precisely \(\sum_mw_m^2\le(\sum_mw_m)^2\), and equality requires \(w_mw_\ell=0\) whenever \(m\ne\ell\). A constant plus a first harmonic and one higher harmonic describes exactly these supports, subject to the necessary curvature nonnegativity for convexity; the displayed single-harmonic family realizes every order \(m\ge2\).

**Step 5: the almost-sure gap.** The nonnegative process \(M_t=2^tD_t\) is a martingale of constant expectation \(D_0\), so it converges almost surely to a finite \(M_\infty\). For any fixed Fourier order \(m\), the factors \(2\cos^2(mU)\) in \(2^tW_{m,t}\) are independent and identically distributed, with integrable logarithm and
\[
\mathbb E\log(2\cos^2(mU))=-\log2<0.
\]
The logarithmic expectation follows from \(\pi^{-1}\int_0^\pi\log|\cos u|\,du=-\log2\); the finite exceptional zero set has probability zero. The strong law gives \(2^tW_{m,t}\to0\) almost surely for each fixed \(m\). For a cutoff \(N\), the remaining nonnegative sum \(T_{N,t}=\sum_{m>N}2^tW_{m,t}\) is a martingale with constant mean \(\sum_{m>N}w_m\), and converges almost surely. Since the finitely many retained terms vanish, \(\lim_tT_{N,t}=M_\infty\) almost surely. Fatou's lemma gives \(\mathbb E M_\infty\le\sum_{m>N}w_m\), and letting \(N\to\infty\) forces \(M_\infty=0\) almost surely. The coefficient-of-variation formula follows by dividing the exact variance by the squared mean. Its divergence and the almost-sure limit together prove nonuniform integrability for a noncircular body.

## Verification

Run `python verify.py` with Python 3 and NumPy in a directory containing this document and the included script. It returns `VERIFY_OK` after independently applying reflections to complex Fourier support coefficients, using deterministic two-dimensional angle quadrature to compare one- and two-step expectations, variances, and covariance with the analytic formulas, comparing a direct support integral for area, checking the convexity condition, and testing the one-frequency equality case. A \(128\times128\) angular tensor grid resolves the finite trigonometric polynomials in that test; this does not by itself prove the all-body statement. The infinite Fourier case, equality classification, and almost-sure assertion are proved analytically above, not inferred from computation.

## Relationship to prior work

Coupier and Davydov, *Random symmetrizations of convex bodies* (arXiv:1211.1785, Section 4.2, Proposition 5), establish the factor-\(1/2\) decay of the expected squared \(L^2\) norm of the centered support function in dimension two, together with almost-sure convergence bounds. That known first-order contraction is credited; it is neither the isoperimetric-area variance nor a two-time covariance identity. The present proof needs the fourth angular moments and the cross-frequency orthogonality, which the cited expected-\(L^2\) formula alone cannot supply.

Bianchi, Gardner, and Gronchi, *Symmetrization in Geometry* (arXiv:1603.00643, primary MSC 52A20), develop deterministic properties and characterizations of Minkowski symmetrization, including mean-width preservation. Their framework identifies the geometric operation but does not provide the random area-deficit covariance or the sharp Fourier concentration equality classification. Earlier work on random Minkowski symmetrization by Bourgain, Lindenstrauss, and Milman considers high-dimensional ball approximation, not these planar intrinsic-area moments. Kwong and Lee (arXiv:2008.07242) treat deterministic Fourier inequalities for isoperimetric deficits rather than random symmetrization. These comparisons do not establish exhaustive historical novelty.

## Limitations

The formulas require independent Haar-uniform reflection axes and the planar quadratic support-function area identity; they need not extend to biased angles, Steiner symmetrization, or higher dimension. Pairwise uncorrelated squared Fourier modes are not asserted to be jointly independent. The deterministic verifier uses a smooth finite-mode example and cannot certify arbitrary convex bodies or almost-sure convergence. There is residual historical risk of a previously unindexed equivalent stochastic-geometric fourth-moment calculation. Independent external validation has not been performed.

## References

1. D. Coupier and Yu. Davydov, *Random symmetrizations of convex bodies*, arXiv:1211.1785v1 (first public version 2012-11-08), especially Proposition 5 and Section 4.2. https://arxiv.org/abs/1211.1785
2. G. Bianchi, R. J. Gardner, and P. Gronchi, *Symmetrization in Geometry*, arXiv:1603.00643v1 (first public version 2016-03-02), primary MSC 52A20, 52A39, Sections 2–3, 7–9. https://arxiv.org/abs/1603.00643
3. J. Bourgain, J. Lindenstrauss, and V. Milman, *Minkowski sums and symmetrizations*, Institut des Hautes Études Scientifiques preprint archive, especially Section 2, pp. 13–20. https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/BOURGAIN/1984-1989/M_88_14/M_88_14_web.pdf
4. K.-K. Kwong and H. Lee, *Higher order Wirtinger-type inequalities and sharp bounds for the isoperimetric deficit*, arXiv:2008.07242 (2020), Introduction and deterministic inequality results. https://arxiv.org/abs/2008.07242
