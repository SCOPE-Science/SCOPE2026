# Weak-flux detection law and a resonant-rate jump on a monitored quantum triangle

## Finding

Consider the three-site magnetic tight-binding ring, with one-site projective detection after each fixed unitary step, initially prepared in the antisymmetric state of the two undetected sites. At zero magnetic phase this state is perfectly dark. At fixed positive dimensionless observation interval \(t\), a small nonzero magnetic phase \(\alpha\) makes its first-detection attempt count \(N_\alpha\) finite almost surely. Its full weak-phase limit is

\[
\alpha^2 N_\alpha\ \xrightarrow[\alpha\to0,\ \alpha\ne0]{\mathrm{law}}\ \operatorname{Exp}(\Lambda(t)),\qquad
\Lambda(t)=\begin{cases}
\frac92t^2,&3t\notin2\pi\mathbb Z,\\
t^2,&3t\in2\pi\mathbb Z.
\end{cases}
\]

Here \(\operatorname{Exp}(\Lambda)\) has survival function \(e^{-\Lambda x}\). At each fixed \(t>0\) and each integer \(m\ge1\), the corresponding moments converge:

\[
\lim_{\alpha\to0,\ \alpha\ne0}\alpha^{2m}\mathbb E[N_\alpha^m]=\frac{m!}{\Lambda(t)^m}.
\]

Consequently \(\alpha^2\mathbb E[N_\alpha]\to2/(9t^2)\) off the sampling revivals, but \(\alpha^2\mathbb E[N_\alpha]\to1/t^2\) exactly at each positive revival \(t=2\pi k/3\). The weak-phase escape rate therefore changes by a factor \(9/2\) at any fixed positive revival. The theorem concerns an initial state that is dark at zero phase, not the return-to-detector protocol.

## Assumptions and scope

Let \(\{|0\rangle,|1\rangle,|2\rangle\}\) be an orthonormal basis. The Hamiltonian and observation unitary are

\[
H=-\gamma\left(e^{i\alpha}\left(|0\rangle\langle1|+|1\rangle\langle2|+|2\rangle\langle0|\right)+\mathrm{h.c.}\right),\quad
U_\alpha=e^{-iH\tau},\quad t=\gamma\tau>0.
\]

Here \(\gamma,\tau>0\) are fixed, and \(\alpha\in\mathbb R\) tends to zero through nonzero values. Initially \(|d\rangle=(|1\rangle-|2\rangle)/\sqrt2\). After each period \(\tau\), perform the ideal projective test \(\{|0\rangle\langle0|,I-|0\rangle\langle0|\}\), and halt at the first outcome \(|0\rangle\). Denote the positive-integer attempt number by \(N_\alpha\). All asymptotic statements fix \(t\); none claims uniformity when \(t\) approaches a revival concurrently with \(\alpha\).

Put \(|s\rangle=(|1\rangle+|2\rangle)/\sqrt2\), and \(P=I-|0\rangle\langle0|\). The non-detection step \(K_\alpha=PU_\alpha P\) is restricted to \(\mathrm{span}\{|s\rangle,|d\rangle\}\). The exact survival identity is

\[
\mathbb P(N_\alpha>n)=\|K_\alpha^n|d\rangle\|^2\quad(n=0,1,2,\ldots).
\]

## Proof

**1. Exact two-dimensional survival matrix.** Diagonalizing the cyclic three-site Hamiltonian (or summing its three Fourier modes) yields the following exact matrix in the ordered basis \((|s\rangle,|d\rangle)\):

\[
K_\alpha=\begin{pmatrix}
(2u+w\cos\beta)/3 &w\sin\beta/\sqrt3\\
-w\sin\beta/\sqrt3&w\cos\beta
\end{pmatrix},\qquad
u=e^{2it\cos\alpha},\quad w=e^{-it\cos\alpha},\quad
\beta=\sqrt3\,t\sin\alpha.
\]

This identity follows by splitting the three Fourier energies into the symmetric mode \(-2\gamma\cos\alpha\) and the pair \(\gamma\cos\alpha\mp\sqrt3\gamma\sin\alpha\), then taking the \(2\times2\) compression. The matrix is a contraction because it is a compression of a unitary. At \(\alpha=0\) the dark vector is an eigenvector with eigenvalue \(e^{-it}\) of modulus one.

**2. Non-revival sampling.** Assume \(3t\notin2\pi\mathbb Z\), and write \(w_0=e^{-it}\), \(u_0=e^{2it}\). The eigenvalues of \(K_0\) are \(w_0\) and \((2u_0+w_0)/3\); the second has squared modulus \((5+4\cos3t)/9<1\). They are distinct. Standard analytic perturbation of the explicit matrix gives the eigenvalue continuing \(w_0\):

\[
\lambda_d(\alpha)=w_0\left[1+\left(\frac{it}{2}-\frac{3t^2}{2}
+\frac{3t^2}{2(e^{3it}-1)}\right)\alpha^2+O_t(\alpha^4)\right].
\]

Indeed, \(K_{dd}=w_0[1+(it/2-3t^2/2)\alpha^2+O_t(\alpha^4)]\), the two off-diagonal entries are \(\pm w_0t\alpha+O_t(\alpha^3)\) with opposite signs, and the second-order correction to the dark eigenvalue is their product divided by \(w_0-(2u_0+w_0)/3\). Since \(\operatorname{Re}(1/(e^{i\theta}-1))=-1/2\) whenever \(\theta\notin2\pi\mathbb Z\),

\[
|\lambda_d(\alpha)|^2=1-\frac92t^2\alpha^2+O_t(\alpha^4).
\]

