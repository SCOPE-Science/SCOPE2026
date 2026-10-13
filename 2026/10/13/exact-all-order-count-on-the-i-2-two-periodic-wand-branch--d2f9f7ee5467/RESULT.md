# Exact all-order count on the \(I_2\) two-periodic wand branch

## Finding

For the three-state hard-core model of type wand on the Cayley tree of order \(k\ge2\), consider the two-periodic invariant set \(I_2\) used by Khakimov and Umirzakova. On this set the boundary-law equations reduce to
\[
z=h(t),\qquad t=h(z),\qquad h(x)=\alpha(1+x^{-1})^k,\qquad \alpha=\frac{\lambda}{2^k}.
\]
Define
\[
\lambda_{\mathrm{cr}}(k)=2^k(k-1)\left(\frac{k-1}{k}\right)^k.
\]
Then the complete positive-solution count on \(I_2\) is
\[
\boxed{
\begin{array}{ll}
\lambda\ge\lambda_{\mathrm{cr}}(k):&\text{exactly one positive solution},\\
0<\lambda<\lambda_{\mathrm{cr}}(k):&\text{exactly three positive ordered solutions}.
\end{array}
}
\]
The unique solution in the first line is the translation-invariant fixed point. In the second line, the other two solutions are one swapped pair \((z,t)\) and \((t,z)\), hence one symmetry-broken two-cycle.

Every nontrivial pair is uniquely parameterized by \(s>0\):
\[
z(s)=\sum_{j=1}^{k-1}e^{2js},\qquad
t(s)=\sum_{j=1}^{k-1}e^{-2js},
\]
\[
\boxed{
\lambda(s)=2^k\frac{\sinh^{k+1}((k-1)s)}{\sinh(s)\,\sinh^k(ks)}.
}
\]
The function \(s\mapsto\lambda(s)\) is a strictly decreasing bijection from \((0,\infty)\) onto \((0,\lambda_{\mathrm{cr}}(k))\).

At the merger with the translation-invariant branch,
\[
\boxed{
\left|\log\frac{z}{t}\right|
=
\sqrt{\frac{24k}{\lambda_{\mathrm{cr}}(k)(k+1)}}
\sqrt{\lambda_{\mathrm{cr}}(k)-\lambda}
+O\!\left((\lambda_{\mathrm{cr}}(k)-\lambda)^{3/2}\right).
}
\]
Thus the bifurcating pair has an explicit square-root onset for every tree order.

## Assumptions and scope

The result assumes integer \(k\ge2\), activity \(\lambda>0\), and the source's invariant set \(I_2\), on which the two parity classes are represented by two positive scalars \(z,t\). It concerns positive solutions of the reduced boundary-law equations and the corresponding \(G_k^{(2)}\)-periodic splitting Gibbs measures on that invariant set.

The source explicitly notes that other invariant sets may exist. The result therefore does not classify all periodic Gibbs measures of the full four-variable system. It also makes no assertion about extremality, reconstruction, free-energy dominance, or non-periodic Gibbs measures.

## Proof

The function \(h\) is strictly decreasing on \((0,\infty)\), with \(h(x)\to\infty\) as \(x\downarrow0\) and \(h(x)\to\alpha\) as \(x\to\infty\). Hence \(x=h(x)\) has exactly one positive solution, giving the translation-invariant point for every \(\lambda>0\).

Consider a nontrivial solution and, after swapping the parity classes if necessary, assume \(z>t\). Set
\[
x=z^{1/k},\qquad y=t^{1/k},\qquad r=\frac{x}{y}>1,
\qquad a=\alpha^{1/k}=\frac{\lambda^{1/k}}2.
\]
The two equations become
\[
x=a(1+y^{-k}),\qquad y=a(1+x^{-k}).
\]
Subtracting them and cancelling \(x-y\ne0\) gives
\[
a=\frac{x^k y^k}{x^{k-1}+x^{k-2}y+\cdots+y^{k-1}}.
\]
Substituting \(x=ry\) back into the first equation yields
\[
y^k=\sum_{j=1}^{k-1}r^{-j},\qquad
x^k=\sum_{j=1}^{k-1}r^j.
\]
Therefore every nontrivial solution has
\[
t=\sum_{j=1}^{k-1}r^{-j},\qquad
z=\sum_{j=1}^{k-1}r^j,
\]
and conversely these formulas satisfy the system when
\[
\lambda=2^k\frac{r(r^{k-1}-1)^{k+1}}{(r-1)(r^k-1)^k}.
\]
Writing \(r=e^{2s}\) produces the stated hyperbolic formula.

