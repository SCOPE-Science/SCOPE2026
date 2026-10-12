# Two logarithmic modal scales in order-\(k\) Poisson laws

## Finding
For each integer \(k\ge2\), let \(N_1,\ldots,N_k\) be independent Poisson variables, all with intensity \(\lambda>0\), and set
\[
X_{k,\lambda}=\sum_{j=1}^k jN_j.
\]
Define the **zero-mode threshold** and the **zero-versus-\(k\) crossover** by
\[
s_k=\sup\{\lambda>0:\Pr(X_{k,\lambda}=0)\ge\Pr(X_{k,\lambda}=x)\ \text{for every integer }x\ge1\},
\]
\[
r_k:\quad\Pr(X_{k,r_k}=k)=\Pr(X_{k,r_k}=0).
\]
The second equation has exactly one positive solution. As \(k\to\infty\) through integers,
\[
\boxed{s_k\sim\frac{\log k}{k},\qquad
2\sqrt{kr_k}=\log k-\frac12\log\log k+\log(2\sqrt{2\pi})+o(1).}
\]
Consequently,
\[
\boxed{r_k\sim\frac{(\log k)^2}{4k},\qquad
\frac{r_k}{s_k}\sim\frac{\log k}{4}\longrightarrow\infty.}
\]
For every \(k\ge2\), the crossover sequence satisfies \(r_{k+1}<r_k\). There is also the nonasymptotic bound
\[
s_k\ge\frac{\log(k+1)}{k}.
\]
For every sufficiently large \(k\), an intensity lies strictly between \(s_k\) and \(r_k\): zero has ceased to be a mode even though the mass at \(k\) is still smaller than the mass at zero. The winning positive index must exceed \(k\). These claims do not assert the exact finite-\(k\) first positive modal index.

## Assumptions and scope
The dimension/order \(k\) is a positive integer at least two and increases without any constraint on its rate; all Poisson components have the same positive intensity and are mutually independent. Probability masses are compared under the ordinary order on the nonnegative integers; ties count as modes. All logarithms are natural. Define the non-normalized probability coefficients
\[
h_k(x;\lambda)=e^{k\lambda}\Pr(X_{k,\lambda}=x)
=[z^x]\exp\!\left(\lambda\sum_{j=1}^k z^j\right),\qquad x\ge0.
\]
In particular, \(h_k(0;\lambda)=1\). For each positive integer \(x\), the function \(\lambda\mapsto h_k(x;\lambda)\) is a strictly increasing polynomial with nonnegative coefficients and zero constant term. Thus the set of intensities for which zero is a mode is an initial interval. It is nonempty by the lower bound below and bounded by the crossing with the mass at \(k\); hence \(0<s_k<\infty\). No independence between the jump magnitudes conditional on their number is assumed beyond the representation proved next.

## Proof
**1. The uniform-jump lower bound.** Let \(N=\sum_{j=1}^kN_j\). By Poisson superposition, \(N\sim\operatorname{Poisson}(k\lambda)\); conditional on \(N=n\), the sum \(X_{k,\lambda}\) is the sum of \(n\) independent variables uniform on \(\{1,\ldots,k\}\). Convolution of a probability distribution with this uniform law has maximum atom at most \(1/k\), so
\[
\Pr(X_{k,\lambda}=x)\le\frac{1-e^{-k\lambda}}{k},\quad x\ge1,
\qquad\Pr(X_{k,\lambda}=0)=e^{-k\lambda}.
\]
The zero atom therefore dominates all positive atoms whenever \(e^{-k\lambda}\ge1/(k+1)\), or \(\lambda\le\log(k+1)/k\). This proves the claimed bound.

**2. The matching asymptotic upper bound.** Fix \(\epsilon>0\), put \(L=\log k\), and choose \(\lambda=(1+\epsilon)L/k\). The exact mean and variance are
\[
\mu=\frac{\lambda k(k+1)}2,
\qquad \sigma^2=\frac{\lambda k(k+1)(2k+1)}6.
\]
Thus \(\mu\asymp kL\), \(\sigma\asymp k\sqrt L\), and \(\mu-2\sigma>0\) for all sufficiently large \(k\). Chebyshev's inequality places at least \(3/4\) of the probability on the positive integers in \([\mu-2\sigma,\mu+2\sigma]\), an interval containing at most \(4\sigma+3\) integers. Some positive integer consequently has mass at least
\[
\frac{3/4}{4\sigma+3}=\Omega\!\left(\frac{1}{k\sqrt{\log k}}\right).
\]
But the zero mass is exactly \(e^{-k\lambda}=k^{-(1+\epsilon)}\), eventually strictly smaller. Hence \(s_k\le(1+\epsilon)\log k/k\) eventually. Combine this with Step 1 and let \(\epsilon\downarrow0\) to conclude \(s_k\sim(\log k)/k\). The argument uses Chebyshev only to find an atom, not to approximate any particular atom.

