# Exact Condorcet ambiguity from three-candidate position matrices

## Finding
For an election with three labeled alternatives \(A,B,C\), the position matrix retains the number of times each alternative occurs in each rank, but forgets the pairings of ranks within ballots. This result gives an exact, constant-size characterization of **every** election realizing a prescribed integer position matrix and of which alternatives can be its strict Condorcet winner. It also establishes sharp, parity-dependent first failures of Condorcet-winner identifiability from the matrix.

Write \((F_i,M_i,L_i)\) for the first-, middle-, and last-place counts of alternative \(i\). All three row sums and all three column sums equal the positive electorate size \(n\). Define the integers
\[
\ell=\max\{0,L_C-F_B,F_A-L_B\},\qquad
u=\min\{F_A,L_C,M_B\}.
\]
Every anonymous election realizing the matrix occurs **exactly once** in the following list, indexed by each integer \(t\in[\ell,\nu]\):
\[
\begin{array}{c|rrrrrr}
\text{ballot}&ABC&ACB&BAC&BCA&CAB&CBA\\\hline
\text{number}&t&F_A-t&L_C-t&F_B-L_C+t&L_B-F_A+t&M_B-t.
\end{array}
\]
A strict Condorcet winner exists in that realization precisely according to the mutually exclusive conditions
\[
\begin{array}{ll}
 A:&2(L_B+t)>n\quad\text{and}\quad 2(F_A+L_C-t)>n,\\
 B:&2(L_B+t)<n\quad\text{and}\quad 2(F_B+t)>n,\\
 C:&2(F_A+L_C-t)<n\quad\text{and}\quad 2(F_B+t)<n.
\end{array}
\]
Thus membership in the exact range of each possible Condorcet winner is a pair of integer inequalities; there is no search over ballot profiles. Across all realizations of one fixed matrix, **at most two** distinct alternatives can be Condorcet winners.

Two different strict Condorcet winners can occur for the same position matrix **only if** \(n\ge5\) when \(n\) is odd, or \(n\ge10\) when \(n\) is even. Both bounds are sharp. At \(n=5\), exactly three candidate-labeled position matrices have this ambiguity, namely the row permutations of
\[
\begin{pmatrix}2&2&1\\2&2&1\\1&1&3\end{pmatrix}.
\]
Each has exactly two anonymous realizations, with different strict Condorcet winners. At \(n=10\), again exactly three candidate-labeled matrices have this ambiguity, namely the row permutations of
\[
\begin{pmatrix}4&4&2\\4&4&2\\2&2&6\end{pmatrix}.
\]
Each has exactly three anonymous realizations: the two endpoints have different strict Condorcet winners and the middle has none. Here “row permutations” means assignment of the one exceptional row to any of the three labeled alternatives, not six distinct matrices.

For an impartial-culture random ordered profile conditioned on its rank matrix, the exact weight of the realization indexed by \(t\) is proportional to
\[
 w(t)=\frac{n!}{t!\,(F_A-t)!\,(L_C-t)!\,(F_B-L_C+t)!\,(L_B-F_A+t)!\,(M_B-t)!}.
\]
The sequence \(w(t)\) is strictly log-concave wherever it has at least three positive terms. Consequently, summing these explicit weights over the corresponding winner intervals gives the *complete conditional distribution* of the Condorcet outcome. At the first odd ambiguous matrix the two winners have probabilities \(1/2\) each. At the first even ambiguous matrix the two winners have probabilities \(3/22\) each, and no strict Condorcet winner has probability \(8/11\).

## Assumptions and scope
An election comprises \(n\ge1\) **strict, complete rankings** of precisely three labeled alternatives, with repetitions allowed. Its position matrix has candidate rows and rank columns, so that the three rank columns and candidate rows all sum to \(n\). A Condorcet winner must strictly beat each rival in head-to-head ballot counts; ties do not count. Elections are distinct anonymously when their six ballot multiplicities differ. For the conditional probability statement, the sample space instead consists of ordered profiles of \(n\) labeled voters under independent, uniform rankings, conditioned on the stated position matrix. No assumption of an odd electorate is made in the general classification.

## Proof
**Rank-fiber parametrization.** Let \(x_{ABC}=t\). First-place \(A\) fixes \(x_{ACB}=F_A-t\); last-place \(C\) fixes \(x_{BAC}=L_C-t\); first-place \(B\) then gives \(x_{BCA}=F_B-L_C+t\); last-place \(B\) gives \(x_{CAB}=L_B-F_A+t\); and middle-place \(B\) gives \(x_{CBA}=M_B-t\). The other rank equations follow from the equal row and column sums, and all multiplicities are nonnegative exactly when \(\ell\le t\le\nu\). This proves exhaustiveness, distinctness, and integrality of the displayed fiber.

**Majority inequalities.** The numbers of ballots preferring \(A\) to \(B\), \(B\) to \(C\), and \(A\) to \(C\) are respectively \(L_B+t\), \(F_B+t\), and \(F_A+L_C-t\). Comparing each against \(n/2\) yields the three stated conditions. For any strict Condorcet winner \(i\), summing its two head-to-head majority counts gives more than \(n\). The same sum is \(2F_i+M_i=n+F_i-L_i\); hence \(F_i>L_i\). Because \(\sum_i(F_i-L_i)=0\), at most two alternatives can satisfy this necessary condition.

