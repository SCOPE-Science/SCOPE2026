# Exact two-time singleton covariance in the random labeled-tree uncover process

## Finding

Let \(n\ge4\) be an integer and let \(T_n\) be uniformly distributed over the \(n^{n-2}\) trees on labeled vertices \([n]\). Reveal vertices in increasing label order. Let \(I_j\) be the number of isolated vertices in the induced subgraph on \([j]\). For all integers \(2\le j\le k<n\), set

\[
 a_n=1-\frac1n,\quad b_n=1-\frac2n,\qquad
 p_{n,h}=\frac{n-h}{n}a_n^{h-2},
\]
\[
 u_{n,j,k}=\frac{(n-j)(n-k)}{n^2}
 a_n^{k-j}b_n^{j-3},
 \qquad
 v_{n,j,k}=\frac{(n-j-1)(n-k)}{n^2}
 a_n^{k-j-1}b_n^{j-2}\quad(j<k).
\]

**Exact temporal covariance theorem.** The complete two-time second moment and covariance satisfy

\[
 \mathbb E[I_jI_k]=j p_{n,k}+j(j-1)u_{n,j,k}
 +j(k-j)v_{n,j,k},
\]
\[
 \boxed{\operatorname{Cov}(I_j,I_k)=j p_{n,k}+j(j-1)u_{n,j,k}
 +j(k-j)v_{n,j,k}-jk p_{n,j}p_{n,k}.}
\]

For \(j=k\), the term multiplied by \(k-j\) is omitted, so \(v_{n,j,j}\) need not be defined. In particular, \(\mathbb E I_j=j p_{n,j}\), and the covariance is an exact expression at every finite order and every pair of reveal times.

For fixed \(0<s\le t<1\), as \(n\to\infty\),

\[
 \boxed{\frac1n\operatorname{Cov}(I_{\lfloor ns\rfloor},I_{\lfloor nt\rfloor})\longrightarrow
 K(s,t)=s(1-t)e^{-t}\left[1-(1-s)e^{-s}+s(2-s)(1-t)e^{-s}\right].}
\]

The kernel is strictly positive for all \(0<s\le t<1\). It is semiseparable of rank at most two off the diagonal: for \(s\le t\),

\[
 K(s,t)=\bigl[s(1-(1-s)e^{-s})\bigr]\bigl[(1-t)e^{-t}\bigr]
 +\bigl[s^2(2-s)e^{-s}\bigr]\bigl[(1-t)^2e^{-t}\bigr].
\]

The limit is a covariance result, **not** an assertion that the centered singleton-count process has a Gaussian process limit.

## Assumptions and scope

The tree is uniform among *labeled* Cayley trees; the increasing-label reveal order is equivalent in law to a uniformly random reveal permutation independent of an unlabeled re-labeling. Isolated means degree zero in the currently revealed induced forest, not a leaf in the full tree. Times are integers \(2\le j\le k<n\); at time \(1\) the count is deterministically one and at time \(n\) it is deterministically zero. The continuum statement is for fixed \(0<s\le t<1\), or uniformly on compact subsets strictly inside that triangle. All probabilities are unconditional over the tree.

## Proof

**1. A two-marked-vertex spanning-tree identity.** Take a complete graph on \(n\) vertices, distinguish two nonadjacent marked vertices \(x,y\), and allow edges from \(x\) to a prescribed set \(A\) and from \(y\) to a prescribed subset \(B\subseteq A\) of the other \(N=n-2\) vertices. All edges among the other \(N\) vertices are allowed. Put \(a=|A|\), \(b=|B|\), where \(1\le b\le a\le N\). The number of its spanning trees is

\[
 F_n(a,b)=ab\,n^{b-1}(n-1)^{a-b}(n-2)^{n-a-3}.
\]

For completeness, remove the Laplacian row and column of \(x\). The remaining cofactor, after eliminating the \(y\) row/column by a Schur complement, is

\[
 b\det\left(NI-J+\operatorname{diag}(\mathbf1_A+\mathbf1_B)
 -b^{-1}\mathbf1_B\mathbf1_B^{\mathsf T}\right).
\]

Write \(D=NI+\operatorname{diag}(\mathbf1_A+\mathbf1_B)\). Its diagonal entries are \(N+2\) on \(B\), \(N+1\) on \(A\setminus B\), and \(N\) elsewhere. The rank-two determinant lemma gives

\[
 \frac{\det(D-J-b^{-1}\mathbf1_B\mathbf1_B^{\mathsf T})}{\det D}
 =\left(1-\frac{b}{N+2}-\frac{a-b}{N+1}-\frac{N-a}{N}\right)
 \left(1-\frac1{N+2}\right)-\frac{b}{(N+2)^2}
 =\frac{a}{N(N+2)}.
\]

Since \(\det D=(N+2)^b(N+1)^{a-b}N^{N-a}\), the claimed formula follows. All denominators are nonzero for the specified integer ranges.

**2. One-vertex isolation.** A fixed vertex \(x\in[j]\) is isolated after revealing \([j]\) iff all its tree neighbors belong to \(\{j+1,\ldots,n\}\). A single-marked-vertex Matrix–Tree cofactor gives \((n-j)n^{n-j-1}(n-1)^{j-2}\) allowed labeled trees, out of \(n^{n-2}\). Therefore \(\Pr(x\text{ isolated at }j)=p_{n,j}\).

