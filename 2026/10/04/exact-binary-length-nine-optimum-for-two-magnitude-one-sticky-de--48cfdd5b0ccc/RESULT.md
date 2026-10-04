# Exact binary length-nine optimum for two magnitude-one sticky deletions
## Finding
For the binary limited-magnitude sticky-deletion model introduced by Shuche Wang, Van Khu Vu, and Vincent Y. F. Tan, use the explicit at-most convention from their Definition 6. For a source word \(x\in\{0,1}^9\), let \(E^{\le}_{2,1}(x)\) contain the no-error outcome and all words obtained by choosing at most two distinct runs of \(x\), each of length at least \(2\), and deleting exactly one repeated bit from each chosen run. A run is never deleted completely.

Let \(M^{\le}_{2,1}(9)\) be the largest cardinality of a set \(C\subseteq\{0,1}^9\) such that
\[
E^{\le}_{2,1}(x)\cap E^{\le}_{2,1}(y)=\varnothing
\]
for every two distinct \(x,y\in C\). Then
\[
M^{\le}_{2,1}(9)=120.
\]

The files `artifacts/codewords.txt` and `artifacts/weights.csv` are finite certificates for the lower and upper bounds, respectively.

## Assumptions and scope
A run is a maximal constant-symbol block. A magnitude-one sticky deletion removes one copy of a symbol from a run of length at least \(2\); because the removed symbols inside one run are indistinguishable at the word level, a chosen run produces a unique shortened run. The parameter \(t=2\) bounds the number of distinct affected runs, and \(\ell=1\) bounds the decrement in each affected run. The channel considered here includes zero, one, or two affected runs, matching the “at most” wording of Definition 6 in arXiv:2302.02754v1.

The claim is only for binary source length \(9\), \(t=2\), and \(\ell=1\). It does not classify all optimum codes and does not assert a formula at other lengths.

## Proof
The lower bound is direct. `artifacts/codewords.txt` contains \(120\) distinct binary words of length \(9\). The verifier reconstructs \(E^{\le}_{2,1}(x)\) from the run definition for each listed word and checks that all \(120\) error balls are pairwise disjoint. Hence \(M^{\le}_{2,1}(9)\ge 120\).

For the upper bound, let \(Y=\{0,1}^7\cup\{0,1}^8\cup\{0,1}^9\). The file `artifacts/weights.csv` specifies a nonnegative rational function \(w:Y\to\mathbb{Q}_{\ge0}\), with unlisted outputs assigned weight \(0\). Its \(154\) nonzero entries use only \(1/3\), \(1/2\), and \(1\), and satisfy
\[
\sum_{y\in Y}w(y)=120.
\]
Exact rational replay checks for every one of the \(512\) source words that
\[
\sum_{y\in E^{\le}_{2,1}(x)}w(y)\ge1.
\]
If \(C\) is any correcting code, its error balls are disjoint, so
\[
|C|\le \sum_{x\in C}\sum_{y\in E^{\le}_{2,1}(x)}w(y)
=\sum_{y\in \bigcup_{x\in C}E^{\le}_{2,1}(x)}w(y)
\le \sum_{y\in Y}w(y)=120.
\]
Thus \(M^{\le}_{2,1}(9)\le120\), proving equality.

## Verification
Run `python3 verify.py` beside the supplied `artifacts` directory. The verifier uses only the Python standard library and exact `Fraction` arithmetic. It reconstructs every error ball in two ways—by shortening selected maximal runs and by deleting selected original positions subject to distinct-run constraints—checks the two implementations agree on all \(512\) source words, validates the \(120\)-word packing, parses the rational upper certificate, checks its total weight, and tests the ball-weight inequality on all sources.

The committed replay reports `CODE_SIZE=120`, `CODE_BALL_UNION=403`, `NONZERO_WEIGHTS=154`, `TOTAL_WEIGHT=120`, `MIN_BALL_WEIGHT=1`, `TIGHT_SOURCE_BALLS=327`, `MAX_BALL_WEIGHT=4`, `POSITION_CROSSCHECK=512`, `ALL_CHANNEL_OUTPUTS=894`, and terminates with `VERIFY_OK`.

## Relationship to prior work
Wang, Vu, and Tan define a sticky deletion as removing repetition bits without deleting an entire run, then define \(t\) sticky deletions of \(\ell\)-limited magnitude by allowing at most \(t\) run-length coordinates to decrease, each by at most \(\ell\). They prove an equivalence with asymmetric limited-magnitude errors in their run representation and develop general non-systematic and systematic constructions with logarithmic redundancy. Their displayed special finite construction focuses on \(t=1\); the inspected full text does not state the exact binary length-nine \(t=2,\ell=1\) packing number proved here.

Earlier repetition-error work of Dolecek and Anantharam studies immunity to a prescribed total number of repetitions and gives asymptotic constructions and upper bounds. That model does not impose the present per-run magnitude-one restriction, so a result for two unrestricted repetition errors does not determine this two-distinct-run channel. The adjacent-transposition/deletion work arXiv:2301.11680 studies deletion/shift models and limited-magnitude blocks of zero-deletions, not this exact run-limited packing problem.

## Limitations
This is an exact finite result, not an asymptotic theorem. The proof establishes the optimum value but not uniqueness or a symmetry classification of optimum codes. The weighted certificate was discovered computationally, but its validity is purely finite and is replayed with exact rational arithmetic. A residual literature risk remains that an unindexed finite computation could contain the same small-parameter value; no inspected primary source or searched published-finding record stated it.

## References
1. Shuche Wang, Van Khu Vu, Vincent Y. F. Tan, “Codes for Correcting \(t\) Limited-Magnitude Sticky Deletions,” arXiv:2302.02754v1, first posted 2023-02-06.
2. Shuche Wang, Van Khu Vu, Vincent Y. F. Tan, “Codes for Correcting Asymmetric Adjacent Transpositions and Deletions,” arXiv:2301.11680v1, first posted 2023-01-27.
3. Lara Dolecek and Venkat Anantharam, “Repetition Error Correcting Sets: Explicit Constructions and Prefixing Methods,” SIAM Journal on Discrete Mathematics 23(4), 2120–2146, DOI 10.1137/080730093.
