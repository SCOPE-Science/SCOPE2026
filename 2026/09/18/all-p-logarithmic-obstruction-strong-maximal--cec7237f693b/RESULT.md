# All-p logarithmic obstruction to the Buckley endpoint power for the strong maximal operator

## Statement

Let \(1<p<\infty\) and \(d\ge 2\). Let \(M_{\mathrm s}\) be the strong maximal operator on \(\mathbb R^d\), and let
\[
[w]_{A_p^{\mathrm{str}}}
=
\sup_R \langle w\rangle_R
\left\langle w^{-1/(p-1)}\right\rangle_R^{p-1},
\]
where the supremum is over bounded axis-parallel rectangles.

There are constants \(c_p,C_p>0\) and, for every sufficiently small \(\theta>0\), weights
\(w_\theta\in A_p^{\mathrm{str}}(\mathbb R^d)\) such that
\[
c_p\theta^{-(p-1)}
\le [w_\theta]_{A_p^{\mathrm{str}}}
\le C_p\theta^{-(p-1)}
\]
and
\[
\|M_{\mathrm s}\|_{L^p(w_\theta)\to L^p(w_\theta)}
\ge
c_p\,\theta^{-1}\left(\log\frac1\theta\right)^{1/p}.
\]
Equivalently, along this family,
\[
\boxed{
\|M_{\mathrm s}\|_{L^p(w_\theta)\to L^p(w_\theta)}
\gtrsim_p
[w_\theta]_{A_p^{\mathrm{str}}}^{1/(p-1)}
\bigl(\log [w_\theta]_{A_p^{\mathrm{str}}}\bigr)^{1/p}.
}
\]

Consequently, for every \(1<p<\infty\) and every \(d\ge2\), there is no uniform estimate
\[
\|M_{\mathrm s}\|_{L^p(w)\to L^p(w)}
\le C_{p,d}[w]_{A_p^{\mathrm{str}}}^{1/(p-1)}.
\]
For \(p=2\) this is Lerner's 2026 theorem. The new content is the extension to every
\(p\in(1,\infty)\), with the explicit logarithmic lower factor above.

This does **not** imply that the infimum of admissible pure-power exponents is strictly larger than \(1/(p-1)\): a logarithm is smaller than every positive power. It shows that the endpoint power itself is unattainable as a uniform pure-power bound.

## Context

Buckley's one-parameter theorem gives the sharp estimate
\[
\|M\|_{L^p(w)\to L^p(w)}
\lesssim_{p,d}
[w]_{A_p}^{1/(p-1)}.
\]
For the strong maximal operator the sharp dependence on the rectangular \(A_p\) characteristic remains open.

Lerner recently constructed, in dimension two and at \(p=2\), weights with
\[
[w_\theta]_{A_2^{\mathrm{str}}}\asymp \theta^{-1},\qquad
\|M_{\mathrm s}\|_{L^2(w_\theta)\to L^2(w_\theta)}
\gtrsim
\theta^{-1}\sqrt{\log(1/\theta)}.
\]
His paper explicitly restricts the argument to \(p=2\). A subsequent all-\(p\) upper-bound paper of Ombrosi--Rey cites precisely this \(p=2\) lower obstruction while improving known upper exponents for every \(p\).

The observation here is that Lerner's mass recurrence has a natural \(A_p\) realization:
keep the same positive density \(\sigma\), but replace the reciprocal weight by
\[
w=\sigma^{-(p-1)}.
\]
The two estimates in the construction then scale with exactly the powers needed for all \(p\).

## Proof in dimension two

We retain the geometric partition and mass recurrence from Lerner's construction, and include the required estimates to make the \(p\)-dependence explicit.

