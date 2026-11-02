# Alternating boundary-vacancy covariance in finite Page–Rényi dimer parking

## Finding

For the uniformly prioritized random sequential adsorption of length-two dimers on a path of \(n\) sites, let \(U_n\) and \(V_n\) be the indicators that the first and last sites, respectively, remain vacant at jamming. For every integer \(n\ge3\),

\[
(-1)^n\operatorname{Cov}(U_n,V_n)>0.
\]

The endpoint covariance is strictly negative for every odd length and strictly positive for every even length. Moreover,

\[
\operatorname{Cov}(U_n,V_n)=(-1)^n\frac{2^{n-2}}{(n-1)!}\left(1+O\left(\frac1n\right)\right),\quad n\to\infty.
\]

The exact answer, for \(n\ge4\), is

\[
\operatorname{Cov}(U_n,V_n)=\sum_{j=0}^{n-4}\frac{(-2)^j}{j!}-\frac{2(-2)^{n-4}}{(n-1)(n-4)!}-\left(\sum_{j=0}^{n-1}\frac{(-1)^j}{j!}\right)^2.
\]

At \(n=3\), the covariance is \(-1/4\); at \(n=2\), it is zero. This describes a complete finite-size sign classification, not merely an infinite-lattice limit.

## Assumptions and scope

Fix an integer \(n\ge2\). Sites \(1,\dots,n\) form a path, with possible dimers covering \((i,i+1)\) for \(1\le i<n\). Draw independent, identically distributed continuous priorities for its \(n-1\) edges and process the edges in increasing priority order. Accept an edge precisely when neither endpoint has previously been covered; rejected attempts do nothing. At the end every available edge has been attempted, and no further dimer can fit. The ordering is a uniform permutation of edges. Define \(U_n=1\) precisely when site \(1\) is uncovered, and \(V_n=1\) precisely when site \(n\) is uncovered. All covariance statements refer to this finite random parking law.

By reflection \(\mathbb E U_n=\mathbb E V_n=:a_n\). Set \(b_n=\mathbb E(U_nV_n)\). The artificial one-site model has \(a_1=b_1=1\), used solely as a base case; for two sites \(a_2=b_2=0\).

## Proof

**Single-end marginal.** For \(n\ge3\), condition on the first attempted edge, uniformly among \(n-1\) edges. To leave the leftmost site vacant, the first edge cannot be \((1,2)\). If it is \((i,i+1)\) for \(i\ge2\), the left fragment of \(i-1\) sites evolves independently under uniformly ordered remaining priorities. Hence

\[
(n-1)a_n=\sum_{k=1}^{n-2}a_k,
\quad a_1=1,\quad a_2=0.
\]

The unique solution is \(a_n=\sum_{j=0}^{n-1}(-1)^j/j!\), which can be checked directly from the recurrence, or from \(A(z)=\sum_{n\ge1}a_nz^n=ze^{-z}/(1-z)\).

**Joint endpoints.** To leave both endpoints vacant, the first accepted edge must be \((i,i+1)\) with \(2\le i\le n-2\), splitting the remaining problem into independent left and right fragments of respective lengths \(i-1\) and \(n-i-1\). Thus for \(n\ge4\),

\[
(n-1)b_n=\sum_{k=1}^{n-3}a_k a_{n-k-2}=[z^{n-2}]A(z)^2.
\]

Since \(A(z)^2=z^2e^{-2z}/(1-z)^2\), evaluating the coefficient gives

\[
b_n=\sum_{j=0}^{n-4}\frac{(-2)^j}{j!}-\frac{2(-2)^{n-4}}{(n-1)(n-4)!}.
\]

**Strict sign.** For \(n\ge4\), write \(m=n-4\) and

\[
I_m=\int_0^1(1-u)^m e^{-2u}\,du.
\]

Taylor's integral remainder yields

\[
b_n-e^{-2}=\frac{2(-2)^m}{m!}\left(I_m-\frac1{m+3}\right).
\]

If \(W\) has the \(\operatorname{Beta}(1,m+1)\) distribution, then \(I_m=\mathbb E(e^{-2W})/(m+1)\). Strict Jensen convexity and \(\mathbb EW=1/(m+2)\) imply

\[
I_m>\frac{e^{-2/(m+2)}}{m+1}>\frac1{m+3}.
\]

