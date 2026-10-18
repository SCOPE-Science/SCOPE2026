# The least \(\mu\)-Sondow witness is \(145\) along a Fermat-index progression

## Finding
For an integer \(\mu\), call an integer \(m>1\) **\(\mu\)-Sondow** if, for every prime power \(p^e\parallel m\),
\[
p^e\mid \frac{m}{p}+\mu.
\]
For every positive integer \(r\), set
\[
\mu_r=2^{2^{3r}}.
\]
Then the **least** integer \(m>1\) that is \(\mu_r\)-Sondow equals
\[
\boxed{m=145=5\cdot29\qquad\text{for all integers }r\ge1.}
\]
Equivalently, the full interval \(2\le m\le144\) contains no \(\mu_r\)-Sondow number, but \(145\) is one, independently of \(r\). This produces an exact constant least-witness law on an infinite progression of Fermat exponents, substantially sharper than merely knowing that a witness exists below the parameter.

## Assumptions and scope
All parameters \(r\) are integers \(r\ge1\). No unproved assertion about the primality of Fermat numbers is assumed. The count is over all positive integers \(m>1\), not merely squarefree integers; squarefreeness in the indicated bounded range is a proved consequence, not a hypothesis.

## Proof
**Step 1: exclusion of even and nonsquarefree candidates.** Since \(\nu_2(\mu_r)=2^{3r}\ge8\), if \(m\le144\) is even and \(2^e\parallel m\), then \(1\le e\le7\), and
\[
\nu_2\!\left(\frac m2+\mu_r\right)=e-1<e.
\]
Thus the condition fails at the prime \(2\). If an odd prime \(p\) satisfies \(p^2\mid m\), then \(p\mid m/p\), whereas \(p\nmid\mu_r\); hence the condition fails at \(p\). It remains to exclude precisely the \(58\) odd squarefree integers \(3\le m\le143\).

**Step 2: a complete finite local-obstruction certificate.** For an odd prime \(p\), define the forward orbit
\[
\mathcal O_p=\{x_1,x_2,\ldots\},\qquad
x_1\equiv 2^8\pmod p,\quad x_{k+1}\equiv x_k^8\pmod p.
\]
This is a finite, explicitly calculable set: follow the recurrence until the first repeated state. For every integer \(r\ge1\),
\[
\mu_r\equiv x_r\pmod p.
\]
If \(m\) is odd and squarefree, a necessary condition for \(m\) to be \(\mu_r\)-Sondow is that, for each prime \(p\mid m\),
\[
-\frac{m}{p}\pmod p\in\mathcal O_p.
\]
The following finite table gives **one blocking prime** for each of the \(58\) candidates: in every row and for every indicated \(m\), one verifies
\[
-\frac{m}{p}\pmod p\notin\mathcal O_p.
\]
The table is obtained solely by trial division and modular powering. The longest encountered prime orbit has \(52\) distinct states. It is also reconstructed from scratch by the accompanying standalone verifier.

| Blocking prime \(p\) | All excluded \(m<145\) assigned to \(p\) |
| ---: | :--- |
| 3 | 3, 21, 39, 57, 93, 111, 129 |
| 5 | 5, 15, 35, 55, 65, 85, 105, 115 |
| 7 | 7, 77, 91 |
| 11 | 11, 33 |
| 13 | 13, 143 |
| 17 | 17, 51, 119 |
| 19 | 19, 95, 133 |
| 23 | 23, 69 |
| 29 | 29, 87 |
| 31 | 31 |
| 37 | 37 |
| 41 | 41, 123 |
| 43 | 43 |
| 47 | 47, 141 |
| 53 | 53 |
| 59 | 59 |
| 61 | 61 |
| 67 | 67 |
| 71 | 71 |
| 73 | 73 |
| 79 | 79 |
| 83 | 83 |
| 89 | 89 |
| 97 | 97 |
| 101 | 101 |
| 103 | 103 |
| 107 | 107 |
| 109 | 109 |
| 113 | 113 |
| 127 | 127 |
| 131 | 131 |
| 137 | 137 |
| 139 | 139 |

These rows cover every odd squarefree \(m<145\) once, so **all** candidates below \(145\) are excluded simultaneously for **every** \(r\ge1\). A finite computation is sufficient here because its domain is the complete finite interval \(m<145\), while the modular-orbit argument handles all infinitely many indices \(r\).

**Step 3: a uniform witness.** Direct modular calculation gives
\[
2^8\equiv111\pmod{145},\qquad111^8\equiv111\pmod{145}.
\]
Thus \(\mu_r\equiv111\pmod{145}\) for every \(r\ge1\). Because
\[
\frac{145}{5}+111=29+111=140\equiv0\pmod5
\]
and
\[
\frac{145}{29}+111=5+111=116\equiv0\pmod{29},
\]
the number \(145\) satisfies the defining condition at both prime divisors. Combining Steps 1--3 proves the theorem.

## Verification
Run `python3 verify.py` with standard Python 3 and no third-party packages. The verifier re-factors every integer below \(145\), checks a modular forward orbit for all \(58\) remaining odd squarefree candidates, requires at least one prime obstruction per candidate, and verifies the two exact residues at \(145\). Independently it directly checks the defining prime-power divisibilities at every integer \(2\le m\le145\) for eight indices \(3,6,\ldots,24\); these latter finite spot-checks are diagnostic rather than the infinite proof. Expected output begins with `CERTIFICATE_PASS` and confirms \(58\) candidates, \(33\) blocking primes, and maximal prime-orbit length \(52\).

## Relationship to prior work
Grau, Oller-Marcén, and Sadornil introduced \(\mu\)-Sondow numbers and asked in their Conjecture 1(i) for small nontrivial witnesses outside finitely many exceptional parameters (arXiv:2111.14211v1, publicly posted 28 November 2021). A later public mathematical note, “Positive \(\mu\)-Sondow small-witness conjecture reduces to new Fermat primes” (2026), already establishes \(145\in S_{256}\) and a general reduction to Fermat-prime parameters. Its full text does not assert the all-\(r\) congruence \(\mu_r\equiv111\pmod{145}\), or the exact uniform **least** witness \(145\) for all \(r\ge1\). Its single-parameter membership fact does not logically imply the present infinite uniform minimality theorem. The 2021 source also does not give this least-witness classification.

## Limitations
The claim covers exactly the indicated infinite arithmetic progression of Fermat indices \(3r\), not every Fermat index. The local exclusion certificate is finite and transparent but not replaced here by a shorter purely conceptual inequality. The result neither settles the original small-witness conjecture for every parameter nor proves absolute publication priority; a general unindexed periodic-minimality theorem could in principle imply it.

## References
1. J. M. Grau, A. M. Oller-Marcén, and D. Sadornil, “On \(\mu\)-Sondow numbers,” arXiv:2111.14211v1 (28 November 2021), https://arxiv.org/abs/2111.14211; subsequently *Acta Mathematica Hungarica* 168 (2022), 217–227, DOI:10.1007/s10474-022-01271-w.
2. “Positive \(\mu\)-Sondow small-witness conjecture reduces to new Fermat primes,” public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-positive-mu-sondow-small-witness-conjecture-reduces-to-new-ferma--941441ce16d2.
