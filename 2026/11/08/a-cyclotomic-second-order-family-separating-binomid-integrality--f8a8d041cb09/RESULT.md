# A cyclotomic second-order family separating binomid integrality from divisibility

## Finding

For integers \(q\ge 2\), \(t\ge 1\), define \(f_0=-(t+1)\), \(f_1=q\), and
\[
f_{n+2}=-q f_{n+1}-q^2 f_n\qquad(n\ge0).
\]
For \(0\le k\le n\), define the generalized binomial coefficient
\[
{n\brack k}_f=\frac{\prod_{j=n-k+1}^{n}f_j}{\prod_{j=1}^{k}f_j},
\]
with empty products equal to \(1\). Call the sequence *binomid* if these are integers for every \(n\ge k\ge0\), and *divisible* if \(f_m\mid f_n\) whenever \(m,n\ge1\) and \(m\mid n\).

**Theorem.** The following are exact equivalences for this complete two-parameter family:
\[
\boxed{f\text{ is binomid}\iff t\mid q^4,\qquad
f\text{ is divisible}\iff t\mid q^2.}
\]
In particular, for each \(q\ge2\), any choice \(t\mid q^4\) with \(t\nmid q^2\) yields a binomid, nondivisible sequence satisfying a genuine second-order integer recurrence. Such choices exist for every \(q\ge2\); for instance take \(t=q^3\).

## Assumptions and scope

All parameters and indices above are integers in the specified ranges. Negative terms are permitted: binomid means *integer*, not necessarily nonnegative, generalized coefficients, consistently with the definition for nonzero integer sequences in Shapiro (2023). Every positive-index term in the stated family is nonzero. The assertion concerns binomid integrality at the base triangle level only; no assertion of integrality at every level of the binomid pyramid is made.

The recurrence has characteristic polynomial \(X^2+qX+q^2\), whose distinct complex roots are \(q\exp(2\pi i/3)\) and \(q\exp(-2\pi i/3)\). These roots have modulus \(q>1\), so the sequence is unbounded in absolute value and is not eventually periodic.

## Proof

**1. Explicit recurrence solution.** Define the three-periodic integer weights
\[
u_{3j+1}=1,\qquad u_{3j+2}=t,\qquad
u_{3j+3}=-(t+1)\qquad(j\ge0),
\]
with \(u_0=-(t+1)\). Since every three successive weights sum to zero, the sequence \(f_n=q^nu_n\) satisfies \(f_{n+2}=-qf_{n+1}-q^2f_n\) and the prescribed initial values. Thus it is the unique solution, and every term is a nonzero integer.

**2. Block-count formula.** Fix \(n\ge k\ge1\), and write \(s=n-k\). For \(r\in\{0,2\}\), let
\[
E_r(n,k)=\#\{j:s+1\le j\le n,\ j\equiv r\pmod3\}
-\#\{j:1\le j\le k,\ j\equiv r\pmod3\}.
\]
The exponent difference of \(q\) between numerator and denominator is
\[
\sum_{j=s+1}^{s+k}j-\sum_{j=1}^k j=ks=k(n-k).
\]
The factors from the three weight classes therefore give the exact rational identity
\[
{n\brack k}_f=q^{k(n-k)}t^{E_2(n,k)}\bigl(-(t+1)\bigr)^{E_0(n,k)}.
\]

**3. All-index integrality.** Any block of \(k\) consecutive integers contains at least \(\lfloor k/3\rfloor\) multiples of three; the initial block \([1,k]\) contains exactly that many. Hence \(E_0(n,k)\ge0\) always.

For the residue class \(2\pmod3\), the initial block has the minimum possible count if \(k\equiv1\pmod3\), has the same count as any block if \(3\mid k\), and has the maximum possible count if \(k\equiv2\pmod3\). Consequently \(E_2(n,k)\ge-1\); a negative value is necessarily \(-1\), and it can occur only when \(k\equiv2\pmod3\), with the terminal block starting at a multiple of three. Such a terminal block cannot start at \(0\) or a negative index, and the earliest possible start is \(3\). Thus \(k\ge2\) and \(s=n-k\ge2\), giving \(k(n-k)=ks\ge4\). If \(t\mid q^4\), the power \(q^{ks}\) cancels the only possible denominator \(t\). The nonnegative powers of \(-(t+1)\) and any remaining power of \(t\) are integers. The boundary cases \(k=0\) and \(k=n\) give coefficient \(1\). Therefore all coefficients are integers.

