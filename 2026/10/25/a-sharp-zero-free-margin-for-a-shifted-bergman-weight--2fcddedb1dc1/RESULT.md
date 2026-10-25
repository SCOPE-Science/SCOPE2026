# A sharp zero-free margin for a shifted Bergman weight

## Finding

Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), use unnormalized area measure \(dA\), and give the holomorphic space the norm
\[
\|f\|_r^2=\int_{\mathbb D}|f(z)|^2|z-r|^2\,dA(z),\qquad 0\le r<1.
\]
Its weighted Bergman kernel is
\[
K_r(z,w)=
\frac{P_r(z,\overline w)}
{\pi(1-z\overline w)^2(1-rz)^2(1-r\overline w)^2},
\qquad
P_r(z,v)=2-r^2-r(z+v)+(2r^2-1)zv.
\]
The canonical polynomial numerator has the exact sharp margin
\[
\boxed{\min_{\substack{|z|\le1\\|v|\le1}}|P_r(z,v)|=(1-r)^2.}
\]
The minimum is attained at \(z=v=1\). In particular, \(K_r(z,w)\ne0\) for every \((z,w)\in\mathbb D^2\). Moreover, if \(E\) is continuous on the closed bidisk and \(\|E\|_\infty<(1-r)^2\), then \(P_r+E\) is zero-free there. This threshold is sharp: the constant perturbation \(E\equiv-(1-r)^2\) creates a zero at \((1,1)\). A rotation reduces a general interior weight zero \(a\in\mathbb D\) to \(r=|a|\), so the same margin and stability radius are \((1-|a|)^2\).

## Assumptions and scope

The weight is exactly \(|z-a|^2\), with one simple zero \(a\) in the disk. The measure is \(dA\), not normalized area; this fixes the factor \(1/\pi\) in the kernel. The margin concerns the canonical polynomial numerator after the displayed rational normalization, not the minimum modulus of the full kernel. The result does not classify weights with multiple interior zeros or arbitrary nonradial weights.

## Proof

**Step 1: Kernel formula and factorization.** The unweighted disk kernel is
\[
K(z,w)=\frac{1}{\pi(1-z\overline w)^2}.
\]
The one-zero weighted-kernel decomposition gives
\[
K_r(z,w)=\frac{1}{(z-r)(\overline w-r)}
\left(K(z,w)-\frac{K(z,r)K(r,w)}{K(r,r)}\right),
\]
with removable singularities at \(z=r\) and \(w=r\). Substituting the disk kernel and using
\[
\begin{aligned}
&(1-rz)(1-rv)-(1-r^2)(1-zv)=(z-r)(v-r),\\
&(1-rz)(1-rv)+(1-r^2)(1-zv)=P_r(z,v)
\end{aligned}
\]
cancels the removable factors and yields the stated formula.

