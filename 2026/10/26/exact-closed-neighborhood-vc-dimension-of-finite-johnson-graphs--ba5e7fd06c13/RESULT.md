# Exact closed-neighborhood VC dimension of finite Johnson graphs

## Finding

Let \(n\ge2\) and \(1\le k\le n-1\). The Johnson graph \(J(n,k)\) has the \(k\)-subsets of \([n]\) as vertices, with \(A\sim B\) when \(|A\cap B|=k-1\). Write \(N[A]=\{B:|A\cap B|\ge k-1\}\) for a **closed** neighborhood, including \(A\) itself, and let \(v(n,k)\) be the VC dimension of the family \(\{N[A]:A\in\binom{[n]}k\}\).

Then the following table is exact:

\[
v(n,k)=\begin{cases}
0,&\min(k,n-k)=1,\\
1,&\min(k,n-k)=2,\ n=4,\\
2,&\min(k,n-k)=2,\ n=5,\\
3,&\min(k,n-k)=2,\ n\in\{6,7\},\\
3,&(n,k)=(6,3),\\
4,&\text{all other cases with }\min(k,n-k)\ge2.
\end{cases}
\]

In particular, **every** finite Johnson graph has closed-neighborhood VC dimension at most four, the bound is attained for every \(\min(k,n-k)\ge3\) except \(J(6,3)\), and the previously known two-element-slice case agrees with the table above. Unlike the open-neighborhood VC dimension, the closed-neighborhood VC dimension of both \(J(6,3)\) and \(J(7,2)\) equals three rather than four.

## Assumptions and scope

All neighborhoods are closed, not open; centers and shattered points are required to be vertices of the **same** Johnson graph. A finite set \(S\) is shattered if \(\{S\cap N[A]:A\in\binom{[n]}k\}=2^S\). The degree-zero cases \(k=0\) and \(k=n\), if admitted, each have VC dimension zero. The theorem does not concern variable-radius balls, arbitrary induced subgraphs, or other distance predicates. The parameter \(n\) is the size of the underlying alphabet and \(k\) the fixed subset cardinality.

## Proof

**1. A universal trace reduction.** For all \(k\)-sets \(A,B\), the Johnson graph distance is \(d(A,B)=k-|A\cap B|\). Suppose five distinct vertices are shattered. Since their complete five-point trace occurs, there is a center \(C\) whose closed neighborhood contains all five. Let \(R=C\) and \(T=[n]\setminus C\). The vertices of \(N[C]\) are \(C\) and the distinct swaps \(X_{a,b}=C\setminus\{a\}\cup\{b\}\) with \(a\in R\), \(b\in T\). Regard these swaps as distinct cells of an \(|R|\)-by-\(|T|\) grid.

Every other center \(D\) has precisely one of the following trace forms on cells \(X_{a,b}\):

* If \(d(C,D)=0\), the trace includes **all** cells and \(C\).
* If \(d(C,D)=1\), write \(D=X_{p,q}\). The cells within one of \(D\) are exactly those with \(a=p\) **or** \(b=q\); \(C\) is included. Thus the trace is a row-column cross.
* If \(d(C,D)=2\), write \(D=C\setminus\{p,r\}\cup\{q,s\}\), with distinct \(p,r\in R\) and distinct \(q,s\in T\). The cells within one of \(D\) are exactly the intersection of the two selected rows and two selected columns: \(a\in\{p,r\}\) **and** \(b\in\{q,s\}\). The vertex \(C\) is excluded.
* If \(d(C,D)\ge3\), no member of \(N[C]\) is in \(N[D]\).

These are exhaustive, by the triangle inequality and the displayed intersection calculation.

**2. Finite exhaustive obstruction, with a bounded kernel.** There are two and only two cases for a purported shattered five-set: (I) five distinct grid cells, excluding \(C\); or (II) four distinct grid cells together with \(C\). In case I every possible trace is contained in the union of the empty trace, the full trace, all row-column crosses and all two-by-two row-column rectangles. In case II the empty and rectangular traces omit \(C\), whereas the full and cross traces contain it.

For a configuration of \(m\) distinct labeled grid cells, record the equivalence relations on \([m]\) defined by equality of row indices and by equality of column indices. Conversely, any pair of set partitions that gives distinct ordered row-column pairs describes every combinatorial possibility up to relabeling of rows and columns. A center can name at most two row indices and two column indices, so **two fresh dummy rows and two fresh dummy columns** suffice to realize every trace possible in an arbitrarily larger grid. Allowing these dummy indices, and even allowing the empty trace when no actual distant center exists, can only enlarge the real trace family.

The completely explicit standard-library program `verify.py` enumerates set partitions in restricted-growth form, rejects coincident cells, and builds the stated superfamily of trace masks directly from crosses and rectangles. In case I it checks all **1,153** valid pairs of partitions for five cells and finds at most **24** different traces, strictly fewer than the required \(2^5=32\). In case II it checks all **113** valid pairs for four cells and finds at most **25** different traces, again fewer than 32. The enumeration is exhaustive by the partition correspondence and the two-dummy-coordinate argument. Consequently no shattered five-set exists in any \(J(n,k)\), proving \(v(n,k)\le4\) universally.

