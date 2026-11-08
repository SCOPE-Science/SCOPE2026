# A certified \(0.7764\) lower bound for the unitary–exponential divisor-sum density

## Finding
For each positive integer \(n\), let \(\sigma^*(n)\) be its unitary-divisor sum and \(\sigma^{(e)}(n)\) its exponential-divisor sum. Let \(\delta\) be the natural density of integers satisfying \(\sigma^*(n)>\sigma^{(e)}(n)\). Then
\[
\boxed{\delta\ge \frac{502}{503}\left(\frac{771520086457799875}{10^{18}}+\frac{13}{180}\prod_{p\le503}\left(1-\frac1p\right)\right)>0.7764.}
\]
The product is over all \(96\) primes at most \(503\). The bound is unconditional. Its exact rational right-hand side is about \(0.776432356352\). The result does not determine \(\delta\).

## Assumptions and scope
For primes \(p\), define
\[
\rho_p(0)=1,\qquad \rho_p(a)=\frac{1+p^a}{\sum_{d\mid a}p^d}\quad(a\ge1).
\]
Multiplicativity gives \(\sigma^*(n)/\sigma^{(e)}(n)=\prod_p\rho_p(v_p(n))\). For \(a=1\), \(\rho_p(1)=1+1/p>1\); for \(a\ge2\), \(\rho_p(a)<1\). The existence of \(\delta\) follows from the standard additive-function limiting-distribution criterion noted in Trudgian's paper; the proof below in any case establishes the stated bound for the lower asymptotic density.

Set \(P=503\), \(B=100000\), and \(Q=10^{18}\). For each prime \(p\le P\), retain the nonnegative exponents \(a\) with \(p^{a+1}<10^{12}\); discard every larger exponent (without renormalizing). Define certified integer scores \(s_p(a)\le B\log\rho_p(a)\) by the rational method in the proof. Denote the retained local exponent-weight sum for total score at least zero by \(W\).

## Proof
**1. A finite sufficient event.** For a finite vector \(\mathbf a=(a_p)_{p\le P}\) of nonnegative exponents, define \(R(\mathbf a)=\prod_{p\le P}\rho_p(a_p)\). If \(R(\mathbf a)\ge1\) and every prime greater than \(P\) has exponent at most one, then \(\sigma^*(n)>\sigma^{(e)}(n)\) except possibly when no larger prime divides \(n\). The integers with no prime factor exceeding the fixed \(P\) have density zero (they are \(P\)-smooth). Thus the required lower bound may count all such vectors, including those with equality \(R(\mathbf a)=1\).

For prescribed exponents \(a_p\) on primes \(p\le P\), the density of the corresponding integers with all primes \(q>P\) of exponent \(0\) or \(1\) equals
\[
\prod_{p\le P}\frac{p-1}{p^{a_p+1}}\prod_{q>P}(1-q^{-2}).
\]
The tail product satisfies
\[
\prod_{q>P}(1-q^{-2})\ge1-\sum_{q>P}q^{-2}\ge1-\sum_{j>P}j^{-2}>1-\frac1P=\frac{502}{503},
\]
where the final inequality follows from integrating \(t^{-2}\) from \(P\) to infinity. (Replacing strict inequalities by weak ones would also suffice.)

**2. Exact lower logarithm bins.** For positive rational \(r=A/C\), let \(u=(A-C)/(A+C)\), so \(|u|<1\). Put
\[
T(u)=2\sum_{j=0}^{19}\frac{u^{2j+1}}{2j+1},\qquad
E(u)=\frac{2|u|^{41}}{41(1-u^2)}.
\]
The convergent \(\operatorname{atanh}\) series and the geometric remainder bound give \(\log r\ge T(u)-E(u)\). Therefore
\[
s_p(a)=\left\lfloor B\bigl(T(u_{p,a})-E(u_{p,a})\bigr)\right\rfloor\le B\log\rho_p(a)
\]
is certified using fractions only. For \(a=0\) the score is exactly zero. Hence any retained exponent vector with \(\sum_{p\le P}s_p(a_p)\ge0\) has \(R(\mathbf a)\ge1\).

