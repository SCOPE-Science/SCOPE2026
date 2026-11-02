# Two-branch spectral density for integer-oversampled hat-spline Gabor frames

## Finding

Let \(g(t)=(1-|t|)_+\) and, for each integer \(q\geq2\), let \(S_q\) be the Gabor frame operator on \(L^2(\mathbb R)\) for the lattice \((q^{-1}\mathbb Z)\times\mathbb Z\). Define
\[
L_q=\frac{q^2-1}{3q},\qquad C_q=\frac{q^2+2}{3q}.
\]
The spectrum of \(S_q\) is precisely \([L_q,q]\); these are its optimal lower and upper frame bounds. Its Zak-fiber spectral distribution \(\mu_q\), defined below, is absolutely continuous, with density
\[
\rho_q(\lambda)=
\begin{cases}
\dfrac{\sqrt q}{2\sqrt{q-\lambda}},&L_q<\lambda<C_q,\\[5pt]
\dfrac{\sqrt q}{\pi\sqrt{q-\lambda}}
\arcsin\!\left(\dfrac1{\sqrt{q(\lambda-L_q)}}\right),&C_q<\lambda<q,\\[5pt]
0,&\lambda\notin[L_q,q].
\end{cases}
\]
The branches join continuously at \(C_q\). The first branch fails to extend differentiably across \(C_q\): as \(\delta\downarrow0\),
\[
\rho_q(C_q+\delta)-\frac{\sqrt q}{2\sqrt{q-C_q-\delta}}
=-\frac{q}{\pi\sqrt{q-C_q}}\sqrt\delta+O_q(\delta^{3/2}).
\]
Moreover,
\[
\int\lambda\,d\mu_q(\lambda)=\frac{2q}{3},\qquad
\int\lambda^2\,d\mu_q(\lambda)=\frac{q^2}{2}+\frac1{30q^2}.
\]
The spectrum is purely absolutely continuous and there are no eigenvalues. As \(q\to\infty\), the distribution of \(\lambda/q\) under \(\mu_q\) converges weakly to the arcsine distribution on \([1/3,1]\), of density \(1/(\pi\sqrt{(t-1/3)(1-t)})\).

## Assumptions and scope

Use the Fourier modulation convention \(M_m f(t)=e^{2\pi i mt}f(t)\) and translation \(T_yf(t)=f(t-y)\). The frame family is \(\{M_mT_{j/q}g:m,j\in\mathbb Z\}\). All norms and frame bounds refer to unnormalized \(g=(1-|t|)_+\), not its unit-norm rescaling. The normalized period-one Zak transform is
\[
(Zf)(x,\theta)=\sum_{n\in\mathbb Z}f(x+n)e^{-in\theta},
\qquad (x,\theta)\in[0,1]\times[0,2\pi],
\]
with measure \(dx\,d\theta/(2\pi)\). It is unitary on \(L^2\). The canonical **fiber spectral distribution** is the probability measure
\[
\mu_q(E)=\int_0^1\int_0^{2\pi}
\mathbf1_{\{s_q(x,\theta)\in E\}}\,\frac{d\theta}{2\pi}\,dx
\]
for Borel \(E\), where \(s_q\) is the scalar multiplier derived below. This is a normalized distribution of Zak-fiber multipliers, **not** a finite trace of the operator on \(L^2(\mathbb R)\).

## Proof

**1. Diagonalization.** Poisson/Parseval summation over the integral modulation lattice, initially for smooth compactly supported test functions and then by boundedness, gives the exact Walnut identity
\[
S_qf(t)=\sum_{\ell\in\mathbb Z}f(t-\ell)
\sum_{j\in\mathbb Z}g(t-j/q)g(t-\ell-j/q).
\]
Because the window is supported on \([-1,1]\), only \(\ell=-1,0,1\) contribute, almost everywhere. Define the \(q^{-1}\)-periodic functions
\[
A_0(t)=\sum_jg(t-j/q)^2,\quad
A_1(t)=\sum_jg(t-j/q)g(t-1-j/q).
\]
The cardinal hat identity \(\sum_{\ell\in\mathbb Z}g(u-\ell)=1\) and \(\sum_jg(t-j/q)=q\) imply \(A_0(t)+2A_1(t)=q\). For \(0\le x\le q^{-1}\), summing the squares of the two arithmetic progressions of linear hat values yields exactly
\[
A_0(x)=\frac{2q}{3}+\frac1{3q}-2qx(q^{-1}-x).
\]
Since these coefficients are periodic with integer period, the Zak transform sends \(S_q\) to scalar multiplication by
\[
s_q(x,\theta)=A_0(x)+2A_1(x)\cos\theta
=q-D_q(x)(1-\cos\theta),
\]
where
\[
D_q(x)=\frac{q^2-1}{3q}+2qx(q^{-1}-x).
\]
The multiplier's maximum is \(q\), achieved at \(\theta=0\), while its minimum occurs at \(x=1/(2q)\) and \(\theta=\pi\), giving \(q-2((q^2-1)/(3q)+1/(2q))=L_q\). Continuity and connectedness of the parameter rectangle imply its essential range is \([L_q,q]\). As \(L_q>0\), the Gabor system is a frame with precisely those sharp constants.

