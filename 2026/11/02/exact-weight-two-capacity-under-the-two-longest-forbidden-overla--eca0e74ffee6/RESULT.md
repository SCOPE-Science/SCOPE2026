# Exact weight-two capacity under the two longest forbidden overlaps

## Finding

For every integer \(n\geq4\), the maximum cardinality of a set of binary length-\(n\) words of Hamming weight exactly two with **no prefix–suffix matches of length \(n-2\) or \(n-1\)**, between any ordered pair of codewords including a word with itself, is

\[
M(n)=\left\lfloor\frac{n-1}{2}\right\rfloor\left\lfloor\frac n3\right\rfloor
+\mathbf1_{\{2\mid n\}}\left\lfloor\frac n6\right\rfloor.
\]

A constructive code attaining this bound is given below for every \(n\). Its asymptotic density within the binary weight-two layer \(\binom n2\) tends to \(1/3\). The parity correction counts the exceptional antipodal rotation orbit at even lengths.

## Assumptions and scope

A binary length-\(n\) word is indexed at coordinates \(0,\dots,n-1\). Its support is the set of positions containing ones. For a word \(x\), let \(\operatorname{pre}_t(x)\) and \(\operatorname{suf}_t(x)\) denote its first and last \(t\) symbols, respectively. A code \(\mathcal C\) is admissible precisely when

\[
\operatorname{pre}_t(x)\ne\operatorname{suf}_t(y)
\quad\text{for all }x,y\in\mathcal C,\quad t\in\{n-2,n-1\}.
\]

Self-pairs \(x=y\) are not exempted. This is a restricted-overlap or weakly mutually uncorrelated constraint with minimum forbidden overlap \(n-2\), **not** a Hamming-distance constraint and **not** the condition forbidding all proper overlaps. The alphabet is binary and each word has exactly two ones. There are no restrictions at lengths below \(n-2\).

## Proof

**Rotation-orbit upper bound.** Each support of size two lies in exactly one cyclic-rotation orbit labeled by the shorter directed separation \(d\), with \(1\le d\le\lfloor n/2\rfloor\). If \(2d<n\), the orbit has \(P_d=n\) distinct words. If \(2d=n\), the two markers are antipodal and the orbit has \(P_d=n/2\) distinct words. These orbits partition the \(\binom n2\) possible words. In one orbit, a word and its rotation by one or two positions have a forbidden match of length \(n-1\) or \(n-2\), respectively; this also applies to a rotation returning the same word. Consequently the selected rotation phases must be separated by at least three steps on the cyclic group of order \(P_d\). Every such selection has at most \(\lfloor P_d/3\rfloor\) words, including the short antipodal orbit with \(P_d=2\), for which the self-overlap excludes its words. Summing the orbit bounds proves

\[
|\mathcal C|\le\sum_{1\le d<n/2}\left\lfloor\frac n3\right\rfloor
+\mathbf1_{\{2\mid n\}}\left\lfloor\frac{n/2}{3}\right\rfloor=M(n).
\]

**Explicit construction.** For every \(d=1,\dots,\lfloor n/2\rfloor\), put \(P_d=n\) unless \(2d=n\), in which case put \(P_d=n/2\). For each integer \(j\) with \(0\le j<\lfloor P_d/3\rfloor\), include the unique binary word with support

\[
\{r,(r+d)\bmod n\},\qquad r=3j.
\]

The indicated words are distinct: a non-antipodal support has a unique start of its shorter directed separation, while an antipodal support has a unique representative \(0\le r<n/2\). The number of constructed words is the upper-bound sum.

**Checking cross-orbit overlaps.** Write a constructed support as \(\{r,s\}\), where \(s=(r+d)\bmod n\), and let \(k\in\{1,2\}\). A possible prohibited overlap after dropping the first \(k\) symbols would have the form \(y=x_kx_{k+1}\cdots x_{n-1}z\), with an arbitrary binary tail \(z\) of length \(k\). Because \(y\) must also have weight two, the number of ones in \(z\) equals the number of ones among the dropped \(k\) positions. We show that no such \(y\) belongs to the construction.

If neither marker is dropped, then \(r\ge3\) (otherwise position zero is marked). The shorter directed separation remains \(d\) and its chosen starting coordinate becomes \(r-k\), which is positive but not divisible by three. For antipodal pairs, the representative is also \(r-k\) in the prescribed half-period. Therefore \(y\) is not selected.

