# A Plancherel–Bessel crossover for the standard mode of quantum random-transposition walks

## Finding

Fix any integer \(n\ge2\) and define \(C_n=\binom n2\). On \(\ell^2(S_n)\), let \(L_\tau|g\rangle=|\tau g\rangle\) for a transposition \(\tau\), and set
\[
H_n=C_n^{-1}\sum_{\tau\text{ transposition}}L_\tau.
\]
Consider the trace-preserving quantum stochastic evolution
\[
\dot\rho=-i\alpha[H_n,\rho]+\frac{\gamma}{C_n}\sum_\tau(L_\tau\rho L_\tau^\dagger-\rho),\qquad
\rho(0)=|e\rangle\langle e|,
\]
where \(\alpha\in\mathbb R\), \(\gamma\ge0\). Put \(p_t(g)=\langle g|\rho(t)|g\rangle\). The *normalized standard Fourier coefficient* is
\[
M_{n,\alpha,\gamma}(t)=\frac1{n-1}\sum_{g\in S_n}(\operatorname{Fix}(g)-1)p_t(g).
\]
Let \(d_\lambda\) be the degree of the irreducible \(S_n\)-representation indexed by \(\lambda\), \(\lambda\searrow\nu\) signify adding one cell to \(\nu\), and \(c(\lambda/\nu)\) be that cell's column minus row. For \(\theta\in\mathbb R\), define
\[
\Phi_{n,\nu}(\theta)=\sum_{\lambda\searrow\nu}\frac{d_\lambda}{n d_\nu}
 e^{i\theta c(\lambda/\nu)/C_n}.
\]
Then, exactly for all finite parameters,
\[
\boxed{M_{n,\alpha,\gamma}(t)=e^{-2\gamma t/(n-1)}\kappa_n(\alpha t)},\qquad
\boxed{\kappa_n(\theta)=\frac n{n-1}\sum_{\nu\vdash n-1}\frac{d_\nu^2}{(n-1)!}|\Phi_{n,\nu}(\theta)|^2-\frac1{n-1}}.
\]
In particular, \(-1/(n-1)\le\kappa_n(\theta)\le1\). At the coherent time scale \(\theta=s n^{3/2}\), every fixed real \(s\) satisfies
\[
\boxed{\lim_{n\to\infty}\kappa_n(s n^{3/2})=\mathfrak B(s)},\qquad
\mathfrak B(s)=\begin{cases}\bigl(J_1(4s)/(2s)\bigr)^2,&s\ne0,\\1,&s=0.\end{cases}
\]
Here \(J_1\) is the Bessel function of the first kind, of order one. Thus, if \(g\ge0\) and \(s\ge0\) are fixed while \(\gamma_n=g/\sqrt n\), \(\alpha=1\), and \(t_n=s n^{3/2}\), the *open-system* standard mode converges to \(e^{-2gs}\mathfrak B(s)\). At each positive zero of \(J_1\), the normalized standard mode tends to zero. No assertion about all Fourier modes or total-variation mixing follows solely from this statement.

## Assumptions and scope

Every permutation basis vector is orthonormal. The generator averages *all transpositions with equal weight*, and its Hamiltonian and jumps use the same normalized central conjugacy class. The initial density matrix is concentrated at the identity; measurement is in the permutation basis. The formula holds for \(n=2\), for negative or zero coherent coupling, for zero or positive dissipative strength, and for all \(t\ge0\). The large-degree limit fixes \(s\) before sending \(n\) to infinity. This is a theorem about a particular irreducible Fourier coefficient, not a claim of uniform mixing or a cutoff.

## Proof

