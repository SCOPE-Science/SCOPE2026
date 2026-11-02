# Signed log-square spectral laws for boundary-chirp Bergman forms

## Finding

The analytic Bergman space of the disk admits a natural family of radial, highly oscillating boundary symbols whose multiplication forms may not be absolutely integrable, yet whose radial-cutoff Toeplitz extensions belong to every Schatten class. For the logarithmic radial coordinate \(u=-\log |z|^2\), fix \(0\le\beta<2\) and set
\[
\Phi_\beta(z)=u^{-\beta}\sin(1/u),\qquad 0<|z|<1.
\]
The value at the origin is immaterial. Write \(T_\beta\) for the extension of its radially cutoff form, as defined below. Its monomial eigenvalues, with \(s=n+1\), are
\[
\lambda_{s-1}(\beta)
=s\int_0^\infty e^{-su}u^{-\beta}\sin(1/u)\,du
=2s\,\operatorname{Im}\left[
 \left(\frac{-i}{s}\right)^{(1-\beta)/2}
 K_{1-\beta}(2\sqrt{-is})\right].
\]
Here \(K_\nu\) is the modified Bessel function of the second kind, with principal complex powers and roots. For every fixed \(0\le\beta<2\), uniformly as the integer \(s\to\infty\),
\[
\lambda_{s-1}(\beta)=\sqrt\pi\,s^{(2\beta+1)/4}e^{-\sqrt{2s}}
\left[\sin\left(\sqrt{2s}+\frac{\pi(2\beta-1)}8\right)
+O_\beta(s^{-1/2})\right].
\]
Consequently, \(T_\beta\in\mathcal S_p\) for every \(p>0\). Define its positive and negative spectral counting functions for \(\varepsilon>0\) by
\[
N_\pm(\varepsilon)=\#\{n\ge0:\ \pm\lambda_n(\beta)>\varepsilon\},
\qquad N_{\rm abs}=N_++N_-.
\]
For \(L=\log(1/\varepsilon)\to\infty\), both signs have the *sharp two-term law*
\[
\boxed{N_\pm(e^{-L})=\frac{L^2}{4}
+\frac{2\beta+1}{4}\,L\log L+O_\beta(L),}
\]
with the corresponding absolute count
\[
\boxed{N_{\rm abs}(e^{-L})=\frac{L^2}{2}
+\frac{2\beta+1}{2}\,L\log L+O_\beta(L).}
\]
In particular, the second counting coefficient recovers the singularity order \(\beta\) by the exact inverse relation
\[
\beta=\lim_{L\to\infty}\frac{N_{\rm abs}(e^{-L})-L^2/2}{L\log L}-\frac12.
\]
Every \(T_\beta\) has infinitely many positive and infinitely many negative eigenvalues. At \(\beta=3/2\) the eigenvalues have the elementary exact form
\[
\lambda_n(3/2)=\sqrt\pi(n+1)e^{-\sqrt{2(n+1)}}
\sin\left(\sqrt{2(n+1)}+\frac\pi4\right),
\]
none of which vanishes; thus this non-absolutely-integrable example gives an injective, self-adjoint, all-Schatten operator with two-sided infinite spectrum.

## Assumptions and scope

Use normalized area \(dA/\pi\) on \(\mathbb D\) and the Hilbert space \(A^2(\mathbb D)\) of holomorphic functions square integrable for that measure. The vectors \(e_n(z)=\sqrt{n+1}\,z^n\), \(n\ge0\), form an orthonormal basis. For polynomials \(f,g\) define the radial-cutoff sesquilinear form
\[
\mathfrak t_\beta[f,g]=\lim_{R\uparrow1}\frac1\pi
\int_{|z|<R}\Phi_\beta(z)f(z)\overline{g(z)}\,dA(z).
\]
The integral before the limit is ordinary Lebesgue integration. For \(1\le\beta<2\), the limiting form is generally **not** an absolutely convergent area integral, and no assertion about a multiplication-compression operator on an everywhere-defined \(L^2\) domain is intended. The bound on the form extends it uniquely from polynomials to \(A^2(\mathbb D)\); its representing bounded operator is \(T_\beta\). The spectral claims use precisely this radial-cutoff convention, with the stated normalization, and concern fixed real \(\beta\) in the given range.

