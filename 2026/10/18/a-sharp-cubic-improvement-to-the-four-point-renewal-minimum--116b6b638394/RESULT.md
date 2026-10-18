# A sharp cubic improvement to the four-point renewal minimum

## Finding

For a renewal process whose independent increments take values in \(\{1,2,3,4\}\), write \(a,b,c,d\) for the four probabilities, with \(a,b,c,d\geq0\) and \(a+b+c+d=1\). Define the renewal masses \(u_n=\Pr\{n=S_j\text{ for some }j\geq0\}\) for \(n\geq1\), where \(S_0=0\) and \(S_j\) is the sum of the first \(j\) increments, and put \(m_4=\inf_{n\geq1}u_n\).

Nikolov and Savov's canonical polynomial lower envelope is
\[
Q_4=a(a+b)(a+b+c).
\]
The cubic polynomial
\[
\boxed{P_4=a(a+b)(a+b+c)+2abd}
\]
satisfies \(Q_4\leq P_4\leq m_4\) for **every** such increment law. The improvement is strict whenever \(abd>0\), including interior distributions. Moreover, \(P_4\) belongs to the restricted polynomial class \(\widehat{\mathcal A}_4\) of Nikolov–Savov, as well as to \(\mathcal A_4\). Hence \(Q_4\) is neither maximal in \(\mathcal A_4\) nor largest in \(\widehat{\mathcal A}_4\), disproving both universal claims of their Conjecture 3.7 at \(k=4\).

The coefficient \(2\) is best possible within the natural one-term family \(Q_4+\alpha abd\): for \(\alpha\geq0\), this polynomial lies below \(m_4\) throughout the simplex if and only if \(\alpha\leq2\). No optimality among arbitrary degree-three polynomial minorants is asserted.

## Assumptions and scope

Any individual probability may vanish, and the result covers the whole closed probability simplex, not just aperiodic laws. The definition of \(m_4\) excludes \(u_0=1\). In the cited setting, Corollary 3.4 establishes
\[
m_4=\min\{u_1,u_2,u_3\}.
\]
This finite-minimum reduction is the only external renewal-theoretic premise; for completeness it also follows directly because, for \(n\geq4\), the renewal recursion expresses \(u_n\) as a convex combination of \(u_{n-1},u_{n-2},u_{n-3},u_{n-4}\), taking \(u_0=1\): induction shows \(u_n\geq\min\{1,u_1,u_2,u_3\}\), and all three initial masses are at most one.

To make class membership precise, \(\mathcal A_4\) consists of polynomials of total degree at most \(3\) in \((a,b,c)\) that lie below \(m_4\) throughout \(a,b,c\geq0\), \(a+b+c\leq1\). The subclass \(\widehat{\mathcal A}_4\) requires that the polynomial written in cumulative coordinates \(s_1=a\), \(s_2=a+b\), \(s_3=a+b+c\) have degree at most \(j\) after the last \(3-j\) cumulative variables are set to \(1\), for each \(j=1,2,3\).

## Proof

The renewal recursion \(u_n=\sum_{j=1}^{\min(n,4)}p_ju_{n-j}\), with \(u_0=1\), gives exactly
\[
 u_1=a,\qquad u_2=a^2+b,\qquad u_3=a^3+2ab+c.
\]
Let \(P_4=Q_4+2abd\), where \(d=1-a-b-c\). Direct polynomial identities, valid whenever the four probabilities sum to \(1\), are
\[
\begin{aligned}
 u_1-P_4&=a\bigl(c+d(1+a-b)\bigr),\\
 u_2-P_4&=b^2+bc+d\bigl(a^2+b(1-a)\bigr),\\
 u_3-P_4&=ab(b+c)+c(1-a^2).
\end{aligned}
\]
Every term on the right is nonnegative on the closed probability simplex because \(0\leq a,b\leq1\). Thus \(P_4\leq\min(u_1,u_2,u_3)=m_4\). Also \(P_4-Q_4=2abd\geq0\), strictly if \(abd>0\). The displayed expression has total degree at most three in the independent coordinates \((a,b,c)\); therefore \(P_4\in\mathcal A_4\).

