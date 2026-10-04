# Sharp first upper-quota failures of Jefferson apportionment
## Finding
Consider pure Jefferson apportionment, equivalently the D'Hondt highest-averages rule, with \(s\) entities having positive shares
\[
p_1+\cdots+p_s=1,
\]
a house of \(h\) seats, no statutory minimum allocation, and a unique cutoff among the Jefferson quotients
\[
p_i,\ \frac{p_i}{2},\ \frac{p_i}{3},\ldots.
\]
The upper quota of entity \(i\) is
\[
\left\lceil hp_i\right\rceil .
\]

Among all parameter pairs \((s,h)\), ordered coordinatewise, the minimal cells that permit an upper-quota violation are exactly
\[
(s,h)=(3,3)\quad\text{and}\quad(s,h)=(4,2).
\]

For three entities and three seats, relabel the violating entity as \(A\). The entire violation chamber is
\[
\frac35<p_A\le\frac23,\qquad
p_B<\frac{p_A}{3},\qquad
p_C<\frac{p_A}{3}.
\]
Every profile in this chamber gives all three seats to \(A\), although \(A\)'s upper quota is at most two. Conversely, every tie-independent upper-quota violation in this cell lies in this chamber.

Under normalized Lebesgue measure on the two-dimensional share simplex, equivalently a Dirichlet distribution with all parameters equal to one, the probability of a violation is exactly
\[
\frac1{45}.
\]
Among positive integer populations, the least possible total is six, with unique witness up to permutation
\[
(4,1,1).
\]

For four entities and two seats, the complete chamber is
\[
\frac25<p_A\le\frac12,\qquad
p_j<\frac{p_A}{2}\quad(j\ne A).
\]
Every profile there gives both seats to \(A\), whose upper quota is one. Its normalized simplex probability is exactly
\[
\frac1{40}.
\]
The least-total positive-integer witness is uniquely
\[
(3,1,1,1)
\]
up to permutation, again with total six.

## Assumptions and scope
The result concerns the pure apportionment problem: every share is strictly positive, allocations may be zero, and there is no imposed one-seat minimum. Jefferson is implemented by selecting the \(h\) largest quotients \(p_i/k\) for positive integers \(k\). The cutoff is required to be strict, so no tie-breaking convention is part of the theorem.

A parameter cell \((s,h)\) is called coordinatewise minimal for upper-quota failure if some profile in that cell violates upper quota but no cell \((s',h')\) with \(s'\le s\), \(h'\le h\), and at least one strict inequality admits a violation.

The probabilities use normalized Lebesgue measure on the open share simplex. Boundary hyperplanes have measure zero, so strict versus weak inequalities on those boundaries do not affect the probability statements.

## Proof
First exclude all cells below the claimed boundary.

For two entities, suppose \(A\) receives \(a\) of \(h\) seats and the other entity receives \(h-a\). If \(a>0\), strict Jefferson selection implies that \(A\)'s \(a\)-th selected quotient exceeds the other entity's next unselected quotient:
\[
\frac{p_A}{a}>
\frac{1-p_A}{h-a+1}.
\]
Therefore
\[
a<p_A(h+1)=hp_A+p_A<hp_A+1.
\]
Since \(a\) is integral,
\[
a\le\left\lceil hp_A\right\rceil .
\]
The case \(a=0\) is immediate, and the same argument applies to the other entity. Hence two-entity Jefferson never violates upper quota.

For \(h=1\), every positive share has upper quota one, so upper quota cannot fail.

Now take \(s=3\) and \(h=2\). A violation would require one entity \(A\) to receive both seats while \(p_A\le1/2\). Receiving both seats uniquely requires
\[
\frac{p_A}{2}>\max(p_B,p_C)\ge\frac{1-p_A}{2},
\]
which forces \(p_A>1/2\), a contradiction.

It follows that any coordinatewise-minimal violating cell must be either \((3,h)\) with \(h\ge3\), \((s,2)\) with \(s\ge4\), or larger in both coordinates. It therefore suffices to classify \((3,3)\) and \((4,2)\).

For \(s=3,h=3\), an entity receiving two seats cannot violate upper quota. Indeed, if \(A\) receives two seats, it must be the largest entity: if \(p_B>p_A\), then the three quotients
\[
p_B,\quad \frac{p_B}{2},\quad p_A
\]
all exceed \(p_A/2\), so \(A\)'s second quotient is not among the top three. Thus \(p_A>1/3\), giving upper quota at least two. Consequently a violation requires one entity \(A\) to receive all three seats. This happens exactly when
\[
\frac{p_A}{3}>\max(p_B,p_C).
\]
Upper quota is then violated exactly when
\[
3p_A\le2.
\]
Because
\[
\max(p_B,p_C)\ge\frac{1-p_A}{2},
\]
strict selection also forces \(p_A>3/5\). This proves the stated three-entity chamber.

