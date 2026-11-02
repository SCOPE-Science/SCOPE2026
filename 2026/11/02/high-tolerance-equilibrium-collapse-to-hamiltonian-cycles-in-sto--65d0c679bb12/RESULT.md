# High-tolerance equilibrium collapse to Hamiltonian cycles in stochastic default delegation

## Finding

For the stochastic default-delegation game described below, let the common independent probability of casting be \(p\in(0,1)\), put \(q=1-p\), and let \(D>0\) be the diameter of the voters' positions. For every \(n\ge2\), the explicit **high-tolerance condition**

\[
\tau > T_n(D,p):=\frac{Dq(1-q^{n-1})}{p q^{n-1}}
\]

implies that the pure Nash equilibria are **exactly the directed Hamiltonian cycles**, one default delegate per voter. There are exactly \((n-1)!\) such labeled profiles. At every equilibrium, every voter is represented whenever at least one voter casts; hence expected lost votes equal the global minimum \(nq^n\). The sufficient bound \(T_n\) is **not asserted to be a sharp threshold for arbitrary positions**.

For the three-voter instance with positions \((0,h,2h)\), where \(h>0\), \(2h\le1\), and \(\tau>2h\), put \(\tau_c=h(1+1/q)\). The equilibrium sets have the exact phase diagram

\[
\begin{array}{c|c}
2h<\tau<\tau_c&\{(1,0,1),(1,2,1)\}\\
\tau=\tau_c&\{(1,0,1),(1,2,1),(1,2,0),(2,0,1)\}\\
\tau>\tau_c&\{(1,2,0),(2,0,1)\}.
\end{array}
\]

Here a tuple is the vector of delegates, with voters labeled \(0,1,2\). Thus for three equally spaced voters, the transition from two adjacent mutual-delegation components with a tail to full Hamiltonian cycles is sharp, including its tie case.

## Assumptions and scope

There are \(n\ge2\) labeled voters at distinct positions \(x_i\in[0,1]\), with diameter \(D=\max_{i,j}|x_i-x_j|>0\). Each casts independently with the same probability \(p\in(0,1)\). Every voter names exactly one default delegate, including herself if desired, so a delegation profile is a function \(d:[n]\to[n]\). Delegation follows pointers until the first casting voter is reached or a repeated voter would occur, as in the default-delegation model of Brill et al. All voters use the common tolerance \(\tau>0\), and relative opinion loss is absolute distance.

For voter \(i\), write her forward orbit of **distinct** vertices as \(y_0=i,y_1=d(i),\ldots,y_{\ell_i-1}\), stopping immediately before the first repetition. Her expected utility is

\[
U_i(d)=p\sum_{r=0}^{\ell_i-1}q^r\bigl(\tau-|x_i-x_{y_r}|\bigr).
\]

A pure Nash equilibrium is a profile in which no voter can increase her own utility by changing only her named default delegate. The proof uses the exact finite functional-digraph model, not a continuum approximation. For the main theorem, position distinctness only guarantees a positive diameter; the algebra remains valid for repeated positions if a positive diameter is retained.

## Proof

**1. Orbit length dominates opinion distance.** Separating the tolerance term gives

\[
U_i(d)=\tau(1-q^{\ell_i})-E_i(d),\qquad
E_i(d)=p\sum_{r=1}^{\ell_i-1}q^r|x_i-x_{y_r}|.
\]

Every orbit has length between \(1\) and \(n\). Uniformly in \(i,d\),

\[
0\le E_i(d)\le pD\sum_{r=1}^{n-1}q^r
=Dq(1-q^{n-1})=:B.
\]

If two possible choices of a single voter's delegate give orbit lengths \(\ell'<\ell''\), the first term's advantage for the longer orbit is