**Central spectrum and character expansion.** Let \(z_\lambda\) denote the sum of the contents of every cell in \(\lambda\). The Jucys–Murphy identities show that the sum of all transpositions acts as scalar \(z_\lambda\) in the irreducible representation \(\lambda\); hence the spectrum of \(H_n\) is \(z_\lambda/C_n\). Starting at the identity, the unitary wavefunction is the central class function
\[
A_\theta(g)=\frac1{n!}\sum_{\lambda\vdash n}d_\lambda e^{-i\theta z_\lambda/C_n}\chi_\lambda(g).
\]
The corresponding quantum measurement distribution is \(q_\theta(g)=|A_\theta(g)|^2\). The standard character is \(\chi_{(n-1,1)}(g)=\operatorname{Fix}(g)-1\). By character orthogonality and the usual triple-character expression for Kronecker multiplicities,
\[
\kappa_n(\theta)=\frac1{n!(n-1)}\sum_{\lambda,\mu\vdash n}
 d_\lambda d_\mu\,g_{\lambda,\mu,(n-1,1)}
 e^{-i\theta(z_\lambda-z_\mu)/C_n}.
\tag{1}
\]
This formula is real because the \(\lambda,\mu\) summands come in conjugate pairs.

**Branching converts the Kronecker sum into positive square moduli.** The natural permutation representation decomposes as \(\mathbf1\oplus V_{(n-1,1)}\), while it is also induced from the trivial representation of \(S_{n-1}\). Tensor induction and Frobenius reciprocity therefore give
\[
 g_{\lambda,\mu,(n-1,1)}
 =\sum_{\nu\vdash n-1}{\bf1}_{\nu\nearrow\lambda}{\bf1}_{\nu\nearrow\mu}
 -{\bf1}_{\lambda=\mu}.
\tag{2}
\]
Here \(\nu\nearrow\lambda\) means a valid single-box extension, and multiplicity-free branching is essential. Substituting (2) in (1) makes the first term a sum over \(\nu\) of squared absolute values. If \(\lambda\searrow\nu\), the central eigenvalue increment is exactly \(z_\lambda-z_\nu=c(\lambda/\nu)\); therefore the common phase \(e^{-i\theta z_\nu/C_n}\) cancels. The branching dimension identity \(\sum_{\lambda\searrow\nu}d_\lambda=n d_\nu\) and Plancherel identity \(\sum_{\nu\vdash n-1}d_\nu^2=(n-1)!\) yield the displayed finite branching formula. Each inner coefficient \(d_\lambda/(n d_\nu)\) is a probability. Consequently \(|\Phi_{n,\nu}|\le1\) and the stated two-sided bound follows. The negative constant in the formula comes from subtracting the trivial summand of the natural permutation representation; it cannot be omitted.

**Exact dissipative factor.** Every \(L_\tau\) commutes with the central Hamiltonian \(H_n\), so the Hamiltonian commutator commutes with the full dissipative generator. Starting with \(|e\rangle\langle e|\), the dissipative evolution is diagonal, and its diagonal follows the continuous-time, uniform random-transposition walk. The unitary and dissipative distributions consequently convolve as central functions on \(S_n\). A normalized Fourier coefficient of their convolution is the product of normalized coefficients. The transposition character ratio in the standard representation is \((n-3)/(n-1)\), so its continuous-time multiplier is \(\exp[-\gamma(1-(n-3)/(n-1))t]=e^{-2\gamma t/(n-1)}\). This proves the exact identity for \(M_{n,\alpha,\gamma}(t)\).

**Plancherel transition measures and the limiting profile.** Choose \(\nu\vdash n-1\) according to the Plancherel probability \(d_\nu^2/(n-1)!\). Its *conditional one-box transition measure* is
\[
\mu_{n,\nu}=\sum_{\lambda\searrow\nu}\frac{d_\lambda}{n d_\nu}\,\delta_{c(\lambda/\nu)/\sqrt n}.
\]
The Vershik–Kerov/Logan–Shepp limit shape, together with Kerov's continuity of the transition-measure map, implies that \(\mu_{n,\nu}\) converges *in probability, weakly* to the semicircle measure
\[
\sigma(dx)=\frac{\sqrt{4-x^2}}{2\pi}{\bf1}_{[-2,2]}(x)\,dx.
\]
The needed conditional convergence, as opposed merely to convergence of the randomly added cell after averaging, follows by applying continuity to the concentrated random Young-diagram profile; see Romik–Śniady, Theorems 3.1–3.2 and their proof. For \(\theta=s n^{3/2}\), the exponent in \(\Phi_{n,\nu}\) equals \(2s[n/(n-1)]c(\lambda/\nu)/\sqrt n\). Thus \(\Phi_{n,\nu}(s n^{3/2})\) converges in probability to the semicircle characteristic function
\[
\int_{-2}^{2}e^{2isx}\,\sigma(dx)=\frac{J_1(4s)}{2s},
\]
with continuous value one at the origin. Since \(|\Phi_{n,\nu}|\le1\), bounded convergence in probability gives convergence of the expected squared moduli. Finally \(n/(n-1)\to1\) and \(1/(n-1)\to0\), proving the limiting Bessel-square law. Inserting \(t_n=s n^{3/2}\) and \(\gamma_n=g/\sqrt n\) into the exact dissipative factor proves the stated joint-scale limit.

