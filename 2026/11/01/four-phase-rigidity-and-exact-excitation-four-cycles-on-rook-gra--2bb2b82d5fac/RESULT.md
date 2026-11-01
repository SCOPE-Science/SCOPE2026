# Four-phase rigidity and exact excitation four-cycles on rook graphs

## Finding

Let \(R_{a,b}=K_a\square K_b\) be the simple, loopless rook graph on the \(ab\) labelled cells \((i,j)\), \(1\le i\le a\), \(1\le j\le b\), with \(a,b\ge2\). Neighbors are all other cells in the same row or column. For synchronous threshold-one three-state Greenberg--Hastings dynamics, **every primitive temporal four-cycle is a four-phase rectangle wave**, and the number of distinct primitive temporal four-cycle orbits is
\[
Q_4(a,b)=\frac{(2^a-2)(2^b-2)}2
       =2(2^{a-1}-1)(2^{b-1}-1).
\]

Precisely, partition the rows into two nonempty blocks and the columns into two nonempty blocks. Give their four Cartesian rectangles the excitation phases \(0,1,2,3\) in a cyclic order around the block square, or in the opposite cyclic order. A vertex with phase \(s\in\mathbb Z/4\mathbb Z\) is excited (state \(1\)) exactly at times \(t\equiv s\pmod4\), is refractory (state \(2\)) at time \(s+1\), and is at rest (state \(0\)) at the other two times. Every period-four orbit has this form; the phase origin merely selects one of its four temporal states.

## Assumptions and scope

All cells are labelled, and **orbits are identified under temporal shift only**, not under row permutations, column permutations, or swapping board axes. The synchronous local update \(F\) is
\[
F(x)_v=\begin{cases}2,&x_v=1,\\0,&x_v=2,\\1,&x_v=0\text{ and some }u\sim v\text{ has }x_u=1,\\0,&x_v=0\text{ and no }u\sim v\text{ has }x_u=1.\end{cases}
\]
A primitive four-cycle is a state \(x\) satisfying \(F^4(x)=x\) but \(F^2(x)\ne x\). No other periodic-orbit counts, global period restrictions, or universal transient bounds are claimed.

## Proof

**Step 1: the four-phase lemma.** On any finite connected graph, a site on a temporal four-cycle either remains at zero at all four times or follows a cyclic shift of the word \(1,2,0,0\). Indeed the automatic transitions \(1\to2\to0\) prevent two excitations inside any cyclic window of length four. If a site is zero at all times, none of its neighbors can ever be excited, so connectedness implies that either all sites stay zero or every site has exactly one excitation per four steps. Since a primitive four-cycle is not the all-zero fixed point, the latter alternative holds at every vertex.

Let \(c(v)\in\mathbb Z/4\mathbb Z\) be the time modulo four at which vertex \(v\) is excited. The rule is equivalent to two conditions:

1. No two adjacent vertices have opposite phases \(s\) and \(s+2\). Otherwise the vertex of phase \(s\), which is resting at time \(s+2\), would be excited too early.
2. Every vertex of phase \(s\) has a neighbor of phase \(s-1\); this neighbor triggers its excitation at time \(s\).

Conversely, these conditions ensure that at the earlier resting step a vertex has no excited neighbor, and at the later resting step it has a predecessor-phase excited neighbor. The prescribed four-word is therefore an actual orbit. The predecessor condition forces all four phases to occur.

**Step 2: rectangle rigidity.** For the rook graph, cells in one row or one column are all adjacent. By the no-opposites condition, the phases appearing in a row or column form a singleton or a pair of consecutive phases on the four-cycle. Some row uses a pair; otherwise each row would be monochromatic, and every column would contain all four globally occurring phases, contradicting the no-opposites condition. Rotate the phase labels so the chosen row has exactly the phases \(0,1\). Write \(C_0,C_1\) for its nonempty column classes.

Take a cell in that row in any column of \(C_0\). It needs a neighboring phase-\(3\) site. This cannot lie in its own row, so a second row contains phase \(3\) in a column \(c\in C_0\). That phase-\(3\) site needs a phase-\(2\) neighbor; it cannot lie in column \(c\), where phase \(0\) already occurs, so it lies in the second row in some column of \(C_1\). Consequently this second row has phase \(3\) throughout \(C_0\) and phase \(2\) throughout \(C_1\): a cell above phase \(0\) can only be in \(\{3,0,1\}\), but phases \(0,1\) are opposite to one of the already present \(2,3\); likewise above phase \(1\) only phase \(2\) remains possible.

