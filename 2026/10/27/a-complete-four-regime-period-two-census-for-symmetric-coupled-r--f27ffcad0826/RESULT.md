# A complete four-regime period-two census for symmetric coupled RMSProp

## Finding

For the uncorrected, per-coordinate RMSProp map defined below, with positive-definite coupled Hessian \(A=\begin{pmatrix}a&b\\b&a\end{pmatrix}\), \(a>b>0\), there are exactly \(0\), \(1\), \(2\), or \(4\) distinct prime-period-two orbits, depending on the learning rate. Define the strictly increasing thresholds
\[
h_+=\frac{2\varepsilon}{a+b},\qquad h_-=\frac{2\varepsilon}{a-b},\qquad h_{\mathrm{sb}}=\frac{2\varepsilon(a+b)}{(a-b)^2}.
\]
Writing \(N(h)\) for the number of geometric period-two orbits (an orbit is counted once, not once for each of its two points), the **complete census** is
\[
N(h)=\begin{cases}
0,&0<h\le h_+,\\
1,&h_+<h\le h_-,\\
2,&h_-<h\le h_{\mathrm{sb}},\\
4,&h>h_{\mathrm{sb}}.
\end{cases}
\]
At the last threshold two asymmetric branches merge into the antisymmetric branch. At arbitrarily large learning rates the two additional cycles have normalized spatial representatives converging to \((1/2,-b/(2a))\) and \((b/(2a),-1/2)\); thus they are **not** corner cycles, even though the Hessian is strictly diagonally dominant.

## Assumptions and scope

Fix real \(a>b>0\), \(0<\beta<1\), \(h>0\), and \(\varepsilon>0\). Let \(A=\begin{pmatrix}a&b\\b&a\end{pmatrix}\), so its eigenvalues are \(a+b\) and \(a-b\), both positive. The loss is \(L(x)=\frac12x^\top Ax\). At state \((x,v)\in\mathbb R^2\times[0,\infty)^2\), first update the coordinatewise second moment and then the position:
\[
v_i'=\beta v_i+(1-\beta)(Ax)_i^2,\qquad
x_i'=x_i-\frac{h(Ax)_i}{\sqrt{v_i'}+\varepsilon}\quad(i=1,2).
\]
No bias correction, momentum, or square-root-inside regularization is assumed. The result counts **all** geometric prime-period-two orbits of the four-dimensional map, without imposing symmetry on candidate orbits. It does not assert their orbital stability.

For explicit representatives, set \(c=\varepsilon/h\), \(X=x/h\), and \(W_i=\sqrt{v_i}/h\). Every prime-two orbit is determined by a nonzero \(X\in(-1/2,1/2)^2\), modulo \(X\sim-X\), satisfying
\[
(AX)_i=\frac{2cX_i}{1-2|X_i|}\quad (i=1,2).
\tag{1}
\]
Its two original states are \((hX,h^2|AX|^{\odot2})\) and \((-hX,h^2|AX|^{\odot2})\). Here absolute values and squares are coordinatewise.

The always-symmetric branch has representatives \(X=(t_+,t_+)\), with
\[
t_+=\frac12\left(1-\frac{2c}{a+b}\right)>0,
\]
and exists exactly for \(c<(a+b)/2\). The antisymmetric branch has \(X=(t_-,-t_-)\), with
\[
t_-=\frac12\left(1-\frac{2c}{a-b}\right)>0,
\]
and exists exactly for \(c<(a-b)/2\). The two further branches exist exactly for
\[
0<c<c_{\mathrm{sb}}:=\frac{(a-b)^2}{2(a+b)}.
\]
Write
\[
s=\frac{a+b-2c}{2a},\qquad
D=\frac{(a+b-2c)((a-b)^2-2c(a+b))}{4a^2(a+b)},\qquad
x=\frac{s+\sqrt D}{2},\quad z=\frac{s-\sqrt D}{2}.
\]
Their representatives are \(X=(x,-z)\) and \(X=(z,-x)\), with \(0<z<x<1/2\). In the limit \(c\downarrow0\), \(x\to1/2\) and \(z\to b/(2a)\). At \(c=c_{\mathrm{sb}}\), \(D=0\) and \(x=z=b/(a+b)=t_-\), so the extra branches have merged rather than supplying extra orbits.

