# Exact arithmetic aliasing and prime-optimal time quadrature for quadratic Fourier flows

## Finding

Let \(K\geq 0\), \(N\geq 1\) be integers, and let \(a=(a_0,\ldots,a_K)\in\mathbb C^{K+1}\). For \(x,t\in\mathbb R/\mathbb Z\), put
\[
U_a(x,t)=\sum_{n=0}^{K}a_ne^{2\pi i(nx+n^2t)},\qquad
Q_{K,N}(a)=\frac1N\sum_{j=0}^{N-1}\int_0^1|U_a(x,j/N)|^4\,dx,
\]
and define \(Q_{K,\infty}(a)=\int_0^1\int_0^1|U_a(x,t)|^4\,dx\,dt\). Let \(d_N=N/\gcd(N,2)\) and, for every positive integer \(d\), set
\[
\sigma(d)=\min_{v\mid d}\left(v+\frac d v\right).
\]

**Exact quadrature theorem.** For every \(K,N,a\),
\[
Q_{K,\infty}(a)=2\left(\sum_{n=0}^{K}|a_n|^2\right)^2-\sum_{n=0}^{K}|a_n|^4,
\]
and the *exact signed sampling defect* is
\[
Q_{K,N}(a)-Q_{K,\infty}(a)
=4\!\sum_{\substack{h,r\ge1,\;h+r\le K\\N\mid 2hr}}
\ \sum_{m=0}^{K-h-r}
\operatorname{Re}\left(a_{m+h+r}\overline{a_{m+r}}\,\overline{a_{m+h}}a_m\right).
\]
Consequently, the identity \(Q_{K,N}(a)=Q_{K,\infty}(a)\) holds **for every** complex coefficient vector \(a\) if and only if
\[
\boxed{\ K<\sigma(d_N).\ }
\]

**Sharp quartic norm and optimal time-grid size.** Define the best sampled fourth-power norm constant
\[
C_{K,N}=\sup_{a\ne0}\frac{Q_{K,N}(a)}{\left(\sum_{n=0}^{K}|a_n|^2\right)^2}.
\]
For all \(K\ge0\),
\[
\boxed{\ C_{K,N}=2-\frac1{K+1}\quad\Longleftrightarrow\quad K<\sigma(d_N).\ }
\]
In the equality regime the nonzero maximizing vectors are precisely those with all \(|a_n|\) equal; all phases are unrestricted. Outside it, \(C_{K,N}>2-1/(K+1)\).

For every \(K\ge2\), the **smallest positive number of equally spaced time samples** giving exact quadrature for all coefficient vectors (equivalently, preserving the sharp constant) is
\[
\boxed{\ p_K=\min\{p\ge K:p\text{ is an odd prime}\}.\ }
\]
Thus the exact temporal quadrature requirement grows linearly in bandwidth, although an unrestricted time-frequency degree bound would suggest a quadratic number of samples. These statements also hold for any translated consecutive frequency band.

## Assumptions and scope

All spatial and temporal integrals use normalized Haar measure on \(\mathbb R/\mathbb Z\); the time grid is exactly \(\{j/N:0\le j<N\}\). The Fourier modes are consecutive integers with quadratic dispersion \(n\mapsto n^2\). Coefficients are arbitrary complex numbers, including zero entries. The result is valid for all \(N\ge1\) and all \(K\ge0\), except that the least-grid prime assertion is stated for \(K\ge2\) because \(K=0,1\) requires only one time sample.

## Proof

**1. Spatial orthogonality.** For \(0\le h\le K\), define
\[
B_h(t)=\sum_{m=0}^{K-h}a_{m+h}\overline{a_m}\,e^{2\pi i(2hm+h^2)t}.
\]
The spatial Fourier coefficient of \(|U_a(x,t)|^2\) at frequency \(h>0\) is \(B_h(t)\), at frequency \(-h\) it is \(\overline{B_h(t)}\), and at zero it is \(S=\sum_n|a_n|^2\). Parseval therefore gives
\[
\int_0^1|U_a(x,t)|^4\,dx=S^2+2\sum_{h=1}^{K}|B_h(t)|^2.
\]

**2. Temporal orthogonality and the exact defect.** In the expansion of \(|B_h(t)|^2\), indices \(m,n\) contribute a temporal character of frequency \(2h(m-n)\). The time integral retains just \(m=n\), giving
\[
Q_{K,\infty}(a)=S^2+2\sum_{h=1}^{K}\sum_{m=0}^{K-h}|a_{m+h}|^2|a_m|^2
=2S^2-\sum_n|a_n|^4.
\]
The \(N\)-point average retains the integer frequencies divisible by \(N\). Pair each off-diagonal term \(m\ne n\) with its conjugate, and write the positive distance \(r=|m-n|\). This produces exactly the displayed signed-defect identity, with all \(1\le h,r\), \(h+r\le K\), and \(0\le m\le K-h-r\).

**3. Arithmetic no-alias threshold.** The divisibility \(N\mid 2hr\) is equivalent to \(d_N\mid hr\). If \(d_N\mid hr\), let \(v=\gcd(d_N,h)\). Then \(v\mid h\) and \(d_N/v\mid r\), so
\[
h+r\ge v+d_N/v\ge\sigma(d_N).
\]
Conversely, a divisor \(v\mid d_N\) attaining \(\sigma(d_N)\) supplies \(h=v\), \(r=d_N/v\), hence a collision whenever \(K\ge\sigma(d_N)\). If such a collision exists, set every \(a_n=1\). Every term in the defect is nonnegative and at least one is strictly positive, so equality cannot hold for all coefficient vectors. This proves both directions of the threshold, including its boundary.

