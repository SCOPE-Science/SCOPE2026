# Exact independence-root phase diagram for clique coronas with independent leaves

## Finding

Let \(G_{r,k}=K_r\circ\overline{K_k}\): start with a complete graph on \(r\) vertices and attach \(k\) pairwise nonadjacent private leaves to each core vertex. For integers \(r,k\ge1\), its independence polynomial is
\[
I(G_{r,k};z)=(1+z)^{k(r-1)}Q_{r,k}(z),\qquad Q_{r,k}(z)=(1+z)^k+r z.
\]
The factorization itself is a specialization of the known corona/whiskering formula. The scalar factor \(Q_{r,k}\) is also the independence polynomial of the complete split (complete multipartite) graph \(K_ree\overline{K_k}=K_{k,1,\ldots,1}\). Thus the result concerns two naturally related graph constructions with the same nontrivial roots; the novelty is the exact position of **all** roots relative to the imaginary axis.

For each integer \(k\ge1\), define
\[
J_k=\{j\in\mathbb Z_{\ge0}:4j+3<k\},\quad
\theta_{k,j}=\frac{(4j+3)\pi}{2k},\quad
R_{k,j}=\frac{1}{\sin\theta_{k,j}\,\cos^{k-1}\theta_{k,j}}\quad(j\in J_k).
\]
For any **positive real** parameter \(r\), the number of zeros of \(Q_{r,k}\) in the open right half-plane, with algebraic multiplicity, is exactly
\[
\boxed{N_+(r,k)=2\#\{j\in J_k:r>R_{k,j}\}.}
\]
The number of its zeros on the imaginary axis is exactly
\[
\boxed{N_0(r,k)=2\#\{j\in J_k:r=R_{k,j}\}.}
\]
All those boundary roots are simple and equal to \(\pm i\tan\theta_{k,j}\) for the indices with \(r=R_{k,j}\). In particular, putting \(R_k=\min_{j\in J_k}R_{k,j}\) when \(J_k\ne\varnothing\) and \(R_k=+\infty\) otherwise, the polynomial \(I(G_{r,k};z)\) has all roots in the **open** left half-plane if and only if \(r<R_k\), and all roots in the **closed** left half-plane if and only if \(r\le R_k\). For \(k\le3\), \(J_k\) is empty and both properties hold for all positive \(r\). For \(k\ge4\), this is a finite, explicit trigonometric threshold test.

The first few sharp transitions are \(R_4=8+8\sqrt2\), \(R_5=16(1+\sqrt5)/5\), and \(R_6=8\). Thus an integer \(r=8\) for \(k=6\) lies exactly on the boundary; at \(k=8\), two distinct successive thresholds produce two separate jumps in the number of right-half-plane roots.

## Assumptions and scope

All graphs are finite, simple, and have labelled vertices; \(\overline{K_k}\) means the edgeless graph on \(k\) vertices, not a \(k\)-clique. Root counts include complex multiplicities. The phase diagram is proved for every real \(r>0\) in the polynomial family \(Q_{r,k}\), and applies to graphs when \(r\) is a positive integer. A polynomial is **strictly stable** when all roots satisfy \(\operatorname{Re}z<0\); **closed-half-plane stable** permits \(\operatorname{Re}z=0\). This result does not assert real-rootedness.

## Proof

**1. Factorization.** An independent set can omit every core vertex, contributing \((1+z)^{kr}\), or contain exactly one of the \(r\) core vertices, contributing \(r z(1+z)^{k(r-1)}\). These cases are disjoint and exhaustive, proving the stated factorization. The explicit factor \((1+z)^{k(r-1)}\) has only negative real roots, so it remains to count roots of \(Q_{r,k}\).

**2. All imaginary-axis parameters.** We have \(Q_{r,k}(0)=1\). If \(Q_{r,k}(iy)=0\) with \(y>0\), then \((1+iy)^k=-riy\). Set \(\theta=\arctan y\in(0,\pi/2)\). Taking arguments and moduli yields
\[
k\theta=\frac{3\pi}{2}+2\pi j\quad(j\ge0),\qquad
r=\frac{(1+y^2)^{k/2}}{y}=\frac{1}{\sin\theta\cos^{k-1}\theta}.
\]
The inequality \(\theta<\pi/2\) becomes \(4j+3<k\). Conversely each \(j\in J_k\) produces precisely the pair \(\pm i\tan\theta_{k,j}\) at \(r=R_{k,j}\). By conjugation these are all imaginary-axis zeros. There are no zeros at \(z=0\).

**3. Transversal crossing, always left to right.** Regard \(r\) as a real variable. At any root of \(Q_{r,k}\), the derivative with respect to \(z\) is
\[
\partial_z Q_{r,k}=k(1+z)^{k-1}+r=\frac{r(1-(k-1)z)}{1+z}.
\]
This is nonzero for \(z=iy\), so every imaginary-axis root is simple. By implicit differentiation,
\[
\frac{dz}{dr}=\frac{z(1+z)}{r((k-1)z-1)},\qquad
\left.\frac{d}{dr}\operatorname{Re}z\right|_{z=iy}
=\frac{k y^2}{r(1+(k-1)^2y^2)}>0.
\]
Every conjugate pair therefore crosses **from the left half-plane into the right half-plane** as \(r\) increases through its threshold. Several distinct pairs may cross at the same parameter; they remain individually simple, and their contributions add.

**4. Global root count.** At \(r=0\), the polynomial is \((1+z)^k\), so all roots equal \(-1\) and are in the open left half-plane. For all sufficiently small positive \(r\), all roots remain near \(-1\). On every compact parameter interval, its leading coefficient remains nonzero (one for \(k\ge2\), and \(1+r\) for \(k=1\)) and all coefficients remain bounded, so roots cannot escape to infinity. By continuity of polynomial roots, the number of right-half-plane roots can change only at an imaginary-axis crossing. Step 2 lists every crossing and Step 3 determines its direction and contribution. Thus \(N_+=2\#\{j:r>R_{k,j}\}\), with the boundary count as claimed. The fixed powers of \(1+z\) add no nonnegative-real-part roots. This completes the proof.

## Verification

The accompanying standard-library Python program `verify_threshold.py` independently enumerates independent sets of small labelled coronas and checks their polynomial coefficients, implements exact rational Routh arrays for polynomials \((1+z)^k+r z\), and compares their right-half-plane root counts to the trigonometric thresholds across a finite parameter grid. Its checked output reports **108748 explicit vertex subsets and 940 exact-rational nonsingular Routh instances**, with no skipped singular instances in that grid. It also verifies three low-degree thresholds and the exact boundary factorization
\[
Q_{8,6}(z)=(z^2+1)(z^4+6z^3+14z^2+14z+1).
\]
Run from the file's directory: `python3 verify_threshold.py`. The infinite classification relies on the proof, not on finite computation. The Routh tests deliberately use nonboundary parameters; the boundary at \(r=8,k=6\) is checked algebraically.

## Relationship to prior work

Brown and Cameron (2018), Theorem 3.2, state the general corona independence-polynomial identity, attributed there to Gutman; their Lemma 2.1 proves eventual right-half-plane roots for \(f(z)+r z\) when \(f\) has sufficiently large degree, while their Proposition 3.1 handles stars. Their Section 4 also discusses stability of complete multipartite graphs but does not classify the exact \(K_{k,1,\ldots,1}\) root-count thresholds. These give the factorization and qualitative extremal behavior, **not** the all-parameter thresholds or exact numbers of right-half-plane roots proved here.

Hibi, Kara, and Vien (2026), Section 3, derive a more general leaf-attachment formula and study polynomial symmetry and evaluation at \(-1\); those conditions do not imply the present complex-root phase diagram. Zhang and Tu (2026), Theorem 4, show strict stability of all spiders; this covers the one-core-vertex case, but a clique with multiple core vertices is generally not a spider. The distinctions are between mathematical statements and their implications, not differences of terminology.

## Limitations

The result determines half-plane root counts, not the exact complex coordinates of nonboundary roots. There is no claim that the factorization is new. The numerical verifier is finite; it does not certify the infinite argument. Bibliographic priority beyond the inspected public works and mathematical-record searches remains subject to further independent checking. No independent mathematical audit has been performed.

## References

1. J. I. Brown and B. Cameron, *On the Stability of Independence Polynomials*, Electronic Journal of Combinatorics 25(1), #P1.46 (2018), DOI: 10.37236/7280; full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v25i1p46/pdf/.
2. T. Hibi, S. Kara, and D. Vien, *Independence polynomials of graphs*, arXiv:2603.16695, first posted 2026-03-17; https://arxiv.org/abs/2603.16695.
3. L. Zhang and J. Tu, *Stability of independence polynomials of spiders*, arXiv:2609.04694, first posted 2026-09-04; https://arxiv.org/abs/2609.04694.
4. I. Gutman, general corona independence-polynomial identity, as credited in Brown--Cameron (2018), Theorem 3.2.
