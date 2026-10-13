# Five copies per population are the sharp polymorphic biallelic G_ST–Jost D ranking-reversal boundary
## Finding
Consider two equally weighted biallelic populations. Let the exact frequency of allele A be
\[
p=\frac{a}{m}
\]
in the first population and
\[
q=\frac{b}{m}
\]
in the second, where
\[
1\le a,b\le m-1.
\]
Thus both alleles are present in both populations.

Write the mean within-population heterozygosity as
\[
H_S=p(1-p)+q(1-q),
\]
and the total heterozygosity of the pooled population as
\[
H_T=2\bar p(1-\bar p),
\qquad
\bar p=\frac{p+q}{2}.
\]

Nei's differentiation statistic is
\[
G_{ST}=\frac{H_T-H_S}{H_T},
\]
and for two populations Jost differentiation is
\[
D=2\frac{H_T-H_S}{1-H_S}.
\]

Define the allele-count gap and pooled-frequency imbalance by
\[
d=|a-b|,
\qquad
t=|a+b-m|.
\]
Then
\[
G_{ST}=\frac{d^2}{m^2-t^2},
\qquad
D=\frac{2d^2}{m^2+d^2+t^2}.
\]

Hence, if two population pairs have the same nonzero count gap \(d\), increasing \(t\)—moving the pooled allele frequency farther from one half—strictly increases \(G_{ST}\) while strictly decreasing \(D\).

No strict ranking reversal is possible on the positive frequency grids with
\[
m\le4.
\]

At
\[
m=5,
\]
a strict reversal occurs for the first time and is unique up to exchanging the populations and globally relabeling the two alleles. It compares
\[
(a,b)=(1,2)
\]
with
\[
(a,b)=(2,3).
\]

For \((1,2)\),
\[
G_{ST}=\frac1{21},
\qquad
D=\frac1{15}.
\]
For \((2,3)\),
\[
G_{ST}=\frac1{25},
\qquad
D=\frac1{13}.
\]
Therefore
\[
\frac1{21}>\frac1{25}
\]
but
\[
\frac1{15}<\frac1{13}.
\]
So \(G_{ST}\) declares the first population pair more differentiated, while Jost \(D\) declares the second more differentiated.

The reversal is structural rather than isolated. For every \(m\ge5\), compare \((1,2)\) with the adjacent pair nearest pooled frequency one half: use
\[
\left(\frac{m-1}{2},\frac{m+1}{2}\right)
\]
for odd \(m\), and
\[
\left(\frac m2-1,\frac m2\right)
\]
for even \(m\). Both comparisons have \(d=1\), but the first is farther from pooled frequency one half, so the two differentiation measures rank them in opposite strict orders.

## Assumptions and scope
The theorem concerns one biallelic locus and two equally weighted populations.

The frequencies are exact rational population frequencies on a common denominator \(m\). They are not treated as noisy estimates from an underlying larger population.

Both alleles must be present in both populations. If fixation is allowed, smaller-grid reversals occur; the positive-frequency restriction isolates disagreement away from the boundary of the allele-frequency simplex.

Population labels are irrelevant, and a global exchange of the two allele labels is treated as the same configuration.

The theorem uses the theoretical heterozygosity definitions of \(G_{ST}\) and Jost \(D\), not finite-sample bias-corrected estimators.

## Proof
For a biallelic population with allele-A frequency \(p\), heterozygosity is
\[
2p(1-p).
\]
Averaging the two populations gives
\[
H_S=p(1-p)+q(1-q).
\]
The pooled allele-A frequency is
\[
\bar p=\frac{p+q}{2},
\]
so
\[
H_T=2\bar p(1-\bar p).
\]
A direct expansion yields
\[
H_T-H_S=\frac{(p-q)^2}{2}=\frac{d^2}{2m^2}.
\]
Also,
\[
H_T=\frac{(a+b)(2m-a-b)}{2m^2}.
\]
Since
\[
(a+b)(2m-a-b)=m^2-(a+b-m)^2=m^2-t^2,
\]
we obtain
\[
G_{ST}=\frac{d^2}{m^2-t^2}.
\]

