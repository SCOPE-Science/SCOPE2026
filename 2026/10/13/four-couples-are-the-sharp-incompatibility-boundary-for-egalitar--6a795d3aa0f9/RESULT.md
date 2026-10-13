# Four couples are the sharp incompatibility boundary for egalitarian versus minimum-regret Stable Marriage
## Finding
Consider the complete strict Stable Marriage problem with \(n\) men and \(n\) women. Every participant strictly ranks all participants on the opposite side.

For a stable matching \(M\), let \(r_x(M)\) be the one-based rank that participant \(x\) assigns to its partner. Define
\[
e(M)=\sum_x r_x(M)
\]
and
\[
g(M)=\max_x r_x(M).
\]
Let \(E(I)\) be the stable matchings minimizing \(e\), and let \(G(I)\) be those minimizing \(g\).

Every instance with at most \(3\) couples satisfies
\[
E(I)\cap G(I)\ne\varnothing.
\]

This is sharp. There is a complete strict \(4\)-couple instance for which
\[
E(I)\cap G(I)=\varnothing.
\]

For \(3\) labeled men and \(3\) labeled women there are
\[
(3!)^6=6^6=46656
\]
complete strict preference profiles. Their exact optimum-set relation is
\[
\begin{array}{c|r}
\text{relation}&\text{profiles}\\ \hline
E=G&40056\\
E\subsetneq G&5400\\
G\subsetneq E&1200
\end{array}
\]
with no disjoint or nonnested-overlap cases.

Thus exactly
\[
6600
\]
three-couple profiles make the criteria select different sets, an incidence of
\[
\frac{6600}{46656}=\frac{275}{1944},
\]
but all \(6600\) still have at least one stable matching optimal for both criteria.

A sharp \(4\)-couple witness is:

\[
\begin{aligned}
A&:a\succ b\succ c\succ d,\\
B&:b\succ d\succ c\succ a,\\
C&:b\succ a\succ d\succ c,\\
D&:c\succ d\succ a\succ b,
\end{aligned}
\]
and
\[
\begin{aligned}
a&:B\succ D\succ C\succ A,\\
b&:A\succ B\succ D\succ C,\\
c&:C\succ D\succ A\succ B,\\
d&:C\succ D\succ B\succ A.
\end{aligned}
\]

It has exactly two stable matchings:
\[
M_E=\{Ab,Ba,Cd,Dc\},
\]
whose eight partner ranks are
\[
(2,4,3,1,1,1,2,1),
\]
so
\[
e(M_E)=15,\qquad g(M_E)=4,
\]
and
\[
M_G=\{Ab,Bd,Ca,Dc\},
\]
whose eight partner ranks are
\[
(2,2,2,1,3,1,2,3),
\]
so
\[
e(M_G)=16,\qquad g(M_G)=3.
\]

Therefore
\[
E(I)=\{M_E\},
\qquad
G(I)=\{M_G\},
\]
and the two canonical fairness objectives force different stable choices.

## Assumptions and scope
Preferences are complete and strict, and the two sides have equal size.

A pair consisting of one man and one woman blocks a matching when both strictly prefer one another to their assigned partners.

The egalitarian criterion minimizes total partner rank over all participants. The minimum-regret criterion minimizes the worst partner rank over all participants.

The lower bound is exhaustive through \(3\) couples. The \(4\)-couple statement is an explicit sharp witness, not a census of all \(4\)-couple instances.

## Proof
For \(n=1\), there is one profile and one stable matching.

For \(n=2\), every one of the
\[
(2!)^4=16
\]
profiles is enumerated. In all \(16\), the egalitarian and minimum-regret optimum sets coincide.

For \(n=3\), every one of the
\[
(3!)^6=46656
\]
profiles is enumerated. Every one of the \(3!=6\) perfect matchings is tested for stability.

The stable-matching count distribution is
\[
34080
\]
profiles with one stable matching,
\[
11484
\]
with two, and
\[
1092
\]
with three.

For each stable matching, the total rank and maximum rank are computed. The exact optimum-set relation census is
\[
40056,\ 5400,\ 1200
\]
for \(E=G\), \(E\subsetneq G\), and \(G\subsetneq E\), respectively. There are no disjoint or nonnested-overlap cases. Hence the two criteria always share an optimizer through \(3\) couples.

For the displayed \(4\)-couple instance, all
\[
4!=24
\]
perfect matchings are tested. Exactly \(M_E\) and \(M_G\) are stable. Their rank vectors and objective pairs are exactly those displayed above, so the egalitarian and minimum-regret optimum sets are disjoint.

## Verification
The embedded `verify_sm_egal_minregret_boundary.py` uses only the Python standard library.

It independently checks stability in two ways:
1. by precomputed rank maps;
2. by direct traversal of the original preference lists.

It independently computes the two objective values:
1. from rank maps;
2. from direct preference-list positions.

The verifier reproduces:
- all complete strict profiles for \(n=1,2,3\);
- the exact stable-matching count distribution for \(n=3\);
- the exact \(40056/5400/1200\) optimum-set relation census;
- the absence of disjoint optimum sets through \(3\) couples;
- all \(24\) perfect matchings of the displayed \(4\)-couple witness;
- exactly two stable witness matchings;
- exact objective pairs \((15,4)\) and \((16,3)\).

Run:

`python3 verify_sm_egal_minregret_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Egalitarian and minimum-regret stable marriages are standard optimality concepts.

De Clercq, Schockaert, De Cock, and Nowé define the egalitarian cost as the sum of participant costs and the regret cost as the maximum participant cost, and they treat both as commonly studied criteria. Their paper also records polynomial-time solvability of the classical complete strict problems.

The contribution here is not the criteria or their algorithms. It is the sharp small-market compatibility boundary and exact preceding census: every complete strict instance through \(3\) couples has a common optimizer; the entire three-couple relation is \(40056\) equal cases, \(5400\) cases with \(E\subsetneq G\), and \(1200\) cases with \(G\subsetneq E\); and a \(4\)-couple witness makes the optimum sets disjoint.

Targeted searches by the two criterion names, exact profile count, exact relation counts, and disjoint-optimum language did not locate an equivalent finite classification.

## Limitations
The theorem is restricted to complete strict preferences.

The \(4\)-couple contribution is a witness, not a complete census.

No claim is made about incomplete lists, ties, unequal market sizes, or the prevalence of incompatibility beyond the sharp first witness size.

An unindexed historical table, thesis appendix, or software test corpus could contain the same finite classification.

## References
1. S. De Clercq, S. Schockaert, M. De Cock, and A. Nowé, “Solving stable matching problems using answer set programming,” arXiv:1512.05247, first submitted 16 December 2015.
2. D. Gusfield, “Three fast algorithms for four problems in stable marriage,” *SIAM Journal on Computing* 16 (1987), 111–128.
3. R. W. Irving, P. Leather, and D. Gusfield, “An efficient algorithm for the optimal stable marriage,” *Journal of the ACM* 34 (1987), 532–543.
