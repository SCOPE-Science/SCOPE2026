# Exponential Mahler growth along the cube–cross-polytope Minkowski interpolation

## Finding

Let \(d\ge2\), let \(C_d=[-1,1]^d\), let \(O_d=\{x\in\mathbb R^d:\sum_{i=1}^d|x_i|\le1\}\), and set \(K_{d,t}=C_d+tO_d\) for \(t\ge0\). Write \(\mathcal P(K)=\operatorname{vol}_d(K)\operatorname{vol}_d(K^\circ)\), and normalize by the common cube/cross-polytope value \(4^d/d!\). Then the exact profile is
\[
R_d(t):=\frac{\mathcal P(K_{d,t})}{4^d/d!}
=\frac{d!\sum_{k=0}^d\binom dk\,t^k/k!}{\prod_{j=1}^d(t+j)}.
\]
For each \(d\ge2\), a finite global maximizing parameter \(t_d>0\) exists. For **any** selection of global maximizers, as \(d\to\infty\),
\[
\frac{t_d}{d}\longrightarrow s_*,\qquad
\frac1d\log\max_{t\ge0}R_d(t)\longrightarrow\gamma_*.
\]
Here \(y_*\) is the unique root greater than \(1\) of
\[
y=\log(1+y+y^2),
\]
and
\[
s_*:=\frac{1}{y_*(1+y_*)}=0.199634949883067661\ldots,
\quad \gamma_*=0.261152459394093055\ldots.
\]
In particular, the maximum normalized Mahler product along this interpolation is
\[
\max_{t\ge0}R_d(t)
=\exp\bigl((\gamma_*+o(1))d\bigr)
=(1.298425607525639\ldots)^{d+o(d)}.
\]
This does **not** assert uniqueness of maximizing parameters for a fixed finite dimension, nor optimality outside this one-parameter family.

## Assumptions and scope

Volumes are ordinary Euclidean \(d\)-dimensional Lebesgue volumes. Polarity \(K^\circ\) is with respect to the origin and the standard Euclidean pairing. All claims concern the **Minkowski sum** of the full unit cube and a nonnegative dilate of the unit cross-polytope, not their intersection or their convex hull. Dimensions are integers \(d\ge2\), parameters \(t\ge0\), and asymptotic limits take \(d\to\infty\) through integers. The definition of \(\gamma_*\) is the explicit variational value evaluated in the proof.

## Proof

**1. Exact volume identities.** A point \(x\in\mathbb R^d\) belongs to \(K_{d,t}\) precisely when its \(\ell_1\)-distance to the cube is at most \(t\), namely
\[
\sum_{i=1}^d(|x_i|-1)_+\le t.
\]
Fixing an orthant and selecting the \(k\) coordinates that exceed \(1\), the excesses fill a positive \(k\)-simplex of volume \(t^k/k!\); the other coordinates independently range over unit intervals. Summing subsets and orthants gives
\[
\operatorname{vol}_d(K_{d,t})=2^d\sum_{k=0}^d\binom dk\frac{t^k}{k!}.
\]
The support function of \(C_d+tO_d\) equals \(\|y\|_1+t\|y\|_\infty\). Thus
\[
K_{d,t}^\circ=\{y:\|y\|_1+t\|y\|_\infty\le1\}.
\]
In any nonnegative coordinate-order chamber, write ordered coordinates as \(y_i=\sum_{j=i}^d z_j\), with \(z_j\ge0\). This triangular change of variables has unit determinant, and the polar inequality becomes \(\sum_{j=1}^d(j+t)z_j\le1\). Its volume is \(1/(d!\prod_{j=1}^d(j+t))\). There are \(2^d d!\) congruent signed chambers, so
\[
\operatorname{vol}_d(K_{d,t}^\circ)=\frac{2^d}{\prod_{j=1}^d(t+j)}.
\]
Multiplication proves the exact profile.

