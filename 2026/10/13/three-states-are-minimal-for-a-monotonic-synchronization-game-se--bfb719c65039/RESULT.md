# Three states are minimal for a monotonic synchronization-game separation
## Finding
Consider the synchronization game on a complete deterministic binary automaton. Alice moves first, the players alternately choose one input letter, and Alice wins as soon as the active image of the whole state set becomes a singleton.

Among synchronizing monotonic binary automata, three states are the minimum for which Bob can have a winning strategy.

Fix the preserved order
\[
0<1<2.
\]
Among all \(10^2=100\) ordered pairs of nondecreasing self-maps of this chain, exactly four are synchronizing but Bob-winning:
\[
\begin{aligned}
&(001,022),\qquad (002,122),\\
&(022,001),\qquad (122,002).
\end{aligned}
\]
Here, for example, \(001\) denotes the map \((0,0,1)\). These four normalized presentations form one orbit under interchange of the two letters and reversal of the chain.

A representative is
\[
a=(0,0,1),\qquad b=(0,2,2).
\]
It is synchronizing because \(aa\) is a reset word. Nevertheless Bob wins by always choosing \(b\). After each of Bob's moves, the active set is \(\{0,2\}\): if Alice chooses \(a\), then
\[
\{0,2\}\xrightarrow{a}\{0,1\}\xrightarrow{b}\{0,2\},
\]
whereas if Alice chooses \(b\), then
\[
\{0,2\}\xrightarrow{b}\{0,2\}\xrightarrow{b}\{0,2\}.
\]
The same conclusion holds from the initial full set after the first Alice-Bob pair of moves.

## Assumptions and scope
An automaton is monotonic if some linear order on its states is preserved by every input letter. For the finite census, one preserved order is fixed and labeled \(0<1<\cdots<n-1\), so a letter is a nondecreasing self-map of that chain. The count of four exceptional ordered pairs is therefore a count of normalized chain presentations, not of abstract automata with every possible preserved order.

The alphabet consists of exactly two named letters during enumeration. The minimal-state statement concerns synchronizing binary monotonic automata.

## Proof
There is no one-state obstruction.

For two states with preserved order \(0<1\), the only nondecreasing self-maps are
\[
(0,0),\qquad (0,1),\qquad (1,1).
\]
The only nonconstant map is the identity. Hence a binary two-state monotonic automaton is synchronizing only if one of its two letters is constant. Alice chooses such a constant letter on her first move and wins. Therefore at least three states are necessary.

For three states there are
\[
\binom{2\cdot3-1}{3}=10
\]
nondecreasing self-maps, hence \(100\) ordered binary transition pairs. The exhaustive game solution splits them into
\[
77\ \text{synchronizing Alice-win},\qquad
4\ \text{synchronizing Bob-win},\qquad
19\ \text{nonsynchronizing}.
\]
The four Bob-winning pairs are exactly the four displayed in the finding.

The game computation is finite and exact. One engine operates on every nonempty active subset. It initializes all singleton positions as winning for Alice. At an Alice position, a state is winning when at least one letter leads to a winning Bob position; at a Bob position, it is winning when every letter leads to a winning Alice position. Iterating these monotone rules to their least fixed point gives the reachability-game winning region.

A second engine uses only endpoint pairs. Monotonicity implies that a word maps an active subset to a singleton exactly when it merges the minimum and maximum states of that subset. Thus the pair game is equivalent to the full active-set game. The two engines agree for every ordered transition pair on one, two, and three states.

For the representative \(a=(0,0,1)\), \(b=(0,2,2)\), the explicit stationary Bob strategy above prevents synchronization forever, while \(aa\) independently proves ordinary synchronizability. Finally, letter interchange and chain reversal generate all four exceptional normalized presentations from this representative.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier independently enumerates all nondecreasing maps and every ordered binary pair for one, two, and three states. It solves the synchronization game twice: once on all active subsets and once on endpoint pairs. It checks the exact census
\[
\begin{array}{c|ccc}
n&\text{synchronizing Alice-win}&\text{synchronizing Bob-win}&\text{nonsynchronizing}\\
\hline
1&1&0&0\\
2&8&0&1\\
3&77&4&19
\end{array}
\]
and checks the complete list of four three-state exceptions.

It also verifies \(aa\) as a reset word, checks Bob's stationary response \(b\) on both possible Alice moves, and confirms that all four exceptions form one letter-swap/chain-reversal orbit.

As a literature comparison, the verifier checks directly that the three-state non-A example drawn in the 2024 paper is not monotonic under any of the six linear orders on its states.

## Relationship to prior work
Fernau, Haase, and Hoffmann studied synchronization games on monotonic automata in 2022. They exhibited a four-state synchronizing monotonic automaton for which Alice has no winning strategy and reduced the monotonic game to a reachability game on endpoint pairs. Their paper does not claim state-minimality or enumerate the three-state case.

Fernau, Haase, Hoffmann, and Volkov later gave a three-state synchronizing automaton on which Bob wins while developing winning strategies for DS-automata. That displayed three-state automaton is not monotonic: one letter swaps two states nontrivially, so it cannot preserve any linear order. Their main theorem supplies a sufficient algebraic condition for Alice to win but does not classify small monotonic automata.

The later uniform-strategy extension again treats transition-monoid classes rather than the minimum number of states or the three-state monotonic census. Targeted searches for three-state monotonic counterexamples, smallest monotonic synchronization-game separations, and equivalent Alice/Bob winning formulations located the papers above but no statement of the four-presentation classification or the minimality theorem.

## Limitations
The exact enumeration is only for binary automata with at most three states. It does not classify larger Bob-winning monotonic automata or determine the complexity of the bounded-length synchronization game on the whole monotonic class.

The count four is presentation-dependent because a monotonic automaton can in principle admit more than one preserved order.

An unindexed note or unpublished finite census could contain the same three-state classification despite the targeted searches.

## References
1. H. Fernau, C. Haase, and S. Hoffmann, “The Synchronization Game on Subclasses of Automata,” FUN 2022, LIPIcs 226, Article 14, DOI 10.4230/LIPIcs.FUN.2022.14.
2. H. Fernau, C. Haase, S. Hoffmann, and M. V. Volkov, “Winning Strategies for the Synchronization Game on Subclasses of Finite Automata,” arXiv:2409.06971v1; EPTCS 407 (2024), 77–85, DOI 10.4204/EPTCS.407.6.
3. H. Fernau, C. Haase, S. Hoffmann, and M. V. Volkov, “Uniform winning strategies for the synchronization games on subclasses of finite automata,” arXiv:2512.11007v1.
