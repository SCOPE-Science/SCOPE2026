# Directed-cycle partitions determine and extremize two-step metapopulation extinction

## Finding

For a discrete extinction–recolonization model on \(n\ge2\) identical habitat patches, suppose each patch has exactly one distinct incoming and one distinct outgoing directed dispersal connection, and all patches are initially occupied. Let \(e\in(0,1)\) be the independent local-extinction probability and \(c\in(0,1]\) the independent colonization probability per eligible dispersal connection. If the directed permutation of patches has cycle lengths \(\ell_1,\ldots,\ell_k\ge2\), summing to \(n\), the probability \(P_2\) of complete extinction by the end of the second update is exactly

\[
P_2=\prod_{j=1}^{k}\left(\lambda_+^{\ell_j}+\lambda_-^{\ell_j}\right),\quad
\lambda_\pm=\frac{s\pm\sqrt{s^2-4d}}2,\quad
s=e(2-e),\quad d=ce^2(1-e)^2.
\]

The roots obey \(0<\lambda_-<\lambda_+\). Writing \(\rho=\lambda_-/\lambda_+\in(0,1)\), an exact, strictly ordered classification follows:

- Among **all** such networks on \(n\) patches, the single directed \(n\)-cycle uniquely minimizes \(P_2\) up to relabeling. The maximum is attained uniquely up to relabeling by \(n/2\) reciprocal two-cycles when \(n\) is even, or by \((n-3)/2\) reciprocal two-cycles and one directed three-cycle when \(n\) is odd.
- Fix exactly \(m\) reciprocal two-cycles, so that \(R=n-2m\) equals zero or is at least three. The minimum within this class uses one remaining \(R\)-cycle (when \(R>0\)). The maximum uses remaining directed cycles of length three, with at most one cycle of length four or five: if \(R=3q\), take \(q\) three-cycles; if \(R=3q+1\), take \(q-1\) three-cycles and one four-cycle; and if \(R=3q+2\), take \(q-1\) three-cycles and one five-cycle. For \(R=0\), the only cycle multiset consists of the \(m\) two-cycles.
- For known \(n,e\), the entire response curve \(c\mapsto P_2(c)\) on any nonempty open subinterval of \((0,1)\) uniquely determines the complete multiset of directed cycle lengths, including counts. A single measured probability at one \(c\) is not asserted to determine that multiset.

The probability after just one update is always \(P_1=e^n\). Thus two updates are the earliest possible point at which this model's fully occupied initial state can distinguish dispersal arrangements.

## Assumptions and scope

At each synchronous update, (i) each currently occupied patch independently goes locally extinct with probability \(e\); (ii) each empty patch (including one just emptied) independently becomes occupied with probability \(c\) if its unique incoming neighbor survived the extinction substep. No patch recolonized during the same update can transmit until a later update. All random extinction and eligible colonization coins are conditionally independent. The patch network has no self-connections: its connection map is a fixed-point-free permutation. There are no empty patches initially, no immigration from outside, and no common environmental shocks.

\(P_2\) is the **unconditional cumulative probability of global extinction by the end of two updates** from the fully occupied initial state. Extinction is absorbing, so this also equals the probability of global extinction at the end of update two. It is not an expected extinction time, infinite-horizon persistence threshold, or stationarity statistic. All strict inequalities and uniqueness statements concern cycle multisets (network relabelings are equivalent). The boundary \(c=0\) is excluded because cycle distinctions collapse there.

## Proof

**1. Probability reduction.** Let \(S_i\in\{0,1\}\) indicate that initially occupied patch \(i\) survives the extinction substep of the first update. These indicators are independent with \(\Pr(S_i=1)=1-e\). Let \(X_i\) indicate occupation at the end of the first update. Given \(X\), complete extinction in the second update occurs if and only if every occupied patch becomes extinct in its extinction substep: if any patch survives, at least that patch remains occupied; if none survives, there is no source for recolonization. Its conditional probability is therefore \(e^{\sum_i X_i}\). Thus

\[
P_2=\mathbb E\left[e^{\sum_i X_i}\right].
\]

Given the first-step survival vector \(S\), the colonization outcomes at different patches are independent. With \(s=S_{\mathrm{pred}(i)}\) and \(t=S_i\), the weight \(\Pr(S_i=t)\,\mathbb E[e^{X_i}\mid S_i=t,S_{\mathrm{pred}(i)}=s]\) equals the corresponding entry in

