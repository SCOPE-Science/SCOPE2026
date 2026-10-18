# Farey-indexed gaps and an exponential gap law for Sturmian beta parameters

## Finding
Let \(\mathcal B\subset(1,2)\) consist of the bases whose lexicographically maximal beta-expansion is the characteristic maximal Sturmian word of an irrational slope. Its closure \(C\subset[1,2]\) is a perfect, nowhere-dense Cantor set of Hausdorff dimension zero. Its complementary intervals in \([1,2]\) are indexed bijectively by reduced rationals \(0<p/q<1\), and **both endpoints of every gap are explicit algebraic numbers**.

Precisely, put \(u_j=\lceil(j+1)p/q\rceil-\lceil jp/q\rceil\) for \(0\le j<q\), and \(P_{p,q}(t)=\sum_{j=0}^{q-1}u_jt^{j+1}\). Let \(b^-_{p/q}\) and \(b^+_{p/q}\) be the unique solutions in \((1,2)\) of, respectively,
\[
P_{p,q}(1/b^-_{p/q})=1-(b^-_{p/q})^{-q},\qquad
P_{p,q}(1/b^+_{p/q})+(2-(b^+_{p/q})^{-1})(b^+_{p/q})^{-q}=1.
\]
Then \(b^-_{p/q}<b^+_{p/q}\) and the components of \((1,2)\setminus C\) are exactly \((b^-_{p/q},b^+_{p/q})\). Moreover, the set \(C\cap[1+\varepsilon,2]\) has upper box dimension zero for every \(\varepsilon>0\): for each integer \(n\ge1\), it admits at most \(\sum_{q=1}^n\varphi(q)\le n^2\) covering intervals of length at most \(4\varepsilon^{-1}(1+\varepsilon)^{-n}\).

There is also a **sharp local gap-width law**. For any reduced rationals \(p_k/q_k\to\alpha\in(0,1)\setminus\mathbb Q\), let \(B_k=b^-_{p_k/q_k}\), \(\beta=\beta(\alpha)\), and \(a_j=\lceil(j+1)\alpha\rceil-\lceil j\alpha\rceil\). Then
\[
\lim_{k\to\infty}(b^+_{p_k/q_k}-b^-_{p_k/q_k})B_k^{q_k}
=\frac{1-\beta^{-1}}{\displaystyle\sum_{j=0}^{\infty}(j+1)a_j\beta^{-j-2}}>0.
\]

## Assumptions and scope
The slope \(\alpha\) belongs to \((0,1)\setminus\mathbb Q\). Define \(a_j(\alpha)=\lceil(j+1)\alpha\rceil-\lceil j\alpha\rceil\in\{0,1\}\), for integers \(j\ge0\), and let \(\beta(\alpha)\in(1,2)\) uniquely solve
\[
F_{\alpha}(\beta):=\sum_{j=0}^{\infty}a_j(\alpha)\beta^{-j-1}=1.
\]
The existence and identification of this base with the maximal Sturmian beta-shift are established in the cited primary literature; the statements above concern the base-parameter set \(\mathcal B=\{\beta(\alpha):\alpha\in(0,1)\setminus\mathbb Q\}\), not all beta-shifts failing typical periodic optimization. The closure \(C\) includes non-Sturmian endpoint bases, which must not be mistaken for extra members of \(\mathcal B\). Throughout, \(\varphi\) is Euler's totient function.

## Proof
**1. Ordering and continuity.** For \(t=\beta^{-1}\in(0,1)\), put \(c_n(\alpha)=\lceil n\alpha\rceil\) with \(c_0=0\). Abel summation gives the absolutely convergent identity
\[
F_\alpha(1/t)=(1-t)\sum_{n=1}^{\infty}c_n(\alpha)t^n.
\]
For \(\alpha_1<\alpha_2\), the ceilings are termwise ordered and eventually strictly ordered, so \(F_{\alpha_1}(1/t)<F_{\alpha_2}(1/t)\) for every \(0<t<1\). Because each digit series is strictly decreasing in \(\beta\), \(\beta(\alpha)\) is strictly increasing. It is continuous at each irrational slope: every fixed prefix is locally constant there, the digit series converges uniformly on compact subintervals of \((1,2]\), and its defining root is unique. At \(\alpha\downarrow0\) the digits tend to \(1000\ldots\) and \(\beta\to1\); at \(\alpha\uparrow1\) they tend to \(1111\ldots\) and \(\beta\to2\). At an irrational slope, uniqueness and monotonicity give the required compact localization of the roots before uniform convergence is applied.

