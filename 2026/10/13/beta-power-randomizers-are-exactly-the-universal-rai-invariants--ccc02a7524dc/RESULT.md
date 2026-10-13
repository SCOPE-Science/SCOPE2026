# Beta-power randomizers are exactly the universal RAI invariants
## Finding
Let \(Z\) be an absolutely continuous random variable on \((0,1)\) with strictly increasing distribution function \(G\) and density \(g>0\) almost everywhere. For every nonnegative absolutely continuous random variable \(X\), write \(F_X\) for its distribution function, \(Q_X\) for its quantile function, and
\[
\breve L_X(t)=\frac{-t f_X(t)}{F_X(t)\log F_X(t)}
\]
for its reversed aging intensity (RAI) function at points where \(0<F_X(t)<1\).

The randomizer \(Z\) has the universal invariance property
\[
\breve L_{Q_X(Z)}(t)=\breve L_X(t)
\]
for every such parent distribution \(X\) if and only if
\[
G(u)=u^a,\qquad 0<u<1,
\]
for some \(a>0\). Equivalently, the universal RAI-invariant randomizers are exactly the \(\operatorname{Beta}(a,1)\) laws.

As a consequence, if \(Z_a\sim\operatorname{Beta}(a,1)\) and \(Z_b\sim\operatorname{Beta}(b,1)\), then for arbitrary admissible parents \(X,Y\),
\[
Q_X(Z_a)\le_{RAI}Q_Y(Z_b)
\quad\Longleftrightarrow\quad
X\le_{RAI}Y.
\]
No usual-stochastic-order assumption is needed, and the two randomizers may have different parameters. The increasing-RAI and decreasing-RAI classes are also invariant under every such transform.

For positive integers \(n,m\), \(Q_X(Z_n)\) and \(Q_Y(Z_m)\) are the maxima \(X_{n:n}\) and \(Y_{m:m}\) of iid samples. Hence
\[
X_{n:n}\le_{RAI}Y_{m:m}
\quad\Longleftrightarrow\quad
X\le_{RAI}Y
\]
for every \(n,m\ge1\).

## Assumptions and scope
All parent distributions in the theorem are nonnegative and absolutely continuous. The displayed RAI identities are asserted on the interior set where the corresponding cdf lies strictly between zero and one and the density formula is defined. The randomizer cdf \(G\) is absolutely continuous and strictly increasing on \((0,1)\), with positive density almost everywhere.

The characterization is universal: it concerns randomizers that preserve the RAI function for every admissible parent distribution. It does not classify randomizers that happen to preserve RAI for one specially chosen parent.

## Proof
For any randomizer \(Z\) on \((0,1)\), the random-quantile identity gives
\[
F_{Q_X(Z)}(t)=G(F_X(t)).
\]
Writing \(u=F_X(t)\), differentiation at regular points gives
\[
f_{Q_X(Z)}(t)=g(u)f_X(t).
\]
Therefore
\[
\frac{\breve L_{Q_X(Z)}(t)}{\breve L_X(t)}
=
\frac{u\log u\,g(u)}{G(u)\log G(u)}.
\tag{1}
\]

If \(G(u)=u^a\) with \(a>0\), then \(g(u)=a u^{a-1}\), so the right side of (1) is identically one. This proves RAI invariance for every parent.

