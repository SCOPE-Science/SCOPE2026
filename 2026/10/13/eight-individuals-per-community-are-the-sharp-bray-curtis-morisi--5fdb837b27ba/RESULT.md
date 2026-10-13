# Eight individuals per community are the sharp Bray–Curtis–Morisita–Horn reversal boundary
## Finding
Fix a common species set of size
\[
k\ge2.
\]

Each community has strictly positive integer abundances
\[
x_1,\ldots,x_k
\]
and total census size
\[
\sum_i x_i=N.
\]

For two communities \(x\) and \(y\) with the same total \(N\), use Bray–Curtis similarity
\[
B(x,y)=\frac{\sum_i\min(x_i,y_i)}{N}
\]
and Morisita–Horn similarity
\[
H(x,y)=
\frac{2\sum_i x_i y_i}
{\sum_i x_i^2+\sum_i y_i^2}.
\]

No two such community comparisons receive opposite strict similarity rankings from \(B\) and \(H\) when
\[
N\le7.
\]

At
\[
N=8,
\]
strict reversal appears for the first time. It necessarily uses
\[
k=4,
\]
and, up to joint species relabeling and exchange of the two communities in either comparison, the first-layer reversal is unique.

Comparison \(A\) is
\[
(1,1,2,4)
\quad\text{versus}\quad
(1,4,2,1).
\]
It has
\[
B(A)=\frac58,
\qquad
H(A)=\frac{13}{22}.
\]

Comparison \(C\) is
\[
(1,1,3,3)
\quad\text{versus}\quad
(3,3,1,1).
\]
It has
\[
B(C)=\frac12,
\qquad
H(C)=\frac35.
\]

Therefore
\[
B(A)>B(C)
\]
but
\[
H(A)<H(C).
\]

Bray–Curtis judges \(A\) more similar, while Morisita–Horn judges \(C\) more similar.

The phenomenon is not confined to census size eight. Multiplying every abundance in both comparisons by any positive integer \(q\) leaves both similarities unchanged, so the same reversal occurs at every total
\[
N=8q.
\]

## Assumptions and scope
All four communities being ranked have the same total abundance \(N\), and each has positive abundance for every one of the same \(k\) species.

The positivity restriction removes presence–absence turnover: the disagreement is caused purely by how the two abundance-sensitive similarities weight shared species.

Bray–Curtis is written as a similarity rather than its complementary dissimilarity. Replacing either similarity by its complement reverses its numerical direction but not the substantive ordering comparison.

Morisita–Horn is the sampling-with-replacement form
\[
\frac{2\sum_i p_iq_i}{\sum_i p_i^2+\sum_i q_i^2},
\]
which reduces to the count formula above for equal totals.

## Proof
For fixed \(N\) and \(k\), every admissible community is a positive integer composition of \(N\) into \(k\) parts.

A community comparison is unchanged by jointly relabeling species and by swapping its two communities. It can therefore be represented canonically by sorting the coordinate pairs
\[
(x_i,y_i)
\]
and taking the lexicographically smaller representative after also allowing
\[
(x_i,y_i)\leftrightarrow(y_i,x_i).
\]

For each
\[
2\le N\le8
\]
and every
\[
2\le k\le N,
\]
the verifier generates every positive composition, every pair of communities, and every canonical comparison type. It then compares every unordered pair of comparison types having the same \(N\) and \(k\).

The total numbers of canonical comparison types, summed over richness values, are
\[
1,3,7,15,32,66,137
\]
for
\[
N=2,3,4,5,6,7,8.
\]

The corresponding numbers of within-richness ranking comparisons are
\[
0,1,7,31,136,566,2357.
\]

The strict-reversal counts are
\[
0,0,0,0,0,0,1.
\]

The sole first reversal is the pair stated in the finding.

For comparison \(A\),
\[
\sum_i\min(x_i,y_i)=5,
\]
so
\[
B(A)=\frac58.
\]
Also
\[
\sum_i x_i y_i=13
\]
and each squared norm is \(22\), hence
\[
H(A)=\frac{26}{44}=\frac{13}{22}.
\]

For comparison \(C\),
\[
\sum_i\min(x_i,y_i)=4,
\]
so
\[
B(C)=\frac12.
\]
Moreover
\[
\sum_i x_i y_i=12
\]
and each squared norm is \(20\), hence
\[
H(C)=\frac{24}{40}=\frac35.
\]

Finally, both indices are homogeneous of degree zero under simultaneous scaling of the two abundance vectors. This proves the infinite scaled family.

## Verification
The embedded `verify_bray_morisita_horn_boundary.py` uses only the Python standard library and exact rational arithmetic.

It generates every positive abundance vector through total eight, canonically quotients all species-label and community-order symmetries, checks every admissible ranking pair, and reproduces the unique first reversal.

It also verifies recurrence under common scaling for
\[
1\le q\le50.
\]
The scaling statement itself follows algebraically from the formulas and is not inferred from that finite replay.

Run:

`python3 verify_bray_morisita_horn_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Bray and Curtis introduced the abundance-sensitive coefficient that became the Bray–Curtis similarity/dissimilarity family in community ecology.

Horn's overlap work supplies the sampling-with-replacement modification underlying the Morisita–Horn similarity.

Chao and coauthors compare Bray–Curtis and Morisita–Horn as established abundance-based similarity indices and emphasize that they behave differently: Morisita–Horn is particularly sensitive to dominant species, while Bray–Curtis has different sampling behavior.

Beck, Holloway, and Schwanghart likewise compare both measures in a broad beta-diversity study. Their full-text analysis places Morisita–Horn in a Simpson-weighted family that increasingly emphasizes common species, while Bray–Curtis is the quantitative Sørensen-type measure. They report that different abundance-based metrics need not yield identical empirical site orderings.

Generic metric disagreement is therefore prior work. The claim here is the exact positive-count, equal-total finite boundary: no strict reversal through seven individuals per community, a unique first reversal at eight, and a complete first-layer classification.

Targeted searches using both metric names, equal sample size, integer abundance, exact witness vectors, smallest reversal, and four-species language did not locate this boundary.

## Limitations
The theorem requires every species to be present in every community. Allowing zero counts creates a different, less controlled boundary problem involving species turnover as well as abundance weighting.

All four communities in the ranking comparison have the same total census size. Bray–Curtis has known sampling-fraction issues outside controlled equal-sampling settings, so unequal totals are deliberately excluded.

The finite census proves only the global lower boundary and first layer. It does not classify every larger unscaled reversal.

The original Bray–Curtis article could not be inspected as a complete lawful full text through the checked route, so no whole-document novelty claim is made from that source alone.

## References
1. J. R. Bray and J. T. Curtis, “An Ordination of the Upland Forest Communities of Southern Wisconsin,” *Ecological Monographs* 27(4), 325–349, first published 1 October 1957. DOI: 10.2307/1942268.
2. H. S. Horn, “Measurement of ‘Overlap’ in Comparative Ecological Studies,” *The American Naturalist* 100(914), 419–424, published 1 September 1966. DOI: 10.1086/282436.
3. A. Chao, R. L. Chazdon, R. K. Colwell, and T.-J. Shen, “Abundance-Based Similarity Indices and Their Estimation When There Are Unseen Species in Samples,” *Biometrics* 62(2), 361–371, first published 21 June 2006. DOI: 10.1111/j.1541-0420.2005.00489.x.
4. J. Beck, J. D. Holloway, and W. Schwanghart, “Undersampling and the measurement of beta diversity,” *Methods in Ecology and Evolution* 4(4), 370–382, first published 25 January 2013. DOI: 10.1111/2041-210X.12023.