The other eigenvalue remains uniformly inside the unit disk, and the dark spectral projector converges to \(|d\rangle\langle d|\). Thus for fixed \(x\ge0\), setting \(n=\lfloor x/\alpha^2\rfloor\) in the exact survival identity gives \(\|K_\alpha^n d\|^2\to e^{-9t^2x/2}\).

**3. Exact-revival sampling.** Suppose \(t=2\pi k/3\), with integer \(k\ge1\), so \(e^{2it}=e^{-it}\). Expansion of the exact matrix gives

\[
e^{it}K_\alpha=I+\alpha t\begin{pmatrix}0&1\\-1&0\end{pmatrix}
+\alpha^2\begin{pmatrix}-t^2/2-it/2&0\\0&-3t^2/2+it/2\end{pmatrix}
+O_t(\alpha^3).
\]

The first-order matrix has simple eigenvalues \(\pm it\) and mutually orthogonal normalized eigenvectors \((1,\pm i)/\sqrt2\). In each of those eigenvectors the second-order diagonal matrix has expectation \(-t^2\). Hence the two eigenvalues of \(K_\alpha\) are

\[
\lambda_\pm(\alpha)=e^{-it}\left(1\pm it\alpha-t^2\alpha^2+O_t(\alpha^3)\right),\quad
|\lambda_\pm(\alpha)|^2=1-t^2\alpha^2+O_t(|\alpha|^3).
\]

Their spectral projections converge to the orthogonal projections onto the two circular eigenvectors. For \(n=\lfloor x/\alpha^2\rfloor\), each diagonal survival contribution tends to its initial squared projection weight times \(e^{-t^2x}\). The cross term tends to zero because the two spectral subspaces become orthogonal, even though their relative phase may rotate rapidly. Their weights sum to one. Consequently \(\|K_\alpha^n d\|^2\to e^{-t^2x}\). This proves the second case, including the changed coefficient.

**4. Eventual detection and all moments.** For each fixed \(t>0\), the preceding expansions show that every eigenvalue of \(K_\alpha\) has modulus strictly below one for all sufficiently small nonzero \(\alpha\). Both the non-revival eigenprojectors and the two revival eigenprojectors remain uniformly bounded as \(\alpha\to0\) along nonzero values. Therefore there exist \(C,c,\varepsilon>0\), depending on fixed \(t\), such that

\[
\mathbb P(N_\alpha>n)\le C e^{-c\alpha^2n}
\quad(0<|\alpha|<\varepsilon,\ n\ge0).
\]

This proves almost-sure detection and uniform exponential integrability of the scaled attempt count for sufficiently small exponential parameters. Together with the pointwise survival limits, it implies distributional convergence and convergence of every positive integer moment, completing the proof.

## Verification

A self-contained checker \(\texttt{verify.py}\) constructs the exact compressed matrix and independently constructs the full three-site Hamiltonian and exponential. It compares the matrices at 25 parameter choices, computes first-detection means via a discrete Lyapunov identity, compares weak-phase survival curves, and checks spectral losses in both sampling regimes. Running \(\texttt{python verify.py}\) with NumPy and SciPy passed 49 checks. In particular, the predicted scaled mean at \(t=1\) is \(2/9=0.222222\ldots\), and at \(t=2\pi/3\) it is \(9/(4\pi^2)=0.227972\ldots\); the respective values at \(\alpha=0.005\) were \(0.222240057148\) and \(0.227987937706\). Numeric checks are corroboration of, and not replacements for, the analytic proof above.

## Relationship to prior work

Wang et al. (arXiv:2402.15843, Secs. II, V, VI, and Appendix B) introduce and analyze precisely this three-site magnetic Hamiltonian and the on-site monitoring protocol. They identify the antisymmetric dark state at zero flux, analyze phase-factor coincidences and finite-resolution broadening, and discuss slow null-detection decay. The present statement concerns a distinct *singular weak-magnetic-phase first-hitting-time limit* of that initially dark state. It supplies the full limiting distribution, the exact escape coefficient, its discontinuous dependence on a fixed revival sampling interval, and all moment limits; these statements are not given by the cited phase-matching or return-time results. The general quantum-renewal framework of Friedman, Kessler and Barkai, and the dark/bright state classification of Thiel et al., provide relevant background but neither an equivalent numerical rate for this setup nor the comparison of two fixed sampling regimes.

## Limitations

The asymptotics fix \(t=\gamma\tau>0\) before taking \(\alpha\to0\). No two-parameter crossover is claimed as \(t\) approaches \(2\pi k/3\) on the scale of \(\alpha\); the jump in the coefficient is a nonuniform-limits phenomenon. This is a three-site, one-site, ideal-projective, noiseless monitoring result for one specified coherent initial state. The limiting exponential law does not assert that the finite-phase detection distribution is exactly geometric. No independent scientific audit or publication-priority certification is asserted.

## References

1. Q. Wang, S. Ren, R. Yin, K. Ziegler, E. Barkai, and S. Tornow, *First Hitting Times on a Quantum Computer: Tracking vs. Local Monitoring, Topological Effects, and Dark States*, arXiv:2402.15843 (first posted 2024-02-24); https://arxiv.org/html/2402.15843v2 .
2. H. Friedman, D. A. Kessler, and E. Barkai, *Quantum walks: the first detected passage time problem*, arXiv:1611.05676 (2016); https://arxiv.org/abs/1611.05676 .
3. F. Thiel, I. Mualem, D. Meidan, E. Barkai, and D. A. Kessler, *Dark states of quantum search cause imperfect detection*, Physical Review Research 2, 043107 (2020); https://doi.org/10.1103/PhysRevResearch.2.043107 .
4. R. Yin et al., *Restart uncertainty relation for monitored quantum dynamics*, arXiv:2401.01307 (2024); https://arxiv.org/abs/2401.01307 .
