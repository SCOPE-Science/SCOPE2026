# Exact two-child and three-child profiles of multiplicity-four numerical semigroups

## Finding

Let \(e_d(g)\) count numerical semigroups of multiplicity \(4\), genus \(g\), and exactly \(d\) children in the **full** numerical-semigroup tree. A child is obtained by removing a minimal generator strictly larger than the Frobenius number; its multiplicity need not remain \(4\). For every integer \(g\ge3\),

\[
\boxed{\sum_{g\ge3}e_2(g)z^g=\frac{z^5(1+z+z^3)}{(1-z)(1-z^5)}}.
\]

Equivalently, with a summand interpreted as zero when \(g<j\),

\[
\boxed{e_2(g)=\sum_{j\in\{5,6,8\}}\max\!\left\{0,1+\left\lfloor\frac{g-j}{5}\right\rfloor\right\}}.
\]

There is **exactly one** multiplicity-four semigroup having three children for each genus \(g\ge4\), and exactly one with four children, namely the ordinary semigroup of genus \(3\). No multiplicity-four semigroup has more than four children. Thus

\[
\boxed{\sum_{g\ge3}e_3(g)z^g=\frac{z^4}{1-z},\qquad \sum_{g\ge3}e_4(g)z^g=z^3.}
\]

The complete branching-degree distribution is determined by these formulas, the existing zero-child census, and the existing total count: \(e_1(g)=N_4(g)-e_0(g)-e_2(g)-e_3(g)-e_4(g)\). In particular, \(e_2(g)=\frac35g+O(1)\). The novelty claimed here is the **two-child and three-child classification and their exact counts**, not a new proof of the previously available zero-child or total formulas.

## Assumptions and scope

