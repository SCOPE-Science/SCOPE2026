# Exact potential and equilibrium census for one-vacancy diversity jumps on complete bipartite graphs

## Finding

**Theorem.** Fix integers \(a,b\ge2\) and \(k\ge2\). On the labeled complete bipartite graph \(K_{a,b}\), place exactly \(a+b-1\) agents of \(k\) fixed types, one per vertex, leaving exactly one vacant vertex. An agent may jump into the vacancy, and its utility is the fraction of its **occupied** neighbors whose types differ from its own. For every type population, this finite game admits an **exact potential** (not just an ordinal potential): for all legal unilateral jumps, the change in potential equals the moving agent's utility change. Consequently, every strictly improving jump sequence terminates at a pure Nash equilibrium; one uniform coarse bound is \(4(a+b)^3\) jumps.

More precisely, write the bipartition as \(A\sqcup B\), define \(c=a-1\), \(d=b-1\), let \(R_t\) denote the total population of type \(t\) and \(x_t\) the number of its agents currently in \(A\), and let \(e_B\) be one if the vacancy lies in \(B\) and zero otherwise. Then

\[
\Psi=\frac{(c+d)\sum_{t=1}^k x_t^2-2c\sum_{t=1}^k R_t x_t+(c-d)e_B}{2cd}
\]

is an exact potential for the entire jump game, including jumps that are not improving.

For the special case of two types (blue and red), an assignment is an equilibrium **if and only if the completely occupied bipartition class is monochromatic**. With \(z\) marking the number of red agents, the exact labeled-vertex equilibrium polynomial (agents of a given color are not individually distinguished) is

\[
E_{a,b}(z)=a(1+z)^{a-1}(1+z^b)+b(1+z)^{b-1}(1+z^a).
\]

There are exactly \(a2^a+b2^b\) such profiles out of \((a+b)2^{a+b-1}\) vacancy-and-type profiles. Thus the equilibrium fraction on \(K_{m,m}\) is \(2^{1-m}\), while for fixed \(a\) and \(b\to\infty\), it tends to \(2^{1-a}\).

## Assumptions and scope

* The graph is the **simple** undirected complete bipartite graph with distinguishable vertices, parts of orders \(a,b\ge2\), and exactly one vacancy. All agents are allowed to jump and have fixed immutable types. Type counts may be arbitrary nonnegative integers summing to \(a+b-1\), with at most \(k\) types represented.
* Each occupied agent's utility is \(u_i(C)=\#\{\text{occupied opposite-type neighbors}\}/\#\{\text{occupied neighbors}\}\). Every occupied vertex has at least one occupied neighbor because both parts have at least two vertices and only one vertex is empty. After a jump, the old vertex becomes empty and the destination becomes occupied.
* An improving jump requires **strictly** greater utility. The pure Nash condition is no profitable jump. No updating of types, swapping, random migration, or secondary positional preferences is included.
* The polynomial counts vertex colorings with a marked vacancy. If agents of a given type are distinct individuals, multiply the coefficient for red count \(r\) by \(r!(a+b-1-r)!\) to count individual labeled-agent placements.

## Proof

Fix \(c=a-1\), \(d=b-1\), so \(c,d\ge1\). Write \(j_t=R_t-x_t\). Let \(F=2cd\Psi\), the integer numerator in the theorem.

**Jump within the same part.** A same-part jump exchanges an agent with the sole vacancy in its own part. Every agent in that part sees the same occupied opposite part before and after the move, so the mover's utility is unchanged. All \(x_t\) and \(e_B\) are unchanged, so \(\Delta F=0=2cd\,\Delta u\).

**Jump from \(B\) to a vacancy in \(A\).** Before the jump, \(A\) contains \(c\) agents; afterwards \(B\) contains \(d\). For a type-\(t\) agent, its old utility and new utility are

\[
u_{\mathrm{old}}=1-\frac{x_t}{c},\qquad
u_{\mathrm{new}}=1-\frac{j_t-1}{d}.
\]

Here \(x_t\) increases to \(x_t+1\) and \(e_B\) increases from zero to one. Direct substitution gives

\[
\Delta F=(c+d)(2x_t+1)-2cR_t+(c-d)
=2\bigl(dx_t-c(j_t-1)\bigr)
=2cd\,(u_{\mathrm{new}}-u_{\mathrm{old}}).
\]

**Jump from \(A\) to a vacancy in \(B\).** Before the jump, \(B\) contains \(d\) agents; afterwards \(A\) contains \(c\). The type-\(t\) mover has

\[
u_{\mathrm{old}}=1-\frac{j_t}{d},\qquad
u_{\mathrm{new}}=1-\frac{x_t-1}{c}.
\]

Now \(x_t\) decreases to \(x_t-1\) and \(e_B\) decreases from one to zero; hence

\[
\Delta F=(c+d)(-2x_t+1)+2cR_t-(c-d)
=2\bigl(cj_t-d(x_t-1)\bigr)
=2cd\,(u_{\mathrm{new}}-u_{\mathrm{old}}).
\]

