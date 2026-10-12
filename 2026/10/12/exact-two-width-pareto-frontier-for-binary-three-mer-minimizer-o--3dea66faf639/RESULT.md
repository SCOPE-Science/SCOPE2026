# Exact two-width Pareto frontier for binary three-mer minimizer orders

## Finding
For a binary three-mer minimizer under one strict ranking of all eight three-mers, the nondominated pair of expected selection densities for windows containing respectively four and nine three-mers is **exactly**
\[
\left\{\left(\frac{46}{128},\frac{759}{4096}\right),\left(\frac{50}{128},\frac{750}{4096}\right)\right\}.
\]
The first pair is attained by 48 rankings, the second by 32; every other ranking is weakly dominated in both densities, with strict improvement in at least one. These scores are incompatible: no ranking simultaneously minimizes both densities.

There is a stronger nearby compatibility statement: exactly 48 rankings simultaneously minimize each width from two through eight, namely all rankings whose four smallest three-mers (encoded in ordinary binary as integers from 0 to 7) appear in order \((3,2,0,6)\) or \((4,5,7,1)\), with the other four in arbitrary order. None of these 48 rankings attains the width-nine optimum.

## Assumptions and scope
Fix the eight binary words of length three, identify each with its integer in \(\{0,\ldots,7\}\), and assign their types a strict total ranking. In each sliding window containing \(w\) consecutive overlapping three-mers, select the *leftmost occurrence* of the lowest-ranked type. On an iid fair infinite binary string, define \(d_w\) as the almost-sure limiting proportion of selected three-mer starting positions. By stationarity and ergodicity, this equals the probability that the window selector changes after one step. Let \(N_w=2^{w+3}d_w\). A window shift involves precisely \(w+1\) overlapping three-mers and therefore \(w+3\) independent input bits. The exact result concerns all \(8!=40320\) strict rankings, not arbitrary context-dependent local schemes, arbitrary alphabets, or nonuniform input.

## Proof
For three-mer state \(u\in\{0,\ldots,7\}\) and next input bit \(b\in\{0,1\}\), the successor state is \(T(u,b)=(2u+b)\bmod8\). The de Bruijn walk of \(w\) edges (or \(w+1\) consecutive states) is in bijection with one binary word of length \(w+3\); each word has probability \(2^{-(w+3)}\). Given states \(x_0,\ldots,x_w\), the old window uses indices 0 through \(w-1\); the shifted one uses 1 through \(w\). Let \(r(u)\) be the rank of state \(u\) (0 lowest). With leftmost ties, the selected starting position changes if and only if either (I) \(r(x_0)\le r(x_i)\) for every \(1\le i\le w\), or (II) \(r(x_w)<r(x_i)\) for every \(0\le i<w\). The two events are disjoint. To justify the criterion: in all other cases the previous winner remains inside the new window and the arriving candidate cannot displace it; in case (I) the winner departs and in case (II) the new position strictly improves it.

For each rank \(j\), the unique state \(u\) at that rank determines the first state in (I) or last state in (II). In case (I) count length-\(w\) walks beginning at \(u\), staying in the induced directed multigraph on states with rank at least \(j\). In case (II) count length-\((w-1)\) walks entirely in states with rank greater than \(j\), followed by one edge into \(u\); initialize the earlier state with one walk per eligible start vertex. Summation over \(j=0,\ldots,7\) gives exactly \(N_w\). Parallel directed edges (distinct appended bits) retain multiplicity.

This finite transfer recursion and the independent direct word-by-word criterion were evaluated for all 40320 rankings. The transfer enumeration gives, in increasing width from two through nine, the minimum numerator and its ranking multiplicity as
\[
(20,3668),(29,176),(46,48),(76,48),
(130,48),(229,48),(413,164),(750,48).
\]
The set of rankings simultaneously attaining the first seven minima (widths two through eight) contains precisely 48 members, with the two four-type prefixes stated above. Their intersection with the width-nine minimizers is empty.

For the simultaneous width-four and width-nine problem, the exhaustive enumeration produces 1145 distinct objective pairs. Order these pairs by first coordinate and keep a pair exactly when its second coordinate strictly improves on all earlier second coordinates. This dominance filter leaves precisely \((46,759)\), attained 48 times, followed by \((50,750)\), attained 32 times. The filter is exhaustive, as every possible strict ranking appears once in the eight-element permutation loop. This establishes both Pareto completeness and the claimed impossibility of one jointly optimal ranking.

## Verification
The standalone `verify_transfer.cpp` enumerates every type order and uses the induced-subgraph dynamic program just proved to check all widths two through nine, joint minimizers, two prefix families and the Pareto frontier. The independent `verify_direct.cpp` iterates every relevant binary input word of length seven (128 words) or twelve (4096 words) and applies the explicit selector-change event, then enumerates the same 40320 rankings. Both programs returned `VERIFY_OK` with the same two Pareto vectors and multiplicities. To replay, compile each independently with `c++ -std=c++17 -O3 <source>.cpp -o <executable>` and execute it. No numerical tolerances, floating-point rounding, heuristic search or external solver are involved.

## Relationship to prior work
Classical winnowing/minimizer schemes and their density/charging principle predate this result, and the precise binary-three-mer **individual** density optima are not claimed as new. Marçais, DeBlasio and Kingsford (2018) explicitly enumerate all 40320 rankings to obtain minimum and maximum densities at each separate window width through 27. That scalar statement alone does **not** determine which common rankings attain optima simultaneously, when compatibility first fails, or the two-width Pareto frontier with multiplicities. Marçais et al. (2017) analyze density and the effect of three-mer orderings, while Orenstein et al. (2016) motivate compact universal hitting sets. The claim here is solely the simultaneous-order comparison and complete two-objective classification.

## Limitations
The result addresses binary three-mers and iid equiprobable bits only; it does not optimize variable-order minimizers, larger \(k\), or general genomic distributions. Earlier work exhaustively enumerated individual densities, so an undisclosed computational appendix or independently published cross-width table might contain the joint data; that bibliographic risk remains. Exact finite calculations establish all 40320 cases but do not imply general asymptotic laws. Independent external validation has not been performed.

## References
Orenstein, Pellow, Marçais, Shamir and Kingsford (2016), “Compact Universal k-mer Hitting Sets,” *Algorithms in Bioinformatics*, DOI: 10.1007/978-3-319-43681-4_21 (WABI meeting 22–24 August 2016).

Marçais, Pellow, Bork, Orenstein, Shamir and Kingsford (2017), “Improving the performance of minimizers and winnowing schemes,” *Bioinformatics* 33, i110–i117, DOI: 10.1093/bioinformatics/btx235.

Marçais, DeBlasio and Kingsford (2018), “Asymptotically optimal minimizers schemes,” *Bioinformatics* 34, i13–i22, DOI: 10.1093/bioinformatics/bty258.
