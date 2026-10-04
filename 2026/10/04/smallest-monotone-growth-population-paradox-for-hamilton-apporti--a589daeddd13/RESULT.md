# Smallest monotone-growth population paradox for Hamilton apportionment
## Finding
Hamilton's largest-remainder method can exhibit the population paradox at the smallest possible nontrivial parameter cell: three states and a two-seat house.

No population paradox is possible with a one-seat house, regardless of the number of states, and none is possible with only two states, regardless of house size. Therefore the coordinatewise-minimal cell is
\[
(s,h)=(3,2).
\]

Restrict now to positive integer populations and to two censuses in which every state's population weakly increases. Measure an example by the combined population of the two censuses. The least possible combined total is
\[
46.
\]
At this total there are exactly six labeled examples, and they form one orbit under relabeling of the three states. A canonical representative is
\[
(1,4,14)\longrightarrow(4,5,18).
\]
Hamilton allocates the two seats as
\[
(0,0,2)\longrightarrow(0,1,1).
\]
Thus the third state loses a seat to the second even though its population-growth factor is
\[
\frac{18}{14}=\frac97>rac54=\frac54,
\]
the growth factor of the gaining state.

## Assumptions and scope
For a population vector \(p=(p_1,\ldots,p_s)\) and house size \(h\), Hamilton first assigns each state its lower quota
\[
\left\lfloor \frac{hp_i}{\sum_j p_j}\right\rfloor
\]
and then gives the remaining seats, one per state, to the largest fractional remainders. A profile is used only when the cutoff remainder is strict, so no tie-breaking convention enters.

A population paradox between an old census \(p\) and a new census \(p'\) means that some state \(i\) loses a seat and some state \(j\) gains a seat although
\[
\frac{p'_i}{p_i}>\frac{p'_j}{p_j}.
\]
For the integer-minimality statement, all populations are positive integers and additionally satisfy \(p'_k\ge p_k\) for every state \(k\). The size functional being minimized is \(\sum_k p_k+\sum_k p'_k\).

## Proof
For a one-seat house, Hamilton gives the unique seat to the state with largest population. If state \(i\) initially holds the seat and state \(j\) later gains it, then \(p_i>p_j\) while \(p'_j>p'_i\). These inequalities imply
\[
p'_i p_j<p'_j p_i,
\]
so \(p'_i/p_i<p'_j/p_j\). Hence a faster-growing state cannot lose the unique seat to a slower-growing state.

For two states and any house size \(h\), write
\[
x=\frac{hp_1}{p_1+p_2}.
\]
Away from a remainder tie, Hamilton's allocation to state 1 is nearest-integer rounding of \(x\): if \(x\) is nonintegral, the two fractional remainders are the fractional part of \(x\) and its complement. If state 1 grows faster than state 2, the ratio \(p_1/p_2\) increases, hence \(x\) increases, and nearest-integer rounding cannot decrease. Therefore a two-state population paradox is impossible.

It remains to exhibit a three-state, two-seat paradox. For the old census \((1,4,14)\), total population is \(19\), and the quotas are
\[
\frac2{19},\quad\frac8{19},\quad\frac{28}{19}=1+\frac9{19}.
\]
After lower quotas, one seat remains; the third remainder \(9/19\) is largest, giving \((0,0,2)\).

For the new census \((4,5,18)\), total population is \(27\), and the quotas are
\[
\frac8{27},\quad\frac{10}{27},\quad\frac{36}{27}=1+\frac9{27}.
\]
The remaining seat goes to the second state because \(10/27>9/27>8/27\), giving \((0,1,1)\). The losing third state grows by \(18/14=9/7\), while the gaining second state grows by \(5/4\), and \(9/7>5/4\).

The least-total integer statement is finite. The verifier enumerates every pair of positive three-state integer censuses with combined total at most \(46\), retains only pairs for which every population weakly increases and both Hamilton allocations have strict cutoffs, and tests every loser-gainer pair by exact cross-multiplication of growth factors. No paradox occurs below combined total \(46\). At \(46\) there are exactly six labeled pairs. Canonicalization under all six state relabelings gives one orbit, represented by the pair above.

## Verification
Run

`python3 verify_hamilton_population_boundary.py`

The verifier uses exact rational and integer arithmetic and implements Hamilton twice: once with exact fractional quotas and once with integer quotient/remainder arithmetic. The two implementations are asserted equal on every enumerated census.

The exhaustive search covers every positive three-state pair with combined total at most \(46\) satisfying componentwise nondecrease. It verifies zero paradoxes below \(46\), six at \(46\), one candidate-relabeling orbit, the representative allocations, and the strict growth comparison. Additional finite sweeps cross-check the analytic one-seat and two-state formulas.

## Relationship to prior work
Balinski and Young's classical work formalizes apportionment, exact quotas, lower and upper quota, and the structural axioms used to compare apportionment methods. Their 1975 paper also explains the Hamilton tradition and the role of monotonicity-style requirements. The population paradox itself is a classical defect of Hamilton's method and is not claimed as new.

Later expositions and government reports describe the population paradox as a transfer from a faster-growing state to a slower-growing state and give historical or pedagogical examples with much larger houses and populations. The new statement here is the sharp parameter boundary \((3,2)\) together with the complete least-total positive-integer census under the stronger condition that all three populations weakly increase.

Targeted searches under Hamilton, largest remainder, population monotonicity, two-seat and three-state formulations, the exact witness vectors, and the combined total \(46\) found no equivalent finite classification.

## Limitations
The integer-minimality statement uses the combined population of the two censuses as its size measure. It does not claim minimality under maximum component, initial total alone, or final total alone.

The exhaustive census requires all three populations to be weakly nondecreasing. The usual population-paradox definition is weaker and allows some states to shrink; the coordinatewise parameter-boundary proof does not require this stronger condition, but the \(46\)-person integer classification does.

An unindexed historical note, textbook exercise, or unpublished computation could contain the same smallest integer witness or orbit classification.

## References
1. M. L. Balinski and H. P. Young, “A New Method for Congressional Apportionment,” *Proceedings of the National Academy of Sciences USA* 71 (1974), 4602–4606. DOI: 10.1073/pnas.71.11.4602.
2. M. L. Balinski and H. P. Young, “The Quota Method of Apportionment,” *American Mathematical Monthly* 82 (1975), 701–730. DOI: 10.1080/00029890.1975.11993911.
3. M. L. Balinski and H. P. Young, “Apportionment Schemes and the Quota Method,” *American Mathematical Monthly* 84 (1977), 450–455. DOI: 10.1080/00029890.1977.11994382.
4. Congressional Research Service, “The House of Representatives Apportionment Formula: An Analysis of Proposals,” R41382, 26 August 2010.
