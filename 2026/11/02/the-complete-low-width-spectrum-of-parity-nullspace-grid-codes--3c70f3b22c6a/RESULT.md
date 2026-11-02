# The complete low-width spectrum of parity-nullspace grid codes

## Finding

For every positive integer \(n\) and each width \(w\in\{1,2,3,4\}\), let \(G_{w,n}=P_w\square P_n\), with \(P_s\) the path on \(s\) vertices. Let \(C_{w,n}\subseteq\mathbb F_2^{wn}\) be the binary linear code of all vertex subsets \(S\) satisfying \(|S\cap N[v]|\equiv0\pmod2\) for every grid vertex \(v\), where \(N[v]\) is its **closed** neighborhood and the empty set is allowed. A nonzero codeword is a *nullspace matrix*. Put

\[
W_{w,n}(z)=\sum_{c\in C_{w,n}}z^{\operatorname{wt}(c)},\qquad h=n+1.
\]

The **complete Hamming weight enumerator** is as follows. Every case not listed has \(W_{w,n}(z)=1\) and dimension zero.

| Width | Condition | \(W_{w,n}(z)\) | Dimension | Generalized Hamming weights \((d_1,\ldots,d_k)\) |
|---|---|---|---|---|
| \(w=1\) | \(h=3t\) | \(1+z^{2t}\) | \(1\) | \((2t)\) |
| \(w=2\) | \(h=4t\) | \(1+3z^{4t}\) | \(2\) | \((4t,6t)\) |
| \(w=2\) | \(h\equiv2\pmod4\), \(h=2t\) | \(1+z^{2t}\) | \(1\) | \((2t)\) |
| \(w=3\) | \(h=6t\) | \(1+7z^{8t}\) | \(3\) | \((8t,12t,14t)\) |
| \(w=3\) | \(h\equiv3\pmod6\), \(h=3t\) | \(1+3z^{4t}\) | \(2\) | \((4t,6t)\) |
| \(w=4\) | \(h=5t\) | \(1+13z^{8t}+2z^{12t}\) | \(4\) | \((8t,12t,14t,16t)\) |

In these formulas \(t\) is a positive integer, and the congruence clauses exclude the full-dimensional case in the same width. For a \(k\)-dimensional code \(C\), \(d_r\) is the smallest number of coordinates in the union of the supports of an \(r\)-dimensional subcode, \(1\le r\le k\).

The first four widths therefore have a sharp qualitative boundary: every nonzero codeword at widths \(1,2,3\), for any fixed dimensions with a nontrivial code, has the **same** weight, but the family of four-row grids with \(n=5t-1\) is a two-nonzero-weight family with multiplicities \(13\) and \(2\). Its minimum distance is \(8t\), and its entire higher-support hierarchy is explicit.

An exact finite strengthening describes subcodes at every rank. For \(w=4\), \(n=5t-1\), the numbers of \(r\)-dimensional subcodes having union support of size \(s\) are:

| \(r\) | \(s\) and multiplicity |
|---|---|
| \(1\) | \(8t:13\), \(12t:2\) |
| \(2\) | \(12t:22\), \(14t:12\), \(16t:1\) |
| \(3\) | \(14t:4\), \(15t:8\), \(16t:3\) |
| \(4\) | \(16t:1\) |

These are *all* the subspaces at each rank, not a sample; the numbers of subcodes at ranks \(1,2,3,4\) are \(15,35,15,1\). For the other nonzero cases the full rank-support profiles are determined by the indicated dimension and weight, except the \(w=3\), \(h=6t\) case, where all seven one-dimensional subspaces have support \(8t\), all seven two-dimensional subspaces have support \(12t\), and the full space has support \(14t\).

For comparison with the existing *prime nullspace matrix* definition (nonzero array containing **no entirely zero row and no entirely zero column**), the exact number of such arrays among these four widths is \(1\) for \((w,n)=(1,2)\) or \((2,1)\), \(2\) for \((2,3)\) or \((3,2)\), \(4\) for \((3,5)\), and \(15\) for \((4,4)\), and is \(0\) otherwise. This last consequence should not be read as a claim of new primeness criteria: prior work already gives strong primeness results, especially for square boards.

## Assumptions and scope

