# Two exponential scales for simplicity and indecomposability in random perfect evolution algebras

## Finding

Fix a prime power \(q\). For each \(n\geq1\), choose a matrix \(M\) uniformly from \(\operatorname{GL}_n(\mathbb F_q)\) and form the **labelled, basis-fixed** evolution algebra \(E_M\) with natural basis \(e_1,\ldots,e_n\) and multiplication \(e_i e_j=0\) for \(i\ne j\) and \(e_i^2=\sum_jM_{ij}e_j\). Put \(g_n=|\operatorname{GL}_n(\mathbb F_q)|\), \(g_0=1\), and let \(c_n\) be the number of these matrices with indecomposable \(E_M\). Then, exactly,

\[
c_1=g_1,\qquad c_n=g_n-\sum_{k=1}^{n-1}\binom{n-1}{k-1}c_k g_{n-k},\qquad
\sum_{n\geq0}\frac{g_nz^n}{n!}=\exp\!\left(\sum_{n\geq1}\frac{c_nz^n}{n!}\right).
\]

For **each fixed** \(q\) as \(n\to\infty\), the following sharp conditional asymptotics hold:

\[
\begin{aligned}
\Pr(E_M\text{ not simple})
 &=\frac{2n(q-1)}{q^n-1}+O_q\!\left(n^2q^{-2n+4}\right),\\
\Pr(E_M\text{ decomposable})
 &=\frac{n(1-q^{-1})q^{-2n+2}}{1-q^{-n}}+O_q\!\left(n^2q^{-4n+8}\right).
\end{aligned}
\]

In particular, the conditional probability of decomposability *among the nonsimple algebras* satisfies

\[
\Pr(E_M\text{ decomposable}\mid E_M\text{ not simple})
 \sim \frac{1}{2q^{n-1}}.
\]

This distinguishes non-simplicity (a one-way zero cut) from decomposability (a two-way zero cut): their leading probabilities differ by an exponential factor \(q^{n-1}\). The exact recurrence counts **labelled structure matrices**, not isomorphism classes of algebras.

## Assumptions and scope

The coefficient field is any finite field \(\mathbb F_q\), with prime-power order \(q\geq2\). The asymptotic limit is \(n\to\infty\) with \(q\) fixed. The matrix distribution is uniform on \(\operatorname{GL}_n\), rather than uniform on isomorphism classes or on all matrices. Constants in \(O_q\) may depend on \(q\). The asymptotic assertions are for sufficiently large \(n\); the recurrence is exact for all \(n\ge1\). An evolution algebra is *indecomposable* if it cannot be written as a direct sum of two nonzero algebra ideals. The support digraph of \(M\) has an arrow \(i\to j\) exactly when \(M_{ij}\ne0\); its weak connectivity disregards arrow orientations.

## Proof

**1. Algebra and graph.** Every \(M\in\operatorname{GL}_n(\mathbb F_q)\) defines a perfect evolution algebra. The established finite-dimensional graph criteria say that \(E_M\) is simple exactly when its support digraph is strongly connected, and is indecomposable exactly when the underlying undirected graph is connected. These are, respectively, Corollaries 4.10 and 5.8 of Cabrera Casado--Siles Molina--Velasco (arXiv:1601.01832). Both directions apply because all the matrices here are invertible.

**2. Exact indecomposable count.** The weakly connected components of a support digraph form a unique partition of \([n]\). After simultaneously permuting rows and columns by that partition, \(M\) is block diagonal; invertibility forces every block to be invertible. Let the component containing label \(1\) have cardinality \(k\). There are \(\binom{n-1}{k-1}\) choices of its other labels, \(c_k\) possibilities on that component, and \(g_{n-k}\) independent invertible possibilities on the remaining labels. Hence \(g_n=\sum_{k=1}^n\binom{n-1}{k-1}c_k g_{n-k}\). Rearranging gives the recurrence; grouping matrices by all connected components gives the displayed exponential formula in the ring of formal power series over \(\mathbb Q\).

**3. Exact probabilities of cuts.** Set \(\kappa_m=\prod_{j=1}^m(1-q^{-j})\), with \(\kappa_0=1\), so \(g_m=q^{m^2}\kappa_m\). For a fixed subset \(S\subset[n]\), \(|S|=k\), the event that all entries from rows in \(S\) to columns in \(S^c\) vanish makes \(M\) block lower triangular. There are exactly \(g_k g_{n-k}q^{k(n-k)}\) such invertible matrices. Therefore the conditional probability of this *directed* zero cut is

\[
p_{k,n}^{\rightarrow}=q^{-k(n-k)}\frac{\kappa_k\kappa_{n-k}}{\kappa_n}.
\]

Requiring also the reverse block to vanish makes \(M\) block diagonal, with exactly \(g_k g_{n-k}\) realizations, and conditional probability

\[
p_{k,n}^{\leftrightarrow}=q^{-2k(n-k)}\frac{\kappa_k\kappa_{n-k}}{\kappa_n}.
\]

In particular, the singleton one-way and two-way probabilities are

