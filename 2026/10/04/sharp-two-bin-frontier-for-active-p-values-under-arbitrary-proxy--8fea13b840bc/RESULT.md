# Sharp two-bin frontier for active p-values under arbitrary proxy dependence
## Finding
Let \(P\in[0,1]\) be a valid null p-value, so \(\Pr(P\le s)\le s\) for every \(s\in[0,1]\). Let a proxy be reduced to two bins \(J\in\{1,2\}\), with no restriction on the dependence between \(J\) and \(P\). Let \(U\sim\mathrm{Unif}(0,1)\) be independent of \((P,J)\). Fix query probabilities \(0\le h_1\le h_2\le1\) and queried p-value multipliers \(0<b_1\le b_2\le1\), and define

\[
P^{\mathrm{act}}=
\begin{cases}
1,&U\ge h_J,\\
b_JP,&U<h_J.
\end{cases}
\]

Then \(P^{\mathrm{act}}\) is super-uniform for every joint law of \((P,J)\) having super-uniform \(P\) if and only if

\[
\frac{h_1}{b_1}+\frac{h_2-h_1}{b_2}\le1.
\]

When \(h_1>0\), the smallest universally valid first-bin multiplier at fixed \(h_1,h_2,b_2\) is therefore

\[
b_1^\star=\frac{h_1}{1-(h_2-h_1)/b_2},
\]

whenever the denominator is positive. The concrete boundary point \((h_1,h_2,b_1,b_2)=(1/5,4/5,1/2,1)\) is universally valid under arbitrary proxy dependence. It is outside the split-tail sufficient class of Kuang, Gang, and Xia: their nonquery constraint would require \(\beta\ge4/5\), while their queried constraint in bin \(1\) would require \(\beta\le3/5\).

## Assumptions and scope
The result concerns a single null hypothesis, a two-valued proxy label, a bona fide super-uniform p-value \(P\), and an independent auxiliary uniform randomizer \(U\). The proxy label may depend arbitrarily on \(P\). The nonquery output is fixed at \(1\); the queried branch rescales \(P\) by a bin-specific factor. The ordering \(h_1\le h_2\) and \(b_1\le b_2\) labels the low-query/more-aggressive bin first. The restriction \(b_2\le1\) focuses on power-improving queried multipliers and is used in the clean three-region form of the proof.

The claim is not a characterization of every active p-value of arbitrary functional form, nor is it a multiple-testing FDR theorem. It is a sharp universal-validity frontier for the smallest nonconstant finite proxy alphabet.

## Proof
Fix a rejection level \(s<1\). The nonquery output equals \(1\), so it cannot reject at level \(s\). Conditional on \((P,J)\), the rejection probability over \(U\) is

\[
h_J\,\mathbf{1}\{b_JP\le s\}.
\]

For \(p\in[0,1]\), define the worst proxy choice

\[
g_s(p)=\max\left\{h_1\mathbf{1}\{p\le s/b_1\},\;h_2\mathbf{1}\{p\le s/b_2\}\right\}.
\]

Because \(b_1\le b_2\) and \(h_1\le h_2\), if \(t_i(s)=\min\{1,s/b_i\}\), then \(t_1(s)\ge t_2(s)\) and

\[
g_s(p)=
\begin{cases}
h_2,&0\le p\le t_2(s),\\
h_1,&t_2(s)<p\le t_1(s),\\
0,&p>t_1(s).
\end{cases}
\]

Thus \(g_s\) is nonincreasing. Super-uniformity of \(P\) means that \(P\) stochastically dominates a uniform random variable. Hence, for every bounded nonincreasing function such as \(g_s\),

\[
\mathbb E[g_s(P)]\le\int_0^1g_s(p)\,dp
=h_1t_1(s)+(h_2-h_1)t_2(s)=:W(s).
\]

For every possible dependence between \(J\) and \(P\),

\[
\Pr(P^{\mathrm{act}}\le s)
=\mathbb E\!\left[h_J\mathbf{1}\{b_JP\le s\}\right]
\le\mathbb E[g_s(P)]\le W(s).
\]

Write

\[
C=\frac{h_1}{b_1}+\frac{h_2-h_1}{b_2}.
\]

If \(0\le s\le b_1\), then \(W(s)=Cs\). If \(b_1\le s\le b_2\), then

\[
W(s)=h_1+\frac{h_2-h_1}{b_2}s.
\]

