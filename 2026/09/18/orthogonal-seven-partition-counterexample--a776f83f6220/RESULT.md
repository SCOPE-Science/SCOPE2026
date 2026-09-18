# A 70-point counterexample to orthogonal 7-partitions

## Result

There exists a centrally symmetric set \(P\subset \mathbb{Z}^2\) of 70 points for which no two perpendicular lines, even under the weak boundary-assignment convention, partition \(P\) into four cyclic classes of sizes
\[
7,\quad 7,\quad 28,\quad 28.
\]
Hence the smallest integer \(k\) for which the planar discrete orthogonal-partition problem admits a counterexample is at most \(7\). Since \(k=1\) is known to be always solvable, the smallest such integer lies in \(\{2,3,4,5,6,7\}\).

This improves the previously explicit counterexample at \(k=8\) in Leonardo Martínez-Sandoval, *Counterexamples and Symmetry for Uneven Orthogonal Mass Partitions in the Plane*, arXiv:2609.16757 (2026), whose Problem 8.4 asks specifically whether a counterexample exists for some \(2\le k\le7\).

## Construction

Let
\[
P=\{p_1,\ldots,p_{35},-p_1,\ldots,-p_{35}\},
\]
where the representatives are:

| \(i\) | \(x_i\) | \(y_i\) | \(i\) | \(x_i\) | \(y_i\) |
|---:|---:|---:|---:|---:|---:|
| 1 | 9819 | -2040 | 2 | 11243 | 4733 |
| 3 | 14190 | 7834 | 4 | 11346 | 2091 |
| 5 | 12771 | 7469 | 6 | 11823 | 5289 |
| 7 | 12740 | 7482 | 8 | 14801 | 23200 |
| 9 | 6088 | 7088 | 10 | 21833 | 30621 |
| 11 | 5789 | 7430 | 12 | -555 | 12635 |
| 13 | 7842 | 15683 | 14 | 1395 | 11274 |
| 15 | 5735 | 7425 | 16 | 5790 | 5801 |
| 17 | -1581 | 7384 | 18 | -86 | 11967 |
| 19 | 5479 | 6853 | 20 | -19959 | 27734 |
| 21 | -9521 | 2933 | 22 | -20592 | 27518 |
| 23 | -12753 | 10971 | 24 | -9879 | 1919 |
| 25 | -22191 | 22391 | 26 | -26821 | 30017 |
| 27 | -6656 | 5663 | 28 | -8957 | 3615 |
| 29 | -28523 | 33939 | 30 | -4555 | 6755 |
| 31 | -9719 | 2427 | 32 | -9202 | 3386 |
| 33 | -3277 | 7149 | 34 | -9554 | 2691 |
| 35 | -8713 | 3961 |  |  |  |

The 70 points are distinct, and no three are collinear.

## Exact certificate

Write \(N=70=2m\), so \(m=35\), and let \(k=7\). For a nonzero direction \(n\), put \(u=Jn=(-n_y,n_x)\). Following the finite reduction in Appendix B of arXiv:2609.16757, let
\[
A=\operatorname{Top}_m(u),\qquad B=\operatorname{Top}_{2k}(n),
\]
where all admissible choices are allowed when the cutoff projection is tied. If
\[
q=|A\cap B|,
\]
then the four cyclic sector counts are
\[
q,\quad m-q,\quad m-2k+q,\quad 2k-q.
\]
Thus a weak orthogonal \(7\)-partition exists exactly when \(q=7\) for some direction and some admissible tied-cutoff assignment.

Projection orders can change only when \(n\) is parallel or perpendicular to a difference \(p_i-p_j\). Exact integer arithmetic gives 2450 critical projective rays. Central symmetry identifies antipodal directions, so these rays cut one projective direction circle into 2450 open chambers.

For one exact sample in each open chamber, the values of \(q\) are
\[
q=8\quad\text{in 2351 chambers},\qquad
q=9\quad\text{in 99 chambers}.
\]
At the critical rays, every admissible tied-cutoff assignment was enumerated exactly. The possible \(q\)-sets are
\[
\{8\}\quad\text{at 2331 rays},\qquad
\{9\}\quad\text{at 79 rays},\qquad
\{8,9\}\quad\text{at 40 rays}.
\]
In particular, \(q=7\) never occurs. Therefore no weak orthogonal \(7\)-partition exists.

The standalone verifier `artifacts/verify.py` reproduces these counts using only integer arithmetic and the Python standard library. It also checks distinctness and absence of collinear triples.

## Context and value

Martínez-Sandoval proves that every even planar point set has an orthogonal \(1\)-partition, recalls that convex-position sets admit all targets, and gives a 96-point counterexample at \(k=8\). Problem 8.4 in that paper asks for the smallest counterexample parameter and explicitly asks whether any counterexample exists for \(2\le k\le7\). The construction above answers the latter question affirmatively at \(k=7\), lowering the explicit upper bound from \(8\) to \(7\).

## Limitations

This result does not determine the smallest counterexample parameter: \(k=2,\ldots,6\) remain unresolved here. It also does not claim that 70 is the minimum number of points for a \(k=7\) counterexample, nor that the displayed configuration is unique. The certificate is an exact finite computation, not a formal proof-assistant verification.

The motivating preprint is very recent, so unindexed or unpublished parallel work remains a residual originality risk.

## Reproducibility

Run:

```text
python3 artifacts/verify.py
```

The expected exact summary is:

```text
points=70
representatives=35
critical_projective_rays=2450
open_projective_chambers=2450
open_q_counts={8: 2351, 9: 99}
critical_q_sets={(8,): 2331, (8, 9): 40, (9,): 79}
max_cutoff_tie=2
distinct_points=True
no_three_collinear=True
no_weak_orthogonal_7_partition=True
```

## Reference

- Leonardo Martínez-Sandoval, *Counterexamples and Symmetry for Uneven Orthogonal Mass Partitions in the Plane*, arXiv:2609.16757v1, submitted 15 September 2026. https://arxiv.org/abs/2609.16757