**3. A finite polynomial for the competing crossover.** Extracting the coefficient of degree \(k\) from the generating function, or ordering \(m\) positive parts summing to \(k\), gives
\[
Q_k(\lambda):=h_k(k;\lambda)
=\sum_{m=1}^k\binom{k-1}{m-1}\frac{\lambda^m}{m!}.
\]
Since \(Q_k(0)=0\), \(Q_k(1)>1\) for \(k\ge2\), and \(Q_k\) is strictly increasing for positive \(\lambda\), there is exactly one \(r_k\in(0,1)\) with \(Q_k(r_k)=1\). The binomial coefficients satisfy
\[
Q_{k+1}(\lambda)>Q_k(\lambda)\quad(\lambda>0),
\]
where the inequality is strict already in the quadratic term. Their unique positive roots therefore satisfy \(r_{k+1}<r_k\).

**4. Uniform control by a Bessel series.** Write \(u=k\lambda\), and introduce
\[
F(u)=\sum_{m=1}^\infty\frac{u^m}{m!(m-1)!}
=\sqrt u\,I_1(2\sqrt u),\qquad u\ge0,
\]
with \(I_1\) the modified Bessel function. The binomial coefficient identity yields
\[
kQ_k(u/k)=\sum_{m=1}^k\frac{u^m}{m!(m-1)!}
\prod_{j=1}^{m-1}\left(1-\frac jk\right).
\]
For \(1\le m\le k\), the product loss is between zero and \(\sum_{j=1}^{m-1}j/k=m(m-1)/(2k)\). For \(m>k\), regard the product as zero; its loss of one is likewise bounded by \(m(m-1)/(2k)\). Termwise summation, together with
\[
\sum_{m\ge1}m(m-1)\frac{u^m}{m!(m-1)!}=uF(u),
\]
proves the **uniform comparison**, for all \(k\ge2\) and \(u\ge0\),
\[
\boxed{0\le F(u)-kQ_k(u/k)\le\frac{u}{2k}F(u).}
\]
No remainder estimate from a numerical fit is involved.

The standard fixed-order Bessel asymptotic \(I_1(t)=e^t/\sqrt{2\pi t}\,(1+O(t^{-1}))\), for real \(t\to+\infty\), gives
\[
F(u)=\frac{u^{1/4}e^{2\sqrt u}}{2\sqrt\pi}\bigl(1+O(u^{-1/2})\bigr),\qquad u\to\infty.
\]
Let \(u_k=kr_k\). For \(u=c(\log k)^2\), the last display yields \(F(u)=k^{2\sqrt c+o(1)}\). The comparison with \(kQ_k\), first at \(c=1/16\) and then at \(c=1\), and monotonicity of \(Q_k\), show
\[
\frac{(\log k)^2}{16}<u_k<(\log k)^2
\]
for all sufficiently large \(k\). Hence \(u_k=O((\log k)^2)\), and the boxed inequality evaluated at \(u_k\), where \(kQ_k(r_k)=k\), gives
\[
F(u_k)=k\bigl(1+O((\log k)^2/k)\bigr).
\]
Put \(t_k=2\sqrt{u_k}\). Using the Bessel asymptotic again,
\[
\log k=t_k+\frac12\log t_k-\log(2\sqrt{2\pi})+o(1).
\]
It follows first that \(t_k/\log k\to1\), and then, by substitution into the logarithm, that
\[
t_k=\log k-\frac12\log\log k+\log(2\sqrt{2\pi})+o(1).
\]
This proves the claimed second-order formula for \(r_k\), its leading equivalent, and the ratio \(r_k/s_k\sim(\log k)/4\).

