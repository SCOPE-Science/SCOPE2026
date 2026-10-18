# A full interval of local rough-count multiplicities and strict growth of prime-gap constants

## Finding
Let \(P\ge7\) be any prime, let \(h=P-1\), and define
\[
U_h=\{\ell\text{ prime}: h/2<\ell<h,\ \ell\nmid h+2\},\qquad t_h=|U_h|.
\]
For every integer \(0\le k\le t_h\), the endpoint-admissible rough-count statistic \(\rho_h\) takes the exact value \(k\) on at least \(\binom{t_h}{k}\) distinct residue classes modulo \(Q_h\). In particular, the local counts have no gaps in the interval \(0,\dots,t_h\).

For the finite, positive constants \(c_r\) defined in [1], this gives
\[
\boxed{c_{r+1}>c_r\quad\text{for every integer }r\ge1.}
\]
More precisely, whenever \(t_h\ge r\),
\[
 c_{r+1}-c_r\ \ge\ \Sigma(h)\frac{\binom{t_h}{r}}{|A_h|}\ >0.
\]
Here \(t_h\sim h/(2\log h)\) along primes \(P=h+1\), so a suitable \(h\) exists for each fixed \(r\).

## Assumptions and scope
For each even integer \(h\ge2\), put \(Q_h=\prod_{p<h}p\), the product over primes strictly smaller than \(h\), and
\[
 A_h=\{b\pmod{Q_h}:\gcd(b(b+h),Q_h)=1\},\qquad
 \rho_h(b)=\#\{1\le i\le h-1:\gcd(b+i,Q_h)=1\}.
\]
Let \(\Sigma(h)>0\) be the usual admissible prime-pair singular series for \(\{0,h\}\), and let
\[
 c_r=\sum_{\substack{h\ge2\\h\text{ even}}}\Sigma(h)\Pr_{b\in A_h}(\rho_h(b)<r),\quad r\in\mathbb Z_{\ge1}.
\]
Existence and finiteness of these constants are already established in [1], Definition 1.1 and Lemma 2.4; that analytic result is used, not re-proved. This note proves the new local support and positivity assertions unconditionally. Only the interpretation via the number of *actual consecutive-prime gaps* requires the prime-tuples hypothesis in [1], Hypothesis 3.3.

## Proof
Fix an odd prime \(P\ge7\), put \(h=P-1\), and choose any subset \(T\subseteq U_h\). For every prime \(p<h\), impose by the Chinese remainder theorem
\[
 b\equiv\begin{cases}2\pmod p,&p\in T,\\1\pmod p,&p\notin T.\end{cases}
\]
This determines a unique class \(b_T\pmod{Q_h}\).

**Endpoint admissibility.** If \(p\notin T\), neither \(b_T\equiv1\) nor \(b_T+h\equiv h+1=P\) vanishes modulo \(p\), because \(P\) is a prime greater than \(p\). If \(p\in T\), then \(b_T\equiv2\not\equiv0\pmod p\), since \(p>h/2\ge3\), and \(b_T+h\equiv h+2\not\equiv0\pmod p\) by the definition of \(U_h\). Therefore \(b_T\in A_h\).

**Exactly the selected interior positions survive.** Write \(m=i+1\in\{2,\ldots,h\}\). If \(m\) is composite, it has a prime divisor \(p\le m/2\le h/2\); if \(m\) is prime and \(m\le h/2\), choose \(p=m\). In either case \(p\notin T\) and \(b_T+i\equiv1+(m-1)\equiv0\pmod p\). Thus these positions do not contribute to \(\rho_h\).

