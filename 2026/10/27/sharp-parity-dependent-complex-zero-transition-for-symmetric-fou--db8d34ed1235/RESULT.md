# Sharp parity-dependent complex-zero transition for symmetric four-atom Fourier transforms

## Finding

Let \(n\ge3\) be an integer, let \(0<p<1\), and put the symmetric probability measure
\[\mu_{n,p}=\frac p2(\delta_{-n}+\delta_n)+\frac{1-p}{2}(\delta_{-(n-2)}+\delta_{n-2}).\]
Its entire Fourier transform is
\[F_{n,p}(z)=\int e^{izx}\,d\mu_{n,p}(x)=p\cos(nz)+(1-p)\cos((n-2)z).\]
Define the sharp parameter
\[p_n=\begin{cases}\frac12,&n\text{ even},\\ \frac{n-2}{2(n-1)},&n\text{ odd}.\end{cases}\]
**Theorem.** Every complex zero of \(F_{n,p}\) is real if and only if \(p\ge p_n\). More precisely, in every strip \(0\le\operatorname{Re}z<2\pi\), counted with multiplicity, there are exactly \(2n\) zeros:

- If \(p>p_n\), all \(2n\) are real and simple.
- If \(p=p_n\) and \(n\) is even, all zeros are real; the two zeros at \(z=\pi/2,3\pi/2\) are each double, and all other zeros are simple.
- If \(p=p_n\) and \(n\) is odd, all zeros are real; the two zeros at \(z=\pi/2,3\pi/2\) are each triple, and all other zeros are simple.
- If \(0<p<p_n\), precisely four zeros per strip are nonreal, all simple, at
\[z=\frac\pi2+\pi k\pm iv,\qquad k=0,1,\]
with the unique \(v>0\) determined by
\[\frac{\cosh(nv)}{\cosh((n-2)v)}=\frac{1-p}{p}\quad(n\text{ even}),\qquad\frac{\sinh(nv)}{\sinh((n-2)v)}=\frac{1-p}{p}\quad(n\text{ odd}).\]
The remaining \(2(n-2)\) zeros are real and simple. All zeros elsewhere are obtained by adding integer multiples of \(2\pi\) to the listed strip representatives.

The nonreal zero height undergoes a square-root collision at the threshold: as \(p\uparrow p_n\),
\[v\sim\begin{cases}\sqrt{\frac{2}{n-1}(p_n-p)},&n\text{ even},\\\sqrt{\frac{6(n-1)}{n(n-2)}(p_n-p)},&n\text{ odd}.\end{cases}\]
The parity distinction is substantial: for each fixed \(0<p<1/2\), *all even degrees* have nonreal zeros, while an odd degree has only real zeros exactly when \(n\le2(1-p)/(1-2p)\).

## Assumptions and scope

The frequencies are the two consecutive positive integers of the same parity \(n-2,n\), and each signed pair carries a positive total mass, \(p\) and \(1-p\). Thus the measure has four distinct atoms for every \(n\ge3\). The assertion is about **all complex zeros** of the entire characteristic function, not just its zeros on the real axis. Multiplicities are complex-analytic orders of vanishing. In a half-open fundamental strip, \(\cos z=t\) has two preimages for each \(t\in\mathbb C\setminus\{\pm1\}\), counted with multiplicity, because \(e^{iz}\) solves a quadratic equation. Neither endpoint \(\pm1\) is a root of the polynomial considered below.

## Proof

Write \(T_j\) for the Chebyshev polynomial characterized by \(T_j(\cos z)=\cos(jz)\), and define
\[Q(t)=pT_n(t)+(1-p)T_{n-2}(t).\]
Then \(F_{n,p}(z)=Q(\cos z)\), \(\deg Q=n\), \(Q(1)=1\), and \(Q(-1)=(-1)^n\). The identity \(Q(-t)=(-1)^nQ(t)\) gives parity symmetry. For real \(|t|>1\), both Chebyshev terms have the same strict sign, so no root lies outside \((-1,1)\) on the real line.

For \(j=0,\ldots,n-2\), set \(\theta_j=(j+1/2)\pi/(n-1)\) and \(t_j=\cos\theta_j\). Since \(\cos((n-1)\theta_j)=0\) and \(\sin((n-1)\theta_j)=(-1)^j\), the cosine addition formulas give
\[Q(t_j)=(1-2p)(-1)^j\sin\theta_j.\]
For \(p\ne1/2\), the values alternate strictly in sign. Consequently each of the \(n-2\) disjoint intervals \((t_{j+1},t_j)\) contains a distinct real root. Since \(Q\) has degree \(n\), at most two additional roots, counted with multiplicity, remain.

For \(p>1/2\), \(Q(t_0)<0<Q(1)\), while \(Q(t_{n-2})\) and \(Q(-1)\) have opposite signs. Hence the two outer gaps contain the two remaining real roots. All \(n\) are simple and in \((-1,1)\).

At \(p=1/2\), the standard recurrence gives \(Q(t)=tT_{n-1}(t)\). If \(n\) is even, \(T_{n-1}\) has one simple zero at \(t=0\), making the product double there, with all other roots simple. If \(n\) is odd, \(T_{n-1}(0)\ne0\) and all roots are simple.

For \(0<p<1/2\), the two roots remaining after the sign-change argument must either be two real roots or a conjugate pair. If nonreal, they are purely imaginary: a nonreal root outside the imaginary axis, its complex conjugate, and their two distinct negatives would produce four nonreal roots, contradicting the degree bound.

