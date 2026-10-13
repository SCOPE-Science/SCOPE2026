# Exact global dynamics of the shift-three Euler totient map

## Finding
Let \(\varphi\) be Euler's totient function, with \(\varphi(1)=1\), and define the map
\[
F:\mathbb Z_{>0}\longrightarrow\mathbb Z_{>0},\qquad F(n)=\varphi(n)+3.
\]
For **every** starting integer \(x_0\ge1\), the orbit \(x_{j+1}=F(x_j)\) eventually enters exactly one of the following three cycles, up to cyclic rotation:
\[
(9),\qquad (11,13,15),\qquad (23,25).
\]
They have respective minimal periods \(1\), \(3\), and \(2\). In particular,
\[
\limsup_{j\to\infty}x_j\le25
\]
for every starting value, and **\(25\) is the least possible universal eventual upper bound**, because the periodic orbit \(23\leftrightarrow25\) attains it infinitely often. Thus the complete set of periodic points is \(\{9,11,13,15,23,25\}\).

## Assumptions and scope
All integers and starting states are strictly positive. The totient is the standard multiplicative arithmetic function, with the conventional value \(\varphi(1)=1\). The shift is exactly \(3\); the claim is not a classification of other shifts, nor a formula for the basin of each individual cycle.

## Proof
**1. Reduction to odd states.** For any integer \(n\ge3\), \(\varphi(n)\) is even, so \(F(n)\) is odd and at least \(5\). Also \(F(1)=F(2)=4\) and \(F(4)=5\). Consequently, every positive orbit enters the odd integers at least \(5\) after at most two transitions and remains in that set.

**2. The composite descent inequality.** If \(m\ge4\) is composite and \(q\) is its least prime divisor, then \(q\le\sqrt m\). By the Euler product for the totient,
\[
\varphi(m)\le m\left(1-\frac1q\right)
\le m-\sqrt m.
\tag{1}
\]
Thus every odd composite \(m\ge27\) satisfies
\[
F(m)\le m-\sqrt m+3<m.
\tag{2}
\]
These inequalities require no unproved assumption about the distribution of primes.

**3. Prime-state descent in at most three steps.** Suppose \(p\ge27\) is an odd prime; necessarily \(p\ge29\). Then
\[
F(p)=p+2.
\]
If \(p+2\) is composite, applying (1) gives
\[
F^2(p)=\varphi(p+2)+3
\le p+5-\sqrt{p+2}<p,
\]
because \(p+2\ge31>25\).

If instead \(p+2\) is prime, then \(p>3\) and both \(p\) and \(p+2\) are prime, so \(p\equiv2\pmod3\) and \(3\mid p+4\). In particular, \(p+4>3\) is composite. Its factor \(3\) implies \(\varphi(p+4)\le 2(p+4)/3\); therefore
\[
F^3(p)=\varphi(p+4)+3
\le\frac{2(p+4)}3+3
=\frac{2p+17}{3}<p.
\tag{3}
\]
It follows that from every odd state \(n\ge27\), an orbit reaches a **strictly smaller odd state** in at most three transitions.

**4. Finite absorption.** Starting from any odd state \(n\ge27\), repeatedly apply the descent established in steps 2 and 3 at the end of each block of at most three transitions. The successive block endpoints form a strictly decreasing sequence of positive odd integers at least \(5\), until one lies at most \(25\). An infinite such strictly decreasing sequence is impossible. Hence every orbit reaches
\[
E=\{5,7,9,11,13,15,17,19,21,23,25\}.
\]
For all \(m\in E\), \(F(m)\in E\), as the following exhaustive **exact integer** evaluations show:

| \(m\) | \(F(m)\) |
|:---:|:---:|
| 5 | 7 |
| 7 | 9 |
| 9 | 9 |
| 11 | 13 |
| 13 | 15 |
| 15 | 11 |
| 17 | 19 |
| 19 | 21 |
| 21 | 15 |
| 23 | 25 |
| 25 | 23 |

The arrows form precisely the three stated cycles, with every other state in \(E\) flowing into one of them. Therefore the list is exhaustive for **all** initial values, not merely initial values below a computational cutoff.

**5. Sharpness.** The identities \(F(23)=25\) and \(F(25)=23\) establish a periodic orbit attaining \(25\) infinitely often. Since every orbit eventually stays in \(E\), the least universal eventual upper bound is exactly \(25\). This completes the proof.

## Verification
The accompanying `verify.py` implements Euler's totient by an integer sieve (no symbolic packages). It checks the exact eleven-state transition table, the three cycles and eventual absorption for every initial value \(1\le x_0\le200000\). It also tests composite one-step descent and prime two- or three-step descent for all odd states from \(27\) through \(49999\). Run `python verify.py`; the supplied `verification_output.txt` records the resulting finite checks. These computations supplement, and are not a substitute for, the unrestricted proof in the preceding section.

## Relationship to prior work
Leonetti and Luca prove that the orbit of \(\varphi(n)+k\) is eventually periodic for all integer shifts \(k\ge0\), and their Theorem 2 provides the explicit starting-value-dependent estimate \(\sup_j x_j\le\max\{x_0,k^4\}+(k+1)^2\). They do not enumerate all periodic orbits of the shift-three map or prove its sharp universal eventual bound of \(25\). Their proof already uses the general estimate (1) and a prime-progression obstruction; neither fact is claimed as novel here. The contribution is the globally exhaustive special-shift classification and the sharp absorbing set obtained by combining these ingredients with a direct finite transition analysis.

The related result *Sharp period-size bound and extremal structure for shifted Euler cycles* proves that a cycle of minimal length \(T\) for shift \(k\ge2\) has maximum at most \([T(k-1)+1]^2\) and classifies equality. It explicitly exhibits \(23\leftrightarrow25\) at shift \(3\), which is credited here as previously known. Its period-conditional estimate and example **do not provide an upper bound on possible periods or rule out additional shift-three cycles**. The present proof supplies the missing global exclusion and identifies all three possible minimal periods.

A later improvement by Danh and collaborators concerns the separate two-step recurrence \(x_{j+2}=\varphi(x_{j+1})+\varphi(x_j)+k\), not the one-step map at issue. Searches of arithmetic-sequence databases and the examined papers found no statement implying the complete present classification. Absence from those searches is not a proof of worldwide novelty.

## Limitations
No claim is made about the number or density of initial values attracted to each of the three cycles, the smallest entrance time for a given starting value, or all possible shifts. The prime-composite descent arguments are unrestricted; the finite verifier checks only bounded inputs. Publication elsewhere of an equivalent global classification cannot be excluded by the performed searches, and independent validation has not been performed.

## References
1. Paolo Leonetti and Florian Luca, “On the iterates of shifted Euler's function,” arXiv:2302.01783v1 (first publicly posted 2023-02-03), https://arxiv.org/html/2302.01783v1. Relevant material: Theorem 2, proof of Theorem 2, and the introduction. Primary MSC \(11A25,11B37\).
2. “Sharp period-size bound and extremal structure for shifted Euler cycles,” publicly available mathematical research record, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-sharp-period-size-bound-and-extremal-structure-for-shifted-euler--02d25ffc40ae/RESULT.md. Relevant material: full finding and proof, including the \(23\leftrightarrow25\) example.
3. Tran Nguyen Thanh Danh and collaborators, “An improvement to a theorem of Leonetti and Luca,” *Bulletin of the Australian Mathematical Society* **109** (2024), 437–442, DOI: 10.1017/S0004972723000862. The recurrence analyzed there is two-step.
4. OEIS A000010, Euler totient function, https://oeis.org/A000010.
