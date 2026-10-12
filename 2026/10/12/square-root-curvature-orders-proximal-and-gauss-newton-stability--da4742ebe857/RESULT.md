# Square-root curvature orders proximal and Gauss–Newton stability on radial losses

## Finding

Fix a dimension \(d\geq1\), a radius \(r>0\), and a regularization parameter \(\alpha>0\). Let \(\phi:[0,\infty)\to[0,\infty)\) be finite, convex, nondecreasing, with \(\phi(0)=0\), \(\phi(r)>0\), and derivative \(g=\phi'(r)>0\). On \(\mathbb R^d\), put \(f(y)=\phi(\|y\|)\) and choose any \(x\) with \(\|x\|=r\). Define the exact-proximal (SPP) stability index
\[
\delta_{\rm SPP}(\alpha)=f(x)-\min_y\left\{f(y)+\frac{\|y-x\|^2}{2\alpha}\right\},
\]
and the nonnegative Gauss–Newton (NGN) model index
\[
\delta_{\rm NGN}(\alpha)=f(x)-\min_y\left\{\left(\sqrt{f(x)}+\frac{\langle\nabla f(x),y-x\rangle}{2\sqrt{f(x)}}\right)^2+\frac{\|y-x\|^2}{2\alpha}\right\}.
\]
Let \(q(t)=\sqrt{\phi(t)}\) on \([0,r]\). Then, **for every \(\alpha>0\)**:

* If \(q\) is convex on \([0,r]\), then \(\delta_{\rm SPP}(\alpha)\leq\delta_{\rm NGN}(\alpha)\).
* If \(q\) is concave on \([0,r]\), then \(\delta_{\rm NGN}(\alpha)\leq\delta_{\rm SPP}(\alpha)\).
* If \(q\) is affine on \([0,r]\), the two indices coincide for every \(\alpha>0\).

For the natural radial power family \(f(y)=\|y\|^p/p\) with \(p\geq1\), this is a **strict, sharp threshold at \(p=2\)**: NGN has the strictly smaller index for \(1\leq p<2\); they agree for \(p=2\); SPP has the strictly smaller index for \(p>2\). Moreover, the signed discrepancy has exact small- and large-regularization laws,
\[
\lim_{\alpha\downarrow0}\frac{\delta_{\rm NGN}(\alpha)-\delta_{\rm SPP}(\alpha)}{\alpha^2}
=\frac{p-2}{4}r^{3p-4},
\quad
\lim_{\alpha\to\infty}\alpha\bigl(\delta_{\rm NGN}(\alpha)-\delta_{\rm SPP}(\alpha)\bigr)
=\frac{r^2}{2}\left(1-\frac4{p^2}\right).
\]

## Assumptions and scope

Only one proximal/model step, not a convergence trajectory, is compared. The radial profile is convex, nondecreasing, finite and vanishes at its center. Its differentiability is required only at the nonzero test radius. No global smoothness or stochastic interpolation hypothesis is used. In particular, the exponent \(p=1\) is allowed despite nondifferentiability at the minimizer. The quantities compared are *model stability indices*, not the actual objective values at the two distinct next iterates. The NGN square-root model need not be a global lower bound for \(f\), so this ordering does **not** by itself establish an NGN convergence theorem.

## Proof

**Radial reduction.** Write \(x=re\) for a unit vector \(e\). Since \(\phi\) is nondecreasing, among vectors of norm \(t\) the one closest to \(re\) is \(te\); furthermore, \(\phi(t)+(r-t)^2/(2\alpha)\) cannot be minimized at \(t>r\), because \(\phi(t)\geq\phi(r)\) there while the value at \(t=r\) equals \(\phi(r)\). Hence the exact proximal envelope equals
\[
P=\min_{0\leq t\leq r}\left\{\phi(t)+\frac{(r-t)^2}{2\alpha}\right\}.
\]
Let \(F=\phi(r)>0\) and \(g=\phi'(r)>0\). The squared-tangent model has its unconstrained minimizer on the line through \(e\), with radial coordinate
\[
t_{\rm N}=r-\frac{\alpha g}{1+\alpha g^2/(2F)}.
\]
Its exact model envelope is
\[
N=\frac{F}{1+\alpha g^2/(2F)},
\qquad \delta_{\rm NGN}=F-N,\quad \delta_{\rm SPP}=F-P.
\]
On the test segment, define the affine tangent \(\ell(t)=q(r)+q'(r)(t-r)\), where \(q'(r)=g/(2\sqrt F)\), so the NGN model is \(\ell(t)^2\).

**Convex square root.** Convexity with \(q(0)=0\) implies \(q'(r)\geq q(r)/r\). Consequently the affine tangent vanishes at
\[
t_0=r-\frac{q(r)}{q'(r)}=r-\frac{2F}{g}\in[0,r).
\]
For \(t\in[t_0,r]\), convexity yields \(q(t)\geq\ell(t)\geq0\), hence \(\phi(t)\geq\ell(t)^2\). At every \(0\leq t<t_0\), nonnegativity of \(\phi\) and monotonicity of the squared distance imply
\[
\phi(t)+\frac{(r-t)^2}{2\alpha}\geq\frac{(r-t_0)^2}{2\alpha}
=\ell(t_0)^2+\frac{(r-t_0)^2}{2\alpha}\geq N.
\]
For \(t\geq t_0\), the preceding squared-tangent comparison gives the same lower bound \(N\). Therefore \(P\geq N\), i.e. \(\delta_{\rm SPP}\leq\delta_{\rm NGN}\). Notice that merely squaring a convex function's tangent globally would be invalid once that tangent becomes negative: the split at \(t_0\) is essential.

**Concave square root.** Concavity with \(q(0)=0\) gives \(rg\leq2F\) and \(q(t)\leq\ell(t)\) for \(0\leq t\leq r\). Here \(\ell(t)\geq\ell(0)\geq0\), so \(\phi(t)\leq\ell(t)^2\) on the test segment. If \(t_{\rm N}\geq0\), then \(t_{\rm N}\in[0,r]\), and evaluation of the proximal envelope at the NGN minimizer gives \(P\leq N\).

The remaining case \(t_{\rm N}<0\) can arise only when \(rg<2F\); the defining formula implies
\[
\alpha>\frac{2Fr}{g(2F-rg)}.
\]
The competing proximal point \(t=0\) gives \(P\leq r^2/(2\alpha)\). Direct multiplication shows
\[
\frac{r^2}{2\alpha}\leq \frac{F}{1+\alpha g^2/(2F)}=N
\quad\Longleftrightarrow\quad
\alpha\geq\frac{2Fr^2}{4F^2-r^2g^2}.
\]
This condition follows strictly from the crossing condition, because their right-hand-side ratio (second divided by first) equals \(rg/(2F+rg)<1\). Thus \(P\leq N\) also after the unconstrained NGN step crosses the radial center. This proves \(\delta_{\rm NGN}\leq\delta_{\rm SPP}\) for all stepsizes.

**Affine case.** If \(q(t)=ct\) on \([0,r]\), then \(\ell(t)=ct\) on that segment. The exact and model envelopes attain their minima within that segment (indeed the model minimizer has positive radius), so \(P=N\).

**Powers and quantitative sharpness.** For \(\phi(t)=t^p/p\), the square root is a positive constant times \(t^{p/2}\): strictly concave for \(1\leq p<2\), affine at \(p=2\), strictly convex for \(p>2\). In the convex branch the inequality is strict because the true proximal minimizer has \(0<t<r\), and either it is below \(t_0\), producing a strictly larger distance cost than at \(t_0\), or the strictly convex tangent inequality is strict at it. In the concave branch, if \(t_{\rm N}\geq0\), strict concavity makes the model inequality strict at \(t_{\rm N}<r\); if \(t_{\rm N}<0\), the last displayed crossing comparison is strict. Thus strictness holds for each \(\alpha>0\) when \(p\ne2\).

For \(p>1\), the exact proximal radius \(t_\alpha\in(0,r)\) is the unique solution of
\[
t_\alpha+\alpha t_\alpha^{p-1}=r.
\]
For \(p=1\), it equals \(\max\{r-\alpha,0\}\). Using these exact relations, a Taylor expansion at \(\alpha=0\) gives
\[
\delta_{\rm SPP}=\frac\alpha2 r^{2p-2}-\frac{\alpha^2}{2}(p-1)r^{3p-4}+o(\alpha^2),
\quad
\delta_{\rm NGN}=\frac\alpha2 r^{2p-2}-\frac{\alpha^2p}{4}r^{3p-4}+o(\alpha^2).
\]
For \(p=1\), the same expansion follows from the exact soft-threshold solution for sufficiently small \(\alpha\). Subtraction proves the first limit. As \(\alpha\to\infty\), \(t_\alpha\to0\), \(\alpha\phi(t_\alpha)\to0\), and therefore \(\alpha P\to r^2/2\). The explicit NGN envelope satisfies \(\alpha N\to2r^2/p^2\). Their difference yields the second limit. The signs change only at \(p=2\), establishing the claimed sharp threshold.

## Verification

The included standalone Python script `verify.py` computes both indices by solving the scalar proximal optimality equation with bisection, checks all three ordering regimes, and tests a simple exact linear witness. Running `python verify.py` produced `VERIFY_OK 702 cases; exact linear witness`. The proof above, not the finite sampling, establishes the infinite parameter ranges and both asymptotic limits. The script uses only the Python standard library.

## Relationship to prior work

Schaipp, Gower and Taylor (2026, arXiv:2602.09842v2, Sections 4.3–4.4 and Appendix A.3) give the explicit NGN index and upper bounds for SPP, and exhibit the scalar quadratic equality. Their results compare both with SGD, but do not supply a general sign classification **between** NGN and the exact proximal index for nonquadratic radial losses. Orvieto and Xiao (2024, arXiv:2407.04358v1, Sections 2–4) derive NGN and analyze its adaptation and convergence; the distinction between squared tangents and exact proximal envelopes is not their stated result. Islamov and collaborators (2025, arXiv:2508.15071v1) study a momentum-augmented NGN method rather than the static comparison proved here.

The new assertion is not a universal ordering of the two models over all convex objectives. It identifies a sufficient one-dimensional *shape criterion* determining the sign for an entire natural radial class; the proof handles the otherwise troublesome negative affine-tangent and center-crossing regimes. The quadratic equality already known in the motivating source is included solely to identify the sharp boundary, not claimed independently as new.

## Limitations

The theorem is restricted to nonnegative convex radial losses with a differentiable positive test radius and a square root that is convex or concave on the radial segment. It makes no claim for arbitrary nonradial convex objectives, nonzero loss floors, stochastic expectations without further conditions, multi-step dynamics, or global model minorization. Positive values of the NGN stability index do not guarantee objective monotonicity of actual NGN iterates. Equivalent unindexed results in model-based optimization literature remain possible, and independent validation has not been performed.

## References

1. Fabian Schaipp, Robert M. Gower and Adrien Taylor. *Step-Size Stability in Stochastic Optimization: A Theoretical Perspective*. arXiv:2602.09842v1, 10 February 2026; inspected v2, Sections 4.3–4.4 and Appendix A.3. https://arxiv.org/html/2602.09842v2
2. Antonio Orvieto and Lin Xiao. *An Adaptive Stochastic Gradient Method with Non-negative Gauss–Newton Stepsizes*. arXiv:2407.04358v1, 5 July 2024, Sections 2–4. https://arxiv.org/html/2407.04358v1
3. Rustem Islamov, Niccolò Ajroldi, Antonio Orvieto and Aurélien Lucchi. *Enhancing Optimizer Stability: Momentum Adaptation of the NGN Step-size*. arXiv:2508.15071v1, 20 August 2025; bibliographic abstract inspected. https://arxiv.org/abs/2508.15071
