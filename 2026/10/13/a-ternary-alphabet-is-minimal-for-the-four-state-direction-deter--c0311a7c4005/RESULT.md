# A ternary alphabet is minimal for the four-state direction-determinate extremum
## Finding
For a four-state direction-determinate two-way deterministic finite automaton with nonempty language, the published alphabet-unrestricted maximum possible length of a shortest accepted string is
\[
\binom{4}{2}-1=5.
\]

This extremum cannot be attained over a binary alphabet. The exact binary maximum is
\[
4.
\]
A binary witness has
\[
Q^+=\{0,1,2\},\qquad Q^-=\{3\},
\]
enters the input in state \(0\), accepts at the right end-marker only in state \(1\), and has input transitions
\[
\begin{array}{c|cc}
 & a & b\\
\hline
0&(2,+1)&(3,-1)\\
1&(1,+1)&(2,+1)\\
2&(3,-1)&(0,+1)\\
3&\text{undefined}&(1,+1).
\end{array}
\]
All noninitial end-marker transitions are undefined. Its shortest accepted word is \(\mathtt{abba}\).

Three letters already recover the unrestricted value \(5\). A ternary witness with the same partition, initial entrance state \(0\), and sole accepting state \(1\) has
\[
\begin{array}{c|ccc}
 & a & b & c\\
\hline
0&(0,+1)&(3,-1)&\text{undefined}\\
1&\text{undefined}&(0,+1)&(1,+1)\\
2&(2,+1)&(2,+1)&(3,-1)\\
3&(1,+1)&(2,+1)&\text{undefined}.
\end{array}
\]
Its shortest accepted word is
\[
\mathtt{abbac}.
\]
Therefore the minimum alphabet size needed to attain the four-state direction-determinate extremum \(5\) is exactly \(3\).

## Assumptions and scope
A two-way deterministic finite automaton has a partial transition function on its alphabet together with left and right end-markers. It accepts when it reaches the right end-marker in an accepting state. A direction-determinate automaton has a partition \(Q=Q^+\cup Q^-\) such that every right-moving transition enters \(Q^+\) and every left-moving transition enters \(Q^-\).

The result concerns exactly four states and compares alphabet sizes. It uses the published theorem that every four-state direction-determinate automaton has a shortest accepted string of length at most \(5\), and that this unrestricted bound is attainable.

For the displayed witnesses, the initial left-endmarker transition moves right into state \(0\); all later left-endmarker transitions and all right-endmarker transitions are undefined.

## Proof
The ternary lower bound is direct. Simulating the displayed ternary automaton on every ternary word of lengths \(0,1,2,3,4\) yields rejection, while \(\mathtt{abbac}\) is accepted. Its accepting computation, listing the scanned input position after the initial end-marker move, is
\[
(0,1)\to(0,2)\to(3,1)\to(1,2)\to(0,3)\to(3,2)\to(2,3)\to(2,4)\to(2,5)\to(3,4)\to(1,5),
\]
followed by a right move in state \(1\) to the right end-marker. Hence its shortest accepted length is \(5\). The published unrestricted upper bound shows that \(5\) is optimal.

For the binary upper bound, exhaust all direction splits. Write \(k=|Q^+|\) and \(4-k=|Q^-|\). For a fixed split, each state-symbol transition has exactly five choices: undefined, right to one of the \(k\) states in \(Q^+\), or left to one of the \(4-k\) states in \(Q^-\). Thus each binary input letter has \(5^4=625\) possible transition maps.

State relabeling inside \(Q^+\) lets the initial entrance state be fixed as state \(0\). Once that is fixed, a singleton accepting state has only two symmetry types: state \(0\) itself, or one other state of \(Q^+\). It is enough to use singleton accepting sets: if an automaton with several accepting states has shortest accepted word \(w\), retaining only the accepting state first reached by the accepting computation of \(w\) cannot create a shorter accepted word and still accepts \(w\).