**4. Sharp constant and equality cases.** In the absence of collisions, Cauchy--Schwarz gives
\[
Q_{K,N}(a)=2S^2-\sum|a_n|^4
\le\left(2-\frac1{K+1}\right)S^2,
\]
with equality precisely at constant coefficient magnitude (for nonzero \(a\)). If a collision exists, the all-ones vector yields strict enlargement of this bound relative to the continuous constant, hence \(C_{K,N}>2-1/(K+1)\).

**5. Exact minimal sample count.** Let \(p_K\) be the least odd prime \(\ge K\). With \(N=p_K\), one has \(d_N=p_K\) and \(\sigma(d_N)=p_K+1>K\), so this grid works. The elementary Bertrand--Chebyshev prime-between-\(K\)-and-\(2K\) theorem gives \(p_K<2K\) for \(K\ge2\). For \(N<p_K\), if \(N<K\), then \(\sigma(d_N)\le d_N+1\le K\). If \(N\ge K\) is even, then \(d_N=N/2<K\) and again \(\sigma(d_N)\le K\). If \(N\ge K\) is odd, it is composite by the definition of \(p_K\). For \(K\ge9\), choose a divisor \(v\) with \(3\le v\le\sqrt N\). Since \(x+N/x\) decreases on \((0,\sqrt N]\),
\[
\sigma(N)\le v+N/v\le3+N/3<3+2K/3\le K.
\]
For \(2\le K\le8\), direct divisor checks with \(p_K=3,3,5,5,7,7,11\), respectively, give the same conclusion (the only odd composite with \(K\le N<p_K\) is \(K=8,N=9\), and \(\sigma(9)=6\)). Thus no smaller \(N\) works. Translating the Fourier band by an integer multiplies \(U\) by a unit character and changes \(x\) by \(2n_0t\), preserving its spatial fourth moment for each \(t\). This finishes the proof.

## Verification

The standalone file `verify.py` performs finite integer-arithmetic tests independent of trigonometric quadrature floating-point evaluation. It enumerates momentum and quadratic-time congruence relations directly for \(0\le K\le11\), \(1\le N\le37\), compares the full fourth moment against the exact defect formula on two Gaussian-integer coefficient vectors per case, and checks the divisor threshold. It also checks least sample counts against primes for \(2\le K\le139\), plus an explicit signed-negative-defect instance. Run `python3 verify.py` in any standard-library Python 3 environment.

One boundary check: at \(K=2,N=2\) and \(a=(1,i,1)\), the sampled and continuous fourth moments equal \(11\) and \(15\), respectively; therefore the sampling defect is not pointwise nonnegative. The general proof is symbolic and does not depend on finite verification.

## Relationship to prior work

Bourgain's one-dimensional parabola restriction argument proves the continuous fourth-moment orthogonality mechanism, in particular the distinct-frequency uniqueness used in his Proposition 2.1. Hu--Li and Wooley study related *continuously integrated* discrete restriction/Strichartz norms. Matsutani--Onishi study quadratic phases at rational Talbot times through Gauss sums. The new target here is different: the exact arbitrary-coefficient **uniform temporal quadrature identity** and its signed alias terms, full divisor-sum criterion over all temporal moduli, the strict sharp-constant transition, and the globally minimal prime sampling cardinality. None of the inspected statements directly identifies this complete sampling law. The classical spatial/time Fourier orthogonality mechanism itself is not claimed as new.

## Limitations

The theorem concerns one spatial dimension, a consecutive spectral band, quadratic integer dispersion, the fourth moment, **uniform equally spaced samples beginning at zero**, and continuous spatial integration. It does not claim a sharp sampled constant in the aliasing regime, nor pointwise monotonicity of sampled moments, and it does not extend automatically to higher moments, altered dispersions, nonuniform time nodes or alternative spatial discretizations. The finite verifier is a diagnostic, not an infinite proof. A historically equivalent formula may exist in quadrature, wave/Talbot or finite Fourier literature beyond the inspected works; bibliographic priority is not certified.

## References

1. J. Bourgain, *Fourier transform restriction phenomena for certain lattice subsets and applications to nonlinear evolution equations, Part I: Schrödinger equations*, Geometric and Functional Analysis 3 (1993), 107--156. Relevant Proposition 2.1 and proof. Open full text: https://math.mit.edu/classes/18.158/bourgain-restriction.pdf.
2. S. Matsutani and Y. Ônishi, *Wave-Particle Complementarity and Reciprocity of Gauss Sums on Talbot Effects*, arXiv:math-ph/0207011v1, publicly submitted 2002-07-07; https://arxiv.org/abs/math-ph/0207011.
3. Y. Hu and X. Li, *Discrete Fourier restriction associated with Schrödinger equations*, arXiv:1108.5164v1 (2011); https://arxiv.org/abs/1108.5164.
4. T. D. Wooley, *Discrete Fourier restriction via efficient congruencing: basic principles*, arXiv:1508.05329v1 (2015); https://arxiv.org/abs/1508.05329.
