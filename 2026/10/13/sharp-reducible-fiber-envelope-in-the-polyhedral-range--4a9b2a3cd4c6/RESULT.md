# Sharp reducible-fiber envelope in the polyhedral range
## Finding
Let
\[
\pi:X\longrightarrow\mathbf P^1
\]
be a semistable Jacobian elliptic surface over \(\mathbf C\) with
\[
\chi=\chi(\mathcal O_X)\ge3,
\]
finite Mordell--Weil group, and at least one reducible fiber. Write the reducible fibers as
\[
I_{n_1},\ldots,I_{n_s},\qquad n_i\ge2,
\]
and use the two quantities appearing in Laface--Li:
\[
\delta(\pi)=\sum_{i=1}^s\frac{\lfloor n_i^2/4\rfloor}{n_i},
\qquad
N(\pi)=\sum_{i=1}^s n_i.
\]

If
\[
\delta(\pi)\le\chi,
\]
then
\[
\boxed{
N(\pi)\le\left\lfloor\frac{9\chi}{2}\right\rfloor.
}
\]

The equality cases are rigid.

If \(\chi\) is even and
\[
N(\pi)=\frac{9\chi}{2},
\]
then every reducible fiber is \(I_3\), and there are exactly
\[
\frac{3\chi}{2}
\]
such fibers.

If \(\chi\) is odd and
\[
N(\pi)=\frac{9\chi-1}{2},
\]
then the reducible-fiber multiset is necessarily one of
\[
I_4+\frac{3(\chi-1)}{2}I_3
\]
or
\[
2I_2+\frac{3(\chi-1)}{2}I_3.
\]
This is a classification of the equality patterns forced by the numerical condition \(\delta(\pi)\le\chi\); it does not assert that both patterns are geometrically realized for every \(\chi\).

For \(\chi=3\), Laface--Li construct a surface with singular-fiber configuration
\[
I_4+3I_3+23I_1.
\]
Its reducible fibers have
\[
N(\pi)=4+3\cdot3=13
=
\left\lfloor\frac{27}{2}\right\rfloor,
\]
so their counterexample sits on the absolute numerical boundary of the polyhedral range.

## Assumptions and scope
The setup is exactly the semistable Jacobian elliptic-surface setting of Laface--Li: the base is \(\mathbf P^1\), the surface is over \(\mathbf C\), \(\chi(\mathcal O_X)\ge3\), the Mordell--Weil group is finite, and the reducible fibers are multiplicative fibers \(I_{n_i}\).

The inequality uses only the numerical polyhedrality condition
\[
\delta(\pi)\le\chi
\]
and the definition of \(N(\pi)\). Irreducible \(I_1\)-fibers do not enter \(N(\pi)\) or \(\delta(\pi)\).

The equality classification gives necessary reducible-fiber multisets for an actual surface attaining the bound. It does not prove the existence of an elliptic surface realizing each listed multiset for every value of \(\chi\).

## Proof
For an integer \(n\ge2\), define
\[
d(n)=\frac{\lfloor n^2/4\rfloor}{n}.
\]
We first prove the sharp termwise inequality
\[
d(n)\ge\frac{2n}{9},
\]
with equality if and only if \(n=3\).

If \(n\) is even, then
\[
d(n)=\frac n4,
\]
so
\[
d(n)-\frac{2n}{9}
=
\frac n{36}>0.
\]

If \(n\) is odd, then
\[
d(n)=\frac{n^2-1}{4n},
\]
and therefore
\[
d(n)-\frac{2n}{9}
=
\frac{n^2-9}{36n}.
\]
For odd \(n\ge3\), this is nonnegative and vanishes exactly at \(n=3\).

Summing over the reducible fibers gives
\[
\delta(\pi)
=
\sum_i d(n_i)
\ge
\frac29\sum_i n_i
=
\frac{2N(\pi)}9.
\]
Hence
\[
N(\pi)\le\frac{9\chi}{2},
\]
and integrality gives
\[
N(\pi)\le\left\lfloor\frac{9\chi}{2}\right\rfloor.
\]

Now suppose equality holds.

If \(\chi\) is even, then
\[
N(\pi)=\frac{9\chi}{2}.
\]
The inequalities
\[
\chi\ge\delta(\pi)\ge\frac{2N(\pi)}9=\chi
\]
are both equalities. Thus every term satisfies
\[
d(n_i)=\frac{2n_i}{9},
\]
which forces \(n_i=3\) for every \(i\). Their number is
\[
\frac{N(\pi)}3=\frac{3\chi}{2}.
\]

Assume next that \(\chi\) is odd. Put
\[
e(n)=d(n)-\frac{2n}{9}.
\]
At the integer maximum
\[
N(\pi)=\frac{9\chi-1}{2},
\]
we have
\[
\sum_i e(n_i)
=
\delta(\pi)-\frac{2N(\pi)}9
\le
\chi-\left(\chi-\frac19\right)
=
\frac19.
\]