**5. Consequence for the first modal change.** Since \(s_k/r_k\to0\), for each sufficiently large \(k\) choose \(\lambda\) strictly between the thresholds. Then zero is not a mode, so \(h_k(x;\lambda)>1\) for some \(x\ge1\), while \(h_k(k;\lambda)<1\). For \(1\le x\le k\), the same coefficient formula with \(k\) replaced by \(x\) shows \(h_k(x;\lambda)\le h_k(k;\lambda)\), because \(\binom{x-1}{m-1}\le\binom{k-1}{m-1}\). Thus the competing value \(x\) necessarily exceeds \(k\).

As an exact finite illustration, with \(k=15\) and \(\lambda=501/2000\), direct rational coefficient evaluation gives
\[
h_{15}(15;501/2000)<1<h_{15}(25;501/2000).
\]
The existence of a non-\(k\) first mode for this order was previously reported numerically; the rational comparison here is a reproducibility check, **not** a claim of novelty for that example.

## Verification
Run `python3 verify.py` from the directory containing this file and the provided verifier. It uses only Python's standard library. It computes each of 32 finite examples twice, using (i) the generating-function derivative recurrence and (ii) truncated products of exponential generating factors; checks the degree-\(k\) polynomial formula; certifies the two strict rational inequalities at \(k=15\); checks monotonicity of nine numerically approximated crossovers; and tests finite instances of the Bessel-series comparison. These tests validate identities and illustrations independently of the analytic proof, but are **not** proofs of asymptotic limits, uniqueness for all \(k\), or eventual modal behavior.

## Relationship to prior work
Georghiou, Philippou, and Saghafi (2013) derive general bounds for the location of modes and the generating-function recurrence. Philippou (2014) proves a sufficient zero-mode range of order \(k^{-2}\) and completely treats order two. Kwon and Philippou (2023) define the root \(r_k\), treat orders three and four, and explicitly ask whether zero stays modal until \(r_k\) and how \(r_k\) decreases. These are starting results and questions, not results newly asserted here.

Mane's September 2023 notes numerically exhibit the first non-\(k\) double mode at order 15 and prove monotonic decrease of the zero-mode threshold. They do not derive the logarithmic equivalents above. One note fits the finite-range data to a conjectural power law for the zero-mode threshold with exponent \(-7/8\); its own text labels that fit numerical, not proved. The first theorem here establishes a different **true asymptotic order** and explains why a finite-range power fit cannot determine the limiting exponent. A companion October 2023 note supplies other probability-mass inequalities and conditional bounds, not these global thresholds. The special-function asymptotic is a standard result of the NIST Digital Library of Mathematical Functions.

## Limitations
The theorem does not compute the exact finite-\(k\) threshold \(s_k\), the first positive modal location, or the full mode diagram. It does not claim that the first departing index exceeds \(k\) for every \(k\): the conclusion is eventual. The asymptotics may converge slowly. Equivalent earlier formulations outside the inspected literature may exist; no claim of exhaustive bibliographic priority is made. The displayed finite computations cannot certify the infinite statements by themselves.

## References
1. C. Georghiou, A. N. Philippou, and A. Saghafi, *On the Modes of the Poisson Distribution of Order k*, Fibonacci Quarterly 51 (2013), 44–48. https://fq.math.ca/Papers1/51-1/GeorghiouPhilippouSaghafi.pdf
2. A. N. Philippou, *A Note on the Modes of the Poisson Distribution of Order k*, Fibonacci Quarterly 52 (2014), 203–205. https://fq.math.ca/Papers1/52-3/Philippou12302013.pdf
3. Y. Kwon and A. N. Philippou, *The Modes of the Poisson Distribution of Order 3 and 4*, Entropy 25 (2023), 699; first published 2023-04-21. https://doi.org/10.3390/e25040699
4. S. R. Mane, *Asymptotic results for the Poisson distribution of order k*, arXiv:2309.05190 (first submitted 2023-09-11). https://arxiv.org/abs/2309.05190
5. S. R. Mane, *First double mode of the Poisson distribution of order k*, arXiv:2309.09278 (first submitted 2023-09-17). https://arxiv.org/abs/2309.09278
6. S. R. Mane, *Analytical proofs for the properties of the probability mass function of the Poisson distribution of order k*, arXiv:2310.00827 (first submitted 2023-10-02). https://arxiv.org/abs/2310.00827
7. NIST Digital Library of Mathematical Functions, §10.40(i), Eq. 10.40.1 (fixed-order large-argument asymptotic for \(I_\nu\)). https://dlmf.nist.gov/10.40.E1
