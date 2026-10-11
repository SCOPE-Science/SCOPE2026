# Exact endpoint norm and dyadic parity law for the cyclic Hilbert transform
## Finding
For every integer \(N\ge 3\), let \(H_N\) be the Fourier multiplier on \(\mathbb Z_N\) that multiplies positive non-Nyquist frequencies by \(-i\), negative frequencies by \(+i\), and frequency \(0\) by \(0\); for even \(N\), the Nyquist frequency is also multiplied by \(0\). With normalized counting measure, define
\[
L_N=\|H_N\|_{\ell^1\to\ell^1}=\|H_N\|_{\ell^\infty\to\ell^\infty}.
\]
Then, for odd \(N\),
\[
L_N=\frac{2}{N}\sum_{j=0}^{(N-3)/2}\cot\!\left(\frac{(2j+1)\pi}{2N}\right),
\]
and, for even \(N\),
\[
L_N=\frac{4}{N}\sum_{j=0}^{\lfloor (N-2)/4\rfloor}\cot\!\left(\frac{(2j+1)\pi}{N}\right).
\]
In particular,
\[
L_{2N}=L_N\qquad\text{for every odd }N\ge3.
\]
The exact formulas have three asymptotic residue classes. If \(\gamma\) is Euler's constant, then along odd \(N\),
\[
L_N=\frac{2}{\pi}\log N+\frac{2}{\pi}\left(\gamma+\log\frac{4}{\pi}\right)-\frac{7\pi}{36N^2}+O(N^{-4}),
\]
while along even \(N\),
\[
L_N=\frac{2}{\pi}\log N+\frac{2}{\pi}\left(\gamma+\log\frac{2}{\pi}\right)+
\begin{cases}
\frac{2\pi}{9N^2}+O(N^{-4}),&4\mid N,\\
-\frac{7\pi}{9N^2}+O(N^{-4}),&N\equiv2\pmod4.
\end{cases}
\]
Thus doubling an odd cycle leaves the exact endpoint norm unchanged, even though the logarithmic normalization changes by the expected \((2/\pi)\log 2\) shift.

## Assumptions and scope
The Fourier transform is normalized by
\[
\widehat f(k)=\frac1N\sum_{x\in\mathbb Z_N}f(x)e^{-2\pi i kx/N},
\]
with inversion \(f(x)=\sum_k\widehat f(k)e^{2\pi i kx/N}\). For \(1\le p<\infty\), the norm is computed with normalized counting measure, \(\|f\|_p=(N^{-1}\sum_x|f(x)|^p)^{1/p}\); \(\|f\|_\infty=\max_x|f(x)|\). Reversing the sign convention for the Hilbert multiplier replaces \(H_N\) by \(-H_N\) and does not alter the norm.

The claim concerns the canonical finite DFT Hilbert phase shifter and only the endpoint norms \(p=1\) and \(p=\infty\). It does not claim sharp norms for intermediate exponents.

## Proof
Let \(K_N\) be the inverse Fourier transform of the multiplier, so that
\[
H_Nf(x)=\frac1N\sum_{y\in\mathbb Z_N}K_N(x-y)f(y).
\]
If \(N=2m+1\) is odd, then
\[
K_N(r)=2\sum_{k=1}^{m}\sin\!\left(\frac{2\pi kr}{N}\right).
\]
For \(r\ne0\), the finite sine-sum identity gives
\[
K_N(r)=
\begin{cases}
\cot\!\left(\frac{\pi r}{2N}\right),&r\text{ odd},\\
-\tan\!\left(\frac{\pi r}{2N}\right),&r\text{ even}.
\end{cases}
\]
Indeed, with \(\delta=\pi r/(2N)\), the numerator reduces to \(\sin^2(\pi r/2)-\sin^2\delta\). Pairing \(r\) with \(N-r\), and using \(\tan(\pi j/N)=\cot((N-2j)\pi/(2N))\), converts the absolute kernel sum into the stated odd cotangent sum.

If \(N=2m\) is even, then
\[
K_N(r)=2\sum_{k=1}^{m-1}\sin\!\left(\frac{2\pi kr}{N}\right)
=
\begin{cases}
2\cot\!\left(\frac{\pi r}{N}\right),&r\text{ odd},\\
0,&r\text{ even}.
\end{cases}
\]
Pairing \(r\) with \(N-r\) gives the stated even cotangent sum; when \(N\equiv2\pmod4\), its last displayed cotangent is \(\cot(\pi/2)=0\).

