# The cubic truthfulness threshold for three-site inverse-power facility omission

## Finding

Let \(\alpha\ge0\) be real. For exactly three strategic agents in an arbitrary metric space, the inverse-power omission rule chooses two of the three reported sites as facilities, omitting report \(i\) with probability proportional to \(\delta_i^{-\alpha}\), where \(\delta_i\) is its nearest-other-report distance. For coincident reports it covers all distinct reported sites.

**Theorem.** This mechanism is strategyproof in expectation for every metric space and every triple of agents **if and only if** \(0\le\alpha\le3\). The endpoint \(\alpha=3\) is attained: the inverse-cube rule is truthful, while every \(\alpha>3\) admits a profitable deviation already on the real line.

For perspective, combining the truthfulness endpoint with the established power-law welfare calculation gives the inverse-cube rule a sharp two-facility social-cost ratio \(R\), the unique solution \(R>1\) to \(27R^2(R-1)=2\), namely \(R=1.0652744484818824\ldots\). The *novel claim is the global incentive classification*, not the previously derived exponent-dependent welfare expression.

## Assumptions and scope

Fix any metric space \((X,d)\). Three agents at true locations \((x_1,x_2,x_3)\) report arbitrary elements of \(X\). When reports \((r_1,r_2,r_3)\) are distinct, let \(\delta_i=\min_{j\ne i}d(r_i,r_j)>0\) and set
\[
\Pr(\text{omit }i)=\frac{\delta_i^{-\alpha}}{\sum_{j=1}^3\delta_j^{-\alpha}}.
\]
Two facilities are installed at the other two reports. If any reports coincide, facilities cover all distinct reports (at most two). An agent pays the distance of her **true** location to the closest facility. Strategyproofness in expectation means that for every true profile, agent and unilateral alternative report, expected cost cannot strictly decrease. No transfers, restrictions to a line, or assumptions on available extra metric points are imposed. The exponent family under study is \(\alpha\ge0\).

