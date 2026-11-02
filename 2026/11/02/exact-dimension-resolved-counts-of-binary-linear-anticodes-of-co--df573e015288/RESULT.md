# Exact dimension-resolved counts of binary linear anticodes of codiameter two

## Finding

For integers \(n\ge 2\) and \(2\le r\le n\), let \(B_{n,r}\) be the number of distinct **labeled** \((n-r)\)-dimensional subspaces \(C\le\mathbb F_2^n\) whose Hamming diameter is at most \(n-2\). Coordinate positions are fixed, and different subspaces are counted separately. Then

\[
B_{n,r}=\frac{2^r-1}{|\operatorname{GL}(r,2)|}
\sum_{j=1}^{r}{r-1\brack j-1}_2
(-1)^{r-j}2^{\binom{r-j}{2}}
\frac{(2^j-1)^n-\varepsilon_{j,n}}{2^j},
\qquad
\varepsilon_{j,n}=\begin{cases}
1&\text{if }n\text{ is even},\\
2^j-1&\text{if }n\text{ is odd}.
\end{cases}
\]

Here \({a\brack b}_2\) is the Gaussian binomial coefficient, and
\(\lvert\operatorname{GL}(r,2)\rvert=\prod_{i=0}^{r-1}(2^r-2^i)\).

The first **nonoptimal-dimension** specialization, \(r=3\), has an unexpectedly short closed form:

\[
B_{n,3}=\begin{cases}
(7^n-6\cdot3^n+5)/192&\text{if }n\text{ is even},\\
(7^n-6\cdot3^n+11)/192&\text{if }n\text{ is odd}.
\end{cases}
\quad(n\ge 3).
\]

For each fixed \(r\ge2\), comparison with the number \({n\brack r}_2\) of all \((n-r)\)-subspaces yields

\[
\frac{B_{n,r}}{{n\brack r}_2}\sim(1-2^{-r})^{n+1}
\qquad (n\to\infty).
\]

This exact **dimension-by-dimension** enumeration refines the known exponential-order enumeration of linear anticodes in the near-full-diameter regime, without claiming a new maximum-dimension characterization.

## Assumptions and scope

An \(n\)-coordinate binary linear anticode is a linear subspace \(C\le\mathbb F_2^n\) with
\(\operatorname{diam}(C)=\max\{d_H(x,y):x,y\in C\}\). Because \(C\) is linear, this diameter equals \(\max_{c\in C}\operatorname{wt}(c)\). The inequality \(\operatorname{diam}(C)\le n-2\) is equivalent to the absence of all weight-\(n\) and weight-\(n-1\) words. Every \(r\) in \(\{2,\ldots,n\}\) is included, including the unique zero subspace when \(r=n\). No full-support hypothesis is imposed.

For consistency, the optimal-dimension slice \(r=2\) reduces to
\[
B_{n,2}=\frac{3^n-2+(-1)^n}{8}.
\]
This slice lies within the known structural theory of optimal binary Hamming anticodes; the substantive extension is the formula for **every other codimension**, notably \(r=3\) and beyond.

## Proof

**1. Parity-check characterization.** Write \(V=\mathbb F_2^r\) and choose an \(r\)-by-\(n\) full-row-rank matrix \(H=(h_1\ \cdots\ h_n)\) over \(\mathbb F_2\), with \(C=\ker H\). Put \(s=h_1+\cdots+h_n=H\mathbf1\). The all-ones word belongs to \(C\) exactly when \(s=0\); the word with a single zero in position \(i\), namely \(\mathbf1+e_i\), belongs to \(C\) exactly when \(h_i=s\). Therefore
\[
\operatorname{diam}(C)\le n-2
\quad\Longleftrightarrow\quad
s\ne0\quad\text{and}\quad h_i\ne s\text{ for every }i.
\]
The full-row-rank requirement is that the columns span \(V\). Since there are \(2^r-1\) possible nonzero \(s\), it suffices to count spanning \(n\)-tuples in \(V\setminus\{s\}\) summing to \(s\) for each fixed \(s\ne0\).

**2. Exact constrained-sum count in a subspace.** Let \(W\le V\) have dimension \(j\ge1\) and contain \(s\). Let \(F_j(n)\) be the number of ordered \(n\)-tuples in \(W\setminus\{s\}\) summing to \(s\). Orthogonality of additive characters on \(W\) gives
\[
F_j(n)=\frac1{2^j}\sum_{\chi\in\widehat W}
\chi(s)\left(\sum_{x\in W\setminus\{s\}}\chi(x)\right)^n.
\]
For the trivial character the inner sum is \(2^j-1\). For any nontrivial character it is \(-\chi(s)\), and \(\chi(s)\in\{+1,-1\}\). The \(2^{j-1}\) characters with \(\chi(s)=+1\) include the trivial one; among nontrivial characters, \(2^{j-1}-1\) have value \(+1\) and \(2^{j-1}\) have value \(-1\). Hence the entire nontrivial contribution is \(-1\) when \(n\) is even and \(-(2^j-1)\) when \(n\) is odd, yielding
\[
F_j(n)=\frac{(2^j-1)^n-\varepsilon_{j,n}}{2^j}.
\]
This is an exact integer, not an asymptotic estimate.