**2. Rational discontinuities.** Fix reduced \(p/q\in(0,1)\). Approaching from below, for each fixed \(n\), \(c_n(\alpha)\to\lceil np/q\rceil\). From above, \(c_n(\alpha)\to\lceil np/q\rceil+\mathbf 1_{q\mid n}\), with the indicator interpreted only for \(n\ge1\). Thus the limiting digit strings are respectively \(u_0u_1\ldots u_{q-1}\) repeated periodically and the string obtained by adding \(1\) at positions \(kq-1\) and subtracting \(1\) at positions \(kq\), for each \(k\ge1\). In particular, their generating functions in \(t\) are
\[
F^-(t)=\frac{P_{p,q}(t)}{1-t^q},\qquad
F^+(t)=F^-(t)+\frac{(1-t)t^q}{1-t^q}
=\frac{P_{p,q}(t)+(1-t)t^q}{1-t^q}.
\]
Both series have first digit \(1\), contain infinitely many \(1\)'s, and are not all ones. Consequently each equation \(F^\pm(1/b)=1\) has exactly one solution in \((1,2)\). Since \(F^+>F^-\), these satisfy \(b^+_{p/q}>b^-_{p/q}\). Rearranging gives the two displayed algebraic equations.

**3. Exhaustion of gaps and topology.** Strict monotonicity implies that none of the irrational-slope bases lies in any open interval \((b^-_{p/q},b^+_{p/q})\); the same holds for their closure. Conversely, suppose \(y\in(1,2)\setminus C\). Let \(\alpha_0\) be the cut of irrational slopes at which \(\beta(\alpha)\) passes \(y\). It cannot be irrational, since continuity at such a cut would give \(y=\beta(\alpha_0)\in C\). Thus \(\alpha_0=p/q\) is rational and its one-sided limits bracket \(y\) strictly (the endpoints themselves belong to \(C\)). This identifies every complementary component and proves its label is unique. The closure is perfect: every irrational-slope value is approached by distinct irrational-slope values, each rational jump endpoint is approached from its defining side, and \(1,2\) are approached as slopes tend to \(0,1\). It is nonempty, compact and totally disconnected by the gap classification; the next step shows it has empty interior. Hence it is a Cantor set.

