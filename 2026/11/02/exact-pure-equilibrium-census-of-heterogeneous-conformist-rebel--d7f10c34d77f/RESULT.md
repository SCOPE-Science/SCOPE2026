# Exact pure-equilibrium census of heterogeneous conformist–rebel cycles

## Finding

**Theorem.** Let \(n\ge3\) labeled players occupy the vertices of the simple cycle \(C_n\). Each is either a conformist or a rebel, at least one player is a rebel, and every player chooses one of \(m\ge3\) common actions. A conformist earns one per adjacent player choosing the same action; a rebel earns one per adjacent player choosing a different action. Write the cyclic type word as
\[
R C^{\ell_1} R C^{\ell_2}\cdots R C^{\ell_r},\qquad
r\ge1,\quad \ell_j\ge0,\quad r+\sum_{j=1}^r\ell_j=n.
\]
The number \(N\) of labeled pure-strategy Nash equilibrium profiles is zero if any \(\ell_j=1\). Otherwise define \(q=m-1\),
\[
F_0(z)=1,\quad
F_\ell(z)=\sum_{h=0}^{\lfloor(\ell-2)/2\rfloor}
{\ell-2-h\choose h}z^h\quad(\ell\ge2),
\qquad B=\sum_{j=1}^r b(\ell_j),
\]
where \(b(0)=1\) and \(b(\ell)=2\) for \(\ell\ge2\). Then
\[
\boxed{N=q^B\prod_{j=1}^r F_{\ell_j}(q)
+(-1)^Bq\prod_{j=1}^r F_{\ell_j}(-1).}
\]
More finely, let \(a_t=[z^t]z^B\prod_jF_{\ell_j}(z)\). Exactly
\[
a_t\bigl(q^t+(-1)^tq\bigr)
\]
equilibrium profiles have precisely \(t\) cycle edges joining *different* actions. The count depends only on the multiset of conformist-run lengths, not their cyclic order. It can be evaluated in \(O(n)\) integer-arithmetic operations using \(F_2(z)=F_3(z)=1\) and \(F_\ell(z)=F_{\ell-1}(z)+zF_{\ell-2}(z)\) for \(\ell\ge4\).

For a concrete infinite family, on a cycle with cyclic type word \((RCCCC)^r\), using three actions gives exactly \(12^r\) pure equilibria, or a fraction \((4/81)^r\) of all action profiles.

## Assumptions and scope

The vertices and actions are labeled. The graph is a simple undirected cycle, so \(n\ge3\); everyone has exactly two distinct neighbors. The set of available actions is common to all players, with \(m\ge3\). All payoffs are additive over the two incident edges with unit positive weight, exactly as in the multi-strategy conformist–rebel model. No players have fixed/stubborn actions. At least one rebel is present. No claim is made for two-action games, all-conformist cycles, directed or weighted networks, or equilibrium refinements other than pure-strategy Nash equilibrium. Tied best responses count as equilibria because only *strict* profitable deviation is prohibited.

## Proof

**1. Local best responses.** A rebel sees at most two distinct neighbor actions. Since at least three actions are available, an action used by neither neighbor gives payoff two, the largest possible. The rebel is best-responding if and only if both incident edges have unequal endpoint actions. A conformist's largest possible payoff is at least one, attained by adopting a neighbor's action, so the conformist is best-responding if and only if at least one incident edge has equal endpoint actions.

**2. Equal-action edges.** Let \(Z\) be the exact set of cycle edges with equal endpoint actions. By the preceding equivalence, no edge of \(Z\) touches a rebel and every conformist vertex is covered by an edge of \(Z\). Between consecutive rebels there are \(\ell\) conformists. For \(\ell=0\), the connecting rebel–rebel edge is necessarily unequal. For \(\ell=1\), that isolated conformist has no conformist neighbor, so there are no equilibria. For \(\ell\ge2\), the first and last of the \(\ell-1\) conformist–conformist edges must belong to \(Z\), and the unselected interior edges cannot be consecutive. Indeed an unselected pair surrounding one conformist would leave that vertex uncovered; conversely the stated conditions cover every conformist.

There are \(\ell-3\) potentially unselected interior edges. Choosing precisely \(h\) nonconsecutive positions among them gives \({\ell-2-h\choose h}\) possibilities: shift the ordered chosen positions left by \(0,1,\ldots,h-1\) to choose \(h\) ordinary positions from \(\ell-2-h\). Each such choice creates \(2+h\) unequal edges along this rebel-to-rebel segment, while a segment with \(\ell=0\) creates one unequal edge. Thus \(z^B\prod_jF_{\ell_j}(z)\) is precisely the generating polynomial of permissible equality/inequality edge patterns, with exponent counting unequal edges. In particular \(B\ge2\) for every feasible type word in this theorem.

