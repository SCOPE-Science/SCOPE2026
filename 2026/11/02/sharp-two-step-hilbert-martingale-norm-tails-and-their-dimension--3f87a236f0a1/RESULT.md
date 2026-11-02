# Sharp two-step Hilbert-martingale norm tails and their dimension gap

## Finding

**Theorem (exact two-step terminal norm-tail profile).** Fix real numbers \(a,b>0\), a threshold \(x\ge 0\), and a real Hilbert space \(H\) of dimension at least two. Among all integrable \(H\)-valued martingales \((M_0,M_1,M_2)\) with \(M_0=0\) and almost-sure deterministic difference bounds \(\|M_1\|\le a\), \(\|M_2-M_1\|\le b\), the **attained** sharp terminal tail envelope is

\[
\sup \Pr\{\|M_2\|\ge x\}=
\begin{cases}
1,&0\le x\le \sqrt{a^2+b^2},\\
\dfrac{2ab}{x^2-(a-b)^2},&\sqrt{a^2+b^2}<x\le a+b,\\
0,&x>a+b.
\end{cases}
\]

For \(\sqrt{a^2+b^2}<x\le a+b\), put
\[
t=\frac{x^2-a^2-b^2}{2a},\qquad q=\frac{b}{b+t},\qquad h=\sqrt{b^2-t^2}.
\]
An optimizer takes \(M_1\) equally likely equal to \(ae_1\) and \(-ae_1\), with \(e_1,e_2\) orthonormal. Conditional on \(M_1=sae_1\), where \(s\in\{-1,+1\}\), the second increment is \(ste_1+he_2\) and \(ste_1-he_2\), each with probability \(q/2\), and \(-sbe_1\) with probability \(1-q\). For \(\sqrt{a^2+b^2}<x\le a+b\), every optimizer has \(\|M_1\|=a\) almost surely; conditional on the first step, the second-step law consists of a single inward atom \(-be\) of probability \(1-q\), and a mean-zero tangential distribution on \(te+\{z\in e^\perp:\|z\|=h\}\) of probability \(q\), where \(e=M_1/a\). At the upper endpoint \(x=a+b\), the tangential radius is \(h=0\).

**Dimension and symmetry comparisons (same extremal problem).** On the real line, the sharp envelope instead equals \(1\) for \(0\le x\le\max\{a,b\}\), \(b/(b+x-a)\) for \(\max\{a,b\}<x\le a+b\), and \(0\) above \(a+b\). In any real Hilbert space of dimension at least two, imposing conditional symmetry of the second increment, \(\mathcal L(M_2-M_1\mid\mathcal F_1)=\mathcal L(M_1-M_2\mid\mathcal F_1)\), changes the envelope to \(1\) for \(x\le\sqrt{a^2+b^2}\), \(1/2\) for \(\sqrt{a^2+b^2}<x\le a+b\), and \(0\) above \(a+b\). All extrema are attained.

**Fixed quadratic proxy.** Let \(v>0\). If the bounds \(a,b\ge0\) are free to vary subject to \(a^2+b^2=v\), the sharp dimension-at-least-two tail envelope is \(1\) for \(0\le x\le\sqrt v\), \(v/x^2\) for \(\sqrt v<x\le\sqrt{2v}\), and \(0\) for \(x>\sqrt{2v}\). Thus the elementary quadratic Markov bound is genuinely attainable throughout its nontrivial support range by a two-step planar martingale, while fixed unequal difference bounds yield a strictly sharper exact constant.

## Assumptions and scope

Martingale means \(\mathbb E[M_j\mid\mathcal F_{j-1}]=M_{j-1}\) for \(j=1,2\), with an arbitrary filtration, no independence assumption, and bounded differences as stated. All norms and inner products are Hilbertian; the main formula holds equally in finite or infinite real Hilbert dimension at least two. Threshold events include equality \(\ge x\). Bounds are constraints, not assertions that increment lengths must always equal them. The scalar and conditionally symmetric subclasses use the same ordering of the two step bounds; the scalar formula is not claimed as a new result about one-dimensional bounded martingales.

## Proof

