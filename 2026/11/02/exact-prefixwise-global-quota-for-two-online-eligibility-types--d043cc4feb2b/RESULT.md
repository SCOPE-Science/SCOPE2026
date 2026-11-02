# Exact prefixwise global quota for two online eligibility types

## Finding
Let \(N\) be a finite set of agents, and let \(S,T\subseteq N\) be two *known*, nonempty eligibility sets, which may overlap or cross. Unit-size indivisible items arrive one at a time, with each item's eligibility set equal to either \(S\) or \(T\). Every arriving item must be assigned immediately and permanently to one eligible agent. There is a deterministic online assignment algorithm such that, for *every* arrival sequence, *every* finite prefix, and *every* agent \(i\),
\[
\left\lfloor P_i\right\rfloor\le L_i\le\left\lceil P_i\right\rceil,
\qquad P_i=\frac{a}{|S|}\mathbf 1_{i\in S}+\frac{b}{|T|}\mathbf 1_{i\in T},
\]
where \(a,b\) are the numbers of the two item types seen so far and \(L_i\) is the number of items assigned to \(i\). The number of agents is unrestricted, and \(S\) and \(T\) need not form a laminar family. In particular, both lower and upper global quota hold at every prefix; this gives exact eligibility-aware proportionality up to one item for identical unit goods as well as identical unit chores.

## Assumptions and scope
The finite agent set and both nonempty eligibility sets are known before arrivals; the arrival sequence need not be known. All items have one unit of common value or cost. Each item has exactly one of the two eligibility sets. Items are indivisible and cannot be moved once assigned. Agents outside \(S\cup T\) receive no items. Sequences may be of arbitrary finite length and may be chosen adaptively. Distinct eligibility sets are not necessary for validity.

## Proof
Write \(s=|S|\) and \(t=|T|\), swapping type names if necessary so that \(s\le t\). Enumerate the \(k=|S\cap T|\) agents in the intersection as \(u_1,\ldots,u_k\). Fix an ordering of \(S\) that puts \(u_p\) in position \(p\), for \(1\le p\le k\). In an ordering of \(T\), put the same agent \(u_p\) in position
\[
q(p)=\left\lfloor t\left(1-\frac{p}{s}\right)\right\rfloor+1.
\]
These positions are integers between \(1\) and \(t\). They are pairwise distinct: as \(p\) increases by one, the real number within the floor decreases by \(t/s\ge1\). Fill the unused positions in the two orders arbitrarily with agents exclusive to the corresponding set. For each arriving item, choose the next agent in the cyclic ordering of its own eligibility set, beginning with position one. The two type counters operate independently.

Fix a shared agent \(u_p\), and write \(q=q(p)\). The definition of the floor gives
\[
1<\frac{p}{s}+\frac{q}{t}\le1+\frac{1}{t}.
\]
At a prefix with \(a=As+r\), \(b=Bt+v\), \(0\le r<s\), and \(0\le v<t\), the load of this agent is
\[
L_{u_p}=A+B+\mathbf1_{r\ge p}+\mathbf1_{v\ge q},
\]
while its fractional entitlement is \(P_{u_p}=A+B+r/s+v/t\). If neither indicator is one, then
\[
\frac r s+\frac v t\le\frac{p-1}{s}+\frac{q-1}{t}
\le1-\frac1s<1,
\]
so its integer load \(A+B\) equals the lower rounded entitlement. If both indicators are one, then \(r/s+v/t\ge p/s+q/t>1\), and the integer load \(A+B+2\) equals the upper rounded entitlement (the fractional remainder is strictly less than two). If exactly one indicator is one, the integer load is \(A+B+1\). In that case the fractional remainder is strictly between zero and two, so \(A+B+1\) is between its floor and ceiling, inclusive. These exhaust all possibilities.

For an agent belonging to exactly one set, cyclic assignment differs from its fractional entitlement by less than one: it receives either the floor or the ceiling of its own type count divided by the size of its eligibility set. Every agent outside both sets has load and entitlement zero. Thus the quota inequalities hold simultaneously for every agent and prefix, without any knowledge of future arrivals.

For unit chores, if an agent's load exceeds its proportional share, deleting one of its assigned eligible chores lowers its load by one and removes the violation. For unit goods, if an agent's load is below its proportional share, adding one eligible good not currently held by the agent suffices; such a good must exist, because otherwise all the goods relevant to its share were already assigned to it and its load could not be below the share. Consequently this rule also witnesses eligibility-aware Prop1 at every prefix under the usual positive-unit conventions.

## Verification
Run `python3 verify.py` with an ordinary Python 3 interpreter. The standalone integer-arithmetic program checks every pair of sizes \(1\le s\le t\le30\), every feasible intersection size, all relevant shared positions and all possible pairs of type residues. It checks validity and uniqueness of the cyclic positions, the strict phase inequalities, and the exact integer floor/ceiling quota inequalities. The successful execution reports `VERIFY_OK cases= 5425 residue_checks= 19027800`. This is a finite cross-check; the preceding argument, not the test, proves the theorem for every finite size and sequence.

## Relationship to prior work
Biburger, Megow and Shahkarami (2026) formulate eligibility-aware proportional shares and prove strong online approximation limitations for unrestricted eligibility sequences; their theorems do not establish exact prefixwise quota for an arbitrary-size agent set with *two* known eligibility types. Cembrano, Correa, Griesbach and Verdugo (2025) formulate online *global quota* and prove it can be maintained for arbitrary incoming fractional vectors precisely when the number of parties is at most three. Their unrestricted input alphabet differs from the present fixed two-vector alphabet, which permits arbitrarily many agents. Existing prefixwise upper-quota constructions for laminar eligibility families do not imply this crossing-set result or its lower-quota guarantee.

## Limitations
The sets of eligible agents must be fixed and known before arrivals and there may be only two distinct types. The rule does not address three or more eligibility types, varying item sizes, agent-specific valuations, or unknown eligibility alphabets. It guarantees quotas but does not claim stronger envy-freeness, strategic properties or Pareto optimality. The distinction from differently phrased related work has been examined but cannot rule out unindexed earlier results. No independent mathematical audit has been performed.

## References
- J. Biburger, N. Megow and G. Shahkarami, *Online Fair Division under Eligibility Constraints*, arXiv:2610.08064v1, first public 2026-10-06. https://arxiv.org/html/2610.08064v1
- J. Cembrano, J. Correa, S. M. Griesbach and V. Verdugo, *Online Proportional Apportionment*, arXiv:2510.14752v1, first public 2025-10-16. https://arxiv.org/html/2510.14752v1