\[
T=\begin{pmatrix}
e&e(1-e)\\
e\bigl[1-c(1-e)\bigr]&e(1-e)
\end{pmatrix},
\]

with rows indexed by \(s=0,1\) and columns by \(t=0,1\). For example, if \(s=1,t=0\), an empty patch remains empty with probability \(1-c\) or recolonizes with probability \(c\), giving the factor \(e[(1-c)+ce]\). On a directed cycle of length \(\ell\), summing over all \(S\) choices gives \(\operatorname{tr}(T^\ell)\), since the predecessor status at each edge is the preceding vertex's status. Different cycles have disjoint independent coins, so their factors multiply. The trace and determinant of \(T\) are \(s=e(2-e)\) and \(d=ce^2(1-e)^2\). The discriminant is strictly positive: for \(c\le1\),

\[
s^2-4d\ge e^3(4-3e)>0.
\]

Also \(s>0\) and \(d>0\), hence both eigenvalues are distinct and strictly positive. The Cayley–Hamilton recurrence \(u_0=2\), \(u_1=s\), \(u_\ell=s u_{\ell-1}-d u_{\ell-2}\) yields \(u_\ell=\lambda_+^\ell+\lambda_-^\ell\), proving the product formula.

**2. Strict partition extremizers.** For positive integers \(a,b\ge2\), splitting one directed \((a+b)\)-cycle into separate \(a\)- and \(b\)-cycles changes the normalized factor from \(1+\rho^{a+b}\) to

\[
(1+\rho^a)(1+\rho^b)=1+\rho^{a+b}+\rho^a+\rho^b>1+\rho^{a+b}.
\]

Therefore merging all cycles strictly reduces \(P_2\), giving the unique all-network minimum. Conversely, split every cycle of length at least four into a two-cycle and a remaining cycle of length at least two. After this operation, all lengths are two or three. Replacing two three-cycles with three two-cycles again strictly raises \(P_2\), because \(f(\ell)=\log(1+\rho^\ell)\) is positive and strictly decreasing, so \(3f(2)>2f(3)\). This establishes the unique all-network maximum.

At fixed number \(m\) of two-cycles, only the remaining cycles of lengths at least three can change. Merging them strictly decreases \(P_2\) and gives the minimum. For the maximum, split any remaining cycle of length at least six into a three-cycle and another cycle of length at least three; splitting strictly increases the value. Thus only lengths three, four, and five remain. The function \(f(x)=\log(1+\rho^x)\) is strictly decreasing and strictly convex for real \(x>0\), since with \(L=-\log\rho>0\),

\[
f''(x)=\frac{L^2e^{-Lx}}{(1+e^{-Lx})^2}>0.
\]

Two fours can be replaced by a three and a five, strictly increasing the sum of \(f\) by convexity. A four and a five can be replaced by three threes, strictly increasing it because \(3f(3)>f(4)+f(5)\). Two fives can be replaced by two threes and a four, strictly increasing it because \(2f(3)+f(4)>2f(5)\). Therefore at most one four or five remains, and the residue of \(R\) modulo three fixes precisely the claimed extremal partition. Every transformation is strict for \(0<\rho<1\), so no other cycle multiset ties.

**3. Reconstruction from a response curve.** For known \(n,e\), the eigenvalues and \(\rho\) are explicit known functions of \(c\). On \((0,1)\), \(d=ce^2(1-e)^2\) increases strictly, \(\lambda_-\) increases and \(\lambda_+\) decreases, so \(\rho(c)\) is strictly increasing. Dividing by \(\lambda_+(c)^n\) exposes the polynomial

\[
H(z)=\prod_j(1+z^{\ell_j})\quad\text{at }z=\rho(c).
\]

Two networks producing identical response curves on any nonempty open interval must have identical polynomials \(H\), because a nonzero polynomial cannot vanish on an interval. The least positive exponent in \(H\) is its shortest cycle length \(r\), and the coefficient of \(z^r\) equals the multiplicity of that length. Divide by \((1+z^r)\) that many times and repeat. This recursively recovers the whole cycle multiset. No independence or identifiability claim is made for a finite collection of response measurements.