**3. Exact finite base cases.** For any fixed \(n,k\) the symmetric group on \([n]\) acts transitively on Johnson graph vertices. Therefore every shattered set of size \(s\) can be transported into the single fixed ball \(N[C_0]\), where \(C_0=\{1,\ldots,k\}\). To rule out shattering of size \(s\), it is enough to enumerate the \(s\)-subsets of \(N[C_0]\), testing their traces against all \(k\)-set centers. The checker does precisely this for the seven base cases below. The fifth column provides a concrete shattered witness \(S\), written as a list of sets; the companion checker prints and verifies one center for **every** binary trace on each witness.

| \((n,k)\) | Exact VC dimension | Non-shattering tests at size \(v+1\) | Witness sample \(S\) |
|---|---:|---:|---|
| \((4,2)\) | 1 | 10 | \(\{12\}\) |
| \((5,2)\) | 2 | 35 | \(\{12,13\}\) |
| \((6,2)\) | 3 | 126 | \(\{12,13,14\}\) |
| \((7,2)\) | 3 | 330 | \(\{12,13,14\}\) |
| \((8,2)\) | 4 | 1287 | \(\{13,14,25,26\}\) |
| \((6,3)\) | 3 | 210 | \(\{123,124,125\}\) |
| \((7,3)\) | 4 | 1287 | \(\{124,125,136,137\}\) |

In this table a string such as `136` denotes the subset \(\{1,3,6\}\), not an integer. For each base case, the checker uses a separate direct Johnson-distance definition of the closed neighborhood; it does not call the grid-trace kernel used in step 2. This supplies both finite nonexistence certificates and complete positive trace witnesses.

**4. Monotonicity and completion.** If \(n'\ge n\) and \(k'\ge k\), \(n'-k'\ge n-k\), embed \(J(n,k)\) into \(J(n',k')\) by adjoining \(k'-k\) common new elements to every vertex, leaving the remaining added elements unused. This embedding preserves adjacency and equality, so all trace witnesses for a shattered set remain witnesses in the larger graph. Also \(J(n,k)\cong J(n,n-k)\) by complementation. Thus the lower witness in \(J(8,2)\) reaches every \(\min(k,n-k)=2\) with \(n\ge8\), and the witness in \(J(7,3)\) reaches every case \(\min(k,n-k)\ge3\) other than \(J(6,3)\). All remaining nontrivial small cases are in the finite table. When \(\min(k,n-k)=1\), the Johnson graph is complete, so all closed neighborhoods coincide and the VC dimension is zero. Combining these observations with step 2 proves the theorem for every \(n,k\). \(\square\)

## Verification

From the directory containing the package's `verify.py`, run `python verify.py` with a normal Python 3 interpreter; no third-party packages, downloads or nonstandard solvers are needed. It checks 1,153 and 113 abstract partition configurations, replays every trace mask, enumerates 10, 35, 126, 330, 1,287, 210 and 1,287 small-case non-shattering tests respectively, and constructs full positive witness-center charts. It finishes with `VERIFY_OK complete_finite_kernel=PASS small_cases=PASS witnesses=PASS`. The complete output is reproducible and checks the only finite certificates on which the all-parameter proof relies. The monotonicity and reduction arguments themselves are mathematical and cannot be replaced by finite tests.

## Relationship to prior work

Adler, Benediktsson and Macpherson (2020 preprint, published 2022) prove a sharp **open-neighborhood** VC-dimension theorem for Johnson graphs (their Theorems 3.6 and 3.7), and observe that closed-neighborhood dimension is bounded; their statement does not give the exact closed-neighborhood classification here. In fact their open-neighborhood shattering witnesses in \(J(7,2)\) and \(J(6,3)\) show a contrast: for these very graphs the present closed-neighborhood value is only three. Their Section 3 uses a related rook-grid representation, which is an important methodological antecedent. Coudert, Csikós, Ducoffe and Viennot (2024) give a general algorithm for closed-neighborhood graph VC dimension rather than a symbolic Johnson-family classification.

The special triangular-graph case \(k=2\), equivalent to the fixed-size two-vertex edge-hit range system, was previously derived separately. It is incorporated here for a complete classification and is **not** claimed as a new stand-alone result. The new part is the global sharp bound and exact \(k\ge3\) classification, including the exceptional balanced case. No exhaustive literature search can establish publication priority; equivalent descriptions under fixed-weight binary-code, rook-grid or Johnson-ball terminology remain possible.

## Limitations

The result is a computer-assisted mathematical theorem: the finite upper kernel and small cases depend on correct execution of the transparent exhaustive Python enumerator. There is no Lean/external formal proof, no independent audit, and no claim about open neighborhoods beyond the literature comparison, arbitrary induced subgraphs, radius greater than one, or variable-radius unions. The finite certificate checks every required partition pair but does not by itself establish the mathematical reductions (proved above). Independent replication and publication-priority checking remain appropriate before external dissemination.

## References

1. I. Adler, B. G. Benediktsson, and D. Macpherson, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042 (first publicly posted 2020-07-31), published in *Discrete Applied Mathematics* 312 (2022), 29–44. https://arxiv.org/abs/2007.16042
2. D. Coudert, M. Csikós, G. Ducoffe, and L. Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588 (first publicly posted 2024-05-13). https://arxiv.org/abs/2405.07588
