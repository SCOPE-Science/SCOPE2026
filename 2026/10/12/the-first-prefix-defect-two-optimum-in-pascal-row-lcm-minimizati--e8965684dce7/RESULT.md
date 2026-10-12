# The first prefix-defect-two optimum in Pascal-row LCM minimization

## Finding

For Huber's optimization problem, let \(\mathcal P_r=\{\binom{r}{0},\ldots,\binom{r}{\lfloor r/2\rfloor}\}\), and let \(a(n)\) be the minimum least common multiple of \(n\) distinct entries selected from one row. For a support of indices \(S\), define its prefix defect by
\[
\delta(S)=1+\max S-|S|,
\]
and let \(\delta(n)\) be the minimum of \(\delta(S)\) among globally optimal supports.

The least integer \(n\) for which \(\delta(n)=2\) is
\[
n=57.
\]
More precisely,
\[
a(57)=34745667272226689670077824806669345127280961600.
\]
One optimum occurs in row \(120\) with
\[
S_{57}=\{0,1,\ldots,58\}\setminus\{39,40\},
\]
whose defect is \(2\). The corresponding reduction from the full half-row LCM \(\Lambda_{120}\) is
\[
\frac{\Lambda_{120}}{a(57)}=41\cdot61=2501.
\]

Among all \(57\)-element supports having prefix defect at most \(1\), the exact global minimum is
\[
65841579578883348912626466335327204421864343200
=\frac{451}{238}a(57),
\]
attained in row \(118\). The best prefix support has value
\[
130585799498118642010042491565065622103364280680
=\frac{451}{120}a(57),
\]
attained in row \(119\).

## Assumptions and scope

Rows are indexed from \(0\), and only distinct entries through the middle of each Pascal row are used. The statement is an exact finite theorem about the first occurrence of minimum prefix defect \(2\); it does not classify all optimal supports at \(n=57\), and it makes no assertion about later values of \(\delta(n)\).

The finite certification uses the prime-power exclusion principle and finite-row reduction proved in Felix Huber, *Extremal Least Common Multiples in Rows of Pascal's Triangle*, arXiv:2609.23024. Huber's manuscript certifies the defect sequence through \(n=41\), including \(\delta(41)=3\), and explicitly asks how often positive defects occur and how large they become.

## Proof

For a fixed row \(r\), write
\[
v_p(k)=\nu_p\!\left(\binom{r}{k}\right),
\qquad
E_p=\max_{0\le k\le\lfloor r/2\rfloor}v_p(k).
\]
For each prime \(p\) and exponent budget \(0\le e\le E_p\), define the exclusion set
\[
H_{p,e}(r)=\{k:v_p(k)>e\}.
\]
Huber's prime-power exclusion theorem turns the fixed-row minimum into a finite exact optimization over choices of the exponent budgets: if the union of the selected exclusion sets has size at most \(\lfloor r/2\rfloor+1-n\), the surviving row contains at least \(n\) coefficients dividing the corresponding candidate LCM. Therefore maximizing the product of the saved prime powers gives the exact row minimum.

For \(n=57\) and \(r=120\), the maximizing saving is \(41\cdot61\). The relevant exclusion sets are
\[
H_{41,0}(120)=\{39,40\},
\qquad
H_{61,0}(120)=\{60\}.
\]
Their union has three indices. Hence
\[
\frac{\Lambda_{120}}{41\cdot61}
\]
is divisible by every half-row coefficient except those at indices \(39\), \(40\), and \(60\). The first \(57\) surviving indices are exactly
\[
\{0,1,\ldots,58\}\setminus\{39,40\},
\]
giving an optimal row-\(120\) support of defect \(2\).

To prove global optimality, use the finite-row reduction with the displayed row-\(120\) value as an upper bound. The first row beyond the admissible range for which the binomial lower bound exceeds this candidate is \(176\), so only
\[
112\le r\le175
\]
must be searched. Exact prime-power exclusion optimization over every row in this interval gives the displayed value uniquely as the smallest row minimum, with a minimizing row \(120\).

