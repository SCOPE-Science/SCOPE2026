# Exact subsequence-universality law for binary words with runs of length at most two

## Finding

Let \(\mathcal L_n\) be the binary words of length \(n\) avoiding the contiguous factors \(000\) and \(111\). For a word \(w\), let \(\iota(w)\) be the greatest nonnegative integer \(k\) for which **every** binary word of length \(k\) is a scattered subsequence of \(w\). Put
\[
N_{n,k}=\bigl|\{w\in\mathcal L_n:\iota(w)=k\}\bigr|,
\qquad N_{0,0}=1.
\]
For all integers \(n,k\geq0\), the exact bivariate ordinary generating function is
\[
\boxed{\sum_{n,k\geq0}N_{n,k}z^nu^k
=\frac{1+2z+2z^2+uz^3}{1-u(2z^2+z^3)}.}
\]
In particular, write \(B_{r,j}=[z^j](2+z)^r\), with \(B_{r,j}=0\) if \(j<0\) or \(j>r\). For \(k\geq1\), putting \(j=n-2k\), one has the exact finite formula
\[
\boxed{N_{n,k}=B_{k,j}+2B_{k,j-1}+2B_{k,j-2}+B_{k-1,j-1},
\quad B_{r,j}=2^{r-j}\binom rj\text{ for }0\leq j\leq r.}
\]
The \(k=0\) counts are \(N_{0,0}=1\), \(N_{1,0}=2\), \(N_{2,0}=2\), and \(N_{n,0}=0\) for \(n\geq3\). The total number of admissible words is \(2F_{n+1}\) for \(n\geq1\), where \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\).

If \(W_n\) is uniform on \(\mathcal L_n\), then, as \(n\) tends to infinity,
\[
\boxed{\mathbb E\iota(W_n)=\frac n{\sqrt5}+O(1),\quad
\operatorname{Var}(\iota(W_n))=\left(1-\frac{11\sqrt5}{25}\right)n+O(1),}
\]
and
\[
\boxed{\frac{\iota(W_n)-n/\sqrt5}
{\sqrt{\left(1-11\sqrt5/25\right)n}}
\ \xrightarrow{\ d\ }\ \mathcal N(0,1).}
\]
The variance coefficient is strictly positive, approximately \(0.01613008990009\). The mean coefficient is approximately \(0.4472135955\), compared with \(1/3\) for unconditioned uniformly random binary words.

## Assumptions and scope

Words are finite, *linear*, and use the fixed alphabet \(\{0,1\}\). The forbidden-factor condition is contiguous and concerns only length-three homogeneous runs. The subsequence condition is order preserving but **not** contiguous. No cyclic boundary condition is imposed. The empty word is included only to normalize the generating function. The asymptotic distribution is uniform over the finite admissible set at each positive length, not a stationary infinite-chain law or an independent-letter distribution.

## Proof

**Greedy-arch lemma.** Scan a word from left to right and close an *arch* at the first instant both binary symbols have appeared since the preceding closing point. Repeat, leaving a final suffix containing at most one distinct symbol. If \(r\) arches close, then \(\iota(w)=r\). Indeed, for any target of length \(r\), choose its successive letters from the successive arches. Conversely, let \(c_i\) be the last symbol (the first symbol different from the initial symbol) in arch \(i\). Greedy subsequence matching of \(c_1c_2\cdots c_r\) reaches exactly those \(r\) closing positions. The remaining suffix lacks some bit \(d\) (any bit if the suffix is empty). Hence \(c_1\cdots c_rd\) is absent as a subsequence. The argument also covers \(r=0\).

**Finite-state decomposition.** All nonempty admissible words fall into exactly one of three categories. Category \(P\) is a nonempty pending arch, with its currently seen symbol appearing once at the right end; category \(Q\) is a pending arch ending in a run of two equal symbols; category \(E\) has just closed an arch at the final symbol. A just-closed arch ends in a run of one. Weight a completed arch by \(u\), and every bit by \(z\). The class generating functions satisfy the *complete* transition equations
\[
P=2z+zE,\qquad Q=z(P+E),\qquad E=uz(P+Q).
\]
The \(2z\) term permits either initial bit. From \(E\), a different next bit enters \(P\) and an equal next bit enters \(Q\); from \(P\), equal extends to \(Q\) and different closes a new arch; from \(Q\), only different is allowed, closing a new arch. These cases are disjoint and exhaustive because length-three constant runs are forbidden. Consequently,
\[
\sum_{n,k}N_{n,k}z^nu^k=1+P+Q+E
=\frac{1+2z+2z^2+uz^3}{1-u(2z^2+z^3)}.
\]
Expanding the denominator geometrically gives the coefficient formulas in the finding. Ignoring arch marks, a nonempty admissible word is determined by its first bit and its successive run lengths in \(\{1,2\}\); the Fibonacci recurrence gives \(|\mathcal L_n|=2F_{n+1}\).

