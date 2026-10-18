# A complete limiting gap law for coprime records

## Finding

Let \(p_j\) be the \(j\)-th prime and let \(P_j=\prod_{i=1}^j p_i\). Starting at \(r_1=3\), define the strictly increasing sequence of **coprime records** by
\[
 r_{m+1}=r_m+\lambda(r_m-1)-1,
 \qquad \lambda(t)=\min\{p\text{ prime}:p\nmid t\}.
\]
The records are the noninitial records of OEIS A261271, equivalently the records of the greedy coprime permutation investigated by Basistha and Ionaşcu. For each prime \(q\ge3\), write
\[
 R_q(X)=\#\{m:r_m\le X,\ r_{m+1}-r_m=q-1\}.
\]
**Theorem.** For every prime \(q\ge3\), the natural density \(\delta_q=\lim_{X\to\infty}R_q(X)/X\) exists and is strictly positive. No other positive gap has positive frequency (indeed, no other gap occurs). The \(\delta_q\) form a complete countably supported gap-frequency law: if \(\kappa=\lim_{X\to\infty}\#\{r_m\le X\}/X\), then
\[
 \sum_{q\ge3\atop q\text{ prime}}\delta_q=\kappa.
\]
These are densities per ambient integer; dividing by \(\kappa\) gives a probability distribution over the gaps between successive records.

More explicitly, for integers \(n\ge3\) and primes \(q\ge3\), define finite counts
\[
 c_n(q)=\#\{r_m:p_{n+1}\le r_m\le P_n+1,\ \lambda(r_m-1)=q\},
\]
\[
 s_n(q)=\#\{r_m:p_n\le r_m<p_{n+1},\ \lambda(r_m-1)=q\}.
\]
The initial values are \(c_3(3)=4\), \(c_3(5)=4\), \(c_3(7)=1\), and \(c_3(q)=0\) for other primes. For every \(n\ge3\),
\[
 \boxed{c_{n+1}(q)=p_{n+1}c_n(q)-s_{n+1}(q)-\mathbf1_{q=p_{n+1}}+\mathbf1_{q=p_{n+2}}.}
\]
Consequently, the **exact, effectively computable series** is
\[
 \boxed{\delta_q=\frac{c_3(q)}{30}+\sum_{j=4}^{\infty}
 \frac{-s_j(q)-\mathbf1_{q=p_j}+\mathbf1_{q=p_{j+1}}}{P_j}.}
\]
Every truncation has the explicit error bound
\[
 \boxed{\left|\delta_q-\frac{c_N(q)}{P_N}\right|<\frac4{P_N}\qquad(N\ge3).}
\]
The \(s_j(q)\) require only record generation below \(p_{j+1}\), not enumeration through the large primorial \(P_j\).

For example, the densities of record gaps \(2\) and \(4\) satisfy the rigorously bounded numerical statements
\[
 \left|\delta_3-\frac{986204740216}{7420738134810}\right|<\frac4{7420738134810},
\]
\[
 \left|\delta_5-\frac{953846993907}{7420738134810}\right|<\frac4{7420738134810}.
\]
The corresponding rational approximations are \(0.132898469437940\ldots\) and \(0.128538020959477\ldots\), respectively, with absolute errors less than \(5.40\times10^{-13}\); these decimals are approximations, not asserted exact expansions. Since a gap \(2\) is exactly a pair of consecutive records differing by two, \(\delta_3\) also counts twin-record starts per ambient integer.

## Assumptions and scope

All limits count records by their **integer value** rather than by their position in the sequence. The sequence begins at \(3\) so that the exceptional OEIS terms \(1,2\) do not affect the gap law. A prime \(q\) is fixed while \(X\to\infty\); no uniformity for growing \(q\) is asserted. The known record-density constant \(\kappa\) is positive; the proof also establishes completeness of the gap distribution directly.

## Proof

**1. Prime records and the local update.** Every prime \(\ge3\) is a record: if a prime \(p\) were strictly between consecutive records \(r<t\), it would be coprime to \(r-1<p\), contradicting the alternative definition of the next record as the smallest integer greater than \(r\) and coprime to \(r-1\). This alternative definition agrees with the prime-based recurrence because the smallest positive increment that produces a coprime integer is \(\lambda(r-1)-1\). In fact, for an increment smaller than that, the candidate shares a prime factor of \(r-1\), while the increment \(\lambda(r-1)-1\) is coprime to \(r-1\). The latter assertion follows because \(r+\lambda(r-1)-1\equiv\lambda(r-1)\pmod{r-1}\), and \(\lambda(r-1)\) is coprime to \(r-1\). For every integer \(r\) not congruent to \(1\) modulo \(P_n\), the least excluded prime \(\lambda(r-1)\) is at most \(p_n\) and depends only on the residue of \(r\) modulo \(P_n\).

**2. Exact primorial replication.** Directly from the recurrence, the records in \([7,31]\) are
\[
 7,11,13,17,19,23,25,29,31.
\]
In particular \(P_3+1=31\) is a record. Suppose inductively that \(P_n+1\) is a record and inspect the records in \([p_{n+1},P_n+1]\). At \(tP_n+1\) for \(1\le t<p_{n+1}\), the least prime not dividing the predecessor \(tP_n\) is exactly \(p_{n+1}\). Hence the next record is \(tP_n+p_{n+1}\). From there up to \((t+1)P_n+1\), all intermediate predecessor values are not divisible by \(P_n\); their least missing primes and therefore their record steps are determined modulo \(P_n\). Thus the initial record block, translated by \(tP_n\), is reproduced exactly through \((t+1)P_n+1\). This proves by induction that \(P_{n+1}+1\) is a record and establishes the entire repeated-block structure. The final boundary \(P_{n+1}+1\) has next-step prime \(p_{n+2}\), whereas intermediate boundaries have next-step prime \(p_{n+1}\).

**3. Labelled finite-block recurrence.** The records from \(p_{n+2}\) through \(P_{n+1}+1\) consist of \(p_{n+1}\) translated copies of those from \(p_{n+1}\) through \(P_n+1\), omitting the initial records in \([p_{n+1},p_{n+2})\). Under translation, all next-gap labels remain unchanged except the final boundary: its label changes from \(p_{n+1}\) to \(p_{n+2}\). Hence the displayed recurrence for \(c_{n+1}(q)\) follows, including the two essential boundary corrections. Dividing by \(P_{n+1}=p_{n+1}P_n\) yields
\[
 \frac{c_{n+1}(q)}{P_{n+1}}-\frac{c_n(q)}{P_n}
 =\frac{-s_{n+1}(q)-\mathbf1_{q=p_{n+1}}+\mathbf1_{q=p_{n+2}}}{P_{n+1}}.
\]
Its telescoping series gives the stated expression, provided that the limiting primorial proportion is the natural density.

**4. Natural density and effective bound.** For each \(n\ge3\), define a periodic labelled-record indicator \(F_{n,q}\) of period \(P_n\). On the consecutive interval \([p_{n+1},P_n+p_{n+1}-1]\), set it equal to the actual indicator of records with next-step prime \(q\), and extend periodically in both directions. The interval contains exactly \(c_n(q)\) such records: the record after \(P_n+1\) is \(P_n+p_{n+1}\), outside the chosen interval. Thus the density of \(F_{n,q}\) is exactly \(c_n(q)/P_n\).

The primorial replication in step 2 shows that \(F_{n+1,q}\) and \(F_{n,q}\), both viewed modulo \(P_{n+1}\), differ in no more than \(s_{n+1}(q)+2\) residue classes: the only deletions come from the initial records in \([p_{n+1},p_{n+2})\), and the only changed next-gap label is at the terminal primorial record. Hence the number of mismatches between these two periodic indicators up to any \(X\) is at most
\[
 (s_{n+1}(q)+2)(X/P_{n+1}+1).
\]
For an arbitrary \(X\), select \(J\) by \(P_J\le X<P_{J+1}\). The actual labelled record indicator agrees with \(F_{J,q}\) throughout \([p_{J+1},X]\), apart from at most one terminal boundary. The initial interval \([1,p_{J+1})\) contributes at most \(p_{J+1}\) discrepancies. By telescoping the comparisons with \(F_{j,q}\) for \(N<j\le J\), the difference of the normalized actual record count and \(c_N(q)/P_N\) has limit superior at most
\[
 \sum_{j>N}\frac{s_j(q)+2}{P_j}.
\]
Indeed, the extra terms after division by \(X\) are bounded by a constant multiple of
\[
 \frac{p_{J+1}+\sum_{j=N+1}^J(s_j(q)+2)+P_N}{X},
\]
which tends to zero: Bertrand gives \(p_{J+1}<2^{J+1}\), while \(P_J\ge(J+1)!\), and \(s_j(q)<p_j\). This shows ordinary, not merely primorial-subsequence, convergence once the right-hand tail tends to zero.

By Bertrand's postulate, \(p_{j+1}<2p_j\), so \(0\le s_j(q)<p_j\). Hence
\[
 \sum_{j>N}\frac{s_j(q)+2}{P_j}
 <2\sum_{j>N}\frac1{P_{j-1}}
 \le\frac4{P_N},
\]
using \(P_{j+1}\ge2P_j\). Therefore the ordinary density exists, equals the limit of \(c_n(q)/P_n\), and satisfies the strict error bound and the exact telescoping series.

**5. Strict positivity for every permitted gap.** For \(q=p_j\) with \(j\ge4\), the least missing prime at a record is \(q\) only if its predecessor is divisible by \(P_{j-1}\). Within the initial block for level \(j-1\), the unique such record is \(P_{j-1}+1\), so \(c_{j-1}(p_j)=1\). In the next block no low record in \([p_j,p_{j+1})\) has this label, and precisely one terminal label changes, giving \(c_j(p_j)=p_j-1\). The error bound therefore gives
\[
 \delta_{p_j}>\frac{p_j-5}{P_j}>0\qquad(j\ge4).
\]
For \(q=3\) and \(q=5\), direct initial values and the recurrence give \(c_4(3)=28\) and \(c_4(5)=27\); both exceed the error numerator \(4\), proving positivity as well.

**6. Exhaustiveness.** Each gap is \(q-1\) for a prime \(q\ge3\), by definition. If the next gap at a record is larger than \(p_N-1\), all the first \(N\) primes divide its predecessor. Such records lie in the single congruence class \(1\pmod{P_N}\), whose ambient upper density is at most \(1/P_N\). Sending \(N\to\infty\) shows that the sum of the individual gap densities equals the density \(\kappa\) of all records: there is no escaped mass at unbounded gaps. This also proves that the conditional probabilities \(\delta_q/\kappa\) sum to one.

## Verification

The included standalone \(\texttt{verify.py}\) uses only the Python standard library. It (i) generates actual records with the least-excluded-prime recurrence to value \(10^6\), (ii) independently regenerates the first 2,500 transitions by searching for the least coprime larger integer, (iii) compares the labelled recurrence against direct enumeration for levels \(4\) through \(7\), including all \(64\) label-level comparisons, and (iv) uses only small prime-interval counts to compute exact level-\(12\) numerators. Run \(\texttt{python3 verify.py}\) from the extracted folder. The exact rational counts and bounded intervals appear in its output. Finite checks are not substitutes for the infinite proof.

## Relationship to prior work

Basistha and Ionaşcu (2023 preprint, 2025 journal paper) establish the sequence's record recursion, primorial replication, and the existence of the **unlabelled** record density \(\kappa\). Their article discusses composite records and twin-record patterns, but does not state the limiting distribution of each successor gap or the boundary-corrected labelled recurrence above. OEIS A261271 documents the sequence and its first terms but no gap-density theorem. A separate finite record-multiple result identifies the first break in a particular arithmetic progression of composite records; it does not cover the limit law of all prime-minus-one successor gaps. The present result refines the source's primorial replication into a complete labelled distribution, with positivity and effective error bounds; it does not claim that the underlying replication principle is new.

## Limitations

The series uses recursively generated small-prime record counts; it is not a closed expression in elementary constants. The density \(\delta_q\) concerns fixed \(q\), and no uniform tail asymptotic in \(q\) is obtained. The direct calculation is finite. No claim about prime-twin infinitude or about the distribution of ordinary prime gaps is made.

## References

1. A. K. Basistha and E. J. Ionaşcu, *A special sequence and primorial numbers*, arXiv:2302.02838, first posted 6 February 2023; journal version, *Revue Roumaine de Mathématiques Pures et Appliquées* 70 (2025), 235–255. https://arxiv.org/abs/2302.02838 ; https://imar.ro/journals/Revue_Mathematique/pdfs/2025/3-4/4.pdf
2. OEIS A261271, *a(n) = a(n-1)-1+p where p is the smallest prime not dividing a(n-1)-1*. https://oeis.org/A261271
