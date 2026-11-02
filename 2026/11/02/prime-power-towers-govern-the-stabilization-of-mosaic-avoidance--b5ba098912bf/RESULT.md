# Prime-power towers govern the stabilization of mosaic-avoidance densities

## Finding

Let \(S\) be a nonempty finite set of primes. In the recursively factored prime-exponent mosaic of a positive integer \(n\), let \(P_i(n)\) be the primes appearing in its first \(i\) levels. Write \(\delta_i(S)\) for the natural density of integers for which \(P_i(n)\cap S=\varnothing\), and \(\delta_\infty(S)\) for the natural density of integers in whose *entire* mosaic no prime of \(S\) occurs. Both densities exist; \(\delta_\infty(S)>0\).

Put \(q=\min S\), and let \(r\) and \(s\) be the first two primes outside \(S\), in increasing order. Define the tower sequence
\[
M_1=q,\qquad M_{i+1}=r^{M_i}\quad(i\ge1).
\]
Let \(\lambda_S(n)\) be the first depth at which a prime of \(S\) occurs in the mosaic of \(n\), with \(\lambda_S(n)=\infty\) if none occurs. For every \(i\ge1\),
\[
\min\{n\ge1:\lambda_S(n)=i\}=M_i,
\]
and the minimizing integer is unique. Define
\[
B_{S,p}=(1-p^{-1})\left(1+\sum_{e\ge1:\lambda_S(e)=\infty}p^{-e}\right)
\quad(p\notin S),\qquad
B_{S,p}=1-p^{-1}\quad(p\in S),
\]
and the positive constant
\[
K_S=(1-r^{-1})\prod_{p\ne r}B_{S,p}>0.
\]
Then the exact first-order asymptotic as the *level* tends to infinity is
\[
\boxed{\delta_i(S)-\delta_\infty(S)\sim K_S\,r^{-M_i}.}
\]
Indeed the successive increments obey
\[
\boxed{\delta_i(S)-\delta_{i+1}(S)\sim K_S\,r^{-M_i}.}
\]
In particular the limiting density is approached strictly from above at every finite level and with a sharp iterated-exponential scale, not merely an unspecified small error.

## Assumptions and scope

The set \(S\) is fixed, finite, nonempty and consists of rational primes; the limit is \(i\to\infty\). The set of integers is \(\mathbb N=\{1,2,\ldots\}\). The recursion of mosaic levels begins with the ordinary prime factors at level \(1\), then prime factors of the exponents at level \(2\), and so forth; the mosaic of \(1\) contains no primes. A natural density is an asymptotic proportion of positive integers up to \(X\) as \(X\to\infty\), with \(i\) held fixed before the level limit. The limits in \(X\) and \(i\) are not interchanged without proof.

For illustration, \(S=\{2\}\) has \(q=2,r=3\) and \(M_1=2,M_2=9,M_3=19683\); \(S=\{3\}\) has \(q=3,r=2\) and \(M_1=3,M_2=8,M_3=256\).

## Proof

**1. Depth recurrence and exact minimum.** Define \(\lambda_S(1)=\infty\). If \(n=\prod_p p^{a_p}>1\), where positive exponents are indexed by its prime divisors, then
\[
\lambda_S(n)=\begin{cases}
1,&\text{if some }p\mid n\text{ belongs to }S,\\
1+\min_{p\mid n}\lambda_S(a_p),&\text{otherwise},
\end{cases}
\]
where \(1+\infty=\infty\). This is the definition of recursive prime-exponent factorization. When \(\lambda_S(n)=1\), the least possible integer is \(q\), uniquely. Suppose that the least integer of depth \(i\) is \(M_i\). If \(\lambda_S(n)=i+1\), all ordinary prime factors of \(n\) lie outside \(S\); at least one prime-power exponent \(a_p\) has \(\lambda_S(a_p)=i\). Therefore \(a_p\ge M_i\), \(p\ge r\), and \(n\ge p^{a_p}\ge r^{M_i}\). Equality forces \(n=r^{M_i}\), which has depth exactly \(i+1\). This proves the tower minimum and its uniqueness by induction.

**2. Densities and positive Euler factors.** The full-avoidance indicator is multiplicative on coprime integers. For every prime \(p\in S\), only exponent zero is allowed. For \(p\notin S\), exponent \(e\ge1\) is allowed exactly when its own complete mosaic avoids \(S\). Finite sets of prime-power divisibility requirements have natural densities by the Chinese remainder theorem. The obstruction associated with a prime \(p\notin S\) requires its exponent to be at least \(q\ge2\), so for a cutoff \(P\), the upper density of obstructions at primes \(p>P\) is bounded by \(\sum_{p>P}p^{-q}\to0\). For each of finitely many primes, exponents above a cutoff \(E\) have total density at most \(\sum_{p\le P}p^{-E}\to0\). Consequently the limit defining \(\delta_\infty(S)\) exists, equals \(\prod_p B_{S,p}\), and agrees with \(\lim_{i\to\infty}\delta_i(S)\). For \(p\notin S\), exponents \(0\) and \(1\) are always allowed, hence \(B_{S,p}\ge (1-p^{-1})(1+p^{-1})=1-p^{-2}\). The factors for \(p\in S\) are positive and finite in number. Thus the product is strictly positive. The analogous finite-level Euler factors are
\[
B_{i,p}=1-p^{-1}\ (p\in S),\qquad
B_{i,p}=(1-p^{-1})\left(1+\sum_{e\ge1:\lambda_S(e)>i-1}p^{-e}\right)\ (p\notin S),
\]
so \(\delta_i(S)=\prod_p B_{i,p}\) and \(B_{i,p}\downarrow B_{S,p}\).

