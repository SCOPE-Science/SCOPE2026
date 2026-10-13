# Exact first ten stopping-time strata of the second Schemmel totient

## Finding
For the second Schemmel totient \(L_2\), define the stopping-time strata
\[
\mathcal B_r=\{n>1: n\text{ odd},\ R_2(n)=r\}.
\]
Every stratum of rank \(1\le r\le10\) has the exact size and maximum below. Each maximum has a **unique** attaining integer.

| Rank \(r\) | \(|\mathcal B_r|\) | Maximum integer | Number of maximizers |
| ---: | ---: | ---: | ---: |
| 1 | 1 | 3 | 1 |
| 2 | 3 | 15 | 1 |
| 3 | 13 | 105 | 1 |
| 4 | 54 | 735 | 1 |
| 5 | 226 | 5,145 | 1 |
| 6 | 986 | 36,015 | 1 |
| 7 | 4,071 | 252,105 | 1 |
| 8 | 16,693 | 1,764,735 | 1 |
| 9 | 67,816 | 12,353,145 | 1 |
| 10 | 275,129 | 86,472,015 | 1 |

In particular, for every integer \(2\le r\le10\),
\[
\max\mathcal B_r=15\cdot7^{r-2}.
\]
This verifies the inequality in Defant's Conjecture 20 for every odd integer \(n>3\) whose stopping time is at most ten. The statement is **not** a proof for larger stopping times.

## Assumptions and scope
For a prime-power factorization \(n=\prod p^a\) with \(n>1\) odd, the second Schemmel totient is
\[
L_2(n)=\prod_{p^a\parallel n}p^{a-1}(p-2),\qquad L_2(1)=1.
\]
For every odd \(n>1\), the integer \(L_2(n)\) is positive, odd and strictly smaller than \(n\); consequently iteration reaches \(1\) in finitely many steps. Define \(R_2(n)\) to be the least positive number of such steps. (The special value at \(n=1\) does not enter any stratum.) All parameters, primality tests and comparisons in the proof are exact integer operations.

## Proof
**Inverse-prime-power lemma.** Fix an odd integer \(m\ge1\). The complete odd preimage \(\{n>1:L_2(n)=m\}\) is constructed as follows. For every positive divisor \(d\mid m\) with \(p=d+2\) prime, choose either no factor \(p\), or precisely one exponent \(a\ge1\) satisfying
\[
c_{p,a}=p^{a-1}(p-2)\mid m.
\]
Keep exactly those selections of distinct primes for which the product of their chosen \(c_{p,a}\) is \(m\); output the corresponding product of prime powers. The output \(n=1\) is omitted. By unique factorization and the displayed formula for \(L_2\), this procedure is both necessary and sufficient. There are finitely many choices: \(p-2\) divides \(m\), and the exponent is bounded by the divisibility of \(p^{a-1}(p-2)\) into \(m\). In particular the otherwise special prime \(p=3\) has no infinite exponent ambiguity, since \(3^{a-1}\mid m\).

**Stopping-time induction.** The only odd integer \(n>1\) satisfying \(L_2(n)=1\) is \(n=3\): in the prime-power product every local factor must equal one, which only occurs at exponent one for prime three. Hence \(\mathcal B_1=\{3\}\). Since \(L_2(n)<n\) for every odd \(n>1\), and each such integer has a unique image, the inverse-prime-power lemma gives the disjoint and exact recurrence
\[
\mathcal B_{r+1}=\bigcup_{m\in\mathcal B_r}\{n>1:L_2(n)=m\}.
\]
There is no bound on \(n\) in this recurrence: only the depth \(r\) is limited.

**Exact finite certificate.** The accompanying standard-library Python program `verify.py` implements the displayed inverse-prime-power lemma, using complete divisor enumeration and deterministic integer trial division for primality. It applies the recurrence successively through \(r=10\), computes every class as an exact set, checks its cardinality, maximum and uniqueness, and verifies forward images on every generated integer. The resulting ten rows are precisely the table under Finding. The included small-range independent forward check also compares direct iteration for every odd \(3\le n\le50000\). Because the lemma and recurrence are proved exact, this exhaustive certificate proves the finite-depth table; this is not an argument from statistical sampling.

For an explicit lower-bound witness, \(L_2(15)=3\) and
\[
L_2(15\cdot7^k)=15\cdot7^{k-1}\quad(k\ge1).
\]
Thus \(R_2(15\cdot7^{r-2})=r\) for every \(r\ge2\); uniqueness of the maximum in the table is proved by the finite exhaustive certificate through rank ten.

**Connection with the conjecture.** The stated bound of Defant's Conjecture 20 is equivalent, for odd \(n>3\), to
\[
n\le15\cdot7^{R_2(n)-2}.
\]
The table verifies this separately for every rank \(2\le R_2(n)\le10\), hence for their union.

## Verification
Run `python3 verify.py` with Python 3 standard library. The program prints ten exact rows and terminates with `EXACT_CERTIFICATE_OK`. It enumerates \(364992\) different integers through rank ten, including \(275129\) at rank ten, and checks the \(50000\) forward-window boundary as described above. The program has no online dependencies or probabilistic primality tests. The result depends on the finite exhaustive execution; an interrupted program is not a certificate.

## Relationship to prior work
Colin Defant, *On Arithmetic Functions Related to Iterates of the Schemmel Totient Functions* (2015), defines \(R_2\), states the universal inequality as Conjecture 20, and plots the first \(300000\) inputs. This result concerns complete stopping-time **rank classes**, rather than a fixed interval of inputs, and establishes exact cardinalities and unique maxima through rank ten. OEIS A241664 records values of the stopping-time function and the same conjecture, but does not state this complete inverse-tree table. Harrington and Jones (2010) study the related exceptional-unit iteration on a restricted domain; no claim about its full unrestricted inverse-rank table is made here.

## Limitations
The result covers exactly the ten stated stopping-time ranks and says nothing about rank eleven or higher. The finite certificate is complete within these ranks but does not establish the global conjecture. The uniqueness assertion is certified only at ranks at most ten. Subsequent or unindexed literature could contain the same finite census. The closely related Harrington--Jones paper could not be fully inspected; its full text remains a prior-work uncertainty.

## References
1. C. Defant, *On Arithmetic Functions Related to Iterates of the Schemmel Totient Functions*, Journal of Integer Sequences **18** (2015), Article 15.2.1, especially Section 4, Conjecture 20. https://cs.uwaterloo.ca/journals/JIS/VOL18/Defant/defant5.pdf
2. OEIS A241664, *Number of iterations of A058026 needed to reach either 0 or 1*. https://oeis.org/A241664
3. J. Harrington and L. Jones, *On the Iteration of a Function Related to Euler's \(\varphi\)-Function*, Integers **10** (2010), 497–515, doi:10.1515/INTEG.2010.042.
