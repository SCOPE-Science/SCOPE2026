# Exact two-summand exception sets for the Rudin–Shapiro sign classes

## Finding

Let \(\kappa(n)\) count overlapping occurrences of the block \(11\) in the ordinary binary expansion of \(n\ge 0\). Define
\[
A_i=\{n\in\mathbb N_0:\kappa(n)\equiv i\pmod 2\},\qquad i=0,1.
\]
Then the following three identities hold **for every nonnegative integer**, with repeated summands allowed:
\[
A_0+A_0=\mathbb N_0,
\]
\[
\mathbb N_0\setminus(A_0+A_1)=\{0,1,2,9\},
\]
\[
\mathbb N_0\setminus(A_1+A_1)
=\{0,1,2,3,4,5,7,8,10,11,13,20\}.
\]
In particular, the negative-sign Rudin–Shapiro indices form an asymptotic additive basis of order two, and the precise finite exceptional set is now specified. The theorem is a complete classification rather than a density or a finite-range observation.

## Assumptions and scope

Indices and summands are nonnegative ordinary integers. The expansion of zero has no \(11\) occurrence. Overlaps are counted, so the word \(111\) contributes two occurrences. The sumset \(A_i+A_j\) means the set of sums of an element of \(A_i\) with one from \(A_j\), allowing equality when \(i=j\). No density assumption is needed. The primary subject is digital/additive number theory, MSC2020 11B85.

## Proof

We give a finite-state proof with a self-contained and executable exhaustive reachability lemma. All states and transitions are explicitly defined below and implemented in the accompanying `verify.py`, so the finite calculation can be reproduced from the definitions.

Read binary digits of the target \(n\) from least significant to most significant. A nondeterministic addition automaton has state \((c,u,v,e,f)\in\{0,1\}^5\), with carry \(c\), most recently read summand bits \(u,v\), and parities \(e,f\) of the number of adjacent \(11\) blocks already read in the two summands. The initial state is \((0,0,0,0,0)\). On reading target bit \(d\in\{0,1\}\), choose any two summand bits \(a,b\in\{0,1\}\) satisfying
\[
a+b+c\equiv d\pmod 2.
\]
The unique corresponding next state is
\[
\left(\left\lfloor\frac{a+b+c}{2}\right\rfloor,
 a,b,e\oplus(ua), f\oplus(vb)\right),
\]
where \(\oplus\) denotes exclusive-or. At termination, accept precisely when \(c=0\), \(e=i\), and \(f=j\), without constraining the last summand bits. This nondeterministic machine has exactly 32 possible states.

**Transition invariant.** After \(k\) input digits, the chosen bits of each summand determine an integer below \(2^k\). The carry is the ordinary outgoing carry of the addition of these truncated summands; \(u,v\) are their highest processed digits and \(e,f\) are exactly the parities of adjacent \(11\) occurrences wholly within the processed bits. The initial state satisfies the invariant, and the displayed transition preserves it. When the whole input has been read and \(c=0\), the two guessed summands add to the target with no additional nonzero digits; adding leading zero digits cannot change their \(11\)-parities. Conversely, every valid representation supplies a run of this machine. Consequently the target is in \(A_i+A_j\) exactly when the machine accepts its reverse-bit input.

For an exact finite comparison with the three proposed exception lists, determinize the above machine using subsets \(U\subseteq\{0,\ldots,31\}\). Starting with the singleton initial state, the deterministic transition on digit \(d\) is the union of all nondeterministic successors on \(d\). The accept predicate is that the subset intersects the original accept mask for parity pair \((i,j)\).

Independently recognize each listed finite exception set using the state \((z,w)\), initially \((0,1)\), where \(z\) is the value of the binary digits processed so far and \(w\) the next power of two, **both saturated at 21**. On input \(d\), use
\[
z\longmapsto\min(21,z+dw),\qquad
w\longmapsto\min(21,2w).
\]
Since the largest proposed exception is 20, saturation at 21 preserves membership in each proposed exception set exactly, for every length and every digit string. The product state is \((U,z,w)\). It is initialized as the singleton subset with \((z,w)=(0,1)\). Breadth-first search from this state applies both input digits to every newly reached state; this checks **all finite binary words**, not a fixed digit-length bound.

