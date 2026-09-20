# Quantitative near-eigenfunction rigidity for the sharp centered maximal inequality

## Result

Let \(1<p<\infty\), \(p'=p/(p-1)\), and let
\[
M_+f(x)=\sup_{h>0}\frac1h\int_x^{x+h}|f(y)|\,dy,\qquad
M_-f(x)=\sup_{h>0}\frac1h\int_{x-h}^{x}|f(y)|\,dy,
\]
and
\[
M_{\mathrm c}f(x)=\sup_{r>0}\frac1{2r}\int_{x-r}^{x+r}|f(y)|\,dy.
\]
Madrid proved in 2026 that
\[
\|M_{\mathrm c}\|_{L^p(\mathbb R)\to L^p(\mathbb R)}=p',
\]
and that the same norm remains \(p'\) when the centered radii are restricted to powers of two.

The sharp constant is not attained. More quantitatively, put
\[
r_p=\max\{2,p\},\qquad
\Delta_p(f)=p'-\frac{\|M_{\mathrm c}f\|_p}{\|f\|_p}
\]
for \(0\ne f\in L^p(\mathbb R)\). There is a constant \(C_p<\infty\), depending
only on \(p\), such that
\[
\boxed{
\frac{\|M_\pm f-p'|f|\|_p}{\|f\|_p}
\le C_p\,\Delta_p(f)^{1/r_p}
}
\]
for both signs, and
\[
\boxed{
\frac{\|M_{\mathrm c}f-p'|f|\|_p}{\|f\|_p}
\le C_p\,\Delta_p(f)^{1/r_p}.
}
\]
Thus every centered extremizing sequence is simultaneously an approximate
\(p'\)-eigenfunction for the left, right, and centered maximal operators.

The conclusion also holds for Madrid's dyadic-radii centered operator
\[
M_{\mathrm{dyad}}f(x)
=\sup_{j\in\mathbb Z}\frac1{2^{j+1}}
\int_{x-2^j}^{x+2^j}|f(y)|\,dy.
\]
If
\[
\Delta_{p,\mathrm{dyad}}(f)
=p'-\frac{\|M_{\mathrm{dyad}}f\|_p}{\|f\|_p},
\]
then, after changing \(C_p\),
\[
\frac{\|Tf-p'|f|\|_p}{\|f\|_p}
\le C_p\,\Delta_{p,\mathrm{dyad}}(f)^{1/r_p}
\]
for
\[
T\in\{M_-,M_+,M_{\mathrm c},M_{\mathrm{dyad}}\}.
\]

As a compactness consequence, no normalized centered extremizing sequence can
have a strongly convergent subsequence in \(L^p(\mathbb R)\), even after
arbitrary translations and \(L^p\)-normalized dilations.

## Proof

It is enough to work with \(f\ge0\), because every operator above is defined
using \(|f|\). Normalize \(\|f\|_p=1\).

### 1. An exact one-sided identity

For bounded compactly supported \(f\ge0\), Riesz's rising-sun identity, in the
form recalled by Madrid, says
\[
\lambda\,|\{M_\pm f>\lambda\}|
=\int_{\{M_\pm f>\lambda\}} f(x)\,dx.
\]
Layer cake and Tonelli therefore give the exact identity
\[
\boxed{
\|M_\pm f\|_p^p
=
p'\int_{\mathbb R} f(x)\,(M_\pm f(x))^{p-1}\,dx.
}
\tag{1}
\]
For general nonnegative \(f\in L^p\), apply this to
\[
f_m=\min\{f,m\}\mathbf 1_{[-m,m]}.
\]
Then \(f_m\uparrow f\) and \(M_\pm f_m\uparrow M_\pm f\). Monotone convergence
extends (1) to all \(f\in L^p_+\).

Write
\[
u=M_+f,\qquad v=M_-f,\qquad
a=\|u\|_p,\qquad b=\|v\|_p.
\]
The sharp one-sided estimate gives \(a,b\le p'\), while
\[
M_{\mathrm c}f\le \frac{u+v}{2}.
\]
If
\[
\delta=\Delta_p(f)=p'-\|M_{\mathrm c}f\|_p,
\]
then
\[
p'-\delta
\le \frac{a+b}{2}\le p',
\]
and consequently
\[
a,b\ge p'-2\delta.
\tag{2}
\]

### 2. Near equality forces one-sided near-eigenfunctions

For \(a>0\), set \(h=u/a\), so \(\|h\|_p=1\). Identity (1) gives
\[
\int f\,h^{p-1}
=\frac{a}{p'}.
\]
By (2),
\[
\int f\,h^{p-1}\ge1-\frac{2\delta}{p'}.
\tag{3}
\]
The functional \(h^{p-1}\) has \(L^{p'}\)-norm one and norms \(h\). Hence
\[
\left\|\frac{f+h}{2}\right\|_p
\ge
\frac12\int(f+h)h^{p-1}
\ge1-\frac{\delta}{p'}.
\]
The classical Clarkson-Hanner uniform convexity estimate for \(L^p\) has
power type
\[
r_p=\max\{2,p\}:
\qquad
1-\left\|\frac{x+y}{2}\right\|_p
\ge c_p\|x-y\|_p^{r_p}
\]
for unit vectors \(x,y\), with a positive constant depending only on \(p\).
It follows that
\[
\|f-h\|_p\le C_p\delta^{1/r_p}.
\]
Together with \(|a-p'|\le2\delta\), this yields
\[
\|M_+f-p'f\|_p
=\|ah-p'f\|_p
\le C_p\delta^{1/r_p}.
\]
The same argument gives
\[
\|M_-f-p'f\|_p\le C_p\delta^{1/r_p}.
\tag{4}
\]

### 3. The centered operator is forced to the same profile

Put
\[
w=\frac{M_+f+M_-f}{2}.
\]
Equation (4) implies
\[
\|w-p'f\|_p\le C_p\delta^{1/r_p}.
\tag{5}
\]
Since \(0\le M_{\mathrm c}f\le w\), the elementary inequality
\[
(A-B)^p\le A^p-B^p,\qquad 0\le B\le A,
\]
gives
\[
\|w-M_{\mathrm c}f\|_p^p
\le
\|w\|_p^p-\|M_{\mathrm c}f\|_p^p
\le
(p')^p-(p'-\delta)^p.
\]
Hence
\[
\|w-M_{\mathrm c}f\|_p\le C_p\delta^{1/p}.
\]
When \(p\ge2\), \(r_p=p\); when \(1<p\le2\), \(1/p\ge1/2=1/r_p\), and for
small \(\delta\) the term \(\delta^{1/p}\) is bounded by
\(\delta^{1/r_p}\). Enlarging the constant handles the remaining bounded
range of \(\delta\). Combining with (5) proves
\[
\|M_{\mathrm c}f-p'f\|_p\le C_p\delta^{1/r_p}.
\]

### 4. Nonattainment

Suppose a nonzero \(f\) attained the centered norm. Then \(\delta=0\), so the
previous argument forces
\[
M_+|f|=p'|f|
\qquad\text{almost everywhere.}
\tag{6}
\]
Let
\[
F(t)=|\{|f|>t\}|.
\]
Applying the one-sided level-set identity to (6), with
\(\lambda=p't\), gives
\[
p'tF(t)
=
\int_{\{|f|>t\}}|f|
=
tF(t)+\int_t^\infty F(s)\,ds.
\]
Thus
\[
(p'-1)tF(t)=\int_t^\infty F(s)\,ds.
\tag{7}
\]
If the right side is not identically zero, its absolutely continuous
representative solves
\[
tG'(t)+(p-1)G(t)=0,
\qquad
G(t)=\int_t^\infty F(s)\,ds,
\]
so
\[
G(t)=Ct^{-(p-1)},\qquad
F(t)=(p-1)Ct^{-p}
\]
with \(C>0\). But then
\[
\|f\|_p^p
=
p\int_0^\infty t^{p-1}F(t)\,dt
\]
diverges logarithmically. Therefore \(C=0\), forcing \(f=0\), a
contradiction. The sharp centered norm is not attained.

### 5. Dyadic radii and escape of compactness

Madrid proved
\[
\|M_{\mathrm{dyad}}\|_{p\to p}=p',
\qquad
0\le M_{\mathrm{dyad}}f\le M_{\mathrm c}f.
\]
If \(\delta_d=\Delta_{p,\mathrm{dyad}}(f)\), then
\(\Delta_p(f)\le\delta_d\), so the preceding estimates already control
\(M_\pm f\) and \(M_{\mathrm c}f\). Moreover,
\[
\|M_{\mathrm c}f-M_{\mathrm{dyad}}f\|_p^p
\le
\|M_{\mathrm c}f\|_p^p-\|M_{\mathrm{dyad}}f\|_p^p
\le
(p')^p-(p'-\delta_d)^p,
\]
which yields the asserted estimate for \(M_{\mathrm{dyad}}\).

Finally, centered maximal norms are invariant under translations and under
the \(L^p\)-normalized dilations
\[
f(x)\mapsto \lambda^{1/p}f(\lambda(x-a)).
\]
The map \(f\mapsto M_{\mathrm c}f\) is Lipschitz on \(L^p\), because
pointwise
\[
|M_{\mathrm c}f-M_{\mathrm c}g|
\le M_{\mathrm c}(f-g)
\]
and its operator norm is \(p'\). If a normalized centered extremizing
sequence could be made strongly precompact by these symmetries, a strongly
convergent transformed subsequence would converge to a normalized
\(L^p\) extremizer, contradicting nonattainment.

## Relation to prior work

Madrid's 2026 preprint determines the exact centered \(L^p\) norm \(p'\),
constructs smooth compactly supported extremizing sequences, and proves the
same exact norm for the centered operator with dyadic radii. Its upper-bound
proof recalls the sharp one-sided inequalities and the rising-sun
level-set identity used above. The paper does not state nonattainment or a
near-extremizer classification.

The one-dimensional uncentered maximal operator has a different sharp norm.
Grafakos and Montgomery-Smith determined that norm in 1997. Colzani and
Pérez Lázaro later studied eigenfunctions of the uncentered operator and
proved nonattainment of its \(L^p\) norm. Those results concern the
uncentered operator and do not provide the centered \(p'\)-norm rigidity
above.

The quantitative step here is the observation that the proof of the newly
sharp centered inequality has a stable equality chain. A centered
near-extremizer must nearly saturate both one-sided inequalities. The exact
one-sided identity converts that numerical saturation into almost equality
in Hölder, and uniform convexity then forces both one-sided maximal
functions to approach the same profile \(p'|f|\). Pointwise domination
transfers the same rigidity to the centered operator.

## Limitations

- The exponent \(1/\max\{2,p\}\) comes from the standard power type of the
  \(L^p\) modulus of convexity. It is not claimed to be the optimal
  near-extremizer exponent for this maximal inequality.
- No spatial classification of Madrid's multiscale extremizing sequences is
  obtained. The conclusion is an operator-profile rigidity statement.
- The compactness conclusion rules out strong precompactness modulo the
  natural translation/dilation symmetries; it does not identify a complete
  concentration-compactness decomposition.
- The result is one-dimensional and uses the exact one-sided \(p'\) identities.
  No higher-dimensional analogue is claimed.
- The dyadic-radii statement concerns the centered geometric family in
  Madrid's definition, not the usual dyadic-grid maximal operator.

## References

1. J. Madrid, *The norm of the centered Hardy--Littlewood maximal operator*,
   arXiv:2609.12440 (2026). https://arxiv.org/abs/2609.12440
2. L. Grafakos and S. Montgomery-Smith, *Best Constants for Uncentred
   Maximal Functions*, Bull. London Math. Soc. 29 (1997), 60--64.
   https://doi.org/10.1112/S0024609396002081
3. L. Colzani and J. Pérez Lázaro, *Eigenfunctions of the Hardy--Littlewood
   maximal operator*, Colloq. Math. 118 (2010), 379--389.
   https://doi.org/10.4064/CM118-2-2
4. O. Hanner, *On the uniform convexity of \(L^p\) and \(\ell^p\)*,
   Ark. Mat. 3 (1956), 239--244.
   https://doi.org/10.1007/BF02589410
