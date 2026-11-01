# Hankel-signature transitions and exact nonnormality energy for fractional Cesàro–Hardy operators

## Finding

Let \(\alpha>0\) be real. On the complex Hilbert space \(L^2(0,1)\), define the generalized continuous Cesàro–Hardy operator
\[
(C_\alpha f)(x)=\frac{\alpha}{x^\alpha}\int_0^x(x-y)^{\alpha-1}f(y)\,dy
\qquad(0<x<1),
\]
and the self-adjoint integral operator
\[
(J_\alpha f)(x)=\alpha\int_0^1(1-xy)^{\alpha-1}f(y)\,dy.
\]
Both are bounded; \(J_\alpha\) is trace class, and the exact self-commutator factorization is
\[
\boxed{C_\alpha^*C_\alpha-C_\alpha C_\alpha^*=-J_\alpha^2.}
\]
Consequently every \(C_\alpha\) is cohyponormal and its self-commutator is negative trace class. With \(\psi\) the digamma function and \(\gamma\) Euler's constant, the **exact trace norm of this defect** is
\[
\boxed{\|C_\alpha^*C_\alpha-C_\alpha C_\alpha^*\|_1
=\operatorname{Tr}(J_\alpha^2)
=\alpha^2\frac{\psi(2\alpha)+\gamma}{2\alpha-1},\quad\alpha\ne\tfrac12,}
\]
with the continuous value \(\pi^2/24\) at \(\alpha=1/2\). In addition,
\[
\boxed{\operatorname{Tr}(J_\alpha)=
\frac{\alpha\sqrt\pi\,\Gamma(\alpha)}{2\Gamma(\alpha+1/2)}.}
\]

Write \(n_+(J_\alpha)\) and \(n_-(J_\alpha)\) for the numbers of strictly positive and strictly negative eigenvalues, counted with multiplicity, allowing infinity. The **complete inertia classification** is:

* If \(\alpha=m\) is a positive integer, then \(J_m\) has rank exactly \(m\),
\[
\boxed{(n_+(J_m),n_-(J_m))=
(\lceil m/2\rceil,\lfloor m/2\rfloor),}
\]
and its kernel is infinite-dimensional.
* If \(2k<\alpha<2k+1\) with integer \(k\ge0\), then
\[
\boxed{(n_+(J_\alpha),n_-(J_\alpha))=(\infty,k).}
\]
* If \(2k+1<\alpha<2k+2\) with integer \(k\ge0\), then
\[
\boxed{(n_+(J_\alpha),n_-(J_\alpha))=(k+1,\infty).}
\]
For every noninteger \(\alpha>0\), \(J_\alpha\) is injective with dense range. Hence the self-commutator has infinite rank and a strictly negative quadratic form on every nonzero vector. At each integer order its rank collapses to that integer.

## Assumptions and scope

The parameter \(\alpha\) ranges over all positive **real** numbers; no complex-order assertion is made. Operators act on complex \(L^2(0,1)\) with Lebesgue measure. The integrals define bounded operators by the convolution argument below, including when the kernel is unbounded at the corner for \(0<\alpha<1\). The symbol \(\|\cdot\|_1\) denotes the trace-class norm. For a compact self-adjoint operator the inertia counts spectral eigenvalues with multiplicities; a zero eigenvalue is excluded from both counts.

This is a statement about the **continuous** generalized Cesàro–Hardy family. No identification with a discrete Cesàro matrix or a fractional operator power is assumed.

## Proof

**1. Exact Hankel-square factorization.** Define the unitary logarithmic-coordinate map \(U:L^2(0,1)\to L^2(0,\infty)\) by
\[
(Uf)(s)=e^{-s/2}f(e^{-s}).
\]
Changing variables \(y=xe^{-t}\) gives \(UC_\alpha U^{-1}=W_\alpha\), where
\[
(W_\alpha g)(s)=\int_0^\infty k_\alpha(t)g(s+t)\,dt,\qquad
k_\alpha(t)=\alpha e^{-t/2}(1-e^{-t})^{\alpha-1}.
\]
The kernel is in \(L^1(0,\infty)\), so \(W_\alpha\) is bounded. Set
\[
(H_\alpha g)(s)=\int_0^\infty k_\alpha(s+t)g(t)\,dt.
\]
Here \(H_\alpha=H_\alpha^*\), and it is Hilbert–Schmidt because
\[
\|H_\alpha\|_2^2=\int_0^\infty t|k_\alpha(t)|^2\,dt<\infty:
\]
the integrand is \(O(t^{2\alpha-1})\) at zero and exponentially small at infinity. For a bounded, compactly supported approximation to \(k_\alpha\), direct multiplication of the integral kernels of \(W_\alpha\) and \(W_\alpha^*\) gives
\[
(W_\alpha W_\alpha^*-W_\alpha^*W_\alpha)(s,t)
=\int_0^\infty k_\alpha(s+u)k_\alpha(t+u)\,du
=(H_\alpha^2)(s,t).
\]
Approximation in \(L^1\) for \(W_\alpha\) and in weighted \(L^2(t\,dt)\) for \(H_\alpha\) passes this identity to every real \(\alpha>0\). Finally, the inverse logarithmic unitary sends \(H_\alpha\) exactly to \(J_\alpha\): setting \(x=e^{-s}\), \(y=e^{-t}\) in the Hankel kernel yields \(\alpha(1-xy)^{\alpha-1}\). Thus \(C_\alpha^*C_\alpha-C_\alpha C_\alpha^*=-J_\alpha^2\).

