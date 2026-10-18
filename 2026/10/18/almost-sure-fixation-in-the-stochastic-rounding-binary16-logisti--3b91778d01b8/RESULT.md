# Almost-sure fixation in the stochastic-rounding binary16 logistic map

## Finding

For the fully chaotic real logistic polynomial \(f(x)=4x(1-x)\), replace its **exact real-valued result** after each iteration by one independent ideal stochastic rounding to a neighboring nonnegative IEEE-754 binary16 value. This explicit *single-final-rounding* Markov chain has exactly two closed recurrent classes, both absorbing singletons: \(0\) and \(3/4\). **Every initial representable state is absorbed in finite time with probability one.** Thus nonperiodicity is not preserved indefinitely by ideal stochastic rounding even in this canonical chaotic example.

Among the exactly \(15{,}361\) distinct nonnegative binary16 values in \([0,1]\), there are \(15{,}315\) states from which fixation at \(0\) has probability one, exactly two states (\(1/4\) and \(3/4\)) from which fixation at \(3/4\) has probability one, and exactly \(44\) states from which both outcomes have strictly positive probability. There are \(15{,}359\) states with a positive-probability path to \(0\) and \(46\) with one to \(3/4\). The transition graph has \(30{,}623\) distinct directed edges, \(13{,}616\) strongly connected components, and maximum shortest positive-probability distance to \(\{0,3/4\}\) equal to \(23\), attained at seven states.

## Assumptions and scope

The finite state set \(S\) comprises the nonnegative IEEE-754 binary16 values from positive-zero code `0x0000` through positive-one code `0x3c00` inclusive, counting gradual-underflow subnormals but identifying the two signed zeros as the same arithmetic state. For \(x\in S\), form \(y=4x(1-x)\) **exactly over the reals**. If \(y\in S\), the next state is \(y\) with probability one. Otherwise let \(a<b\) be the adjacent representable values bracketing \(y\). The next state is \(a\) with probability \((b-y)/(b-a)\) and \(b\) with probability \((y-a)/(b-a)\); independent random choices are made at each iteration. The polynomial maps \([0,1]\) to itself, and both bracketing probabilities are strictly positive. This specifies ideal unbiased stochastic rounding **once after the exact polynomial**, not the potentially different scheme of rounding multiplication and subtraction separately. No pseudorandom-generator period is assumed.

The interval endpoint \(1\) is retained because a trajectory started below \(1\) can reach it exactly; the chain then maps \(1\) to \(0\). The singular choices \(x=0,1/4,3/4\) and \(x=1\) are included. The result concerns the finite Markov chain, not the real logistic map's invariant probability density, not other floating-point formats, and not other evaluation orders.

## Proof

**Step 1: exact state encoding and transition probabilities.** A nonnegative binary16 code \(h\) with \(0\le h\le15360\) represents
\[
x_h=\begin{cases}
h/2^{24},&0\le h<1024,\\
(1024+(h\bmod 1024))/2^{25-\lfloor h/1024\rfloor},&1024\le h\le15360.
\end{cases}
\]
These strictly increasing rational values enumerate \(S\) without omission or duplication. For each \(h\), calculate exactly \(y_h=4x_h(1-x_h)\). Locate \(y_h\) by binary search in this sorted rational sequence; its unique one or two possible targets, and their positivity, follow directly from the rounding definition. This gives a finite directed graph \(G\) with an edge if and only if the corresponding transition probability is strictly positive.