**3. Isolation of the leading forbidden exponent.** Let \(s>r\) be the next prime outside \(S\). For sufficiently large \(i\), any integer \(e\ne M_i\) whose first forbidden prime from \(S\) occurs at depth \(i\) satisfies \(e\ge2M_i\). Indeed, choose a prime-power component \(p^a\mid e\) with \(\lambda_S(a)=i-1\). Then \(a\ge M_{i-1}\). If \(p=r\), either \(a>M_{i-1}\), giving \(e\ge rM_i\), or \(a=M_{i-1}\), giving \(e=M_i\) or an additional integer factor of at least two. If \(p\ge s\), then \(e\ge s^{M_{i-1}}\ge2r^{M_{i-1}}=2M_i\) for all sufficiently large \(i\), since \((s/r)^{M_{i-1}}\to\infty\). The same conclusion applies to depths greater than \(i\): their minimal witness is \(M_{i+1}\ge2M_i\).

**4. Sharp density estimate.** For integers passing the first \(i\) levels but failing at a deeper level, at least one prime-power valuation \(v_p(n)\) has forbidden depth at least \(i\). By Step 3, the only valuation below \(2M_i\) that can cause a later failure at the smallest permitted outer prime \(r\) is \(v_r(n)=M_i\); for every other permitted prime \(p\ge s\), the offending exponent is at least \(M_i\).

The subset of these integers satisfying \(v_r(n)=M_i\) and complete avoidance at all other primes has exact natural density
\[
(1-r^{-1})r^{-M_i}\prod_{p\ne r}B_{S,p}=K_Sr^{-M_i}.
\]
It lies in the difference between level-\(i\) and complete avoidance. Conversely, the difference is contained in the union of: (a) \(v_r(n)=M_i\) with all other prime-power components avoiding \(S\) through level \(i\); (b) \(v_r(n)\ge2M_i\); (c) \(v_p(n)\ge M_i\) for some \(p\ge s\) outside \(S\). Their upper densities are, respectively,
\[
(1-r^{-1})r^{-M_i}\prod_{p\ne r}B_{i,p},\qquad
r^{-2M_i},\qquad
\sum_{p\ge s}p^{-M_i}=O_S(s^{-M_i}).
\]
As \(i\to\infty\), the first product tends to \(\prod_{p\ne r}B_{S,p}\), while the last two bounds are \(o(r^{-M_i})\). Squeezing proves the first boxed asymptotic. Applying the same argument to failures occurring *exactly* at level \(i+1\), rather than at some later level, gives the second boxed asymptotic: the lower-bound event uses complete avoidance at other primes, and the same three classes upper-bound it. Positivity of the first-step difference follows by the displayed exact lower-bound event at every \(i\).

## Verification

The included `verify.py` computes least forbidden depths by the prime-power recurrence with exact integer arithmetic and checks the tower minima for nine distinct finite prime sets through a limit of \(200000\). In particular it finds \(19683\) as the first depth-three witness for \(S=\{2\}\) and \(256\) for \(S=\{3\}\); the next depth-three witnesses in this range occur at \(98415\) and \(1280\), respectively, both at least twice the minimum. It also checks positive finite Euler factors via exact rational arithmetic. These checks test small instances and do not establish the infinite asymptotics, which follow from the proof above. Run with `python3 verify.py` using Python's standard library.

## Relationship to prior work

Dao, Kasian, and Mirabi (2026, arXiv:2606.22842, Sections 2 and 7) define the finite mosaic levels and compute the fixed-level Euler products for \(\delta_i(S)\). Their results motivate the level-limit question but do not state the exact tower-scale limit \(\delta_i(S)-\delta_\infty(S)\sim K_Sr^{-M_i}\). The Euler-factor representation used here agrees with theirs.

Devlin and Gnang (2014, arXiv:1204.5251, Sections 2–3) derive full-tower avoidance probabilities for a *single* forbidden prime. Thus existence of full-tower density in that case is prior work, not asserted to be new here. They do not identify the sharp asymptotic for successive depth truncations. De Koninck and Verreault (2023, arXiv:2308.09149, Sections 5–6) derive densities for unrestricted total tower height and an upper bound governed by minimal all-prime towers. Total-height exclusion differs from forbidding specified prime labels, and its bound does not yield the present leading constant. Conti, Contucci, and Iudelevich (2025, arXiv:2512.01376, Theorem 2.3) count integers of a prescribed unlabeled tree type, rather than these labeled-prime avoidance probabilities and their level-to-infinity asymptotics.

## Limitations

The asymptotic is for each fixed finite nonempty \(S\) and \(i\to\infty\); neither uniformity in growing \(S\) nor a numerical closed form for \(\delta_\infty(S)\) is claimed. The constant \(K_S\) is an absolutely convergent Euler product, not a proven elementary constant. Existing papers give related density products and height bounds, so priority of a previously unstated derivation remains a literature risk. Computational examples are finite checks only; independent validation has not been performed.

## References

- The Anh Dao, Tim Kasian, and Mostafa Mirabi, *Level Totients for Integer Mosaics*, arXiv:2606.22842, submitted 2026-06-22. https://arxiv.org/abs/2606.22842
- Patrick Devlin and Edinah K. Gnang, *Primes Appearing in the Tower Factorization of Integers*, arXiv:1204.5251v2 (2014). https://arxiv.org/html/1204.5251v2
- Jean-Marie De Koninck and William Verreault, *On the Tower Factorization of Integers*, arXiv:2308.09149 (2023). https://arxiv.org/abs/2308.09149
- Roberto Conti, Pierluigi Contucci, and Vitalii Iudelevich, *Tree asymptotic densities in number theory*, arXiv:2512.01376 (2025). https://arxiv.org/abs/2512.01376
