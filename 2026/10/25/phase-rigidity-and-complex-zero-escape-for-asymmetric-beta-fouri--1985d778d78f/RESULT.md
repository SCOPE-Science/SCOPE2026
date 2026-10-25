# Phase rigidity and complex-zero escape for asymmetric Beta Fourier transforms

## Finding

For all real \(p,q>0\), define the entire Fourier transform
\[
H_{p,q}(t)=\frac{1}{B(p,q)}\int_0^1 u^{p-1}(1-u)^{q-1}e^{it(2u-1)}\,du
=e^{-it}{}_1F_1(p;p+q;2it).
\]
Put \(m=p+q\) and \(\delta=p-q\). The following statements hold.

**Exact dichotomy and phase law.** The transform \(H_{p,q}\) has a real zero if and only if \(p=q\). If \(p\ne q\), then \(H_{p,q}(t)\ne0\) for every real \(t\). Its unique continuous unwrapped argument \(\theta_{p,q}:\mathbb R\to\mathbb R\), normalized by \(\theta_{p,q}(0)=0\), is strictly increasing for \(p>q\) and strictly decreasing for \(p<q\). More precisely, for every \(t>0\),
\[
\operatorname{Im}\bigl(H'_{p,q}(t)\overline{H_{p,q}(t)}\bigr)
=\delta\,t^{-m}\int_0^t s^{m-1}|H_{p,q}(s)|^2\,ds,
\]
\[
\theta'_{p,q}(t)
=\frac{\delta}{t^{m}|H_{p,q}(t)|^2}\int_0^t s^{m-1}|H_{p,q}(s)|^2\,ds.
\]
The phase derivative has the same strict sign for negative \(t\) and satisfies \(\theta'_{p,q}(0)=\delta/m\).

**Symmetric boundary.** If \(p=q=r>0\), let \(\nu=r-\tfrac12> -\tfrac12\). The complete real zero set is
\[
\{\pm j_{\nu,k}:k\ge1\},\qquad
H_{r,r}(t)=\Gamma(\nu+1)(2/t)^{\nu}J_\nu(t),
\]
with the continuous, entire interpretation at \(t=0\), where the \(j_{\nu,k}\) are the positive simple zeros of \(J_\nu\). Every real Fourier zero is simple.

**Quantified complex escape.** Fix \(m>0\), set \(p=(m+\delta)/2\), \(q=(m-\delta)/2\), and \(\nu=(m-1)/2\). For each fixed \(k\ge1\), there is a holomorphic zero branch \(t_k(\delta)\) for sufficiently small complex \(\delta\), with \(t_k(0)=j_{\nu,k}\), and for real \(\delta\to0\),
\[
t_k(\delta)=j_{\nu,k}+i C_{\nu,k}\delta+O_{m,k}(\delta^2),
\qquad
C_{\nu,k}=\frac{\int_0^{j_{\nu,k}}J_\nu(s)^2\,ds}{j_{\nu,k}J_\nu'(j_{\nu,k})^2}>0.
\]
These exact first-order imaginary velocities satisfy the further asymptotic
\[
C_{\nu,k}=\tfrac12\log k+O_\nu(1)\qquad(k\to\infty).
\]
The branch from a negative real zero is determined by \(H_{p,q}(-\overline z)=\overline{H_{p,q}(z)}\) and has the same leading imaginary displacement.

## Assumptions and scope

The distribution is \(Y=2U-1\) with \(U\sim\operatorname{Beta}(p,q)\), and the Fourier convention is \(e^{itY}\). Under the alternative convention \(e^{-2\pi i\xi Y}\), put \(t=-2\pi\xi\). The measure is a positive normalized probability measure for all \(p,q>0\), including parameters below one where its density has integrable endpoint singularities. The nonvanishing and phase claims concern the **real** frequency axis, not zero-freeness of the entire continuation. The complex-zero displacement takes \(\delta\to0\) with \(k,m\) fixed; the \(k\to\infty\) asymptotic applies to the derivative at \(\delta=0\) and is not a uniform two-parameter zero approximation.

## Proof

**1. The differential equation with its boundary conditions.** The probability density on \((-1,1)\) is
\[
w_{p,q}(y)=\frac{2^{1-m}}{B(p,q)}(1+y)^{p-1}(1-y)^{q-1}.
\]
Its product \((1-y^2)w_{p,q}(y)\) vanishes at both endpoints, because \(p,q>0\). Direct differentiation gives
\[
\frac{d}{dy}\{(1-y^2)w_{p,q}(y)\}
=\{\delta-my\}w_{p,q}(y).
\]
Multiply by \(e^{ity}\), integrate by parts and use \(H'(t)=i\int yw(y)e^{ity}\,dy\) and \(H''(t)=-\int y^2w(y)e^{ity}\,dy\). Therefore
\[
tH''(t)+mH'(t)+tH(t)=i\delta H(t),
\quad H(0)=1,\quad H'(0)=i\delta/m.
\]
The identity holds at \(t=0\) by continuity. The integrations remain legitimate for all \(p,q>0\), since the endpoint-vanishing product is absolutely continuous with integrable derivative.

**2. A sign-definite complex Wronskian.** For real \(t>0\) write \(H=H_{p,q}\) and
\[
W(t)=H'(t)\overline{H(t)}-H(t)\overline{H'(t)}.
\]
The differential equation and its conjugate imply
\[
W'(t)+\frac m t W(t)=\frac{2i\delta}{t}|H(t)|^2,
\quad \frac d{dt}\{t^mW(t)\}=2i\delta t^{m-1}|H(t)|^2.
\]
Since \(W(0)=2i\delta/m\) is finite and \(m>0\), the integration constant at zero is exactly zero. This proves the first boxed identity in the finding. For \(\delta\ne0\), the right side is strictly nonzero for every \(t>0\), as \(H(0)=1\) and the integrand is continuous and nonnegative. A zero of \(H(t)\) would force \(W(t)=0\), a contradiction. The identity \(H(-t)=\overline{H(t)}\) excludes negative real zeros; \(H(0)=1\). With no real zeros, the continuous logarithm of \(H\) exists globally on the real line. Dividing \(\operatorname{Im}(H'\overline H)\) by \(|H|^2\) gives its phase derivative, with sign \(\delta\). Reflection makes the phase odd and its derivative even. At the origin, \(H'(0)=i\delta/m\), giving \(\theta'(0)=\delta/m\).

**3. Every symmetric real zero is a simple Bessel zero.** When \(p=q=r\), the density is proportional to \((1-y^2)^{r-1}\). The classical Fourier–Bessel integral gives
\[
H_{r,r}(t)=\Gamma(r+\tfrac12)(2/t)^{r-1/2}J_{r-1/2}(t).
\]
The right-hand side is analytic and equals one at the origin. The order \(\nu=r-1/2>-1/2\) has infinitely many positive Bessel zeros, all simple, and these are the only real nonzero zeros. The negative zeros are their negatives by evenness.

**4. Derivative of each zero under asymmetry.** Fix \(m>0\) and set \(H_\delta(t)=H_{(m+\delta)/2,(m-\delta)/2}(t)\). Analytic dependence on \(\delta\) holds locally for \(|\delta|<m\) by dominated differentiation of the beta integral, and analyticity in complex \(t\) follows from compact support. Let \(h=H_0\), \(g=\partial_\delta H_\delta|_{\delta=0}\). Parameter differentiation of the differential equation gives
\[
tg''+mg'+tg=ih,\qquad th''+mh'+th=0.
\]
Consequently, the mixed Wronskian \(V=hg'-h'g\) satisfies
\[
(t^m V)'=it^{m-1}h(t)^2.
\]
Its integration constant at zero vanishes because \(h,g,h',g'\) are finite. At the simple zero \(j=j_{\nu,k}\),
\[
-j^m h'(j)g(j)=i\int_0^j s^{m-1}h(s)^2\,ds.
\]
The holomorphic implicit-function theorem gives a unique nearby zero \(t_k(\delta)\), and
\[
t_k'(0)=-g(j)/h'(j)
=i\frac{\int_0^j s^{m-1}h(s)^2\,ds}{j^m h'(j)^2}.
\]
Substitute \(h(s)=\Gamma(\nu+1)(2/s)^\nu J_\nu(s)\), and use \(m=2\nu+1\): its constant and power factors cancel to yield exactly the asserted positive \(C_{\nu,k}\). This proves the sign and local expansion. The reality symmetry relates the negative branch.

**5. Logarithmic growth of the velocities.** At fixed order \(\nu>-1/2\), standard Bessel large-argument asymptotics give
\[
J_\nu(s)^2=\frac{1+\cos(2s-\pi\nu-\pi/2)}{\pi s}+O_\nu(s^{-2})
\]
for large positive \(s\). The oscillatory integral converges conditionally after dividing by \(s\), so
\[
\int_0^{j_{\nu,k}}J_\nu(s)^2\,ds
=\pi^{-1}\log j_{\nu,k}+O_\nu(1).
\]
At a simple zero, the derivative Bessel asymptotic and \(j_{\nu,k}=\pi(k+\nu/2-1/4)+O_\nu(k^{-1})\) give
\[
j_{\nu,k}J_\nu'(j_{\nu,k})^2=2/\pi+O_\nu(k^{-1}).
\]
Division yields \(C_{\nu,k}=\tfrac12\log j_{\nu,k}+O_\nu(1)=\tfrac12\log k+O_\nu(1)\), completing the proof.

## Verification

The standalone `checker.py` uses `mpmath` at 55-digit precision. It evaluates the Kummer formula, its analytic frequency derivative, and the integrated Wronskian identity for five asymmetric and symmetric parameter choices. It then evaluates the exact Bessel-integral zero velocity for four choices of symmetric shape and zero index, and locates a perturbed complex zero at asymmetry \(\delta=2\cdot10^{-4}\) by high-precision root finding. The checker confirms the numerical identity and local displacement, not an exhaustive or infinite proof. Run `python checker.py` after installing the dependency in `requirements.txt`; see `CHECKER_OUTPUT.txt` for the representative execution output.

## Relationship to prior work

The beta/Kummer representation of weighted finite Fourier transforms is classical. Dixit, Jiu, Moll and Vignat [1] work out finite Fourier transforms of Jacobi-related functions, with their formula (1.4) giving a weighted hypergeometric representation. Their results provide the transform's known closed form, but their stated theorems concern evaluations, Jacobi polynomials and biorthogonality, not the all-parameter *real-axis zero dichotomy*, exact phase Wronskian, or the infinitesimal complex-zero drift. Lin and Luo [2], Theorem 1.3, establish a growth lower bound for the moduli of all Kummer zeros and cite the classical large-zero asymptotic; these statements neither locate all imaginary-axis zeros nor imply the present global phase identity. The NIST reference [3] tabulates **real-argument** zeros of the Kummer function and zero-free parabolic subsets of the complex plane, which are not the same as full imaginary-axis zero-freeness for all positive unequal Jacobi exponents. Milne [4] treats real zeros of Whittaker \(W\) and related special functions, not the present characteristic-function Wronskian and zero motion. The familiar Bessel diagonal case and all general Bessel asymptotics are used as established facts.

## Limitations

The claim does **not** classify the other complex zeros of the asymmetric Kummer function or their global trajectories, prove a uniform zero displacement simultaneously in the index and asymmetry, or give stable quantitative Fourier deconvolution bounds. Its phase identity depends on positive real beta shapes. Older comprehensive special-function theory, including Buchholz's and Slater's monographs discussed in [3], might contain equivalent zero-location results not identified by the accessible comparison. The present scientific assessment is a self-review only; no independent audit or priority certification has been performed.

## References

[1] A. Dixit, L. Jiu, V. H. Moll and C. Vignat, *The finite Fourier transform of classical polynomials*, arXiv:1402.5544 (first public 2014-02-22), especially Introduction, §3 and §5; https://arxiv.org/abs/1402.5544.

[2] W.-C. Lin and X.-D. Luo, *On the zeros of Confluent Hypergeometric Functions*, arXiv:1510.01285 (first public 2015-10-05), Theorem 1.3; https://arxiv.org/abs/1510.01285.

[3] NIST Digital Library of Mathematical Functions, §§13.4, 13.9 and §§10.17, 10.21; https://dlmf.nist.gov/13.9.

[4] A. Milne, *On the Roots of Confluent Hypergeometric Functions*, Proc. Edinburgh Math. Soc. 33, pp. 48–64 (1915 reading noted in primary text), doi:10.1017/S0013091500002352.