Fix
\[
0<\theta<1/256,\qquad c_0=\frac1{32},\qquad
D=\left\lfloor\frac{c_0}{\theta}\right\rfloor,\qquad a=2^{-D}.
\]
Partition \([0,1)\) into
\[
I_0=[0,a),\qquad I_r=[2^{r-1}a,2^ra),\quad 1\le r\le D.
\]
Set
\[
C_{r,s}=I_r\times I_s,\qquad
P_r=[0,2^ra),\qquad R_{r,s}=P_r\times P_s.
\]
Then, for \(u\le r\), \(v\le s\),
\[
\frac{|C_{u,v}|}{|R_{r,s}|}
\le 2^{-(r-u)-(s-v)},
\]
and for \(r,s\ge1\),
\[
|C_{r,s}|=\frac14|R_{r,s}|.
\]

Define
\[
T_{r,s}=\sum_{k\ge0}\binom rk\binom sk\theta^k,\qquad
S_{r,s}=(1-\theta)^{-(r+s)}T_{r,s},
\]
and cell masses
\[
m_{0,0}=1,\qquad m_{r,s}=\theta S_{r,s}
\quad((r,s)\ne(0,0)).
\]
The recurrence implies
\[
\sum_{u\le r,\ v\le s}m_{u,v}=S_{r,s}.
\]
Let \(\sigma\) be constant on each cell with
\[
\sigma|_{C_{r,s}}=\frac{m_{r,s}}{|C_{r,s}|},
\]
and define the \(p\)-dependent weight
\[
\boxed{w_\theta=\sigma^{-(p-1)}}.
\]
Thus \(w_\theta^{-1/(p-1)}=\sigma\).

### 1. The rectangular \(A_p\) characteristic

Lerner's recurrence gives the uniform growth estimate
\[
\frac{S_{r,s}}{S_{u,v}}
\le
\kappa^{(r-u)+(s-v)},\qquad \kappa=\frac32,
\]
for \(u\le r\), \(v\le s\), and also \(m_{u,v}\ge \theta S_{u,v}\).

Since
\[
w_\theta(C_{u,v})
=
|C_{u,v}|
\left(\frac{m_{u,v}}{|C_{u,v}|}\right)^{-(p-1)}
=
\frac{|C_{u,v}|^p}{m_{u,v}^{p-1}},
\]
we obtain on an anchored rectangle
\[
\begin{aligned}
\langle w_\theta\rangle_{R_{r,s}}
\langle \sigma\rangle_{R_{r,s}}^{p-1}
&=
\frac{S_{r,s}^{p-1}}{|R_{r,s}|^p}
\sum_{u\le r,\ v\le s}
\frac{|C_{u,v}|^p}{m_{u,v}^{p-1}}\\
&\le
\theta^{-(p-1)}
\sum_{u\le r,\ v\le s}
\left(\frac{S_{r,s}}{S_{u,v}}\right)^{p-1}
\left(\frac{|C_{u,v}|}{|R_{r,s}|}\right)^p\\
&\le
\theta^{-(p-1)}
\sum_{i,j\ge0}
\left(\frac{\kappa^{p-1}}{2^p}\right)^{i+j}.
\end{aligned}
\]
The ratio is strictly less than one for every \(p>1\), because
\[
\frac{\kappa^{p-1}}{2^p}
=
\frac{3^{p-1}}{2^{2p-1}}
<1.
\]
Hence the anchored \(A_p\) characteristic is \(O_p(\theta^{-(p-1)})\).

Lerner's averaging lemma says that every average of a nonnegative cell-constant function over an arbitrary rectangle in the unit square is at most \(16\) times an average over a suitable anchored rectangle, with the same anchored rectangle usable for both functions. Applying it to \(w_\theta\) and \(\sigma\) gives
\[
[w_\theta]_{A_p^{\mathrm{str}}([0,1]^2)}
\lesssim_p \theta^{-(p-1)}.
\]