**1. Upper bound for the large-threshold region.** Let \(X=M_2-M_1\), and condition on \(\mathcal F_1\). Set \(r=\|M_1\|\in[0,a]\). If \(x>\sqrt{a^2+b^2}\), then \(x>b\). At \(r=0\), the event \(\|M_1+X\|\ge x\) is impossible. At \(r>0\), define \(e=M_1/r\) and \(Y=\langle e,X\rangle\). Since \(\|X\|\le b\), the event \(E=\{\|M_1+X\|\ge x\}\) entails
\[
Y\ge t_r:=\frac{x^2-r^2-b^2}{2r}>0.
\]
Moreover \(Y\ge-b\) and \(\mathbb E[Y\mid\mathcal F_1]=0\). Hence
\[
0=\mathbb E[Y\mid\mathcal F_1]\ge t_r\Pr(E\mid\mathcal F_1)-b\bigl(1-\Pr(E\mid\mathcal F_1)\bigr),
\]
so \(\Pr(E\mid\mathcal F_1)\le b/(b+t_r)\). Since
\[
\frac{\mathrm d t_r}{\mathrm dr}=-\frac{x^2-b^2}{2r^2}-\frac12<0,
\]
this is at most \(b/(b+t_a)=2ab/[x^2-(a-b)^2]\). If \(x>a+b\), the triangle inequality instead forces probability zero.

**2. All thresholds are sharp.** For \(x\le\sqrt{a^2+b^2}\), use two independent symmetric signs and orthonormal \(e_1,e_2\): take \(M_1=\pm ae_1\) and \(M_2-M_1=\pm be_2\). Then \(\|M_2\|=\sqrt{a^2+b^2}\) surely. For \(\sqrt{a^2+b^2}<x\le a+b\), the \(t,q,h\) in the finding satisfy \(0<t\le b\), \(0\le h^2=b^2-t^2\), and \(qt=(1-q)b\). The stated second-increment law is therefore centered and supported on the radius-\(b\) sphere. Its two outgoing atoms have terminal squared norm \((a+t)^2+h^2=x^2\), while its inward atom has terminal norm \(|a-b|<x\). The event probability is exactly \(q\). The endpoint \(x>a+b\) is impossible and hence sharp.

**3. Extremizer rigidity.** For \(\sqrt{a^2+b^2}<x\le a+b\), monotonicity of \(t_r\) is strict. Equality of the integrated upper bound therefore forces \(r=a\) almost surely. For each conditional law, equality in the scalar one-sided mean inequality forces \(Y=t\) on \(E\) and \(Y=-b\) on \(E^c\), almost surely. The pointwise norm inequality forcing \(Y\ge t\) then implies \(\|X\|=b\) on \(E\). On \(E^c\), \(Y=-b\) together with \(\|X\|\le b\) implies \(X=-be\). Writing \(X=te+z\) on \(E\) gives \(z\perp e\), \(\|z\|=h\); conditional centering gives \(\mathbb E[z\mid E,\mathcal F_1]=0\) whenever \(q>0\). Conversely every such conditional law attains equality. At \(x=a+b\), \(h=0\) and this reduces to a two-point law.

**4. Real-line and symmetry refinements.** On \(H=\mathbb R\), the event is certain up to \(\max\{a,b\}\) by using only the longer increment. If \(x>\max\{a,b\}\) and the first position has absolute value \(r\le a\), the negative-direction exit after the second step is impossible because \(x>b\). The event requires a forward increment at least \(x-r\), so the mean-zero, lower-bound-\(-b\) argument gives at most \(b/(b+x-r)\le b/(b+x-a)\). A centered two-atom conditional second step with values \(x-a\) and \(-b\), and a symmetric \(\pm a\) first step, attains equality whenever \(x\le a+b\). For the symmetry restriction in dimension at least two, pair each possible second increment \(z\) with \(-z\). For \(x>\sqrt{a^2+b^2}\), their terminal squared norms sum to \(2(r^2+\|z\|^2)\le2(a^2+b^2)<2x^2\), so at most one member of a pair reaches the threshold. Conditional symmetry gives probability at most \(1/2\), attained by the collinear symmetric \(\pm b\) second step when \(x\le a+b\); the orthogonal construction attains probability one below the transition.