## Proof

**1. Antipodal reduction for every prime-two state.** Work in normalized coordinates \((X,W)\), where \(W=\sqrt v/h\), and write the map as
\[
W_i'=\sqrt{\beta W_i^2+(1-\beta)(AX)_i^2},\qquad
X_i'=X_i-\frac{(AX)_i}{W_i'+c}.
\]
Suppose two states \((X_1,W_1)\) and \((X_2,W_2)\) form a period-two pair. Fix coordinate \(i\), and abbreviate \(u=(W_1)_i\), \(v=(W_2)_i\), \(s=|(AX_1)_i|\), and \(t=|(AX_2)_i|\). The two memory updates give
\[
(1+\beta)u^2=\beta s^2+t^2,\qquad
(1+\beta)v^2=s^2+\beta t^2.
\tag{2}
\]
The spatial displacements are opposite, so \(s/(v+c)=t/(u+c)\), equivalently \(s(u+c)=t(v+c)\). If \(s>t\), then \(su<tv\). However (2) gives
\[
(1+\beta)(s^2u^2-t^2v^2)=\beta(s^4-t^4)>0,
\]
a contradiction. Interchanging \(s,t\) rules out \(t>s\). Thus \(s=t\), and (2) gives \(u=v=s\). The signed opposite displacements now imply \((AX_1)_i=-(AX_2)_i\). This holds in both coordinates; invertibility of \(A\) gives \(X_2=-X_1\) and identical memory vectors \(W_1=W_2=|AX_1|\). The position update becomes \(2X_i=(AX)_i/(|(AX)_i|+c)\). Necessarily \(|X_i|<1/2\); solving for \((AX)_i\) yields (1). Conversely any nonzero solution of (1) yields a genuine period-two orbit by substitution. The argument uses \(\beta>0\) for strictness and applies also if an individual gradient coordinate vanishes.

**2. Every nonzero coordinate is nonzero.** If \(X_1=0\), equation (1) gives \((AX)_1=bX_2=0\), hence \(X_2=0\), contrary to the nonzero requirement. By symmetry the other coordinate cannot vanish. Thus after replacing \(X\) with \(-X\), every solution has either the form \((x,z)\) or \((x,-z)\), with \(x,z>0\).

**3. Same-sign solutions.** For \((X_1,X_2)=(x,z)\), (1) gives
\[
a+b\frac zx=\frac{2c}{1-2x},\qquad
a+b\frac xz=\frac{2c}{1-2z}.
\]
If \(x>z\), the first left side is smaller than the second, while its right side is larger. If \(z>x\), the reverse contradiction holds. Therefore \(x=z=t_+\). Substitution shows the stated existence condition and uniqueness.

**4. Opposite-sign solutions.** For \(X=(x,-z)\), (1) becomes
\[
a x-b z=\frac{2cx}{1-2x},\qquad
a z-b x=\frac{2cz}{1-2z}.
\tag{3}
\]
When \(x=z\), (3) has precisely \(x=z=t_-\), which exists if and only if \(c<(a-b)/2\). Suppose instead \(x\ne z\). Subtract (3) to obtain
\[
(1-2x)(1-2z)=\frac{2c}{a+b}.
\tag{4}
\]
Subtract the two equations after division by \(x\) and \(z\), respectively; using (4) gives
\[
\frac{b(x+z)}{xz}=2(a+b).
\tag{5}
\]
Consequently their sum and product are uniquely fixed:
\[
x+z=s:=\frac{a+b-2c}{2a},\qquad xz=\frac{bs}{2(a+b)}.
\tag{6}
\]
The discriminant of the quadratic with roots \(x,z\) is precisely \(D\) in the statement. Since \(x,z>0\) and (4) requires \(c>0\), the only region in which distinct positive real roots can occur is \(0<c<c_{\mathrm{sb}}\). Conversely in this region \(s>0\), the product in (6) is positive and \(D>0\), so the two roots are positive. Moreover \(s<1\), and (4) is positive: hence either both roots lie below \(1/2\) or both above; the latter would imply \(s>1\), impossible. Thus \(0<z<x<1/2\). Relations (4)–(6) reconstruct both equations (3), so both permutations actually solve (1). For \(c=c_{\mathrm{sb}}\) the roots coalesce and yield the already counted antisymmetric branch. For \(c>c_{\mathrm{sb}}\) no distinct-root solution exists.

