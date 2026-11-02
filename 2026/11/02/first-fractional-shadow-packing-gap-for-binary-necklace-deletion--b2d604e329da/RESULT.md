# First fractional-shadow packing gap for binary necklace deletion codes

## Finding

For each integer \(n\ge1\), let \(\mathcal N_n\) be the set of binary length-\(n\) necklaces (binary words identified under cyclic rotation, **not** reversal or bit complementation). For \(u\in\mathcal N_n\), define its one-deletion shadow \(D_n(u)\subseteq\mathcal N_{n-1}\) as the set of rotation classes obtained by deleting exactly one position from any representative. There is a unique empty necklace when \(n=0\). Define

\[
A_n=\max\{|C|:C\subseteq\mathcal N_n,\ D_n(u)\cap D_n(v)=\varnothing\text{ for distinct }u,v\in C\},
\]

and the natural fractional deletion-shadow packing optimum

\[
F_n=\max\left\{\sum_{u\in\mathcal N_n}x_u:\ x_u\ge0,\ \sum_{u:\,y\in D_n(u)}x_u\le1\ \text{for every }y\in\mathcal N_{n-1}\right\}.
\]

The integer and fractional optima agree for every \(1\le n\le8\), with their common values

\[
(A_1,\ldots,A_8)=(F_1,\ldots,F_8)=(1,2,2,3,3,5,6,8).
\]

At length nine, however,

\[
\boxed{A_9=9\quad\text{and}\quad F_9=\frac{41}{4}.}
\]

Consequently \(n=9\) is the **first blocklength** at which the natural fractional deletion-shadow packing relaxation is nonintegral in optimal value for binary rotation classes. This is a finite theorem, not an extrapolation to longer lengths.

## Assumptions and scope

Each necklace is an equivalence class under cyclic shifts only. A deletion removes one bit, after which the receiver observes the remaining binary circle without a distinguished starting point. The input and output are thus both rotation classes. Deleting from other representatives produces the same set of output necklaces. A code corrects this channel exactly when distinct codewords have disjoint deletion shadows. Repeated deletions producing the same output are counted once, not with multiplicity.

The integer \(A_n\) counts messages represented by distinct necklaces, not the number of labeled rooted words in a standard deletion code. The fractional quantity \(F_n\) is the displayed *output-capacity* linear program, not a pairwise-clique relaxation or a probability of channel error.

## Proof

**1. Finite universe and exact shadows.** For any word \(w\in\{0,1\}^n\), write \(\operatorname{can}(w)\) for its lexicographically smallest rotation, with \(\operatorname{can}(\epsilon)=\epsilon\). Then

\[
\mathcal N_n=\{\operatorname{can}(w):w\in\{0,1\}^n\},\qquad
D_n(\operatorname{can}(w))=\{\operatorname{can}(w_0\cdots w_{i-1}w_{i+1}\cdots w_{n-1}):0\le i<n\}.
\]

Rotating \(w\) before deleting a position merely rotates the resulting word, so this formula is well-defined and exhaustive. It gives \(|\mathcal N_9|=60\) and \(|\mathcal N_8|=36\).

**2. Integral witnesses and fractional upper bounds for \(1\le n\le8\).** For each length, `certificates.json` contains a complete explicit set \(C_n\) of size \(1,2,2,3,3,5,6,8\), respectively, and a nonnegative rational weight \(z_y\) on each length-\((n-1)\) output necklace, zero unless listed. Direct exact checks give

\[
\sum_{y\in D_n(u)}z_y\ge1\quad(\forall u\in\mathcal N_n),
\qquad \sum_{y\in\mathcal N_{n-1}}z_y=|C_n|.
\]

For any fractional packing \((x_u)\), these inequalities imply
\[
\sum_u x_u\le\sum_u x_u\sum_{y\in D_n(u)}z_y
=\sum_y z_y\sum_{u:y\in D_n(u)}x_u\le\sum_y z_y.
\]

Each \(C_n\) is feasible since its shadows are disjoint, and its incidence vector is itself a feasible fractional packing. Therefore \(A_n=F_n=|C_n|\) for all eight lengths. The length-one boundary case uses the empty output necklace and is checked explicitly.

