# Sharp single-swap PAV loss on consecutive-pair voter-interval elections

## Finding

**Theorem.** Let \(k\ge1\) be an integer. There are \(2k\) ordered voters \(v_1,\dots,v_{2k}\), and \(2k-1\) candidates \(c_1,\dots,c_{2k-1}\). Candidate \(c_i\) is approved by precisely \(v_i\) and \(v_{i+1}\). The committee size is exactly \(k\). For the harmonic Proportional Approval Voting (PAV) score, every **single-swap local maximum** \(W\)—meaning that replacing one elected candidate by one unelected candidate never strictly increases the score—satisfies

\[
2k-\frac12\left\lfloor\frac{k}{3}\right\rfloor\ \le\ \operatorname{PAV}(W)\ \le\ 2k.
\]

Both extremes are attained for every \(k\). Thus the exact worst possible ratio to the global optimum is

\[
1-\frac{\lfloor k/3\rfloor}{4k}\ \ge\ \frac{11}{12},
\]

with equality for all positive multiples of three. The first nonoptimal single-swap local maximum is at \(k=3\), namely the selected-candidate incidence word `11010`. The global optimum is the alternating word `10101`.

This is a sharp **restricted-domain** statement: it does not assert a \(11/12\) guarantee for arbitrary voter-interval profiles or elections where candidates have arbitrary consecutive supporter intervals.

## Assumptions and scope

For any candidate subset \(W\), voter \(i\)'s utility is the number of elected candidates approved by that voter, and the PAV score is the sum of harmonic utilities \(H_0=0\), \(H_1=1\), \(H_2=3/2\). The ordered candidate support intervals all have length two, so these elections belong to the voter-interval (VI) domain. No voter approves more than two candidates. The number of candidates is one less than the number of voters, and the prescribed committee size is half the voter count. No dummy or repeated candidates are used.

Identify a committee with a binary word \(w=w_1\cdots w_{2k-1}\) with exactly \(k\) ones, with \(w_i=1\) exactly when \(c_i\in W\). Write \(a(w)\) for the number of adjacent pairs of ones, and \(r(w)\) for the number of maximal runs of ones. Since there are \(k\) ones, \(a(w)=k-r(w)\).

## Proof

**Score identity and optimum.** Every selected candidate contributes exactly two approval incidences, so the total number of incidences equals \(2k\). Every voter receives zero, one, or two; a twice-represented voter loses exactly \(1/2\) relative to summing its two incidences. Twice-represented voters correspond bijectively to adjacent elected candidate pairs. Hence

\[
\operatorname{PAV}(W)=2k-\frac{a(w)}2.
\]

The alternating selection \(101\cdots01\) has \(k\) ones and no adjacent ones, proving that the global optimum is \(2k\). A swap improves the PAV score strictly if and only if it reduces \(a(w)\), or equivalently increases \(r(w)\).

**Forbidden patterns in a nonoptimal local maximum.** Suppose \(w\) is swap-local and \(a(w)>0\). If some one is flanked by two ones (the pattern `111`), deleting the middle one removes two adjacent selected pairs. Every originally empty position is nonadjacent to this middle position, and insertion at any such position could add at most two adjacent selected pairs. Swap-locality therefore forces **every** zero to have two selected neighbors. There are exactly \(k-1\) zeros and \(k\) ones in a word of length \(2k-1\); zeros all flanked by ones force the unique alternating word, contradicting `111`. Therefore every one-run has length one or two.

If any zero has no selected neighbor, replace one member of an adjacent elected pair by that zero. This removes at least one adjacent pair and creates none, contradiction. Hence there is no `000`, no initial `00`, and no terminal `00`. Moreover `1100` is impossible: replace the last one in this pattern by the immediately following zero. The removed one has a selected left neighbor, while the newly selected position, after removal, has no selected neighbor. This is a strict improvement. By reflection `0011` is impossible. The initial pattern `011` is likewise forbidden (replace the first one by the initial zero); symmetrically, the terminal pattern `110` is forbidden.

**Charging the extra zeros.** Let \(a=a(w)\), and let \(s\) be the number of singleton one-runs. Since no one-run has length greater than two, there are exactly \(a\) runs of length two and \(s\) runs of length one. Thus \(k=2a+s\), and the total number of one-runs is \(a+s=k-a\). Separating these runs uses \((a+s-1)\) mandatory zeros. The word contains \(k-1\) zeros, so precisely \(a\) zeros are **extra**: each belongs either to a length-two interior zero gap (its second zero), or to a single leading or trailing zero.

The excluded patterns show that an interior zero gap of length two can occur only between two **singleton** one-runs, and a leading or trailing zero can occur only next to a singleton one-run. Partition the singleton one-runs into maximal consecutive blocks in the ordered list of all one-runs, separated by the length-two one-runs. A block of \(t\) singleton runs supports at most \(t-1\) extra interior zeros and at most one extra boundary zero: since \(a>0\), no such block touches both ends of the complete list of one-runs. Therefore the number of extra zeros satisfies \(a\le s\). Since \(k=2a+s\), one gets \(3a\le k\), i.e., \(a\le\lfloor k/3\rfloor\). If \(a=0\), the same inequality is immediate. Substitution in the score identity proves the lower bound.