To rule out defects \(0\) and \(1\), a support of defect at most \(1\) can use only indices \(0,1,\ldots,57\). Repeating the exact exclusion optimization on those restricted prefixes across the same finite row range gives the exact minimum
\[
65841579578883348912626466335327204421864343200,
\]
which is strictly larger than \(a(57)\).

Finally, the same exact finite-row computation gives:
| \(n\) | \(\delta(n)\) | an optimal row |
|---:|---:|---:|
| \(42\) | \(1\) | \(91\) |
| \(43\) | \(1\) | \(91\) |
| \(44\) | \(1\) | \(91\) |
| \(45\) | \(0\) | \(92\) |
| \(46\) | \(0\) | \(92\) |
| \(47\) | \(0\) | \(95\) |
| \(48\) | \(0\) | \(95\) |
| \(49\) | \(0\) | \(99\) |
| \(50\) | \(0\) | \(99\) |
| \(51\) | \(0\) | \(101\) |
| \(52\) | \(0\) | \(104\) |
| \(53\) | \(0\) | \(105\) |
| \(54\) | \(0\) | \(107\) |
| \(55\) | \(0\) | \(116\) |
| \(56\) | \(0\) | \(116\) |
| \(57\) | \(2\) | \(120\) |

Huber's Proposition 6.3 already certifies all \(n\le41\): only \(15,23,24,36\) have defect \(1\), all other \(n\le40\) have defect \(0\), and \(\delta(41)=3\). Combining that published prefix with the exact table above proves that \(57\) is the first value with defect exactly \(2\).

## Verification

The accompanying verifier uses Python integer arithmetic only. It independently reconstructs all binomial coefficients, prime valuations, full-row LCMs, prime-power exclusion masks, the finite row bounds, and the restricted-prefix comparisons. It also checks the published \(n=41\), row-\(90\) certificate, reproducing the saving \(23\cdot31\cdot47\) and the five excluded indices \(22,29,30,44,45\).

As a second implementation for the decisive row \(120\), the verifier runs an LCM-state dynamic program that keeps divisibility-minimal LCM states while omitting exactly four of the sixty-one half-row entries. It returns the same row minimum as the prime-power exclusion computation.

## Relationship to prior work

Huber proves the exact prime-power exclusion framework, the finite-row reduction, asymptotic localization of optimal rows, and the first two finite structural transitions. His certified finite data establish the defect sequence only through \(n=41\), where the minimum defect first exceeds \(1\), and the manuscript's outlook asks for finer information about the size and frequency of \(\delta(n)\).

The present result uses that framework to determine the next missing natural defect value: the first exact occurrence of \(\delta(n)=2\). Searches of the primary manuscript, its indexed descriptions, published-finding corpus records, and exact-value/parameter aliases found no statement implying the \(n=57\) transition.

## Limitations

This theorem is finite. It does not bound the future growth of \(\delta(n)\), determine the next occurrence of defect \(2\), or classify every optimizer at \(n=57\). The ancillary reproducibility archive accompanying arXiv:2609.23024 was not independently retrieved; the manuscript itself expressly describes its supplementary defect certification as proving the claims through \(n=41\). The exact computations here therefore independently cover the new range \(42\le n\le57\).

## References

1. Felix Huber, *Extremal Least Common Multiples in Rows of Pascal's Triangle*, arXiv:2609.23024, first submitted 2026-09-19; inspected version 2.
2. Bakir Farhi, *An identity involving the least common multiple of binomial coefficients and its application*, American Mathematical Monthly 116 (2009), 836–839.
3. Wolfram MathWorld, *Pascal's Triangle*, entry incorporating Huber's asymptotic and the certified transitions at \(n=15\) and \(n=41\).