The exhaustive verifier also allows more end-marker freedom than an actual automaton needs. For every later visit to the left end-marker in a state of \(Q^-\), it independently allows rejection or a right move to any state of \(Q^+\); for every nonaccepting visit to the right end-marker in a state of \(Q^+\), it independently allows rejection or a left move to any state of \(Q^-\). Treating the initial entrance and later left-endmarker behavior independently makes this search space a superset of the actual four-state automata, so an upper bound proved in it is valid a fortiori.

The exact maxima in this enlarged binary search space are
\[
\begin{array}{c|cccc}
(|Q^+|,|Q^-|)&(1,3)&(2,2)&(3,1)&(4,0)\\
\hline
\text{maximum shortest length}&0&3&4&3.
\end{array}
\]
Consequently no binary four-state direction-determinate automaton can have shortest accepted length \(5\). The displayed binary automaton has shortest accepted length \(4\), so the binary maximum is exactly \(4\).

## Verification
Run `python3 verify.py` beside `verify.cpp` and `certificate.json`.

The verifier enumerates all \(625^2\) ordered binary input-transition pairs for each of the four possible direction splits. It exhausts the symmetry-reduced initial and final states and every allowed boundary-return map in the enlarged search space. Each candidate is simulated on all binary words through length \(5\), with repeated configurations detected as loops.

The program independently replays the displayed binary witness on every shorter binary word and on \(\mathtt{abba}\). It also checks all ternary words shorter than length \(5\) against the displayed ternary witness and replays \(\mathtt{abbac}\).

## Relationship to prior work
Martynova and Okhotin prove that the alphabet-unrestricted four-state direction-determinate maximum is \(5\), as the \(n=4\) case of their exact formula
\[
\binom{n}{\lfloor n/2\rfloor}-1.
\]
Their extremal construction for a fixed split uses a distinct input symbol for each consecutive pair in an ordered family of crossing-state patterns. In the four-state extremal split \((|Q^+|,|Q^-|)=(3,1)\), that construction therefore uses five input symbols.

Earlier work on shortest strings in two-way automata treats fixed alphabet size as a separate asymptotic regime, establishing lower bounds for each fixed alphabet size, but it does not give this exact four-state binary-versus-ternary boundary. The 2026 journal refinement of the shortest-string bounds repeats the exact direction-determinate formula without reporting a four-state fixed-alphabet threshold.

Searches using the exact four-state parameter, binary and ternary alphabet formulations, the fixed-alphabet terminology, and the witness word \(\mathtt{abbac}\) located the general shortest-string papers but no published statement that binary gives \(4\) while ternary first attains \(5\).

## Limitations
This is a four-state alphabet-economy result. It does not determine the minimum alphabet size needed to attain the direction-determinate extremum for general \(n\), nor the exact fixed-alphabet maxima for larger state sets.

The binary upper bound is computational but exhaustive over a search space that contains all relevant binary automata. Unindexed or unpublished small-state computations could contain the same boundary even though the inspected literature does not report it.

## References
1. O. Martynova and A. Okhotin, “The maximum length of shortest accepted strings for direction-determinate two-way finite automata,” arXiv:2210.00235v1, first public version 2022-10-01.
2. O. Martynova and A. Okhotin, “Shortest Accepted Strings for Two-Way Finite Automata: Approaching the \(2^n\) Lower Bound,” Descriptional Complexity of Formal Systems 2023, LNCS 13918, pp. 134–145, DOI 10.1007/978-3-031-34326-1_10.
3. E. Dobronravov, N. Dobronravov, and A. Okhotin, “On the Length of Shortest Strings Accepted by Two-way Finite Automata,” Fundamenta Informaticae 180(4), 315–331, 2021, DOI 10.3233/FI-2021-2044.
4. O. Martynova and A. Okhotin, “Improved bounds on the length of shortest strings accepted by two-way finite automata,” Information and Computation 311, 105462, 2026, DOI 10.1016/j.ic.2026.105462.