Only ordinary Cartesian products of finite paths are considered, with open boundaries (no wraparound), nearest-neighbor horizontal/vertical edges, and closed-neighborhood parity over \(\mathbb F_2\). The empty array contributes the constant coefficient one. Arrays have labelled positions, and the enumerator does not quotient by rotations or reflections. All statements hold for *every* positive length \(n\) in the specified four widths. The nullspace codes are not assumed to contain a strictly positive even number of selected neighbors at every vertex; zero is allowed.

## Proof

**1. Deterministic column recurrence.** Fix a width \(w\) and represent each column by a vector in \(\mathbb F_2^w\). Put \(B_w=I_w+A(P_w)\), the tridiagonal matrix with diagonal and neighboring entries equal to one. Writing the columns \(v_1,\ldots,v_n\), the closed-neighborhood parity equations are equivalent, *including the two boundary columns*, to

\[
v_0=v_{n+1}=0,\qquad v_{j+1}=B_wv_j+v_{j-1}\quad(1\le j\le n).
\]

Thus every pattern is uniquely determined by its first column \(a=v_1\). Set \(F_0(X)=0\), \(F_1(X)=I\), and \(F_{j+1}(X)=X F_j(X)+F_{j-1}(X)\) for a matrix \(X\). Then \(v_j=F_j(B_w)a\), and admissibility is exactly \(F_{n+1}(B_w)a=0\). In particular, no patterns are missed by the seed enumeration.

**2. Finite exact period/rank identities.** Direct multiplication over \(\mathbb F_2\) gives the following table, listing the *ranks* of \(F_j(B_w)\) from \(j=1\) through the first zero matrix:

| \(w\) | First zero index \(p_w\) | Ranks \(\operatorname{rank}F_1,\ldots,\operatorname{rank}F_{p_w}\) |
|---|---|---|
| 1 | 3 | \((1,1,0)\) |
| 2 | 4 | \((2,1,2,0)\) |
| 3 | 6 | \((3,3,1,3,3,0)\) |
| 4 | 5 | \((4,4,4,4,0)\) |

These identities are finite matrix equalities, not numerical extrapolations. The polynomial addition identity \(F_{p+j}(B)=F_{p+1}(B)F_j(B)+F_p(B)F_{j-1}(B)\) follows by induction on \(j\). Whenever \(F_p(B)=0\), the transfer operator \((x,y)\mapsto(y,x+By)\) is invertible, so \(D=F_{p+1}(B)=F_{p-1}(B)\) is invertible. Consequently \(F_{p+j}(B)=D F_j(B)\); iterating shows that \(\ker F_h(B)\) and its dimension depend only on \(h\bmod p\). The displayed ranks establish all allowable initial-column spaces and their dimensions.

**3. Reflection and exact multiplicity scaling.** Suppose the admissible first columns for a fixed residue class satisfy \(F_p(B_w)a=0\), with \(p\) respectively \(3,4,2,6,3,5\) in the six cases in the first table. At column \(p\), the vector is zero, and the recurrence forces \(v_{p+j}=v_{p-j}\) for \(1\le j<p\). Repeating at columns \(2p,3p,\ldots\) shows that a pattern of length \(pt-1\) consists of \(t\) disjoint reflected copies of the original \((p-1)\)-column pattern, separated by zero columns. The same is true simultaneously for all words in any subcode. Both single-word weights and union-support sizes are therefore multiplied by exactly \(t\), while the subspace counts remain unchanged. The case \(w=2\), \(p=2\) uses the seed kernel \(\ker B_2\); the case \(w=3\), \(p=3\) uses \(\ker(B_3^2+I)\). Cases not in the table have only the zero word by Step 2.

**4. Exhaustive, fully specified finite base calculations.** To make every base value reproducible, index seed bits from top to bottom, and for each seed \(a\in\{0,\ldots,2^w-1\}\) compute \(v_0=0\), \(v_1=a\), and \(v_{j+1}=B_wv_j+v_{j-1}\). Retain only seeds with \(v_{p}=0\). Each retained seed produces a distinct base word. The base nonzero Hamming weights are:

| Base size | Nonzero seed values and weight |
|---|---|
| \(1\times2\) | \(1:2\) |
| \(2\times1\) | \(3:2\) |
| \(2\times3\) | \(1:4,\ 2:4,\ 3:4\) |
| \(3\times2\) | \(2:4,\ 5:4,\ 7:4\) |
| \(3\times5\) | \(1:8,\ 2:8,\ 3:8,\ 4:8,\ 5:8,\ 6:8,\ 7:8\) |
| \(4\times4\) | \(1\) through \(15\): \(13\) words of weight \(8\); seeds \(9\) and \(15\) have weight \(12\) |