For the last strict inequality, put \(t=1/(m+2)\in(0,1)\) and use \(\log((1+t)/(1-t))>2t\). Therefore \(\operatorname{sign}(b_n-e^{-2})=(-1)^n\). The strict alternating-series remainder for \(e^{-1}\) gives \(\operatorname{sign}(a_n-e^{-1})=(-1)^{n-1}\), hence the same sign for \(a_n^2-e^{-2}\). Their difference \(b_n-a_n^2\) consequently has the sign \((-1)^n\). For \(n=3\), direct conditioning gives \(a_3=1/2\), \(b_3=0\).

**Sharp scale.** The beta integral admits the expansion

\[
I_m=\frac1{m+1}-\frac2{(m+1)(m+2)}+\frac4{(m+1)(m+2)(m+3)}+O(m^{-4}),
\]

where the remainder comes from Taylor's theorem for \(e^{-2u}\) and the beta moments. Thus

\[
I_m-\frac1{m+3}=\frac{2}{(m+1)(m+2)(m+3)}(1+O(m^{-1})).
\]

It follows that

\[
b_n-e^{-2}=(-1)^n\frac{2^{n-2}}{(n-1)!}(1+O(n^{-1})).
\]

Finally the alternating-series bound gives \(|a_n-e^{-1}|\le1/n!\), so \(a_n^2-e^{-2}=O(1/n!)\), asymptotically negligible on the preceding scale. This proves the stated covariance expansion.

## Verification

The accompanying `verify.py` uses only Python's standard library. It checks the exact marginal and joint recurrences, the closed form and strict sign for each \(3\le n\le120\), independently exhausts every edge ordering for \(1\le n\le8\), and computes exact-rational scaled asymptotic ratios at five larger sizes. Its execution produced 390 passing exact assertion groups. Enumeration checks small instances and is not substituted for the all-size proof.

## Relationship to prior work

Gerin's *The Page–Rényi parking process* (first publicly posted as arXiv:1411.8002 on 2014-11-28) studies the self-review, including the exact priority-order construction, an infinite-line vacancy marginal and a factorial-decay bound for spatial correlations. The fully inspected preprint does not state a finite-path covariance formula for the two endpoints or the exact parity sign and coefficient proved here. Flajolet's *A Seating Arrangement Problem* treats the equivalent unfriendly-seating model, principally through the count of occupied places. Earlier work by Page and broad treatments of one-dimensional adsorption provide the underlying splitting technique and correlation context. In particular, Bonnier, Boyer and Viot (1994) derive a pair distribution for one-dimensional adsorption; the accessible abstract does not determine whether a finite-path endpoint specialization is present. Its full text and Page's 1959 full text were not accessible for direct comparison, so full historical priority remains uncertain. These limitations do not affect the mathematical proof.

## Limitations

The result concerns length-two random sequential adsorption on a finite **path**, using exchangeable continuous edge priorities and the terminal jammed configuration. It does not establish corresponding sign laws for cycles, nonuniform attempts, longer particles or intermediate-time occupancy. Its strict sign proof uses path decomposition and does not derive general finite-lattice two-point functions. Independent literature priority confirmation has not been performed.

## References

- L. Gerin, *The Page–Rényi parking process*, arXiv:1411.8002v1 (publicly posted 2014-11-28), *Electronic Journal of Combinatorics* 22(4), P4.4 (2015). https://arxiv.org/abs/1411.8002 .
- P. Flajolet, *A Seating Arrangement Problem* (1997). https://algo.inria.fr/libraries/autocomb/fatmen-html/fatmen1.html .
- E. S. Page, *The Distribution of Vacancies on a Line*, *Journal of the Royal Statistical Society, Series B* 21(2), 364–374 (1959). https://academic.oup.com/jrsssb/article/21/2/364/7027981 .
- B. Bonnier, D. Boyer, and P. Viot, *Pair correlation function in random sequential adsorption processes*, *J. Phys. A: Math. Gen.* 27, 3671 (1994). https://doi.org/10.1088/0305-4470/27/11/017 .
- J. W. Evans, *Random and cooperative sequential adsorption*, *Rev. Mod. Phys.* 65, 1281 (1993). https://doi.org/10.1103/RevModPhys.65.1281 .
