# Binary single-deletion list capacity through length seven and the first strict two-class size gap

## Finding

For \(n\ge1\) and integer \(L\ge1\), write \(M(n,L)\) for the maximum size of a binary length-\(n\) code such that **each** received word of length \(n-1\) can result from deleting one symbol from at most \(L\) **different codewords**. Then the complete length-seven profile is

\[
\big(M(7,L)\big)_{L=1}^{8}=(16,33,50,65,81,96,112,128).
\]

For lengths \(1\le n\le6\), the exact \((M(n,1),M(n,2))\) pairs are

\[
(1,2),\ (2,3),\ (2,4),\ (4,7),\ (6,12),\ (10,19).
\]

Consequently, length seven is the **smallest binary block length** where the optimal list-two cardinality exceeds twice the optimal list-one cardinality: \(M(7,2)=33>2M(7,1)=32\), while \(M(n,2)\le 2M(n,1)\) for all \(n\le6\). This strict cardinality gap is the structural content of the finite classification. In particular, the 33-word witness is not a union of two list-one codes; this does not claim that no smaller *nondecomposable* list-two code exists.

## Assumptions and scope

A code is an arbitrary *set* of fixed-length binary words; it is not required to be linear. A deletion shadow \(\Delta(x)\) is the *set* of all distinct length-\(n-1\) subsequences formed by removing exactly one coordinate of \(x\). Deleting different coordinates that produce the same received word contributes **only one** possible codeword to a decoder's list. The constraint is \(\#\{x\in C:y\in\Delta(x)\}\le L\) for every \(y\). All codes and decoding lists use this ordinary adversarial single-deletion model. The exact length-seven profile includes every meaningful \(L\) up to the maximum possible list length \(8\); for \(L\ge8\) the full 128-word code is admissible.

## Proof

Put \(X=\{0,1\}^n\), \(Y=\{0,1\}^{n-1}\), and \(A_{y,x}=1\) precisely if \(y\in\Delta(x)\), and \(0\) otherwise. The exact finite problem is the binary integer linear program

\[
\max\sum_{x\in X}z_x\quad\text{subject to}\quad
\sum_{x\in X}A_{y,x}z_x\le L\ (y\in Y),\qquad z_x\in\{0,1\}.
\]

Indeed the support of any admissible \(z\) is a deletion-list code and conversely every such code gives exactly this feasible support. Thus no search-space reduction or symmetry assumption is needed. Enumerating all \(2^n\) columns and \(2^{n-1}\) rows creates the entire finite instance. The supplied `verify.py` generates the matrix in two distinct ways: once by forming deletion shadows of all codewords, and once by inserting either bit into all possible positions of each received word; it asserts equality entrywise. The latter check also establishes that each binary length-\(n-1\) received word has exactly \(n+1\) distinct one-symbol supersequences.

For \(n=7\), `witnesses.json` supplies eight separate integer feasible vectors (explicit lists of length-seven words) attaining the eight asserted optima. The verifier checks every received word against every supplied list. In addition, the verifier solves the complete binary linear program with SciPy's HiGHS mixed-integer optimizer for each \(L=1,\dots,8\), verifies successful proven-optimal termination, integrality, and the primal and dual bounds tight enough to exclude the next larger integer. The resulting integer optima, in order, are exactly \(16,33,50,65,81,96,112,128\). For \(1\le n\le6\), the same exhaustive finite formulation is solved for \(L=1,2\), giving the six claimed pairs. The enumeration is exhaustive **as a mathematical reduction**, while the actual integer lower/upper optimality checks rely on complete trusted mixed-integer optimization, not on a handwritten branch-tree certificate.

For clarity on the structural consequence, partition the 128 length-seven words by their Varshamov–Tenengolts syndromes \(\sum_{i=1}^{7}i x_i\pmod 8\). The eight classes each have 16 words and each class has mutually disjoint deletion shadows; the verifier checks both facts directly. More generally, any union of two list-one codebooks has size at most \(2M(n,1)\), whether or not the two codebooks overlap. The exhibited 33-word list-two code at length seven therefore **cannot** equal such a union. The exact first-six-length capacities rule out an earlier **capacity gap** of this type; they do not settle whether smaller, non-maximum codes can be nondecomposable.

## Verification

Run `python verify.py` from the directory containing `verify.py` and `witnesses.json`, with Python 3, NumPy and SciPy (tested with SciPy 1.17.0). This runs all 14 relevant small-instance integer programs, the full length-seven feasible-witness checks, independently formed incidence matrices, and the 8-class VT verification; the expected final output is `VERIFY_OK`. No network access is needed. The code asserts the continuous solver dual bound is sufficiently strong to exclude the next integer value and rejects any nonoptimal or timed-out MILP solve. Actual complete execution of the packaged script returned `VERIFY_OK` in the described environment.

## Relationship to prior work

Kiah, Wei and Zeng (2026) study fixed-list insertion/deletion decoding and establish both asymptotic bounds and a finite-length run-counting upper bound (Theorem 23). **Their actual bound**, specialized to binary length seven, exactly one deletion and a list of two, gives

\[
|C|\le\min_{0\le r\le6}\left(\frac{128}{r+1}+2\sum_{j=0}^{r-1}\binom{6}{j}\right)=\frac{170}{3},
\]

with the empty sum interpreted as zero. It thus does not imply the exact bound 33. The full HTML of that source and Con, Doron and Ribeiro's 2026 capacity paper was inspected in relevant sections. The latter studies asymptotic insertion/deletion list capacities rather than this finite exact vector. No (2019) develops finite mixed-integer bounds for **unique** deletion decoding, not for exact list-size-two and higher optima. The new finite profile and the strict two-class capacity gap are not stated or implied by the inspected source results. An earlier exact table cannot be excluded by searches alone.

## Limitations

These numbers address exactly **one deletion**, binary words, and the indicated short lengths. The code and numerical solver logs are finite, replayable computation, not a purely symbolic proof of every integer upper bound; no independent, software-free branch-and-bound certificate is included. No capacity statement for unbounded length or more than one deletion is inferred. A previously unindexed exact finite table remains possible; the live original of No (2019) could not be completely accessed, although substantive sections were available through indexing.

## References

1. H. M. Kiah, H. Wei and R. Zeng, *Constant-List Insertion--Deletion Codes: New Bounds and an Improvement of Levenshtein's Lower Bound*, arXiv:2609.21395 (first publicly posted 2026-09-18).
2. G. Con, E. Doron and A. Ribeiro, *The Insertion List-Decoding Capacity and an Improved Bound on the Deletion List-Decoding Capacity*, arXiv:2607.03989 (2026).
3. A. No, *Nonasymptotic Upper Bounds on Binary Single Deletion Codes via Mixed Integer Linear Programming*, *Entropy* 21 (2019), article 1202, doi:10.3390/e21121202.
