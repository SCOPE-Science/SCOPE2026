# First nondecomposable two-list single-deletion codebooks at length seven

## Finding

For \(n\geq 1\), let \(M_2(n)\) be the largest cardinality of a binary block code \(C\subseteq\{0,1\}^n\) in which every length-\(n-1\) word occurs as a subsequence of at most two **distinct** codewords. The exact initial capacity sequence is

\[
(M_2(1),M_2(2),M_2(3),M_2(4),M_2(5),M_2(6),M_2(7))
=(2,3,4,7,12,19,33).
\]

For all \(1\leq n\leq6\), the optimum is attained by a disjoint union of two Varshamov–Tenengolts single-deletion-correcting syndrome classes. At \(n=7\), the two largest such classes have total size \(32\), whereas \(M_2(7)=33\). Moreover the maximum size of any uniquely single-deletion-correcting binary length-seven code is \(16\). Consequently **no optimal length-seven two-list code is a union of two uniquely single-deletion-correcting codes**, and length seven is the first blocklength at which decomposable optimality fails.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), with the two symbols distinguished. For \(x=x_1\cdots x_n\), its one-deletion set is

\[
D_1(x)=\{x_1\cdots x_{i-1}x_{i+1}\cdots x_n:1\leq i\leq n\},
\]

with repeated outcomes counted only once. A code \(C\) is *two-list single-deletion decodable* precisely when \(|\{x\in C:y\in D_1(x)\}|\leq2\) for every \(y\in\{0,1\}^{n-1}\). At \(n=1\), the unique output is the empty word. The comparison with uniquely decodable codes uses the analogous upper bound one, not pairwise multiplicities of deletion positions.

## Proof

**1. Exact finite optimization.** For each binary \(x\) of length \(n\), introduce \(u_x\in\{0,1\}\). Writing \(P(y)=\{x:y\in D_1(x)\}\), the exact maximum-code problem is

\[
\max\sum_x u_x\quad\text{subject to}\quad
\sum_{x\in P(y)}u_x\leq2\quad(\forall y\in\{0,1\}^{n-1}).
\]

There is no relaxation in this equivalence: codewords correspond bijectively to coordinates equal to one.

**2. Explicit lower bounds.** The accompanying `certificate.json`, under `capacities`, contains full sets of \(M_2(n)\) word indices for each \(1\leq n\leq7\), using fixed-width binary encoding. For clarity, one 33-word length-seven code is:

```text
0000000 0000011 0000111 0001000 0001010 0001110 0010101 0011100 0011111 0100010 0101000
0101101 0110001 0110110 0110111 0111001 1000001 1001001 1001011 1001100 1001111 1010010
1011010 1011110 1100000 1100011 1100110 1110000 1110101 1110111 1111000 1111100 1111111
```

The pure-Python verifier reconstructs every distinct one-deletion output and checks that no output has more than two parents in any listed code. It similarly verifies a length-seven 16-word uniquely decodable witness.

**3. Exact rational upper-bound certificates.** Fix a branch with some coordinates \(u_x\) set to zero or one. Let \(S\) be those fixed to one, \(U\) the free coordinates and \(b_y=2-|S\cap P(y)|\). If any \(b_y<0\), the branch is infeasible. Otherwise for arbitrary nonnegative rational weights \(\lambda_y\), every feasible continuation satisfies

\[
|C|\leq |S|+\sum_y\lambda_y b_y+
\sum_{x\in U}\max\left(0,1-\sum_{y\in D_1(x)}\lambda_y\right).
\tag{1}
\]

Indeed the constraints yield \(\sum_{x\in U}u_x\sum_{y\in D_1(x)}\lambda_y\leq\sum_y\lambda_y b_y\), while \(u_x\leq1\) bounds each remaining nonnegative deficit. The right side of (1) is evaluated as an **exact rational number** in the certificate checker, not by floating-point optimization.

