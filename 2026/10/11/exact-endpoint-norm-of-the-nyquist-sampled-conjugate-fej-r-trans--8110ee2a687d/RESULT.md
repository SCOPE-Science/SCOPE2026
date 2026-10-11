# Exact endpoint norm of the Nyquist-sampled conjugate Fejér transform
## Finding
For every integer \(n\ge2\), let \(T_n\) act on functions on \(\mathbb Z_{2n}\), with normalized counting measure, by the Fourier multiplier
\[
m_n(0)=m_n(n)=0,
\qquad
m_n(k)=-i\,\operatorname{sgn}(k)\left(1-\frac{|k|}{n}\right)
\]
for the representatives \(1\le |k|\le n-1\). Thus \(T_n\) is the conjugate Fejér, or first Cesàro-smoothed Hilbert, multiplier sampled at the critical Nyquist grid.

Its convolution kernel is exactly
\[
Q_n(r)=
\begin{cases}
0,&r=0\text{ or }r=n,\\[1mm]
\displaystyle \cot\!\left(\frac{\pi r}{2n}\right),&r\in\mathbb Z_{2n}\setminus\{0,n\},
\end{cases}
\]
and therefore its two endpoint operator norms coincide and have the sharp all-scale formula
\[
\boxed{
C_n:=\|T_n\|_{\ell^1\to\ell^1}
=\|T_n\|_{\ell^\infty\to\ell^\infty}
=\frac1n\sum_{r=1}^{n-1}\cot\!\left(\frac{\pi r}{2n}\right).
}
\]

The constants obey the exact two-scale identity
\[
\boxed{
2C_{2n}-C_n
=\frac1n\sum_{j=0}^{n-1}
\cot\!\left(\frac{(2j+1)\pi}{4n}\right).
}
\]
The right-hand side is exactly the endpoint norm of the untapered cyclic sign-Hilbert multiplier on \(\mathbb Z_{4n}\). Finally,
\[
C_n=
\frac{2}{\pi}\log n
+\frac{2}{\pi}\left(\gamma+\log\frac{2}{\pi}\right)
-\frac{\pi}{36n^2}
+O(n^{-4}).
\]

## Assumptions and scope
The Fourier transform uses the standard characters \(r\mapsto e^{2\pi i kr/(2n)}\) and normalized counting measure \((2n)^{-1}\sum_r\). The Nyquist character \(k=n\) is assigned multiplier zero, as is the constant character. The result concerns endpoint \(\ell^1\) and \(\ell^\infty\) norms of this particular first-order Cesàro taper; no interior \(\ell^p\) norm formula is asserted.

The source literature motivates the conjugate Fejér kernel as a regularized conjugate Fourier/Hilbert kernel. The finite cyclic operator here is defined independently by its multiplier, so the theorem does not depend on any normalization convention used for continuous kernels or sampling formulas in the cited sources.

## Proof
Pairing the positive and negative frequencies in Fourier inversion gives
\[
Q_n(r)=2\sum_{k=1}^{n-1}
\left(1-\frac{k}{n}\right)
\sin\!\left(\frac{\pi kr}{n}\right).
\]
For a real variable \(t\), the finite geometric-series identity and its derivative give
\[
2\sum_{k=1}^{n-1}\left(1-\frac{k}{n}\right)\sin(kt)
=
\frac{\sin t-\frac1n\sin(nt)}{1-\cos t}.
\]
At the grid point \(t=\pi r/n\), one has \(\sin(nt)=0\). For \(r\notin\{0,n\}\),
\[
Q_n(r)=\frac{\sin t}{1-\cos t}
=\cot\!\left(\frac t2\right)
=\cot\!\left(\frac{\pi r}{2n}\right).
\]
At \(r=0\) and \(r=n\), the original sine sum is zero. This proves the kernel formula.

Since convolution is normalized by \((2n)^{-1}\), Young's inequality gives
\[
\|T_n\|_{\ell^\infty\to\ell^\infty}
\le \frac1{2n}\sum_{r\in\mathbb Z_{2n}}|Q_n(r)|.
\]
Equality is attained by choosing an input whose values have the signs of the reflected kernel and evaluating at one point. Finite-dimensional duality gives the same \(\ell^1\)-norm. The cotangent is positive for \(1\le r\le n-1\), negative for \(n+1\le r\le2n-1\), and antisymmetric across \(n\). Hence
\[
\frac1{2n}\sum_r|Q_n(r)|
=\frac1n\sum_{r=1}^{n-1}\cot\!\left(\frac{\pi r}{2n}\right),
\]
which proves the sharp norm formula.

