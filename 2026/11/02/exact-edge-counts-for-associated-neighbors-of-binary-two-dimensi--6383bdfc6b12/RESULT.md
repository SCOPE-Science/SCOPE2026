# Exact edge counts for associated neighbors of binary two-dimensional LCD codes

## Finding

Let \(n\ge 2\) be an integer and let the vertices be all **labeled** two-dimensional binary linear complementary dual (LCD) subspaces of \(\mathbb F_2^n\). Distinct vertices \(C,D\) are joined when some \(z\in\mathbb F_2^n\setminus(C\cup C^\perp)\) satisfies
\[
D=\langle C\cap z^\perp,z\rangle.
\]
This is the *associated-neighbor* relation. On LCD vertices it is symmetric, so each unordered pair is counted once.

Write \(h=2^{n-2}\). The exact number of edges is
\[
\boxed{\;e_n=\begin{cases}
2^{n-1}h(h-1)/4,&n\text{ even},\\
(2^{n-1}-1)h(h-2)/4,&n\text{ odd}.
\end{cases}\;}
\]
In particular, for \(n=2,3,4,5,6,7,8,9\), these numbers are
\(0,0,24,180,1920,15120,129024,1028160\), respectively.

## Assumptions and scope

All vector spaces and scalar products are over \(\mathbb F_2\). The bilinear form is the standard coordinate dot product \(x\cdot y=\sum_i x_i y_i\); an LCD subspace means \(C\cap C^\perp=\{0\}\). A two-dimensional subspace is specified by its actual vectors, with distinct coordinate labels: no permutation, isometry, or code-equivalence quotient is applied. The associated neighbor above is narrower than ordinary Grassmann-graph adjacency \(\dim(C\cap D)=1\). The formula includes both small boundary lengths \(n=2\) and \(n=3\).

## Proof

**1. Shared-line criterion.** If \(D=\langle C\cap z^\perp,z\rangle\) with \(z\notin C\cup C^\perp\), then \(C\cap D=C\cap z^\perp=\langle u\rangle\) for a unique nonzero binary vector \(u\). Let \(Q(x)=x\cdot x\), equal to the parity of the Hamming weight of \(x\).

If \(Q(u)=0\), no associated pair of LCD planes can share \(\langle u\rangle\). Indeed, for a basis \(u,v\) of any LCD plane \(D\) containing it, the Gram determinant is
\[
Q(u)Q(v)+(u\cdot v)^2=u\cdot v=1.
\]
Thus every \(z\in D\setminus\langle u\rangle\) satisfies \(u\cdot z=1\), contrary to the defining condition \(u\in C\cap z^\perp\).

If \(Q(u)=1\), set \(H_u=u^\perp\). Any LCD plane \(C\) containing \(u\) has a **unique** orthogonal basis \(\{u,v\}\) with \(v\in H_u\), \(Q(v)=1\): replace the other generator \(v\) with \(v+u\) if necessary. Uniqueness follows because adding \(u\) changes its pairing with \(u\). Conversely each such \(v\) defines an LCD plane \(C_v=\langle u,v\rangle\). For distinct choices \(v,w\), the planes \(C_v,C_w\) are associated neighbors **if and only if** \(v\cdot w=1\). Indeed, the only vector in \(C_w\setminus\langle u\rangle\) orthogonal to \(u\) is \(w\); the condition \(C_v\cap w^\perp=\langle u\rangle\) is exactly \(v\cdot w=1\), which also ensures \(w\notin C_v^\perp\). This condition is symmetric in \(v,w\).

**2. Count choices and pairs through one odd line.** Put \(t=(1,\ldots,1)\) and \(f=t+u\). For all \(v\in H_u\),
\[
Q(v)=t\cdot v=f\cdot v.
\]
Because \(Q(u)=1\), the restriction to \(H_u\) is nondegenerate. Thus \(f\in H_u\). If \(f=0\), then \(u=t\), possible only when \(n\) is odd, and there are no \(v\in H_u\) of odd norm. For any other odd \(u\), \(f\neq0\) and precisely \(h=2^{n-2}\) vectors of \(H_u\) satisfy \(Q(v)=1\).