**5. Exhaustive counting.** The branches from steps 3–4 exhaust all sign patterns modulo antipodality. Their existence thresholds in \(c\) satisfy
\[
0<c_{\mathrm{sb}}<\frac{a-b}{2}<\frac{a+b}{2}
\]
because \(a>b>0\). On replacing \(c\) with \(\varepsilon/h\), the existence conditions give exactly the four regimes in the Finding. Distinct representatives cannot describe the same orbit unless they differ by a global sign; none of the listed positive-first-coordinate representatives do. The limiting formulas follow by taking \(c\downarrow0\) in (6) and \(D\), as stated. This completes the classification.

## Verification

The accompanying standalone script `check_cycles.py` computes the explicit branch formulas, substitutes them into the reduced self-consistency equations, and applies both steps of the four-dimensional RMSProp map with several choices of \(\beta\). It reports `CHECKS_PASS: 120 complete two-step orbit substitutions across four Hessians and three memory parameters; 3 exact-rational discriminant checks.` This numerically tests the stated formulas on a finite parameter collection; the exhaustive orbit count and all real-parameter assertions follow from the analytic proof, not from those finite tests.

## Relationship to prior work

Regis and Chewi (May 7, 2026), §§5.1–5.2 and Appendix D, study per-component RMSProp and its oscillatory edge-of-stability limit, motivating the question of exact discrete-cycle geometry; their quadratic analytic example is scalar and their main object is a continuous-time rod-flow approximation. Subsequently, Loh, Mireles James, Xu, and Tao (October 21, 2026), §§3 and 5, prove a general period-two reduction and existence theory for quadratic RMSProp, including branches near strictly admissible corners. The present theorem complements their statements by classifying **every** period-two orbit in an explicit non-diagonal two-dimensional family and identifying two noncorner large-learning-rate cycles and their exact merger threshold. Their corner theorem only guarantees two corner branches modulo sign for this diagonally dominant Hessian and does not logically imply that the other two branches are absent or present. Earlier scalar-cycle accounts do not themselves imply a coupled two-coordinate census.

## Limitations

The Hessian is restricted to the reflection-symmetric family with strictly positive coupling \(0<b<a\). The count is for exact prime-two orbits of the uncorrected epsilon-outside discrete map; it does not classify other periods, chaotic attractors, or orbit stability, and it does not apply without proof to alternative RMSProp regularizations or bias-corrected variants. The branch-merger statement concerns the zero set of the period-two equations, not a claim about a Floquet-stability bifurcation. Independent mathematical and literature-priority validation remains outstanding.

## References

1. E. Regis and S. Chewi, *A Rod Flow Model for Adam at the Edge of Stability*, arXiv:2605.06821v1 (first public May 7, 2026), §§5.1–5.2, Appendix D, https://arxiv.org/abs/2605.06821.
2. K. Loh, J. D. Mireles James, Z. Xu, and M. Tao, *The Dynamics of RMSProp Beyond the Stability Threshold*, arXiv:2610.30078v1 (first public October 21, 2026), Lemma 5.1, Theorems 5.2 and 5.9–5.10, Remark 5.11, https://arxiv.org/abs/2610.30078.