Let \(t=i\sinh v\) with \(v>0\). The elementary Chebyshev identities \(T_m(i\sinh v)=\cos(m(\pi/2-iv))\) give, with the indicated alternating signs, the equation \(Q(t)=0\) precisely when
\[\frac{\cosh(nv)}{\cosh((n-2)v)}=\frac{1-p}{p}\quad\text{for even }n,\]
or
\[\frac{\sinh(nv)}{\sinh((n-2)v)}=\frac{1-p}{p}\quad\text{for odd }n.\]
Each left-hand side is strictly increasing for \(v>0\): its logarithmic derivative is respectively \(n\tanh(nv)-(n-2)\tanh((n-2)v)>0\) or \(n\coth(nv)-(n-2)\coth((n-2)v)>0\). For the second inequality, \(a\mapsto a\coth(av)\) increases strictly for \(a>0\), because \(\sinh u\cosh u>u\) for \(u>0\). The limiting ratios at \(v\downarrow0\) are respectively \(1\) and \(n/(n-2)\), and both ratios tend to infinity as \(v\to\infty\). There is therefore exactly one positive imaginary-polynomial-root height precisely for \(p<1/2\) in even degree or \(p<(n-2)/(2(n-1))\) in odd degree. Then the two remaining polynomial roots are exactly \(\pm i\sinh v\), simple by degree exhaustion.

It remains to settle odd \(n\) in the interval \(p_n\le p<1/2\). Write \(n=2r+1\), \(r\ge1\). The polynomial is odd, and
\[Q'(0)=(-1)^r\bigl(2(n-1)p-(n-2)\bigr).\]
For \(p_n<p<1/2\), its sign on sufficiently small positive \(t\) is \((-1)^r\), whereas its value at the closest positive grid point \(t_{r-1}\) has sign \((-1)^{r-1}\). Thus there is an additional positive root in \((0,t_{r-1})\) and a negative reflected root; together with the \(n-2\) roots supplied by sign changes (including \(0\) in the central interval), these exhaust degree \(n\), proving all are real and simple. At \(p=p_n\), \(Q'(0)=0\) and odd parity forces multiplicity at least three at the origin. The sign-change roots in the other \(n-3\) intervals, together with that triple root, exhaust degree \(n\), so the central multiplicity is exactly three and the others are simple.

The map \(z\mapsto\cos z\) has nonzero derivative over every root of \(Q\), because \(Q(\pm1)\ne0\). Each polynomial root therefore produces exactly two roots of \(F_{n,p}\) modulo \(2\pi\), with the same multiplicity. In the nonreal case the pair \(\pm i\sinh v\) lifts exactly to \(z=\pi/2+\pi k\pm iv\), \(k=0,1\). This establishes all counts, locations, multiplicities, and the zero-free/nonreal dichotomy.

Finally, expand the even hyperbolic ratio as \(1+2(n-1)v^2+O_n(v^4)\) and its right side as \(1+4(p_n-p)+O((p_n-p)^2)\). For odd \(n\), divide the ratio by \(n/(n-2)\) and expand it as \(1+\frac{2}{3}(n-1)v^2+O_n(v^4)\); the similarly normalized right side is \(1+\frac{4(n-1)^2}{n(n-2)}(p_n-p)+O_n((p_n-p)^2)\). Solving gives both stated square-root asymptotics. The fixed-\(p\) odd-degree inequality is just an algebraic rearrangement of \(p\ge p_n\). No limiting or numerical root count is used for the exact theorem.

## Verification

A standalone Python/SymPy checker rederived 46 rational-parameter Sturm real-root counts for every \(3\le n\le15\) below, at, and above the relevant threshold, confirmed all critical multiplicities, compared 48 independent Fourier/Chebyshev evaluations, and verified 15 symbolic threshold-coefficient identities. See `checker.py` and `CHECKER_OUTPUT.txt`. These are finite stress tests, not an infinite-degree proof; the proof above is independent of the checker. For a nonreal example, \(n=3,p=1/5\) has polynomial \(Q(t)=\frac45t^3+\frac15t\) and imaginary roots \(\pm i/2\). For a distinct odd-degree real example below half mass, \(n=3,p=2/5\) gives \(Q(t)=\frac85t^3-\frac35t\), all three roots real.

## Relationship to prior work

Stankov [1] considers general fixed-coefficient combinations of first-kind Chebyshev polynomials, including precisely our two-term subclass. His Theorem 1 controls *asymptotic* roots as the degree tends to infinity in terms of the characteristic polynomial; Example 3.1 records the equal-weight identity \(T_n+T_{n-2}=2tT_{n-1}\), an established identity **not asserted as new here**. His statements do not give the finite-degree, parity-sensitive threshold, universal four-nonreal-zero geometry, or triple collision above. The binomial-combination family of Al Hamdani and Tran [2] has a different degree-dependent coefficient sequence, and its theorem gives an order-independent upper bound on the number of off-interval roots rather than this exact one-parameter classification. These comparisons concern the actual polynomial families and implications, not titles alone.

## Limitations

The theorem does not classify arbitrary four frequencies, asymmetric atoms, continuous probability densities, or nonpositive complex weights. Because two-term Chebyshev combinations are classical, an unlocated specialized finite-degree theorem or broader quasi-orthogonal-polynomial criterion might imply this classification; exhaustive historical priority has not been established. No independent mathematical audit has been performed.

## References

1. D. Stankov, *On linear combinations of Chebyshev polynomials*, arXiv:1311.2230 (first posted 2013-11-09), later *Publ. Inst. Math. (Beograd)* 97(111) (2015), 57–67. https://arxiv.org/abs/1311.2230
2. S. Al Hamdani and K. Tran, *Zeros of a binomial combination of Chebyshev polynomials*, arXiv:2006.11475 (first posted 2020-06-20). https://arxiv.org/abs/2006.11475