A numerical semigroup \(S\) is a cofinite additive submonoid of \(\mathbb N_0\). Its genus is \(g=\#(\mathbb N_0\setminus S)\), its Frobenius number \(F\) is its greatest gap, and its multiplicity is its least positive element. Set

\[
\operatorname{Ap}(S,4)=\{0,w_1,w_2,w_3\},\quad
w_1=4a+1,\ w_2=4b+2,\ w_3=4c+3.
\]

The positive integers \((a,b,c)\) determine a semigroup precisely when

\[
b\le2a,\qquad c\le a+b,\qquad a\le b+c+1,\qquad b\le2c+1.
\]

Its genus is \(a+b+c\) and \(F=\max(w_1,w_2,w_3)-4\). For genus at least \(4\), generator \(4\) is not above \(F\). The statements count children in the full tree, not just children remaining in the fixed-multiplicity subtree.

## Proof

**1. Testing effective Apéry generators.** Every minimal generator other than \(4\) belongs to the Apéry set. From the four Kunz inequalities and the only residue-compatible decompositions, the three Apéry elements are minimal exactly when, respectively,

\[
M_1:\ a\le b+c,\qquad M_2:\ b<2a\text{ and }b\le2c,\qquad M_3:\ c<a+b.
\]

For a maximal Apéry value \(W=\max(w_1,w_2,w_3)\), an Apéry generator is effective exactly when it is minimal and its value exceeds \(W-4\). Therefore any pair \(i,j\) is simultaneously effective precisely when \(M_i,M_j\) hold, \(|w_i-w_j|\le3\), and the third Apéry value is at most \(\min(w_i,w_j)+3\). This last condition is necessary because both selected values must exceed \(W-4\), and it is sufficient by the same inequality.

**2. Six disjoint-within-pair parameter families.** Write \(P_{ij}\) for the set of semigroups for which both \(w_i\) and \(w_j\) are effective. Substituting the three explicit weight expressions into the conditions just proved gives exactly the following six families, where \(t\) is any positive integer and every displayed interval contains all its integer points:

\[
\begin{array}{c|l}
P_{12}& (t,t,c),\quad \lceil t/2\rceil\le c\le t\\
& (t+1,t,c),\quad \lceil t/2\rceil\le c\le t\\[2pt]
P_{13}& (t,b,t),\quad 1\le b\le t\\
& (t+1,b,t),\quad 1\le b\le t+1\\[2pt]
P_{23}& (a,t,t),\quad \lfloor t/2\rfloor+1\le a\le t+1\\
& (a,t+1,t),\quad \lceil(t+2)/2\rceil\le a\le t+1.
\end{array}
\]

To see completeness directly, the residue difference between two selected Apéry elements is \(-1\), \(-2\), or \(-1\) modulo \(4\), respectively; requiring its absolute value at most \(3\) forces the displayed two consecutive choices of equal or adjacent Kunz coordinates. The upper bound on the third value and the minimality conditions then give exactly the displayed intervals. Conversely each interval satisfies all four Kunz inequalities and both effectiveness tests. This is an exact classification, not a finite-search inference.

**3. Counting pairs by genus.** Let \(P_{ij}(z)=\sum_{S\in P_{ij}}z^{g(S)}\). Summing the intervals in step 2, splitting \(t\) into odd and even cases as necessary, gives

\[
P_{12}(z)=\frac{1+z}{1-z}\left(\frac{z^3+z^5}{1-z^5}-\frac{z^4+z^7}{1-z^6}\right),
\]
\[
P_{13}(z)=\frac1{1-z}\left(\frac{z^3+z^4}{1-z^2}-\frac{z^4+z^6}{1-z^3}\right),
\]
\[
P_{23}(z)=\frac1{1-z}\left(\frac{z^3+z^5+z^6+z^7}{1-z^5}-\frac{z^5+z^6+z^8+z^9}{1-z^6}\right).
\]

All series are formal power series in \(z\). Multiplication by the displayed denominators, followed by elementary polynomial cancellation, gives the exact rational identity

\[
P_{12}(z)+P_{13}(z)+P_{23}(z)-\frac{3z^3}{1-z}
=\frac{z^5(1+z+z^3)}{(1-z)(1-z^5)}.
\]

**4. Triple intersections and correction.** All three Apéry elements are effective exactly for the three triples

\[
(t,t,t),\qquad(t+1,t,t),\qquad(t+1,t+1,t),\qquad t\ge1.
\]

Indeed, if all three exceed \(W-4\), their largest and smallest values differ by at most \(3\); applying the distinct residues to the three values yields exactly these configurations. Every listed triple satisfies the minimality tests. Their genera are \(3t\), \(3t+1\), and \(3t+2\), respectively, so there is exactly one such triple in each genus \(g\ge3\). A semigroup with exactly two effective Apéry generators belongs to exactly one pair family, whereas one with all three belongs to all three. Therefore subtracting three copies of \(\sum_{g\ge3}z^g=z^3/(1-z)\) from the sum of the pair generating functions counts exactly two-child semigroups. By step 3 this is the asserted \(e_2\) rational generating function.

Finally, at genus \(3\) the unique triple is \((1,1,1)\), with Frobenius number \(3\), so its generator \(4\) is additionally effective and it has four children. For every \(g\ge4\), \(F\ge4\), so the triple has precisely three children. No others have three or four, since at most three Apéry generators and generator \(4\) can be effective. Expanding \(1/((1-z)(1-z^5))\) proves the coefficient formula and its \(3g/5+O(1)\) asymptotic.

## Verification

Run `python3 verify.py` from this directory using Python's standard library. The checker constructs all multiplicity-four semigroups through genus \(90\) from Kunz inequalities, computes minimal generators independently by genuine additive decompositions using Apéry-based membership, counts generators strictly above the Frobenius number, and verifies every degree count against the six pair families and the closed coefficient formula. It checks the unique three-child class, exceptional four-child class, and disjointness of family descriptions within each pair. The finite checks corroborate but do not substitute for the infinite proof.

## Relationship to prior work

Casas, Madrid and Rosales (2026), *Internal numerical semigroups*, distinguish internal semigroups and leaves, give generation algorithms, and tabulate their counts at fixed genus and multiplicity. The present theorem further separates the internal stratum according to exact branching degree, proving uniform formulas for two and three children at fixed multiplicity four.

García-Sánchez, Marín-Aragón and Robles-Pérez (2018), *The tree of numerical semigroups with low multiplicity*, classify branching at multiplicity three and count **all** multiplicity-four semigroups by genus (Section 3); their multiplicity-four section does not give this two-child rational function or the three-child uniqueness theorem. A previously available four-family classification of multiplicity-four *leaves* concerns the zero-child stratum and does not determine the split of internal semigroups into one-, two-, and three-child strata. O'Dorney (2024) gives global asymptotic offspring-degree proportions as genus grows with no restriction on multiplicity, not this fixed-multiplicity exact finite-genus profile.

## Limitations

The theorem counts children in the full tree and concerns multiplicity exactly \(4\); it does not assert the same rational formulas for other multiplicities or for the fixed-multiplicity subtree. Its numerical tests only cover bounded genera; all-genus validity depends on the displayed combinatorial proof. No assertion of absolute bibliographic priority is made: an equivalent formula in unindexed work or expressed through an older child-degree enumerator remains a possible originality risk. Independent validation has not been performed.

## References

1. M. Casas, J. A. Madrid, J. C. Rosales, *Internal numerical semigroups*, arXiv:2608.19984v1 (first public 2026-08-20), https://arxiv.org/html/2608.19984v1.
2. P. A. García-Sánchez, D. Marín-Aragón, A. M. Robles-Pérez, *The tree of numerical semigroups with low multiplicity*, arXiv:1803.06879v1 (2018), https://arxiv.org/html/1803.06879v1.
3. E. O'Dorney, *Degree asymptotics of the numerical semigroup tree*, arXiv:2403.13120 (2024), https://arxiv.org/abs/2403.13120.
4. M. Bras-Amorós, *Bounds on the number of numerical semigroups of a given genus*, J. Pure Appl. Algebra 213 (2009), 997–1001 (background on the tree and genus).
