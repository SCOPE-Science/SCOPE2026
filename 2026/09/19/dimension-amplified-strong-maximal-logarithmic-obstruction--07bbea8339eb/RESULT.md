# Dimension-amplified logarithmic endpoint failure for the strong maximal operator

## Statement

Let \(n\ge 2\) and \(1<p<\infty\). Let \(M_{\mathrm s}\) be the strong maximal operator on \(\mathbb R^n\), with the supremum taken over all bounded axis-parallel rectangles, and let
\[
[w]_{A_p^{\mathrm{str}}}
=
\sup_R \langle w\rangle_R
\left\langle w^{-1/(p-1)}\right\rangle_R^{p-1}.
\]

There are constants \(c_{n,p},C_{n,p}>0\) and, for every sufficiently small
\(0<\theta<\theta_{n,p}\), a weight \(w_\theta\in A_p^{\mathrm{str}}(\mathbb R^n)\)
such that
\[
c_{n,p}\theta^{1-p}
\le [w_\theta]_{A_p^{\mathrm{str}}}
\le C_{n,p}\theta^{1-p},
\]
while
\[
\|M_{\mathrm s}\|_{L^p(w_\theta)\to L^p(w_\theta)}
\ge
c_{n,p}\theta^{-1}
\left(\log\frac1\theta\right)^{(n-1)/p}.
\]
Equivalently, along weights with \(A=[w]_{A_p^{\mathrm{str}}}\to\infty\),
\[
\boxed{
\|M_{\mathrm s}\|_{L^p(w)\to L^p(w)}
\gtrsim_{n,p}
A^{1/(p-1)}(\log A)^{(n-1)/p}.
}
\]

Consequently the endpoint Buckley-type estimate
\[
\|M_{\mathrm s}\|_{L^p(w)\to L^p(w)}
\lesssim_{n,p}
[w]_{A_p^{\mathrm{str}}}^{1/(p-1)}
\]
fails for every \(n\ge2\) and every \(1<p<\infty\).

For \(n=2,p=2\) this reduces, up to constants, to Lerner's recent lower bound
\([w]_{A_2^{\mathrm{str}}}\sqrt{\log [w]_{A_2^{\mathrm{str}}}}\).
The new point is that the same mass mechanism admits an \(n\)-parameter, all-\(p\)
formulation whose hyperbolic multiplicity produces the exponent \((n-1)/p\).

## Context

Lerner proved the failure of the linear \(A_2\) estimate in
\(\mathbb R^2\), explicitly restricting the presentation to \(n=2,p=2\)
for simplicity [1]. Shortly afterwards Ombrosi and Rey improved the known upper
power exponents for every \(1<p<\infty\) and \(n\ge2\); in their introduction the
available lower-bound advance is still Lerner's two-dimensional \(p=2\) result [2].
The optimal power exponent remains unknown.

The theorem here does not improve the lower *power* exponent
\(1/(p-1)\); the gain is logarithmic. It shows, however, that failure at that
endpoint power is universal in both \(p\) and dimension, and that the logarithmic
obstruction grows with the number of independent rectangular parameters.

## Construction on the unit cube

Fix \(n\ge2\), \(1<p<\infty\), and \(0<\theta\ll_{n,p}1\).
Choose \(D\) maximal with
\[
\theta(D+1)^{n-1}\le \frac14,
\]
so \(D\asymp_n\theta^{-1/(n-1)}\), and put \(a=2^{-D}\).
Partition \([0,1)\) into
\[
I_0=[0,a),\qquad
I_r=[2^{r-1}a,2^ra),\quad 1\le r\le D.
\]
For \(\mathbf r=(r_1,\dots,r_n)\in\{0,\dots,D\}^n\), write
\[
C_{\mathbf r}=\prod_{i=1}^n I_{r_i},
\qquad
R_{\mathbf r}=\prod_{i=1}^n[0,2^{r_i}a).
\]
Let \(\mathbf0=(0,\dots,0)\), and define positive cell masses recursively by
\[
m_{\mathbf0}=1,
\qquad
m_{\mathbf r}
=
\frac{\theta}{1-\theta}
\sum_{\substack{\mathbf u\le\mathbf r\\ \mathbf u\ne\mathbf r}}
m_{\mathbf u}
\quad(\mathbf r\ne\mathbf0).
\]
Set
\[
S_{\mathbf r}=\sum_{\mathbf u\le\mathbf r}m_{\mathbf u}.
\]
Then
\[
m_{\mathbf r}=\theta S_{\mathbf r}\quad(\mathbf r\ne\mathbf0),
\qquad S_{\mathbf0}=1.
\]

Define a density \(\sigma\) by
\[
\sigma|_{C_{\mathbf r}}=\frac{m_{\mathbf r}}{|C_{\mathbf r}|},
\]
and set
\[
w=\sigma^{1-p}.
\]
Thus \(\sigma=w^{-1/(p-1)}\).

