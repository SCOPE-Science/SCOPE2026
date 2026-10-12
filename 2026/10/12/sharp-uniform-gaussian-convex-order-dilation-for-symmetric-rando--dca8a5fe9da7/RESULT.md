# Sharp uniform Gaussian convex-order dilation for symmetric random walks after two or three steps

## Finding
Let \(\varepsilon_1,\varepsilon_2,\ldots\) be independent symmetric signs, let \(S_n=n^{-1/2}\sum_{i=1}^n\varepsilon_i\), and let \(G\) be a standard Gaussian. Define \(\Phi\) and \(\varphi\) to be the standard normal distribution function and density, respectively. Put
\[
 c_2=\frac{\sqrt2}{4\varphi(\Phi^{-1}(3/4))}=1.1125848189719498\ldots,\qquad
 c_3=\frac{\sqrt{6\pi}}4=1.0854018818374014\ldots .
\]
For every integer \(n\ge2\) and every finite-valued convex function \(f:\mathbb R\to\mathbb R\) whose Gaussian expectation exists, one has \(\mathbb Ef(S_n)\le\mathbb Ef(c_2G)\). For **every integer \(n\ge3\)**, the strictly smaller constant \(c_3\) suffices. These are the **smallest possible constants uniform over the respective infinite sets of sample sizes**. The first bound is sharp already at \(n=2\) with a positive-part function, and the second already at \(n=3\) with \(f(x)=|x|\). Equivalently, \(S_n\preceq_{\rm cx}c_2G\) for all \(n\ge2\), and \(S_n\preceq_{\rm cx}c_3G\) for all \(n\ge3\).

## Assumptions and scope
All signs are mutually independent with probability \(1/2\) for each of \(\pm1\), and each normalized sum has mean zero and variance one. Convex-order comparisons are for all convex tests with finite right-hand expectation (and hold trivially when the right-hand expectation is \(+\infty\)); they do not assert stochastic dominance of upper-tail probabilities at each threshold. The Gaussian comparator has standard deviation \(c_j\), rather than matching variance. The sample-size lower limits are essential: \(n=1\) requires the larger optimal constant \(\sqrt{\pi/2}\).

## Proof
**1. Finite upper-quantile criterion.** For a centered integrable law \(X\), define its integrated upper quantile \(A_X(p)=\int_{1-p}^{1}Q_X(u)\,du\), \(0\le p\le1\). Centered laws \(X,Y\) satisfy \(X\preceq_{\rm cx}Y\) if and only if \(A_X(p)\le A_Y(p)\) for every \(p\in[0,1]\). Indeed, the right side controls the support function of all upper-tail events of mass \(p\) and is equivalent, by Legendre duality, to \(\mathbb E(X-t)_+\le\mathbb E(Y-t)_+\) for every real \(t\). Affine parts and positive hinges generate convex tests in the standard integral representation. For \(G\sim N(0,1)\), integration by parts yields \(A_{cG}(p)=cI(p)\), where \(I(p)=\varphi(\Phi^{-1}(p))\). Differentiation gives \(I''(p)=-1/I(p)<0\) on \((0,1)\). If \(X\) has a finite discrete law, \(A_X\) is affine between cumulative masses of its largest atoms. Since \(I\) is concave, it suffices to check each such mass. Symmetry reduces the comparison to \(0<p\le1/2\), since \(A_X(p)=A_X(1-p)\) and \(I(p)=I(1-p)\).

**2. A finite Gaussian comparison lemma.** The following cut-point table is obtained directly by listing the binomial atoms of \(S_n\). Each entry is \((p,A_{S_n}(p))\), with \(p\) increasing. It lists all nontrivial positive-atom endpoints at or below \(1/2\), including the middle endpoint when necessary:

| \(n\) | Cut points \((p,A_{S_n}(p))\) |
|---|---|
| 2 | \((1/4,\sqrt2/4)\), \((1/2,\sqrt2/4)\) |
| 3 | \((1/8,\sqrt3/8)\), \((1/2,\sqrt3/4)\) |
| 4 | \((1/16,1/8)\), \((5/16,3/8)\), \((1/2,3/8)\) |
| 5 | \((1/32,\sqrt5/32)\), \((3/16,\sqrt5/8)\), \((1/2,15/(16\sqrt5))\) |

Their exact values also follow from the binomial telescoping identity
\[
 \sum_{j=0}^{k}(n-2j){n\choose j}=n{n-1\choose k},\qquad 0\le k<n.
\]
Because the Gaussian profile \(I\) increases on \((0,1/2)\), when \(S_n\) has a zero atom the plateau from the last positive endpoint to \(1/2\) requires no extra inequality.

The noncentral endpoints for \(n=3,4,5\) satisfy the **strict inequalities** \(A_{S_n}(p)<c_3 I(p)\). Here is a fully rational verification of the only five needed Gaussian-profile estimates: use the rational upper bounds \(z_p\) on \(|\Phi^{-1}(p)|\) below and elementary upper bounds on the listed \(A\):

| \(p\) | \(z_p\) | Rational upper bound for \(A_{S_n}(p)\) |
|---|---|---|
| \(1/8\) | \(117/100\) | \(1733/8000\) |
| \(1/16\) | \(39/25\) | \(1/8\) |
| \(5/16\) | \(1/2\) | \(3/8\) |
| \(1/32\) | \(19/10\) | \(2237/32000\) |
| \(3/16\) | \(91/100\) | \(2237/8000\) |