For the reverse bound, \(R_{1,0}\) is the union of two equal-area cells. Their \(\sigma\)-masses are
\[
1,\qquad \frac{\theta}{1-\theta}.
\]
A direct calculation gives
\[
\langle w_\theta\rangle_{R_{1,0}}
\langle \sigma\rangle_{R_{1,0}}^{p-1}
=
\frac{
1+\left(\frac{1-\theta}{\theta}\right)^{p-1}
}{
2^p(1-\theta)^{p-1}
}
\ge 2^{-p}\theta^{-(p-1)}.
\]
Therefore
\[
[w_\theta]_{A_p^{\mathrm{str}}([0,1]^2)}
\asymp_p \theta^{-(p-1)}.
\]

### 2. The maximal-function lower bound

Let \(Q=C_{0,0}\) and test with
\[
f_\theta=\sigma\mathbf 1_Q.
\]
Because \(w_\theta=\sigma^{-(p-1)}\),
\[
\|f_\theta\|_{L^p(w_\theta;[0,1]^2)}^p
=
\int_Q \sigma^p\sigma^{-(p-1)}
=
\sigma(Q)=1.
\]

For \(x\in C_{r,s}\), the rectangle \(R_{r,s}\) contains both \(x\) and \(Q\), so
\[
M_{\mathrm s}f_\theta(x)\ge \frac1{|R_{r,s}|}.
\]
When \(r,s\ge1\),
\[
w_\theta(C_{r,s})
=
\frac{|C_{r,s}|^p}{(\theta S_{r,s})^{p-1}}
=
\frac{|R_{r,s}|^p}{4^p\theta^{p-1}S_{r,s}^{p-1}}.
\]
Consequently
\[
\int (M_{\mathrm s}f_\theta)^p w_\theta
\ge
\frac1{4^p\theta^{p-1}}
\sum_{r,s=1}^D S_{r,s}^{-(p-1)}.
\]

On the hyperbolic region
\[
1\le r,s\le D,\qquad rs\le D,
\]
Lerner's elementary estimate gives \(S_{r,s}<2\). The number of such pairs is
\[
\sum_{r=1}^D\left\lfloor\frac Dr\right\rfloor
\gtrsim D\log D
\asymp \theta^{-1}\log\frac1\theta.
\]
Therefore
\[
\int (M_{\mathrm s}f_\theta)^p w_\theta
\gtrsim_p
\theta^{-p}\log\frac1\theta,
\]
and, since \(\|f_\theta\|_{L^p(w_\theta)}=1\),
\[
\|M_{\mathrm s}\|_{L^p(w_\theta)\to L^p(w_\theta)}
\gtrsim_p
\theta^{-1}\left(\log\frac1\theta\right)^{1/p}.
\]

### 3. Extension from the square to \(\mathbb R^2\)

Let
\[
\pi(t)=\operatorname{dist}(t,2\mathbb Z)\in[0,1]
\]
and extend
\[
W_\theta(x,y)=w_\theta(\pi(x),\pi(y)).
\]
For every bounded interval \(J\subset\mathbb R\), there is an interval
\(J_*\subset[0,1]\), depending only on \(J\), such that every nonnegative \(g\) satisfies
\[
\frac1{|J|}\int_J g(\pi(t))\,dt
\le
\frac3{|J_*|}\int_{J_*}g.
\]
Applying this in both coordinates to \(w_\theta\) and to its dual weight \(\sigma\) yields
\[
[W_\theta]_{A_p^{\mathrm{str}}(\mathbb R^2)}
\le
9^p [w_\theta]_{A_p^{\mathrm{str}}([0,1]^2)}.
\]
The reverse characteristic bound and the maximal-function test remain valid on the original unit square. Thus the theorem holds on \(\mathbb R^2\).

## Extension to every dimension \(d\ge2\)

