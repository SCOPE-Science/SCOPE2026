# Exact potential and reentrant equilibrium census for one-vacancy multipartite diversity jumps

## Finding

For every complete multipartite graph \(K_{s_1,\ldots,s_h}\) with \(h\ge3\) and positive integer part sizes, place exactly one vacancy and give all remaining occupants the same fractional diversity-seeking preference: the utility of an occupant is the proportion of occupied neighbors whose type differs from its own. An **exact potential** exists for any finite type set. With two colors, every pure Nash equilibrium has monochromatic fully occupied parts, and a pair of explicit integer inequalities per such part is necessary and sufficient. These inequalities provide the complete red-count equilibrium polynomial for arbitrary part sizes.

When all part sizes are \(m\ge1\), the equilibrium polynomial is
\[
E_{h,m}(z)=hm(1+z)^{m-1}(1+z^m)^{h-1}.
\]
Among all vacancy-and-color assignments with both color names permitted, the equilibrium fraction is exactly \(2^{-(h-1)(m-1)}\). Unequal parts exhibit a genuine arithmetic reentrance: in \(K_{2,2,b}\), if the vacancy lies in the part of size \(b\ge2\) and the two size-two parts have opposite monochromatic colors, such a state can be an equilibrium exactly for \(b\in\{2,3,5\}\); it cannot for \(b=4\) or \(b\ge6\).

## Assumptions and scope

The graph is simple, labeled, complete multipartite, with parts \(V_1,\ldots,V_h\) of sizes \(s_1,\ldots,s_h\), \(h\ge3\), and \(N=\sum_i s_i\). There are \(N-1\) strategically movable occupants and exactly one vacant vertex. All occupants may jump to that vertex, without locality restrictions, only if their **own** utility increases strictly. Occupants have finitely many types \(t\in\mathcal T\); types may have zero population. Utilities count **occupied** neighbors and exclude the occupant. Since \(h\ge3\), every relevant neighborhood contains at least one occupant. Two occupants of the same type are interchangeable for the enumerators; positions and the vacancy are labeled.

Write \(R_t\) for the total number of type-\(t\) occupants, \(x_{it}\) for the number in part \(i\), and \(H_i=N-s_i-1\). Each \(H_i\ge1\). A Nash equilibrium is a configuration in which no occupant can strictly improve by jumping to the vacancy. For the two-color specialization use red \(R\) and blue \(B\); the polynomial \(E_G(z)\) gives the number of equilibria having precisely \(r\) red occupants as the coefficient of \(z^r\), ranging over all red/blue populations from zero through \(N-1\).

For a given vacant part \(j\), choose a subset \(A\subseteq\{1,\ldots,h\}\setminus\{j\}\) of the fully occupied parts that are red; all other fully occupied parts are blue. Define \(P_A=\sum_{i\in A}s_i\) and \(Q_A=\sum_{i\notin A,\ i\ne j}s_i\). If the vacant part contains \(r\) red and \(s_j-1-r\) blue occupants, the exact stability conditions are
\[
\begin{aligned}
Q_A(s_j-s_i)&\le(s_j-1-r)H_j&&\text{for every }i\in A,\\
P_A(s_j-s_i)&\le rH_j&&\text{for every }i\notin A,\ i\ne j.
\end{aligned}
\]
The conditions are vacuous over an empty collection. Let \(\mathbf1_{j,A,r}\) equal one if all these conditions hold and zero otherwise.

## Proof