In any further row, the two established reference rows restrict entries in \(C_0\) to \(\{0,3\}\), and in \(C_1\) to \(\{1,2\}\). No row may contain both a phase \(0\) and a phase \(2\), or both \(3\) and \(1\). Since each column class is nonempty, the whole row must therefore be of exactly one type:
\[
\begin{array}{c|cc}
& C_0&C_1\\\hline
\text{type A}&0&1\\
\text{type B}&3&2
\end{array}.
\]
Both row types occur. Thus the four phase classes are exactly the four rectangles induced by two nonempty row blocks and two nonempty column blocks. Undoing the phase rotation, and allowing either direction around the four rectangles, gives all the possible phase arrangements.

**Step 3: converse and exact count.** Every such rectangle labeling has no opposite phases in one row or column. Each vertex has a neighbor of the preceding phase: it lies in the other block of the same row or the other block of the same column. Hence Step 1 gives a primitive four-cycle, not a shorter orbit, because all four excitation phases occur.

There are \((2^a-2)/2\) unordered bipartitions of the labelled rows into two nonempty blocks and \((2^b-2)/2\) of the columns. For each pair, choose a canonical order of the two blocks (for instance, the block containing the least label first). There are precisely two possible cyclic directions for assigning \(0,1,2,3\) around the resulting block square after quotienting by global phase rotation; each direction gives one distinct temporal four-cycle. Multiplying gives the displayed value of \(Q_4(a,b)\). \(\square\)

## Verification

Compile \(check_four_cycles.cpp\) with `g++ -O3 -std=c++17 check_four_cycles.cpp -o check_four_cycles` and execute `./check_four_cycles`. The executable independently (i) tests \(F^4(x)=x\ne F^2(x)\) for **every** ternary initial state in nine board sizes, and (ii) constructs all rectangle-phase states by enumerating nontrivial row and column partitions and both orientations, requiring the two sets to coincide exactly. It covered **20,280,861** labelled configurations. The reproduced output appears in `check_four_cycles_output.txt`. The calculated orbit counts include \(Q_4(2,2)=2\), \(Q_4(2,3)=6\), \(Q_4(3,3)=18\), \(Q_4(3,4)=42\), and \(Q_4(3,5)=90\).

These finite computations are consistency checks; the all-size conclusion follows from the combinatorial argument in Steps 1--3.

## Relationship to prior work

The Greenberg--Hastings model was introduced for excitable media by Greenberg and Hastings. Gravner, Lyu, and Sivakoff established a general circulation/maximum-cycle-mean characterization of activity for three-color excitation on arbitrary connected graphs (in particular their Theorem 3). That theory supplies important qualitative constraints on oscillation, but not a count of temporal four-cycles on rook graphs or the row-column rectangle rigidity proved above. Direct enumeration on the four-vertex square gives two four-cycles, matching the \(a=b=2\) boundary case but not implying this two-parameter theorem.

For square boards, the sequence \(Q_4(n,n)=2(2^{n-1}-1)^2\) appears numerically in OEIS A087291 after an index shift, in a distinct coprime-polynomial interpretation. The numerical sequence is **not** claimed to be new. The asserted contribution is its excitation-dynamical realization together with the full rectangle classification for all rectangular dimensions.

## Limitations

The theorem counts only primitive temporal four-cycle orbits. It does **not** classify all eventual periods, first-entry times, or attraction basins, and does not claim that period-four orbits dominate the dynamics. Historical or unindexed literature on constrained graph homomorphisms or excitable networks may contain an equivalent reformulation. The 1993 paper on excitable cellular automata was available as an abstract but not as a readable full text in this review, so no whole-paper noncoverage claim is made about it. No independent external audit has been performed.

## References

1. J. M. Greenberg and S. P. Hastings, *Spatial Patterns for Discrete Models of Diffusion in Excitable Media*, SIAM J. Appl. Math. **34** (1978), 515--523, DOI: 10.1137/0134040.
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (first posted October 24, 2016); later Ann. Appl. Probab. **28** (2018), 3324--3357.
3. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002 (1993), abstract available.
4. OEIS A087291, a numerical sequence with a separate coprime-polynomial interpretation.
