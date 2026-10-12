# Exact parameter fibers of \(g_\alpha\)

## Finding
Fix \(n=\prod_{i=1}^r p_i^{e_i}>1\), put \(h=\gcd(e_1,\ldots,e_r)\), and for every positive integer \(\alpha\) define
\[
g_\alpha(n)=\prod_{i=1}^r p_i^{\operatorname{lcm}(e_i,\alpha)}.
\]
Then, for all positive integers \(\alpha\) and \(\beta\),
\[
g_\alpha(n)=g_\beta(n)
\quad\Longleftrightarrow\quad
\frac{\alpha}{\gcd(\alpha,h)}=\frac{\beta}{\gcd(\beta,h)}.
\]
For \(s\ge1\), define
\[
h_s=\prod_{\ell\mid h,\,\ell\mid s}\ell^{v_\ell(h)},
\qquad h^{(s)}=\frac{h}{h_s}.
\]
The full fiber of the normalized parameter \(s\) is
\[
\left\{\alpha\ge1:\frac{\alpha}{\gcd(\alpha,h)}=s\right\}
=\left\{s h_s d:d\mid h^{(s)}\right\},
\]
and therefore has cardinality \(\tau(h^{(s)})\). Hence \(\alpha\mapsto g_\alpha(n)\) is injective exactly when \(h=1\). Its image is infinite and is canonically indexed by \(s\ge1\), for example with representative \(g_{hs}(n)\) for index \(s\).

## Assumptions and scope
The integer \(n\) is fixed and exceeds \(1\); its prime factorization uses distinct primes \(p_i\) and positive exponents \(e_i\). Parameters \(\alpha,\beta\) are positive integers. The result concerns equality of outputs as the parameter varies while \(n\) is held fixed. It makes no assertion about equality between values attached to two different base integers.

## Proof
Unique factorization gives \(g_\alpha(n)=g_\beta(n)\) exactly when
\[
\operatorname{lcm}(e_i,\alpha)=\operatorname{lcm}(e_i,\beta)
\qquad(1\le i\le r).
\]
Fix a prime \(\ell\). Write \(a_i=v_\ell(e_i)\), \(t=v_\ell(\alpha)\), and \(u=v_\ell(\beta)\). Since valuation turns a least common multiple into a maximum, the \(\ell\)-adic data in the displayed system are the vectors
\[
(\max(a_i,t))_i \quad\text{and}\quad (\max(a_i,u))_i.
\]
Let \(m=\min_i a_i=v_\ell(h)\). If \(t\le m\), the first vector is simply \((a_i)_i\). If \(t>m\), choose an index \(j\) with \(a_j=m\); then the \(j\)-th coordinate equals \(t\), so the vector recovers \(t\) itself. Therefore
\[
(\max(a_i,t))_i=(\max(a_i,u))_i
\quad\Longleftrightarrow\quad
\max(t-m,0)=\max(u-m,0).
\]
But
\[
v_\ell\!\left(\frac{\alpha}{\gcd(\alpha,h)}\right)=\max(t-m,0),
\]
and the analogous identity holds for \(\beta\). Equality for every prime \(\ell\) is thus equivalent to the claimed equality of normalized parameters.

For the fiber formula, fix \(s\). Prime by prime, if \(\ell\mid h\) and \(\ell\mid s\), the exponent of \(\ell\) in \(\alpha\) is forced to be \(v_\ell(h)+v_\ell(s)\). If \(\ell\mid h\) but \(\ell\nmid s\), that exponent may be any integer from \(0\) through \(v_\ell(h)\). Primes outside \(h\) have the exponent already prescribed by \(s\). This is exactly the parametrization \(\alpha=s h_s d\) with \(d\mid h^{(s)}\), and the divisor count gives \(\tau(h^{(s)})\).

If \(h=1\), the normalized parameter is \(\alpha\), so the map is injective. If \(h>1\), the fiber \(s=1\) contains every divisor of \(h\), so the map is not injective. Finally, choosing \(\alpha=hs\) realizes every normalized parameter \(s\), proving that the image is infinite and indexed by the positive integers.

## Verification
The symbolic proof is unbounded and does not depend on computation. As regression evidence, `verify.py` checks both directions of the equality criterion for all ordered exponent tuples of support sizes \(1\) through \(4\), exponents at most \(12\), and parameters at most \(120\). It separately verifies the closed fiber formula for \(1\le h\le100\) and \(1\le s<80\). The recorded replay output is:

`VERIFY_OK parameter_checks=2714400 fiber_cases=7900 supports=1..4 exponent_max=12 alpha_max=120`

## Relationship to prior work
Mittou introduced \(g_\alpha\) as the least-common-multiple companion to an earlier greatest-common-divisor exponent function. The 2023 paper proves the special fiber
\[
g_\alpha(n)=n \quad\Longleftrightarrow\quad \alpha\mid h,
\]
where \(h=\gcd(e_1,\ldots,e_r)\), and proves composition identities for the family. The present result recovers that theorem as the fiber \(s=1\) and determines every other parameter fiber as well.

A 2025 follow-up, classified under MSC 11A25, studies inequalities and compositions of \(f_\alpha\) and \(g_\alpha\), and an equivalence relation on base integers of the form \(n\mathrel{R}m\) when one common parameter makes \(g_\alpha(n)=g_\alpha(m)\). That relation varies the base integer and is different from the fixed-\(n\) parameter-fiber problem here. The inspected paper does not state the normalized-parameter criterion or the fiber cardinalities above.

## Limitations
The originality comparison is limited to the inspected focal paper, its 2025 follow-up, targeted scholarly searches, literature-claim searches, and the previously checked research result. A mathematically equivalent statement could exist under different notation outside those sources. The result is elementary once the correct prime-adic invariant is identified; its value is the complete fiber classification for the specific arithmetic-function family, not technical depth. No independent audit has been performed.

## References
B. Mittou, “New arithmetic function related to the least common multiple,” *Journal of Science and Arts* 23(1) (2023), 123–128. DOI: 10.46939/J.Sci.Arts-23.1-a09. Published online 2023-03-30.

B. Mittou, “New properties of arithmetic functions related to gcd and lcm,” *Notes on Number Theory and Discrete Mathematics* 31(1) (2025), 91–97. DOI: 10.7546/nntdm.2025.31.1.91-97. 2020 MSC: 11A25.