**2. Nuclear expansion and both traces.** The binomial series yields, with \(v_j(x)=x^j\),
\[
J_\alpha=\sum_{j=0}^\infty a_j\,v_j\otimes v_j,
\qquad a_j=\alpha(-1)^j\binom{\alpha-1}{j}
=\frac{\alpha(1-\alpha)_j}{j!}.
\]
For noninteger \(\alpha>0\), the Gamma-function ratio gives \(|a_j|=O(j^{-\alpha})\). Because \(\|v_j\|_2^2=(2j+1)^{-1}\),
\[
\sum_{j\ge0}|a_j|\|v_j\|_2^2<\infty.
\]
The series therefore converges in trace norm, justifying its quadratic-form expansion and diagonal integration. For integer orders it terminates. Consequently,
\[
\operatorname{Tr}J_\alpha=
\alpha\int_0^1(1-x^2)^{\alpha-1}\,dx
=\frac{\alpha}{2}B(\tfrac12,\alpha).
\]
Since \(J_\alpha\) is self-adjoint Hilbert–Schmidt,
\[
\operatorname{Tr}(J_\alpha^2)=\alpha^2\int_0^1\!\int_0^1(1-xy)^{2\alpha-2}\,dx\,dy
=\alpha^2\int_0^1(-\log u)(1-u)^{2\alpha-2}\,du.
\]
For \(2\alpha>1\) differentiate the beta integral at its first argument \(1\). The resulting identity continues analytically to all \(2\alpha>0\): the integrand is integrable at the problematic endpoint because the logarithm supplies one additional factor. This gives the stated digamma quotient. At \(2\alpha=1\), its removable limit is \(\psi'(1)=\pi^2/6\), multiplied by \(\alpha^2=1/4\). Since the self-commutator is negative, its trace-class norm is exactly \(\operatorname{Tr}J_\alpha^2\).

**3. Integer orders.** If \(\alpha=m\in\mathbb N\), the only nonzero coefficients are
\[
a_j=m(-1)^j\binom{m-1}{j},\qquad 0\le j<m.
\]
The vectors \(1,x,\ldots,x^{m-1}\) are linearly independent. The finite-rank operator is a Gram congruence of the diagonal matrix \(\operatorname{diag}(a_0,\ldots,a_{m-1})\); hence Sylvester inertia gives exactly \(\lceil m/2\rceil\) positive and \(\lfloor m/2\rfloor\) negative eigenvalues and rank \(m\).

**4. Noninteger inertia.** Fix \(m\ge0\) and \(m<\alpha<m+1\). The coefficients \(a_j\) are nonzero; those with \(j<m\) have signs \((-1)^j\), while **every** \(j\ge m\) has the common sign \((-1)^m\). Thus the quadratic form is a finite signed sum of the first \(m\) moments plus a definite infinite tail:
\[
\langle J_\alpha f,f\rangle=
\sum_{j=0}^\infty a_j\left|\int_0^1x^j f(x)\,dx\right|^2.
\]
The number of coefficients among \(j<m\) opposite to the tail sign is \(\lceil m/2\rceil\), giving an immediate upper bound on the opposing inertia index. On the closed infinite-dimensional subspace of functions whose first \(m\) moments vanish, the tail form is strictly of sign \((-1)^m\): its zero set there is trivial because the monomials \(x^m,x^{m+1},\ldots\) span a dense subspace of \(L^2(0,1)\). This proves the infinite index of the tail sign.

For sharpness of the opposing finite index, invert the \(m\times m\) Hilbert moment matrix to obtain polynomials \(g_r\) satisfying
\[
\int_0^1x^j g_r(x)\,dx=\delta_{jr},\qquad 0\le j<m.
\]
For \(0<\varepsilon<1\), define \(f_{r,\varepsilon}(x)=\varepsilon^{-r-1}g_r(x/\varepsilon)\mathbf1_{(0,\varepsilon)}(x)\). Their moments below \(m\) are exactly \(\delta_{jr}\), while their moments of order \(j\ge m\) are bounded in modulus by \(\|g_r\|_1\varepsilon^{j-r}\). As \(\varepsilon\to0\), the quadratic-form Gram matrix of the vectors with indices opposite to the tail sign therefore tends to \(\operatorname{diag}(a_r)\) on that set. It has the required definite sign for small \(\varepsilon\), establishing the matching lower bound. Rewriting by the parity of \(m\) yields the two stated noninteger cases.

Finally, if \(J_\alpha f=0\), then for \(|x|<1\) its analytic integral expression has Taylor coefficients \(a_j\int_0^1y^j f(y)\,dy\). All coefficients vanish; every \(a_j\ne0\), so every polynomial moment of \(f\) vanishes, forcing \(f=0\). Thus \(J_\alpha\) is injective with dense range and infinite rank. As \(\ker J_\alpha^2=\ker J_\alpha\), the corresponding defect statements follow.

## Verification

The standalone script `check_signature.py` uses only Python's standard library. Running `python3 check_signature.py` checks exact rational identities for the binomial coefficients, the two integer-order trace formulas, the invertible moment Gram matrices, and the integer and noninteger coefficient-sign patterns. It reports 1102 passing assertions for integer orders \(1\) through \(10\) and half-integer orders \(1/2\) through \(17/2\). These are consistency checks, **not** exhaustive verifications of the continuum of parameters or substitutes for the analytic proof.

As a transparent special case, \(J_2\) has kernel \(2(1-xy)\), has two nonzero eigenvalues \((2\pm\sqrt7)/3\), and satisfies \(\operatorname{Tr}J_2^2=22/9\). For \(\alpha=1\), \(J_1\) is the orthogonal projection onto constant functions and the defect is exactly its negative.

## Relationship to prior work

Abadías, Mahillo, and Miana study the generalized continuous Cesàro–Hardy family via weighted Koopman semigroups and establish its fine spectra and intertwining properties. The present question is different: exact Hilbert-space self-commutators, trace-class nonnormality energy, and the inertia of the associated signed Hankel factor. Mirotin describes holomorphic functions and fractional powers of the classical continuous Cesàro operator; those operator powers are not identified here with the order parameter \(\alpha\), and the inspected material does not state this inertia classification. Brown–Halmos–Shields already treat the classical order-one operator; the \(\alpha=1\) case is a benchmark, not a new assertion by itself.

General Wiener–Hopf/Toeplitz Hankel-compression identities explain why a Hankel-square factorization is plausible, but do not by themselves provide the precise order-dependent finite-versus-infinite inertia, injectivity, or the explicit digamma trace. The novelty claim is limited to this **combined complete quantitative and signature classification**, and publication priority remains subject to broader literature verification.

## Limitations

The signs of eigenvalues of \(J_\alpha\) are classified, but their individual magnitudes and multiplicities are not evaluated for noninteger \(\alpha\). The theorem gives no sharp decay law for those eigenvalues, no uniform behavior in complex \(\alpha\), and no classification for discrete Cesàro matrices. The exact defect factorization does not constitute independent external validation. General results on indefinite kernels or classical Hankel operators may imply special parts of the classification under another vocabulary; the available comparisons do not eliminate that residual publication-priority risk.

## References

1. L. Abadías, A. Mahillo, and P. J. Miana, *Cesàro-Hardy operators on \(L^p[0,1]\): fine spectrum, weighted Koopman semigroups and invariant subspaces*, arXiv:2604.20408v1, first submitted 22 April 2026. https://arxiv.org/abs/2604.20408
2. A. R. Mirotin, *Functions of continuous Cesáro operators*, arXiv:2411.15578v1 (23 November 2024); accepted manuscript, *Canadian Mathematical Bulletin*, DOI:10.4153/S000843952610232X. https://doi.org/10.4153/S000843952610232X
3. A. Brown, P. R. Halmos, and A. L. Shields, *Cesàro operators*, *Acta Scientiarum Mathematicarum (Szeged)* 26 (1965), 125–137.
