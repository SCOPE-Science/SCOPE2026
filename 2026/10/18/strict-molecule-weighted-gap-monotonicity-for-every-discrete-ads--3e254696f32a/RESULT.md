# Strict molecule-weighted gap monotonicity for every discrete adsorption length

## Finding

For every integer \(k\geq2\), consider one-dimensional random sequential adsorption of nonoverlapping consecutive \(k\)-site rods on an initially vacant integer segment, with each admissible rod selected uniformly at each placement until no further placement is possible. For \(0\leq l\leq k-1\), let \(g_{k,l}\) be the limiting expected number of maximal vacant gaps of size \(l\), divided by segment length, as the segment grows. Then

\[
0\,g_{k,0}<1\,g_{k,1}<2\,g_{k,2}<\cdots<(k-1)g_{k,k-1}.
\]

Equivalently, for every integer \(k\geq2\) and \(0\leq l\leq k-2\),

\[
(l+1)g_{k,l+1}-l g_{k,l}>0.
\]

The full quantified range is essential: prior finite certificates establish the conclusion for \(2\leq k\leq20\), whereas the present analytic argument covers every integer \(k\), including \(k\geq21\), without finite parameter enumeration.

## Assumptions and scope

The sequential adsorption model and the existence of its limiting densities are those of Pinsky, Theorem 2 (2026), following earlier work on gap counts. That theorem gives the exact integral

\[
g_{k,l}=2\int_0^1(1-s)s^l W_k(s)\,ds,\qquad
W_k(s)=\exp\!\left(2\sum_{j=1}^{k-1}\frac{s^j-1}{j}\right).
\]

For the argument, the integral is a well-defined positive quantity for all integers \(l\geq0\); **only** indices \(0\leq l\leq k-1\) represent physical terminal-gap densities. Throughout, \(k\) is a fixed integer at least two; no assertion about a model with an infinite rod length is required.

## Proof

**1. An exact sign identity.** Define \(I_{k,l}=\int_0^1(1-s)s^l W_k(s)\,ds\) for integers \(l\geq0\). Direct logarithmic differentiation gives

