# Six agents are the sharp incompatibility boundary for egalitarian versus minimum-regret Stable Roommates
## Finding
Consider the complete strict Stable Roommates problem on an even number of agents. Every agent strictly ranks every other agent, and a stable matching is a perfect matching with no blocking pair.

For a stable matching \(M\), let \(r_i(M)\) be the rank that agent \(i\) assigns to its partner. Define the egalitarian cost and regret by
\[
e(M)=\sum_i r_i(M),
\qquad
g(M)=\max_i r_i(M).
\]
Write \(E(I)\) for the stable matchings minimizing \(e\), and \(G(I)\) for those minimizing \(g\).

Every solvable instance with at most \(4\) agents satisfies
\[
E(I)\cap G(I)\ne\varnothing.
\]
This common-optimizer property is sharp: there is a complete strict \(6\)-agent instance with
\[
E(I)\cap G(I)=\varnothing.
\]

For \(4\) labeled agents there are
\[
6^4=1296
\]
complete strict profiles. Exactly \(48\) are unsolvable. Among the remaining
\[
1248
\]
profiles, the exact relation between the two optimum sets is
\[
\begin{array}{c|r}
\text{relation}&\text{profiles}\\ \hline
E=G&1176\\
E\subsetneq G&48\\
G\subsetneq E&24
\end{array}
\]
and there are no disjoint or nonnested-overlap cases.

Thus exactly
\[
72
\]
solvable four-agent profiles make the criteria disagree, an incidence of
\[
\frac{72}{1248}=\frac3{52},
\]
but every such profile still has a stable matching optimal for both criteria.

The \(72\) disagreements form exactly three isomorphism classes under simultaneous relabeling of the four agents. Each orbit has size \(24\).

Using agents \(A,B,C,D\), canonical representatives are:

1. \(A:B\succ C\succ D\), \(B:C\succ A\succ D\), \(C:D\succ B\succ A\), \(D:B\succ A\succ C\).  
   The two stable matchings are \(AB,CD\), with \((e,g)=(7,3)\), and \(AD,BC\), with \((e,g)=(8,3)\). Hence \(E\subsetneq G\).

2. \(A:B\succ C\succ D\), \(B:C\succ D\succ A\), \(C:A\succ D\succ B\), \(D:C\succ B\succ A\).  
   The two stable matchings are \(AB,CD\), with \((e,g)=(7,3)\), and \(AC,BD\), with \((e,g)=(7,2)\). Hence \(G\subsetneq E\).

3. \(A:B\succ C\succ D\), \(B:D\succ A\succ C\), \(C:B\succ A\succ D\), \(D:C\succ A\succ B\).  
   The two stable matchings are \(AB,CD\), with \((e,g)=(7,3)\), and \(AC,BD\), with \((e,g)=(8,3)\). Hence \(E\subsetneq G\).

For the sharp \(6\)-agent incompatibility witness, take
\[
\begin{aligned}
A&:F\succ E\succ D\succ B\succ C,\\
B&:F\succ C\succ D\succ A\succ E,\\
C&:E\succ A\succ B\succ F\succ D,\\
D&:B\succ E\succ A\succ F\succ C,\\
E&:A\succ B\succ D\succ C\succ F,\\
F&:C\succ A\succ E\succ D\succ B.
\end{aligned}
\]
It has exactly two stable matchings:
\[
M_G=\{AF,BC,DE\},
\qquad
(e(M_G),g(M_G))=(13,3),
\]
and
\[
M_E=\{AF,BD,CE\},
\qquad
(e(M_E),g(M_E))=(12,4).
\]
Consequently
\[
G(I)=\{M_G\},
\qquad
E(I)=\{M_E\},
\]
so the two criteria force different stable choices.

Because complete Stable Roommates instances have an even number of agents, the exhaustive two- and four-agent lower bound together with this six-agent witness proves that six is the smallest possible size for disjoint egalitarian and minimum-regret optimum sets.

## Assumptions and scope
Preference lists are complete and strict. Every acceptable pair is therefore present, and the number of agents is even.

A pair \(\{i,j\}\) blocks a perfect matching \(M\) when both \(i\) and \(j\) strictly prefer one another to their partners in \(M\).

The rank \(r_i(M)\) is one-based: an agent's first choice has rank \(1\).

The result distinguishes two thresholds. The criteria can first have different optimum sets already at \(4\) agents, but they cannot be incompatible there because the optimum sets always intersect. Disjointness first occurs at \(6\).