**5. Fixed-proxy optimization.** Put \(v=a^2+b^2\). In the nontrivial interval \(x^2>v\), the main expression is \((v-\delta)/(x^2-\delta)\), where \(\delta=(a-b)^2\ge0\). Because its derivative with respect to \(\delta\) is \((v-x^2)/(x^2-\delta)^2<0\), it is maximized at \(\delta=0\), or \(a=b=\sqrt{v/2}\), where it equals \(v/x^2\). Moreover \(a+b\le\sqrt{2v}\). Orthogonal increments attain one for \(x\le\sqrt v\), and no admissible two-step process reaches \(x>\sqrt{2v}\). This proves the asserted complete proxy envelope.

## Verification

The standalone `verify.py` makes 3,892 deterministic assertions in exact rational arithmetic. For positive integer bounds \(1\le a,b\le8\), selected squared thresholds ranging from the orthogonal radius to the maximal radius, and intermediate first-step magnitudes, it checks the extremal law's probabilities, zero drift, radius, event threshold, upper-bound monotonicity, endpoint values, and fixed-proxy inequalities. An unequal-bound construction with \(a=3\), \(b=4\), \(x^2=30\) has \(t=5/6\), \(q=24/29\), and transverse squared length \(h^2=551/36\). Run `python verify.py`; the companion `verification_output.txt` records the actual result. The universal, uncountable-parameter and dimension-independent claims follow from the displayed proof, not the finite tests.

## Relationship to prior work

Juškevičius and Šileikis (2026) prove high-quality Gaussian-comparison and large-deviation upper bounds for Euclidean-valued martingales, and their Theorem 3 compares expectations of functions with convex second derivative of suitable type. Neither such expectation comparison nor their stated tail bounds supplies the exact two-step indicator-tail supremum, the unequal-step rational profile, or its equality geometry. For instance, when \(a=b=1\), \(x=3/2\), the sharp planar tail is \(8/9\), versus \(2/3\) for the scalar class; a two-sign Rademacher sum has only probability \(1/2\) of absolute value at least \(3/2\). Consequently, moment ordering cannot be silently substituted for sharp tail ordering.

Pinelis (1994) supplies foundational martingale distribution inequalities in 2-smooth Banach spaces, and Janz (2026) studies time-uniform, covariance-dependent Bennett/Bernstein bounds. Their general-purpose regimes and parameterizations differ from an *attained exact* two-step deterministic-increment envelope. Dzindzalieta (2009) treats exact optimal terminal and crossing tails for **real-valued** bounded martingales; that scalar analysis is not claimed new here. The dimension-two geometry is essential for the full upper envelope, whereas one-dimensional exit theory is not a substitute.

## Limitations

This is an exact two-step fixed-terminal-time result, not an optimum for arbitrary horizon lengths, time-uniform first-crossing tails, nonsmooth Banach norms, or martingales whose constraints are only variance bounds. The scalar comparison depends on the order \(a\) then \(b\). The middle branch is meaningful only for strictly positive step bounds. No claim of prior-work uniqueness follows from database searches; an unlocated earlier sharp two-stage Bellman-function computation remains a historical-priority risk. Equality of the terminal second moment alone does not establish the tail envelope without the conditional projection argument.

## References

1. T. Juškevičius and M. Šileikis, *Concentration inequalities for vector-valued martingales*, arXiv:2610.31449v1, first posted 2026-10-22, https://arxiv.org/html/2610.31449v1 (Theorems 1–3, Sections 2–4).
2. D. Dzindzalieta, *Exact bounds for tail probabilities of martingales with bounded differences*, Liet. Mat. Rink. LMD Darbai 50 (2009), 412–415, https://www.journals.vu.lt/LMR/article/download/18001/17160/30346 .
3. I. Pinelis, *Optimum bounds for the distributions of martingales in Banach spaces*, Ann. Probab. 22 (1994), 1679–1706, https://arxiv.org/abs/1208.2200 .
4. D. Janz, *Self-normalised Bennett inequalities for Hilbert-valued martingales*, arXiv:2608.15874v1, first posted 2026-08-16, https://arxiv.org/abs/2608.15874 .