Conversely, the first possible negative residue-count case is \((n,k)=(4,2)\). Direct calculation gives
\[
{4\brack2}_f=\frac{f_4f_3}{f_2f_1}
=-\frac{q^4(t+1)}{t}.
\]
Since \(\gcd(t,t+1)=1\), this rational is integral only if \(t\mid q^4\). This proves the first equivalence.

**4. Index divisibility.** Suppose \(m\ge1\) divides \(n\ge m\). By the explicit formula,
\[
\frac{f_n}{f_m}=q^{n-m}\frac{u_n}{u_m}.
\]
If \(m\equiv0\pmod3\), then \(n\equiv0\pmod3\), so the weight ratio is \(1\). If \(m\equiv1\pmod3\), then \(u_m=1\), so the ratio is integral. If \(m\equiv2\pmod3\), then \(u_m=t\). When \(n\equiv2\pmod3\), the weight ratio is again \(1\). Otherwise \(n\ge2m\), whence \(n-m\ge m\ge2\), and the only possible denominator is \(t\), multiplying either \(1\) or \(-(t+1)\). Therefore \(t\mid q^2\) ensures divisibility for every pair of indices.

For necessity, use the pair \(m=2\), \(n=4\):
\[
\frac{f_4}{f_2}=\frac{q^4}{tq^2}=\frac{q^2}{t}.
\]
It is integral only if \(t\mid q^2\). This proves the second equivalence.

**5. Explicit counterexample.** Take \(q=2\), \(t=8\). Then \(8\mid16\) but \(8\nmid4\), so \(f\) is binomid and not divisible. The initial terms are
\[
-9,\ 2,\ 32,\ -72,\ 16,\ 256,\ -576,\ldots
\]
and \({4\brack2}_f=-18\) is integral while \(32\nmid16\). Because \(t=q^3\) satisfies \(t\mid q^4\) and \(t\nmid q^2\) for each \(q\ge2\), there are infinitely many such distinct recurrences. \(\square\)

## Verification

The standalone file `artifacts/check.py` reconstructs the recurrence directly and checks all generalized coefficients as exact ratios of integer products, without invoking the closed-form proof to determine integrality. It tests \(1950\) parameter pairs \((q,t)\) with \(2\le q\le14\), \(1\le t\le150\), all indices through \(23\), and checks five nondivisible binomid choices through index \(100\). It also checks the closed form and the explicit counterexample. Execute with `python3 artifacts/check.py`; its deterministic stdout is in `artifacts/check_output.txt`. These finite tests corroborate but do not establish the universal quantifiers; the block-count argument above does.

## Relationship to prior work

Shapiro, *Divisibility Properties for Integer Sequences* (arXiv:2302.02243, publicly posted 2023-02-04), Section 4.4, Question 27(1), asks whether binomid sequences satisfying a second-order constant-coefficient recurrence must be divisibility sequences. The stated theorem gives a negative answer to its binomid (base-level) implication; it does not decide the stronger 'binomid at every level' implication or classify every second-order recurrence.

Caalim and Tanaka's 2024 and 2025 work provides a general theory of positive binomid indices, including periodic and eventually periodic index structures. This paper uses a three-residue block-count calculation specialized to the signed second-order cyclotomic recurrence and identifies the precise sharp constraints on its two parameters. Koshkin's 2022 work classifies *divisibility* recurrences in a cyclotomic context; that property is stronger and fails in the counterexample here. Comparison with these results concerns theorem hypotheses and implications, not merely matching vocabulary.

## Limitations

This is a two-parameter cyclotomic slice, not a complete classification of all second-order binomid recurrences. The example has some negative terms, permissible under Shapiro's nonzero-integer definition; no example with every term positive and second-order recurrent is claimed. Binomid integrality beyond the base triangle and novelty beyond the inspected primary literature require separate investigation. External independent validation has not been performed.

## References

1. D. B. Shapiro, *Divisibility Properties for Integer Sequences*, arXiv:2302.02243 (first posted 2023-02-04), Section 4.4, Question 27; https://arxiv.org/abs/2302.02243.
2. J. Caalim and Y. Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, Integers 24 (2024), A53; DOI: 10.5281/zenodo.11221709.
3. J. Caalim and Y. Tanaka, *On the monoid of lexicographically minimal extensions*, arXiv:2505.20018 (2025); https://arxiv.org/abs/2505.20018.
4. S. Koshkin, *Non-classical linear divisibility sequences and cyclotomic polynomials*, arXiv:2206.09493 (2022); https://arxiv.org/abs/2206.09493.