It remains to prove that this parameterization never folds. For fixed \(s>0\), define
\[
H_s(u)=u\coth(us),\qquad u>0.
\]
A direct differentiation gives
\[
H_s''(u)=2s\,\operatorname{csch}^2(us)\bigl(us\coth(us)-1\bigr)>0,
\]
so \(H_s\) is strictly convex. If \(\Delta_j=H_s(j+1)-H_s(j)\), then \(\Delta_j\) is strictly increasing. Differentiating the logarithm of \(\lambda(s)\) gives
\[
\frac{d}{ds}\log\lambda(s)
=(k+1)H_s(k-1)-H_s(1)-kH_s(k)
=
\sum_{j=1}^{k-2}\Delta_j-k\Delta_{k-1}<0,
\]
where the sum is empty when \(k=2\). Thus \(\lambda(s)\) is strictly decreasing.

Using \(\sinh(cs)\sim cs\) at the origin gives
\[
\lim_{s\downarrow0}\lambda(s)
=2^k\frac{(k-1)^{k+1}}{k^k}
=\lambda_{\mathrm{cr}}(k),
\]
while \(\lambda(s)\sim2^k e^{-2s}\to0\) as \(s\to\infty\). Hence there is exactly one nontrivial unordered pair for every \(0<\lambda<\lambda_{\mathrm{cr}}(k)\), and none at or above the critical activity.

Finally,
\[
\log\lambda(s)
=
\log\lambda_{\mathrm{cr}}(k)
-\frac{k(k+1)}6s^2+O(s^4).
\]
Also \(z/t=r^k=e^{2ks}\), so \(\lvert\log(z/t)\rvert=2ks\). Inverting the preceding expansion gives the claimed square-root law.

## Verification

The accompanying `verify.py` performs exact rational substitutions for the parameterization for \(2\le k\le12\) and several rational values of \(r>1\). It also checks the source's special critical values \(\lambda_{\mathrm{cr}}(2)=1\) and \(\lambda_{\mathrm{cr}}(3)=128/27\), samples strict monotonicity for \(2\le k\le40\), and checks the stated near-critical coefficient numerically. These computations are supplementary; the all-order proof is the algebraic reduction and strict-convexity argument above.

## Relationship to prior work

Khakimov and Umirzakova derive the same reduced system on \(I_2\). Their preprint proves exact one-versus-three counts for \(k=2\) and \(k=3\), then states for general \(k\ge2\) only that at least three periodic splitting Gibbs measures exist when \(0<\lambda<\lambda_{\mathrm{cr}}(k)\). Their proof uses a derivative criterion that guarantees a two-cycle but does not exclude additional positive two-cycles. The result above supplies that exclusion, an explicit global parameterization, and the merger asymptotic.

The earlier Rozikov--Shoyusupov paper studies periodic Gibbs measures for fertile three-state hard-core models, but its periodic section treats the hinge case and explicitly remarks that the wand case requires a separate analogue. It therefore does not imply the present \(I_2\) wand classification. The Rozikov--Khakimov paper gives the arbitrary-order translation-invariant classification for fertile three-state hard-core models, not the all-order two-periodic count on \(I_2\).

Targeted searches using the source title, theorem language, the exact critical activity, the scalar two-cycle equation, the hyperbolic parameterization, and aliases for two-periodic splitting Gibbs measures did not locate a published statement implying the exact all-order count.

## Limitations

The classification is exact only on \(I_2\). The source's full two-periodic system has four positive variables and several invariant sets, and the source notes that other invariant sets may exist. The result does not rule out periodic measures outside \(I_2\).

The square-root law describes the boundary-law ratio near the \(I_2\) merger; it is not a thermodynamic critical exponent claim. No extremality statement is made for the periodic measures.

A residual originality risk is an equivalent one-dimensional two-cycle classification in weakly indexed hard-core or Bethe-lattice literature under different coordinates.

## References

1. R. M. Khakimov and K. O. Umirzakova, “Periodic Gibbs measures for three states HC models in the case Wand,” arXiv:2007.14611v1, first submitted 2020-07-29; journal version, *Journal of Mathematical Physics, Analysis, Geometry* 20 (2024), 66–81, DOI 10.15407/mag20.01.066.
2. U. A. Rozikov and Sh. A. Shoyusupov, “Fertile Three State Hard-Core Models on a Cayley Tree,” arXiv:math-ph/0703039v1, first submitted 2007-03-13; journal version, *Theoretical and Mathematical Physics* 156 (2008), 1319–1330, DOI 10.1007/s11232-008-0109-5.
3. U. A. Rozikov and R. M. Khakimov, “Gibbs measures for the fertile three-state hard-core models on a Cayley tree,” *Queueing Systems* 81 (2015), 49–69, DOI 10.1007/s11134-015-9450-1.
