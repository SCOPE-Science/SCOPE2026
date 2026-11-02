# Complete equality classification for random-priority agent–object waste with four agents and three objects

## Finding

Consider random serial dictatorship (RSD) with exactly four labeled agents and three distinct indivisible objects. Every agent has a strict ordering of the three objects and their personal outside option. For a preference profile \(P\), let \(u_i(P)\) count the 24 priority orders in which agent \(i\) is unassigned, and let \(v_x(P)\) count the orders in which object \(x\) remains unassigned. Define the agent–object waste

\[
W(P)=\frac1{24}\max_{\substack{i\in N,\ x\in O\\x\succ_i\bot}}\min\{u_i(P),v_x(P)\},
\]

with maximum zero when there is no acceptable agent–object pair. The sharp upper bound \(W(P)\le 1/6\) is known from Basteck and Ehlers (2026). The following **complete equality classification and census** hold:

1. Of all \((4!)^4=331{,}776\) labeled full-domain preference profiles, the respective numbers with \(24W(P)=0,1,2,3,4\) are exactly \(317{,}664\), \(1{,}728\), \(5{,}040\), \(6{,}912\), and \(432\). No higher value occurs.
2. The equality case \(W(P)=1/6\) consists of exactly six distinct orbits under independent relabeling of agents and objects, each containing 72 labeled profiles. Thus its exact impartial-culture frequency is \(432/331{,}776=1/768\).
3. Every equality case admits the normal form below, and every listed normal form attains equality. In every equality case, exactly one acceptable agent–object pair realizes \(W(P)\).
4. All six normal forms yield identical deterministic assignments for each of the 24 labeled priority orders (not merely identical aggregate waste).

The normal forms use named agents \(T_1,T_2,X,Y\) and objects \(a,b,c\). Write `ab_c` for the ranking \(a\succ b\succ\bot\succ c\); other strings give the ranking in descending preference order, with `_` representing the outside option. Then

\[
T_1=T_2=\texttt{ab\_c},\qquad
X\in\{\texttt{ac\_b},\texttt{acb\_}\},\qquad
Y\in\{\texttt{bac\_},\texttt{bc\_a},\texttt{bca\_}\}.
\]

These are six independent choices for \((X,Y)\), with all four agents' outside options distinct but represented by the same underscore symbol. Each equality form has unassignment-count vectors \((u_{T_1},u_{T_2},u_X,u_Y)=(11,11,2,4)\) and \((v_a,v_b,v_c)=(0,0,4)\). Its unique maximally wasted acceptable pair is \((Y,c)\).

## Assumptions and scope

The entire domain consists of all 24 strict orderings of \(O\cup\{\bot\}\) for each of four agents; objects below that agent's outside option are unacceptable. For each of the 24 equiprobable permutations of the four agents, serial dictatorship offers the current agent their highest-ranked available acceptable object or leaves them unassigned. No random object tie-breaking or valuations are involved. The probability that an object is unassigned is a *marginal* across priorities, not the probability that it and an agent are simultaneously unassigned in the same priority order. Agent–object waste is the smaller of the two unassignment marginal probabilities for an acceptable pair.

The permutation group \(S_4\times S_3\) acts by independently relabeling agents and the three objects, preserving each agent's outside option. The classification concerns this precise group action. It does not identify profiles differing only by arbitrary changes to the number of objects or by removing the outside option.

## Proof

**Exact reduction to a finite certificate.** Every profile is an ordered 4-tuple of four-element permutations; hence there are exactly \(24^4\) profiles. Every serial-dictatorship priority is an ordered permutation of the four agent labels, hence there are exactly 24. For each profile and priority, start with the three objects available. In priority order, scan each agent's strict ranking until either the first available object is encountered (allocate and remove it) or their outside option is reached (leave unassigned). This deterministic recursion uniquely defines an allocation and has no unresolved tie cases.

Maintain integer counters \(u_i\) for each agent and \(v_x\) for each object, initially zero. After each priority, increment \(u_i\) if agent \(i\) is unassigned and \(v_x\) if object \(x\) was not allocated. Scanning exactly the acceptable prefix of every ranking, calculate

\[
w(P)=\max_{i,x:\ x\succ_i\bot}\min\{u_i(P),v_x(P)\};\qquad W(P)=w(P)/24.
\]

`verify_cpp.cpp` implements precisely these loops with fixed-size arrays and a three-bit available-object mask, traversing every one of the \(24^4\) profiles and every priority. Its complete integer histogram is

| \(w(P)\) | Labeled profiles |
|---:|---:|
| 0 | 317,664 |
| 1 | 1,728 |
| 2 | 5,040 |
| 3 | 6,912 |
| 4 | 432 |

