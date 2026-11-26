# The local Wiener-norm profile at Bessel cusps for shrinking Malmquist poles

## Finding

For integers \(n\ge2\) and \(0\le c<n\), put \(\lambda=c/n\) and
\[
 f_{n,\lambda}(z)=\frac1{1-\lambda z}\left(\frac{z-\lambda}{1-\lambda z}\right)^{n-1},\qquad F(c)=\sum_{k\in\mathbb Z}|J_k(2c)|.
\]
For fixed \(C>0\), \(\|f_{n,c/n}\|_W=F(c)+O_C(n^{-1})\) uniformly on \([0,C]\). At \(c_0=j_{m,r}/2>0\), where \(j_{m,r}\) is the \(r\)-th positive zero of \(J_m\), define \(D=\tfrac12(F'_+(c_0)+F'_-(c_0))\). With \(u=s-c_0/2\), the local profile is
\[
 \lim_{n\to\infty} n\bigl(\|f_{n,(c_0+s/n)/n}\|_W-F(c_0)\bigr)
 =D u+
 \begin{cases}
  2|J'_0(2c_0)|\,|u|,&m=0,\\
  4|J'_m(2c_0)|\max\{|u|,mc_0/2\},&m\ge1.
 \end{cases}
\]
Convergence is uniform for \(s\) in compact sets. Thus after subtracting the linear part, the limiting first-order profile for \(m\ge1\) is constant between the two distinct kinks separated by \(mc_0\) in the scaled coordinate. The individual coefficient zero displacements are classical Jacobi endpoint-zero asymptotics in these coordinates; the claim here concerns the absolute sum of all coefficients.

## Assumptions and scope

The Wiener norm is the sum of moduli of the Taylor coefficients, or of the Laurent coefficients after centering on the unit circle. Hardy norms use normalized Haar measure. Here \(J_k\) is the Bessel function of the first kind. The local limit fixes \((m,r)\) before taking \(n\to\infty\). The estimate for bounded \(c\) also holds for the ratio to the Hardy norm because \(\|f_{n,c/n}\|_{H^2}=(1-c^2/n^2)^{-1/2}\) by the unit modulus of the Blaschke factor and the geometric series.

## Proof

