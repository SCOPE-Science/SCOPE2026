# Minimal jump support for failure of the two-trial compound-binomial log-concavity criterion
## Finding
Let \(0<p<1\), put \(q=1-p\), and let
\[
f=(f_0,f_1,f_2,0,\ldots)
\]
be a probability mass function on \(\mathbb N\) with \(f_1>0\). Let \(M\sim\operatorname{Bin}(2,p)\), let \(X_1,X_2,\ldots\) be iid with pmf \(f\), independent of \(M\), and define
\[
S=\sum_{i=1}^M X_i.
\]
If \(g\) is the pmf of \(S\), then
\[
g\in\mathrm{LC}
\quad\Longleftrightarrow\quad
3\delta f_1^2\ge 2f_2,
\qquad
\delta=\frac{p}{pf_0+q}.
\]
Thus the first log-concavity inequality identified by Xia and Lv is not merely necessary in this three-point-jump regime: it is sufficient as well. No log-concavity assumption on \(f\) is needed for this equivalence.

Xia and Lv give a two-trial example with jumps supported on \(\{0,1,2,3\}\) for which
\[
3\delta f_1^2=2f_2
\]
but the compound law is not log-concave. Combining their counterexample with the theorem above shows that, for \(M\sim\operatorname{Bin}(2,p)\), maximum jump size \(3\) is the smallest at which their criterion can fail to be sufficient.

## Assumptions and scope
The claim is restricted to a binomial claim count with exactly two trials and a nonnegative integer-valued jump distribution supported on \(\{0,1,2\}\), with \(f_1>0\). The parameter \(p\) lies in \((0,1)\). Log-concavity means that a nonnegative sequence \(a\) with interval support satisfies
\[
a_k^2\ge a_{k-1}a_{k+1}
\]
at every interior index.

The result does not assert sufficiency for arbitrary jump support or for \(\operatorname{Bin}(n,p)\) with \(n\ge3\).

## Proof
Let
\[
A=q+pf_0,\qquad B=pf_1,\qquad C=pf_2.
\]
A one-trial compound binomial variable has pmf
\[
h=(A,B,C).
\]
Because \(\operatorname{Bin}(2,p)\) is the sum of two independent \(\operatorname{Bern}(p)\) variables, the two-trial compound law is the convolution \(g=h*h\). Therefore
\[
(g_0,g_1,g_2,g_3,g_4)
=
\left(
A^2,\,
2AB,\,
B^2+2AC,\,
2BC,\,
C^2
\right).
\]

There are only three log-concavity inequalities. The first gives
\[
g_1^2-g_0g_2
=
A^2\left(3B^2-2AC\right).
\]
The middle one is automatic, because
\[
g_2^2-g_1g_3
=
B^4+4A^2C^2>0.
\]
The last gives
\[
g_3^2-g_2g_4
=
C^2\left(3B^2-2AC\right).
\]
Hence \(g\) is log-concave if and only if
\[
3B^2\ge2AC.
\]
Since \(A=pf_0+q\), \(B=pf_1\), \(C=pf_2\), and
\[
\delta=\frac{p}A,
\]
the last inequality is equivalent, after division by the positive factor \(Ap\), to
\[
3\delta f_1^2\ge2f_2.
\]
This proves the equivalence.

For minimality of the jump-support cutoff, Xia and Lv use
\[
p=\frac{20}{23},\qquad
f=\left(\frac1{20},\frac15,\frac3{10},\frac9{20},0,\ldots\right).
\]
They compute \(\delta=5\) and
\[
3\delta f_1^2=2f_2,
\]
yet the convolution square violates log-concavity at a later index. Since the theorem rules out every failure when the maximum jump is at most \(2\), their maximum-jump-\(3\) example is support-minimal in this sense.

## Verification
The proof is exact algebra and covers every admissible real parameter choice. The bundled script `verify_three_point_compound_binomial.py` independently reconstructs the convolution with exact rational arithmetic, checks the three factorized log-concavity defects on thousands of rational parameter triples, and exactly replays the published maximum-jump-\(3\) counterexample. A successful replay prints an output beginning with `VERIFY_OK`.

The finite replay is a regression check only. The all-parameter theorem follows from the displayed symbolic identities.

## Relationship to prior work
Xia and Lv derive the necessary condition
\[
(n+1)\delta f_1^2\ge2f_2
\]
for log-concavity of a compound \(\operatorname{Bin}(n,p)\) law when the jump pmf is log-concave. They prove sufficiency for \(n=1\), then show that the condition is not sufficient in general for \(n\ge2\) using the explicit \(n=2\), maximum-jump-\(3\) counterexample quoted above. Their paper does not state a support-minimality result or a complete \(n=2\) classification for jumps supported on \(\{0,1,2\}\).

Earlier work by Yu develops entropy and relative-log-concavity methods for compound distributions, while Johnson, Kontoyiannis and Madiman study compound Poisson log-concavity. Those broader frameworks motivate the subject but do not supply the finite convolution-square classification proved here.

Targeted searches for two-trial compound binomial log-concavity, three-point jump distributions, convolution squares of three-point laws, the inequality \(3B^2\ge2AC\), and minimal jump support did not locate the stated equivalence or support-minimality conclusion.

## Limitations
The theorem exploits that a three-point one-trial compound law has a five-point convolution square, whose middle log-concavity defect factors as a sum of two positive terms. With jumps of size \(3\), additional interior inequalities appear and the Xia--Lv counterexample shows that the first-curvature condition no longer controls them.

The originality search is targeted rather than exhaustive. An older result on convolution squares of three-point sequences could contain an equivalent algebraic criterion under different terminology.

## References
1. W. Xia and W. Lv, “Log-concavity and relative log-concave ordering of compound distributions,” *Probability in the Engineering and Informational Sciences* 38 (2024), 579–593, DOI 10.1017/S0269964823000293. First publicly verified online date: 2024-01-29. Proposition 4.6 contains the necessary condition and the maximum-jump-\(3\) counterexample.
2. Y. Yu, “On the entropy of compound distributions on nonnegative integers,” *IEEE Transactions on Information Theory* 55 (2009), 3645–3650, DOI 10.1109/TIT.2009.2023725.
3. O. Johnson, I. Kontoyiannis and M. Madiman, “On the entropy and log-concavity of compound Poisson measures,” arXiv:0805.4112.