For every row, the rational inequalities \(\int_0^{z_p}e^{-t^2/2}\,dt>\sqrt{2\pi}(1/2-p)\) and \(e^{-z_p^2/2}/\sqrt{2\pi}>A_{\rm upper}/(10853/10000)\) hold. Hence \(|\Phi^{-1}(p)|<z_p\) and \(I(p)>A_{\rm upper}/c_3\), because \(c_3>10853/10000\). The exact rational checker `verification/checker.py` proves all ten inequalities: it uses Machin's arctangent identity with alternating-series rational brackets for \(\pi\), bounds \(\sqrt{2\pi}\), and computes Taylor remainder bounds for the integrals and exponentials. At \(p=1/2\) for \(n=3\), one has exact equality \(\sqrt3/4=c_3/\sqrt{2\pi}\). At \(p=1/2\) for \(n=5\), \(15/(16\sqrt5)<\sqrt3/4\), equivalent to \(225<240\). The \(n=4\) midpoint lies on the plateau after \(p=5/16\). Thus \(S_n\preceq_{\rm cx}c_3G\) for \(n=3,4,5\).

For \(n=2\), the cut at \(p=1/4\) yields exactly \(c_2\). The \(p=1/2\) ratio is \(\sqrt\pi/2<c_3<c_2\), where the last inequality follows from the rational bounds \(0.64<|\Phi^{-1}(1/4)|\), \(c_3<1.0855\), and \(\sqrt2>1.4142\) certified by the same checker. Therefore \(S_2\preceq_{\rm cx}c_2G\).

**3. Tensorizing into arbitrarily long walks.** If independent centered \(U_i\preceq_{\rm cx}V_i\), then \(\sum_iU_i\preceq_{\rm cx}\sum_iV_i\), because conditioning and applying convex order one summand at a time preserves every convex test. For any \(n\ge3\), partition its \(n\) signs into disjoint blocks having sizes in \(\{3,4,5\}\): these sizes generate all integers at least three (subtract three repeatedly). A block of size \(m\) has distribution \(\sqrt m S_m\preceq_{\rm cx}c_3\sqrt mG_m\). Adding independent blocks and dividing by \(\sqrt n\) yields \(S_n\preceq_{\rm cx}c_3G\), since the independent Gaussian block contributions sum to a Gaussian of variance \(c_3^2\). Likewise every \(n\ge2\) can be partitioned into blocks of sizes \(2\) and \(3\), so the established two- and three-step bounds (with \(c_3<c_2\)) give \(S_n\preceq_{\rm cx}c_2G\).

**4. Sharpness.** The integrated-quantile comparison at \(n=2\), \(p=1/4\), forces \(c\ge\sqrt2/[4I(1/4)]=c_2\). Indeed the corresponding supporting hinge at \(t=c_2\Phi^{-1}(3/4)\) gives equality; any smaller \(c\) strictly violates an integrated-quantile inequality. At \(n=3\), \(p=1/2\), comparison forces \(c\ge (\sqrt3/4)/I(1/2)=c_3\), equivalently \(\mathbb E|S_3|=c_3\mathbb E|G|\). Hence both **uniform** constants are optimal.

## Verification
Run `python verification/checker.py` using Python's standard library. The checker performs exact rational arctangent/Taylor comparisons for all five noncentral cut points, a rational normal-quartile separation, positive-constant comparisons, and binomial cumulative-mean identities for all \(n\in\{2,3,4,5\}\). It reports `PASS: pi, Gaussian quantile brackets, 2/3/4/5-step tail cuts, c2>c3, combinatorial identities`. The infinite-family conclusion comes from the independent-block tensorization proof; no finite numerical sample is used as a substitute for the universal argument.

## Relationship to prior work
Zhang [1] established that **every** centered random variable whose moment-generating function is bounded by that of a standard Gaussian is convexly dominated by \(\sqrt{\pi/2}G\), with optimality witnessed by one symmetric sign. The present assertion concerns only the equal-weight averages of **at least two or at least three independent** signs, and establishes strictly smaller **sharp uniform constants**. The inequality in [1] alone does not imply either improvement. Davis–Power [2] proved a different universal comparison for the larger class defined by two-sided tail bounds and explained Gaussian-convex-order tensorization. Havrilla–Tkocz [3] proved sharp moment (Khinchin-type) inequalities for symmetric discrete uniforms; those individual moment comparisons do not provide this all-convex-loss sharp dilation. The integrated-quantile criterion, binomial probability masses, and convolution preservation of convex order are classical ingredients, not claimed as new.

## Limitations
No claim is made that the sharp dilation for each individual \(n\ge4\) equals \(c_3\), nor that the constants are optimal for arbitrary unequal weights or non-Rademacher sub-Gaussian sums. A differently indexed prior theorem may already entail the same numerical comparison; publication priority has not been independently established. No independent scientific audit has been performed.

## References
[1] Yihan Zhang, *Sharp One-Dimensional Sub-Gaussian Comparison in Convex Order*, arXiv:2604.26819 (first posted April 29, 2026), https://arxiv.org/abs/2604.26819.

[2] Damek Davis and Sam Power, *The sharp one-dimensional convex sub-Gaussian comparison constant*, arXiv:2604.03170 (2026), https://arxiv.org/abs/2604.03170.

[3] Alex Havrilla and Tomasz Tkocz, *Sharp Khinchin-type inequalities for symmetric discrete uniform random variables*, arXiv:1912.13345 (2019), https://arxiv.org/abs/1912.13345.
