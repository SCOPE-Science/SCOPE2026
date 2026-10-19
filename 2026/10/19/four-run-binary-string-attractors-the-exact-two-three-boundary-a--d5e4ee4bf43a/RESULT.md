# Four-run binary string attractors: the exact two-three boundary and all two-point witnesses

## Finding

A string attractor of a finite word is a set of positions meeting at least one occurrence of each distinct nonempty contiguous factor. Fix any positive integers \(a,b,c,d\), and let
\[
w=0^a1^b0^c1^d,\qquad n=a+b+c+d.
\]
A run is a maximal block of equal symbols, so the displayed decomposition consists of exactly four runs. Write \(\gamma(w)\) for the minimum attractor size, and \(N_2(w)\) for the number of attractors consisting of exactly two positions. Positions in the following classification are **one-indexed**.

**Theorem.** Every size-two attractor is in exactly one of the following three disjoint families; the listed conditions are necessary and sufficient.

1. **First two runs.** \(\{x,a+b\}\), with \(1\le x\le a\), provided \(a\ge c\), \(b\ge d\), and either \(b=1\) or \(x=a\).
2. **Last two runs.** \(\{a+b+1,y\}\), with \(a+b+c+1\le y\le n\), provided \(c\ge a\), \(d\ge b\), and either \(c=1\) or \(y=a+b+c+1\).
3. **Middle two runs.** \(\{a+t,a+b+z\}\), with \(1\le t\le b\) and \(1\le z\le c\), provided \(c\ge a\), \(b\ge d\), and all of
\[
(t=1\ \text{or}\ z=c),\quad(t=b\ \text{or}\ z=1),\quad
 t\le d+1,\quad z\ge c-a.
\]

Put \(I(E)=1\) when condition \(E\) is true, and \(I(E)=0\) otherwise; comma-separated conditions within \(I\) denote conjunction. Define
\[
H(a,b,c,d)=\begin{cases}
\min(c,a+1),&b=1,\\
\min(b,d+1),&b>1\text{ and }c=1,\\
I(c-a\le1)+I(b-d\le1),&b>1\text{ and }c>1.
\end{cases}
\]
The exact two-point attractor count is
\[
\boxed{N_2(w)=I(a\ge c,\ b\ge d)(a\text{ if }b=1\text{ else }1)
+I(c\ge a,\ d\ge b)(d\text{ if }c=1\text{ else }1)
+I(c\ge a,\ b\ge d)H(a,b,c,d).}
\]
In particular, the optimal size has the sharp dichotomy
\[
\boxed{\gamma(w)=3\ \Longleftrightarrow\
(a>c\text{ and }d>b)\ \text{or}\ (c\ge a+2\text{ and }b\ge d+2).}
\]
In all other cases, \(\gamma(w)=2\). This is a result for all positive run lengths, not merely bounded lengths.

For example, \(0101\) has three two-position attractors; \(00110011\) has four. The word \(01110001\) has none, so its minimum attractor size is three. The word \(011001\) has two, exhibiting the one-unit threshold at which a two-position attractor survives.

## Assumptions and scope

The alphabet is \(\{0,1\}\), all four run lengths \(a,b,c,d\) are strictly positive, factors are contiguous, and attractor positions refer to the linear word (not the circular word). The theorem classifies all attractors **of size two**, not all size-three attractors when \(\gamma=3\).

For proof bookkeeping denote the four runs by \(A=0^a\), \(B=1^b\), \(C=0^c\), \(D=1^d\). Positions within a run are indexed from its left boundary, starting at one.

## Proof

**Factor reduction.** Every nonempty factor crosses one, two, three, or four consecutive runs. One-run factors are constant words. A two-run factor is \(0^i1^j\) across \(A/B\) or \(C/D\), or \(1^j0^i\) across \(B/C\), where \(i,j\ge1\). Each three-run factor contains the *entire* intermediate run \(B\) or \(C\); each four-run factor contains both entire middle runs. Any attractor must contain a zero position and a one position, since it must cover the two singleton factors. Thus a two-position candidate has one position in each of two opposite-letter runs. The four possibilities are \(A/B\), \(A/D\), \(C/B\), \(C/D\). The \(A/D\) option is impossible, because the factor \(10\) occurs only across \(B/C\).

**First-two-run case.** Let the zero position be \(x\in A\) and the one position \(y\in B\). The longest constant factors force \(a\ge c\), \(b\ge d\). The unique \(10\) occurrence forces \(y\) to be the last position of \(B\), i.e. \(a+b\). If \(b>1\), the factor \(01\) forces \(x\) to be the last position of \(A\), i.e. \(a\). Conversely, under those conditions every constant factor can be placed through the chosen occurrence in \(A\) or \(B\); every \(0^i1^j\) factor has an occurrence across \(A/B\) crossing \(x\) when \(b>1\), or crossing the only position of \(B\) when \(b=1\); every \(1^j0^i\) factor crosses the last position of \(B\). Every factor spanning at least three runs includes the entire run \(B\) or a suffix of \(B\) ending at its last position, and is therefore met. This proves family 1.

**Last-two-run case.** Let the zero position be \(x\in C\) and the one position \(y\in D\). The analogous constant factors force \(c\ge a\), \(d\ge b\). The unique \(10\) forces \(x\) to be the first position of \(C\). If \(c>1\), the factor \(01\) forces \(y\) to be the first position of \(D\). Conversely, the chosen first position of \(C\) covers every \(1^j0^i\) factor and every factor spanning three or more runs; the first position of \(D\), when needed, covers factors \(0^i1^j\) at \(C/D\). A factor \(0^i1^j\) from \(A/B\) also occurs across \(C/D\) because \(c\ge a\) and \(d\ge b\). Constant factors are met in the longer runs. This proves family 2.