**Step 2: \(P_r\) has no zeros on the closed bidisk.** For \(r=0\), \(P_0(z,v)=2-zv\), so \(|P_0|\ge1\) whenever \(|z|,|v|\le1\). Let \(0<r<1\), and suppose \(P_r(z,v)=0\). Rearrangement gives
\[
\big((2r^2-1)z-r\big)v=rz+r^2-2.
\]
Put \(N=rz+r^2-2\), \(D=(2r^2-1)z-r\), and \(\rho=|z|\). Direct expansion gives
\[
|N|^2-|D|^2=(1-r^2)
\left((4r^2-1)|z|^2-6r\operatorname{Re}z+4-r^2\right).
\]
The bracket is at least
\[
f_r(\rho)=(4r^2-1)\rho^2-6r\rho+4-r^2.
\]
For \(r^2\le1/4\), \(f_r'(\rho)\le-6r<0\). For \(r^2\ge1/4\), \(f_r'\) is increasing and
\[
f_r'(1)=2(4r+1)(r-1)<0,
\]
so \(f_r'(\rho)<0\) for \(0\le\rho\le1\) as well. Therefore
\[
f_r(\rho)\ge f_r(1)=3(1-r)^2>0.
\]
Thus \(|N|>|D|\). If \(D=0\), then \(N\ne0\); otherwise the equation forces \(|v|=|N/D|>1\). Both cases contradict \(P_r(z,v)=0\) on the closed bidisk.

**Step 3: Reduce the minimum to the torus.** Since \(P_r\) is zero-free on the closed bidisk, \(1/P_r\) is holomorphic on a neighborhood of it. Applying the maximum-modulus principle in each variable shows that the minimum of \(|P_r|\) on the closed bidisk equals its minimum on \(|z|=|v|=1\).

Write \(z=e^{i\theta}\), \(v=e^{i\phi}\), \(x=(\theta+\phi)/2\), and \(y=(\theta-\phi)/2\). A direct expansion gives
\[
e^{-ix}P_r(z,v)=(1+r^2)\cos x-2r\cos y-3i(1-r^2)\sin x.
\]
Set \(c=|\cos x|\) and \(c_0=2r/(1+r^2)\). Minimizing over \(\cos y\in[-1,1]\) reduces the squared modulus to
\[
G_r(c)=
\begin{cases}
9(1-r^2)^2(1-c^2),&0\le c\le c_0,\\
((1+r^2)c-2r)^2+9(1-r^2)^2(1-c^2),&c_0\le c\le1.
\end{cases}
\]
On the first interval, the minimum occurs at \(c_0\), with value
\[
\frac{9(1-r^2)^4}{(1+r^2)^2}\ge(1-r)^4.
\]
On the second interval,
\[
G_r''(c)=8(2r^2-1)(2-r^2).
\]
If \(r^2\le1/2\), \(G_r\) is concave, so its minimum occurs at an endpoint; the value at \(c_0\) is at least \((1-r)^4\), while \(G_r(1)=(1-r)^4\). If \(r^2\ge1/2\), \(G_r\) is convex and
\[
G_r'(1)=2(1-r)^2\big((1+r^2)-9(1+r)^2\big)<0.
\]
Hence \(G_r\) decreases on \([c_0,1]\), and again its minimum is \(G_r(1)=(1-r)^4\). The bound is attained at \(z=v=1\), proving the exact margin \((1-r)^2\).

## Verification

The kernel identity follows by factoring the difference of two squares in the one-zero decomposition formula. The zero-free step is an analytic inequality valid for every \(0\le r<1\) and every \(|z|\le1\); it is not inferred from a finite numerical search. The boundary minimization treats both curvature regimes \(r^2\le1/2\) and \(r^2\ge1/2\), including the endpoints. The sharpness witness is \(z=v=1\). No numerical approximation or external certificate is needed.

## Relationship to prior work

Jacobson's 2013 paper gives the one-zero weighted-kernel decomposition, a general finite-zero extension, and qualitative results on how kernel zero sets change under this weight. That establishes the route to the rational kernel formula, but the sharp global minimum of its canonical numerator is not stated in the inspected text. Miña-Díaz's later representation covers a broader family of finite Blaschke-factor weights, but the exact \((1-r)^2\) bidisk margin is not stated in the inspected text. Targeted literature searches returned related radial-weight and jet-kernel work, but no exact statement of this off-center one-zero numerator margin in the inspected sources. The contribution here is the sharp quantitative minimum, not the general kernel-decomposition method.

## Limitations

The exact margin is attached to the displayed canonical numerator normalization. It does not by itself give the minimum modulus of \(K_r\), a perturbation theorem for arbitrary changes of weight, or a zero-free criterion for weights with several zeros. The general weighted-kernel formulas in the literature make this family accessible, so the originality claim is limited to the sharp extremal inequality and its boundary-degeneration rate.

## References

1. R. Jacobson, “Weighted Bergman kernel functions associated to meromorphic functions,” arXiv:1309.4800 (first submitted 18 September 2013). https://arxiv.org/abs/1309.4800
2. E. Miña-Díaz, “A representation for the reproducing kernel of a weighted Bergman space,” arXiv:2212.08118 (first submitted 15 December 2022). https://arxiv.org/abs/2212.08118