## Uniform control of the rectangular \(A_p\) characteristic

### Cumulative-mass growth

If \(\mathbf r+e_i\) remains in \(\{0,\dots,D\}^n\), the new slab
\(R_{\mathbf r+e_i}\setminus R_{\mathbf r}\) contains
\(\prod_{j\ne i}(r_j+1)\) cells. Every such cell \(C_{\mathbf u}\) has
\(m_{\mathbf u}=\theta S_{\mathbf u}\le\theta S_{\mathbf r+e_i}\). Hence
\[
S_{\mathbf r+e_i}
\le
S_{\mathbf r}
+
\theta\prod_{j\ne i}(r_j+1)\,S_{\mathbf r+e_i}.
\]
By the choice of \(D\),
\[
S_{\mathbf r+e_i}\le \frac43 S_{\mathbf r}.
\]
Iteration gives
\[
\frac{S_{\mathbf r}}{S_{\mathbf u}}
\le
\left(\frac43\right)^{|\mathbf r-\mathbf u|_1}
\qquad(\mathbf u\le\mathbf r).
\]

### Anchored rectangles

For \(\mathbf u\le\mathbf r\),
\[
\frac{|C_{\mathbf u}|}{|R_{\mathbf r}|}
\le 2^{-|\mathbf r-\mathbf u|_1},
\]
and \(m_{\mathbf u}\ge\theta S_{\mathbf u}\), including \(\mathbf u=\mathbf0\)
because \(\theta\le1\). Therefore
\[
\begin{aligned}
\langle w\rangle_{R_{\mathbf r}}
\langle\sigma\rangle_{R_{\mathbf r}}^{p-1}
&=
\sum_{\mathbf u\le\mathbf r}
\left(\frac{|C_{\mathbf u}|}{|R_{\mathbf r}|}\right)^p
\left(\frac{S_{\mathbf r}}{m_{\mathbf u}}\right)^{p-1}\\
&\le
\theta^{1-p}
\sum_{\mathbf u\le\mathbf r}
2^{-p|\mathbf r-\mathbf u|_1}
\left(\frac43\right)^{(p-1)|\mathbf r-\mathbf u|_1}\\
&\le C_{n,p}\theta^{1-p}.
\end{aligned}
\]
The last sum converges uniformly because
\[
2^{-p}\left(\frac43\right)^{p-1}<1
\qquad(p>1).
\]

Lerner's one-dimensional averaging lemma applies coordinate by coordinate:
for every interval \(J\subset[0,1)\) there is an anchored interval \(P_r\),
depending only on \(J\), such that every nonnegative function constant on the
\(I_u\) satisfies
\[
\langle g\rangle_J\le4\langle g\rangle_{P_r}.
\]
Applying it successively in all \(n\) coordinates, to both \(w\) and \(\sigma\),
shows
\[
[w]_{A_p^{\mathrm{str}}([0,1)^n)}
\le C_{n,p}\theta^{1-p}.
\]

For the reverse estimate, \(R_{e_1}\) is the union of two equal-volume cells.
Their \(\sigma\)-masses are \(1\) and \(t=\theta/(1-\theta)\). Hence
\[
\langle w\rangle_{R_{e_1}}
\langle\sigma\rangle_{R_{e_1}}^{p-1}
=
2^{-p}(1+t^{1-p})(1+t)^{p-1}
\gtrsim_p \theta^{1-p}.
\]
Thus the local characteristic is comparable to \(\theta^{1-p}\).

## A large hyperbolic family with bounded cumulative mass

From the definition,
\[
S_{\mathbf r}
=
1+\theta
\sum_{\substack{\mathbf0<\mathbf u\le\mathbf r}}S_{\mathbf u}.
\]
Let
\[
N_{\mathbf r}=\prod_{i=1}^n(r_i+1)-1.
\]
Since \(S_{\mathbf u}\le S_{\mathbf r}\) for \(\mathbf u\le\mathbf r\),
\[
S_{\mathbf r}\le1+\theta N_{\mathbf r}S_{\mathbf r}.
\]
Therefore
\[
\theta\prod_{i=1}^n(r_i+1)\le\frac12
\quad\Longrightarrow\quad
S_{\mathbf r}\le2.
\]

Define
\[
\mathcal H_\theta
=
\left\{
\mathbf r\in\{1,\dots,D\}^n:
\theta\prod_{i=1}^n(r_i+1)\le\frac12
\right\}.
\]
Then
\[
\#\mathcal H_\theta
\gtrsim_n
\theta^{-1}
\left(\log\frac1\theta\right)^{n-1}.
\]