## Proof

**1. Cutoff existence and the sharp domain boundary.** Angular integration makes distinct monomials orthogonal, so the only nonzero matrix coefficients to consider are diagonal. With \(s=n+1\), the squared radial variable \(t=|z|^2\), and then \(u=-\log t\), the diagonal coefficient is
\[
s\int_0^1 t^{s-1}(-\log t)^{-\beta}
\sin(1/(-\log t))\,dt
=s\int_0^\infty e^{-su}u^{-\beta}\sin(1/u)\,du.
\]
At infinity this integral converges absolutely. At \(u\downarrow0\), the substitution \(v=1/u\) gives a tail of the form
\[
\int_M^\infty e^{-s/v}v^{\beta-2}\sin v\,dv.
\]
Its real amplitude is eventually decreasing to zero if \(\beta<2\), so Dirichlet's test gives a finite limit. For \(\beta=2\) the oscillatory primitive has no limit, and for \(\beta>2\) the boundary terms in integration by parts have unbounded oscillation. Thus the **radial-cutoff prescription itself**, already tested on the constant polynomial, exists exactly when \(\beta<2\) among nonnegative exponents. In contrast, the symbol belongs to \(L^1(\mathbb D)\) exactly for \(0\le\beta<1\), since \(|\sin v|\) has positive mean and \(\int_M^\infty v^{\beta-2}|\sin v|\,dv\) converges precisely for \(\beta<1\).

**2. Exact Bessel transform and complete diagonal operator.** The classical Macdonald integral, initially for \(s>0\), \(\operatorname{Re}a>0\), reads
\[
\int_0^\infty u^{-\beta}e^{-su-a/u}\,du
=2(a/s)^{(1-\beta)/2}K_{1-\beta}(2\sqrt{as}).
\]
Approach \(a=-i\) through \(a=\eta-i\) as \(\eta\downarrow0\). For \(\beta<2\), the above Dirichlet estimate controls the oscillatory tail uniformly in \(\eta\), while dominated convergence handles every interval bounded away from zero. Taking imaginary parts proves the stated exact eigenvalue formula. Radial symmetry eliminates off-diagonal coefficients; the real eigenvalue sequence uniquely determines the bounded self-adjoint extension when it is bounded.

**3. Oscillatory spectral envelope.** On the fixed ray \(\arg z=-\pi/4\), the standard large-argument asymptotic for fixed \(\nu\) is
\[
K_\nu(z)=\sqrt{\frac\pi{2z}}e^{-z}(1+O_\nu(|z|^{-1})).
\]
Substitute \(z=2\sqrt{-is}=\sqrt{2s}(1-i)\) in the exact formula. Collecting positive powers and the argument of the prefactor gives
\[
\lambda_{s-1}(\beta)=A(s)(\sin\vartheta_s+E_s),
\quad A(s)=\sqrt\pi\,s^a e^{-\sqrt{2s}},
\quad a=\frac{2\beta+1}{4},
\]
where \(\vartheta_s=\sqrt{2s}+\pi(2\beta-1)/8\) and \(|E_s|\le C_\beta s^{-1/2}\) for all sufficiently large integer \(s\). The error is an **absolute error relative to the positive envelope** \(A(s)\), not a relative error to \(\sin\vartheta_s\); no estimate is asserted after division by an eigenvalue close to zero. The envelope gives \(\sum_{s\ge1}|\lambda_{s-1}|^p<\infty\) for each \(p>0\), by comparison with \(\sum s^{ap}e^{-p\sqrt{2s}}\). This proves boundedness of the cutoff form and all Schatten memberships.