For \(d>2\), set
\[
\widetilde W_\theta(x_1,\dots,x_d)=W_\theta(x_1,x_2).
\]
The extra coordinates factor out of rectangular averages, so
\[
[\widetilde W_\theta]_{A_p^{\mathrm{str}}(\mathbb R^d)}
=
[W_\theta]_{A_p^{\mathrm{str}}(\mathbb R^2)}.
\]
If
\[
F_\theta(x)
=
f_\theta(x_1,x_2)\prod_{j=3}^d\mathbf1_{[0,1]}(x_j),
\]
then on \((0,1)^{d-2}\) in the extra coordinates one may choose the rectangle factors
\([0,1]\), giving
\[
M_{\mathrm s}^{(d)}F_\theta
\ge
M_{\mathrm s}^{(2)}f_\theta.
\]
The input and lower-output norms factor, proving the same lower bound in every \(d\ge2\).

## Adversarial checks

- The geometric series in the \(A_p\) estimate converges for the entire range \(1<p<\infty\):
  \[
  3^{p-1}/2^{2p-1}<1.
  \]
- The dual weight is exactly \(\sigma\), so the input normalization is exact rather than asymptotic.
- The lower \(A_p\) estimate is explicit on \(R_{1,0}\) and has the same \(\theta^{-(p-1)}\) scale as the upper bound.
- The logarithmic factor comes from the cardinality of the hyperbolic set \(rs\le D\); no limiting interchange or numerical estimate is used.
- Passing to dimensions \(d>2\) neither changes the rectangular characteristic nor weakens the two-dimensional test.
- At \(p=2\) the construction reduces to Lerner's weight and reproduces his theorem, providing a consistency check.

## Relation to prior results and originality scope

Lerner's arXiv:2609.14008v1 proves the \(p=2\), \(d=2\) case and explicitly says that, for simplicity and clarity, the paper concentrates on that case. Ombrosi--Rey, arXiv:2609.17246, prove improved all-\(p\), all-dimensional upper bounds and cite Lerner's lower result specifically at \(p=2\). Luque--Pérez--Rela had earlier identified the direct Buckley-type question for strong weights as open.

Exact and synonymous searches for an all-\(p\) logarithmic lower obstruction, rectangular \(A_p\) endpoint counterexamples, and extensions of Lerner's mass recurrence did not locate the theorem above. The current SCOPE archive was also searched by object, source identifier, and equivalent terminology without finding an overlap.

Accordingly, the originality claim is limited to the \(p\ne2\) extension and its all-dimensional consequence, together with the explicit lower rate
\[
A^{1/(p-1)}(\log A)^{1/p}.
\]
The \(p=2\) construction, the mass recurrence itself, the averaging lemma, and the reflection device are Lerner's prior work and are not claimed as new.

Because the principal source and the follow-up upper-bound paper are both very recent, unindexed simultaneous observations remain a residual originality risk.

## Limitations

1. The result rules out the endpoint **pure-power estimate**, but does not prove that the infimum power exponent \(\alpha_p\) exceeds \(1/(p-1)\).
2. The logarithmic exponent \(1/p\) is a lower bound produced by this family; no claim is made that it is the optimal slowly varying correction.
3. The construction concerns the strong maximal operator over all axis-parallel rectangles. It does not by itself give analogous lower bounds for other multiparameter operators.
4. No endpoint \(p=1\) assertion is made.

## References

1. Andrei K. Lerner, *Failure of the linear \(A_2\) bound for the strong maximal operator*, arXiv:2609.14008v1 (2026). https://arxiv.org/abs/2609.14008
2. Sheldy Ombrosi and Guillermo Rey, *Improved weighted bounds for the strong maximal function*, arXiv:2609.17246 (2026). https://arxiv.org/abs/2609.17246
3. Teresa Luque, Carlos Pérez, and Ezequiel Rela, *Reverse Hölder Property for strong weights and general measures*, J. Geom. Anal. 27 (2017), 162--182; arXiv:1512.01112. https://arxiv.org/abs/1512.01112

Same-model review: passed. Cross-model review: not yet performed.
