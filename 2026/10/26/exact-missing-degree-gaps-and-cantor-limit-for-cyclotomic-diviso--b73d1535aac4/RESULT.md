# Exact missing-degree gaps and Cantor limit for cyclotomic divisors with two-prime support

## Finding
For integers \(a,b\ge1\) and an odd prime \(p\), put \(M=2^a\), \(N=Mp^b\), and let \(\mathcal D_N\subseteq\{0,1,\ldots,N\}\) be the degrees of **monic divisors of \(X^N-1\) in \(\mathbb Z[X]\)**. Every degree is uniquely determined as a *number* by its value, whether or not multiple divisors realize it. The exact set is
\[
\mathcal D_N=\left\{u_0+(p-1)\sum_{j=1}^b p^{j-1}u_j:\ 0\le u_j\le M\text{ for }0\le j\le b\right\}.
\]
When \(p\le M+1\), this equals the whole interval \(\{0,\ldots,N\}\); the completeness of this case is already known from \(\varphi\)-practicality theory [1]. The additional description below concerns the complementary, noncomplete regime \(p>M+1\).

**Exact distinct-degree count and gaps.** For \(p>M+1\), the coefficient tuple \((u_0,\ldots,u_b)\) in the displayed expression is unique. Consequently,
\[
|\mathcal D_N|=(M+1)^{b+1},\qquad
|\{0,\ldots,N\}\setminus\mathcal D_N|=Mp^b+1-(M+1)^{b+1}.
\]
Order \(\mathcal D_N\) increasingly and record each difference between consecutive entries. Gap \(1\) occurs \(M(M+1)^b\) times. For every \(j\in\{1,\ldots,b\}\), the gap
\[
G_j=(p-1-M)p^{j-1}
\]
occurs \(M(M+1)^{b-j}\) times. If \(G_1=1\), the multiplicities of equal gap sizes should be added; this can only occur outside the strict noncomplete regime, so in the present theorem the values are distinct and exceed one. The largest gap is \((p-1-M)p^{b-1}\), occurring \(M\) times.

**Cantor scaling.** Fix \(a,p\) with \(p>M+1\). Give each *distinct degree* equal weight and normalize it by \(N\). As \(b\to\infty\), this probability distribution converges weakly to the law of
\[
Y=\frac{p-1}{M}\sum_{r=1}^\infty\frac{U_r}{p^r},
\]
where \(U_r\) are independent and uniformly distributed on \(\{0,1,\ldots,M\}\). The support is a self-similar Cantor subset of \([0,1]\) with Hausdorff dimension \(\log(M+1)/\log p\). The limit has no atoms and is singular with respect to Lebesgue measure. This is a degree-*support* theorem, not a theorem about the number of polynomial divisors of any fixed degree.

## Assumptions and scope
All parameters are exact integers; \(a,b\ge1\) and \(p\) is odd prime. The polynomial ring is \(\mathbb Z[X]\), not a finite-field polynomial ring. A divisor is taken monic, avoiding the irrelevant sign ambiguity. The cyclotomic factors of \(X^N-1\) are all distinct, and each has degree \(\varphi(d)\). No claim is made for integer moduli with three or more distinct prime factors, or for nonmonic factors.

## Proof
**1. Complete block representation.** By unique factorization over \(\mathbb Z[X]\), each monic divisor of \(X^N-1\) is a product of a subset of the distinct factors \(\Phi_d(X)\), with \(d\mid N\). Their degrees are the totients \(\varphi(d)\). The divisors of \(N=2^ap^b\) are \(2^ip^j\) with \(0\le i\le a\), \(0\le j\le b\). For \(j=0\) the totient-degree list is
\[
1,\ 1,\ 2,\ 4,\ldots,2^{a-1}.
\]
Its subset sums fill every integer from \(0\) to \(M\): starting from the two unit weights, each following weight is no larger than one plus the sum of its predecessors, and the total sum is \(M\). For a fixed \(j\ge1\), all weights are multiplied by \(\varphi(p^j)=(p-1)p^{j-1}\), so this block contributes exactly \((p-1)p^{j-1}u_j\) with \(0\le u_j\le M\). Blocks correspond to disjoint cyclotomic factors and can be selected independently. This proves the displayed exact representation for all parameters.

**2. Previously known complete regime.** If \(p\le M+1\), then \(p-1\le M\). For a block \((p-1)p^{j-1}u_j\), consecutive translated copies of the previously complete interval \([0,Mp^{j-1}]\) touch or overlap, since the new step is at most \(Mp^{j-1}+1\); the first starts at zero and the last ends at \(Mp^j\). Induction on \(j\) gives \(\mathcal D_N=\{0,\ldots,N\}\). This is also the specialized completeness conclusion of [1, Lemma 4.1].

**3. Unique digit tuples and ordering.** Assume \(p-1>M\). Equality of two representations implies \(u_0-v_0\equiv0\pmod{p-1}\); since \(|u_0-v_0|\le M<p-1\), necessarily \(u_0=v_0\). Divide the remaining equality by \(p-1\). Successive reductions modulo \(p\) show \(u_j=v_j\) for every \(1\le j\le b\), since \(0\le u_j,v_j\le M<p\). Thus all \((M+1)^{b+1}\) tuples give different degrees. For any \(j\ge1\), the *maximal total contribution* of lower indices \(0,\ldots,j-1\) is
\[
M+(p-1)M\sum_{i=1}^{j-1}p^{i-1}=Mp^{j-1},
\]
strictly less than the \(j\)-th place value \((p-1)p^{j-1}\). Therefore degree order is lexicographic order on \((u_b,u_{b-1},\ldots,u_0)\).

