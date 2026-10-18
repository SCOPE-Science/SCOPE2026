# Sharp symmetry breaking in the first residual-minimizing Lyapunov ADI shift

## Finding

For a stable symmetric Lyapunov equation with exactly two active eigenvalues and equal forcing energy in their eigenspaces, the real shift minimizing the first low-rank alternating-direction implicit (ADI) residual undergoes a sharp symmetry-breaking bifurcation at spectral condition number \(7+4\sqrt{3}\). Below and at this threshold, the unique optimal shift is the geometric mean of the two eigenvalues. Above it, that geometric mean becomes a strict local **maximum** of the residual, and precisely two reciprocal global minimizers replace it. The geometric-mean minimax shift can cost almost twice the optimal first-step residual, with sharp supremum \(2\).

## Assumptions and scope

Let \(H\) be any real symmetric positive-definite matrix with exactly two distinct eigenvalues \(0<a<b\), and let \(P_a,P_b\) be their orthogonal spectral projectors. Let \(u\ne0\) satisfy \(\|P_a u\|^2=\|P_b u\|^2=\sigma^2>0\). Consider the unique symmetric solution of \(HX+XH=uu^{\mathsf T}\) and start low-rank ADI with \(X_0=0\). For one real ADI shift \(-p\), where \(p>0\), the standard one-step approximation and residual are
\[
X_1(p)=2p(H+pI)^{-1}uu^{\mathsf T}(H+pI)^{-1},\qquad
R_1(p)=uu^{\mathsf T}-HX_1(p)-X_1(p)H.
\]
The optimization objective is the actual Frobenius residual norm \(\|R_1(p)\|_F\), not the norm of a solution error, the norm squared, or a worst-spectral-factor surrogate. Eigenspace multiplicities are unrestricted. All claims use exact arithmetic and concern the first step only.

Write \(\kappa=b/a>1\), \(g=\sqrt{ab}\), and \(c=(\sqrt b-\sqrt a)/(\sqrt b+\sqrt a)\). Then \(0<c<1\). If \(\kappa\le7+4\sqrt3\), the global optimizer is uniquely \(p=g\), with minimum residual \(2\sigma^2c^2\). At equality the minimum is quartically flat in the natural Cayley coordinate.

If \(\kappa>7+4\sqrt3\), define
\[
w_* = \frac{3c^2-1}{c^2(3-c^2)},\qquad
p_{\pm}=g\frac{1\pm\sqrt{w_*}}{1\mp\sqrt{w_*}}.
\]
Then \(0<w_*<1\) and \(p_-p_+=ab\). These are exactly the two global minimizing shifts, with minimum residual
\[
\|R_1(p_\pm)\|_F=\sigma^2\frac{6c^2-c^4-1}{4c^2}.
\]
The geometric mean is then a strict local maximum of residual. Its excess factor compared with the optimum is
\[
\frac{\|R_1(g)\|_F}{\min_{p>0}\|R_1(p)\|_F}
=\frac{8c^4}{6c^2-c^4-1},
\]
which increases strictly with \(\kappa>7+4\sqrt3\) and approaches the sharp unattained value \(2\) as \(\kappa\to\infty\).

## Proof

**Residual factorization.** Put \(V=(H+pI)^{-1}u\). Direct multiplication gives
\[
R_1=uu^{\mathsf T}-2p(HVV^{\mathsf T}+VV^{\mathsf T}H)
=ww^{\mathsf T},\quad
w=u-2pV=(H-pI)(H+pI)^{-1}u.
\]
Because a real rank-one outer product has Frobenius norm \(\|ww^{\mathsf T}\|_F=\|w\|^2\), the balanced eigenspace masses imply the **exact** scalar identity
\[
\frac{\|R_1(p)\|_F}{\sigma^2}=f(p)
=\left(\frac{a-p}{a+p}\right)^2+\left(\frac{b-p}{b+p}\right)^2.
\]

**Cayley reduction.** Use the one-to-one change of coordinates \(z=(p-g)/(p+g)\in(-1,1)\) and \(w=z^2\in[0,1)\). The spectral fractions become \(-(c+z)/(1+cz)\) and \((c-z)/(1-cz)\), up to interchange, so
\[
f(p)=2\frac{c^2+(1-4c^2+c^4)w+c^2w^2}{(1-c^2w)^2}.
\]
For \(0\le w<1\), the denominator is strictly positive. Exact differentiation yields
\[
\frac{df}{dw}=\frac{2(1-c^2)\bigl[(1-3c^2)+c^2(3-c^2)w\bigr]}{(1-c^2w)^3}.
\]
Its sign is the sign of the displayed affine expression in \(w\). If \(c^2<1/3\), it is positive for every admissible \(w\), so the unique minimum is \(w=0\), namely \(p=g\). At \(c^2=1/3\), the derivative vanishes only at \(w=0\) and is positive at every \(w>0\), again giving a unique minimum. At equality, expansion about \(z=0\) yields \(f=2/3+(16/27)z^4+O(z^6)\).