Conversely, suppose RAI invariance holds for every admissible parent. It is enough to apply it to a rate-one exponential parent, whose cdf \(F_X(t)=1-e^{-t}\) ranges over all \(u\in(0,1)\). Equation (1) then forces, almost everywhere on \((0,1)\),
\[
\frac{u\log u\,G'(u)}{G(u)\log G(u)}=1.
\tag{2}
\]
Put \(y(u)=-\log G(u)>0\). Since \(G'(u)/G(u)=-y'(u)\), equation (2) becomes
\[
\frac{y'(u)}{y(u)}=\frac{1}{u\log u}.
\]
Integration yields
\[
\log y(u)=\log(-\log u)+C,
\]
so
\[
-\log G(u)=a(-\log u)
\]
for a constant \(a>0\). Thus \(G(u)=u^a\). Absolute continuity upgrades the almost-everywhere differential identity to the stated cdf identity on all of \((0,1)\).

For the order consequence, a \(\operatorname{Beta}(a,1)\) randomizer gives
\[
F_{Q_X(Z_a)}(t)=F_X(t)^a
\quad\text{and}\quad
\breve L_{Q_X(Z_a)}(t)=\breve L_X(t).
\]
Hence the pointwise inequality defining RAI order is unchanged, even if the two transforms use different positive exponents \(a,b\). The IRAI and DRAI statements follow because the RAI function itself is unchanged.

Finally, when \(a=n\) is a positive integer, \(F_X(t)^n\) is the cdf of the iid sample maximum \(X_{n:n}\), giving the parallel-system corollary.

## Verification
No numerical experiment or finite enumeration is needed for the theorem. The critical identity is (1), obtained by differentiating the exact random-quantile cdf composition. Necessity is reduced to the first-order differential equation (2), whose complete positive solution family is \(G(u)=u^a\), \(a>0\).

Two boundary checks are built into the solution. Because \(G\) is a cdf on \((0,1)\), the integration constant must satisfy \(a>0\): \(a=0\) would give the constant function one, and \(a<0\) would violate the cdf boundary behavior. Conversely every \(a>0\) gives a valid strictly increasing cdf with density \(a u^{a-1}\).

The theorem makes no claim for singular randomizers, randomizers with flat cdf pieces, or parent distributions outside the stated absolutely continuous domain.

## Relationship to prior work
Kayid and Alshehri study RAI preservation under random quantiles. Their random-quantile formula is exactly
\[
F_{Q_X(Z)}(t)=F_Z(F_X(t)).
\]
Their Theorem 5.1 gives sufficient preservation conditions for a common randomizer and additionally assumes a usual stochastic ordering of the parent distributions. Their Example 5.2 takes \(Z\sim\operatorname{Beta}(n,1)\), so that the transforms are iid sample maxima, and concludes RAI preservation under that extra stochastic-order assumption. Their conclusion explicitly identifies preservation for two different randomizers \(Q_X(Z_1)\) and \(Q_Y(Z_2)\) as a future problem.

The present result isolates a natural family in that future direction: different \(\operatorname{Beta}(a,1)\) randomizers preserve the RAI comparison exactly and require no stochastic-order side condition. It also proves a converse classification: among absolutely continuous strictly increasing randomizers, this power family is the only one that leaves every parent RAI function unchanged.

Buono, Longobardi, and Szymkowiak develop generalized RAI functions and their orders. Their work supplies relevant background on ordinary and generalized RAI and discusses largest order statistics through generalized RAI quantities, but the inspected full text does not formulate the random-quantile randomizer-classification problem or the universal invariance theorem above. Their later paper on improvements to generalized RAI likewise studies relations among generalized RAI constructions rather than random-quantile invariance.

## Limitations
The uniqueness statement is for absolutely continuous, strictly increasing randomizer cdfs with positive density almost everywhere. Singular or partly discrete randomizers are not classified here.

The result identifies the exact universal-invariance class, not all pairs \((Z_1,Z_2)\) that may preserve one particular RAI comparison for specially chosen parents. Thus it gives a complete natural subproblem, rather than a complete solution of the broad two-randomizer preservation question.

Bibliographic searches cannot exclude an equivalent observation under unrelated reliability terminology. The closest inspected sources do not state the universal randomizer characterization or the different-parameter equivalence.

## References
1. M. Kayid and M. A. Alshehri, “Stochastic aspects of reversed aging intensity function of random quantiles,” *Journal of Inequalities and Applications* 2024, 119 (2024). DOI: 10.1186/s13660-024-03198-y.
2. F. Buono, M. Longobardi, and M. Szymkowiak, “On generalized reversed aging intensity functions,” *Ricerche di Matematica* 71 (2022), 85–108. DOI: 10.1007/s11587-021-00560-w.
3. F. Buono, M. Longobardi, and M. Szymkowiak, “Some improvements on generalized reversed aging intensity functions,” *Ricerche di Matematica* 74 (2025), 819–834. DOI: 10.1007/s11587-024-00862-9.
