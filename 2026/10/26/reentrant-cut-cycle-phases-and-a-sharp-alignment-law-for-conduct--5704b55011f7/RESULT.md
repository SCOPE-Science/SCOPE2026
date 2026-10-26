# Reentrant cut-cycle phases and a sharp alignment law for conductance-weighted split graphs

## Finding

Let \(A\) be a clique of \(m\ge2\) vertices and let \(B\) be an independent set of \(n\ge2\) vertices. Connect every vertex of \(A\) to every vertex of \(B\). Give each clique edge electrical conductance \(x^2\) and each cross edge conductance \(1\), with \(x>0\). On the real edge space, let \(Q\) be the canonical conductance-symmetrized Euclidean-orthogonal cut projection and \(P=I-Q\) its cycle-space complement.

Put \(h=mx^2+n\), and define the four edge-column quantities
\[
\begin{aligned}
C_A&=\frac{2((m-1)x^2+nx)}h,&
C_B&=1+\frac{(m-1)(x+2(n-1)/m)}h,\\
Z_A&=1+\frac{2((m-3)x^2+nx)}h,&
Z_B&=2-\frac2m+\frac{(m-1)(x+2(n-2)/m)}h.
\end{aligned}
\]
Here the subscript \(A\) denotes a clique-edge source column; \(B\) denotes a cross-edge source column. Then, for every \(m,n\ge2\) and every \(x>0\),
\[
\boxed{\|Q\|_{1\to1}=\|Q\|_{\infty\to\infty}=\max\{C_A,C_B\}},\qquad
\boxed{\|P\|_{1\to1}=\|P\|_{\infty\to\infty}=\max\{Z_A,Z_B\}}.
\]

The maximizing-edge phase diagram is completely determined by the following polynomials:
\[
\begin{aligned}
F_C(x)&=m(m-2)x^2+m(2n-m+1)x-3mn+2m+2n-2,\\
F_Z(x)&=m(m-4)x^2+m(2n-m+1)x-3mn+4m+4n-4.
\end{aligned}
\]
The clique-edge columns win exactly when the corresponding polynomial is positive, the cross-edge columns win when it is negative, and the two orbits tie exactly at a zero.

**Sharp phase-alignment law.** For every \(m\ge4\), each polynomial has exactly one positive root, denoted \(\theta_C\) and \(\theta_Z\), respectively. Both projection norms switch from cross-edge to clique-edge maximizers at their corresponding root. Their relative order is
\[
\boxed{
\begin{cases}
\theta_Z<\theta_C,&m<2n+1,\\
\theta_Z=\theta_C,&m=2n+1,\\
\theta_C<\theta_Z,&m>2n+1.
\end{cases}}
\]
The transitions coincide if and only if \(m=2n+1\); the common conductance square root is
\[
\boxed{\theta_C=\theta_Z=\sqrt{\frac{m+n-1}{m}}}.
\]
For instance, when \((m,n)=(5,2)\), both edge classes tie simultaneously for both projections at \(x=\sqrt{6/5}\). At this point their norms are \(6/5+\sqrt{6/5}/2\) and \(8/5+\sqrt{6/5}/2\), respectively.

**Low-clique reentrance.** If \(m=3\) and \(n\ge2\), the cycle polynomial has precisely two positive roots \(\theta_Z^-<1<\theta_Z^+\), and the cycle norm is attained on cross edges, then clique edges, then cross edges as \(x\) increases. The cut norm switches once at \(1<\theta_C<\theta_Z^+\), and \(\theta_Z^-<\theta_C\). If \(m=2\), the cut switch is always at \(x=1\). For \(n\ge3\), the cycle norm has the same cross–clique–cross reentrance, with its two roots straddling \(1\). For \((m,n)=(2,2)\), the cycle norm is instead attained on clique edges for \(0<x<3/2\) and on cross edges for \(x>3/2\), with a tie at \(3/2\). These statements include every tie as equality between the respective orbit formulas.

## Assumptions and scope

