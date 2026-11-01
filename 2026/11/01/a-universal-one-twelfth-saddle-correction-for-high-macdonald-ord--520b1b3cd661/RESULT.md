# A universal one-twelfth saddle correction for high Macdonald order derivatives

## Finding

For each fixed real \(x>0\), let \(N\) tend to infinity through positive even integers and define the order derivative
\[
D_N(x)=\left.\frac{\partial^N}{\partial\nu^N}K_\nu(x)\right|_{\nu=0}.
\]
There is exactly one positive \(t_N\) satisfying \(x t_N\sinh t_N=N\). Put
\[
\Phi_N(t)=N\log t-x\cosh t,\quad
B_N=\frac N{t_N^2}+x\cosh t_N,
\quad G_N=\sqrt{\frac{2\pi}{B_N}}\,e^{\Phi_N(t_N)}.
\]
With the explicit dimensionless correction
\[
Q_N=\frac{-6N/t_N^4-x\cosh t_N}{8B_N^2}
+\frac{5(2N/t_N^3-x\sinh t_N)^2}{24B_N^3},
\]
one has the **two-term saddle expansion with a controlled relative remainder**
\[
\boxed{D_N(x)=G_N\left[1+Q_N+O_x\!\left(\frac{t_N^2}{N^2}\right)\right].}
\]
In particular the first deviation from the Gaussian saddle is eventually positive and has the universal, nonzero limit
\[
\boxed{\lim_{\substack{N\to\infty\\N\ \mathrm{even}}}
\frac{N}{t_N}\left(\frac{D_N(x)}{G_N}-1\right)=\frac1{12}.}
\]
The saddle satisfies \(t_N\sim W(2N/x)\sim\log N\), where \(W\) is the positive Lambert function. Thus the relative error after the explicit \(Q_N\) correction is \(O_x((\log N)^2/N^2)\), and the normalized Gaussian-only error has exact leading scale \((\log N)/(12N)\).

## Assumptions and scope

The argument \(x\) is a fixed positive real number; the derivative index \(N\) is even and tends to infinity. The derivatives are with respect to the **order** \(\nu\), not the argument \(x\). Constants in big-O notation may depend on \(x\), not on \(N\). Neither complex arguments nor a regime where \(x\) moves with \(N\) is asserted. The odd derivatives at \(\nu=0\) vanish by parity and are not covered by the nonzero relative asymptotic formula.

## Proof

**Step 1: integral and unique saddle.** The classical Macdonald representation for \(x>0\) is
\[
K_\nu(x)=\frac12\int_{-\infty}^{\infty}e^{\nu t-x\cosh t}\,dt.
\]
For each fixed integer \(N\), differentiation under this integral is justified by superexponential decay. At \(\nu=0\) and even \(N\), symmetry gives the exact identity
\[
D_N(x)=\int_0^\infty t^N e^{-x\cosh t}\,dt
=\int_0^\infty e^{\Phi_N(t)}\,dt.
\]
The phase is strictly concave on \((0,\infty)\), since
\(\Phi_N''(t)=-N/t^2-x\cosh t<0\). Its derivative tends to \(+\infty\) at zero and to \(-\infty\) at infinity. Hence it has exactly one maximizing saddle \(t_N\), determined by \(x t_N\sinh t_N=N\). Its curvature is \(-B_N\).

**Step 2: growth and saddle-scale derivatives.** The saddle equation yields \(t_N\to\infty\) and
\[
\frac{2N}{x}=t_N e^{t_N}(1-e^{-2t_N}),\qquad
\frac{B_Nt_N}{N}=\frac1{t_N}+\coth t_N\longrightarrow1.
\]
Consequently \(t_N\sim W(2N/x)\sim\log N\) and \(B_N\asymp_x N/t_N\to\infty\). Write \(\epsilon_N=B_N^{-1/2}\), which is asymptotic to \(\sqrt{t_N/N}\). For every fixed \(j\ge3\), direct differentiation gives
\[
\Phi_N^{(j)}(t)=(-1)^{j-1}(j-1)!\,\frac N{t^j}
-x\begin{cases}\sinh t,&j\text{ odd},\\\cosh t,&j\text{ even}.
\end{cases}
\]
At the saddle (and on a fixed-width neighborhood), \(\Phi_N^{(j)}=O_{x,j}(B_N)\), hence the standardized derivatives
\(a_{j,N}=\Phi_N^{(j)}(t_N)B_N^{-j/2}\) satisfy
\(a_{j,N}=O_{x,j}(\epsilon_N^{j-2})\) for all fixed \(j\ge3\).

**Step 3: Gaussian localization, including tails.** Set \(u=\sqrt{B_N}(t-t_N)\). On \(|t-t_N|\le1\), the saddle equation and comparison of \(\sinh\) and \(\cosh\) on this interval give \(-\Phi_N''(t)\ge c_x B_N\) for all sufficiently large \(N\), with \(c_x>0\). For \(t\le t_N-1\) and \(t\ge t_N+1\), strict concavity and the resulting one-sided slope bounds, together with \(\Phi_N(t)\to-\infty\) at both ends, bound the corresponding integrals by \(e^{\Phi_N(t_N)}O_x(e^{-c_xB_N})\) times a polynomial factor in \(N\). On the intermediate region \(|u|>\epsilon_N^{-1/8}\), the local curvature bound gives a Gaussian tail \(O(e^{-c_x\epsilon_N^{-1/4}})\) relative to \(G_N\). Both contributions are smaller than any fixed power of \(\epsilon_N\). This justifies extending local Gaussian integrals to the entire real line and controls the far tails, not merely pointwise Taylor series.