To obtain the two-scale identity, split the sum defining \(C_{2n}\) into even and odd indices:
\[
C_{2n}
=\frac1{2n}
\left[
\sum_{r=1}^{n-1}\cot\!\left(\frac{\pi r}{2n}\right)
+
\sum_{j=0}^{n-1}\cot\!\left(\frac{(2j+1)\pi}{4n}\right)
\right].
\]
The first bracketed sum is \(nC_n\), proving the displayed relation. The standard inverse transform of the untapered sign multiplier on \(\mathbb Z_{4n}\) has absolute row sum equal to the odd cotangent sum divided by \(n\), giving the stated interpretation.

For the asymptotic formula, write
\[
f(x)=\cot\!\left(\frac{\pi x}{2}\right)-\frac{2}{\pi x},
\qquad f(0):=0.
\]
Then
\[
C_n=\frac{2}{\pi}H_{n-1}
+\frac1n\sum_{r=1}^{n-1}f(r/n).
\]
The function \(f\) is smooth on \([0,1]\), with
\[
f(1)=-\frac2\pi,
\qquad
f'(0)=-\frac\pi6,
\qquad
f'(1)=-\frac\pi2+\frac2\pi,
\]
and
\[
\int_0^1 f(x)\,dx=\frac2\pi\log\frac2\pi.
\]
Combining Euler--Maclaurin for the Riemann sum with
\[
H_{n-1}=\log n+\gamma-\frac1{2n}-\frac1{12n^2}+O(n^{-4})
\]
cancels the \(n^{-1}\) terms and leaves the coefficient \(-\pi/36\) at order \(n^{-2}\). The next Euler--Maclaurin term is of order \(n^{-4}\), proving the expansion.

## Verification
The accompanying `verify.py` reconstructs the kernel independently from the Fourier multiplier for every \(2\le n\le240\), compares it with the cotangent formula at every grid point, compares direct absolute row sums with the closed norm, checks the two-scale identity for \(2\le n\le500\), and checks the predicted \(n^{-4}\) remainder scale at five larger values of \(n\). The replay output is stored in `verification_output.txt`.

These finite computations are corroborative only. The proof above establishes the identities for every integer \(n\ge2\).

## Relationship to prior work
Krasniqi's paper explicitly defines the conjugate Fejér kernel as the Cesàro average of conjugate Dirichlet kernels and uses it in an \(L^1\)-convergence argument. Its public article page records publication on March 11, 2011, and the paper lists 42A20 and 42A32 as its 2010 AMS classifications. It does not formulate the critical finite cyclic multiplier above or evaluate its sharp endpoint operator norm.

Boche and Pohl's 2015 presentation studies sampled conjugate Fejér means as approximations to the Hilbert transform and writes an explicit closed form for the continuous conjugate Fejér kernel. Their sampled operator and divergence estimates motivate the finite-grid stability question, but the inspected material does not state the exact \(\mathbb Z_{2n}\) cotangent collapse, the endpoint norm formula, or the two-scale identity proved here.

Targeted searches were performed under the equivalent formulations “sampled conjugate Fejer exact norm,” “discrete Lebesgue constant,” “cotangent sum,” “Cesàro-smoothed Hilbert multiplier,” and “finite cyclic endpoint norm.” No retrieved statement implied the theorem above. This is evidence for, not a proof of, originality.

## Limitations
Only the first Cesàro taper and the critical grid of size \(2n\) are treated. The theorem does not give sharp interior \(\ell^p\) norms, higher-order Cesàro tapers, or arbitrary oversampling ratios. An older equivalent cotangent-sum identity may exist in approximation-theory or signal-processing terminology not located by the searches. The asymptotic expansion is stated only through the first nonzero finite-size correction.

## References
1. X. Z. Krasniqi, “On L1-Convergence Of Rees-Stanojević's Sums With Coefficients From The Class K,” *Le Matematiche* 65(2), 25–32, DOI 10.4418/2010.65.2.3. Public article page: published 2011-03-11.
2. H. Boche and V. Pohl, “On the Strong Divergence of Hilbert Transform Approximations and a Problem of Ul'yanov,” Dortmund presentation, March 2015, section “Sampled Conjugate Fejer Means.”