**4. The discrete oscillation-counting lemma.** Let \(x_s=\sqrt{2s}\), fix a real \(\phi\), and take an increasing reference endpoint \(X\to\infty\). Among integers with \(x_s\le X\), the number satisfying
\[
|\sin(x_s+\phi)|\le C/x_s+C\exp(-(X-x_s)/2)
\]
is \(O_C(X)\), provided a fixed initial range \(x_s\le x_*\) is discarded. Indeed, each such point lies within a distance bounded by a constant multiple of \(x_k^{-1}+\exp(-(X-x_k)/2)\) from one of the phase zeros \(x_k=k\pi-\phi\). Because \(s=x_s^2/2\), the number of integer \(s\) in the corresponding short interval is at most
\[
O_C(1+x_k\exp(-(X-x_k)/2)).
\]
There are \(O(X)\) zeros below \(X\), and the exponentially weighted sum of their positions is \(O(X)\), since neighboring zeros are separated by \(\pi\). The same argument with only \(C/x_s\) shows that the phase-uncertain sign set has size \(O_C(X)\). Independently, the integers with \(x_s\le X\) and \(\sin(x_s+\phi)>0\), respectively \(<0\), each number \(X^2/4+O_\phi(X)\): adjacent positive and negative phase intervals have nearly equal lengths under \(s=x^2/2\), with at most one rounding error per interval and a total imbalance of \(O(X)\).

**5. Sharp signed counting.** For large \(L\), let \(X_L\) be the decreasing-branch solution of
\[
\sqrt\pi\,(X_L^2/2)^a e^{-X_L}=e^{-L}.
\]
Elementary logarithms give \(X_L=L+2a\log L+O_\beta(1)\). Hence
\[
S_L=X_L^2/2=\tfrac12L^2+2aL\log L+O_\beta(L).
\]
For \(x_s\) below \(X_L\) and above a fixed large threshold, the logarithmic derivative of the envelope with respect to \(x\) is \(2a/x-1\le-1/2\). Consequently, if \(|\lambda_{s-1}|\le e^{-L}\), then
\[
|\sin\vartheta_s|\le C_\beta/x_s+\exp(-(X_L-x_s)/2).
\]
By the counting lemma, only \(O_\beta(L)\) indices below \(S_L\) can be missed. Above \(x_s=X_L+C_\beta\), the envelope bound forbids eigenvalues of modulus greater than \(e^{-L}\); the intervening fixed-width shell in \(x\) contains \(O_\beta(L)\) integers. Therefore \(N_{\rm abs}(e^{-L})=S_L+O_\beta(L)\). By the lemma, the signs of the eigenvalues and the signs of \(\sin\vartheta_s\) disagree at only \(O_\beta(L)\) relevant indices, and those phase signs split equally up to \(O_\beta(L)\). Hence \(N_\pm(e^{-L})=S_L/2+O_\beta(L)\). Substituting \(a=(2\beta+1)/4\) proves both boxed two-term laws and the claim of infinitely many eigenvalues of each sign.

**6. Exact elementary case and the trace diagonal.** For \(\beta=3/2\), the identity \(K_{-1/2}(z)=\sqrt{\pi/(2z)}e^{-z}\) makes the asymptotic formula in Step 3 exact, with no error. Vanishing would force \(\sqrt{2s}=\pi(k-1/4)\) for an integer \(k\), contradicting transcendence of \(\pi\). Thus this operator is injective.

Finally, the Bergman diagonal kernel is \(K(z,z)=(1-|z|^2)^{-2}\). Its naively radially truncated symbol integral equals
\[
\int_{-\log R^2}^{\infty}
 \frac{e^{-u}u^{-\beta}\sin(1/u)}{(1-e^{-u})^2}\,du.
\]
As \(u\downarrow0\), the nonoscillatory factor equals \(u^{-\beta-2}+O(u^{-\beta})\). The error has a finite oscillatory improper integral for \(\beta<2\), while the leading term becomes \(\int^{\infty}v^\beta\sin v\,dv\), which has no limit for any \(\beta\ge0\). Thus the **naive symbol-times-kernel trace integral fails to converge**, although \(T_\beta\) is trace class. This does not contradict valid trace formulas expressed in terms of an operator's Berezin transform under their own hypotheses.