**4. Exact same-summary-metrics example.** For eight patches, \(e=1/2\) and \(c=1\), the cycle-trace recurrence has \(s=3/4\), \(d=1/16\). It gives

\[
P_2(8)=\frac{2207}{65536},\qquad
P_2(4,4)=\frac{2209}{65536},\qquad
P_2(3,5)=\frac{2214}{65536}.
\]

All three directed networks have one incoming and one outgoing link at each vertex, no reciprocal pair, dispersal symmetry index zero, and adjacency spectral radius one. Their different two-step risks therefore cannot be inferred from those shared coarse descriptors alone.

## Verification

A self-contained Python 3 standard-library checker is supplied at `verification/check_cycle.py`. Execute `python3 verification/check_cycle.py` from the package root. It uses rational arithmetic throughout and reports 12,767 passing assertions: independent enumeration of first-step survival/colonization outcomes for all cycle partitions with two to seven vertices and three interior/boundary parameter pairs; exact partition optimization across two to eighteen vertices, including fixed two-cycle counts; polynomial cycle reconstruction across two to twenty-two vertices; and the exact eight-patch fractions above. These finite enumerations verify examples and proof algebra but are not substitutes for the arbitrary-\(n\) arguments in the proof.

## Relationship to prior work

Kleinhans and Jonsson [1] give the same synchronous stochastic extinction–recolonization transition rule, analyze regular directed networks, and relate connectivity, dispersal symmetry, and long-horizon persistence. Their November 4, 2010 public preprint is the dated source for this model. The contribution here is the exact arbitrary-size two-step risk law, the complete unconstrained and reciprocity-constrained cycle-partition orderings, and reconstruction of cycle lengths from a parameter-response curve—not the underlying model or the fact that network cycles can affect persistence.

Bode, Burrage and Possingham [2] analyze stochastic occupancy persistence using directed-network metrics and finite-state calculations, but the inspected author-posted full text focuses on longer-horizon network viability and does not state these all-permutation two-step formulas. Artzy-Randrup and Stone [3] investigate cycles and persistence thresholds in a different age-structured population model; their spectral threshold results do not determine the two-step stochastic extinction probability considered here. Vuilleumier and Possingham [4] study asymmetric recolonization by simulation, with no inspected exact cycle-partition classification. A related later analysis by Shtilerman and Stone [5] was identified but its complete text could not be inspected; historical priority is consequently not certified.

## Limitations

The theorem concerns exactly two synchronous updates of an initially fully occupied, homogeneous, fixed-point-free one-in/one-out network. It does not extend by assertion to third or later update, heterogeneous patch properties, other graph degrees, correlated disturbances, continuous time, or realized ecological systems. All equalities and extremizers depend on the stated event order. The fixed-two-cycle constraint applies only to feasible \(R=0\) or \(R\ge3\). The identifiability result presumes a **known response function on an interval**, not a single noisy observation. Comparison with one highly relevant later source remained incomplete owing to full-text access; the originality assessment is provisional.

## References

1. D. Kleinhans and P. R. Jonsson, *On the impact of dispersal asymmetry on metapopulation persistence*, preprint first publicly posted 2010-11-04, https://arxiv.org/abs/1011.1109 ; later *Journal of Theoretical Biology*, DOI: https://doi.org/10.1016/j.jtbi.2011.09.002 .
2. M. Bode, K. Burrage and H. P. Possingham, *Using complex network metrics to predict the persistence of metapopulations with asymmetric connectivity patterns*, *Ecological Modelling* 214 (2008), 201–209, https://doi.org/10.1016/j.ecolmodel.2008.02.040 .
3. Y. Artzy-Randrup and L. Stone, *Connectivity, cycles, and persistence thresholds in metapopulation networks*, *PLoS Computational Biology* 6 (2010), e1000876, https://doi.org/10.1371/journal.pcbi.1000876 .
4. S. Vuilleumier and H. P. Possingham, *Does colonization asymmetry matter in metapopulations?*, *Proceedings of the Royal Society B* 273 (2006), 1637–1642, https://doi.org/10.1098/rspb.2006.3469 .
5. E. Shtilerman and L. Stone, *The effects of connectivity on metapopulation persistence: network symmetry and degree correlations*, *Proceedings of the Royal Society B* (2015), https://doi.org/10.1098/rspb.2015.0203 .
