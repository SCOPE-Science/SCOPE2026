# A signed finite-size shift for the rho length of fixed-in-degree random mappings

## Finding
Fix an integer \(d\ge2\). Let \(n\) range through multiples of \(d\). Uniformly choose a function \(F:[n]\to[n]\) having exactly \(n/d\) target vertices of indegree \(d\) and all remaining target vertices of indegree zero. The locations of the positive indegrees may be fixed in advance (the resulting law below is invariant under them). Independently choose \(U\) uniformly from \([n]\). Define the rho length \(R_n\) as the least positive \(r\) such that \(F^r(U)\) agrees with one of \(U,F(U),\ldots,F^{r-1}(U)\). Thus \(R_n\) counts distinct visited states before the first repeat.

For every integer \(0\le k\le n/d\), the exact tail is
\[
\Pr(R_n>k)=\left(1-\frac{k}{n}\right)\prod_{j=0}^{k-1}\frac{n-dj}{n-j},
\]
where the empty product equals one, and the tail is zero for larger \(k\). Consequently, for fixed \(d\),
\[
\boxed{\mathbb E R_n=\sqrt{\frac{\pi n}{2(d-1)}}+\frac{2d-7}{3(d-1)}+O_d(n^{-1/2}).}
\]
The order-one correction changes sign: it equals \(-1\) for \(d=2\), \(-1/6\) for \(d=3\), \(1/9\) for \(d=4\), and is strictly positive for all larger integer \(d\). This is an asymptotic refinement of the known leading Rayleigh mean, not a new leading limit theorem.

## Assumptions and scope
The total number of vertices \(n\) is positive and divisible by fixed \(d\ge2\). Indegrees are exactly zero or \(d\); each admissible mapping has equal probability, and the starting vertex is independently uniform over all \(n\) vertices. The expectation is jointly over mapping and start. The error constant may depend on \(d\) and is not asserted uniform for growing \(d\).

## Proof
**Exact enumeration.** For any prescribed nonnegative indegrees \((b_v)_{v\in[n]}\) summing to \(n\), denote by \(e_k(b)\) their \(k\)-th elementary symmetric polynomial. Conditioning on a distinct ordered image path \((v_1,\ldots,v_k)\) of \(k\) distinct targets, the probability of the corresponding \(k\) assignments is \(\prod_{i=1}^k b_{v_i}/(n)_k\), where \((n)_k=n(n-1)\cdots(n-k+1)\). Of the \(n\) possible uniform starting vertices, precisely \(n-k\) avoid that path's target set. Summing over all \(k!\) orderings of every \(k\)-set gives
\[
\Pr(R_n>k)=\frac{n-k}{n}\frac{k!e_k(b)}{(n)_k}=\frac{n-k}{n}\frac{e_k(b)}{\binom nk}.
\]
For the required indegrees, \(e_k(b)=d^k\binom{n/d}{k}\) for \(k\le n/d\), and zero afterward. Cancelling binomials produces the displayed finite product. In particular \(R_n\le n/d+1\) almost surely.

**Gaussian window and uniform remainder.** Set \(a=d-1>0\), \(B=a/2-1\), and \(C=(d^2-1)/6\), and write \(S_n(k)=\Pr(R_n>k)\). For \(0\le k\le K_n=\lfloor\sqrt n\log n\rfloor\), expansion of \(\log(1-z)\), with sums of integer powers, gives
\[
\log S_n(k)=-\frac{ak^2}{2n}+\frac{Bk}{n}-\frac{Ck^3}{n^2}+O_d\left(\frac{k^2+1}{n^2}+\frac{k^4}{n^3}\right).
\]
Indeed \(\log(1-k/n)=-k/n+O(k^2/n^2)\), and
\[
\sum_{j=0}^{k-1}\log\frac{1-dj/n}{1-j/n}=-\frac{a}{n}\sum_{j<k}j-\frac{d^2-1}{2n^2}\sum_{j<k}j^2+O_d(k^4/n^3).
\]
The exponential Taylor bound, with the Gaussian weight retained, then yields
\[
\sum_{k=0}^{K_n}\left|S_n(k)-e^{-ak^2/(2n)}\left(1+\frac{Bk}{n}-\frac{Ck^3}{n^2}\right)\right|=O_d(n^{-1/2}).
\]
For clarity, the pointwise remainder is bounded by a constant times \(e^{-ak^2/(2n)}\) multiplied by \((k^2+1)/n^2+k^4/n^3+(k/n+k^3/n^2)^2\). Gaussian moment sums make its total \(O_d(n^{-1/2})\). Moreover, because \((n-dj)/(n-j)\le\exp(-aj/n)\) whenever the product is nonzero,
\[
S_n(k)\le \exp[-ak(k-1)/(2n)].
\]
For \(k>K_n\), both this survival tail and the Gaussian comparison tails sum to less than any fixed negative power of \(n\). Therefore the approximation may be summed to infinity.

