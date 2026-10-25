# The sharp discrete concavity index of the integer-shape Yule–Simon law

## Finding
For every integer shape \(r\ge1\), let \(X_r\) have the Yule–Simon distribution \(\Pr(X_r=k)=rB(k,r+1)\), \(k=1,2,\ldots\). There is exactly one positive number \(a_r\) satisfying
\[
\left(\frac{r+3}{2}\right)^{a_r}+(r+2)^{-a_r}=2.
\]
The **largest** discrete generalized-mean concavity parameter of this law is exactly \(\alpha_r^*=-a_r\): its mass function is discrete \(\alpha\)-concave if and only if \(\alpha\le-a_r\). Moreover, putting \(R_r=\left(\sum_{j=1}^{r+1}j^{-2}\right)/\left(\sum_{j=1}^{r+1}j^{-1}\right)^2\), one has the strict enclosure
\[
\frac{1}{r+1}<a_r<R_r,
\qquad
\lim_{r\to\infty}a_r(\log r)^2=\log2,
\qquad
\lim_{r\to\infty}\frac{a_r}{R_r}=\frac{6\log2}{\pi^2}.
\]
Thus a single nearest-boundary midpoint test controls infinitely many inequalities and the continuous second-derivative sufficient index in [1] is strictly nonoptimal, by a nonvanishing asymptotic factor.

## Assumptions and scope
The shape \(r\) is a **positive integer** (not an arbitrary positive real), the support is \(\{1,2,\ldots\}\), and the concavity parameter is the generalized-mean parameter of Definition 1.1 in [1]. Outside-support masses vanish; only triples fully inside the positive support impose a condition. For negative \(\alpha=-a\), the inequality is equivalent to convexity of the sequence of reciprocal-mass powers \(p_k^{-a}\). All uniqueness and limit assertions here are proved for this exact family.

## Proof
Let \(r\ge1\) be an integer and put \(h_a(x)=\prod_{j=0}^{r}(x+j)^a\) for \(x\ge1\) and \(a>0\). The normalization of the probability mass function cancels in midpoint tests. For \(\alpha=-a\), Definition 1.1 of [1] is equivalent to \(h_a(k+1)-2h_a(k)+h_a(k-1)\ge0\) for every \(k\ge2\); no condition crosses the boundary of the positive support.

