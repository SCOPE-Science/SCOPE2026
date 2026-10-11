# Exact mixed-exponent numerical ranges of three-site weighted shifts on \(\ell_p\)

## Finding
For every \(1<p<\infty\), put \(q=p/(p-1)\) and
\[
h_p=\frac{(p-1)^{(p-1)/p}}{p}.
\]
Let \(a,b\in\mathbb C\) and define \(T_{a,b}:\ell_p^3(\mathbb C)\to\ell_p^3(\mathbb C)\) by
\[
T_{a,b}(x_1,x_2,x_3)=(a x_2,b x_3,0).
\]
Set \(\alpha=|a|\), \(\beta=|b|\), and, when \(\alpha+\beta>0\), let \(R_p(\alpha,\beta)\) be the **unique positive number** satisfying
\[
\left(\frac{\alpha}{R_p(\alpha,\beta)}\right)^p+
\left(\frac{\beta}{R_p(\alpha,\beta)}\right)^q=1.
\]
Define \(R_p(0,0)=0\). The entire spatial numerical range is the closed disk
\[
\boxed{W_p(T_{a,b})=\{z\in\mathbb C:|z|\le h_p R_p(\alpha,\beta)\}.}
\]
In particular, its numerical radius is \(w_p(T_{a,b})=h_p R_p(\alpha,\beta)\). For \(\alpha\beta>0\), every maximizing unit vector has the same coordinate moduli:
\[
(|x_1|,|x_2|,|x_3|)=
\frac{(r,1,s)}{(1+r^p+s^p)^{1/p}},\qquad
r=\frac{(p-1)\alpha}{p\,w_p(T_{a,b})},\qquad
s=\left(\frac{\beta}{p\,w_p(T_{a,b})}\right)^{1/(p-1)}.
\]
The phases of a maximizing vector are precisely those for which the two nonzero terms in the duality pairing have the same argument. This also characterizes all maximizers.

The law has the exact duality symmetry
\[
\boxed{w_p(T_{a,b})=w_q(T_{b,a}).}
\]
In contrast, reversing the weights at **fixed** non-Hilbert exponent need not preserve the radius. At \(p=4\), the two radii for weights \((8,1)\) and \((1,8)\) satisfy
\[
\boxed{w_4(T_{8,1})>w_4(T_{1,8}).}
\]
For \(p=2\), the formula specializes to the familiar \(w_2(T_{a,b})=\sqrt{|a|^2+|b|^2}/2\).

## Assumptions and scope
The scalar field is complex, \(1<p<\infty\), and both weights may be arbitrary complex numbers (including zero). The **spatial** numerical range of a bounded operator on a smooth Banach space is
\[
W_p(T)=\{J_p(x)(Tx):\|x\|_p=1\},\qquad
J_p(x)(y)=\sum_{j=1}^3\overline{x_j}|x_j|^{p-2}y_j,
\]
where a zero coordinate contributes zero. The normalized duality functional \(J_p(x)\) is the unique norm-one functional satisfying \(J_p(x)(x)=1\). This is not the algebraic numerical range, nor the Hilbert-space \(q\)-numerical range parameterized by an inner-product constraint. Only three-site nilpotent shifts are classified; no formula for longer chains or other matrices is asserted.

## Proof
**1. Reduction to nonnegative moduli.** For \(\|x\|_p=1\), the duality pairing is
\[
J_p(x)(T_{a,b}x)=a\overline{x_1}|x_1|^{p-2}x_2+b\overline{x_2}|x_2|^{p-2}x_3.
\]
Its absolute value is at most
\[
F(u,v,z)=\alpha u^{p-1}v+\beta v^{p-1}z,
\qquad u,v,z\ge0,\quad u^p+v^p+z^p=1.
\]
Conversely, the phases of the three coordinates can always be selected so that both summands have one common argument, because the phase constraints form a path with no cycle. Thus the maximum of \(F\) is exactly \(w_p(T_{a,b})\).

**2. Boundary cases and positivity.** If \(\alpha=\beta=0\), the assertion is immediate. If exactly one weight is nonzero, the problem is the two-coordinate maximization \(\max\{\gamma u^{p-1}v:u^p+v^p=1\}\), whose value is \(h_p\gamma\) by Hölder or a single derivative. The defining equation gives \(R_p=\gamma\) in this case.

Now suppose \(\alpha,\beta>0\). Every global maximizer of \(F\) has \(u,v,z>0\). Indeed, \(v=0\) makes \(F=0\), which is not optimal. If \(u=0\) but \(v,z>0\), adding an \(\varepsilon>0\) first coordinate before renormalization gains the positive term \(\alpha\varepsilon^{p-1}v\), while normalization changes the old value by order \(\varepsilon^p\); since \(p>1\), the gain is dominant. If \(z=0\) but \(u,v>0\), adding \(\varepsilon>0\) in the third coordinate gains \(\beta v^{p-1}\varepsilon\), dominating the normalization loss of order \(\varepsilon^p\). Remaining corner cases have value zero.