For Jost \(D\),
\[
1-H_S
=1-\frac{a(m-a)+b(m-b)}{m^2}.
\]
Using
\[
a^2+b^2=\frac{(a+b)^2+(a-b)^2}{2},
\]
this becomes
\[
1-H_S
=\frac{m^2+d^2+t^2}{2m^2}.
\]
Therefore
\[
D=2\frac{H_T-H_S}{1-H_S}
=\frac{2d^2}{m^2+d^2+t^2}.
\]

For fixed nonzero \(d\), the denominator of \(G_{ST}\) strictly decreases with \(t\), while the denominator of \(D\) strictly increases with \(t\). Thus their rankings by pooled-frequency imbalance are exactly opposite.

The positive grids with \(m=2,3,4\) are finite and are exhaustively checked by the verifier, with no strict reversal.

At \(m=5\), the same exhaustive check finds exactly one reversal class, represented by \((1,2)\) versus \((2,3)\), with the exact values displayed above.

For persistence, both proposed comparisons at every \(m\ge5\) have \(d=1\). The pair \((1,2)\) has
\[
t=m-3.
\]
The central adjacent pair has \(t=0\) for odd \(m\) and \(t=1\) for even \(m\). For \(m\ge5\),
\[
m-3>1,
\]
so the fixed-gap antimonotonicity gives the strict reversal.

## Verification
The embedded `verify_gst_jost_boundary.py` uses exact rational arithmetic.

It enumerates every polymorphic biallelic two-population frequency pair for denominators
\[
2\le m\le5,
\]
quotients by population exchange and global allele relabeling, and checks every unordered pair of resulting configurations.

It confirms no reversal for \(m\le4\) and exactly one at \(m=5\).

It independently checks the closed forms
\[
G_{ST}=\frac{d^2}{m^2-t^2},
\qquad
D=\frac{2d^2}{m^2+d^2+t^2},
\]
verifies fixed-gap opposite monotonicity over a broad finite range, and replays the explicit reversal family for every \(5\le m\le100\).

Run:

`python3 verify_gst_jost_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Jost showed that \(G_{ST}\) can misrank population pairs as a measure of differentiation and gave examples where a more strongly differentiated system receives a lower \(G_{ST}\). He introduced \(D\) as a differentiation measure based on multiplicative diversity partitioning.

Meirmans and Hedrick review the relationship between \(G_{ST}\) and Jost \(D\), give
\[
D=\frac{k}{k-1}\frac{H_T-H_S}{1-H_S},
\]
and emphasize that the relation can be especially nontrivial for pairwise comparisons when the number of populations is small.

The present result does not claim that disagreement between \(G_{ST}\) and \(D\) is new. Its contribution is the exact biallelic two-population mechanism: at fixed allele-frequency difference, the two measures respond in opposite directions to pooled heterozygosity, and five copies per population are the smallest strictly polymorphic common-denominator grid on which this produces a ranking reversal.

Targeted searches using \(G_{ST}\), Jost \(D\), biallelic populations, pairwise differentiation, fixed allele-frequency difference, pooled heterozygosity, exact count pairs, and the values \(1/21,1/25,1/15,1/13\) did not locate this sharp finite statement.

## Limitations
The result is deliberately restricted to one biallelic locus and two equally weighted populations.

It concerns exact frequency-grid values, not bias-corrected estimators from samples.

Allowing a population to be fixed for one allele lowers the first reversal denominator from five to three, so the positivity assumption is substantive.

The theorem does not decide which differentiation concept is preferable for inference about migration, drift, selection, or conservation; the literature distinguishes these interpretations carefully.

An unindexed teaching example or software test could contain the \(m=5\) witness without identifying the sharp positive-grid cutoff or the fixed-gap antimonotonicity theorem.

## References
1. L. Jost, “G_ST and its relatives do not measure differentiation,” *Molecular Ecology* 17(18), 4015–4026, 2008. DOI: 10.1111/j.1365-294X.2008.03887.x. Version of record online 29 August 2008.
2. P. G. Meirmans and P. W. Hedrick, “Assessing population structure: F_ST and related measures,” *Molecular Ecology Resources* 11(1), 5–18, 2011. DOI: 10.1111/j.1755-0998.2010.02927.x. First published 26 October 2010.