**3. Action labels on contracted blocks.** Fix a permissible edge pattern with \(t\ge2\) unequal edges. Contract each maximal path of equal-action edges. There are exactly \(t\) contracted action blocks around a circle. Adjacent blocks must have distinct labels; nonadjacent blocks have no constraint. The number of assignments from the \(m\) actions is the cycle chromatic count
\[
\chi_t(m)=(m-1)^t+(-1)^t(m-1).
\]
The identity follows from the ordinary cycle chromatic polynomial when \(t\ge3\), and for \(t=2\) both boundary edges between the same two blocks demand inequality, giving \(m(m-1)=(m-1)^2+(m-1)\). The contracted block colors determine exactly one original action profile, and every equilibrium gives one unique edge pattern. Therefore the number of equilibria with \(t\) changes is \(a_t\chi_t(m)\).

**4. Summation and consequences.** Writing \(q=m-1\), sum the counts over \(t\):
\[
N=\sum_t a_t(q^t+(-1)^tq)=
q^B\prod_jF_{\ell_j}(q)+(-1)^Bq\prod_jF_{\ell_j}(-1).
\]
As the product is commutative, the count is invariant under permutations of run lengths, even when those permutations change the labeled type word beyond cycle rotation/reflection. The polynomial recurrence follows from the independent-choice decision at the final interior edge; equivalently it follows from Pascal's identity in the displayed binomial sum. Its evaluation for each run uses a number of arithmetic operations linear in that run's length, yielding \(O(n)\) overall.

For the repeated block \((RCCCC)^r\), every run length is four, so \(B=2r\), \(F_4(z)=1+z\), \(F_4(2)=3\), and \(F_4(-1)=0\). The exact count is \(2^{2r}3^r=12^r\), and the total number of three-action profiles is \(3^{5r}\), establishing the claimed proportion. \(\square\)

## Verification

Run \(\texttt{python3 verify.py}\) using Python 3 standard-library modules only. The included program directly evaluates every player's possible deviating actions for 667 labeled type-pattern cases, spanning three through eight vertices and three through five actions, comprising 2,406,873 complete strategy profiles. It separately evaluates the local-equilibrium characterization for 1,252 cases through nine vertices, comprising 14,438,529 profiles. It checks the repeated-block formula for one through eight blocks and distinct run-order configurations. All comparisons use exact integers. These finite checks validate the tested ranges; the proof above covers every finite \(n\) and \(m\) in scope.

## Relationship to prior work

Pei, Cao and Zhang, *Equilibria in heterogeneous multi-strategy network games* (first available 13 July 2026), define the same conformist/rebel payoff model. Their Theorem 4 provides the existence criterion for ring networks with at least three actions: no conformist may have only rebel neighbors. The criterion agrees with the zero/nonzero boundary here, but does not count action profiles, give a run-multiset invariance, or give a disagreement-edge distribution. Cao, Sanchez and Zhang, *Network games with heterogeneous players* (2026), study a binary-action heterogeneous model, so their results do not imply the multi-action counts in this theorem.

The familiar cycle chromatic polynomial and path independent-set binomial counts are classical building blocks, not claimed as discoveries. The contribution is their exact combination through the heterogeneous Nash best-response constraints, yielding all run-length-specific counts and the order-invariance statement. The two-choice ladder-game counting literature concerns different graph geometry and player payoffs.

## Limitations

The theorem does not count mixed equilibria or dynamic basins of attraction, and does not extend without modification to \(m=2\): a rebel with two differently colored neighbors then cannot avoid both, invalidating the local characterization. Adding stubborn agents, heterogeneous link weights or directed interactions changes the permitted equality patterns. The literature comparison is a best-knowledge search rather than proof of absolute publication priority; unindexed equivalents or results phrased as constrained spin-coloring/transfer-matrix enumerations may exist. Computational checks are finite and not a substitute for the unrestricted argument.

## References

1. S. Pei, W. Cao and B. Zhang, *Equilibria in heterogeneous multi-strategy network games*, arXiv:2607.10997 (v1 posted 13 July 2026; v2 posted September 2026). https://arxiv.org/abs/2607.10997 . Model, §2; ring criterion, Theorem 4 in §4.2.
2. W. Cao, A. Sanchez and B. Zhang, *Network games with heterogeneous players*, arXiv:2607.05932 (first posted 7 July 2026). https://arxiv.org/abs/2607.05932 . Binary-action background and scope.
3. J. Lee and H. Shin, *The chromatic polynomial for cycle graphs*, arXiv:1907.04320 (2019). https://arxiv.org/abs/1907.04320 . Classical cycle-coloring identity.
4. V. Sánchez Muñoz and M. Mc Gettrick, *Nash Equilibria in certain two-choice multi-player games played on the ladder graph*, arXiv:2101.09103 (2021). https://arxiv.org/abs/2101.09103 . Distinct network/counting setting.