All vertex sets are finite; \(m,n\) are integers at least \(2\), and \(x\) is an arbitrary positive real. Conductances, not geometric lengths, are assigned to edges. Choose any signed vertex–edge incidence matrix \(D\), let \(W\) be diagonal with conductances \(x^2\) on clique edges and \(1\) on cross edges, and put
\[
L=DWD^{\mathsf T},\qquad Q=W^{1/2}D^{\mathsf T}L^+DW^{1/2},\qquad P=I-Q.
\]
Here \(L^+\) denotes the Moore–Penrose pseudoinverse. The two operators are real symmetric idempotents, and their matrix norms in \(\ell_1(E)\) are the largest absolute column sums. Edge orientations change signs by diagonal isometries but do not change any result.

Only canonical orthogonal projections are being classified, not least-norm projections among arbitrary linear complements. In particular no assertion is made about intermediate \(\ell_p\) norms.

## Proof

**Spectral decomposition.** The weighted Laplacian is invariant under permutations within \(A\) and within \(B\). On the zero-sum fluctuations supported in \(A\), \(L\) acts by the scalar \(h=mx^2+n\); on zero-sum fluctuations supported in \(B\), it acts by the scalar \(m\). On the remaining nonconstant subspace of vectors constant on each part, its nonzero eigenvalue is \(m+n\). These three mutually orthogonal subspaces, together with the constants, exhaust the vertex space.

**Clique-edge source.** Inject a unit edge-coordinate vector along a fixed clique edge \(a_1a_2\). Its divergence is \(x(e_{a_1}-e_{a_2})\), so the grounded potential, up to an additive constant, is \(\phi=x(e_{a_1}-e_{a_2})/h\). The induced cut-projection column has absolute entries \(2x^2/h\) on its source edge, \(x^2/h\) on each of the other \(2(m-2)\) clique edges incident to one source endpoint, and \(x/h\) on each of the \(2n\) incident cross edges; all other entries vanish. Thus its absolute column sum is \(C_A\). Its diagonal is \(2x^2/h\), which belongs to \((0,1]\). For the complementary projection, the column sum equals \(1+C_A-4x^2/h=Z_A\).

**Cross-edge source.** Now inject the source along \(a_1b_1\), with unit conductance. Decompose the divergence into an \(A\)-fluctuation, a \(B\)-fluctuation, and the between-part contrast. One choice of potential is
\[
\phi_{a_i}=\frac{\mathbf{1}_{i=1}-1/m}{h}+u,
\qquad
\phi_{b_j}=\frac{-\mathbf{1}_{j=1}+1/n}{m}+v,
\qquad u-v=\frac1{mn}.
\]
Consequently the absolute transfer currents on cross edges belong to exactly four classes: \(1/m+(m-1)/(mh)\) on the source, \((m-1)/(mh)\) on its \(n-1\) other row edges, \((1-1/h)/m\) on the other \(m-1\) edges into \(b_1\), and \(1/(mh)\) on the remaining \((m-1)(n-1)\) edges. Before taking absolute values, the final class is negative, while the first three are positive because \(h\ge n\ge2\). Additionally, the \(m-1\) clique edges incident to \(a_1\) each carry absolute normalized current \(x/h\). Summing gives \(C_B\). The diagonal is \(1/m+(m-1)/(mh)\), so the cycle-column sum is \(1+C_B-2(1/m+(m-1)/(mh))=Z_B\). This proves the four exact column formulas and, because every edge lies in one of the two classes, both norm identities. Matrix symmetry proves the matching \(\ell_\infty\) identities.

**Threshold polynomials.** Direct subtraction and multiplication by the strictly positive \(mh\) give
\[
mh(C_A-C_B)=F_C(x),\qquad mh(Z_A-Z_B)=F_Z(x).
\]
Their endpoint signs satisfy
\[
F_C(0)<0,\quad F_Z(0)<0\ (m\ge3),\quad
F_C(1)=-(m-2)(n-1),\quad F_Z(1)=-(m-4)(n-1).
\]
For \(m\ge4\), the coefficient of \(x^2\) in \(F_Z\) is nonnegative and the coefficient of \(x\) is positive if \(m=4\); for \(m>4\), the quadratic has positive leading coefficient and negative constant. Thus \(F_Z\) has exactly one positive root. The same argument gives a single positive root for \(F_C\) for every \(m\ge3\) (and \(m=2\) gives the linear root \(1\)). Both polynomials change sign from negative to positive at their unique positive roots.