**Middle-two-run case.** Let the one position be the \(t\)-th position in \(B\) and the zero position the \(z\)-th position in \(C\). The constant factors force \(c\ge a\) and \(b\ge d\). Every \(1^j0^i\) crosses the unique \(B/C\) boundary, and every such factor meets the chosen pair precisely when its shortest instance \(10\) does; this means \(t=b\) or \(z=1\).

For \(0^i1^j\), there are at most two types of occurrences: across \(A/B\) when \(i\le a,j\le b\), and across \(C/D\) when \(i\le c,j\le d\). In the first type an occurrence crosses the selected position exactly when \(j\ge t\); in the second exactly when \(i\ge c-z+1\). Necessity of \(t=1\) or \(z=c\) comes from the factor \(01\). Necessity of \(t\le d+1\) follows by considering \(01^{d+1}\) whenever \(b>d\); otherwise it is automatic. Necessity of \(z\ge c-a\) follows from \(0^{a+1}1\) whenever \(c>a\); otherwise it is automatic.

These are also sufficient: a factor \(0^i1^j\) with \(i\le a,j\le d\) is caught at one of the two boundaries by \(t=1\) or \(z=c\). If \(j>d\), only the first boundary is possible, and \(j\ge d+1\ge t\). If \(i>a\), only the second boundary is possible, and \(i\ge a+1\ge c-z+1\). Cases with both \(i>a\) and \(j>d\) do not occur. All factors using three or four runs contain the whole of \(B\) or \(C\) and are met by the selected pair. This proves family 3.

**Counting and phase boundary.** In family 1 there are \(a\) choices if \(b=1\), otherwise one. In family 2 there are \(d\) choices if \(c=1\), otherwise one. In family 3, if \(b=1\), the possible zero positions satisfy \(\max(1,c-a)\le z\le c\), giving \(\min(c,a+1)\) choices. If \(b>1,c=1\), the possible one positions satisfy \(1\le t\le\min(b,d+1)\). If \(b,c>1\), the only possible pairs of run offsets are \((t,z)=(1,1)\), admissible exactly when \(c-a\le1\), and \((t,z)=(b,c)\), admissible exactly when \(b-d\le1\). The families are disjoint by their selected runs, proving the displayed formula for \(N_2\).

Finally, there is always a three-position attractor. If \(b\ge d\), take the last positions of \(A,B,C\), namely \(\{a,a+b,a+b+c\}\). Otherwise, take the last position of \(A\) and the first positions of \(C,D\), namely \(\{a,a+b+1,a+b+c+1\}\). Each constant factor is met in a sufficiently long chosen run, each two-run factor is met at one of its transitions, and each longer factor contains a selected boundary in its full intermediate run or terminal segment. Thus \(2\le\gamma(w)\le3\). The three disjoint families above show \(N_2=0\) exactly in the two regions
\[
(a>c,\ d>b),\qquad(c\ge a+2,\ b\ge d+2).
\]
Hence \(\gamma=3\) exactly there, and \(\gamma=2\) elsewhere. \(\square\)

## Verification

Run `python3 four_run_checker.py` with Python 3 and no third-party dependencies. The program independently constructs all distinct-factor occurrence-position masks for each of the \(6^4=1296\) quadruples with \(1\le a,b,c,d\le6\), and checks every one of the 125496 two-position candidates against the theorem's predicted complete set. For the \(4^4=256\) smallest parameter tuples it also uses a separate direct factor-set enumeration; it checks the explicit three-position witnesses and the closed counting and threshold formulas. The observed completion message is `ALL_FOUR_RUN_CHECKS_PASSED quadruples 1296 candidate_pairs 125496 direct_quadruples 256`. The proof above establishes the infinite claim; finite tests alone would not.

## Relationship to prior work

The string-attractor notion and generic optimization algorithms are foundational work of Kempa, Policriti, Prezza, and Rotenberg (2018). Mantaci, Restivo, Romana, Rosone, and Sciortino (2019; 2021) study attractors under combinatorial word operations and for special word families; Dvořáková and Hendrychová (2023 preprint) analyze particular pseudopalindromic prefixes. These accessible statements and their relevant proofs do not provide a general four-run binary two-point classification or the exact phase boundary and multiplicity formula above. Other published computations for particular word lengths and periodic families include special cases but do not imply the four-parameter theorem.

## Limitations

No formula for the number of *three-position* minimum attractors is asserted in the regions where the optimum is three. The theorem is restricted to two letters and four nonempty runs; the result should not be applied without proof to words with five or more runs or larger alphabets. An equivalent result in less accessible or unindexed literature remains possible.

## References

- D. Kempa, A. Policriti, N. Prezza, and E. Rotenberg, *String Attractors: Verification and Optimization*, ESA 2018, DOI 10.4230/LIPIcs.ESA.2018.52.
- S. Mantaci, A. Restivo, G. Romana, G. Rosone, and M. Sciortino, *String Attractors and Combinatorics on Words*, arXiv:1907.04660 (first posted 2019-07-10).
- S. Mantaci, A. Restivo, G. Romana, G. Rosone, and M. Sciortino, *A Combinatorial View on String Attractors*, Theoretical Computer Science 850 (2021), 236–248, DOI 10.1016/j.tcs.2020.11.006.
- L. Dvořáková and V. Hendrychová, *String Attractors of Rote Sequences*, arXiv:2308.00850 (first posted 2023-08-01).