**Step 4: two-term expansion and odd cancellation.** For \(|u|\le\epsilon_N^{-1/8}\), Taylor's formula at \(t_N\), with the bounds from Step 2 valid throughout the local region, gives
\[
\Phi_N(t_N+u/\sqrt{B_N})-\Phi_N(t_N)
=-\frac{u^2}{2}+\frac{a_{3,N}u^3}{6}
+\frac{a_{4,N}u^4}{24}
+\frac{a_{5,N}u^5}{120}+O_x(\epsilon_N^4|u|^6).
\]
Expanding the exponential in weighted Gaussian \(L^1\) and retaining terms through order \(\epsilon_N^3\) leaves
\[
1+\frac{a_{3,N}u^3}{6}+\frac{a_{4,N}u^4}{24}
+\frac{a_{3,N}^2u^6}{72}+
\underbrace{\left(\frac{a_{5,N}u^5}{120}
+\frac{a_{3,N}a_{4,N}u^7}{144}
+\frac{a_{3,N}^3u^9}{1296}\right)}_{\text{odd in }u}
+O_{L^1(e^{-u^2/2}du)}(\epsilon_N^4).
\]
All odd terms integrate to zero. The standard Gaussian fourth and sixth moments are \(3\) and \(15\), respectively, so
\[
\frac{D_N(x)}{G_N}
=1+\frac{a_{4,N}}8+\frac{5a_{3,N}^2}{24}
+O_x(\epsilon_N^4)
=1+Q_N+O_x(B_N^{-2}).
\]
Because \(B_N^{-2}=O_x(t_N^2/N^2)\), this is the claimed controlled remainder. The Gaussian localization proof justifies the integrated order symbol and does not rely on finite numerical sampling.

**Step 5: exact limiting coefficient.** From \(x\sinh t_N=N/t_N\) and \(\coth t_N\to1\),
\[
\frac{\Phi_N'''(t_N)}{B_N}\to-1,
\qquad\frac{\Phi_N''''(t_N)}{B_N}\to-1,
\qquad\frac{N}{B_Nt_N}\to1.
\]
Thus
\[
\frac{N}{t_N}Q_N
\longrightarrow-\frac18+\frac5{24}=\frac1{12},
\]
while \(\frac{N}{t_N}O_x(B_N^{-2})\to0\). This proves the universal constant and completes the argument.

## Verification

A finite-sample numerical diagnostic in `check_saddle.py` solves the saddle equation, integrates the *centered* phase on the Gaussian coordinate, and compares the measured ratio to \(1+Q_N\). It uses \(x\in\{1/4,1,3,10\}\) and \(N\in\{60,200,600\}\). For those twelve pairs, the residual multiplied by \((N/t_N)^2\) lies between approximately \(-0.0191\) and \(-0.0052\), consistent with the remainder scaling. Run with `python check_saddle.py` after installing `scipy` and `numpy`. This diagnostic does not prove the asymptotic result; the proof is Steps 1–5 above.

## Relationship to prior work

González Santander, Harrington and Melino (arXiv:2610.31368v1, publicly posted 2026-10-22) supply a general exact integral representation for arbitrary order-derivative index, including the Macdonald kernel (their Eq. 71), and numerical calculations up to order 1000. The inspected paper does not give an \(N\to\infty\) saddle expansion or the \(1/12\) correction. Dunster (arXiv:1502.05971v1) treats derivatives of fixed differentiation order with **large Bessel order**, a different asymptotic parameter. Paris (arXiv:1905.04673v1) treats large differentiation index **with respect to the Bessel argument**, not the Bessel order. González-Santander's 2022 open-access reflection-formula paper treats identities for order derivatives, not this high-index asymptotic. Ryavec (arXiv:2105.00869) gives formulas for order derivatives at one-half, without the present large-index saddle law. General Laplace's method underlies the proof; no exclusive claim to that standard technique is made.

## Limitations

The formula is pointwise in a fixed real \(x>0\), not uniform over \(x\) approaching zero or infinity as \(N\to\infty\). The \(1/12\) coefficient is a large-index limit and need not determine the sign of the finite-index correction \(Q_N\). No full all-orders asymptotic expansion or independently audited certification is asserted. Unindexed classical saddle literature could in principle contain an equivalent expansion and merits later independent priority review.

## References

1. J. L. González Santander, D. A. Harrington, A. Melino, *Integral representations of high-order derivatives of Bessel functions with respect to the order*, arXiv:2610.31368v1 (2026-10-22), especially Theorem 16, Eq. 71, and Sections 3–4. https://arxiv.org/html/2610.31368v1
2. T. M. Dunster, *On the order derivatives of Bessel functions*, arXiv:1502.05971 (2015). https://arxiv.org/abs/1502.05971
3. R. B. Paris, *High-order derivatives of the Bessel functions with an application*, arXiv:1905.04673 (2019), especially Section 2. https://arxiv.org/html/1905.04673v1
4. J. L. González-Santander, *Reflection Formulas for Order Derivatives of Bessel Functions*, Results in Mathematics 78 (2023), article 30. https://doi.org/10.1007/s00025-022-01804-3
5. C. Ryavec, *BesselK Derivatives with respect to Order at one half*, arXiv:2105.00869 (2021). https://arxiv.org/abs/2105.00869