**3. Two-time joint events.** Fix \(x\in[j]\), and \(y\in[k]\) distinct from \(x\). When \(y\in[j]\), the restrictions force \(x\) to attach only outside \([j]\) and \(y\) only outside \([k]\), with respective sets \(A,B\) of sizes \(n-j,n-k\). The marked vertices cannot be adjacent, and \(B\subseteq A\). Step 1 divided by \(n^{n-2}\) gives \(u_{n,j,k}\). When \(y\in\{j+1,\ldots,k\}\), the isolation of \(y\) at time \(k\) also forbids the edge \(xy\), reducing \(x\)'s allowable set to size \(n-j-1\); the two-marked identity then gives \(v_{n,j,k}\). If \(x=y\), isolation at the later time implies isolation at the earlier time, so the joint probability is \(p_{n,k}\).

There are respectively \(j\), \(j(j-1)\), and \(j(k-j)\) ordered pairs in these three cases. Summing their probabilities yields the displayed exact second moment. Subtracting \(\mathbb E I_j\,\mathbb E I_k=jk p_{n,j}p_{n,k}\) proves the covariance formula.

**4. Continuum expansion.** For \(j=\lfloor ns\rfloor\), \(k=\lfloor nt\rfloor\) and \(0<s\le t<1\), the one-point factors satisfy \(p_{n,j}\to(1-s)e^{-s}\), \(p_{n,k}\to(1-t)e^{-t}\). Direct Taylor expansion of the exact pair probabilities, with \(j/n\to s\), yields

\[
 \frac{u_{n,j,k}}{p_{n,j}p_{n,k}}=1+\frac{2-s}{n}+O(n^{-2}),
\qquad
 \frac{v_{n,j,k}}{p_{n,j}p_{n,k}}=
 1-\frac{s(2-s)}{(1-s)n}+O(n^{-2}),
\]

uniformly on compact interior time sets. Substituting into the exact covariance, and remembering that the diagonal \(j\) terms are different from the distinct-vertex terms, gives

\[
 \lim_{n\to\infty}\frac{\operatorname{Cov}(I_j,I_k)}n
 =s p_t(1-p_s)+s^2(2-s)p_sp_t
 -\frac{s^2(t-s)(2-s)}{1-s}p_sp_t,
\]

where \(p_z=(1-z)e^{-z}\). Simplification yields \(K(s,t)\). Both summands in the two-product representation are positive for interior \(s\le t\), giving strict positivity and the stated semiseparable form.

## Verification

The standalone Python file `checker.py` gives complete, independent Prüfer-code enumeration for every \(n\in\{4,5,6,7\}\) and every admissible reveal-time pair. It compares exact rational first and cross moments to the formulas, checks exact-rational covariance positivity for all integer \(4\le n<80\) and \(2\le j\le k<n\) as a finite diagnostic only, and numerically compares the exact covariance with the continuum kernel at four interior points. The script passes 79,130 assertions with the standard Python library. The **proof**, not enumeration, covers all integers and the infinite asymptotic statement. Finite computational positivity tests are not used as proof of finite-order positivity, which is not asserted.

## Relationship to prior work

Hackl, Panholzer and Wagner, *Uncovering a Random Tree* (first publicly available June 8, 2022) and *The uncover process for random labeled trees* (arXiv:2301.00664v1, 2023) developed edge-process fluctuations, single-cluster distributions, and a Matrix–Tree enumeration of specified disjoint components at **one fixed reveal time** (Lemma 8), which already determines one-time isolation moments. The one-time marginal \(p_{n,j}\) is therefore not claimed as new. The present result treats *asymmetric restrictions at two different reveal times*, yielding a distinct joint temporal moment and its explicit positive covariance kernel. Their one-time component formula does not directly provide the mixed-time count. Janson's *Uncovering a graph* (first published September 1, 2025) treats edge-count fluctuation processes and related visible small-subgraph counts; isolated vertices and their mixed-time covariance are not the analyzed observable. These comparisons are not a guarantee of complete historical priority.

## Limitations

The theorem is specific to uniformly sampled labeled trees and uniform reveal order. It does not assert a functional central limit theorem for singleton counts, conditional distribution results, a sharp finite-order positivity theorem, or analogous formulas for recursive trees, nonuniform weighted trees, or graph models. The exact finite covariance is a second-moment identity, not a full distributional characterization. Independent mathematical and historical-priority review has not been performed.

## References

1. B. Hackl, A. Panholzer, S. Wagner, *Uncovering a Random Tree*, AofA 2022, June 8, 2022, DOI: [10.4230/LIPIcs.AofA.2022.10](https://doi.org/10.4230/LIPIcs.AofA.2022.10).
2. B. Hackl, A. Panholzer, S. Wagner, *The uncover process for random labeled trees*, arXiv:2301.00664v1 (January 2, 2023), [open full text](https://arxiv.org/html/2301.00664v1), especially Lemma 8 and Theorem 10.
3. S. Janson, *Uncovering a graph*, *Probability Theory and Related Fields*, first published September 1, 2025, DOI: [10.1007/s00440-025-01401-9](https://doi.org/10.1007/s00440-025-01401-9), especially Sections 8–9.