Set \(\xi=\sqrt{(m+n-1)/m}>1\). Exact algebra gives
\[
F_C(x)-F_Z(x)=2m(x^2-\xi^2),
\qquad F_C(\xi)=-m(\xi-1)(m-2n-1).
\]
For \(m\ge4\), if \(m<2n+1\), then \(F_C(\xi)>0\), so \(\theta_C<\xi\), and therefore \(F_Z(\theta_C)>0\), implying \(\theta_Z<\theta_C\). If \(m>2n+1\), both inequalities reverse. Equality is possible precisely when \(m=2n+1\), at which both polynomials vanish at \(\xi\). This proves the phase-alignment law without relying on numerical root approximations.

Finally, at \(m=3\) the cycle polynomial is a concave quadratic, negative at zero and infinity but positive at \(1\), hence has exactly two positive roots, one on either side of \(1\). The cut root exceeds \(1\). The previous \(\xi\)-identity, with \(m<2n+1\), puts the cut root below \(\xi\), where the cycle polynomial remains positive; consequently the cut root lies between the two cycle roots. At \(m=2\), the cut root is \(1\), while the cycle polynomial is \(-4x^2+2(2n-1)x-(2n-4)\). For \(n\ge3\) its value at zero is negative and its value at one is \(2(n-1)>0\), giving the claimed two roots. For \(n=2\) it factors as \(2x(3-2x)\). This proves every exceptional phase and completes the classification.

## Verification

The accompanying `check_split_graph.py` independently constructs the grounded weighted Laplacian, inverts it using exact rational Gaussian elimination, computes every projection column, and compares the absolute column sums with \(C_A,C_B,Z_A,Z_B\). It checks \(120\) weighted graphs, covering \(2\le m\le7\), \(2\le n\le6\), and four positive rational values of \(x\), amounting to \(3280\) completely reconstructed columns. Two further rational boundary checks are included. This is a finite test of the formulas, not a substitute for the all-parameter spectral and sign proof.

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii (2023 preprint; published 2024) develop cycle and cut projection theory and analyze invariant projections, principally for Hamming graphs and discrete tori. Their work supplies relevant Banach-space motivation, but its stated results do not classify conductance-weighted complete split graphs or their maximizing edge orbits. Li and Sun (2020) study split-graph Laplacian spectra; spectral information alone does not evaluate the absolute transfer-current column sums or imply the two complementary phase transitions. Its full text was not accessible for complete comparison, so possible embedded formulas remain an originality risk. The standard electrical-potential representation is used as background and is not claimed as new.

The new claim is the **joint all-positive-conductance endpoint classification**, the reentrant low-clique cases, and the simultaneous-transition condition \(m=2n+1\), not the general pseudoinverse identity or any unweighted special case by itself.

## Limitations

The result concerns symmetric, real, Euclidean-orthogonal edge projections with only two uniform conductance classes. It does not establish optimality among arbitrary (possibly nonorthogonal) projections, arbitrary heterogeneous edge weights, or extensions to complex interpolation exponents. The exact norm identities and phase classifications hold for all parameters in the stated domain; the accompanying finite checks verify examples but do not certify all real parameters. The originality comparison is based on accessible indexed mathematics and inspected primary material; literature not located or not accessible may contain equivalent statements.

## References

1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582, first posted 21 May 2023; *Proceedings of Symposia in Pure Mathematics* **106** (2024), 97–131. https://arxiv.org/abs/2305.12582.
2. S. Li and W. Sun, *On split graphs with three or four distinct (normalized) Laplacian eigenvalues*, *Journal of Combinatorial Designs* **28** (2020), 763–782, DOI:10.1002/jcd.21743.
