# An improved certified lower density bound for unitary and exponential divisor sums

## Finding
For \(n\ge1\), let \(\sigma^*(n)\) be the sum of unitary divisors and let \(\sigma^{(e)}(n)\) be the sum of exponential divisors. Put
\[
\delta=\lim_{X\to\infty}\frac1X\#\{n\le X:\sigma^*(n)>\sigma^{(e)}(n)\}.
\]
The existence of this density is established in the primary literature. We prove the **rigorous improved lower bound**
\[
\delta\ge \frac{384705031419237}{498500000000000}=0.771725238554\ldots>0.7717.
\]
This improves the earlier rigorous lower bound \(0.753659844064\ldots\). The constant is a rational certificate, not an experimental proportion.

## Assumptions and scope
The only arithmetic inputs are unique prime factorization, the classical CRT valuation densities, and the already established existence of \(\delta\). For a prime \(p\) and exponent \(e\ge0\), define
\[
r_p(0)=1,\qquad r_p(e)=\frac{1+p^e}{\sum_{d\mid e}p^d}\quad(e\ge1).
\]
The divisor \(d\mid e\) in the denominator is a **positive divisor of the exponent**. The ratio \(\sigma^*(n)/\sigma^{(e)}(n)\) equals \(\prod_p r_p(v_p(n))\). All logarithms below are natural. We use the finite prime cutoff \(P=997\), mesh \(H=100000\), integer probability scale \(M=10^{12}\).

For each \(p\le P\) use exponent cutoff \(E_p\) as follows: \(E_2=16\), \(E_3=12\), \(E_5=9\), \(E_7=7\), \(E_{11}=6\), \(E_{13}=5\), \(E_{17}=E_{19}=5\), \(E_{23}=E_{29}=E_{31}=E_{37}=E_{41}=E_{43}=4\), and \(E_p=3\) for all other primes through \(P\). These finite cutoffs are parameters of a reproducible certificate, not additional hypotheses on integers being counted.

## Proof
**1. Rational logarithmic enclosures.** For any positive rational \(q\), put \(u=(q-1)/(q+1)\), and
\[
S(q)=2\sum_{k=0}^{15}\frac{u^{2k+1}}{2k+1},\qquad
R(q)=\frac{2|u|^{33}}{33(1-u^2)}.
\]
The absolutely convergent atanh series yields \(S(q)-R(q)\le\log q\le S(q)+R(q)\). Consequently
\[
a_p(e)=\lfloor H(S(r_p(e))-R(r_p(e)))\rfloor,
\quad b_p(e)=\lceil H(S(r_p(e))+R(r_p(e)))\rceil
\]
are exact **integers**, computed with rational operations only, satisfying \(a_p(e)/H\le\log r_p(e)\le b_p(e)/H\).

**2. Finite prime valuation distributions.** For each fixed prime \(p\), the natural density of integers having \(v_p(n)=e\) is \((p-1)/p^{e+1}\) for \(e\ge0\). The density of those having \(v_p(n)\ge E_p\) is \(1/p^{E_p}\); valuations at distinct finite sets of primes are independent in the limiting CRT measure.

We retain only valuation classes \(0\le e<E_p\), assign shift \(a_p(e)\), and discard the remaining mass.

Starting from a single mass \(M\) at shift zero, combine these independent finite distributions by integer convolution. For a transition with current integer mass \(m\) and exact probability \(w=A/B\), add \(\lfloor mA/B\rfloor\). Because all weights are nonnegative, induction proves that every resulting bin underestimates its exact probability mass. The implementation uses unsigned 64-bit integer arrays; all intermediate multiplications are below \(2^{64}\), and the total mass is checked to remain below \(2M\). No floating-point computation participates in the certificate.

The replay gives integer mass \(L=772112456436\) in bins with summed shift \(\ge0\). Thus the density of finite valuation profiles with \(\prod_{p\le P}r_p(v_p(n))\ge1\) is **at least** \(L/M\).

**3. Infinite tail control.** Restrict the remaining primes \(p>P\) to exponents at most one. The product of their local ratios is then \(\ge1\), and it is strictly greater than one unless no such prime divides \(n\). The \(P\)-smooth integers have density zero. The density of the squarefree-tail restriction is \(\prod_{p>P}(1-p^{-2})\). Since \(P\) is odd, the prime union bound and integral comparison give
\[
\prod_{p>P}(1-p^{-2})\ge1-\sum_{p>P}p^{-2}
\ge1-\sum_{j\ge1}(P+2j)^{-2}\ge1-\frac1{2P}.
\]
Finite-prime CRT independence and squarefree-tail sieving therefore prove
\[
\delta\ge \frac{L}{M}\left(1-\frac1{2P}\right)
=\frac{384705031419237}{498500000000000}.
\]

Exact integer comparison gives the strict bound \(\delta>0.7717\).

## Verification
Run `python verify_unitary_density.py` with NumPy available. Every logarithmic enclosure uses `fractions.Fraction`; the probability convolution uses unsigned 64-bit integer operations, with explicit downward rounding on every transition. The script asserts the lower mass integer and the final strict lower inequality; it also includes an auxiliary upper-envelope diagnostic that is not claimed as new. Its reproducible output includes `VERIFY_OK`, the lower mass numerator and the exact rational lower endpoint. NumPy accelerates exact integer convolutions; it is not used for floating-point approximations. This proof does not infer infinite densities from finite counts of integers.

## Relationship to prior work
Trudgian (first public 2013-12-17) asked for this density, proved that its existence follows from the Erdős--Wintner framework, gave the squarefree lower bound \(6/\pi^2\), and reported an approximate proportion of \(0.778307\) through \(10^9\). OEIS A322446 provides further finite counts but no rigorous interval. A published later result supplied a lower bound \(0.753659844064\ldots\) from a six-prime cylinder enumeration. The present lower bound is strictly stronger and uses a certified finite-prime convolution with a rigorous squarefree-tail restriction.

## Limitations
The lower bound does not evaluate \(\delta\) exactly. The chosen cutoffs are not asserted optimal, and the squarefree-tail restriction intentionally discards many qualifying integers. A pre-existing, differently formulated sharper enclosure is a residual literature risk. No independent audit of the mathematics has been performed.

## References
1. T. Trudgian, *The sum of the unitary divisor function*, arXiv:1312.4615v1 (first public 2013-12-17); final version v3 (2014); Publications de l'Institut Mathématique 97 (2015), 175–180. https://arxiv.org/abs/1312.4615
2. *An explicit \(0.753659844\ldots\) lower bound for the unitary--exponential divisor-sum comparison density*, published mathematical finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-an-explicit-0-753659844-ldots-lower-bound-for-the-unitary-expone--831dd476bf82
3. OEIS A322446, comparison-count sequence and tabulation. https://oeis.org/A322446