**3. Exact fractional optimum at nine.** The length-nine certificate supplies a nonnegative rational fractional input packing \((x_u)\) and an output covering \((z_y)\), each having objective value exactly \(41/4\). Every one of the 36 output capacities is checked for the input packing; every one of the 60 input covering inequalities is checked for the dual. Weak duality in both directions proves \(F_9=41/4\) without relying on a floating-point solver.

**4. Integral optimum at nine.** One feasible nine-word code, written by canonical necklace representatives, is

```
000000001  000011101  000100011
001001001  001100111  001111101
010101011  011101111  111111111
```

Its 36-orbit output universe contains no necklace that is a deletion of two different displayed codewords; `verify.py` checks all pairs. For the converse, form the 60-vertex *conflict graph*, joining different input necklaces exactly when they share an output necklace. A correcting code is an independent set. The certificate contains nineteen explicit vertex subsets \(Q\), each checked to be a clique of this conflict graph, with nonnegative rational weights \(\lambda_Q\). It verifies for every input necklace \(u\) that

\[
\sum_{Q\ni u}\lambda_Q\ge1,
\qquad \sum_Q\lambda_Q=\frac{59}{6}<10.
\]

For any independent set \(C\), every clique \(Q\) has \(|C\cap Q|\le1\), so

\[
|C|\le\sum_{u\in C}\sum_{Q\ni u}\lambda_Q
=\sum_Q\lambda_Q|C\cap Q|\le\frac{59}{6}<10.
\]

Thus \(|C|\le9\). With the exhibited code, \(A_9=9\). Together with the preceding eight cases and the exact fractional value, this proves the first-gap statement.

## Verification

`certificates.json` contains all nine integral lower-bound witnesses, matching output-shadow dual weights through length eight, and the length-nine primal, dual, and nineteen-clique fractional covering certificate. `verify.py` is a standalone Python 3 verifier using only the standard library and exact `fractions.Fraction` arithmetic. From the directory containing these two files, execute `python verify.py`. The expected output begins with `VERIFY_OK` and reports the integral profile, \(F_9=41/4\), and the clique-cover value \(59/6\). This verifies each universal quantifier in the finite domains by reconstructing all binary words and all cyclic rotations; optimization software is not trusted in the final check.

## Relationship to prior work

The ordinary deletion-shadow graph and conventional single-deletion code bounds appear in N. J. A. Sloane's 2002 survey. Its codewords are *rooted* linear words, and its discussion of necklace counts concerns shift-register enumeration, not the deletion channel on rotation classes. Abdel-Ghaffar, Ferreira, and Cheng (2010) study **ordinary** deletion correction within linear/cyclic codes and by extension or expurgation; their theorem about cyclic linear codes is not a theorem about distinct unrooted necklace messages with unrooted outputs. Adamson, Deligkas, Gusev, and Potapov (2020) study \(k\)-centre approximation on necklaces using overlap distance rather than deletion-shadow disjointness. The exact finite optima and first relaxation gap claimed here are not consequences of those inspected statements. They are not claims of priority over all uncatalogued literature.

## Limitations

Only the binary alphabet, the rotation quotient (not bracelets), and **exactly one deletion** are covered. The classification stops at length nine; neither asymptotic packing behavior nor equality-class counts are claimed. The test proves mathematical feasibility of the displayed finite certificates, not independent historical priority or laboratory performance. The use of the term *first* is with respect to all positive blocklengths in precisely the defined mathematical model, not all related deletion coding models.

## References

1. N. J. A. Sloane, *On Single-Deletion-Correcting Codes*, arXiv:math/0207197, first posted 22 July 2002. https://arxiv.org/html/math/0207197v1
2. K. A. S. Abdel-Ghaffar, H. C. Ferreira, L. Cheng, *Correcting Deletions Using Linear and Cyclic Codes*, IEEE Transactions on Information Theory **56** (2010), 5223–5234. https://doi.org/10.1109/TIT.2010.2059790
3. D. Adamson, A. Deligkas, V. V. Gusev, I. Potapov, *The K-Centre Problem for Necklaces*, arXiv:2005.10095, first posted 20 May 2020. https://arxiv.org/abs/2005.10095