If \(n\) is odd, then \(Q(f)=Q(t)+Q(u)=0\), so \(f\) is not one of those \(h\) vectors. For each eligible \(v\), the linear forms \(f\cdot(-)\) and \(v\cdot(-)\) on \(H_u\) are independent: \(v\ne f\), and the form on \(H_u\) is nondegenerate. Hence exactly \(h/2\) eligible \(w\) have \(v\cdot w=1\), including \(w=v\). Removing the diagonal and dividing by two gives \(h(h-2)/4\) unordered associated pairs for each active odd line.

If \(n\) is even, then \(Q(f)=1\), so \(f\) is itself eligible. It pairs to one with all \(h\) eligible vectors, giving \(h-1\) distinct neighbors. Each of the other \(h-1\) vectors \(v\) has exactly \(h/2-1\) eligible partners other than itself, by the same independent-functional count. The degree sum is
\[
(h-1)+(h-1)(h/2-1)=h(h-1)/2,
\]
so there are \(h(h-1)/4\) unordered associated pairs per odd line.

**3. Sum over all odd lines.** Exactly \(2^{n-1}\) vectors of \(\mathbb F_2^n\) have odd norm, each spanning a distinct binary line. If \(n\) is odd, remove the exceptional line \(\langle t\rangle\); if even, none is exceptional. Every associated pair shares one and only one line, because two distinct two-planes with one-dimensional intersection have a unique common line. Summing the preceding pair counts over \(2^{n-1}-(n\bmod2)\) active lines proves the formula. At \(n=2\) the lone LCD plane gives zero edges, and at \(n=3\) the local count \(h(h-2)/4\) is zero, matching the formula.

## Verification

`verify_direct.py` exhaustively generates each distinct binary two-plane, tests the Gram determinant for the LCD condition, and checks the defining associated-neighbor construction literally for all unordered pairs at \(2\le n\le7\). `verify_lines.py` is an independent implementation: it enumerates odd common lines, odd vectors in their orthogonal complements, and the pairing test, for \(2\le n\le9\). Both are self-contained Python 3 programs using only the standard library and exact integer operations; execute them with `python verify_direct.py` and `python verify_lines.py`. Their captured outputs are `verification_direct.txt` and `verification_lines.txt`. All predicted values agree. These finite enumerations are cross-checks, not the proof of the unrestricted statement.

## Relationship to prior work

The associated-neighbor operation and its symmetry for LCD codes are explicitly described in Carlos Vela's *The Neighbor Graph of Linear Complementary Dual Codes* lecture (5th Pythagorean Conference, 2025), including the observation that the associated-neighbor graph is not generally regular and a stated aim of counting its edges. The associated graph is **not** the ordinary LCD neighbor graph: the latter connects every pair of LCD subspaces meeting in codimension one. De la Cruz, Horlemann, Newman, Vela Cabello and Willems, *The Neighbor Graph of Linear Complementary Dual (LCD) Codes*, arXiv:2609.07580v1 (first arXiv version 2026-09-07), compute degrees and orbit subgraph degrees of that ordinary neighbor graph. Their article does not give the associated-graph edge count above. A published mathematical-research record on edge regularity and triangle counts likewise concerns the ordinary neighbor graph, rather than the associated-neighbor relation. The institutional research repository records an earlier presentation on the neighbor-graph topic dated 2025-04-03; its metadata is date evidence, not evidence that its full presentation lacks this count.

## Limitations

The result is exact for binary codes of dimension two and all integer lengths \(n\ge2\). It does not determine the associated-graph edge count for dimensions three or higher, for nonbinary fields, or the number of edges in equivalence-class quotients. No claim of independent mathematical audit or complete priority certification is made. An earlier inaccessible presentation or undiscovered equivalent statement may affect priority, though no such formula was identified in the inspected primary materials.

## References

1. A.-L. Horlemann and M. Newman, *The Neighbor Graph of Linear Complementary Dual Codes*, institutional presentation record (date issued 2025-04-03), https://alexandria.unisg.ch/entities/publication/51180d26-6d64-44a5-817f-6de1d51586c7.
2. C. Vela, *The Neighbor Graph of Linear Complementary Dual Codes*, conference slides, 5th Pythagorean Conference (2025), https://cargo.wlu.ca/5thPythagorean/talks/Carlos_Vela.pdf. See slides presenting associated neighborship, the symmetry theorem and the open edge-count direction.
3. J. de la Cruz, A.-L. Horlemann, M. Newman, C. Vela Cabello and W. Willems, *The Neighbor Graph of Linear Complementary Dual (LCD) Codes*, arXiv:2609.07580v1, 2026-09-07, https://arxiv.org/html/2609.07580v1.
