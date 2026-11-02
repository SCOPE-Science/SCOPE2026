# Exact minimum linear superstring length for all binary five-bit squares

## Finding

Let \(\mathcal S_5=\{uu:u\in\{0,1\}^{5}\}\), the set of all \(32\) binary squares of length \(10\). Among finite *linear* binary words \(w\) in which every member of \(\mathcal S_5\) occurs contiguously, the shortest possible length is

\[
\min\{|w|:\mathcal S_5\subseteq\operatorname{Fact}_{10}(w)\}=82.
\]

The lower bound is sharp. A witness is the following literal binary word, with no separators:

```text
0000000000110001100010000100001010010100101111011110110101101011100111001111111111
```

## Assumptions and scope

The alphabet is the ordered binary alphabet \(\{0,1\}\). The input family consists of the square \(uu\) of *every* indexed five-bit root \(u\), including constant roots; hence there are exactly \(32\) distinct required length-\(10\) words. A factor is ordinary contiguous inclusion, with **no cyclic wraparound**. A covering word may contain other factors and repeated occurrences. Its length counts written bits, including both ends.

For distinct required squares \(s_i,s_j\), let \(o(i,j)\) be the largest proper suffix-prefix overlap length, and let \(c(i,j)=10-o(i,j)\). Here \(0\le o(i,j)\le9\) and \(1\le c(i,j)\le10\).

## Proof

**Reduction to an overlap Hamiltonian path.** In any covering word, choose one occurrence of each required square and order the \(32\) chosen start positions. The difference between successive start positions is at least the corresponding overlap cost. Consequently the word has length at least \(10\) plus the sum of the \(31\) costs in that ordering. Conversely, greedily overlapping any ordered list of all required squares by their maximum suffix-prefix overlaps produces a covering word of exactly that length. Therefore the optimum is exactly the minimum weighted Hamiltonian-path length \(10+\sum c(i,j)\) on the \(32\) distinct squares.

**Necklace bound.** Partition the five-bit roots into classes under cyclic rotation. There are precisely eight classes: two singleton constant roots and six primitive classes of size five. If two roots belong to different classes, their squares overlap by at most four symbols, so \(c(i,j)\ge6\). For distinct roots of the same class, \(c(i,j)\ge1\). An ordering of all squares has \(31\) transitions. If exactly \(q\) cross between different classes, all eight classes must be visited, so \(q\ge7\), and

\[
|w|\ge10+(31-q)+6q=41+5q.
\]

For \(q\ge9\) the right-hand side is at least \(86\). It remains to exclude lengths at most \(81\) with \(q=7\) or \(q=8\).

**Seven crossings.** With \(q=7\), each necklace is visited in one contiguous block. For each possible first and last root of a block, enumerate all its permutations (at most \(5!=120\)) and retain the least internal overlap cost. A subset dynamic program, over the eight visited-necklace bits and the last block's endpoints, adds the minimum internal cost of the next block and the exact cross-block cost. This is exhaustive because an ordering with seven crossings has precisely one block per necklace, and only a block's endpoints affect external costs. The exact integer computation yields minimum total length \(82\), so no such ordering has length at most \(81\). The recurrence and enumeration are implemented in `VERIFY.py` under `q7_optimum`.

**Eight crossings.** At \(q=8\), the necklace bound already equals \(81\). Equality would require every within-necklace transition to cost exactly one and every cross-necklace transition to cost exactly six. A cost-one transition within a primitive five-root necklace is exactly its one-step cyclic rotation, and these edges form one directed five-cycle. There would be nine blocks: one of the six primitive necklaces split into two nonempty directed arcs, and the other seven necklaces occurring once. Every possible ordered split is determined by a choice of one of six primitive necklaces, a start vertex among five, and a cut after one of four vertices, giving \(6\cdot5\cdot4=120\) cases. For each case, the unsplit five-vertex blocks have five possible directed starting phases; the constant blocks have only one. A subset reachability dynamic program over the nine blocks, allowing cross-block transitions only when their exact cost is six, finds **no** Hamiltonian ordering in any of the \(120\) cases. Thus equality at length \(81\) is impossible. The independent finite case construction and reachability recurrence are implemented in `VERIFY.py` under `q8_zero_excess_possible`.

The three cases \(q=7\), \(q=8\), and \(q\ge9\) exhaust all possibilities and prove the lower bound \(82\). Direct factor enumeration verifies that the displayed \(82\)-bit witness contains every member of \(\mathcal S_5\), completing the proof.

## Verification

Run `python3 VERIFY.py` with Python \(3.9\) or later and no third-party dependencies. It rebuilds all square-overlap costs from literal bits, checks all eight necklace classes and cross-neighborhood inequalities, recomputes the exact seven-crossing dynamic program, exhausts all \(120\) eight-crossing equality cases, and checks the witness's \(32\) required length-\(10\) factors. It prints `VERIFY_OK` only after all assertions pass. An alternative formulation as a directed Hamiltonian-path integer program with iterative subtour elimination is in `ALT_MILP.py` (requires NumPy and SciPy); its optimum is also \(82\). This alternative computational check is not an independent scientific audit.

## Relationship to prior work

Au's work on generalized de Bruijn words and powers, publicly available as arXiv:0904.3997 in April \(2009\) and in a revised \(2015\) account, studies precisely these square-covering families. Its general lower-bound proposition implies \(|w|\ge72\) at the binary five-bit parameter. Its published greedy square-cover procedure, evaluated at that parameter, already supplies a length-\(82\) upper-bound construction; the number \(82\) is **not** claimed here as a previously unknown construction. The contribution is a matching, exhaustive lower bound proving that no shorter linear word exists. In particular, the general bounds and greedy construction alone do not imply the stated optimum.

## Limitations

Only the binary length-\(10\) squares from all length-five roots are classified. No formula for other root lengths, larger alphabets, circular covers, or enumeration of all shortest words is asserted. The computational lower certificate is a finite exact dynamic-programming enumeration, not a symbolic all-length theorem; its independently written mathematical rationale is given above. Historical priority outside inspected sources remains subject to additional literature review. No independent scientific audit has been performed.

## References

1. Yu Hin Au, *Generalized de Bruijn words for Primitive words and Powers*, arXiv:0904.3997 (first submitted April 25, 2009), especially the squares section. https://arxiv.org/abs/0904.3997
2. Yu Hin Au, *Generalized de Bruijn words for Primitive words and Powers*, revised account dated May 24, 2015, Section 3, Proposition 14, Theorem 15, Corollary 16 and Algorithm E. https://au-gary.github.io/Au15a.pdf ; published in *Discrete Mathematics* 338 (2015), 2320–2331. DOI:10.1016/j.disc.2015.05.025.