**3. Spanning extraction.** For fixed \(s\ne0\), let \(T(V)\) count constrained-sum \(n\)-tuples whose span is exactly \(V\). A tuple summing to \(s\) necessarily spans a subspace containing \(s\). On the interval \([W,V]\) of the binary subspace lattice the Möbius function is
\[
\mu(W,V)=(-1)^{r-\dim W}2^{\binom{r-\dim W}{2}}.
\]
Therefore ordinary Möbius inversion (grouping subspaces by dimension) gives
\[
T(V)=\sum_{j=1}^r{r-1\brack j-1}_2
(-1)^{r-j}2^{\binom{r-j}{2}}F_j(n),
\]
since the number of \(j\)-dimensional subspaces of \(V\) containing \(s\) is exactly \({r-1\brack j-1}_2\), by the quotient \(V/\langle s\rangle\).

**4. Quotient by basis changes.** There are \(2^r-1\) choices of \(s\) and every full-rank parity-check matrix represents one kernel. Two such matrices have the same kernel if and only if they differ by an invertible left multiplication. The left action of \(\operatorname{GL}(r,2)\) is free on full-row-rank matrices, so each \(C\) has exactly \(\lvert\operatorname{GL}(r,2)\rvert\) presentations. Multiplying \(T(V)\) by \(2^r-1\) and dividing by that group order proves the asserted formula.

**5. Closed case and asymptotics.** For \(r=3\), the dimension weights simplify to \(F_3(n)-3F_2(n)+2F_1(n)\), where \(F_1(n)=0\). Multiplication by \(7/168\) gives the displayed parity-dependent formula. For fixed \(r\ge2\), the leading term in the exact sum is \((2^r-1)^{n+1}/(2^r\lvert\operatorname{GL}(r,2)\rvert)\); other terms have strictly smaller exponential base or bounded size. Since \({n\brack r}_2\sim2^{nr}/\lvert\operatorname{GL}(r,2)\rvert\), division proves the probability asymptotic.

## Verification

Two independent exhaustive formulations check the theorem. `count_anticodes.py` enumerates all reduced-row-echelon parity-check row spaces through length \(8\), tests the criterion \(s\ne0\) and \(h_i\ne s\), and matches the closed formula for **every codimension**. `count_anticodes_direct.py` independently enumerates generator row spaces through length \(7\), constructs their complete codeword sets, and tests the maximum Hamming weight without using the parity-check condition. Both are standalone Python 3 scripts supplied with the numerical output files; the second imports only the exact theoretical evaluation routine from the first, not its exhaustive enumerator.

The complete counts across codimensions \(r=1,\ldots,n\) are

| \(n\) | Counts in order of increasing codimension |
|---:|---|
| 2 | 0, 1 |
| 3 | 0, 3, 1 |
| 4 | 0, 10, 10, 1 |
| 5 | 0, 30, 80, 25, 1 |
| 6 | 0, 91, 590, 455, 56, 1 |
| 7 | 0, 273, 4221, 7415, 2191, 119, 1 |
| 8 | 0, 820, 29820, 115446, 75336, 9688, 246, 1 |

The entry for \(r=1\) is zero and is listed as an additional consistency check; the theorem concerns \(2\le r\le n\). The finite tests do not stand in place of the unrestricted proof above.

Reproduce from a directory containing both scripts using `python3 count_anticodes.py` and `python3 count_anticodes_direct.py`. The supplied output files show all checked pairs and successful assertions.

## Relationship to prior work

Horlemann and Ravi (arXiv:2610.31618v1, first posted 2026-10-22) derive asymptotic counts of linear Hamming anticodes, including \(2^{(1/4+o(1))n^2}\) for the total in the near-full-diameter regime. Their Theorem 4.6 is an **aggregate asymptotic**, and their Proposition 4.3 is an exact support decomposition involving unspecified full-support counts \(a_q(s,d)\). Neither is this explicit all-codimension finite formula at \(d=n-2\), nor does either imply the exact numbers without a further enumeration of those coefficients.

Di Giusto, Gorla, and Ravagnani (arXiv:2512.17542v1) prove a structural classification of **optimal** binary Hamming anticodes (Theorem 2.20). Such optimality has dimension equal to diameter, covering the slice \(r=2\) here. The all-codimension formula in this finding additionally counts nonoptimal spaces of dimensions \(n-3,n-4,\ldots,0\). In particular, the \(r=3\) closed form is not determined by a classification limited to optimal anticodes.

The proof uses standard finite-field character orthogonality and the classical subspace-lattice Möbius function; novelty, if sustained by further literature review, lies in the explicit application and exact uniform dimension-resolution of the natural anticode counting problem, not in these individual techniques.

## Limitations

The result is restricted to binary **linear** subspaces, with upper diameter at most \(n-2\). It does not count non-linear anticodes, or quotient by coordinate permutations, or provide analogous formulas for an arbitrary fixed codiameter greater than two. The enumeration includes codes with smaller actual diameter, and no claim is made about how many have diameter **exactly** \(n-2\). The optimal-dimension \(r=2\) specialization is not independently novel. The asymptotic ratio assumes fixed \(r\) as \(n\) increases.

The finite independent computations cover only the ranges stated; they support, but do not replace, the proof for all \(n,r\). Priority relative to unlocated equivalent subspace-count formulas is not independently certified.

## References

1. Anna-Lena Horlemann and Ananthakrishnan Ravi, *The Asymptotic Number of Anticodes in Hamming Spaces*, arXiv:2610.31618v1 (first posted 2026-10-22). https://arxiv.org/html/2610.31618v1
2. Andrea Di Giusto, Elisa Gorla, and Alberto Ravagnani, *A distance-free approach to generalized weights*, arXiv:2512.17542v1 (first posted 2025-12-19), especially Theorem 2.20. https://arxiv.org/html/2512.17542v1