**Step 2: exhaustive graph certificate.** The included standard-library-only `verify.py` uses Python's arbitrary-precision rational `Fraction` arithmetic to generate **every** state and transition. It implements two independent graph passes: backward reachability from \(0\) and \(3/4\), and iterative Kosaraju decomposition of the entire directed graph. Its explicitly executable assertions verify that there are exactly \(13{,}616\) strongly connected components and that the only components without outgoing edges are the two singleton states \(0\) and \(3/4\). It also verifies exact reachability cardinalities \(|R_0|=15{,}359\), \(|R_{3/4}|=46\), \(|R_0\cap R_{3/4}|=44\), and \(R_{3/4}\setminus R_0=\{1/4,3/4\}\). Here \(R_a\) means the set of vertices with a directed path to \(a\). The code gives an independent shortest-path check of maximum distance \(23\); there are seven states at that distance. No sampled trajectory, floating approximation, or incomplete search is used in these finite assertions. The proof is computationally assisted specifically at this explicit exhaustive graph step, and its self-contained source is supplied.

**Step 3: almost-sure absorption.** In any finite-state Markov chain, with all displayed edge probabilities positive, the states visited infinitely often form a closed recurrent communicating class with probability one. The graph certificate shows that only \(\{0\}\) and \(\{3/4\}\) are such classes. Both are absorbing because \(f(0)=0\) and \(f(3/4)=3/4\). Hence absorption in finite time occurs with probability one from every start. From a state that reaches only one sink, fixation at that sink has probability one. From each of the \(44\) states that reaches both sinks, both absorption probabilities are strictly positive, since any prescribed finite directed path to either sink has strictly positive product probability. This proves the exact partition and claims.

## Verification

Run `python3 verify.py` with a Python 3 standard library. It prints the complete state/edge counts, recurrent-class certificate, reachability partition and shortest-path statistic, and ends in `PASS`. The transition encoding stream (big-endian initial-state code, target count, and target codes) has SHA-256 `94b900c38f4dfb6e88c690e7cdead1540bce5d3836c0daa46b0534d0b89c2917`. The code is the primary independently replayable finite computation; this digest detects changes but is not an alternative proof.

## Relationship to prior work

Klöwer, Coveney, Paxton and Palmer studied finite-precision chaotic simulations, including the logistic map and stochastic rounding. Their 2022 public preprint and 2023 journal article describe improved **finite-run** bifurcation diagrams and identify possible stochastic-rounding collapse for the generalized Bernoulli map. The relevant full journal sections on stochastic rounding, logistic-map bifurcations, Bernoulli-map behavior, and methods do not give the complete recurrent-class classification of the precisely defined **single-final-rounding** logistic chain at \(r=4\). The present result separates transient visual improvement from infinite-horizon almost-sure absorption in this distinct arithmetic semantics. Previously computed **deterministic** binary16 logistic cycles under nearest rounding also do not imply stochastic transition-graph recurrence: deterministic orbits use one transition per state while this Markov chain can use two.

## Limitations

The claim is exact for a fixed, natural, finite arithmetic model; it is not an asymptotic theorem as precision tends to infinity. It does not give closed-form absorption probabilities for each of the \(44\) mixed-outcome states or useful uniform expected-absorption-time estimates. A path of length at most \(23\) with positive probability does not imply typical absorption within \(23\) steps. Most importantly, different orderings or intermediate rounding of the arithmetic operations can produce different transition graphs, so this finding does not certify the detailed implementation or plots in the motivating publication. The correctness of the exhaustive finite-state statements is supported by a replayable exact-arithmetic computation rather than an entirely hand-enumerated list.

## References

1. M. Klöwer, P. V. Coveney, E. A. Paxton and T. N. Palmer, *Periodic orbits in chaotic systems simulated at low precision*, initial preprint posted 8 November 2022, DOI: `10.21203/rs.3.rs-2223046/v1`.
2. M. Klöwer, P. V. Coveney, E. A. Paxton and T. N. Palmer, *Periodic orbits in chaotic systems simulated at low precision*, *Scientific Reports* 13, 11410 (2023), DOI: `10.1038/s41598-023-37004-4`. The peer-reviewed full text specifies stochastic rounding and finite-precision logistic-map experiments.
3. IEEE Standard for Floating-Point Arithmetic, IEEE 754-2019, specifying the binary16 format, subnormal values and rounding representations; only the binary16 value set is required in the present definition.