\[
\tau(q^{\ell'}-q^{\ell''})
\ge \tau p q^{n-1}>B.
\]

The two distance penalties can reduce this advantage by at most \(B\), since each lies in \([0,B]\). Therefore, under \(\tau>T_n(D,p)=B/(pq^{n-1})\), **every unilateral change increasing that voter's orbit length strictly increases her utility**, regardless of its distance consequences. Likewise, any unilateral change reducing orbit length strictly decreases her utility.

**2. Functional-graph improvement lemma.** Every function on a finite set consists of directed cycles with rooted in-trees feeding into them. If a profile is not a directed Hamiltonian cycle, some vertex can increase the number of distinct vertices in her forward orbit by redirecting her sole outgoing arc.

If an off-cycle vertex exists, choose an off-cycle vertex \(t\) whose forward path first reaches a cycle at vertex \(c\). Let \(a\) be the cycle predecessor of \(c\), so currently \(d(a)=c\). Redirect \(a\) to \(t\). The orbit of \(a\) now traverses \(a\), the off-cycle path from \(t\) to \(c\), and then all remaining cycle vertices before returning to \(a\). It is strictly longer than its previous orbit, which contained only that cycle.

Otherwise, every vertex lies on a directed cycle. As the graph is not Hamiltonian, there are at least two cycles. Take a vertex \(a\) on a shortest cycle of length \(s\), and redirect her arc to a vertex \(b\) of another cycle of length \(t\ge s\). Her new orbit visits \(a\) followed by the entire other cycle, of length \(1+t>s\). This proves the lemma.

**3. Exact equilibrium classification.** Under the high-tolerance inequality, the lemma makes every non-Hamiltonian profile unstable. Conversely, a directed Hamiltonian cycle gives every voter an orbit of maximum possible length \(n\). A unilateral change that changes its profile either leaves an orbit with fewer than \(n\) distinct vertices (because its new arc is a chord/self-loop into the already visited cycle) or is not a change. By step 1, no such change can improve utility. Therefore the equilibria are precisely the Hamiltonian cycles. Fixing one vertex as the starting label gives \((n-1)!\) possible cyclic orders.

**4. Vote-loss optimality.** Independently of the delegation profile, the event that none of the \(n\) voters casts has probability \(q^n\); in that event all \(n\) votes are lost. Expected lost votes therefore are at least \(nq^n\). In a directed Hamiltonian cycle, if any voter casts, every other voter eventually reaches a casting voter by following the cycle, so no votes are lost. Thus equality holds at every equilibrium under the high-tolerance condition.

**5. Sharp three-voter phase diagram.** Scale \(h\) out of the distances, leaving \(x=(0,h,2h)\), and assume \(\tau>2h\). Any self-looping voter can strictly improve by delegating to another voter: doing so adds at least one distinct positively valued candidate to an orbit previously consisting only of herself. Thus any equilibrium has no self-loop, leaving only \(2^3=8\) possible profiles. Four profiles are immediately unstable by explicit nearer-neighbor reroutings: in \((1,0,0)\), voter 2 switches from 0 to 1 and gains \(p^2qh\); in \((2,2,1)\), voter 0 switches from 2 to 1 and gains \(p^2qh\); in \((2,0,0)\), voter 0 switches from 2 to 1 and gains \(pqh\); in \((2,2,0)\), voter 2 switches from 0 to 1 and gains \(pqh\). These gains are all strictly positive for admissible parameters.

The remaining four profiles are the adjacent-pair configurations \((1,0,1),(1,2,1)\) and two Hamiltonian cycles \((1,2,0),(2,0,1)\). For either adjacent-pair profile, the only potentially profitable orbit-expanding deviation adds a third vertex at an additional expected opinion penalty; its payoff advantage (new minus old) equals

\[
pq\bigl(q(\tau-h)-h\bigr).
\]

For either Hamiltonian profile, its only potentially profitable shortening deviation has precisely the negative of this expression. Any alternative deviation in these four profiles has nonpositive utility change, by the distance ordering and positivity of \(\tau-|x_i-x_j|\). Consequently an adjacent-pair profile is Nash iff \(q(\tau-h)\le h\), and a Hamiltonian profile is Nash iff \(q(\tau-h)\ge h\). Solving equality yields \(\tau_c=h(1+1/q)\), establishing all three regimes and the tie boundary.

## Verification

The accompanying standalone Python program `verify.py` uses `fractions.Fraction` throughout, enumerates every delegation function for population sizes \(n=2,3,4,5\), three casting-probability settings per size, and computes every individual best-response comparison. It also enumerates the sharp three-person phase diagram at 15 exact-rational parameter settings, including the boundary. Reproducing the script gives:

`VERIFY_OK exact_homogeneous_profiles=10236 exact_deviation_comparisons=197226 cycle_equilibria=99 three_voter_phases=15`

All computed equilibria match the theorem. These finite experiments are independent corroboration only; the all-size theorem and continuous-parameter boundary are proved in the preceding arguments, not inferred from the enumeration.

## Relationship to prior work

Brill et al., *Cycles in Liquid Democracy: A Game-Theoretic Justification* (arXiv:2607.12610, first public 2026-07-14), introduce the relevant stochastic default-delegation game. Their Theorem 5 constrains nontrivial equilibrium components to one cycle each; Proposition 19 identifies a single full cycle as minimizing lost votes; Theorems 13–14 analyze other optimality questions. None of these statements implies that, under an explicit homogeneous high-tolerance condition, **all equilibria** are Hamiltonian cycles, nor does a lost-vote optimizer necessarily have to be a Nash equilibrium. The present result proves those additional implications and computes a sharp three-person parametric equilibrium boundary.

Earlier work by Bloembergen, Grossi, and Lackner on rational delegation (arXiv:1802.08020) and Escoffier, Gilbert, and Pass-Lanneau on iterative delegation convergence (arXiv:1904.05775) studies differently specified strategic or procedural models; those results do not immediately establish this default-delegation equilibrium classification.

## Limitations

The main sufficient tolerance bound need not be optimal. It requires a common strictly interior casting probability, nonnegative absolute-distance opinion cost, a fixed complete set of possible delegates, and no external restriction on outgoing arcs. The three-voter sharp characterization additionally assumes equal spacing and \(\tau>2h\); no claim is made for weaker tolerance, heterogeneous casting rates, or unequal opinion-spacing. The work describes pure Nash equilibria and expected unrepresented votes, not dynamics of convergence or mixed equilibria. Equivalent unindexed research may exist; independent scientific review has not been performed.

## References

- M. Brill, R. Colley, S. George, G. Lisowski, A. Papasotiropoulos, and U. Schmidt-Kraepelin, *Cycles in Liquid Democracy: A Game-Theoretic Justification*, arXiv:2607.12610, https://arxiv.org/abs/2607.12610.
- D. Bloembergen, D. Grossi, and M. Lackner, *On Rational Delegations in Liquid Democracy*, arXiv:1802.08020, https://arxiv.org/abs/1802.08020.
- L. Escoffier, H. Gilbert, and A. Pass-Lanneau, *The Convergence of Iterative Delegations in Liquid Democracy in a Social Network*, arXiv:1904.05775, https://arxiv.org/abs/1904.05775.