## Verification

The reproducibility program at `scripts/verify.py` compares the complex-Bessel eigenvalue formula with independently evaluated oscillatory integrals after \(v=1/u\); checks the exact half-integer Bessel specializations; tests the absolute-envelope asymptotic away from assuming nonzero sine; and compares finite positive, negative and total counts with the two-term profiles. It executed successfully with **93 finite assertions** in the documented numerical environment. These checks do not certify the infinitely many eigenvalues or the asymptotic error term; Steps 1–6 contain the analytical arguments for those statements.

## Relationship to prior work

Taskinen and Virtanen (2017), especially their Proposition 3.2, analyze a closely related inverse-boundary radial sine symbol and prove generalized boundedness despite its absolute-value Toeplitz operator being unbounded. Hagger, Liu, Taskinen and Virtanen (2020, first posted; published 2022) prove broad sufficient conditions and give arbitrarily growing oscillatory radial symbols inducing compact operators. Both works provide the natural motivation and the correct generalized-operator context; neither inspected discussion supplies the present exact Bessel eigenvalues or the **two-term, sign-resolved** logarithmic spectral counts. Rozenblum's earlier sign-changing radial Toeplitz results demonstrate cancellation and fast spectral decay for different, primarily compact-support or Fock-space regimes, but do not imply the disk-boundary chirp counts. Rozenblum and Vasilevski (2019) develop trace-class forms with singular symbols and Berezin-transform trace formulas; those must be distinguished from the divergent, naive symbol-diagonal integral above. Trieu Le (2010) constructs positive, radially unbounded, trace-class Bergman Toeplitz operators using sparse-support symbols, and justifies the kernel-diagonal trace formula there by positivity; that construction is different from the present conditionally integrated sign-changing chirp and divergent naive diagonal. Classical Bessel integral and asymptotic identities are used as known ingredients, not claimed as new.

## Limitations

The symbol is specifically a reciprocal-logarithmic radial sine chirp on the unweighted unit disk, with fixed real \(0\le\beta<2\). Beyond that range the **specified radial-cutoff form** fails already on constants, but alternative generalized regularizations are not ruled out. The statements do not determine individual eigenvalue-order corrections near sine zeros, exact signed traces, or an optimal remainder below \(O_\beta(L)\). The novelty comparison is based on inspected relevant texts and database searches; an equivalent earlier formulation under a different symbol change of variables remains a historical-priority risk. No independent mathematical validation is claimed.

## References

1. J. Taskinen and J. A. Virtanen, *On generalized Toeplitz and little Hankel operators on Bergman spaces*, arXiv:1703.09896 (first version March 29, 2017), especially Proposition 3.2, https://arxiv.org/abs/1703.09896.
2. R. Hagger, C. Liu, J. Taskinen, and J. A. Virtanen, *Toeplitz operators on the unit ball with locally integrable symbols*, arXiv:2011.04699 (first version November 9, 2020), especially Section 6, https://arxiv.org/abs/2011.04699.
3. G. Rozenblum, *On lower eigenvalue estimates for Toeplitz operators with radial symbols in Bergman spaces*, arXiv:1012.3528 (2010), especially Section 5, https://arxiv.org/abs/1012.3528.
4. G. Rozenblum and N. Vasilevski, *Trace class Toeplitz operators with singular symbols*, arXiv:1912.05855 (2019), https://arxiv.org/abs/1912.05855.
5. T. Le, *Trace class Toeplitz operators with unbounded symbols on weighted Bergman spaces* (2010), especially Theorem 1 and its proof, https://www.math.utoledo.edu/~tle20/Data/Trace2010.pdf.
6. NIST Digital Library of Mathematical Functions, modified Bessel function \(K_\nu\), integral representations and large-argument asymptotics, https://dlmf.nist.gov/10.