The four-agent statement is exhaustive. At six agents only the displayed witness is needed for sharpness; no six-agent census is claimed.

## Proof
For \(2\) agents there is one profile and one matching, so the two optimum sets coincide.

For \(4\) agents, each agent has
\[
3!=6
\]
strict preference orders, giving \(6^4=1296\) labeled profiles. For each profile, all three perfect matchings are enumerated.

Stability is checked in two independent forms. One uses precomputed rank maps; the other compares positions directly in the original preference lists. The two tests agree for every matching in every profile.

The exact distribution by number of stable matchings is
\[
48\text{ profiles with }0,\qquad
1098\text{ with }1,\qquad
150\text{ with }2.
\]
For every stable matching, \(e(M)\) and \(g(M)\) are likewise computed independently from rank maps and from direct list positions.

Comparing complete optimum sets gives
\[
1176,\ 48,\ 24
\]
profiles in the \(E=G\), \(E\subsetneq G\), and \(G\subsetneq E\) cases, respectively. No solvable four-agent profile has disjoint optimum sets.

Canonicalizing all \(72\) disagreement profiles under all \(4!\) relabelings gives exactly three classes. Each has orbit size \(24\), so every representative is asymmetric.

For the six-agent witness, all
\[
(6-1)!!=15
\]
perfect matchings are checked. Exactly the two displayed matchings are stable. Their agent-rank vectors are
\[
(1,2,3,2,3,2)
\]
for \(M_G\) and
\[
(1,3,1,1,4,2)
\]
for \(M_E\). Therefore
\[
(e(M_G),g(M_G))=(13,3),
\qquad
(e(M_E),g(M_E))=(12,4),
\]
which proves disjointness.

## Verification
The embedded `verify_sr_egal_minregret_boundary.py` uses only the Python standard library.

It verifies:
- the two-agent base case;
- every one of the \(1296\) complete strict four-agent profiles;
- two independent stability tests;
- two independent calculations of total rank and regret;
- the stable-matching count distribution \(48,1098,150\);
- the exact four-agent optimum-set relation census \(1176,48,24\);
- absence of disjoint and nonnested-overlap cases at four agents;
- exactly three disagreement orbits, each of size \(24\);
- all \(15\) perfect matchings of the six-agent witness;
- exactly two stable witness matchings;
- the exact rank vectors, total ranks, regrets, and disjoint optimum sets.

Run:

`python3 verify_sr_egal_minregret_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Egalitarian and minimum-regret stable matchings are established optimization criteria in the Stable Roommates literature. Abraham, Levavi, Manlove, and O'Malley explicitly describe the egalitarian objective as minimizing the sum of ranks and the minimum-regret objective as minimizing the maximum rank over stable matchings. Their work studies algorithmic and hardness questions for these objectives.

Simola and Manlove later study profile-based optimal Stable Roommates matchings and again place egalitarian and minimum-regret optimization in the same framework.

Those results establish the criteria and their computational significance. They do not, in the inspected material, give the smallest complete strict instance where the two optimum sets become disjoint, nor the complete four-agent relation census.

Targeted searches using the criterion names, Stable Roommates terminology, the four- and six-agent sizes, exact counts \(1176,48,24\), disjoint optimum-set language, and the witness structure did not locate an equivalent classification.

## Limitations
The result is restricted to complete strict preferences.

The exact census stops at four agents. The six-agent contribution is an explicit sharp witness, not an enumeration of all six-agent instances.

The theorem concerns the relation between the full sets of optimal stable matchings. It does not compare approximation ratios, computational complexity, or random-market asymptotics.

An unindexed thesis appendix, software test corpus, or teaching enumeration could contain the same small-instance classification.

## References
1. D. J. Abraham, A. Levavi, D. F. Manlove, and G. O'Malley, “The Stable Roommates Problem with Globally-Ranked Pairs,” in *Internet and Network Economics*, Lecture Notes in Computer Science 4858, 431–444, 2007. DOI: 10.1007/978-3-540-77105-0_48.
2. D. J. Abraham, A. Levavi, D. F. Manlove, and G. O'Malley, “The Stable Roommates Problem with Globally-Ranked Pairs,” *Internet Mathematics* 5(4), 493–515.
3. S. Simola and D. Manlove, “Profile-based optimal stable matchings in the Roommates problem,” arXiv:2110.02555, 2021.