**Evaluation of the sum.** The tail-sum identity gives \(\mathbb E R_n=\sum_{k\ge0}S_n(k)\). Standard half-line Gaussian summation (Euler–Maclaurin, or one rectangle-rule estimate plus the endpoint correction) gives
\[
\sum_{k\ge0}e^{-ak^2/(2n)}=\sqrt{\frac{\pi n}{2a}}+\frac12+O_a(n^{-1/2}),
\]
\[
\sum_{k\ge0}\frac{k}{n}e^{-ak^2/(2n)}=\frac1a+O_a(n^{-1/2}),\qquad
\sum_{k\ge0}\frac{k^3}{n^2}e^{-ak^2/(2n)}=\frac2{a^2}+O_a(n^{-1/2}).
\]
Consequently the constant correction equals
\[
\frac12+\frac Ba-\frac{2C}{a^2}
=1-\frac1a-\frac{d+1}{3a}
=\frac{2d-7}{3(d-1)}.
\]
Its sign is that of \(2d-7\), establishing the threshold and completing the proof.

## Verification
The accompanying standalone `check.py` enumerates every admissible map and starting vertex for six small \((n,d)\) choices, comparing its exact rational tail law both with the elementary-symmetric form and the finite-product form. It independently computes the exact means and checks convergence of five moderate-size mean offsets toward the stated constants. Run `python3 check.py`. The finite checks are not used to establish the asymptotic theorem, which follows from the analytic estimates above.

## Relationship to prior work
Leckey and Wormald (first public version 2018-03-07) establish the leading Rayleigh limit, moment convergence, and a general exact path-enumeration identity (their Lemma 3.2). The finite-product identity above is a specialization and averaging of that known identity, **not** claimed as original. The contribution asserted here is the explicit order-one asymptotic correction across the natural \(\{0,d\}\) family and its sign transition. Earlier restricted-mapping studies by Martins, Panario, Qureshi, and Schmutz focus on global cycle-period statistics; the 2015 Martins–Panario study addresses rho-length heuristics but its full text was not accessible during this comparison. That leaves a specific historical-priority risk for the correction. No claim is made that this finite-size baseline transfers unchanged to any polynomial iteration law.

## Limitations
The model is an idealized uniform restricted-in-degree mapping; actual polynomial maps may contain exceptional vertices of indegree one, whose effects can matter at the same order as the correction. Fixed positive \(d\) is necessary for the stated remainder. Although the exact distribution was previously implicit in general enumeration, the new constant term itself has not been independently priority certified. Independent mathematical validation has not been performed.

## References
1. K. Leckey and N. Wormald, *A limit theorem for the six-length of random functional graphs with a fixed degree sequence*, arXiv:1803.02667v1, first posted 2018-03-07; *Electronic Journal of Combinatorics* 26(4), P4.35 (2019). https://arxiv.org/abs/1803.02667
2. R. S. V. Martins, D. Panario, C. Qureshi, and E. Schmutz, *Periods of iterations of functions with restricted preimage sizes*, arXiv:1701.09148, first posted 2017-01-31; *AofA 2018*, article 30. https://doi.org/10.4230/LIPIcs.AofA.2018.30
3. R. S. V. Martins and D. Panario, *On the heuristic of approximating polynomials over finite fields by random mappings*, arXiv:1505.02983, first posted 2015-05-12. https://arxiv.org/abs/1505.02983
4. J. Hansen and J. Jaworski, *Random mappings with exchangeable in-degrees*, arXiv:math/0603529; *Random Structures & Algorithms* 33 (2008), 105–126. https://arxiv.org/abs/math/0603529