**4. Metric thinness.** A length-\(n\) prefix of \(a(\alpha)\) is constant on each component of \((0,1)\) after deleting the rationals with reduced denominator at most \(n\). There are precisely \(\sum_{q=1}^n\varphi(q)\) such components, and this also bounds the prefixes of all their limit words. Fix \(\varepsilon>0\) and any such prefix \(w\) of length \(n\). Let \(H_w(b)=\sum_{j=0}^{n-1}w_jb^{-j-1}\). Every associated base \(b\in C\cap[1+\varepsilon,2]\) satisfies \(1-\varepsilon^{-1}(1+\varepsilon)^{-n}\le H_w(b)\le1\), since its unseen tail is at most \(b^{-n}/(b-1)\). Since \(w_0=1\), \(-H_w'(b)\ge b^{-2}\ge1/4\); consequently two such bases with the same prefix are separated by at most \(4\varepsilon^{-1}(1+\varepsilon)^{-n}\). This gives the claimed cover and upper box dimension zero on each truncated interval. The union \(C=\{1\}\cup\bigcup_{m\ge1}(C\cap[1+1/m,2])\) has Hausdorff dimension zero. A nonempty interval has dimension one, proving empty interior.

**5. Exact local gap asymptotics.** Let \(b_q^-=B_q\), \(b_q^+=R_q\) for reduced rational slopes tending to an irrational \(\alpha\). Necessarily \(q\to\infty\), and coordinatewise convergence of both one-sided digit sequences to \(a(\alpha)\) gives \(B_q,R_q\to\beta(\alpha)\). At \(B_q\), the right generating function exceeds one by
\[
F_q^+(B_q)-1=\frac{(1-B_q^{-1})B_q^{-q}}{1-B_q^{-q}}.
\]
The mean-value theorem supplies \(\xi_q\in(B_q,R_q)\) with
\[
(R_q-B_q)B_q^q
=\frac{1-B_q^{-1}}{(1-B_q^{-q})[-(F_q^+)'(\xi_q)]}.
\]
The derivative series converge uniformly on a compact neighborhood of \(\beta(\alpha)>1\) by geometric domination and coordinatewise convergence. Hence the denominator converges to \(\sum_{j\ge0}(j+1)a_j(\alpha)\beta^{-j-2}\), positive because \(a_0=1\). This proves the limit without assuming a rate of rational approximation.

## Verification
The accompanying `verify.py` checks the exact finite rational-ceiling identities and characteristic prefix counts, verifies the two endpoint equations by interval bisection, and tests the normalized gap limit on continued-fraction approximants of \(\sqrt2-1\). These finite computations are consistency checks; the quantifiers over all slopes and denominators follow from the proof above. Examples include the gap at slope \(1/2\), with endpoints \((1+\sqrt5)/2\) and the largest real root of \(b^3-b^2-2b+1=0\), approximately \(1.61803398875\) and \(1.80193773580\).

## Relationship to prior work
Huang, Jenkinson, Xu and Zhang (2026), Definition 1.2 and Theorem A, motivate the distinguished base family by showing its failure of typical periodic optimization. Chi and Kwon (2004; 2003 preprint), Theorems 4.3–4.4, establish the Sturmian beta parametrization and the transcendence of irrational-slope bases; their Section 5 discusses measure-theoretic properties, but does not present the Farey-indexed algebraic gap endpoints or the denominator-normalized gap-width law. Allouche (2008) addresses the separate uniqueness-of-expansion property of self-Sturmian numbers. Anagnostopoulou and Jenkinson (2009) classify beta-shifts with a largest invariant measure and provide Farey constructions for periodic Sturmian words; their classification does not identify the complete complement of the irrational-slope base set or its quantitative local gap law. Results concerning devil's staircases for ordered doubling-map orbits (Bullett–Sentenac, 1994) provide related symbolic context but use a different geometric parameter. The present proof uses these classical symbol definitions, not a claim of novelty for the underlying Sturmian words or basic beta-series parametrization.

## Limitations
The theorem applies only to the binary maximal characteristic Sturmian beta bases, not every emergent beta parameter nor every beta-shift lacking typical periodic optimization. Rational slopes label gaps but are excluded from the base family itself. The dimension assertion is for this specific family and its closure, and no global upper box dimension at the accumulation endpoint \(1\) is asserted. The stated normalized local gap limit is along reduced rationals converging to an irrational slope; no uniform formula approaching a rational slope is claimed. The historical literature on ordered symbolic staircases is extensive, and an equivalent parameter-space description outside the inspected primary texts cannot be excluded without independent bibliographic review.

## References
1. W. Huang, O. Jenkinson, L. Xu, Y. Zhang, *Sturmian beta-shifts do not have typical periodic optimization* (2026), arXiv:2610.03619v1, §§1.2–1.3 and 3, https://arxiv.org/html/2610.03619v1.
2. D. P. Chi and D. Kwon, *Sturmian words, beta-shifts, and transcendence*, Theoretical Computer Science **321** (2004), 395–404; arXiv:math/0308140v1, §§3–5, https://arxiv.org/html/math/0308140v1.
3. J.-P. Allouche, *A note on univoque self-Sturmian numbers*, RAIRO ITA **42** (2008), 659–662; arXiv:math/0612816v1, §§2–3, https://arxiv.org/pdf/math/0612816.
4. V. Anagnostopoulou and O. Jenkinson, *Which beta-shifts have a largest invariant measure?*, Journal of the London Mathematical Society **79** (2009), 445–464, §§1 and 3, https://webspace.maths.qmul.ac.uk/o.m.jenkinson/betamax11.pdf.
5. S. Bullett and P. Sentenac, *Ordered orbits of the shift, square roots, and the devil's staircase*, Math. Proc. Cambridge Philos. Soc. **115** (1994), 451–481, doi:10.1017/S0305004100072236 (abstract consulted; complete primary text unavailable).