**Exact exhaustive finite-state lemma.** For the pairs \((i,j)=(0,0),(0,1),(1,1)\), the product has 88 reachable states. At every one of these states, the addition-machine accept predicate is the complement of the membership predicate \(z\in E_{ij}\), where
\[
E_{00}=\varnothing,\quad E_{01}=\{0,1,2,9\},\quad
E_{11}=\{0,1,2,3,4,5,7,8,10,11,13,20\}.
\]
The claim is verified exhaustively by `verify.py`: the program constructs the 32-state transition table, carries out the full product breadth-first search, asserts that no reachable state has unequal predicates, and checks the count 88. The complete finite state space and transition rules are provided here and in the package, so this is a terminating exhaustive certificate. No random testing, heuristic search or numerical limit is used for the infinite identities.

For any nonnegative target, a finite low-to-high binary digit string reaches one of those product states. By the transition invariant, membership in the relevant sumset equals acceptance; by the finite-state lemma, this is equivalent to the target not lying in the corresponding listed exception set. This proves all three identities, including zero and the finite boundaries.

## Verification

Run `python3 verify.py` with the standard Python 3 library; no dependencies or network access are needed. The checker constructs the transition table rather than importing a prerecorded automaton. It exhausts all 88 reachable product states for each of the three cases, printing the exact exception lists and asserting the comparison everywhere. As a secondary check, it evaluates \(\kappa(n)\bmod2\) by the independent recurrence \(p(0)=0\), \(p(n)=p(\lfloor n/2\rfloor)\oplus[n\bmod4=3]\) and directly enumerates representations for all targets below 3000. The secondary finite checks do not substitute for the infinite automaton proof.

## Relationship to prior work

Rudin–Shapiro's automatic sign sequence is catalogued in OEIS A020985. Rajasekaran, Shallit and Smith developed automata methods for additive representation problems, including an explicitly captioned automaton for **mixed sums of Thue–Morse and Rudin–Shapiro numbers** [1]. Shallit studied exact two-summand representation functions for the **Thue–Morse evil/odious** classes and mentioned general Rudin–Shapiro applications for more than four summands [2]. Rampersad and Shallit's work on “Rudin–Shapiro sums” concerns **summatory functions of the signs**, not the two-integer sumsets here [3]. Dombi's work studies higher-fold representation counts for related sign-defined sets [4]. Konieczny established pseudorandomness/Gowers-norm results for Rudin–Shapiro signs [5], not these finite exception lists.

The present statement distinguishes three pairwise sign-class sumsets and gives **all** their exceptional integers; neither broad decidability machinery nor asymptotic representation counts by themselves specify these small exceptional sets. Prior publication priority is not independently certified: the full 2019 article [1], a particularly pertinent mixed-sum source, was not accessible for a complete textual comparison. The title and available figure caption do not establish same-set coverage, but an unreported implication cannot be ruled out.

## Limitations

Only the original overlapping-\(11\) binary Rudin–Shapiro parity sequence and two summands are treated. The complete finite-state certificate does not yield new asymptotic formulas for the number of representations, nor does it classify other blocks, moduli or three-or-more summands. The finite exception lists could have been derived in unindexed sources or as unreported consequences of previous automata constructions. A separate independent mathematical audit has not been performed.

## References

1. A. Rajasekaran, J. Shallit, T. Smith, *Additive Number Theory via Automata Theory*, Theory of Computing Systems 64 (2020), 542–567; first online 2019-05-29. DOI: 10.1007/s00224-019-09929-9.
2. J. Shallit, *Additive Number Theory via Automata and Logic*, arXiv:2112.13627, first posted 2021-12-27.
3. N. Rampersad and J. Shallit, *Rudin–Shapiro Sums via Automata Theory and Logic*, arXiv:2302.00405, first posted 2023-02-01.
4. G. Dombi, *Additive properties of certain sets*, Acta Arith. 103 (2002), 137–146.
5. J. Konieczny, *Gowers norms for the Thue–Morse and Rudin–Shapiro sequences*, Ann. Inst. Fourier 69 (2019), 1897–1913; DOI: 10.5802/aif.3285.
6. OEIS A020985, *The Rudin–Shapiro or Golay–Rudin–Shapiro sequence*, https://oeis.org/A020985.