The counts sum exactly to \(331{,}776\); the program also checks all remaining integer values through 24 have frequency zero. Because this is the entire finite domain and integer computations are exact, the histogram is a complete finite proof, not a sampling inference.

**Equality and orbit classification.** Collect exactly the 432 profiles with \(w=4\). For each one not already grouped, apply every permutation of agents and every permutation of objects, transforming the full strict order (including the unchanged outside option) and computing the resulting orbit as a set. `verify_cpp.cpp` verifies that all orbit elements are in the extremal set, removes each member exactly once, and obtains exactly six disjoint orbits, each of size 72. It checks the six lexicographically selected representatives against the six displayed normal forms, rather than relying only on their number. Their union contains \(6\cdot72=432\) profiles, proving both necessity and sufficiency of the list. During the same exhaustive scan the program counts all maximizing acceptable pairs and verifies that each of the 432 equality profiles has exactly one.

**Direct realization and outcome invariance.** For every displayed form, the independent verifier computes \(u=(11,11,2,4)\) and \(v=(0,0,4)\). The only maximally wasted acceptable pair is \((Y,c)\), for which \(\min\{u_Y,v_c\}=4\). It also compares the complete four-agent allocation vector for every individual priority across all six forms. All vectors agree. This also has a direct dependency explanation. Before \(Y\) acts, only a twin can have taken \(b\), and a twin takes \(b\) only when \(a\) was already unavailable. Hence, when \(Y\) acts, \(b\) being unavailable implies \(a\) is unavailable too: the placement of \(a\) relative to \(c\) or the outside option is behaviorally inert. Before \(X\) acts, only \(Y\) can have taken \(c\), and \(Y\) takes \(c\) only when \(b\) is already unavailable. Thus if the first two choices \(a,c\) of \(X\) are unavailable, the optional third choice \(b\) is unavailable as well. Consequently, adding those objects below the first two acceptable alternatives never affects the realized allocation.

**Independent complete-domain check.** `verify_python.py` uses a separately coded simulator with a list of available objects instead of the C++ bit mask. It fixes the order of the three object labels in the first agent's preference and lets the outside option occupy any of four positions. This is a sixfold object-relabeling quotient because each strict order of three distinct objects has trivial object-label stabilizer. The program checks all \(4\cdot24^3=55{,}296\) quotient representatives. It returns histogram \((52{,}944,288,840,1{,}152,72)\), exactly one sixth of the full counts, independently checks the six normal forms and unique witnesses, and compares their allocation vectors priority by priority. The two implementations agree.

## Verification

Compile and execute `verify_cpp.cpp` with a C++17 compiler without disabling assertions:

```sh
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_cpp.cpp -o verify_cpp
./verify_cpp
python3 verify_python.py
```

The C++ program prints `VERIFY_CPP_OK` only after completing all \(331{,}776\) profiles, the exact histogram, all six complete relabeling orbits, the normal-form equality check, and the unique-witness tests. The independently implemented Python program prints `VERIFY_PY_OK` only after completing all \(55{,}296\) symmetry-reduced profiles and checking the explicit normal forms. Both were executed successfully. Their source code and expected assertions are included with this result.

## Relationship to prior work

Basteck and Ehlers (2026, Section 3, Lemma 1 and Appendix B) prove the sharp universal \(1/6\) bound for RSD, including four agents and three objects, and display one equality example. Thus neither the bound nor the existence of an equality example is new here. The new claim is the exhaustive **equality-case classification** across the full strict-preference domain, its orbit structure, exact incidence distribution, unique extremal witnessing pair, and complete priority-wise outcome invariance. The known existence example is a member of one displayed class after relabeling. Related assignment literature studies different fairness and efficiency measures; no equivalence covering this exact classification was found in the material inspected.

## Limitations

This theorem is exact for four agents and three objects; no extension to other sizes or mechanisms is claimed. Its computational proof depends on the transparent exhaustive enumeration and two independent implementations supplied, not on an unproved asymptotic counting formula. The assignment-probability definition is marginal and should not be confused with simultaneous event probabilities or with aggregate object-wastefulness. Exhaustive enumeration proves the mathematics for this finite domain but does not by itself prove publication priority; unindexed or otherwise inaccessible earlier classifications remain a possibility.

## References

- Christian Basteck and Lars Ehlers, *Strategy-Proof and Minimally Wasteful Random Assignment*, first public version August 27, 2026, https://arxiv.org/abs/2608.27261 . Relevant material: Section 2, Section 3, Lemma 1, Appendix B.
- Pietro Martini, *Strategy-proof and fair assignment is wasteful*, 2016. Cited for background on random-assignment wastefulness; no result of that paper is being asserted as a new contribution here.