**2. Existence at finite dimension.** The exact expression is continuous, \(R_d(0)=1\), and its leading coefficients give \(\lim_{t\to\infty}R_d(t)=1\). Direct logarithmic differentiation at zero yields
\[
R_d'(0)=d-\sum_{j=1}^d\frac1j>0\qquad(d\ge2).
\]
Consequently \(R_d\) attains a maximum strictly above \(1\) at a positive finite parameter.

**3. Localized large-dimensional exponential rate.** Put \(t=ds\), with fixed \(s>0\), and let \(\rho=k/d\). The uniform factorial estimates \(\log(m!)=m\log m-m+O(\log(d+1))\) for \(0\le m\le d\), together with the at most \(d+1\) positive summands, give
\[
\frac1d\log\left(\sum_{k=0}^d\binom dk\frac{(ds)^k}{k!}\right)
\longrightarrow \max_{0\le\rho\le1}
\left[-\rho\log\rho-(1-\rho)\log(1-\rho)
+\rho\log\frac{s}{\rho}+\rho\right].
\]
Here the continuous endpoint convention is \(0\log0=0\). Strict concavity gives a unique saddle \(\rho_s\in(0,1)\) satisfying
\[
\rho_s^2=s(1-\rho_s),\qquad
\rho_s=\frac{\sqrt{s^2+4s}-s}{2}.
\]
The maximum simplifies, using the saddle identity, to \(\rho_s-\log(1-\rho_s)\). On the denominator side, Stirling's formula and a Riemann sum yield
\[
\frac1d\log\frac{d!}{\prod_{j=1}^d(ds+j)}
\longrightarrow -1-\int_0^1\log(s+x)\,dx.
\]
Therefore
\[
\Psi(s):=\lim_{d\to\infty}\frac1d\log R_d(ds)
=\rho_s-\log(1-\rho_s)
-(1+s)\log(1+s)+s\log s.
\]
The preceding factorial and Riemann-sum estimates are **uniform** when \(s\) ranges over any compact subset of \((0,\infty)\): the discrete saddle functions are uniformly continuous there, the error in each log-summand is \(O(\log(d+1)/d)\), and the log-sum differs from its largest term by at most \(\log(d+1)/d\).

**4. Unique maximizing exponential scale.** Differentiation via the saddle-point envelope theorem gives
\[
\Psi'(s)=\frac{\rho_s}{s}-\log\left(\frac{1+s}{s}\right).
\]
Put \(y=(1-\rho_s)/\rho_s\). Then \(s=1/[y(1+y)]\), and
\[
\Psi'(s)=h(y),\qquad h(y)=y-\log(1+y+y^2),\qquad
h'(y)=\frac{y(y-1)}{1+y+y^2}.
\]
The function \(h\) vanishes at zero, decreases strictly on \((0,1)\), and increases strictly on \((1,\infty)\). Since \(h(1)=1-\log3<0\) and \(h(y)\to\infty\), it has exactly one positive zero \(y_*>1\). Because \(y\) decreases as \(s\) increases, \(\Psi\) first increases and then decreases, with unique maximum at \(s_*\). Its endpoint limits are \(\Psi(0+)=\Psi(+\infty)=0\), whereas \(\gamma_*:=\Psi(s_*)>0\). The numerical values displayed above are evaluations of these explicit equations, not substitutes for the uniqueness proof.

**5. Escape of finite-dimensional maximizers is impossible.** Two global bounds ensure that optimization commutes with the large-dimensional limit. First, \(\prod_{j=1}^d(t+j)\ge d!\), \(\binom dk\le d^k/k!\), and \(\sum_{k\ge0}z^{2k}/(k!)^2\le e^{2z}\), hence
\[
R_d(t)\le e^{2\sqrt{dt}}.
\]
Therefore \(t_d/d\to0\) would imply \(d^{-1}\log R_d(t_d)\to0\). Second, after reversing summation indices, \(d!\binom dj/(d-j)!\le d^{2j}/j!\), and \(\prod_{j=1}^d(t+j)\ge t^d\), hence for \(t>0\)
\[
R_d(t)\le\sum_{j=0}^d\frac{(d^2/t)^j}{j!}\le e^{d^2/t}.
\]
Thus \(t_d/d\to\infty\) also forces zero exponential rate. Both contradict \(R_d(t_d)\ge R_d(ds_*)\) and the positive limit \(\gamma_*\). The ratios \(t_d/d\) therefore remain in a compact subset of \((0,\infty)\). Uniform convergence there and uniqueness of the maximizer of \(\Psi\) force every subsequential limit to be \(s_*\). This proves both asserted global limits.