To verify the more restrictive membership, substitute \(a=s_1\), \(b=s_2-s_1\), \(c=s_3-s_2\), \(d=1-s_3\). Then
\[
 \widehat P_4(s_1,s_2,s_3)=s_1s_2s_3+2s_1(s_2-s_1)(1-s_3).
\]
Its terminal specializations are \(\widehat P_4(s_1,1,1)=s_1\) (degree \(1\)), \(\widehat P_4(s_1,s_2,1)=s_1s_2\) (degree \(2\)), and the full expression has total degree at most \(3\). Therefore \(P_4\in\widehat{\mathcal A}_4\). Since \(P_4\succ Q_4\) strictly somewhere, both assertions of Conjecture 3.7 for \(k=4\) fail.

For the optimal coefficient within the specified one-term family, take \(a=b=t\), \(c=0\), \(d=1-2t\) with \(0<t<1/2\). For \(P_\alpha=Q_4+\alpha abd\), direct substitution gives
\[
 u_3-P_\alpha=t^2\bigl[(2-\alpha)+(2\alpha-3)t\bigr].
\]
When \(\alpha>2\), this quantity is negative for every sufficiently small positive \(t\), proving \(P_\alpha\notin\mathcal A_4\). Conversely, for \(0\leq\alpha\leq2\), one has \(P_\alpha\leq P_4\leq m_4\). This proves the sharp iff statement.

## Verification

The standalone file `artifacts/verify.py` uses only the Python standard library. It independently expands all three deficit identities in the polynomial ring \(\mathbb Z[a,b,c]\), verifies the cumulative-coordinate specializations and degree conditions, checks nonnegative inequalities at 8,854 exact-rational simplex grid points, and checks three exact-rational instances illustrating sharpness beyond coefficient \(2\). Command: `python3 artifacts/verify.py`. Expected output starts with `VERIFY_OK`.

At equal masses \(a=b=c=d=1/4\), the benchmark values are \(Q_4=3/32\), \(P_4=1/8\), \(u_1=1/4\), \(u_2=5/16\), \(u_3=25/64\). This gives an explicit interior strict improvement. The symbolic identities and positivity arguments, not the finite grid, establish the universal inequalities.

## Relationship to prior work

Nikolov and Savov, *Properties and conjectures regarding discrete renewal sequences* (arXiv:2307.00545, first publicly posted July 2, 2023; subsequently *Mathematics and Informatics*, 2024), define \(Q_k\), \(\mathcal A_k\), and \(\widehat{\mathcal A}_k\), prove \(Q_k\leq m_k\), and conjecture in Conjecture 3.7 that \(Q_k\) is maximal in \(\mathcal A_k\) and largest in \(\widehat{\mathcal A}_k\) for every \(k\geq3\). Their Proposition 3.8 proves the \(k=3\) case. This finding supplies a counterexample, uniformly on the whole simplex, at the next index \(k=4\); it does not contradict their established \(k=3\) theorem or the general lower-envelope inequality. The source's general Theorem 3.6 rules out a largest element of \(\mathcal A_k\), which is logically weaker than ruling out maximal elements; the present explicit dominating polynomial directly addresses maximality as conjectured.

Standard renewal-process texts establish renewal recursions and limiting renewal masses but do not, in the inspected sources, address this comparison within the polynomial minorant classes. The explicit cubic must be compared with equivalent cumulative-coordinate formulations, not just with identically written formulas.

## Limitations

Only \(k=4\) is settled negatively. The coefficient \(2\) is optimal solely in the family \(Q_4+\alpha abd\), not among all cubic improvements. No assertion is made about a largest element of the restricted class, uniqueness of better polynomial minorants, or other values of \(k\). Literature searches and record comparisons cannot exclude all unindexed earlier equivalent counterexamples; independent scientific validation has not been performed.

## References

1. N. Nikolov and M. Savov, *Properties and conjectures regarding discrete renewal sequences*, arXiv:2307.00545 (first submitted 2023-07-02), https://arxiv.org/abs/2307.00545 ; *Mathematics and Informatics* 67(2) (2024), 111–118, doi:10.53656/math2024-2-1-pro; especially Equations (4)–(8), Corollary 3.4, Theorem 3.6, Conjecture 3.7 and Proposition 3.8.
2. S. P. Lalley, *Renewal Theory*, course notes, https://galton.uchicago.edu/~lalley/Courses/383/Renewal.pdf (background on the discrete renewal recursion).