\[
a_n=\frac{(1-q^{-1})q^{-n+1}}{1-q^{-n}}=\frac{q-1}{q^n-1},\qquad
b_n=\frac{(1-q^{-1})q^{-2n+2}}{1-q^{-n}}=q^{-n+1}a_n.
\]

**4. One-way failure.** A finite digraph on at least two vertices is not strongly connected precisely when it has a nonempty proper outgoing-closed vertex set. Cuts of cardinality \(1\) account for the \(n\) possible singleton rows with all off-diagonal entries zero, and cuts of cardinality \(n-1\) account for the \(n\) possible singleton columns with all off-diagonal entries zero. For sufficiently large \(n\), these \(2n\) events are distinct, each with probability \(a_n\). Two distinct such events together require at least \(2n-3\) prescribed zero entries. Since uniform independent entries conditioned on invertibility have conditioning probability \(\kappa_n\ge\kappa_\infty=\prod_{j\ge1}(1-q^{-j})>0\), each pair intersection is at most \(\kappa_\infty^{-1}q^{-2n+3}\).

Every other outgoing-closed set has size \(2\le k\le n-2\), and by a union bound its total probability is at most

\[
\kappa_\infty^{-1}\sum_{k=2}^{n-2}\binom nk q^{-k(n-k)}=O_q(n^2q^{-2n+4}).
\]

The estimate uses symmetry \(k\leftrightarrow n-k\) and, for \(3\le k\le n/2\), the identity \(k(n-k)-2(n-2)=(k-2)(n-k-2)\): the remaining binomial sum is dominated by a geometric series with ratio bounded by \(nq^{-(n/2-2)}\), tending to zero. Bonferroni bounds for the singleton events, followed by this union bound, give the asserted non-simplicity probability.

**5. Two-way failure.** A finite support digraph is weakly disconnected precisely when a nonempty proper subset has *both* cross-blocks zero. The dominant events are the \(n\) possibilities that one specified vertex is isolated in the underlying undirected graph, each having probability \(b_n\). The intersection for two distinct isolated vertices imposes \(4n-6\) prescribed zeros, so its probability is at most \(\kappa_\infty^{-1}q^{-4n+6}\). All remaining disconnecting cuts satisfy \(2\le k\le n-2\) and have total probability bounded by

\[
\kappa_\infty^{-1}\sum_{k=2}^{n-2}\binom nk q^{-2k(n-k)}=O_q(n^2q^{-4n+8}),
\]

by the same binomial-series argument. This proves the decomposability asymptotic. Because decomposability implies non-simplicity, divide these two asymptotics and use the exact identity \(b_n=q^{-n+1}a_n\) to obtain the final conditional equivalence.

## Verification

Run `python3 check.py` in the same directory as this document. Its exhaustive prime-field tests enumerate all \(\operatorname{GL}_n(\mathbb F_q)\) matrices for \((q,n)=(2,1),(2,2),(2,3),(2,4),(3,2),(3,3)\), independently compute determinant, strong/weak support connectivity and every fixed-size zero-cut incidence, and compare against the recurrence and the exact probabilities from Step 3. For example, at \((q,n)=(2,4)\), the total, simple and indecomposable counts are respectively \(20160,11658,19446\). The script produces `VERIFY_OK`. These finite checks are independent checks of examples, not a substitute for the all-\(n\) proof.

## Relationship to prior work

Cabrera Casado, Siles Molina and Velasco established the graph criteria used in Step 1 (arXiv:1601.01832, Corollaries 4.10 and 5.8); they did not give these finite-field probability laws. Kaygorodov, Martín González and Viruel explicitly pose asymptotic random-evolution-algebra simplicity and indecomposability among the subjects of Question 22 of their October 2026 survey (arXiv:2610.22248). The new calculation answers a concrete dense, basis-fixed, invertible-matrix model of that motivating question. The exponential formula used for the exact count is a classical labelled-combinatorial principle; its general form is not claimed as new. Classical sparse random-matrix rank studies address a different ensemble. The claimed contribution is the **combined sharp probabilities under invertibility conditioning**, and the resulting exponential ratio, not the pre-existing graph equivalences, generic combinatorial formula, or independent-edge digraph asymptotics.

## Limitations

No assertion concerns sparse threshold regimes, random unconditioned structure matrices, isomorphism-uniform random algebras, or varying \(q\). The labelled exact recurrence should not be confused with a count of algebra isomorphism classes. Potential earlier enumeration in broader random finite-field matrix theory is a residual originality risk; no independent mathematical audit is claimed. The constants implicit in the error terms are not optimized.

## References

1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248, first posted 15 October 2026; Section 2.2, Question 22.
2. Y. Cabrera Casado, M. Siles Molina, M. V. Velasco, *Evolution algebras of arbitrary dimension and their decompositions*, arXiv:1601.01832, especially Corollaries 4.10 and 5.8.
3. A. Elduque, A. Labra, *Evolution algebras and graphs*, arXiv:1312.4685.
4. C. Cooper, *On the distribution of rank of a random matrix over a finite field*, Random Structures & Algorithms 17 (2000), 197–212; different sparse-entry ensemble.