For higher-support enumeration, take every \(r\)-tuple of distinct nonzero base words, form its binary span, discard tuples of span dimension less than \(r\), deduplicate spans by their complete member sets, and count the union of supports. This gives the exact rank-support tables above (for the four-row case: \(13/2\), \(22/12/1\), \(4/8/3\), \(1\) across ranks). All seed states and subspaces are finite and exhaustively specified, so this is an exact combinatorial count, not a heuristic sample. Applying Step 3 proves the formulas for every length.

**5. Primeness count.** A repeated construction with \(t\ge2\) has an interior all-zero column, so cannot be prime. If a code is trivial, it has no nonzero prime word. In the six base cases, inspecting all admitted seeds shows prime seed lists \(\{1\}\), \(\{3\}\), \(\{1,2\}\), \(\{2,7\}\), \(\{1,3,4,6\}\), and \(\{1,\ldots,15\}\), respectively. These explicit lists also directly check the zero-row exclusion. Counting them yields the final prime table; antecedent square-grid primeness conditions are credited below.

## Verification

Execute `python3 verify.py` from this package. The standalone standard-library verifier reconstructs the column recurrence, checks the predicted weight polynomial for every \(w\in\{1,2,3,4\}\) and \(1\le n\le72\), and independently verifies all parity equations. It enumerates every subspace at each rank in all six base codes and checks exact support histograms. It checks all base and longer prime counts and, separately, enumerates all binary arrays on the small grids with at most \(16\) cells using the closed-neighborhood equations without referring to the recurrence. The replay output is:

`VERIFY_OK width_length_cases=288 base_support_cases=6 matrix_rank_identities=4 direct_assignments=74954`

The infinite-length conclusion follows from the displayed recurrence and reflection argument, not from the finite computational checks.

## Relationship to prior work

The column recurrence, the Fibonacci-polynomial treatment of parity domination, the count of all nullspace solutions via binary nullity, and zero-row reflection are classical, as presented in Goldwasser–Klostermeyer–Ware (2002), Goldwasser–Klostermeyer (2005), and the more recent Klostermeyer (2026). They are used here, not claimed as discoveries. Existing square-board treatments also exhibit the four-by-four nullspace and existing prime-nullspace criteria; no new general primeness criterion is asserted. The contribution isolated here is the *entire cardinality spectrum for all lengths at widths one through four*, its explicit distinction between the first constant-weight and first two-weight families, and the **complete** four-row subcode-support spectrum and generalized weight hierarchy over arbitrarily long strips. None of those detailed enumerators is stated in the materials inspected for comparison.

## Limitations

The classification is restricted to widths \(1\) through \(4\), ordinary path products, closed-neighborhood parity over \(\mathbb F_2\), and labelled arrays. It is not a general theorem for arbitrary rectangular widths or for positive even domination, nor does it count orbit classes under symmetry. The earlier 2002 *Fibonacci Polynomials and Parity Domination in Grid Graphs* paper could not be inspected in its complete original text; its full historical treatment of weight distributions is a residual priority risk even though accessible accounts present existence and total-count results. Other prior descriptions under Lights Out quiet-pattern, binary-code, or cellular-automaton language could also imply parts of this specialized enumeration. No independent proof audit has been performed.

## References

1. William F. Klostermeyer, *Prime Nullspace Matrices and Even Dominating Sets* (2026), arXiv:2610.31475, version 1 dated 2026-10-22. https://arxiv.org/html/2610.31475v1
2. J. Goldwasser, W. Klostermeyer, and H. Ware, *Fibonacci Polynomials and Parity Domination in Grid Graphs*, Graphs and Combinatorics 18 (2002), 271–283. DOI:10.1007/s003730200020.
3. J. Goldwasser and W. Klostermeyer, *Parity Dominating Sets in Grid Graphs*, Congressus Numerantium (2005), publicly available author-uploaded full text: https://www.researchgate.net/publication/250342861_Parity_Dominating_Sets_in_Grid_Graphs
4. *The Lights Out Puzzle: Solution*, archival exposition of binary grid nullspaces and four-by-four patterns: https://people.sc.fsu.edu/~jburkardt/fun/puzzles/lights_out_solution.html