The possible positive defects are strongly restricted. For even \(n\),
\[
e(n)=\frac n{36},
\]
so the defect budget allows only \(n=2\) or \(n=4\), with
\[
e(2)=\frac1{18},
\qquad
e(4)=\frac19.
\]
For odd \(n\),
\[
e(n)=\frac{n^2-9}{36n}.
\]
Besides \(n=3\), which has zero defect, the only odd value with defect at most \(1/9\) is \(n=5\), with
\[
e(5)=\frac4{45}.
\]
Every \(n\ge6\) has defect exceeding \(1/9\), except for none of the already listed cases.

Because
\[
N(\pi)=\frac{9\chi-1}{2}\equiv1\pmod3,
\]
the total contribution of the non-\(3\) fiber sizes must be congruent to \(1\) modulo \(3\). Under the defect budget \(1/9\), the only possibilities are
\[
4
\]
or
\[
2+2.
\]
Indeed, a single \(5\) has residue \(2\) modulo \(3\); pairing it with any allowed non-\(3\) term exceeds the defect budget. A single \(2\) also has residue \(2\), and it can only be paired with one further \(2\) within the budget. The value \(4\) by itself already uses the full budget.

Thus the non-\(3\) part is either one \(I_4\) or two \(I_2\)'s. In both cases the remaining total is
\[
\frac{9\chi-1}{2}-4
=
\frac{9(\chi-1)}2,
\]
so the number of \(I_3\)-fibers is
\[
\frac{3(\chi-1)}2.
\]
This proves the equality classification.

## Verification
The initiating source defines exactly
\[
\delta(\pi)=\sum_i\frac{\lfloor n_i^2/4\rfloor}{n_i}
\qquad\text{and}\qquad
N(\pi)=\sum_i n_i,
\]
and states that \(\delta(\pi)\le\chi\) is the range in which the visible fiber curves generate a rational polyhedral Mori cone. Its abstract also records the \(\chi=3\) counterexample with configuration
\[
I_4+3I_3+23I_1.
\]

The termwise inequality was checked separately in its two parity cases. The equality classification uses the exact defect
\[
e(n)=d(n)-\frac{2n}{9}.
\]
The only positive defects at most \(1/9\) are
\[
e(2)=\frac1{18},
\qquad
e(4)=\frac19,
\qquad
e(5)=\frac4{45},
\]
while \(e(3)=0\). The congruence of the target total modulo \(3\) then leaves only the two stated odd-\(\chi\) patterns.

As a finite sanity check, exact rational enumeration for \(3\le\chi\le8\) reproduces the predicted maxima and equality patterns. This enumeration is not used as a proof; the proof above covers every integer \(\chi\ge3\) and every finite list \(n_i\ge2\).

For \(\chi=3\), the source's reducible configuration \(I_4+3I_3\) has
\[
\delta(\pi)=1+3\cdot\frac23=3
\]
and
\[
N(\pi)=4+9=13,
\]
so it attains the bound.

## Relationship to prior work
Laface--Li use \(\delta(\pi)\) to characterize the polyhedral Mori-cone range and \(N(\pi)\) to formulate semiampleness and Mori-dream criteria. Their paper emphasizes thresholds such as \(N(\pi)\le2\chi+4\) under additional parity hypotheses and constructs an odd-fiber counterexample at \(\chi=3\).

The present finding compares the two numerical parameters directly. It shows that the polyhedrality inequality itself imposes a universal ceiling on the total reducible multiplicity and completely determines the fiber-size patterns at that ceiling.

The preceding Laface--Li--Liu paper studies Mori-dream Jacobian elliptic surfaces and, in its initial one-reducible-fiber formulation, gives the polyhedral threshold \(n\le4\chi\) and Mori-dream threshold \(n\le2\chi+3\). It does not give the multi-fiber optimization
\[
N(\pi)\le\left\lfloor\frac{9\chi}{2}\right\rfloor
\]
or the equality classification above.

Targeted searches for the exact \(9\chi/2\) envelope, for optimization of \(N(\pi)\) under the \(\delta(\pi)\)-constraint, and for the equality patterns involving \(I_3\), \(I_4\), and \(I_2\) did not locate an implication-equivalent published statement.

## Limitations
The upper bound is sharp for the numerical constraint \(\delta(\pi)\le\chi\). Geometric realizability of every equality pattern for every \(\chi\) is not claimed.

The \(\chi=3\) first pattern is geometrically realized by Laface--Li's explicit counterexample, which proves that the bound is genuinely sharp in that case.

The finding does not decide which extremal configurations are Mori dream surfaces. It controls the size and shape of reducible fibers inside the polyhedral range, not semiampleness of all nef classes.

The current initiating preprint's full PDF was not available through the accessible public full-text route during this review. Its primary abstract, bibliographic record, a detailed full-paper secondary review, and the predecessor's publicly readable full text were inspected. This leaves a residual originality risk that an equivalent elementary optimization appears in an unindexed portion of the current preprint.

## References
A. Laface and S. Li, “Semiampleness on Jacobian elliptic surfaces of Kodaira dimension one,” arXiv:2609.23306v1, first public 2026-09-20; primary MSC \(14C20\).

A. Laface, S. Li, and J. Liu, “Mori dream Jacobian elliptic surfaces of Kodaira dimension one,” arXiv:2608.09002v1, first public 2026-08-10.
