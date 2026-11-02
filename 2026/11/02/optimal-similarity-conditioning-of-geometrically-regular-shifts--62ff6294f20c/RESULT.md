# Optimal similarity conditioning of geometrically regular shifts and its dilogarithmic crossover

## Finding

For a geometrically regular weighted unilateral shift with parameters \(b>1\) and \(N,D\in(-1,1)\), the smallest condition number of a bounded invertible similarity to the unweighted unilateral shift is

\[
\kappa_*(W,S)=\max\{P,P^{-1}\},\qquad
P=\left[\frac{(-N;q)_\infty}{(-D;q)_\infty}\right]^{1/2},\qquad q=b^{-1},
\]

where \((a;q)_\infty=\prod_{j=0}^{\infty}(1-aq^j)\). A positive diagonal intertwiner attains the minimum among **all**, including non-diagonal, invertible intertwiners.

For fixed distinct \(N,D\), writing \(h=\log b\),

\[
\log\kappa_*(W,S)=
\frac{|\operatorname{Li}_2(-D)-\operatorname{Li}_2(-N)|}{2h}
+\frac14\left|\log\frac{1+N}{1+D}\right|+O_{N,D}(h)
\quad (h\downarrow0).
\]

There is also a sharp critical scaling: fixing \(d\in(-1,1)\), taking \(D=d\) and \(N=d+\tau h\) for any fixed real \(\tau\),

\[
\lim_{h\downarrow0}\kappa_*(W,S)
=\exp\!\left(\frac{|\tau|}{2}\frac{\log(1+d)}{d}\right),
\]

where the quotient at \(d=0\) is understood as \(1\). Thus an exponentially ill-conditioned fixed-parameter similarity crosses over to a finite nontrivial limit when the numerator and denominator parameters coalesce on the \(\log b\) scale.

## Assumptions and scope

Work on the complex Hilbert space \(\ell^2(\mathbb N_0)\) with standard orthonormal basis \((e_j)_{j\geq0}\). Let \(Se_j=e_{j+1}\), and let \(We_j=\alpha_j e_{j+1}\) with

\[
\alpha_j=\left(\frac{b^j+N}{b^j+D}\right)^{1/2}
=\left(\frac{1+Nq^j}{1+Dq^j}\right)^{1/2},\quad b>1,\quad q=b^{-1}\in(0,1),\quad -1<N,D<1.
\]

All weights are strictly positive. The similarity invariant is

\[
\kappa_*(W,S)=\inf\bigl\{\|X\|\,\|X^{-1}\|:\ X\text{ is bounded and invertible},\ WX=XS\bigr\}.
\]

The parameters and the exponent are real. For \(N=D\), the shift is \(S\), so \(\kappa_*=1\) and the singular-asymptotic formula reduces identically to zero.

## Proof

**1. A bounded positive diagonal similarity.** Put \(\beta_0=1\) and \(\beta_k=\prod_{j=0}^{k-1}\alpha_j\) for \(k\geq1\). Because \(\log\alpha_j=O(q^j)\), the products converge to a finite \(P>0\). The diagonal operator \(Xe_j=\beta_j e_j\) is bounded and boundedly invertible; moreover \(WXe_j=\beta_j\alpha_j e_{j+1}=\beta_{j+1}e_{j+1}=XSe_j\).

**2. Optimality against arbitrary intertwiners.** If \(N>D\), then every \(\alpha_j>1\) and \(\alpha_j\) strictly decreases with \(j\). Consequently \(\beta_k\) increases from \(1\) to \(P\), and for each positive integer \(k\) the operator norm of the weighted \(k\)-step shift is

\[
\|W^k\|=\sup_{m\geq0}\prod_{j=m}^{m+k-1}\alpha_j=\beta_k.
\]

Every invertible intertwiner satisfies \(W^k=XS^kX^{-1}\), hence \(\|X\|\,\|X^{-1}\|\geq\|W^k\|=\beta_k\); letting \(k\to\infty\) proves \(\kappa_*\geq P\). The constructed diagonal \(X\) has \(\|X\|=P\) and \(\|X^{-1}\|=1\), establishing equality.

If \(N<D\), all \(\alpha_j<1\) and \(\alpha_j\) strictly increases with \(j\). The minimum modulus \(m(T)=\inf_{\|x\|=1}\|Tx\|\) obeys

\[
m(W^k)=\inf_{m\geq0}\prod_{j=m}^{m+k-1}\alpha_j=\beta_k.
\]