For completeness, here is an elementary count. Put \(m=n-1\). For the first
\(m\) coordinates let
\[
P=\prod_{i=1}^{m}(r_i+1).
\]
Restrict to
\[
\frac{1}{8\theta D}\le P\le\frac{1}{16\theta}.
\]
For every such choice, at least \(c/(\theta P)\) integers \(r_n\in[1,D]\)
satisfy
\[
r_n\le\frac{1}{8\theta P},
\]
and then
\(\theta P(r_n+1)\le1/4\).
Because \(D^m\asymp_n\theta^{-1}\), a dyadic decomposition of
\([1,D]^m\) gives
\[
\sum_{\substack{1\le r_i\le D\\
(8\theta D)^{-1}\le P\le(16\theta)^{-1}}}
\frac1P
\gtrsim_n(\log D)^m.
\]
Indeed, each dyadic box contributes a constant amount to this harmonic sum,
and the admissible exponent vectors occupy a fixed positive-volume simplex
inside an \(m\)-dimensional box of side \(\asymp\log D\).
Multiplying by \(c/\theta\) yields the claimed cardinality.

## Testing the maximal operator

Let \(Q=C_{\mathbf0}\) and
\[
f_\theta=\sigma\,\mathbf1_Q.
\]
Since \(w=\sigma^{1-p}\) and \(\sigma(Q)=1\),
\[
\|f_\theta\|_{L^p(w;[0,1)^n)}^p
=
\int_Q\sigma^p w
=
\sigma(Q)
=1.
\]

For \(x\in C_{\mathbf r}\), the anchored rectangle \(R_{\mathbf r}\) contains
both \(x\) and \(Q\), so
\[
M_{\mathrm s}f_\theta(x)
\ge\frac1{|R_{\mathbf r}|}.
\]
If all \(r_i\ge1\), then
\[
|C_{\mathbf r}|=2^{-n}|R_{\mathbf r}|,
\qquad
w(C_{\mathbf r})
=
|C_{\mathbf r}|^p m_{\mathbf r}^{1-p}.
\]
Consequently
\[
\int_{C_{\mathbf r}}(M_{\mathrm s}f_\theta)^p\,w
\ge
2^{-np}\theta^{1-p}S_{\mathbf r}^{1-p}.
\]
For \(\mathbf r\in\mathcal H_\theta\), \(S_{\mathbf r}\le2\), hence each
such cell contributes at least \(c_{n,p}\theta^{1-p}\). The cells are
pairwise disjoint, so
\[
\begin{aligned}
\|M_{\mathrm s}f_\theta\|_{L^p(w;[0,1)^n)}^p
&\gtrsim_{n,p}
\theta^{1-p}\#\mathcal H_\theta\\
&\gtrsim_{n,p}
\theta^{-p}
\left(\log\frac1\theta\right)^{n-1}.
\end{aligned}
\]
Taking \(p\)-th roots gives the asserted local lower bound.

## Extension to \(\mathbb R^n\)

Let
\[
\pi(t)=\operatorname{dist}(t,2\mathbb Z)\in[0,1]
\]
and reflect \(w\) periodically in every coordinate:
\[
W(x_1,\dots,x_n)=w(\pi(x_1),\dots,\pi(x_n)).
\]
Lerner's reflection lemma says that for every interval \(J\subset\mathbb R\)
there is \(J_*\subset[0,1]\), depending only on \(J\), such that
\[
\frac1{|J|}\int_J g(\pi(t))\,dt
\le
\frac3{|J_*|}\int_{J_*}g
\]
for every nonnegative \(g\). Applying this in \(n\) coordinates to both
\(W\) and its dual weight gives
\[
[W]_{A_p^{\mathrm{str}}(\mathbb R^n)}
\lesssim_{n,p}\theta^{1-p}.
\]
The local lower bound for the characteristic survives, as does the testing
lower bound, since the test function may be supported in the original unit cube.
This completes the proof.

## Interpretation and limitations

The logarithmic exponent
\[
\frac{n-1}{p}
\]
comes from an \(n\)-parameter divisor-type count: the family of anchored
rectangles whose cumulative dual mass remains bounded has cardinality
\(\theta^{-1}(\log(1/\theta))^{n-1}\). The construction therefore reveals a
dimension-amplified obstruction rather than merely tensoring the planar example.

This result does **not** determine the optimal power exponent of
\([w]_{A_p^{\mathrm{str}}}\), does not give a matching upper logarithmic factor,
and does not address the weighted weak-type norm. Constants depend on \(n,p\).
Originality is asserted only to the best of our knowledge.

## References

1. A. K. Lerner, *Failure of the linear \(A_2\) bound for the strong maximal operator*, arXiv:2609.14008v1 (2026). https://arxiv.org/abs/2609.14008
2. S. Ombrosi and G. Rey, *Improved weighted bounds for the strong maximal function*, arXiv:2609.17246v1 (2026). https://arxiv.org/abs/2609.17246
3. T. Luque, C. Pérez, and E. Rela, *Reverse Hölder property for strong weights and general measures*, J. Geom. Anal. 27 (2017), 162–182. https://doi.org/10.1007/s12220-016-9678-y