If \(c^2>1/3\), the derivative is negative from \(w=0\) until the unique root \(w_*=(3c^2-1)/[c^2(3-c^2)]\), and positive thereafter. The root is in \((0,1)\), since \(c^4<1\). Consequently the two values \(z=\pm\sqrt{w_*}\) are precisely the global minimizers in \((-1,1)\), and \(z=0\) is a strict local maximum. Substitution gives the asserted minimum. Since \(c^2=1/3\) is equivalent to \(\sqrt\kappa=2+\sqrt3\), the bifurcation occurs at \(\kappa=7+4\sqrt3\).

**Sharp loss of geometric-mean shift.** Let \(x=c^2\in(1/3,1)\). The ratio is \(8x^2/(6x-x^2-1)\) and its derivative in \(x\) is \(16x(3x-1)/(6x-x^2-1)^2>0\). The ratio tends to \(1\) as \(x\downarrow1/3\), and to \(2\) as \(x\uparrow1\); neither endpoint of \(x\in(1/3,1)\) is included.

**Why spectral minimax differs.** The surrogate \(\max\{|(a-p)/(a+p)|, |(b-p)/(b+p)|\}\) is uniquely minimized by balancing its two factors, at \(p=g\), for every \(a<b\). The actual balanced rank-one residual instead **adds the squared factors**. The minimax solution can therefore be a strict local maximum of the actual data-dependent residual in the high-contrast regime.

**Exact witness.** Let \(a=1\), \(b=49\), and \(\sigma^2=1\). Then \(g=7\), \(c^2=9/16\), and \(w_*=176/351\). The exact optimal residual norm is \(527/576\), attained only at \(p_\pm=7(1\pm\sqrt{176/351})/(1\mp\sqrt{176/351})\). The geometric-mean shift gives \(9/8=648/576\), hence an exact excess factor \(648/527\).

## Verification

Run \(\texttt{python verify.py}\) using Python's standard library. The accompanying script checks ADI residual identities and Cayley algebra in rational arithmetic, probes both parameter regimes and the exact witness, and compares the scalar formulas against grids of positive shifts. The verifier reports 3,722 successful exact-rational and numerical checks. Finite computations are corroboration; the preceding derivative sign analysis proves the universal optimization and uniqueness statements.

## Relationship to prior work

Classical low-rank ADI, its Cayley residual factorization, and data-dependent residual-minimizing shift selection are established methods, not claimed innovations. Schulze and Saak's 2024 ADI framework motivates the solver. Kürschner's 2018 paper supplies a general residual-minimizing shift objective, which includes the two-eigenvalue problem here, but its general objective does not itself give the explicit balanced-spectrum global optimization or symmetry-breaking threshold. Benner, Kürschner and Saak's 2014 work contrasts spectral shift selection with residual-aware alternatives. The additional result proved here is the exact two-mode bifurcation, global minimizer classification, and sharp factor-two geometric-mean loss for the actual Frobenius residual.

## Limitations

The theorem assumes real symmetry, two distinct spectral values, equal nonzero spectral forcing masses, rank-one right-hand side, a real negative ADI shift, and one step. It does not characterize complex shifts, unbalanced forcing weights, three or more active spectral values, or multistep residual optimization. The 2024 motivating framework is not presented as new, nor is the general residual-minimization objective. The mathematical-record and source comparisons cannot exclude a mathematically equivalent result in unindexed or inaccessible literature. Independent scientific audit has not been performed.

## References

1. J. Schulze and J. Saak, *A unifying framework for ADI-like methods for linear matrix equations and beneficial consequences* (first public version 2024-06-19), arXiv:2406.13477, https://arxiv.org/abs/2406.13477.
2. P. Kürschner, *Residual minimizing shift parameters for the low-rank ADI iteration* (2018), arXiv:1811.05500, https://arxiv.org/abs/1811.05500.
3. P. Benner, P. Kürschner and J. Saak, *Self-generating and efficient shift parameters in ADI methods for large Lyapunov and Sylvester equations*, Electronic Transactions on Numerical Analysis, 43 (2014–2015), 142–162, https://etna.ricam.oeaw.ac.at/vol.43.2014-2015/pp142-162.dir/pp142-162.pdf.