For each \(1\leq n\leq6\), a single rational-dual leaf certifies the strict upper bound \(M_2(n)+1\). At \(n=7\), the certificate is a complete zero/one decision tree with exactly 101 nodes and 51 leaves; every leaf has a rational bound strictly below \(34\), or a violated integer-capacity constraint. Its two branches at each internal node exhaust all possible codebooks. Thus \(M_2(7)\leq33\), matching the displayed code.

**4. Structural threshold.** The same bound (1), with the capacity \(2\) replaced by \(1\), has a complete 25-node, 13-leaf exact rational decision-tree certificate for \(M_1(7)\leq16\), where \(M_1\) denotes unique one-deletion decoding. Its accompanying 16-word witness proves equality. Two such codes can therefore contain at most \(32\) distinct words in their union, strictly less than \(M_2(7)=33\).

For smaller lengths the verifier enumerates syndrome classes

\[
\operatorname{VT}_a(n)=\left\{x\in\{0,1\}^n:\sum_{i=1}^n i x_i\equiv a\pmod{n+1}\right\}.
\]

Each class is uniquely one-deletion decodable (a classical result); the two largest disjoint classes have sizes \(2,3,4,7,12,19\) at lengths \(1,2,3,4,5,6\), respectively. They meet the independently certified two-list upper bounds at those lengths. Therefore length seven is the first nondecomposable optimum.

## Verification

With Python 3 and the files `verify.py` and `certificate.json` in the same directory, run:

```bash
python verify.py
```

The checker uses only the Python standard library (`fractions.Fraction`, `json`, `pathlib` and `sys`). It enumerates deletion sets independently from the optimization formulation; checks each codebook's distinct parent counts; reconstructs all rational dual bounds from sparse certificate entries; verifies every branch covers both values of a free binary variable; checks the 101-node two-list and 25-node unique-decoding trees; and computes the two-largest-syndrome-class comparison. The recorded successful output is in `verify_output.txt`. No external MILP solver, network connection or unrecorded search log is needed to *check* the certificate.

## Relationship to prior work

Lin's September 22, 2026 paper [1] defines exactly the relevant list-deletion hypergraph and establishes asymptotic lower bounds; its proof for a single deletion uses unions of Varshamov–Tenengolts classes. It does **not** state this exact finite length-seven capacity or its nondecomposability threshold. No's 2019 work [2] treats the unique-decoding case, including the known optimality of Varshamov–Tenengolts codes at length seven; the rational certificate here independently reproduces that particular unique-decoding bound. Song, Cai and Nguyen [3] construct two-list codes for the *more restrictive* joint deletion–substitution channel, without an exact optimum at length seven for the deletion-only channel. These are different assertions: an asymptotic existence bound, a unique-decoding optimum and a stronger-channel construction do not imply the exact two-list packing optimum.

## Limitations

The exact classification is limited to \(1\leq n\leq7\), a binary alphabet, precisely one deletion and maximum decoder list size two. It makes no assertion about \(n\geq8\), larger list sizes, fractional list decoding or deletion-plus-substitution channels. Exact finite verification establishes the stated theorem for the specified sizes; it is not a proof of any asymptotic capacity. Literature searches cannot exclude unindexed or unpublished priority claims, and independent mathematical audit remains outstanding.

## References

1. Andrew D. Lin, *Lower Bounds for all List-Decodable Deletion Codes*, arXiv:2609.26650v1, first submitted September 22, 2026. https://arxiv.org/abs/2609.26650
2. Albert No, *Nonasymptotic Upper Bounds on Binary Single Deletion Codes via Mixed Integer Linear Programming*, Entropy 21(12), 1202 (2019). https://doi.org/10.3390/e21121202
3. Wentu Song, Kui Cai and Tuan Thanh Nguyen, *List-decodable Codes for Single-deletion Single-substitution with List-size Two*, arXiv:2201.02013v2 (2022). https://arxiv.org/abs/2201.02013
