# Exact Cesàro norm limit for the harmonic firmly nonexpansive counterexample
## Finding
Let \(X\) be the infinite-dimensional real Hilbert space and let \(T:X	o X\) be the firmly nonexpansive mapping from the harmonic-mesh construction of Bauschke and Tung. Fix \(0<\delta\le 1/8\). In the notation of that construction,
\[
d_n=\frac{\delta}{n},\qquad t_n=\delta H_{n-1},\qquad \rho_n=\exp\bigl(-\delta^2H_{n-1}^{(2)}\bigr),\qquad x_n=\rho_nu(t_n),
\]
where \(H_m=\sum_{k=1}^m k^{-1}\), \(H_m^{(2)}=\sum_{k=1}^m k^{-2}\), and \(u\) is the Gaussian-kernel curve satisfying
\[
\langle u(s),u(t)\rangle=e^{-(s-t)^2}.
\]
The source proves that \(x_n=T^{n-1}x_1\), that \(x_n\rightharpoonup0\), and that the Cesàro means
\[
y_n=\frac1n\sum_{k=1}^n x_k
\]
are uniformly bounded away from zero. In fact, their norms have the exact limit
\[
\lim_{n\to\infty}\|y_n\|
=e^{-\delta^2\pi^2/6}
\left(\int_0^1e^{-\delta^2(\log r)^2}\,dr\right)^{1/2}.
\]
Equivalently,
\[
\lim_{n\to\infty}\|y_n\|
=e^{-\delta^2\pi^2/6}
\left[
\frac{\sqrt\pi}{2\delta}e^{1/(4\delta^2)}
\operatorname{erfc}\!\left(\frac1{2\delta}\right)
\right]^{1/2},
\]
where \(\operatorname{erfc}(a)=\frac2{\sqrt\pi}\int_a^\infty e^{-s^2}\,ds\). In particular, the harmonic example has a unique positive asymptotic Cesàro norm rather than merely a positive lower envelope.

## Assumptions and scope
The parameter range \(0<\delta\le1/8\) is exactly the harmonic-mesh regime for which the cited construction supplies the firmly nonexpansive mapping and the stated orbit. The result concerns the norm asymptotic of this particular orbit; it does not assert norm convergence of the vectors \(y_n\), which in fact converge weakly to zero. No assertion is made about arbitrary firmly nonexpansive maps or about the block-mesh variants in the same source.

## Proof
The source gives, for all \(i,j\ge1\),
\[
\langle x_i,x_j\rangle
=\rho_i\rho_j
\exp\!\left(-\delta^2(H_{i-1}-H_{j-1})^2\right).
\]
Consequently,
\[
\|y_n\|^2
=\frac1{n^2}\sum_{i,j=1}^n
\rho_i\rho_j
\exp\!\left(-\delta^2(H_{i-1}-H_{j-1})^2\right).
\]
Also \(\rho_n\to\rho_\infty=e^{-\delta^2\pi^2/6}\). Since \(0<\rho_n\le1\),
\[
\frac1{n^2}\sum_{i,j=1}^n
\left|\rho_i\rho_j-\rho_\infty^2\right|
\le \frac2n\sum_{i=1}^n|\rho_i-\rho_\infty|\longrightarrow0
\]
by Cesàro convergence. It therefore remains to evaluate
\[
A_n=\frac1{n^2}\sum_{i,j=1}^n
\exp\!\left(-\delta^2(H_{i-1}-H_{j-1})^2\right).
\]
Fix \(0<\varepsilon<1\). Uniformly for \(i,j\ge\varepsilon n\), the harmonic-number asymptotic \(H_{m}=\log m+\gamma+O(m^{-1})\) gives
\[
H_{i-1}-H_{j-1}=\log(i/j)+o(1).
\]
Hence the part of \(A_n\) with \(i,j\ge\varepsilon n\) is a Riemann sum converging to
\[
\int_\varepsilon^1\!\int_\varepsilon^1
\exp\!\left(-\delta^2(\log(s/t))^2\right)\,ds\,dt.
\]
The omitted indices have total normalized weight at most \(2\varepsilon\). Letting first \(n\to\infty\) and then \(\varepsilon\downarrow0\) therefore yields
\[
A_n\longrightarrow I_\delta
:=\int_0^1\!\int_0^1
\exp\!\left(-\delta^2(\log(s/t))^2\right)\,ds\,dt.
\]
By symmetry and the substitution \(s=rt\) on the triangle \(0<s<t<1\),
\[
I_\delta
=\int_0^1 e^{-\delta^2(\log r)^2}\,dr.
\]
With \(u=-\log r\),
\[
I_\delta=\int_0^\infty e^{-\delta^2u^2-u}\,du
=\frac{\sqrt\pi}{2\delta}e^{1/(4\delta^2)}
\operatorname{erfc}\!\left(\frac1{2\delta}\right).
\]
Thus \(\|y_n\|^2\to\rho_\infty^2I_\delta\). Taking the positive square root proves the claim.

## Verification
The critical source identities were checked in the full text: the recurrence and limit for \(\rho_n\), the Gaussian inner-product formula for \(x_n\), the harmonic choice \(d_n=\delta/n\), and the source's lower bound for \(\|y_n\|\). The proof above then uses only Cesàro convergence, the standard uniform harmonic-number asymptotic away from zero, a bounded-kernel Riemann-sum limit, and an elementary Gaussian integral.

As a non-probative numerical sanity check, the closed form gives approximately \(0.960538\) at \(\delta=1/8\); direct finite double sums approach this value. The numerical check is not used in the proof.

## Relationship to prior work
Bauschke and Tung construct the firmly nonexpansive orbit and prove in the harmonic case that \(y_n\rightharpoonup0\) while \(\inf_n\|y_n\|>0\). Their displayed argument supplies a uniform lower bound but does not identify a norm limit. The result here evaluates the complete two-index Gaussian-kernel average and gives that missing exact asymptotic.

Earlier nonlinear mean-ergodic counterexamples, including the order-preserving nonexpansive examples of Krengel and Lin, establish failure of strong Cesàro convergence in broader nonlinear classes. They do not imply the exact Gaussian harmonic-mesh norm limit above.

## Limitations
The theorem is tied to the harmonic-mesh orbit and its Gaussian kernel. It does not classify Cesàro norm limits for other meshes, does not upgrade weak convergence to norm convergence, and does not give an exact asymptotic for the oscillatory block construction. The originality comparison is necessarily literature-bounded: an equivalent calculation under different terminology could exist outside the inspected sources.

## References
1. H. H. Bauschke and T. T. Tung, *Cesàro means of firmly nonexpansive iterates need not converge strongly*, arXiv:2605.25491v1, 2026; full-text revision arXiv:2605.25491v2.
2. U. Krengel and M. Lin, *Order preserving nonexpansive operators in L1*, Israel Journal of Mathematics 58 (1987), 170–192.