Every distinct three-site profile has nearest-neighbor distances \((a,a,b)\) after relabeling, with \(0<a\le b\); equalities and all metric triangle configurations are allowed. For a particular agent \(i\), let \(d=\delta_i\) and let \(O=\sum_{j\ne i}(d/\delta_j)^\alpha\). Its truthful expected cost is \(c=d/(1+O)\le d/2\). Write \(h=d(x_i,r_i')\) for a deviation. When \(h\ge c\), every possible facility remains at distance at least \(\min\{h,d\}\ge c\), and the deviation cannot help. Reporting another agent's actual site is similarly unprofitable. It suffices to take \(0<h<c\) with all resulting reports distinct. In this regime, if \(O'\) denotes the new relative omission odds, the deviator's exact cost is
\[
C'=h+\frac{d-h}{1+O'}.
\]

## Proof

### 1. An agent initially at the distant site

Suppose the other two agents are separated by \(a\), and the deviator has nearest-neighbor distance \(b\ge a\). Set \(S=2(b/a)^\alpha\ge2\), \(t=h/b\), and \(K=S(1+t)^\alpha\). If the deviating report remains the distant member of the new three-site configuration, the other two nearest-neighbor distances stay \(a\), while its new nearest-neighbor distance is at most \(b+h\); hence \(O'\le K\). If the new report belongs to a closest pair, its two omission-odds terms add to at most \(2\), again \(O'\le K\). Thus
\[
\frac{C'}b\ge t+\frac{1-t}{1+S(1+t)^\alpha}.
\]
Because \(0<t<1/(1+S)\), comparison with \(c/b=1/(1+S)\) is equivalent to
\[
(1+t)^\alpha[1-(1+S)t]\le1.
\]
For \(0\le\alpha\le3\) and \(S\ge2\), the left side is at most \((1+t)^3(1-3t)\le1\); the last function decreases on \([0,1/3]\). Therefore the far-site agent cannot gain.

### 2. An agent initially in a closest pair

Normalize the agent's nearest distance to \(a=1\). Denote its nearest neighbor by \(j\), and the third agent by \(k\), with \(\delta_j=1\), \(\delta_k=b\ge1\). Then
\[
c=\frac1{2+b^{-\alpha}},\qquad 0<h<c\le\frac12.
\]
We partition the possible postdeviation closest-pair geometry.

**2a. The deviating report belongs to a closest pair, and \(b\le1+2h\).** Both members of that pair have the same smallest nearest distance; thus \(O'\le2\), giving \(C'\ge(1+2h)/3\). Put \(s=1+2h\ge1\). As \(b\le s\),
\[
c\le\frac1{2+s^{-\alpha}}\le\frac s3=\frac{1+2h}{3}.
\]
The middle inequality follows from \(2s+s^{1-\alpha}\ge3\), valid for all \(s\ge1\), \(\alpha\le3\), since its derivative is \(2+(1-\alpha)s^{-\alpha}\ge0\) and the value at \(s=1\) is three.

**2b. The deviating report belongs to a closest pair, and \(b\ge1+2h\).** The closest-pair partner must be \(j\): the triangle inequality yields \(d(r_i',x_j)\le1+h\le b-h\le d(r_i',x_k)\). The new nearest distance of \(k\) is at least \(b-h\). Consequently
\[
O'\le1+q(h)^\alpha,\qquad q(h)=\frac{1+h}{b-h}\le1,
\]
and \(C'\ge F(h)=h+(1-h)/(2+q(h)^\alpha)\). At zero, \(F(0)=c\). With \(z=q(h)^\alpha\le1\), differentiation gives
\[
(2+z)^2F'(h)=(1+z)(2+z)
-\alpha\frac{1-h}{1+h}z(1+q).
\]
For \(0\le\alpha\le3\), \(h<1/2\) and \(q\le1\), the second term is at most \(6z\); hence the derivative is at least \((1-z)(2-z)/(2+z)^2\ge0\). This holds for every intermediate displacement between zero and \(h\), so \(C'\ge c\).

**2c. The deviating report becomes the distant member.** Write \(C=d(x_j,x_k)\) for the unchanged distance of the other two sites. Initially \(C\ge b\). After the deviation the new report is distant, so \(C\le\delta_i'\le1+h\). Necessarily \(1\le b\le1+h\), and
\[
O'=2\left(\frac{\delta_i'}{C}\right)^\alpha
\le2\left(\frac{1+h}{b}\right)^\alpha.
\]
Therefore
\[
C'\ge h+\frac{1-h}{1+2((1+h)/b)^\alpha}.
\]
The right side decreases with \(\alpha\), whereas \(c=1/(2+b^{-\alpha})\) increases with \(\alpha\); it is enough to establish the inequality at \(\alpha=3\). Write \(b=1+vh\) for \(0\le v\le1\), \(u=1+h\). Clearing positive denominators gives the **exact identity**
\[
h+\frac{(1-h)b^3}{b^3+2u^3}-\frac{b^3}{2b^3+1}
=\frac{h P(h,v)}{(b^3+2u^3)(2b^3+1)},
\]
where
\[
\begin{aligned}
P(h,v)={}&3v+h(12v^2-6v+12)\\
&+h^2(19v^3-6v^2+18v+16)\\
&+h^3(15v^4-2v^3+18v^2+30v+6)\\
&+h^4(6v^5+6v^3+30v^2+12v)\\
&+h^5(v^6+10v^3+12v^2)+4h^6v^3.
\end{aligned}
\]
This polynomial is nonnegative for \(h\ge0\), \(0\le v\le1\). Indeed the only potentially negative groups satisfy \(12v^2-6v+12>0\), \(18v-6v^2\ge0\), and \(18v^2-2v^3\ge0\); all remaining monomials have nonnegative coefficients. The identity is independently checked by the included exact polynomial verifier. Thus no close-pair agent can gain in the far-transition case.

Combining the three subcases with Part 1 proves strategyproofness for every \(0\le\alpha\le3\), including ties, arbitrary metrics and arbitrary available deviation sites. Coincident truthful reports yield cost zero, so are also incentive-safe.

### 3. Every larger power is manipulable

Take reports \((0,1,2)\) on the line and let the leftmost agent report \(-\varepsilon\) for \(\varepsilon>0\). Its truthful expected cost is \(1/3\), but its deviating cost is
\[
C_\alpha(\varepsilon)=\varepsilon+
\frac{1-\varepsilon}{1+2(1+\varepsilon)^\alpha},\qquad
C_\alpha'(0)=\frac{2(3-\alpha)}9.
\]
For every \(\alpha>3\), this one-sided derivative is strictly negative, producing a profitable deviation for sufficiently small \(\varepsilon>0\). This proves that three is the sharp exponent endpoint.

## Verification

Run `python3 verify.py` with Python 3 and no third-party packages. The standalone script exactly verifies the rational polynomial identity in Part 2c by two-variable integer-polynomial arithmetic; checks all \(4^6=4096\) labeled weighted complete graphs on four vertices with edge weights in \(\{1,2,3,4\}\), followed by exact shortest-path metric closure, all three agents, four possible deviation sites and exponents \(0,1,2,3\) (196,608 comparisons); and checks an exact profitable exponent-four witness. These finite checks corroborate, but do not prove, the continuum-in-exponent and all-metric theorem; the preceding analytical cases supply the proof.

## Relationship to prior work

Escoffier, Gourvès, Nguyen, Pascual and Spanjaard (2011), Section 2, introduced the inverse-first-power rule and proved its strategyproofness. Chan, Lin and Wang (first public release 2026-08-23), Section 4 and Theorem 3, proved the inverse-square rule strategyproof for **all** agent counts and metrics. These prior proofs do not assert truthfulness for the inverse-cube rule. The previously established full-power welfare calculation and the negative incentive obstruction for exponents greater than three also do not imply a positive truthfulness classification for the remaining exponents. The specific addition here is that the sharp, previously necessary cubic upper bound is **attainable for the entire three-agent metric problem**.

As a welfare implication, the already-known full-power formula specializes at exponent three to \(R=1.0652744484818824\ldots\), versus the known inverse-square ratio \((1+\sqrt{3/2})/2=1.1123724356957945\ldots\) for three agents. The welfare formulas themselves are not asserted to be new.

## Limitations

The positive strategyproofness theorem is **only for exactly three agents and two facilities**, and for nonnegative real exponents. It does not claim that exponent three is strategyproof for four or more agents, nor that it is optimal over all randomized strategyproof mechanisms. The decision rule assumes distances in one common metric and facilities constrained to reported positions; no costs of opening facilities or strategic coalitions are modeled. The extremal welfare ratio quoted is from a separate sharp family calculation, not a new welfare proof. No independent mathematical audit has been performed, and unindexed equivalent prior work remains a residual originality risk.

## References

1. H. Chan, J. Lin, and C. Wang, *Randomized Strategyproof Facility Location: Two Facilities and Beyond*, arXiv:2608.22484 (first public 2026-08-23), Section 4 and Theorem 3. https://arxiv.org/abs/2608.22484
2. B. Escoffier, L. Gourvès, N. K. Thang, F. Pascual, and O. Spanjaard, *Strategy-Proof Mechanisms for Facility Location Games with Many Facilities*, Algorithmic Decision Theory, LNCS 6992 (2011), 67–81, Section 2. https://doi.org/10.1007/978-3-642-24873-3_6
3. D. Fotakis and C. Tzamos, *Strategy-Proof Facility Location for Concave Cost Functions*, arXiv:1305.3333 (2013), for a different multi-facility lottery family. https://arxiv.org/abs/1305.3333