**3. Stationary equations and the mixed-exponent law.** Compactness gives a maximizer, and by the preceding step it is interior. Let \(\lambda>0\) be its Lagrange multiplier for \(u^p+v^p+z^p=1\). Since \(F\) and the constraint are homogeneous of degree \(p\), Euler's identity gives \(\lambda=F(u,v,z)=w_p(T_{a,b})\). Put \(r=u/v\), \(s=z/v\). The derivatives in the first, second, and third coordinates give, respectively,
\[
p\lambda=\frac{(p-1)\alpha}{r},\qquad
p\lambda=\alpha r^{p-1}+(p-1)\beta s,\qquad
p\lambda=\frac{\beta}{s^{p-1}}.
\]
Eliminating \(\alpha\) and \(\beta\) from the middle equation yields
\[
\frac{r^p}{p-1}+(p-1)s^p=1.
\]
Since \(h_p^p=(p-1)^{p-1}/p^p\) and \(h_p^q=(p-1)/p^q\), these equations are **equivalent** to
\[
\left(\frac{h_p\alpha}{\lambda}\right)^p+
\left(\frac{h_p\beta}{\lambda}\right)^q=1.
\]
The left side is strictly decreasing continuously from infinity to zero as \(\lambda\) runs from zero to infinity. Hence its positive solution is unique, and \(\lambda=h_pR_p(\alpha,\beta)\). The stationary equations force the unique ratios \(r,s\) displayed in the finding. Conversely the maximizer already exists, so these equations determine **all** maximizing moduli; equality in the triangle inequality determines their phases.

**4. The whole disk.** For each real \(\theta\), the diagonal coordinate isometry with factors \((e^{i\theta},1,e^{-i\theta})\) conjugates \(T_{a,b}\) to \(e^{i\theta}T_{a,b}\). Thus its numerical range is circularly invariant. It contains zero (take \(x=(1,0,0)\)) and is the continuous image of the connected complex unit sphere; it is compact. Consequently the set of attained moduli is the full interval from zero to its maximum. Circular invariance produces exactly the stated closed disk.

**5. Duality and asymmetric example.** Put \(q=p/(p-1)\). Direct simplification gives \(h_p=h_q\) and \(R_p(\alpha,\beta)=R_q(\beta,\alpha)\), hence the duality identity. For \(p=4\), let \(Y_{\alpha,\beta}=R_4(\alpha,\beta)^{4/3}\). Then
\[
Y_{8,1}^3-Y_{8,1}^2-4096=0,\qquad
Y_{1,8}^3-16Y_{1,8}^2-1=0.
\]
Each equation has precisely one positive root. Substituting \(65/4\) gives the exact signs \(-4419/64<0\) and \(4161/64>0\), respectively. Therefore \(Y_{8,1}>65/4>Y_{1,8}\), proving the stated strict asymmetry.

## Verification
The accompanying `verify.py` checks the dual-exponent symmetry and KKT witness identities at multiple exponents and positive weights, tests independently sampled unit vectors, and performs exact rational polynomial-sign calculations for the \(p=4\) asymmetry example. Its successful result is `THREE_SITE_WEIGHTED_LP_NUMERICAL_RADIUS_CHECKS_OK`. These finite checks are **not** the proof for all exponents; the continuous all-parameter assertion follows from the analytical argument above.

## Relationship to prior work
Müller and Tomilov (arXiv:2606.22693v1, first posted June 21, 2026) develop spatial and essential numerical ranges on \(\ell_p\). Their Proposition 2.1 treats arbitrary \(2\times2\) matrices; their Proposition 4.16 treats truncated shifts via a polynomial-functional-calculus comparison, not an exact three-site weighted numerical-radius formula. The present result treats the next chain length with two independent complex weights, identifies the mixed \(p,q\) law, and supplies a fixed-exponent weight-order obstruction.

Chien and Nakazato's 2010 study of \(3\times3\) tridiagonal \(q\)-numerical ranges takes place on a Hilbert space and uses a parameter \(0\le q\le1\) controlling an inner-product constraint between two unit vectors. It is not the conjugate exponent \(q=p/(p-1)\) or the spatial numerical range on non-Hilbert \(\ell_p^3\). Classical weighted-shift numerical-radius papers cited below likewise analyze Hilbert-space numerical ranges, including the \(p=2\) special case here. The literature comparison supports absence of a known covering formula among inspected sources, not a proof of absolute novelty.

## Limitations
The classification is restricted to complex \(\ell_p^3\), \(1<p<\infty\), and two-step nilpotent weighted shifts. It gives neither all-matrix spatial numerical ranges nor the numerical radius of arbitrary longer weighted shifts. The 2010 study is distinct because its \(q\) is not the conjugate \(\ell_p\) exponent. Older unindexed Banach-space shift computations might contain an equivalent formula; no wider priority claim is made.

## References
1. V. Müller and Y. Tomilov, *Numerical and essential numerical ranges on \(\ell_p\)*, arXiv:2606.22693v1 (2026), https://arxiv.org/abs/2606.22693 . First public posting: 2026-06-21 UTC.
2. M.-T. Chien and H. Nakazato, *The \(q\)-numerical range of \(3\times3\) tridiagonal matrices*, Electronic Journal of Linear Algebra **20** (2010), 376–390, https://doi.org/10.13001/1081-3810.1382 .
3. K.-Z. Wang and P. Y. Wu, *Numerical ranges of weighted shifts*, Journal of Mathematical Analysis and Applications **381** (2011), 897–909, https://doi.org/10.1016/j.jmaa.2011.04.010 .
4. H. Blazhko et al., *The algebraic numerical range as a spectral set in Banach algebras*, arXiv:2410.10678, https://arxiv.org/abs/2410.10678 .
