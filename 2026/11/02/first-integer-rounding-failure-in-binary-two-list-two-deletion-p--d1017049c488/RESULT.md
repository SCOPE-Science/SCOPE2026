# First integer-rounding failure in binary two-list two-deletion packing

## Finding
For binary words of length \(n\ge2\), let \(M_n\) be the maximum size of a code such that every received word obtained by deleting exactly two positions has at most two **distinct** codeword parents. Let \(F_n\) be the optimum of the natural bounded deletion-shadow packing linear program defined below. Then
\[
M_8=15,\qquad F_8=\frac{2188}{135},\qquad \lfloor F_8\rfloor=16>15.
\]
For every integer \(2\le n\le7\), in contrast, \(M_n=\lfloor F_n\rfloor\). Thus length eight is the first point at which even integer-rounding of this natural LP bound fails. The exact earlier maximum code sizes for \(n=2,3,4,5,6,7\) are \(2,3,4,4,7,11\), respectively; these values serve as the boundary comparison, not an independent novelty claim.

## Assumptions and scope
The alphabet is \(\{0,1\}\). A received word \(y\) has length \(n-2\). Define \(\mathcal D_2(x)\) as the **set**, without multiplicities, of all distinct outputs obtained from a length-\(n\) word \(x\) after deleting precisely two coordinates. Define the binary incidence matrix \(A_n\) by \(A_n[y,x]=1\) if and only if \(y\in\mathcal D_2(x)\). The code is arbitrary, possibly nonlinear, and a list may contain at most two distinct source words. Define
\[
M_n=\max\{\sum_x z_x:A_nz\le2\mathbf1,\ z_x\in\{0,1\}\},
\]
\[
F_n=\max\{\sum_x z_x:A_nz\le2\mathbf1,\ 0\le z_x\le1\}.
\]
Coordinates of the columns are indexed lexicographically by all binary length-\(n\) words, equivalently the integers from \(0\) through \(2^n-1\) with fixed-length binary padding. Rows are similarly indexed by length-\(n-2\) words. This normalization uniquely fixes the finite certificate.

## Proof
**Attainment.** The fifteen column indices
\[
0,15,24,31,41,67,115,150,188,194,205,224,239,244,255
\]
form a feasible code for \(n=8\). The exact verifier constructs all \(\binom82\) deletion patterns per codeword, merges equal outputs, and checks that every one of the \(64\) received-word rows contains at most two selected columns. Thus \(M_8\ge15\).

**Fractional optimum.** The certificate records a rational feasible vector \(z\) satisfying all \(64\) inequalities and \(0\le z_x\le1\), with exact objective \(2188/135\). It separately records rational nonnegative dual weights \(\lambda_y\). For any such \(\lambda\), the LP objective is bounded by
\[
2\sum_y\lambda_y+\sum_x\left(1-\sum_{y\in\mathcal D_2(x)}\lambda_y\right)_+,
\]
where \(a_+=\max\{0,a\}\). This follows by multiplying each row-capacity constraint by \(\lambda_y\), and using \(z_x\le1\) for positive residual coefficients. The supplied dual weights attain exactly \(2188/135\), matching the feasible primal. Hence \(F_8=2188/135\).

**Integer upper bound.** The standalone \(205\)-node binary search certificate establishes that no feasible code contains \(16\) words. Each internal node branches exhaustively on the inclusion or exclusion of one as-yet-undecided binary word. At a node, let \(S\) be the already included columns, \(R\) the available columns, and \(c_y=2-|\{x\in S:y\in\mathcal D_2(x)\}|\) the residual row capacities. Saturated rows force all not-yet-selected incident columns to be excluded. Each terminal leaf stores nonnegative exact rational row weights \(\lambda_y\), yielding the rigorous bound
\[
|S|+\sum_y c_y\lambda_y+\sum_{x\in R}\left(1-\sum_{y\in\mathcal D_2(x)}\lambda_y\right)_+<16.
\]
There are \(102\) complete binary branches and \(103\) terminal rational-dual leaves, with depth at most \(13\). A dependency-free verifier reconstructs every incidence relation and checks all leaf inequalities using integer rational arithmetic, as well as exact exhaustive branch coverage. Thus \(M_8\le15\), proving equality.

**First such blocklength.** For each \(n=2,3,4,5,6,7\), the certificate contains a feasible integer code of size \(2,3,4,4,7,11\), respectively, and an exact rational dual bound strictly smaller than the next integer. Accordingly \(M_n=\lfloor F_n\rfloor\) throughout this full preceding range. The computed rational bounds for \(n=6\) and \(n=7\) are \(36/5\) and \(666/59\), respectively. The length-eight fractional optimum lies above \(16\), while the integer optimum is only \(15\), establishing the claimed first failure.

## Verification
Run `python verify.py CERTIFICATE.json` from the directory containing those two files. This verifier uses only the Python standard library. It independently generates the binary deletion incidences; validates all integer witnesses, rational primal and dual inequalities; and recursively replays the entire search certificate without numerical optimization or trusting solver logs. A matching output is included as `VERIFICATION_OUTPUT.txt`. The exact result hinges on the included certificate and on the verifier's transparent finite enumeration; finite computations do not establish an asymptotic theorem.

## Relationship to prior work
Lin, *Lower Bounds for all List-Decodable Deletion Codes* (arXiv:2609.26650v1, first posted September 22, 2026), studies asymptotic existence of list-decodable deletion codes and introduces the associated deletion hypergraphs. The present result instead resolves a small-block exact packing and the first failure of a natural fractional bound. Guruswami and Håstad, *Explicit two-deletion codes with redundancy matching the existential bound* (arXiv:2007.10592), provide asymptotic explicit list-two constructions. Previously reported finite results include the length-six two-list/two-deletion optimum \(7\) and the length-seven optimum \(11\); neither implies the length-eight fractional/integer separation. No claim is made to improve the asymptotic rate bound or to rediscover these earlier exact cases.

## Limitations
The result concerns binary alphabets, precisely two deletions, list allowance two, and the specific bounded packing LP. No statement is made for other blocklengths beyond the displayed comparison, other list sizes, other error models, decoding algorithms, or asymptotic rates. The priority assessment may miss an implicit appearance of this finite bound in an older exact-code table or integer-packing literature. The scientific proof is computational but exactly checkable; no independent mathematical audit has been performed.

## References
- A. D. Lin, *Lower Bounds for all List-Decodable Deletion Codes*, arXiv:2609.26650v1 (2026-09-22), https://arxiv.org/abs/2609.26650.
- V. Guruswami and J. Håstad, *Explicit two-deletion codes with redundancy matching the existential bound*, arXiv:2007.10592 (2020-07-21), https://arxiv.org/abs/2007.10592.