**4. Exact adjacent differences.** The least and greatest degrees are \(0\) and \(N=Mp^b\). In a lexicographic successor either \(u_0\) increases by one (gap \(1\)), or for exactly one \(j\ge1\), the digit \(u_j\) increases by one while every lower digit resets from \(M\) to \(0\). The second gap is
\[
(p-1)p^{j-1}-Mp^{j-1}=(p-1-M)p^{j-1}.
\]
The first event has \(M(M+1)^b\) occurrences, while the event at position \(j\) has \(M(M+1)^{b-j}\), accounting for every adjacent pair. Summing those multiplicities gives \((M+1)^{b+1}-1\), as required. The count of omitted degrees follows by subtracting from \(N+1\), or by summing the lengths of all omitted intervals between adjacent degrees.

**5. Limiting self-similar degree support.** Under the uniform distribution on distinct degrees, uniqueness from Step 3 makes the tuple \((u_0,\ldots,u_b)\) uniform on \(\{0,\ldots,M\}^{b+1}\). Reversing the independent digits in the normalized representation gives
\[
\frac{d}{Mp^b}=\frac{u_0}{Mp^b}+\frac{p-1}{M}\sum_{r=1}^b\frac{U_r}{p^r}.
\]
The first term and the infinite-series tail both tend uniformly to zero. Hence the random variables converge under a common coupling and their laws converge weakly to the law of \(Y\). Its support \(K\) satisfies
\[
K=\bigcup_{u=0}^M f_u(K),\qquad
f_u(t)=\frac{t+(p-1)u/M}{p}.
\]
Each \(f_u([0,1])\) has length \(p^{-1}\), and adjacent such intervals have strictly positive separation \((p-1-M)/(Mp)\). At depth \(k\), the support lies in \((M+1)^k\) disjoint level-\(k\) intervals of length \(p^{-k}\), giving the upper bound \(\dim_H K\le\log(M+1)/\log p\). Conversely the uniform cylinder mass is \((M+1)^{-k}\); positive level-one separation ensures each interval of length comparable to \(p^{-k}\) meets only boundedly many level-\(k\) cylinders. The mass-distribution estimate yields the reverse dimension inequality. Since \(M+1<p\), total covering length tends to zero; therefore \(K\) has Lebesgue measure zero. Each singleton corresponds to at most one digit sequence because intervals are disjoint, so its probability is at most \((M+1)^{-k}\) for every \(k\), hence zero. The law is singular continuous.

**Example.** For \(a=1\), \(p=5\), \(b=2\), one has \(M=2\), \(N=50\), and \(\mathcal D_N=\{u_0+4u_1+20u_2:0\le u_i\le2\}\). Exactly \(27\) degrees occur and \(24\) are missing. The adjacent gap profile consists of \(18\) unit gaps, \(6\) gaps of size \(2\), and \(2\) gaps of size \(10\).

## Verification
The accompanying standalone `verify.py` independently builds the possible degree set by subset-summing totients of **all positive divisors** of \(N\). For \(77\) parameter triples in both regimes with \(N\le20{,}000\), it compares this enumeration with the displayed digit formula, checks the full proposed gap histogram, the count and complement symmetry. These finite computations cross-check boundary behavior but are not substitutes for Steps 1–5, which prove the claims for all permitted parameters.

## Relationship to prior work
Thompson [1], particularly Lemma 4.1, proves when a prime power can be appended to a \(\varphi\)-practical integer while preserving representation of **every** degree. Pollack and Thompson [2] study the overall sets of attainable degrees and their distribution across moduli, not the gap histogram for the sparse two-prime family treated here. In the complete range, our completeness statement restates this established theory. The quantitatively new part assessed here is the exact lacunary gap multiset and the limiting singular continuous degree distribution in the noncomplete range. The OEIS practical-number index [3] is a database of which moduli are complete, not a table of these gap multiplicities. Published results about ordinary integer-divisor subset sums, or multiplicities of polynomial divisors for already-complete moduli, have different objects and do not establish the present gap and fractal formulas.

## Limitations
The argument concerns **distinct attainable degrees**, not counts of irreducible factors, of monic divisors giving an individual degree, or of divisors over finite fields. In particular, uniqueness of \((u_0,\ldots,u_b)\) does *not* assert uniqueness of the factor subset realizing a fixed block sum. The Cantor limit fixes \(a,p\) and lets \(b\) grow; no joint-parameter asymptotic is established. Publication priority is assessed against the cited accessible sources and targeted indexed claims, not guaranteed against unindexed equivalent statements. No independent validation is claimed.

## References
[1] Lola Thompson, *Polynomials with divisors of every degree*, arXiv:1111.5401 (first public version, 23 November 2011), especially §4, Lemma 4.1. https://arxiv.org/abs/1111.5401

[2] Paul Pollack and Lola Thompson, *On the degrees of divisors of T^n−1*, arXiv:1206.2084 (11 June 2012). https://arxiv.org/abs/1206.2084

[3] OEIS A260653, *Phi-practical numbers*. https://oeis.org/A260653