Every row and every column of the convolution matrix is a translate of \(K_N/N\). Hence
\[
\|H_N\|_{\ell^\infty\to\ell^\infty}\le \frac1N\sum_r|K_N(r)|,
\qquad
\|H_N\|_{\ell^1\to\ell^1}\le \frac1N\sum_r|K_N(r)|.
\]
Both inequalities are sharp. For the \(\ell^\infty\) norm, choose the real sign pattern \(f(y)=\operatorname{sgn}(K_N(-y))\), assigning any value of modulus at most one where the kernel vanishes. Then \(|H_Nf(0)|=N^{-1}\sum_r|K_N(r)|\). For the normalized \(\ell^1\) norm, a point mass of height \(N\) has norm one and its image has norm \(N^{-1}\sum_r|K_N(r)|\).

If \(N\) is odd, apply the even formula to \(2N\). Its upper index is \((N-1)/2\), and the last term is \(\cot(\pi/2)=0\); the remaining terms are exactly the odd formula for \(N\). This proves \(L_{2N}=L_N\).

For the asymptotics, put \(g(x)=\cot x-1/x\), extended smoothly by \(g(0)=0\). Then
\[
\int_0^{\pi/2}g(x)\,dx=\log\frac{2}{\pi},
\qquad
g'(0)=-\frac13,
\qquad
g'\!\left(\frac\pi2\right)=-1+\frac4{\pi^2}.
\]
Also
\[
\sum_{j=0}^{q-1}\frac1{j+1/2}=2H_{2q}-H_q.
\]
For \(N=4q\), midpoint Euler--Maclaurin applied to \(g\) on \([0,\pi/2]\), together with the harmonic-number expansion, gives
\[
2H_{2q}-H_q=\log q+2\log2+\gamma+\frac1{24q^2}+O(q^{-4}),
\]
and
\[
\frac{\pi}{2q}\sum_{j=0}^{q-1}g\!\left(\frac{(j+1/2)\pi}{2q}\right)
=\log\frac2\pi+\left(\frac{\pi^2}{144}-\frac1{24}\right)q^{-2}+O(q^{-4}).
\]
Substitution yields the \(4\mid N\) expansion. For odd \(N\), the same midpoint formula is applied up to \(\pi/2-\pi/(2N)\); Taylor expansion of the endpoint and of the harmonic numbers gives cancellation of the odd inverse powers through order three and leaves \(-7\pi/(36N^2)+O(N^{-4})\). Finally, the \(N\equiv2\pmod4\) expansion follows from the exact identity \(L_N=L_{N/2}\), because \(N/2\) is odd.

## Verification
The bundled script `verify.py` reconstructs the multiplier kernel directly, compares it with the closed cotangent/tangent formulas for many cycle sizes, compares direct absolute row sums with both exact norm formulas, checks the exact odd-to-double identity numerically, and checks convergence to each displayed second-order asymptotic coefficient. It is a regression check; the universal proof is the finite-sum and Euler--Maclaurin argument above.

## Relationship to prior work
Gold, Oppenheim and Rader's 1969 finite-length Hilbert-transform construction specifies the DFT phase samples that underlie the present multiplier, including the zero and Nyquist conventions. The inspected finite-length section does not derive the induced \(\ell^1\) or \(\ell^\infty\) operator norm, the cotangent row-sum formulas, the odd-to-double identity, or the residue-class asymptotics proved here.

De Carli and Samad study discrete Hilbert and Kak--Hilbert transforms on the infinite lattice \(\mathbb Z\), including their Fourier multiplier viewpoint and \(\ell^p\) behavior. Their object is not the finite cyclic DFT multiplier, and their results do not imply these finite endpoint formulas.

Fermo and Loi study quadrature approximations of the Hilbert transform on the unit circle. Their operators approximate a continuous principal-value integral and are not the finite cyclic Fourier multiplier considered here. Published-index searches for the exact cotangent norms, the dyadic identity, and the three residue-class asymptotics did not locate an equivalent or stronger statement.

## Limitations
The result is confined to the endpoint operator norms of this specific cyclic sign multiplier. It does not determine sharp \(\ell^p\) norms for \(1<p<\infty\), nor does it assert that the cotangent kernel formulas themselves are new. The main originality claim is the combined exact endpoint norm law, its dyadic invariance, and the explicit residue-class asymptotics. A residual risk remains that older signal-processing literature may contain an equivalent endpoint row-sum identity under finite-length Hilbert-transform terminology.

## References
R. Gold, A. V. Oppenheim, and C. M. Rader, *Theory and Implementation of the Discrete Hilbert Transform*, presented at the Symposium on Computer Processing in Communications, April 8--10, 1969.

L. De Carli and G. S. Samad, *One-parameter groups of operators and discrete Hilbert transforms*, arXiv:1506.03362v1, first public June 10, 2015.

L. Fermo and V. Loi, *Approximation of the Hilbert Transform On The Unit Circle*, Journal of Scientific Computing 105 (2025), article 23, DOI:10.1007/s10915-025-03044-3.