**Sharp parity-dependent population thresholds.** Suppose two realizations in one fiber have different strict Condorcet winners, with respective parameters \(t<t+d\). Their winners differ on their own head-to-head comparison, which changes by precisely \(d\) votes toward one candidate (or in the reverse direction). Opposite strict majority signs force \(d\ge1\) for odd \(n\), and \(d\ge2\) for even \(n\), because a tie at \(n/2\) is not a strict win. The first realization contains at least \(d\) copies each of ballots \(ACB,BAC,CBA\), while the second contains at least \(d\) copies each of \(ABC,BCA,CAB\). Each such three-ballot block is a cyclic majority tournament, and \(d\) blocks give every candidate a head-to-head deficit of \(d\) against one rival. The remaining \(n-3d\) ballots can overturn that deficit to a strict win only if \(n-3d>d\). Thus \(n>4d\), giving \(n\ge5\) in the odd case and \(n\ge10\) in the even case.

**Completeness of the first layers.** At \(n=5\), the preceding inequalities force \(d=1\) and exactly two residual ballots outside a three-ballot cycle; at \(n=10\) with even \(n\), they force \(d=2\) and exactly four residual ballots outside two copies of a three-ballot cycle. After a cyclic candidate relabeling, the two different winners must be \(A\) for the \(ABC,BCA,CAB\) cycle and \(B\) for the reverse \(ACB,BAC,CBA\) cycle. To reverse both candidates' respective deficits against \(C\) into **strict** majorities at these population thresholds, all residual ballots must rank both \(A\) and \(B\) above \(C\). Hence they can only be \(ABC\) and \(BAC\). To make \(A\) beat \(B\) in the first realization and \(B\) beat \(A\) in the second, the two residual ballot types must occur equally often: once each at \(n=5\), twice each at \(n=10\). The three cyclic relabelings produce precisely the three claimed matrices, and their ballot-multiplicity vectors give respectively two and three distinct feasible values of \(t\). This proves exactness without extrapolating from a finite search.

**Exact conditional law and log-concavity.** Fixing the six ballot multiplicities leaves exactly \(n!/\prod_\pi x_\pi!\) ordered labeled-voter profiles. Every such profile has the same probability under impartial culture, hence the stated weights are exact. For adjacent feasible values,
\[
\frac{w(t+1)}{w(t)}=
\frac{(F_A-t)(L_C-t)(M_B-t)}{(t+1)(F_B-L_C+t+1)(L_B-F_A+t+1)}.
\]
This ratio strictly decreases as \(t\) increases, proving strict log-concavity in the interior. In the three \(n=5\) exceptional matrices, the two weights are \(60,60\); in the three \(n=10\) exceptional matrices, the weights are \(18900,100800,18900\). Normalization gives the asserted probabilities.

## Verification
Run `python verify.py` using Python 3. The exact-integer program enumerates all anonymous profiles with \(1\le n\le10\) (8,007 profiles and 6,291 different position matrices), independently computes their head-to-head Condorcet winners, reconstructs each complete matrix fiber from the formulas, checks all winner intervals and strict log-concavity, and exhaustively confirms the unique first odd ambiguity orbit. The program includes separate boundary assertions for the \(n=10\) layer, including its three matrices and exact conditional weights. These finite tests **support but do not replace** the all-\(n\) algebraic proof and the parity argument above.

## Relationship to prior work
Boehmer, Cai, Faliszewski, Fan, Janeczko, Kaczmarczyk, and Wąs, *Properties of Position Matrices and Their Elections* (first publicly submitted 2023-03-05, arXiv:2303.02538; AAAI 2023), study realizations of position matrices, prove general counting hardness, and give in Theorem 7 a necessary Condorcet-feasibility inequality. Their Section 5 studies feasibility computationally but does not give this exact three-alternative rank-fiber, the sharp parity-dependent first ambiguity thresholds, or the exact conditional law. Their general integer programming framework can solve individual finite instances; it is not itself the present closed structural classification. Related voting-method results distinguish Condorcet and Borda outcomes but do not determine all outcomes sharing the same full rank matrix. The present result is restricted to three candidates and does not contradict the general counting hardness involving variable candidate count.

## Limitations
The result does not classify higher-dimensional position-matrix fibers with four or more alternatives. The conditional probability is under uniform **ordered** voting profiles, not a uniform law on anonymous realizations, and it does not describe correlated voter models. The theorem gives no claim about strategic manipulation, turnout, or causality. A mathematically equivalent treatment in other positional-information literature remains a possible originality risk; the inaccessible full text of a later 2025 election-map treatment was not used to assert novelty. Independent mathematical verification has not been performed.

## References
1. N. Boehmer, J.-Y. Cai, P. Faliszewski, A. Z. Fan, Ł. Janeczko, A. Kaczmarczyk, T. Wąs, *Properties of Position Matrices and Their Elections*, arXiv:2303.02538, first submission 2023-03-05; AAAI 2023, pp. 5507–5514, doi:10.1609/aaai.v37i5.25684.
2. D. Black, *The Theory of Committees and Elections*, Cambridge University Press, 1958 (classical Condorcet and preferential voting background).