\[
\frac{W_k'(s)}{W_k(s)}
=2\sum_{j=0}^{k-2}s^j
=\frac{2(1-s^{k-1})}{1-s}.
\]

For \(l\geq0\), the function \(s^{l+1}(1-s)^2W_k(s)\) vanishes at both endpoints. Differentiating it and integrating over \([0,1]\) yields

\[
0=\int_0^1s^l(1-s)W_k(s)
\bigl((l+1)(1-s)-2s^k\bigr)\,ds.
\]

Because \((l+1)s-l=1-(l+1)(1-s)\), substitution into the defining integrals proves the exact identity

\[
\Delta_{k,l}:=(l+1)g_{k,l+1}-l g_{k,l}
=2\int_0^1s^l(1-s)W_k(s)(1-2s^k)\,ds.\tag{1}
\]

The identity in (1), or an equivalent moment reduction, also appears in prior literature. The new contribution is the following parameter-uniform positivity proof.

**2. The reflected-kernel inequality.** Substitute \(y=s^k\) and define on \(0<y<1\)

\[
h_k(y)=\frac{1-y^{1/k}}{y^{1/k}}W_k(y^{1/k}),
\qquad r_{k,l}(y)=y^{(l-k+2)/k}.
\]

Then (1) becomes

\[
\Delta_{k,l}=\frac2k\int_0^1(1-2y)h_k(y)r_{k,l}(y)\,dy.\tag{2}
\]

We prove, for **every** integer \(k\geq2\),

\[
h_k(y)>h_k(1-y)\quad(0<y<1/2).\tag{3}
\]

Write \(L_k(y)=\frac{d}{dy}\log h_k(y)\). Using the derivative of \(W_k\), with \(s=y^{1/k}\), gives the *exact* identity

\[
k y L_k(y)=-2+\frac{1-2y}{1-y^{1/k}}.
\]

Set \(G_k(y)=\log h_k(y)-\log h_k(1-y)\). Differentiating (including the minus sign from the reflected argument), and writing \(t=(1-y)^{1/k}\), gives

\[
\begin{aligned}
k y(1-y)G_k'(y)
&=-2+(1-2y)\left(\frac{1-y}{1-s}-\frac{y}{1-t}\right)\\
&=-2+(1-2y)\sum_{j=0}^{k-1}(s^j-t^j).\tag{4}
\end{aligned}
\]

The second equality uses \(1-y=1-s^k\) and \(y=1-t^k\). For \(0<y<1/2\), we have \(s<t\). Every summand in (4) is nonpositive, while \(1-2y>0\). Thus \(G_k'(y)<0\). Since \(G_k(1/2)=0\), integration from \(y\) to \(1/2\) gives \(G_k(y)>0\), proving (3). No numerical bound or large-\(k\) approximation is used.

**3. Reflection of the integral.** For the claimed range \(0\leq l\leq k-2\), the exponent \((l-k+2)/k\leq0\). Hence \(r_{k,l}\) is positive and nonincreasing. Combining this with the strict inequality (3) gives

\[
h_k(y)r_{k,l}(y)>
 h_k(1-y)r_{k,l}(1-y),
\qquad 0<y<1/2.
\]

Splitting (2) at \(1/2\) and replacing \(y\) by \(1-y\) in its upper half gives

\[
\Delta_{k,l}=
\frac2k\int_0^{1/2}(1-2y)
\left[h_k(y)r_{k,l}(y)-h_k(1-y)r_{k,l}(1-y)\right]dy>0.
\]

All integrals are finite: near zero, the product \(h_k(y)r_{k,l}(y)\) is asymptotic to a positive constant times \(y^{(l-k+1)/k}\), whose exponent exceeds \(-1\) for \(l\geq0\); near one, it is \(O(1-y)\). This proves the theorem for all \(k\) and all admissible \(l\). \(\square\)

## Verification

A standalone Python 3 standard-library checker is included as `check_gap.py`. It re-evaluates the geometric-sum derivative identities exactly with rational arithmetic, tests the sign calculation for selected arbitrary and large values of \(k\), and compares two independent integral representations for selected \(k\) and \(l\) using Simpson quadrature. It completed with `PASS: 1554 exact/algebraic/numerical assertions`. The infinite theorem is proved by the analytic reflected-kernel argument above; numerical assertions are finite consistency tests, not substitutes for proof.

## Relationship to prior work

Pinsky's 2026 preprint states the integral formula in Theorem 2 and explicitly identifies the monotonicity of \(l g_{k,l}\) as an unproved numerical observation after Table 1. A subsequent 2026 paper, *The bonded-molecule density of one-dimensional random sequential adsorption is decreasing in k, and an exact reduction for the gap densities*, proves this particular gap inequality by exact finite certificates for \(2\leq k\leq20\) (Theorem 7.1), gives the same underlying moment/integration-by-parts reduction, and explicitly leaves \(k\geq21\) open (section 1.4 and section 9.2). These finite-range results, the moment identity, and that paper's unrelated bonded-density monotonicity result are prior work, **not** claimed here. The independent contribution is the reflected-kernel argument (3)–(4) proving the gap inequality in the unbounded rod-length range. General reviews of one-dimensional adsorption do not supply this explicit parameter-uniform implication in the inspected material.

## Limitations

The result is about limiting *expected* gap densities in the usual sequential-adsorption model; it does not establish corresponding samplewise inequalities, finite-segment monotonicity, or rates of convergence as segment length grows. It makes no assertion that the inequality persists for formal integral indices beyond the physical range. The available literature search cannot exclude every unindexed or unpublished earlier proof; independent priority audit has not been performed.

## References

1. Ross G. Pinsky, *A new look at some aspects of one-dimensional random sequential adsorption and its continuum limit*, arXiv:2608.04730v1, first submitted 2026-08-05, https://arxiv.org/html/2608.04730v1 . Theorem 2 and the paragraph after Table 1.
2. *The bonded-molecule density of one-dimensional random sequential adsorption is decreasing in k, and an exact reduction for the gap densities*, 2026, https://ideosphere.ai/papers/pinsky-monotone-v2.pdf . Theorem 7.1 and sections 1.4 and 9.2.
3. J. W. Evans, *Random and cooperative sequential adsorption*, Reviews of Modern Physics **65** (1993), 1281–1329; general background only.