**Asymptotics.** Put \(R(z)=2z^2+z^3\), and let \(\rho(t)\) be the positive simple root, continued analytically around \(t=0\), of \(e^tR(\rho(t))=1\). At \(t=0\), \(\rho(0)=(\sqrt5-1)/2\). The other zeros of \(1-R(z)\) are \(-1\) and \(-(1+\sqrt5)/2\), both farther from the origin. The consecutive block lengths \(2,3\) have greatest common divisor one, giving a unique dominant simple pole also uniformly for sufficiently small complex \(t\). Thus a nonzero analytic \(C(t)\) satisfies
\[
[z^n]F(z,e^t)=C(t)\rho(t)^{-n}(1+O(q^n))
\]
for a fixed \(q<1\) locally uniformly in \(t\). Consequently the logarithm of the moment-generating function of \(\iota(W_n)\) is \(n\psi(t)+O(1)\), with uniform analytic error, where \(\psi(t)=\log\rho(0)-\log\rho(t)\).

To differentiate, define \(p_2=2\rho(0)^2=3-\sqrt5\) and \(p_3=\rho(0)^3=\sqrt5-2\). They sum to one. The associated length distribution on \(\{2,3\}\) has mean \(2p_2+3p_3=\sqrt5\) and variance \(p_2p_3=5\sqrt5-11\). Implicit differentiation of \(e^tR(\rho(t))=1\) gives
\[
\psi'(0)=\frac1{\sqrt5},\qquad
\psi''(0)=\frac{5\sqrt5-11}{5\sqrt5}
=1-\frac{11\sqrt5}{25}>0.
\]
Uniform analyticity gives the stated first two cumulants with bounded errors. Evaluating the centered log moment-generating function at \(t/\sqrt n\), its Taylor expansion tends to \(\psi''(0)t^2/2\); convergence to the stated Gaussian law follows. This uses an all-length rational generating function, not an inference from finite experiments.

## Verification

The included standard-library script `verify.py` implements four distinct checks: independent direct brute-force enumeration of all admissible binary words through length \(16\); direct definition-level testing of every binary target subsequence through length \(12\); an aggregate three-state recurrence separate from the coefficient formula; and exact binomial-coefficient evaluation of the closed form. It also checks the Fibonacci total and the algebraic constants. Running `python3 verify.py` returns `VERIFY_OK`. Selected complete distributions are \((N_{8,2},N_{8,3},N_{8,4})=(2,50,16)\), \((N_{12,4},N_{12,5},N_{12,6})=(66,336,64)\), and \((N_{16,5},N_{16,6},N_{16,7},N_{16,8})=(22,900,2016,256)\). The finite check does not establish the asymptotic theorem; the pole argument above does.

## Relationship to prior work

Karandikar, Kufleitner and Schnoebelen (2013) develop the older Simon-congruence viewpoint, which motivates subsequence invariants. Karandikar and Schnoebelen (2015), Section 3, explicitly define rich factorization, its greedy closure and the maximal richness statistic; the present arch lemma is the corresponding binary subsequence-universality formulation. Fleischmann and collaborators (2020) establish algorithmic questions and arch methods for unconstrained word universality. Adamson (2023) counts and ranks unrestricted universal words. Adamson, Fleischmann, Huch, Koß, Manea and Nowotka (2023), Section 4, give **general regular-language algorithms** for counting fixed-length universal words; applying their method to the no-triple language could calculate individual counts and must not be represented as a new counting-decidability algorithm. The contribution here is the explicit small rational bivariate law, closed all-length binomial coefficients and a sharp golden-ratio Gaussian fluctuation law for this specific natural constrained source. A published research-record comparison found an unrestricted binary universality-law result, with a different generating function; its unconstrained count does not imply the forbidden-run formula. No reviewed source explicitly supplies the present three components together. Priority may be affected by unindexed special-case results.

## Limitations

No extension is asserted for longer permitted homogeneous runs, nonbinary alphabets, cyclic words, multiple simultaneous constraints, weighted symbol sources, or arbitrary regular languages. General regular-language counting algorithms predate this calculation. Independent mathematical validation and exhaustive historical-priority certification are not claimed. The coefficient check covers only finite lengths, while the proof of the infinite and distributional statements is analytic.

## References

1. P. Karandikar, M. Kufleitner and P. Schnoebelen, *On the index of Simon's congruence for piecewise testability*, first publicly available 2013-10-03, https://arxiv.org/abs/1310.1278.
2. P. Fleischmann, M. Kosche, T. Koß, F. Manea and S. Siemer, *The Edit Distance to k-Subsequence Universality*, first publicly available 2020-07-17, https://arxiv.org/abs/2007.09192.
3. D. Adamson, *Ranking and Unranking k-Subsequence Universal Words*, first publicly available 2023-04-10, https://arxiv.org/abs/2304.04583.
4. D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea and D. Nowotka, *k-Universality of Regular Languages*, first publicly available 2023-11-17, https://arxiv.org/abs/2311.10658, especially Section 4.
5. *Closed-form law for binary subsequence universality*, published research index, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-closed-form-law-for-binary-subsequence-universality--e77c4e8d9f37 (unrestricted binary-word comparison).
6. P. Karandikar and P. Schnoebelen, *The height of piecewise-testable languages and the complexity of the logic of subwords*, first publicly available 2015-11-05, https://arxiv.org/abs/1511.01807, Section 3, rich factorizations.