**3. Finite exact weighted recurrence.** Initialize the score distribution with mass \(Q\) in bin zero. For successive primes \(p\le P\) and each retained exponent \(a\), shift the existing bin \(j\) by \(s_p(a)\), assigning the nonnegative integer contribution
\[
\left\lfloor\frac{M_j(p-1)}{p^{a+1}}\right\rfloor.
\]
Add contributions from all states. This is a *downward* rational rounding: by induction each bin mass divided by \(Q\) is at most the exact probability of its set of exponent vectors. Dropped exponents and rounding losses can only decrease the resulting mass. Direct execution of the accompanying exact-arithmetic certificate, covering every prime through \(503\), gives
\[
\sum_{j\ge0}M_j=771520086457799875.
\]
Consequently the total density weight certified by the nonnegative-score event is at least \(771520086457799875/10^{18}\).

**4. Two disjoint exact-equality cylinders.** The local ratios \(\rho_2(2)=\rho_3(2)=5/6\) and \(\rho_5(1)=6/5\) cancel exactly. Take either (i) exponent two at prime two and exponent one at prime five, or (ii) exponent two at prime three and exponent one at prime five, with exponent zero at every other prime at most \(503\). The two cylinder weights are respectively
\[
\frac1{20}\prod_{p\le503}(1-p^{-1}),\qquad
\frac1{45}\prod_{p\le503}(1-p^{-1}).
\]
They are disjoint from each other. They are also disjoint from the nonnegative-score event: the rational-series computation gives \(s_2(2)=s_3(2)=-18233\) and \(s_5(1)=18232\), so both cylinders have total score \(-1\). Thus their combined weight \((13/180)\prod_{p\le503}(1-p^{-1})\) can be added without double-counting. Their local ratio is one, and the squarefree tail supplies strict inequality outside the zero-density smooth set.

**5. Combine.** Multiply the sum of the disjoint finite-cylinder weights by the squarefree-tail lower bound \(502/503\). The standalone verifier checks, by rational integer comparison, that the resulting explicit rational value exceeds \(1941/2500=0.7764\). This establishes the theorem.

## Verification
Run `python verify_density.py` using Python 3.10 or newer. This standalone script generates the \(96\) primes, constructs all certified rational logarithm bins, performs every downward-rounded finite probability recurrence, reproduces the exact nonnegative-score weight, checks the two disjoint equality cylinders, and proves the final strict rational inequality. It uses the Python standard library only. A fresh replay of the saved script returned `VERIFY_OK` and the stated integer mass. No sampled finite set of integers is used as an infinite-density proof.

## Relationship to prior work
Trudgian's 2013 preprint asks for the proportion of integers on which the unitary divisor sum exceeds the exponential-divisor sum; it records the squarefree lower bound \(6/\pi^2\) and a finite-range empirical frequency about \(0.778307\). A subsequent published finite-cylinder argument gave an unconditional lower bound \(0.753659844\ldots\). An earlier recorded finite-cylinder claim gave \(0.770292125\ldots\), and another recorded claim gave \(\delta<0.785\); neither logically covers the present lower bound. These earlier claims are used for statement-level comparison without renewed assessment. The new result improves the strongest of these recorded lower bounds by more than \(0.0061\), using a ninety-six-prime compressed certificate rather than enumerating a large Cartesian product of exponent vectors. An approximate numerical frequency is not a theorem about \(\delta\).

## Limitations
The certified constant is a lower bound, not an evaluation of the density or a proof that the bound is optimal. The finite prime cutoff, truncation, lower logarithm bins, and two added equality cylinders are sufficient conditions that omit other valid integers. The numerical certificate is finite and reproducible; the infinite step relies on the proved squarefree-tail density argument. Some earlier or unindexed treatment could conceivably contain a stronger explicit bound; the available comparisons do not establish exhaustive historical priority.

## References
1. T. Trudgian, *The sum of the unitary divisor function*, arXiv:1312.4615 (first public version, 17 December 2013), especially Section 4; later journal publication in 2015. https://arxiv.org/abs/1312.4615
2. *An explicit \(0.753659844\ldots\) lower bound for the unitary–exponential divisor-sum comparison density*, published mathematical research note, 2026, public published-finding corpus identifier `831dd476bf82`.
3. G. Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, referenced by Trudgian for the limiting-distribution argument.