Since \(S^k\) is an isometry, \(m(XS^kX^{-1})\geq(\|X\|\,\|X^{-1}\|)^{-1}\). Consequently \(\|X\|\,\|X^{-1}\|\geq\beta_k^{-1}\) for all \(k\), and the lower bound tends to \(P^{-1}\). The same diagonal operator has \(\|X\|=1\) and \(\|X^{-1}\|=P^{-1}\), giving equality. The case \(N=D\) is immediate. This also proves the infinite-product expression by factoring \(b^j\) out of every weight.

**3. Singular dilogarithmic law.** Put \(h=\log b\), so \(q=e^{-h}\), and define

\[
f(x)=\log\frac{1+Ne^{-x}}{1+De^{-x}}.
\]

This function and its first two derivatives are continuous and integrable on \([0,\infty)\), and Euler–Maclaurin summation with an integrable second derivative yields

\[
\log P=\frac12\sum_{j=0}^{\infty}f(jh)=
\frac1{2h}\int_0^\infty f(x)\,dx+\frac{f(0)}4+O_{N,D}(h).
\]

The absolutely convergent real dilogarithm identity on \((-1,1)\) gives

\[
\int_0^\infty f(x)\,dx=\operatorname{Li}_2(-D)-\operatorname{Li}_2(-N).
\]

The integral and \(f(0)\) have the same sign as \(N-D\), so taking the absolute value gives the stated expansion of \(\log\kappa_*\).

**4. Critical crossover.** With \(D=d\), \(N=d+\tau h\), uniformly as \(h\downarrow0\),

\[
f_h(x)=\tau h\frac{e^{-x}}{1+de^{-x}}+O_d(h^2e^{-2x}).
\]

Summing over \(x=jh\) produces

\[
\log P=\frac{\tau}{2}\int_0^\infty\frac{e^{-x}}{1+de^{-x}}\,dx+O_{d,\tau}(h)
=\frac{\tau}{2}\frac{\log(1+d)}d+O_{d,\tau}(h).
\]

The integral equals \(1\) at \(d=0\). Taking its absolute value proves the claimed limit.

## Verification

The standalone file `verify_similarity.py` performs exact rational comparisons of every sampled \(k\)-step block against its initial block, for 7,350 parameter and block cases, including both monotonicity directions and equality. It also performs 12 numerical diagnostics for the two-term dilogarithm expansion. Run with `python verify_similarity.py` (standard library only). These finite checks verify implementations and examples, not the unrestricted results, which follow from the proof above.

## Relationship to prior work

Benhida, Curto and Exner introduced and systematically studied the same geometrically regular shift family, primarily classifying moment-infinite divisibility, subnormality, hyperexpansivity and hyponormality. Their definition and prior classifications are not claimed as new. Shields's classical similarity criterion, as reproduced in Hou, Ji and Xu, decides whether two unilateral weighted shifts are similar using uniform bounds on products of corresponding weights; it does **not itself determine the least norm-condition product among all intertwiners**. The present statement identifies that sharp invariant for this family, and provides a dilogarithmic singular law and a critical parameter-crossover limit. A follow-up paper on safe quotients in the same shift family addresses subnormal and moment-divisibility properties, but full-text comparison remained limited.

## Limitations

The exact optimization relies essentially on monotonicity of the positive weights and does not extend as stated to arbitrary nonmonotone weighted shifts or pairwise comparison of two arbitrary shifts. The asymptotic error for fixed \(N,D\) is not asserted uniform up to the boundary \(N=-1\) or \(D=-1\). The critical-scaling claim fixes \(d\in(-1,1)\) and \(\tau\) while \(h\downarrow0\). The similarity criterion is longstanding and the result may have an earlier formulation under diagonal-conjugacy or weighted Hardy-space terminology. Independent mathematical assessment has not been performed.

## References

1. C. Benhida, R. E. Curto and G. R. Exner, *Geometrically regular weighted shifts*, arXiv:2309.05888 (first posted September 12, 2023), Sections 1–2; https://arxiv.org/abs/2309.05888 .
2. Y. Hou, S. Ji and J. Xu, *On the N-hypercontractions and similarity of multivariable weighted shifts*, arXiv:2208.08387 (2022), Introduction, Lemma 1.2 and references to Shields (1974); https://arxiv.org/abs/2208.08387 .
3. C. Benhida, R. E. Curto and G. R. Exner, *MID and safe quotients for GRWS*, arXiv:2312.06390 (2023), abstract; https://arxiv.org/abs/2312.06390 .
4. A. L. Shields, *Weighted shift operators and analytic function theory*, Mathematical Surveys 13, AMS, 1974; referenced via Hou–Ji–Xu.