Center at the \((n-1)\)-st mode and work in the Banach algebra of absolutely summable Laurent series on the circle. For \(n>2C\), the logarithms of the two factors of \(H_n=z^{-(n-1)}f_{n,c/n}=(1-(c/n)z^{-1})^{n-1}(1-(c/n)z)^{-n}\) converge in the algebra. Expanding through the indicated order gives
\[
 \log H_n=c(z-z^{-1})+n^{-1}Q_c+O_C(n^{-2}),\qquad
 Q_c=cz^{-1}+\tfrac{c^2}{2}(z^2-z^{-2}).
\]
The tail of each logarithmic series past degree two is bounded by \(n\sum_{j\ge3}(C/n)^j=O_C(n^{-2})\). Analyticity of the algebra exponential gives \(H_n=E_c+n^{-1}E_cQ_c+O_C(n^{-2})\), where \(E_c=\exp(c(z-z^{-1}))\). Its coefficients are \(J_k(2c)\) by the Bessel generating series. The first-order coefficient in mode \(k\) is
\[
 B_k(c)=cJ_{k+1}(2c)+\tfrac{c^2}{2}\bigl(J_{k-2}(2c)-J_{k+2}(2c)\bigr)=c(k-1)J'_k(2c),
\]
by \(J_{k-1}+J_{k+1}=(k/c)J_k\) and \(2J'_k=J_{k-1}-J_{k+1}\). The error is in \(\ell^1\), not merely mode by mode. Centering does not change the norm, so the reverse triangle inequality gives the bounded-\(c\) limit and its rate.

The positive zeros of each \(J_m\) are simple and, by Bourget's theorem, distinct nonnegative integral orders share none. For bounded complex \(c\), the series estimates \(|J_k(2c)|\le |c|^k e^{|c|^2}/k!\) for \(k\ge0\) give locally normally convergent tails. For positive bounded \(c\), the first term \(c^k/k!\) has a relative error bounded by \(\exp(C^2/(k+1))-1\), so all sufficiently high orders keep positive sign. Consequently \(F\) is real analytic on the positive axis off the Bessel half-zeros and the absolute-value sum restricted to nonzero modes at \(c_0\) is analytic near \(c_0\). Its derivative is \(D\), since the vanishing absolute-value terms have opposite one-sided derivatives. The derivative jumps are \(4|J'_0(2c_0)|\) for \(m=0\), \(8|J'_m(2c_0)|\) for \(m\ge1\).

Set \(a_k=J_k(2c_0)\) and \(d_k=2J'_k(2c_0)\). In the scaled coordinate \(s\), Taylor expansion in the algebra gives the coefficient sequence \(a+n^{-1}v(s)+O(n^{-2})\) uniformly for bounded \(s\), where \(v_k(s)=d_k(s+c_0(k-1)/2)\). The norm's right directional derivative is \(\sum_{a_k\ne0}\operatorname{sgn}(a_k)v_k+\sum_{a_k=0}|v_k|\): the coordinatewise difference quotients are bounded by \(|v_k|\) and \(v\in\ell^1\). Uniformity on compact \(s\)-sets follows from the uniform remainder and the Lipschitz bound \(\|v(s)-v(t)\|_1=|s-t|\|d\|_1\). For the nonzero-mode sum the terms proportional to \(k\) cancel by pairing \(k\) and \(-k\), giving \(D(s-c_0/2)\). At \(m=0\) the zero-mode contribution is \(2|J'_0||u|\); otherwise the two zero modes contribute \(2|J'_m|(|u+mc_0/2|+|u-mc_0/2|)\). This is the stated formula.

## Relation to individual coefficient roots and prior work

Binomial coefficient extraction, or the hypergeometric representation in DLMF 18.5.7, identifies the exact centered coefficient in mode \(k\ge0\) as \(\lambda^k P_{n-1}^{(k,0)}(1-2\lambda^2)\); in mode \(-m<0\), \(1\le m\le n-1\), it is \((-\lambda)^m P_{n-1-m}^{(m,0)}(1-2\lambda^2)\). The initial binomial coefficient in either extraction is the value of the indicated Jacobi polynomial at 1. By the Frenzen–Wong endpoint asymptotic (DLMF 18.16.8), the \(r\)-th zero measured in the angle \(\theta\) of \(P_d^{(\alpha,0)}(\cos\theta)\) obeys \(\theta=j_{\alpha,r}/(d+(\alpha+1)/2)+O_{\alpha,r}(d^{-3})\). Here \(d+(|k|+1)/2=n+(k-1)/2\) on both branches. Converting back by \(c=n\sin(\theta/2)\) gives precisely \(c=c_0+c_0(1-k)/(2n)+O_{m,r}(n^{-2})\) for each fixed \(k=\pm m\), with a single root at this scale for \(m=0\). Adjacent fixed Jacobi zero labels converge to different Bessel half-zeros. These individual locations are not claimed independently of the Jacobi result.

Auxemery, Borichev and Zarouf (arXiv:2603.03908v1) use the same Malmquist–Walsh witness in their fixed-pole inequality at \(\lambda\ge1/2\). Szehr and Zarouf (arXiv:1701.02358v1) and Borichev, Fouchet and Zarouf (arXiv:2107.00405) study fixed-pole powers of a Blaschke factor. The fixed-parameter estimates are not uniform in the shrinking-pole scaling used here. The local formula for the norm requires the summed first-order estimate and cancellation in the nonzero modes, not just the classical locations of individual zeros. For the Bessel generating formula and zero facts see DLMF §§10.12, 10.21; for the Jacobi formulas see DLMF §§18.5, 18.15–18.16.

## Verification and limitations

The accompanying `CHECK.py` uses NumPy and SciPy and is a finite Fourier check of the norm limit, first-order absolute-sum correction away from cusps, and sample root displacements. It is not a test of the full compact-uniform cusp-profile convergence; the Wiener-algebra argument proves that convergence. The result is for the prescribed rational family, not an optimal class-wide embedding constant, and is not an asymptotic for growing \(c\) or a joint classification of all finite-\(n\) coefficient zeros. Historical priority for equivalent norm-level formulas is not certified.