If both markers are dropped, necessarily \(k=2\) and \(\{r,s\}=\{0,1\}\). To preserve weight two, the two appended symbols are ones, giving the new support \(\{n-2,n-1\}\). Its shorter-gap representative is \(n-2\), larger than every construction start (whose maximum is at most \(n-3\)); thus it is not selected.

Suppose exactly one marker is dropped. If the dropped marker is \(r\), then \(r=0\). The surviving marker moves to \(d-k\), and the appended one has coordinate \(u\in\{n-k,\ldots,n-1\}\). The short directed separation starts at \(u\), which is too close to the end of the word to be a construction start; in the antipodal tie its canonical representative \(u\bmod(n/2)\) is one of the last two positions in the half-period, also beyond the permitted start \(P_d-3\).

Otherwise the dropped marker is \(s\), so \(r\ge3\) and \(s\in\{0,\ldots,k-1\}\). In particular this is not the antipodal case, and \(r+d=n+s\). The surviving marker moves to \(r-k\); the newly appended marker is \(u=n-k+j\) for some \(0\le j<k\). Their forward separation from \(r-k\) to \(u\) is \(d-s+j\). If it is strictly less than \(n/2\), the canonical starting coordinate \(r-k\) is not divisible by three. If it is strictly greater than \(n/2\), the canonical start is \(u\), too large to be a construction start. Equality is possible only for even \(n\), with \(k=2\), \(d=n/2-1\), \(s=0\), \(j=1\), and \(r=n/2+1\). The resulting antipodal pair has representative \(r-k=n/2-1\), beyond the permitted range \(0\le r\le n/2-3\). Again \(y\) is not selected.

These cases exhaust all choices of the discarded markers, and the overlap condition is symmetric in the choice of ordered words because both orders are forbidden. Hence the construction is admissible, proving equality in the upper bound for every \(n\ge4\).

## Verification

The accompanying standard-library program `verify.py` reproduces the construction and formula, checks every codeword pair directly for lengths \(4\le n\le20\), and checks all possible one-step and two-step weight-preserving successor words for lengths \(4\le n\le120\). It also solves the underlying finite independent-set problems by exhaustive branch-and-bound for \(4\le n\le8\), obtaining capacities \(1,2,5,6,7\), respectively. Independent mixed-integer exact optimization of the word-conflict graph agreed through length \(22\), with zero reported solver gaps. These finite checks support the proof; they do not substitute for the all-length argument above.

The formula gives, for lengths \(4\) through \(12\), the capacities \(1,2,5,6,7,12,13,15,22\).

## Relationship to prior work

Blackburn, Nasr Esfahani, Kreher and Stinson establish general bounds and constructions for codes forbidding specified overlap lengths. Their Theorem 1 gives the unrestricted-alphabet bound for forbidden lengths \(k\) through \(n-1\), which at \(k=n-2\) provides an upper bound without resolving the exact binary weight-two layer. Their additional weight-related enumeration in Lemma 24 serves different asymptotic constructions. Yazdi, Kiah, Gabrys and Milenkovic introduce weakly mutually uncorrelated codes for DNA synchronization and derive general and balanced-composition bounds; their balanced results use half-weight (not weight two) and do not yield this exact fixed-weight two-marker formula.

The present result concerns an exact fixed-weight subproblem; it does not improve the unrestricted code-size bounds or enumerate general Hamming weights. Existing results for *fully* non-overlapping codes forbid more overlap lengths and therefore do not imply the present optimum.

## Limitations

The theorem applies only to the binary Hamming-weight-two layer and only to the two forbidden lengths specified. The construction need not be optimal for other weights or other overlap sets. Numerical experiments checked only finite lengths; the infinite assertion rests on the proved orbit upper bound and the constructive boundary-case analysis. An equivalent special case in unindexed coding literature cannot be ruled out by searches alone. Independent external validation has not been performed.

## References

1. S. R. Blackburn, N. Nasr Esfahani, D. L. Kreher, D. R. Stinson, *Constructions and bounds for codes with restricted overlaps*, arXiv:2211.10309, first posted 2022-11-18. https://arxiv.org/abs/2211.10309
2. S. M. H. Tabatabaei Yazdi, H. M. Kiah, R. Gabrys, O. Milenkovic, *Mutually Uncorrelated Primers for DNA-Based Data Storage*, arXiv:1709.05214, first posted 2017-09-13. https://arxiv.org/abs/1709.05214