The remaining \(m\) are precisely the primes \(\ell\) with \(h/2<\ell<h\). If \(\ell\notin T\), then \(b_T+(\ell-1)\equiv\ell\equiv0\pmod\ell\), so that position is excluded. If \(\ell\in T\), check every prime \(p<h\): for \(p\notin T\), \(b_T+(\ell-1)\equiv\ell\pmod p\), nonzero because \(p\ne\ell\); for \(p\in T\), \(b_T+(\ell-1)\equiv\ell+1\pmod p\). This last remainder cannot vanish: \(\ell+1\) is an even integer between \(2\) and \(h\), whereas \(p\) is an odd prime exceeding \(h/2\); as \(2p>h\), its only possible multiple in this range would be \(p\) itself, which is odd. Hence precisely the positions \(i=\ell-1\) with \(\ell\in T\) survive, and
\[
 \rho_h(b_T)=|T|.
\]
Distinct subsets give distinct classes because their prescribed residues differ modulo some selected prime. Selecting all subsets of size \(k\) establishes the binomial lower bound.

**Unbounded support and strict constants.** At most one prime in the interval \((h/2,h)\) can divide \(h+2\): because any two such primes have product larger than \(h^2/4>h+2\) for \(h\ge6\), with the borderline \(h=6\) also immediate; more directly, any prime divisor of \(h+2\) greater than \(h/2\) has cofactor at most \(2\). Consequently \(t_h\ge\pi(h)-\pi(h/2)-1\). The prime number theorem gives \(t_h\sim h/(2\log h)\) as \(P=h+1\to\infty\) through primes. [The displayed inequality is all that is needed for divergence.] For fixed \(r\ge1\) choose such \(h\) with \(t_h\ge r\). Since each term in the defining series for \(c_r\) is nonnegative and finite,
\[
 c_{r+1}-c_r=\sum_{\substack{j\ge2\\j\text{ even}}}\Sigma(j)\Pr_{A_j}(\rho_j=r)
 \ge\Sigma(h)\frac{\binom{t_h}{r}}{|A_h|}>0.
\]
The positivity of \(\Sigma(h)\) follows because an even shift \(h\) makes \(\{0,h\}\) an admissible prime-pair pattern.

## Verification
The included standard-library `verify.py` independently constructs each CRT class for every subset of \(U_h\) at each prime anchor \(7\le P\le101\), checks both endpoint conditions, and compares the exact surviving interior positions with the selected set. It verified 4,042 distinct subset patterns at 23 prime anchors. As a separate check, it exhaustively enumerated all residue classes for \(P=7,11,13,17,19\) and confirmed the predicted binomial lower bound in each local histogram. See `verification_output.txt`; run `python3 verify.py` to reproduce.

Finite checks are corroboration only. The proof above establishes the infinite assertions; no amount of finite sampling alone would establish strict monotonicity for all \(r\).

## Relationship to prior work
Uğurdoğan [1] defines \(A_h,\rho_h,\Sigma(h),c_r\), proves finiteness, obtains asymptotic estimates in \(r\), and under a stated prime-tuples hypothesis relates \(c_r\) to the frequency of gaps with fewer than \(r\) rough integers. In [1], Theorems 1.4–1.5 and §§3–4, no full-interval support construction or strict comparison \(c_{r+1}>c_r\) is stated. The existing lower bound \(c_r>0\) does not imply that successive constants differ. The approximate local computations through \(r=50\) also do not give an infinite proof.

Gafni–Tao [2] treat the earlier zero-rough-number problem, corresponding to the first threshold. Neither the published r-one asymptotic nor the prime-pair singular series alone implies the all-threshold strict comparison. The present CRT argument is self-contained once the local definitions are specified.

## Limitations
This does **not** give an effective bound for the least prime anchor realizing a prescribed \(r\), a precise value for \(c_{r+1}-c_r\), or a local limit theorem. The lower bound may be very small for large \(r\). Actual prime-gap asymptotics require the unproved prime-tuples hypothesis [1]; no unconditional positive-density statement for gaps of a given exact multiplicity is made. As with any literature comparison, an unindexed equivalent construction may exist.

## References
[1] B. Uğurdoğan, *Multiplicity constants for rough numbers in prime gaps*, arXiv:2610.10582v1, first public 2026-10-06. https://arxiv.org/html/2610.10582v1

[2] A. Gafni and T. Tao, *Rough numbers between consecutive primes*, arXiv:2508.06463v1, first public 2025-08-08. https://arxiv.org/abs/2508.06463