**2. Exact spectral distribution.** Let \(U\) be uniform on \([0,1]\) and \(\Theta\) uniform on \([0,2\pi]\), independent. By periodicity, \(\mu_q\) is the law of
\[
\Lambda=q-D(1-\cos\Theta),\qquad
D=L_q+\frac2q U(1-U).
\]
Put \(d_0=L_q\) and \(d_1=L_q+1/(2q)\). A change of variables on the two monotone halves of \(U(1-U)\) gives the density
\[
f_D(d)=\frac{\sqrt{q/2}}{\sqrt{d_1-d}}\,
\mathbf1_{\{d_0<d<d_1\}}.
\]
Conditionally on \(D=d\), the variable \(Z=q-\Lambda=d(1-\cos\Theta)\) has density \(1/(\pi\sqrt{z(2d-z)})\) for \(0<z<2d\). Therefore
\[
f_Z(z)=\frac{\sqrt{q/2}}{\pi\sqrt z}
\int_{\max(d_0,z/2)}^{d_1}
\frac{dd}{\sqrt{(d_1-d)(2d-z)}},\quad 0<z<2d_1.
\]
The integral is elementary: it equals \(\pi/\sqrt2\) when \(z\ge2d_0\), and otherwise it equals
\[
\sqrt2\arcsin\sqrt{\frac{d_1-d_0}{d_1-z/2}}.
\]
Since \(z=q-\lambda\), \(q-2d_1=L_q\), \(q-2d_0=C_q\), and \(d_1-z/2=(\lambda-L_q)/2\), these expressions yield the displayed two-branch density. In particular it is a probability density because it was obtained from a pair of independent probability laws.

**3. Spectral type and shoulder.** Multiplication by the real scalar symbol has spectral projections given by multiplication by indicator functions of its inverse images. Because \(\mu_q\) is absolutely continuous, the inverse image of any Lebesgue-null spectral set has zero product measure. Consequently every scalar spectral measure of \(S_q\) is absolutely continuous, so there are neither point eigenvalues nor a singular-continuous part. At \(\lambda=C_q+\delta\) the identity
\[
\arcsin\left((1+q\delta)^{-1/2}\right)
=\frac\pi2-\sqrt{q\delta}+O_q(\delta^{3/2})
\]
proves the stated sharp square-root shoulder.

**4. Moments and high-redundancy limit.** Direct integration gives \(\mathbb ED=q/3\) and \(\operatorname{Var}(D)=1/(45q^2)\); also \(\mathbb E(1-\cos\Theta)=1\) and \(\mathbb E(1-\cos\Theta)^2=3/2\). Expanding \(\Lambda^2\) proves the two displayed moment identities. Uniformly in \(U\), \(D/q\to1/3\). Hence \(\Lambda/q\) converges in distribution to \((2+\cos\Theta)/3\), the asserted arcsine law.

## Verification

The bundled standard-library script `verify.py` reconstructs all overlap coefficients with rational arithmetic for multiple integer redundancies and positions, checks the exact Zak scalar formula, and numerically integrates the two-branch density with square-root endpoint substitutions. Its calculations test normalization, both moments and sample spectral edges. The extracted script was executed successfully; these finite checks are corroborative and do not replace the all-integer proof above.

## Relationship to prior work

The literature on the second-order \(B\)-spline includes Atindehou--Frederick--Kouagou--Okoudjou (2018), who identify frame-set regions and dual windows; Ghosh--Selvan (2023), who investigate frame regions and obstructions; and Buck--Frederick--Okoudjou--Stangl (2026), who study Gram-matrix blocks and **already establish the upper bound \(q\) at the integer-oversampled parameters**. These precedents do not state the full Zak-fiber probability density, its interior spectral shoulder, or the complete sharp lower-edge/moment/arcsine description given here in the inspected material. Hasannasab--Lemvig (September 2026) subsequently characterize the integer-oversampled *frame property*; its complete manuscript was not accessible for a conclusive theorem-by-theorem comparison, so indirect earlier coverage of the density remains a historical-priority risk. The general Zak diagonalization itself is classical and is not claimed as new. The contribution is the exact probability law and the combined structural spectral consequences for this concrete non-painless Gabor regime.

## Limitations

The law concerns the centered hat \(B\)-spline and the rectangular lattice with integer modulation step \(1\) and translation step \(q^{-1}\), for integers \(q\ge2\). It is not a characterization of all \(B\)-spline Gabor frame regions, and no statement is made for noninteger time oversampling, other modulation steps, or general windows. The fiber measure is a normalized distribution, not a trace-class spectral measure on the infinite-dimensional operator. The standard Zak transform is foundational background. The originality comparison is based on the accessible inspected material; the complete September 2026 integer-oversampling paper was inaccessible, and more general published spectral results could conceivably subsume this specialized law. No independent mathematical audit was performed.

## References

1. A. G. D. Atindehou, C. Frederick, Y. B. Kouagou and K. A. Okoudjou, *On the frame set of the second-order B-spline*, arXiv:1806.05614 (first posted 14 June 2018).
2. A. Ghosh and E. Selvan, *On Gabor frames generated by B-splines, totally positive functions, and Hermite functions*, arXiv:2304.11322 (first posted 22 April 2023).
3. A. Ghosh and E. Selvan, *Obstructions for Gabor frames of the second order B-spline*, arXiv:2310.01141 (first posted 2 October 2023).
4. C. Buck, C. Frederick, K. A. Okoudjou and J. Stangl, *On the structure of the Gram matrix for Gabor systems generated by B-splines*, arXiv:2603.16986 (2026), especially its integer-oversampling upper-bound calculation.
5. M. Hasannasab and J. Lemvig, *The zero set of the Zak transform of B-splines with applications to Gabor frames*, arXiv:2609.13116 (first posted 11 September 2026; abstract and metadata accessible).