**The first interior condition.** Direct telescoping gives
\[
\frac{h_a(3)}{h_a(2)}=\left(\frac{r+3}{2}\right)^a,\qquad
\frac{h_a(1)}{h_a(2)}=(r+2)^{-a}.
\]
Thus the condition at \(k=2\) is \(F_r(a)\ge0\), where
\[
F_r(a)=e^{aA_r}+e^{-aB_r}-2,\quad A_r=\log((r+3)/2)>0,\ B_r=\log(r+2)>A_r.
\]
The function is strictly convex, satisfies \(F_r(0)=0\), \(F_r'(0)=A_r-B_r<0\), and tends to infinity. Therefore it has exactly one positive root \(a_r\), with \(F_r(a)\ge0\) for positive \(a\) exactly when \(a\ge a_r\).

**Why no later lattice test is stronger.** Define \(S_j(x)=\sum_{i=0}^{r}(x+i)^{-j}\) and \(R(x)=S_2(x)/S_1(x)^2\). Two differentiations yield
\[
\frac{h_a''(x)}{h_a(x)}=a S_1(x)^2\big(a-R(x)\big),\qquad
R'(x)=\frac{2(S_2(x)^2-S_1(x)S_3(x))}{S_1(x)^3}<0.
\]
The strict inequality follows from Cauchy–Schwarz and distinct positive summands (because \(r\ge1\)). Also \(R(x)>1/(r+1)\) for finite \(x\ge1\), while \(R(x)\to1/(r+1)\). Consequently \(h_a''\) has at most one sign change on \([1,\infty)\), necessarily negative to positive; the cases of a constant sign are allowed.

We record the deterministic observation that for any twice continuously differentiable function \(h\) whose second derivative has this one-change property, the first nonnegative lattice second difference \(h(3)-2h(2)+h(1)\ge0\) implies every later integer second difference is nonnegative. Indeed, set \(D(x)=h(x+1)-h(x)\), so \(D'(x)=h'(x+1)-h'(x)=\int_x^{x+1}h''(u)\,du\). If the change of sign of \(h''\) is at \(z\), then \(D'\le0\) before \(z-1\), \(D'\ge0\) after \(z\), and \(D'\) is strictly increasing across the intervening interval because \(D''(x)=h''(x+1)-h''(x)>0\) there. Hence \(D'\) also changes sign at most once, negative to positive. Since \(\int_1^2 D'(x)\,dx=D(2)-D(1)\ge0\), this change has occurred by \(x=2\); hence \(D'(x)\ge0\) for \(x\ge2\), and \(D(k)-D(k-1)\ge0\) for all \(k\ge3\). This also covers constant-sign cases by direct monotonicity. Applying the observation to \(h_a\) proves that the condition at \(k=2\) is necessary and sufficient for all interior indices. The generalized means increase with \(\alpha\), so the characterization extends to all real \(\alpha\), not only negative ones.

**Strict comparison with the continuous index.** At \(a=1/(r+1)\) one has \(a<R(x)\) for every finite \(x\); thus \(h_a''(x)<0\), the first second difference is negative, and \(a_r>1/(r+1)\). At \(a=R(1)\), strict decrease of \(R\) gives \(h_a''(x)>0\) for all \(x>1\), so the first second difference is positive, proving \(a_r<R(1)\). The latter is exactly the exponent used as an admissible sufficient index in [1, Example 1.2(3)].

**Sharp large-shape asymptotic.** With \(L=\log r\), \(A_r=L-\log2+o(1)\) and \(B_r=L+o(1)\). For each fixed \(c>0\), Taylor expansion at \(a=c/L^2\) gives
\[
L^2F_r(c/L^2)=c^2-c\log2+o(1).
\]
The unique positive root is trapped between \(c_-/L^2\) and \(c_+/L^2\) for any \(0<c_-<\log2<c_+\), hence \(a_r L^2\to\log2\). Finally \(R(1)=H_{r+1}^{(2)}/H_{r+1}^2\sim(\pi^2/6)L^{-2}\), so \(a_r/R(1)\to6\log2/\pi^2\). No numerical extrapolation is used to prove these limits.

## Verification
The direct symbolic identities for \(h_a(1)/h_a(2)\), \(h_a(3)/h_a(2)\), \(h_a''/h_a\), and \(R'\) can be recomputed from the finite products and sums above. Run `python3 verify.py` using only the Python standard library: this evaluates the root and strictly brackets it between the two analytic comparison indices for representative integer shapes, checks that the sharp boundary is attained at the second lattice site, and spot-checks subsequent sites. Those finite checks do not replace the one-sign-change argument or the asymptotic proof.

At \(r=3\), the new index is approximately \(a_3=0.2854614903\), versus the sufficient exponent \(R_3\approx0.328\) from [1]. Both lie within the variance-inequality regime \(0<a<1/3\), so inserting the sharper admissible parameter into [1, Theorem 1.3] improves the existing inequality's coefficient. This does not assert sharpness of that separate variance bound for the Yule–Simon family.

## Relationship to prior work
Alqasem, Aravinda, and Marsiglietti [1, Definition 1.1, Example 1.2(3)] introduced the discrete generalized-mean criterion and supplied the index \(-R_r\) for the integer-shape Yule–Simon law using the second derivative of the continuous beta-function interpolation at the first support point. Their result is a **sufficient** index, not an optimization of the infinitely many discrete midpoint inequalities. Their Theorem 1.3 can use any newly established admissible parameter. The present statement identifies the **maximal** parameter, a sharp one-test reduction, and its large-shape gap from the continuous index. Connections to power-convex sequences or gamma-ratio inequalities may contain antecedents; the comparison is not a claim of exhaustive historical priority.

## Limitations
The proof does not classify noninteger positive shape parameters, does not optimize the variance inequality of [1] within this distribution family, and does not assert a corresponding threshold for arbitrary heavy-tailed or generalized-beta laws. Finite numerical checks certify only their stated finite cases, while the infinite and asymptotic claims rest on the displayed analytic argument.

## References
[1] A. Alqasem, H. Aravinda, and A. Marsiglietti, *Majorization, Entropy and Concentration Inequalities for Discrete α-Concave Random Variables*, arXiv:2610.05439v1 (first posted 2026-10-04), https://arxiv.org/html/2610.05439v1. See Definition 1.1, Example 1.2(3), and Theorem 1.3.