**Sharp construction.** For \(k=1,2\), take the alternating word. For \(k=3q+t\), where \(q\ge1\) and \(t\in\{0,1,2\}\), take the binary word

\[
\underbrace{110\,110\,\cdots\,110}_{q\text{ copies}}\quad
\underbrace{100\,100\,\cdots\,100}_{q\text{ copies}},
\]

remove its final zero and append \(t\) copies of `10`. The resulting word has length \(2k-1\), precisely \(k\) ones, and exactly \(q=\lfloor k/3\rfloor\) adjacent-one pairs. It consists of \(q\) double-one runs followed by \(q+t\) singleton-one runs. Deleting a singleton one decreases the number of one-runs by one, and inserting a one increases it by at most one. Deleting either member of a double-one run leaves the run count unchanged; after this deletion, **every originally empty position still has a selected neighbor**. Indeed, a zero separating two double runs has the other run as a neighbor; a zero separating a double run from a singleton has the singleton; each of the two zeros between consecutive singleton runs has an adjacent singleton; and any terminal or other singleton-separating zero also touches a singleton. Therefore inserting any originally unselected candidate cannot create a new one-run. No one-for-one replacement increases the number of one-runs, proving swap-locality. Its score equals \(2k-\lfloor k/3\rfloor/2\).

The first possible strictly positive gap has \(\lfloor k/3\rfloor\ge1\), hence \(k=3\); it is witnessed by `11010` versus the unique global optimum `10101`. At \(k=3q\), the ratio equals \(11/12\) and the absolute PAV gap equals \(q/2\), proving sharpness for arbitrarily large populations.

## Verification

The standalone `verify_path_pav.py` exhaustively enumerates all \(\binom{2k-1}{k}\) binary committees for each \(1\le k\le10\), evaluates every one-for-one swap by exact integer counts of adjacent elected pairs, and checks both the theorem's bound and an explicit sharp witness. No numerical tolerances or floating point operations are used. A successful run prints the checked committee sizes, counts of local optima, and sharp words. This computation is **not** used to infer the theorem for unbounded \(k\), which follows from the combinatorial proof.

## Relationship to prior work

Manurangsi and Sornat (2026, arXiv:2604.05953) prove polynomial-time optimization of Thiele scores on voter-interval elections and a concavity theorem across committee sizes. Avramidis, Lassota, Schmidt-Kraepelin, and Vetta (2026, arXiv:2605.03067) independently establish exact tractability on larger structured domains by linear-programming methods. Neither of those global-optimization results supplies this sharp guarantee for local one-swap maxima in the consecutive-pair subclass.

Peters, Vaish, and Yadav (2026, arXiv:2609.07554) study local PAV and prove a general tight \(2/3\) ratio using a structurally different approval construction; their theorem does not imply the sharp \(11/12\) ratio for this path domain. Kraiczy and Elkind (2024) analyze the length of PAV local-search improvement paths rather than this exact restricted-domain quality bound. Schünke (2026, arXiv:2605.30490) studies reconfiguration of **Pareto-optimal** committees in interval domains, rather than optimization of the PAV score along improving swaps.

## Limitations

Only the canonical path-incidence family (consecutive voter pairs, precisely \(2k\) voters and \(2k-1\) candidates, committee size \(k\)) is covered. A local maximum allows score-neutral swaps but prohibits strictly improving swaps. The exact result does not establish bounds for arbitrary interval lengths, voter weights, or alternative Thiele rules. Full historical priority—including possible equivalent fixed-cardinality path energy results under graph-theoretic terminology—has not been independently certified.

## References

1. Pasin Manurangsi and Krzysztof Sornat, *Polynomial-Time Algorithm for Thiele Voting Rules with Voter Interval Preferences*, arXiv:2604.05953, first submitted 2026-04-07. https://arxiv.org/abs/2604.05953
2. Dimitris Avramidis, Alexandra Lassota, Ulrike Schmidt-Kraepelin, and Adrian Vetta, *Computing Thiele Rules on Interval Elections and their Generalizations*, arXiv:2605.03067, first submitted 2026-05-04. https://arxiv.org/abs/2605.03067
3. Dominik Peters, Rohit Vaish, and Jatin Yadav, *Finding Representative and Approximately Efficient Committees*, arXiv:2609.07554, first submitted 2026-09-07. https://arxiv.org/abs/2609.07554
4. Sonja Kraiczy and Edith Elkind, *A Lower Bound for Local Search Proportional Approval Voting*, ESA 2024, DOI:10.4230/LIPIcs.ESA.2024.82. https://doi.org/10.4230/LIPIcs.ESA.2024.82
5. Joshua Schünke, *Pareto Optimality in Approval-Based Multiwinner Voting*, arXiv:2605.30490, first submitted 2026-05-28. https://arxiv.org/abs/2605.30490