**Exact potential for any finite type set.** Define
\[
\Phi(C)=\sum_{i=1}^{h}\frac1{H_i}\sum_{t\in\mathcal T}
\left[\frac{x_{it}(x_{it}+1)}2-R_t x_{it}\right].
\]
A within-part jump merely exchanges an occupant and the vacancy without changing the occupied neighborhoods or the part counts, so both the moving occupant's utility and \(\Phi\) remain unchanged. For a jump from occupied part \(i\) to a vacancy in a **different** part \(j\), the occupant has type \(t\) and initially sees an occupied neighborhood of size \(H_i\). After the jump it sees one of size \(H_j\). Precisely,
\[
 u_{\rm old}=1-\frac{R_t-x_{it}}{H_i},\qquad
 u_{\rm new}=1-\frac{R_t-x_{jt}-1}{H_j}.
\]
Only \(x_{it}\) and \(x_{jt}\) change, by \(-1\) and \(+1\), respectively. Their contribution to the potential changes by
\[
 \Phi(C')-\Phi(C)
 =\frac{R_t-x_{it}}{H_i}-\frac{R_t-x_{jt}-1}{H_j}
 =u_{\rm new}-u_{\rm old}.
\]
This is an **exact** (not merely ordinal) potential identity for every legal move. Finite strategy spaces imply that every strict improvement sequence terminates in a Nash equilibrium.

**Why every full part is monochromatic in a two-color equilibrium.** Suppose the vacancy is in part \(j\) and a distinct fully occupied part \(i\) contains both red and blue. Choose one occupant of each color in \(i\). The sum of their **current** utilities is exactly one: red counts blue outside \(i\), blue counts red outside \(i\), and the occupied neighbors outside \(i\) number \(H_i\). If each occupant were to jump to the vacancy (in two separate hypothetical unilateral deviations), the sum of the resulting utilities would be \((H_j+1)/H_j>1\). Indeed the red jumper still sees every blue occupant outside \(j\), and the blue jumper still sees every red occupant outside \(j\); their separate opposite-type counts sum to the \(H_j+1\) occupants initially outside \(j\). Hence at least one of the two occupants strictly improves, contradicting equilibrium.

**Necessary and sufficient inequalities.** Conversely, suppose all full parts are pure and the red full parts form \(A\). A red occupant in \(i\in A\) sees \(Q_A+s_j-1-r\) blue occupants outside its part, so its current utility is \((Q_A+s_j-1-r)/H_i\). If moved into the vacancy, it sees precisely the \(Q_A\) blue occupants outside \(j\), with utility \(Q_A/H_j\). Therefore its move improves exactly when
\[
 Q_A(s_j-s_i)>(s_j-1-r)H_j.
\]
Analogously, for a blue occupant in a full part \(i\notin A\), improvement occurs exactly when \(P_A(s_j-s_i)>rH_j\). A jump from one vertex of the vacant part to its own vacancy leaves utility unchanged. Thus the displayed non-strict inequalities in the scope section are jointly **necessary and sufficient**, and, with monochromatic full parts, characterize every two-color equilibrium.

**Exact coefficient formula.** Each choice of vacant part \(j\), red full-part subset \(A\), and red occupancy \(r\in\{0,\ldots,s_j-1\}\) yields \(s_j\) distinct vacancy locations and \(\binom{s_j-1}{r}\) placements of the red occupants within the vacant part. These descriptions are disjoint. Consequently
\[
 E_G(z)=\sum_{j=1}^{h}s_j
 \sum_{A\subseteq[h]\setminus\{j\}}z^{P_A}
 \sum_{r=0}^{s_j-1}\binom{s_j-1}{r}z^r\,\mathbf1_{j,A,r}.
\]
If all \(s_i=m\), every left side involving \(s_j-s_i\) is zero, so every choice of \(j,A,r\) satisfies the inequalities. The binomial theorem gives \(E_{h,m}(z)=hm(1+z)^{m-1}(1+z^m)^{h-1}\). The total number of assignments with one labeled vacancy and arbitrary binary colors at occupied vertices is \(hm2^{hm-1}\); hence the equilibrium fraction is \(2^{-(h-1)(m-1)}\).

**Exact reentrance.** For \(K_{2,2,b}\), fix the vacancy in the size-\(b\) part and give the two size-two full parts opposite colors. Their full-color totals are both two, and \(H_j=3\). If the vacancy part contains \(r\) red occupants, the stability inequalities reduce to
\[
 2(b-2)\le3r,\qquad 2(b-2)\le3(b-1-r).
\]
An integer solution exists exactly when \(2\lceil2(b-2)/3\rceil\le b-1\). For \(b=2,3,4,5\), this holds exactly at \(b=2,3,5\), while adding the two inequalities forces \(b\le5\), eliminating all \(b\ge6\). This proves the claimed loss and reappearance of mixed-color full-part equilibria as the vacancy part grows.

## Verification

The standalone script `verify_multipartite.py` computes utilities directly from adjacency and occupied-neighbor fractions, independently of the derived formulas; it compares **every legal move** with the exact potential increment and compares the full two-color equilibrium polynomial with the count obtained from direct enumeration. It uses rational arithmetic, without floating-point tolerances. Tested sixteen graph/type-set cases, including unequal parts and \(K_{2,2,3}\), \(K_{2,2,4}\), and \(K_{2,2,5}\): 35,349 states and 243,582 legal unilateral moves, all consistent. Sample total equilibrium counts are 68, 96, and 252 for those three graphs (all labeled vacancy/color assignments counted). Run with `python verify_multipartite.py` using Python's standard library; no external data files are needed. These finite tests do not establish the universal theorem; the proof above does.

## Relationship to prior work

Narayanan, Sabbagh, and Voudouris introduced the **fractional unlike-neighbor** diversity-seeking jump game and proved potential properties on regular graphs and single-vacancy spiders, as well as equilibrium existence on trees. Equal-part complete multipartite graphs are regular, so mere convergence there is already within the regular-graph theorem. The present **unequal-part, three-or-more-part** exact potential, the complete two-color equilibrium inequalities, the coefficient formula, and the arithmetic reentrance are distinct statements not obtained by simply applying regularity or spider hypotheses. A specialized two-part result also does not entail the interactions among three or more parts. Friedrich and colleagues analyze a different single-peaked rather than monotone fractional utility; Li and colleagues analyze swaps with other diversity utilities, not single-vacancy fractional jumps.

## Limitations

Exactly one vacancy, unconstrained individual jumps, complete multipartite topology, and fully strategic occupants are essential to the stated proof. The potential result allows any finite type set; the full equilibrium classification and enumerator require **exactly two permitted colors** (although one color may have zero occupants). The result does not classify equilibria for three or more types or for multiple vacancies, general non-multipartite networks, or modified utilities. The equality case gives no strictly improving move; no claims about movement under indifferent swaps are made. The standalone exhaustive computations cover only specified small instances. The regular-graph potential case and the two-part special case are not claimed as new; potential coincidences or alternative formulations elsewhere remain a bibliographic risk.

## References

1. L. Narayanan, Y. Sabbagh, and A. A. Voudouris, *Diversity-Seeking Jump Games in Networks*, first posted May 28, 2023, arXiv:2305.17757; open-access journal version, *Autonomous Agents and Multi-Agent Systems* 39 (2025), article 32, DOI:10.1007/s10458-025-09714-8. https://arxiv.org/abs/2305.17757
2. T. Friedrich, P. Lenzner, L. Molitor, and L. Seifert, *Single-Peaked Jump Schelling Games*, first posted February 23, 2023, arXiv:2302.12107. https://arxiv.org/abs/2302.12107
3. Y. Li, L. Narayanan, J. Opatrny, and Y. T. Xu, *Diversity-Seeking Swap Games in Networks*, arXiv:2502.13375 (2025). https://arxiv.org/abs/2502.13375