## Verification

The reproducible program `verify.py` (Python, NumPy and SciPy) computes the exact branching formula using independent hook-length and addable-box routines. It compares this formula against a direct matrix-exponential quantum walk on the full \(n!\)-dimensional Cayley-graph Hilbert space for \(2\le n\le6\) and six values of coherent time. It checks the quadratic moment coefficient for \(2\le n\le15\), and compares fifteen larger-size evaluations with the predicted semicircle/Bessel profile. Run `python verify.py` after installing the versions specified in `requirements.txt`. These are finite checks, not a substitute for the representation-theoretic identities or the conditional Plancherel transition-measure theorem.

## Relationship to prior work

He, Hutsalyuk, Mussardo and Stampiggi [1] formulate the quantum stochastic walk and establish the exact convolution property, the general Kronecker-character formula for its slow mode, and a second-moment estimate identifying the \(n^{3/2}\) scale. The full chapter-level derivations and appendices appear in Stampiggi's publicly available thesis [2], Chapter 3.6 and Appendix C; compare [2], equations (3.108), (3.124), and (3.129)–(3.133). Those existing formulas and the scale itself are *not claimed as new*. The additional result here is the multiplicity-free branching reorganization giving an exact Plancherel average of squared conditional transition transforms and its explicit limiting Bessel-square profile, including asymptotic zeros. Romik and Śniady [3], following Kerov, establish the semicircle transition-measure limit used as an ingredient, but do not treat this stochastic quantum walk. Gerhardt and Watrous [4] give earlier character methods for coherent symmetric-group walks and transposition-generated graphs, with different observables. An earlier implicit derivation is possible; publication priority is not independently certified.

## Limitations

The result does not determine total-variation distance, its cutoff, or a full spectrum-wide mixing law: a single Fourier mode can vanish while others remain. The exact formula requires the identity initial state and the uniform transposition Hamiltonian and jump family. The asymptotic limit fixes the scaled time \(s\), rather than proving a simultaneous uniform-in-time estimate. The complete arXiv paper [1] was not directly available for full-text examination during this comparison; the chapter-length treatment in the publicly accessible thesis [2] was inspected, and any additional material unique to [1] remains a specific priority risk. The numerical checks are finite and have no independent certification status.

## References

1. F. He, A. Hutsalyuk, G. Mussardo, A. Stampiggi, *Quantum Stochastic Walks on the Permutation Group*, first arXiv version dated 2026-09-11, arXiv:2609.13387. https://arxiv.org/abs/2609.13387
2. A. Stampiggi, *Statistical Spectroscopy of Quantum Many-Body Systems*, SISSA thesis (2026), Chapter 3.6, especially equations (3.108), (3.124), (3.129)–(3.133), Appendix C. https://iris.sissa.it/retrieve/a757920f-ee74-4fa1-8338-98fce66b67ed/phd_thesis_v3.pdf
3. D. Romik and P. Śniady, *Jeu de taquin dynamics on infinite Young tableaux and second class particles*, Annals of Probability 43 (2015), Theorems 3.1 and 3.2. https://www.math.ucdavis.edu/~romik/data/uploads/papers/plancherel-aop873.pdf
4. H. Gerhardt and J. Watrous, *Continuous-time quantum walks on the symmetric group* (2003), arXiv:quant-ph/0305182. https://arxiv.org/pdf/quant-ph/0305182
