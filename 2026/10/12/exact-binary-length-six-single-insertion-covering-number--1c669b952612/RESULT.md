# Exact binary length-six single-insertion covering number

## Finding
Let \(I(2,6,1)\) be the smallest size of a set of binary six-symbol strings such that every seven-symbol string contains some selected string as an ordered subsequence. Then
\[
I(2,6,1)=20.
\]
One optimal code consists of the six-bit representations of the multiples of three between 0 and 63, except 21 and 42. Its elements are listed in `witness.txt`.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\). Subsequence means deleting exactly one symbol from a length-seven word, preserving the remaining order; adjacent positions are not required. Every seven-bit string must be covered. The claim applies to ordinary one-insertion covering, not deletion covering, Hamming covering, or a variable-length model. The ambient sets contain respectively \(2^6=64\) potential centers and \(2^7=128\) target words.

## Proof
For a center \(x\), define its insertion ball \(B(x)\) as the set of all words obtained from \(x\) by inserting either binary symbol in any of the seven gaps; duplicate outcomes are counted once. Write \(U=\{0,1\}^{7}\). The covering condition is precisely \(\bigcup_{x\in C}B(x)=U\).

**Construction.** Select the 20 centers specified in `witness.txt`. To verify the upper bound without relying on an optimizer, enumerate each of the 128 targets \(y\), delete each of its seven positions, and test whether a resulting six-bit word belongs to the stated 20-center set. All 128 targets pass. The numbers of targets having exactly one, two, or three distinct selected six-bit subsequences are respectively 98, 28, and 2; they sum to 128. Thus \(I(2,6,1)\le20\).

**Finite exhaustive lower bound.** Consider the following exact recursion with uncovered target set \(R\), forbidden/already selected center set \(S\), and additional-center budget \(b\). A branch can succeed immediately if \(R=\varnothing\), and fails if \(b=0\) while \(R\ne\varnothing\). For each selectable center \(c\notin S\), calculate \(g(c)=|B(c)\cap R|\). A completion of at most \(b\) centers can cover at most \(b\max_c g(c)\) remaining targets and at most the sum of its \(b\) largest available gains. If either of these two upper bounds is smaller than \(|R|\), that branch fails. Otherwise choose any uncovered target \(y\in R\). Every covering completion must contain at least one \(c\notin S\) with \(y\in B(c)\). Branch on *every* such center and recurse on \((R\setminus B(c),S\cup\{c\},b-1)\). These reductions preserve satisfiability; therefore induction on \(b\) proves the recursion exhaustive, and no pruning excludes a feasible completion.

`verify.cpp` builds the complete 64-by-128 incidence relation directly from bit insertions and implements precisely this exhaustive recursion using exact integer bit masks. For \(b=19\) it exhausts 81,671 calls and returns infeasible. The implication for every smaller cardinality follows from monotonicity: any smaller cover could be augmented to 19 centers. Thus \(I(2,6,1)\ge20\), completing the proof.

## Verification
Compile and execute `verify.cpp` with a compiler supporting C++17 and unsigned 128-bit integers, for example `g++ -std=c++17 -O2 verify.cpp -o check && ./check`. The output includes `k=19 feasible=0 nodes=81671`, a 20-center witness, and `VERIFY_OK`. The code independently verifies that the 20 chosen insertion balls cover all 128 targets. A separate direct subsequence check on `witness.txt`, with no optimization solver, gave target multiplicities \((98,28,2)\). An independent mixed-integer optimization formulation of the same 64-column, 128-row covering matrix also found optimum 20; the constructive and exhaustive proof does not rely on floating-point optimization.

## Relationship to prior work
Lenz, Rashtchian, Siegel, and Yaakobi (2020/2021) introduced bounds and constructions for insertion and deletion covering codes. Pikhurko, Verbitsky, and Zhukovskii (2025) sharpened the connection to Turán-type bounds and gave a different exact example \(S(3,4,3)=12\) concerning three-symbol centers and a ternary alphabet, credited to Grozea. Xie, Sun, and Ge (2026) sharpened bounds for insertion and deletion covering, especially in the large-alphabet regime. Their bounds do not determine this fixed binary length-six optimum. In the notation of Pikhurko and collaborators, the present statement is \(S(2,7,6)=20\). This is a finite exact specialization and does not improve those general asymptotic bounds.

## Limitations
The lower bound is a complete finite computation with an inspectable branching proof, not a symbolic uniform formula for larger lengths. The incidence enumerator depends on the explicit, fixed binary length; no result is asserted for length seven or above. The literature comparison cannot exclude an earlier unindexed finite covering table or an independently obtained identical number. No independent audit has been performed.

## References
1. Chengfei Xie, Yubo Sun, Gennian Ge, *New bounds for covering codes under insertions or deletions*, arXiv:2606.15379v1 (13 June 2026), https://arxiv.org/pdf/2606.15379.pdf.
2. Andreas Lenz, Cyrus Rashtchian, Paul H. Siegel, Eitan Yaakobi, *Covering Codes using Insertions or Deletions*, arXiv:1911.09944, https://arxiv.org/pdf/1911.09944.
3. Oleg Pikhurko, Oleg Verbitsky, Maksim Zhukovskii, *New Bounds for the Optimal Density of Covering Single-Insertion Codes via the Turán Density*, arXiv:2409.06425, https://arxiv.org/pdf/2409.06425.
4. Cristian Grozea, *Combinatorial Data* (finite ternary-center insertion-covering computations), https://www.brainsignals.de/users/cristian.grozea/combinatorial.html.
