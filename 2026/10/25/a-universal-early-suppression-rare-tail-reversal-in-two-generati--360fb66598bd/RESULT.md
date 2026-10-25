# A universal early-suppression rare-tail reversal in two-generation Poisson epidemics

## Finding

In an exactly specified two-generation epidemic branching model, consider two temporary transmission policies using the same positive offspring means in opposite orders. Let \(0<a<b\). In the early-suppression policy, the initial infective produces \(\operatorname{Poisson}(a)\) cases and each of those produces independent \(\operatorname{Poisson}(b)\) second-generation cases. The late-suppression policy interchanges \(a\) and \(b\). Write \(C_{a,b}\) and \(C_{b,a}\) for their respective total numbers of new infections through generation two, *excluding* the index case.

The early-suppression policy has fewer expected new infections and a greater probability of preventing every secondary infection:
\[
\mathbb E C_{a,b}=a+ab<b+ab=\mathbb E C_{b,a},\qquad
\Pr(C_{a,b}=0)=e^{-a}>e^{-b}=\Pr(C_{b,a}=0).
\]
In fact, the early-suppression law is strictly smaller in probability-generating-function order:
\[
\mathbb E[z^{C_{a,b}}]>\mathbb E[z^{C_{b,a}}]\qquad(0\le z<1).
\]
Yet the ordering reverses at *every sufficiently high outbreak threshold*, with the sharp exponential comparison
\[
\boxed{\lim_{n\to\infty}\left(
\frac{\Pr(C_{a,b}\ge n)}{\Pr(C_{b,a}\ge n)}
\right)^{1/n}=\frac ba>1.}
\]
More precisely, for arbitrary positive parameters \(c,d\),
\[
\lim_{n\to\infty}\left[\frac1n\log\Pr(C_{c,d}\ge n)+\log\log n\right]=\log d.
\]
Thus front-loading the stronger transmission reduction lowers both the mean and all probabilities of zero-or-light outbreaks measured by the probability generating function, but eventually produces a larger *catastrophic* outbreak tail. The late-generation reproduction parameter controls the logarithmic rare-event coefficient; the first-generation parameter drops out of that coefficient.

For a concrete non-asymptotic example, at \((a,b)=(1/2,2)\) the early-minus-late probability of at least twelve new cases is \(0.0003060185540125093\ldots>0\), although the means are \(3/2\) and \(3\), respectively. All thresholds from one through eleven instead favor early suppression in the usual survival-tail sense.

## Assumptions and scope

There is exactly one index case in generation zero. All individuals are infectious for one generation. Under parameter sequence \((c,d)\), first-generation case count \(K\) has Poisson mean \(c\); conditional on \(K=k\), second-generation case count \(Y\) has Poisson mean \(dk\). Offspring transmissions are mutually independent conditional on their parents and can contact arbitrarily many fresh susceptibles. Define \(C_{c,d}:=K+Y\), a nonnegative integer-valued random variable. All parameters satisfy \(c,d>0\); early suppression requires \(0<a<b\).

This is an exact theorem for the two-generation, infinite-susceptible-reservoir branching model, not an exact theorem about a finite-network SIR process with depletion. A Poisson-degree, locally tree-like contact-network branching approximation with generation-specific thinning has precisely these offspring laws when the unthinned contact mean is at least \(b\). The rate ordering represents temporary suppression that may be relaxed, not a monotone cumulative-vaccination rollout.

## Proof

**The generating function and ordinary indicators.** Conditional Poisson summation gives, for every real \(z\ge0\),
\[
G_{c,d}(z):=\mathbb E[z^{C_{c,d}}]
=\mathbb E\left[(z e^{d(z-1)})^K\right]
=\exp\{c(z e^{d(z-1)}-1)\}.
\]
This is a compound-Poisson law with positive jump size \(1+\operatorname{Poisson}(d)\). Differentiating at one gives \(\mathbb E C_{c,d}=c(1+d)\). Since each jump is positive, \(\Pr(C_{c,d}=0)=e^{-c}\).

For \(z\in[0,1)\), put \(t=1-z>0\) and \(h(t)=b e^{-at}-a e^{-bt}\). Because \(0<a<b\), we have \(h(t)>0\), \(h(0)=b-a\), and
\[
h'(t)=ab(e^{-bt}-e^{-at})<0.
\]
Consequently \(0<h(t)<b-a\). Subtracting the two logarithmic generating functions yields
\[
\log G_{a,b}(z)-\log G_{b,a}(z)
=(b-a)-z h(1-z)>0.
\]
This proves strict generating-function order, and the mean and zero-case inequalities follow as above.

**A sharp tail lemma.** Fix \(c,d>0\) and define \(Q_n=\Pr(C_{c,d}\ge n)\), for integer \(n\ge1\). We show
\[
\log Q_n=-n\log\log n+n\log d+o(n).
\]
For the upper bound, for sufficiently large \(n\) choose
\[
z_n=\frac{\log n-2\log\log n}{d}>1.
\]
The generating function is finite for every positive \(z\). Markov's inequality implies
\[
Q_n\le z_n^{-n}\exp\{c(z_n e^{d(z_n-1)}-1)\}.
\]
Since \(e^{d(z_n-1)}=e^{-d}n/(\log n)^2\), the logarithm of the exponential factor is \(O(n/\log n)=o(n)\); also \(\log z_n=\log\log n-\log d+o(1)\). Therefore
\[
\limsup_{n\to\infty}\left[\frac{\log Q_n}{n}+\log\log n\right]\le\log d.
\]