These exhaust all jumps and prove exactness. Since the state space is finite, strict improvement strictly increases \(F\) and cannot cycle. Every maximal improvement sequence therefore ends at an equilibrium. Moreover \(F\) is integral, every strict increase is at least \(2\), and with \(N=a+b\),

\[
|F|\le(N-2)a^2+2(a-1)(N-1)a+N\le3N^3+N.
\]

The number of strict increases is therefore at most \(3N^3+N<4N^3\), as claimed.

**Two-type equilibrium classification.** Suppose the vacancy is in \(A\), so \(B\) has \(b=d+1\) occupied vertices. Let \(x\) and \(j\) be red counts in \(A\) and \(B\). If \(0<j<b\), both colors occur in \(B\). Stability against a red agent jumping from \(B\) requires \(dx\le c(j-1)\); stability against a blue agent jumping from \(B\) requires \(d(c-x)\le c(b-j-1)\). Adding gives \(dc\le c(b-2)=c(d-1)\), impossible. Thus \(B\) must be monochromatic.

Conversely, if \(B\) is monochromatic, every agent of \(B\) that jumps into \(A\) sees only agents of its own type, obtaining utility zero; no such jump is strictly beneficial. Every same-part jump also preserves utility. Hence the profile is stable. Interchanging \(A\) and \(B\) proves the iff condition for either vacancy location.

If the vacancy is in \(A\), there are \(a\) choices of its vertex, \((1+z)^{a-1}\) for the red subset of the other \(A\)-vertices, and \(1+z^b\) for the monochromatic \(B\). The symmetric contribution for a vacancy in \(B\) is \(b(1+z)^{b-1}(1+z^a)\). These disjoint cases prove the polynomial and its consequences upon setting \(z=1\). All quantified assertions are proved for every \(a,b,k\) in the stated ranges.

## Verification

The standalone Python 3 checker `check_potential.py` uses exact rational arithmetic for utilities and computes utility changes by independently reconstructing the occupied opposite neighborhoods. It exhausts all vacancy positions and type profiles for \(2\le a,b\le4\) and \(k\in\{2,3\}\), checking every unilateral jump, including non-improving jumps, and independently enumerates two-type equilibria. Its execution returned `PASS`, with \(35{,}682\) states, \(225{,}302\) legal jumps, and \(18\) parameter combinations checked. On \(K_{3,4}\) it counts \(88\) equilibria among \(448\) profiles. These finite checks corroborate, but do not replace, the universal algebraic proof above. Run with `python3 check_potential.py`; no third-party dependencies are required.

## Relationship to prior work

Narayanan, Sabbagh, and Voudouris introduced this fractional diversity-seeking jump model in 2023. Their Theorem 5.1 establishes a potential for **regular graphs** with one vacancy; their discussion explicitly raises bipartite graph classes as a further direction. When \(a=b\), \(K_{a,b}\) is regular, so potential-game *existence* is already covered by that result. The new content here is the **explicit exact** potential for arbitrary possibly unequal \(a,b\), together with a uniform polynomial improvement bound and the two-type equilibrium distribution.

Narayanan, Opatrny, Tummala, and Voudouris (2025) establish one-vacancy potential results for **variety-seeking** jump games; their utility counts **distinct other types** rather than the **fraction of occupied other-type neighbors**. These utilities differ even for two types whenever an agent has both same- and different-type neighbors, so their theorem does not imply the present exact potential identity. Bilò et al. (2022) study **single-peaked swap** games with no vacancy, rather than one-vacancy jumps with monotonically diversity-seeking utilities.

## Limitations

The result does not extend by proof to arbitrary bipartite graphs or more than one vacancy, and it does not bound mixing times or characterize welfare-optimal equilibria. The polynomial is a two-type result; for three or more types the exact potential still holds but no corresponding closed equilibrium-count polynomial is claimed. Only labeled-vertex color configurations, not permutations of indistinguishable-type agents, are counted by \(E_{a,b}\). Equivalence to an unlocated more general potential theorem in other literature has not been ruled out. All assessments described here concern mathematical evidence and are not independent validation.

## References

1. L. Narayanan, Y. Sabbagh, and A. A. Voudouris, *Diversity-Seeking Jump Games in Networks*, first publicly available 2023-05-28, arXiv:2305.17757, especially Sections 2, 5 and 7. https://arxiv.org/abs/2305.17757
2. L. Narayanan, J. Opatrny, S. Tummala, and A. A. Voudouris, *Variety-Seeking Jump Games on Graphs*, arXiv:2505.10005 (2025), especially Sections 2 and 3. https://arxiv.org/abs/2505.10005
3. D. Bilò, V. Bilò, P. Lenzner, and L. Molitor, *Tolerance Is Necessary for Stability: Single-Peaked Swap Schelling Games*, arXiv:2204.12599 (2022). https://arxiv.org/abs/2204.12599