## Verification

`verify.py` uses only the Python standard library. Run `python verify.py` from the package directory. It checks the exact volume formula against independent published low-dimensional cube–cross-polytope data for dimensions \(2,3,4,5\), performs exact-rational profile evaluations in dimensions \(2\) through \(18\), checks the saddle constant and strict rate comparisons, and compares finite-dimensional logarithmic ratios to the limiting exponent at dimensions \(100,300,1000,3000\). It prints `VERIFY_OK 203` on success. These finite computations diagnose numerical and normalization mistakes; **the infinite-dimensional asymptotic and global-maximizer theorem rests on the five analytical steps above**.

## Relationship to prior work

The initiating work of Kim and Zvavitch (2013) proves stability properties for the reverse Blaschke–Santaló inequality on unconditional bodies but does not optimize this particular Minkowski interpolation as dimension grows. Fisikopoulos (2013, slide 33 of the cited deck) lists exact volumes of the cube-plus-cross-polytope at parameter \(1\) in dimensions \(2\) through \(5\) and explicitly identifies polar-volume/Mahler computations as further work. Hence the low-dimensional **primal volumes are not asserted to be new**.

A publicly available 2026 research record evaluates a polar-equivalent five-dimensional family \(\{x:\|x\|_\infty+\tau\|x\|_1\le1\}\), its small-\(\tau\) derivative, and four finite-parameter values. For \(t>0\) that family is linearly scaled from \(K_{d,t}^\circ\) when \(\tau=1/t\). Its exact five-dimensional calculations are **acknowledged as prior coverage**, and no novelty is claimed for those specializations. Neither the inspected finite-dimensional result nor the 2013 primary works supplies the present **unique growing-dimensional maximizing scale, global localization, or exponential growth exponent**. A later general volume-product survey gives local minima and stability background, not this parameterized asymptotic. This is an implication comparison, not an inference of novelty from an unsuccessful search alone.

## Limitations

The theorem does not prove uniqueness of a finite-dimensional maximizer, any quantitative convergence rate for \(t_d/d\), or an upper bound for Mahler products of convex bodies outside this one-parameter family. It is not a proof of Mahler's conjecture. Classical Laguerre asymptotic literature might contain an equivalent scalar optimization after a change of variables; exhaustive historical priority verification has not been performed. Numerical computations cannot independently certify the universal theorem.

## References

1. J. Kim and A. Zvavitch, *Stability of the reverse Blaschke–Santaló inequality for unconditional convex bodies*, arXiv:1302.5719v1, publicly posted 22 February 2013. https://arxiv.org/abs/1302.5719
2. V. Fisikopoulos, *Algorithms for high-dimensional polytopes defined by oracles*, presentation dated 22 February 2013, particularly slide 33 and the stated future-work item on polar duals/Mahler volume. https://vissarion.github.io/talks/GeomCompAthens13_slides.pdf
3. M. Fradelizi, M. Meyer, and A. Zvavitch, *Volume Product*, arXiv:2301.06131v1 (2023), Section 3 on known minimizers and stability. https://arxiv.org/abs/2301.06131
4. *Transverse slope-10 Mahler-product growth along the canonical 5D unconditional ray*, public mathematical record (2026). https://github.com/published-finding corpus/2026/blob/main/2026/9/9/SCOPE077/RESULT.md