For the matching lower bound, put \(m_n=\lfloor n/\log n\rfloor\) and \(j_n=n-m_n\), so that \(m_n\ge1\) for large \(n\). The event \(K=m_n\) and \(Y=j_n\) is contained in \(\{C_{c,d}\ge n\}\) and has probability exactly
\[
e^{-c}\frac{c^{m_n}}{m_n!}
 e^{-dm_n}\frac{(dm_n)^{j_n}}{j_n!}.
\]
Here \(m_n/n\to0\), \(m_n\log m_n/n\to1\), \(j_n/n\to1\), and \(\log(j_n/(dm_n))=\log\log n-\log d+o(1)\). Applying \(\log(j!)=j\log j-j+O(\log(j+1))\) to both factorials shows that the logarithm of this particular event probability is
\[
-n\log\log n+n\log d+o(n).
\]
This proves the matching lower bound and hence the tail lemma. Neither truncation of a distribution nor empirical extrapolation is used.

Apply this lemma once with \((c,d)=(a,b)\) and once with \((c,d)=(b,a)\). Subtraction gives
\[
\log\frac{\Pr(C_{a,b}\ge n)}{\Pr(C_{b,a}\ge n)}
=n\log(b/a)+o(n).
\]
Because \(b/a>1\), the ratio eventually exceeds one for **every** sufficiently large integer threshold, and taking the \(n\)-th root proves the boxed formula.

## Verification

The standalone script `verify_poisson.py` requires only Python's standard library. It computes first-generation-conditioned finite probabilities and, separately, coefficients from the logarithmic-derivative recurrence
\[
p_0=e^{-c},\qquad
np_n=ce^{-d}\sum_{j=1}^n
\frac{j d^{j-1}}{(j-1)!}p_{n-j}.
\]
It compares both methods at four positive parameter pairs through degree 32, tests generating-function inequalities at 20 points per pair, and examines exact finite-tail formulas at the illustrative crossover. Executing the packaged script passed 646 numerical checks at 67-decimal-digit working precision. The infinite-tail law and all-parameter conclusions are established by the proof, not by these checks.

For the example, \(\Pr(C_{1/2,2}\ge12)-\Pr(C_{2,1/2}\ge12)=0.000306018554012509325\ldots\), computed by subtracting finite sums of generating-function coefficients from one. All those coefficients also have the independent conditional-Poisson formula
\[
p_n=\sum_{k=0}^n e^{-c}\frac{c^k}{k!}
 e^{-dk}\frac{(dk)^{n-k}}{(n-k)!},
\]
where the \(k=0\) term for \(n>0\) is understood to be zero.

## Relationship to prior work

Boudreau, Allen, Roberts, Allard and Hébert-Dufresne (2023) establish a generation-dependent epidemic probability-generating-function framework and multiple outbreak-risk comparison metrics. Their equations (6)–(9) encompass changing generation-specific offspring laws, and Sections 3–5 discuss risk metrics and numerical crossings for vaccination policies. Those model ingredients and the broad observation that intervention rankings depend on the metric are prior work. The present result gives a distinct all-parameter analytical policy-order comparison, a rigorous eventually reversed *upper tail*, and the exact asymptotic log-tail coefficient in a two-generation Poisson specialization; no first invention of branching-process generating functions or metric disagreements is claimed.

Compound-Poisson and Neyman type-A distributions are classical. Zheng (1995) treats asymptotic approximations of the conventional Neyman type-A tail, while Bening and Korolev (2022) compare compound-Poisson distributions by a different, normal-quantile deficiency notion. Those are relevant mathematical predecessors, not claimed as novel here. In the present model each primary transmission creates a marked cluster of size \(1+\operatorname{Poisson}(d)\), and the theorem jointly compares opposite chronological placements of \(a\) and \(b\). Broader asymptotic theory might eventually be found to subsume the log-tail lemma; research priority is not a mathematical consequence of this proof.

## Limitations

The result concerns exactly two generations and a Poisson branching reservoir, not a depletion-limited, behaviorally adaptive, or heterogeneous finite epidemic. For each fixed finite population there is a maximum possible outbreak size, so the unbounded-tail limit is inapplicable without a branching-scale limit. The asymptotic statement gives no uniform explicit threshold \(n_0(a,b)\), and the threshold may be extremely high when the two means are close. The claim does not say that front-loading interventions is inadvisable in practice: early suppression has lower expected burden and favors every probability-generating-function objective evaluated here. Other effectiveness measures and costs have not been modeled.

## References

1. M. C. Boudreau, A. J. Allen, N. J. Roberts, A. Allard, and L. Hébert-Dufresne, *Temporal and Probabilistic Comparisons of Epidemic Interventions*, Bulletin of Mathematical Biology 85 (2023), article 118, DOI: 10.1007/s11538-023-01220-w. Earliest arXiv posting February 7, 2023: https://arxiv.org/abs/2302.03210. Accessible full text: https://antoineallard.github.io/contributions/articles/BullMathBiol.2023.85.118.Boudreau.Temporal_and_probabilistic_comparisons_of_epidemic_interventions.pdf.
2. Q. Zheng, *A note on an approximation to Neyman type A distributions*, Communications in Statistics - Simulation and Computation 24 (1995), 889–895, DOI: 10.1080/03610919508813282.
3. V. Bening and V. Korolev, *Comparing Compound Poisson Distributions by Deficiency: Continuous-Time Case*, Mathematics 10 (2022), 4712, DOI: 10.3390/math10244712.