When \(C\le1\), the first region satisfies \(W(s)\le s\). At \(s=b_1\) the second region starts below the diagonal, and its slope \((h_2-h_1)/b_2\) is at most \(C\le1\), so it remains below the diagonal. Finally, for \(s\ge b_2\), \(W(s)=h_2\). Since \(b_1\le b_2\),

\[
C\ge\frac{h_1}{b_2}+\frac{h_2-h_1}{b_2}=\frac{h_2}{b_2},
\]

so \(C\le1\) implies \(h_2\le b_2\le s\). Therefore \(W(s)\le s\) for every \(s<1\), while validity at \(s=1\) is automatic.

For necessity, suppose \(C>1\). Choose any \(s\in(0,b_1]\), let \(P\sim\mathrm{Unif}(0,1)\), and define the proxy label as a deterministic function of \(P\): use bin \(2\) when \(P\le s/b_2\), bin \(1\) when \(s/b_2<P\le s/b_1\), and either bin above \(s/b_1\). Then the rejection probability is exactly

\[
h_2\frac{s}{b_2}+h_1\left(\frac{s}{b_1}-\frac{s}{b_2}\right)=Cs>s.
\]

This admissible null law violates super-uniformity. Hence \(C\le1\) is also necessary.

For the example \((1/5,4/5,1/2,1)\), the frontier expression equals \(1\). To see why the split-tail decomposition cannot represent it, the decomposition's nonquery bound at \(s=1\), tested on a deterministic first-bin proxy, requires \(1-h_1\le\beta\), hence \(\beta\ge4/5\). Its queried bound, again on a deterministic first-bin proxy with uniform \(P\) and sufficiently small \(s\), requires \(h_1s/b_1\le(1-\beta)s\), hence \(\beta\le1-h_1/b_1=3/5\), a contradiction.

## Verification
The standalone script `verify.py` checks the exact rational arithmetic of the boundary example, the incompatible decomposition inequalities, the three-region envelope, and a finite family of rational parameter tuples against the stated envelope formula. Those computations are corroborative; the universal theorem is established by the analytic stochastic-order and adversarial-proxy argument above, not by finite enumeration.

## Relationship to prior work
Kuang, Gang, and Xia, *Active Hypothesis Testing under Computational Budgets* (arXiv:2512.01423; first public version 2025-12-01), define the same general active p-value form with nonquery branch \(a(P^a)\), queried branch \(b(P^a)P\), and proxy-dependent query probability. Their equation (3) is the exact tail-validity requirement. They impose separate sufficient bounds on the nonquery and query contributions and explicitly state in Remark 3 that this decomposition is not necessary. Their supplement gives a valid nondecomposable example with \(a\equiv b\equiv1\), but the inspected full text does not state the sharp two-bin multiplier frontier above or the boundary example with a strictly smaller queried multiplier.

Xu, Wang, Wasserman, Roeder, and Ramdas, *Active multiple testing with proxy p-values and e-values* (arXiv:2502.05715; first public version 2025-02-08), prove arbitrary-dependence validity for a particular active p-value family. Their construction couples the proxy value, query probability, and a single queried scaling rule; it does not imply the two-bin necessary-and-sufficient frontier for the nonquery-one family above.

The new statement is therefore narrower than a full characterization of active p-values but sharper within a natural two-bin design: it identifies the exact dependence-robust power boundary, not merely a sufficient construction.

## Limitations
The theorem assumes exactly two proxy bins, ordered query probabilities and multipliers, a nonquery output fixed at \(1\), and queried multipliers no larger than \(1\). It does not optimize the query probabilities themselves, does not handle more than two bins in closed form, and does not establish FDR control beyond the standard consequence that any valid p-value may be supplied to procedures whose assumptions are otherwise met. The literature comparison cannot rule out an equivalent result under terminology not captured by the inspected active-testing and randomized-p-value sources; no such equivalent statement was found in the targeted searches.

## References
1. Qi Kuang, Bowen Gang, and Yin Xia. *Active Hypothesis Testing under Computational Budgets*. arXiv:2512.01423. First public version: 2025-12-01.
2. Ziyu Xu, Catherine Wang, Larry Wasserman, Kathryn Roeder, and Aaditya Ramdas. *Active multiple testing with proxy p-values and e-values*. arXiv:2502.05715. First public version: 2025-02-08.
3. Mathematical Reviews and zbMATH. *MSC2020 Mathematical Sciences Classification System*. Code 62G10: Nonparametric hypothesis testing.