For \(s=4,h=2\), a violation can only occur when one entity \(A\) receives both seats. This is equivalent to
\[
\frac{p_A}{2}>\max_{j\ne A}p_j.
\]
The upper quota is one exactly when \(2p_A\le1\). Since
\[
\max_{j\ne A}p_j\ge\frac{1-p_A}{3},
\]
strict selection implies \(p_A>2/5\). This proves the four-entity chamber.

These two chambers are nonempty, so \((3,3)\) and \((4,2)\) admit violations. Every other violating cell dominates one of them coordinatewise, proving the minimal-cell statement.

For the three-entity probability, fix the violating label \(A\) and put \(x=p_A\). For
\[
\frac35<x<\frac23,
\]
the admissible interval for \(p_B\), with \(p_C=1-x-p_B\), has length
\[
\frac{5x}{3}-1.
\]
The uniform simplex density in these coordinates is two. Thus the probability for one fixed violating label is
\[
2\int_{3/5}^{2/3}\left(\frac{5x}{3}-1\right)\,dx
=\frac1{135}.
\]
The three possible labels give disjoint chambers, hence total probability \(3/135=1/45\).

For the four-entity probability, fix \(A\) and put \(x=p_A\). Conditional on \(x\), normalize the other three shares by \(1-x\). The cap is
\[
t=\frac{x}{2(1-x)},
\]
which lies between \(1/3\) and \(1/2\). For a uniform point on the two-simplex, inclusion-exclusion gives
\[
\Pr(\max Y_j<t)=1-3(1-t)^2+3(1-2t)^2=(3t-1)^2.
\]
The marginal density of \(x\) is \(3(1-x)^2\), so the fixed-label probability is
\[
\int_{2/5}^{1/2}\frac34(5x-2)^2\,dx=\frac1{160}.
\]
Multiplying by four labels gives \(1/40\).

Finally, positive integer witnesses follow directly from the strict quotient inequalities. At \((3,3)\), if the two minor populations are at least one, then the dominant population must exceed three times each, so the least total is six and the unique sorted witness is \((4,1,1)\). At \((4,2)\), it must exceed twice each of three positive minors, giving the unique least-total sorted witness \((3,1,1,1)\).

## Verification
The embedded `verify_jefferson_quota_boundary.py` uses exact rational arithmetic and implements Jefferson in two equivalent ways: direct highest-averages selection and a divisor-interval replay.

The program checks two-entity upper quota over positive integer populations through total \(30\) and house sizes through \(10\), checks the three-entity/two-seat safe cell through total \(30\), and exhaustively compares the analytic chamber descriptions against all positive integer profiles through total \(30\) in the two boundary cells. It also verifies the least-total integer witnesses and evaluates the two simplex integrals as exact fractions.

These finite checks are consistency tests for the analytic proof; they are not used to infer the continuum theorem.

Replay with:

`python3 verify_jefferson_quota_boundary.py`

The first line must be `VERIFY_OK`.

## Relationship to prior work
Balinski and Young formalized exact quota, lower quota, and upper quota in their 1975 treatment of apportionment. Their Theorem 2 shows, among the five classical workable Huntington methods, that the method of smallest divisors satisfies upper quota while Jefferson satisfies lower quota; the surrounding discussion emphasizes that standard divisor methods can fail the opposite quota bound.

Their work on the Jefferson method characterizes it through consistency, house monotonicity, and lower quota, and gives the standard divisor/highest-averages formulation. Thus neither Jefferson's general tendency to favor large entities nor the possibility of upper-quota failure is claimed as new here.

The new statement is the sharp first-failure geometry: the two coordinatewise-minimal \((s,h)\) cells, their complete tie-independent violation chambers, their exact uniform-simplex probabilities, and their unique least-total positive-integer witnesses. Targeted searches by the Jefferson and D'Hondt names, upper-quota terminology, the two boundary cells, the exact witness vectors, and the probabilities \(1/45\) and \(1/40\) found no equivalent published classification.

## Limitations
The theorem does not include statutory minimum-seat requirements, zero-share entities, or tie-breaking at quotient cutoffs. Such variants can change the smallest examples.

The probability calculation uses the uniform distribution on the share simplex; it is not a claim about empirical party-vote or population distributions.

The exact boundary classification was not found in the inspected literature, but an unindexed historical note, textbook exercise, or unpublished computation could contain an equivalent statement.

## References
1. M. L. Balinski and H. P. Young, “A New Method for Congressional Apportionment,” *Proceedings of the National Academy of Sciences USA* 71 (1974), 4602–4606. DOI: 10.1073/pnas.71.11.4602.
2. M. L. Balinski and H. P. Young, “The Quota Method of Apportionment,” *American Mathematical Monthly* 82 (1975), 701–730. DOI: 10.1080/00029890.1975.11993911.
3. M. L. Balinski and H. P. Young, “The Jefferson Method of Apportionment,” IIASA Professional Paper PP-76-006, August 1976; later *SIAM Review* 20 (1978), 278–284. DOI: 10.1137/1020040.
