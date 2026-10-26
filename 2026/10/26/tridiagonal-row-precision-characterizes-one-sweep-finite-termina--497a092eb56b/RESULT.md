# Tridiagonal row precision characterizes one-sweep finite termination of oblique Kaczmarz

## Finding

Let \(n\ge2\), let \(A\in\mathbb R^{n\times n}\) be invertible, and fix the order of its row normals \(a_1,\ldots,a_n\). Put \(G=AA^{\mathsf T}\succ0\) and \(J=G^{-1}\). The unthresholded consecutive-row Kaczmarz method with oblique projection (KO) reaches the exact solution after its first ordered sweep, **for every initial state and right-hand side**, if and only if the row *precision* matrix \(J\) is tridiagonal:

\[
\boxed{\quad x_n=A^{-1}b\ \text{for all}\ x_0,b\quad\Longleftrightarrow\quad J_{ij}=0\ \text{whenever}\ |i-j|\ge2.\quad}
\]

Equivalently, the row Gram matrix obeys the chained partial-covariance identities

\[
\boxed{\quad G_{j,i}=\frac{G_{j,i-1}G_{i-1,i}}{G_{i-1,i-1}}
\quad(3\le i\le n,\ 1\le j\le i-2).\quad}
\]

For \(n=3\), even when exact termination fails, the error-propagation operator has the **exact** Euclidean norm

\[
\boxed{\quad \|T_3\|_2=\frac{|J_{13}|}{\sqrt{J_{11}J_{33}}}
=\frac{|G_{13}-G_{12}G_{23}/G_{22}|}
{\sqrt{(G_{11}-G_{12}^2/G_{22})(G_{33}-G_{23}^2/G_{22})}}<1.\quad}
\]

Thus the three-row contraction factor is precisely the absolute *partial correlation* between the first and third row normals conditioned on the second. Every \(n=2\) invertible system terminates in its first two updates, whereas for \(n\ge3\) the exact-termination criterion is a nontrivial structural restriction.

## Assumptions and scope

All operations are over real numbers in exact arithmetic. The system \(Ax=b\) is square and invertible; rows are visited in the fixed order \(1,2,\ldots,n\). At the first update use the ordinary orthogonal row projection:

\[
x_1=x_0+\frac{b_1-a_1^{\mathsf T}x_0}{\|a_1\|_2^2}a_1.
\]

For every \(i=2,\ldots,n\), set

\[
c_i=\frac{a_i^{\mathsf T}a_{i-1}}{\|a_{i-1}\|_2^2},\qquad
w_i=a_i-c_i a_{i-1},\qquad
x_i=x_{i-1}+\frac{b_i-a_i^{\mathsf T}x_{i-1}}{\|w_i\|_2^2}w_i.
\]

Because the rows are independent, every \(\|w_i\|_2^2\) is strictly positive. This is the exact update defined in Algorithm 2.1 of Li, Wang, Bao, and Liu (arXiv:2106.13368), restricted to the initial ordered sweep and with no tolerance-triggered skipped update. Its practical implementation may skip a direction below a chosen positive tolerance; the theorem does not cover such skipped updates.

## Proof

**1. Rank loss forces full orthogonality.** Let \(x_\ast=A^{-1}b\), let \(e_i=x_i-x_\ast\), and let \(T_i\) be the operator \(e_0\mapsto e_i\). Define \(w_1=a_1\) and

\[
P_i=I-\frac{w_i a_i^{\mathsf T}}{a_i^{\mathsf T}w_i},
\qquad a_i^{\mathsf T}w_i=\|w_i\|_2^2>0,
\qquad T_i=P_iP_{i-1}\cdots P_1.
\]

Each \(P_i\) is an idempotent rank-\(n-1\) projection with kernel \(\operatorname{span}\{w_i\}\). Consequently, a product \(P_iT_{i-1}\) loses at most one rank, and loses exactly one if and only if \(w_i\in\operatorname{im}T_{i-1}\). Initially, \(T_1\) has rank \(n-1\). If every previous update has removed one rank, its image is the common nullspace of the first \(i-1\) row normals: this holds at \(i=1\), and the next update preserves all earlier equations when \(w_i\) belongs to that common nullspace, while imposing the new equation. Thus

\[
\operatorname{rank}T_i=n-i
\quad\Longleftrightarrow\quad
w_k\perp a_j\ \text{for each}\ 2\le k\le i,\ 1\le j\le k-2,
\]

with the right-hand side understood inductively. Since \(n\) projections must remove all \(n\) ranks to make \(T_n=0\), **any** failure of the condition at its first occurrence makes exact termination impossible for some initial error. For \(j\le i-2\), the requirement \(a_j^{\mathsf T}w_i=0\) is exactly

\[
G_{j,i}-\frac{G_{i-1,i}}{G_{i-1,i-1}}G_{j,i-1}=0.
\]

This proves equivalence between universal one-sweep termination and the chained Gram identities, with all quantifiers accounted for.

**2. The sparse-precision equivalence.** Form the unit lower-bidiagonal matrix \(B\) with entries \(B_{ii}=1\) and \(B_{i,i-1}=-c_i\), and set \(W=BA\). The Gram identities from Step 1 say \(w_i\) is perpendicular to **every earlier row**. Therefore

\[
WW^{\mathsf T}=BGB^{\mathsf T}=D,
\qquad D=\operatorname{diag}(\|w_1\|^2,\ldots,\|w_n\|^2),
\]

and hence \(J=B^{\mathsf T}D^{-1}B\), which is tridiagonal. Conversely, every symmetric positive-definite tridiagonal \(J\) possesses a unique factorization \(J=B^{\mathsf T}D^{-1}B\) with \(B\) unit lower bidiagonal and \(D\) positive diagonal. One obtains it by successively eliminating the last row/column; positivity of the Schur complements follows from positive definiteness. Inversion gives \(BGB^{\mathsf T}=D\), so the row innovations \(w_i\) are mutually orthogonal. In particular, \(w_i\perp a_{i-1}\), which fixes the bidiagonal coefficient uniquely to the KO choice \(c_i=G_{i,i-1}/G_{i-1,i-1}\). The innovations are therefore precisely the KO directions and satisfy the Gram identities. This proves the stated if-and-only-if.

**3. Exact three-row contraction.** For \(n=3\), the first two updates are successive orthogonal projections onto the first row's nullspace and onto its intersection with the second row's nullspace, so \(T_2\) is the orthogonal projection onto the one-dimensional line \(L=\{a_1,a_2\}^{\perp}\). Let \(q\) be either unit vector spanning \(L\). The final KO direction \(w_3\) is perpendicular to \(a_2\), and on \(L\) its oblique projection \(P_3\) acts as the ordinary orthogonal projection along \(w_3\): \(a_3^{\mathsf T}q=w_3^{\mathsf T}q\) and \(a_3^{\mathsf T}w_3=\|w_3\|^2\). Hence

\[
\|T_3\|_2^2=\|P_3q\|_2^2
=1-\frac{|w_3^{\mathsf T}q|^2}{\|w_3\|_2^2}.
\]

Put \(u=a_1-(G_{12}/G_{22})a_2\), \(V_1=\|u\|^2=G_{11}-G_{12}^2/G_{22}\), \(V_3=\|w_3\|^2=G_{33}-G_{23}^2/G_{22}\), and \(C=u^{\mathsf T}w_3=G_{13}-G_{12}G_{23}/G_{22}\). The orthogonal decomposition of \(w_3\in a_2^\perp\) into the \(u\)-direction and the \(q\)-direction gives \(|w_3^{\mathsf T}q|^2=V_3-C^2/V_1\). Therefore \(\|T_3\|_2^2=C^2/(V_1V_3)\). The inverse of the positive-definite \(2\times2\) Schur complement of \(G_{22}\) is the corresponding endpoint block of \(J\), and gives \(C^2/(V_1V_3)=J_{13}^2/(J_{11}J_{33})\). Strict inequality \(\|T_3\|_2<1\) follows from the positive determinant of that Schur complement.

**4. Dense exactly soluble families and sharp obstruction.** For each \(n\ge2\) and \(0<\rho<1\), the dense positive-definite Toeplitz Gram matrix \(G_{ij}=\rho^{|i-j|}\) satisfies every chained Gram identity and has tridiagonal precision. Thus any real square root or Cholesky factor \(A\) of \(G\) yields exact first-sweep KO termination despite nonorthogonal, globally correlated rows. Conversely, in dimension three the admissible Gram family

\[
G_t=\begin{pmatrix}1&0&t\0&1&0\t&0&1\end{pmatrix},\quad 0<t<1,
\]

has \(\|T_3\|_2=t\). Its contraction factor can therefore approach one, but equals zero only at the conditional-independence boundary \(t=0\).

## Verification

The standalone file `CHECK.py` performs exact-rational matrix products and inversions. It checks the equality between one-sweep zero propagation and tridiagonal precision for nontrivial rational row matrices, verifies exact termination for 21 chained Markov cases of dimensions two through eight, and verifies the squared three-row norm formula for 48 rational three-row cases. It also reports an explicit non-Markov obstruction of squared norm \(1/1126\). These computational cases are demonstrations; Steps 1–4 prove the universal assertions without extrapolating finite tests.

## Relationship to prior work

Li, Wang, Bao, and Liu introduced the KO update, proved asymptotic convergence for consistent linear systems, and gave exact two-equation examples (arXiv:2106.13368, Algorithm 2.1, Theorem 2.1, Example 2.1). The condition that **all** square systems with a specified row Gram precision pattern terminate on the first ordered sweep is not supplied by those results. Wang and collaborators developed greedy/maximal residual oblique-row variants (arXiv:2106.13606); their random and greedy selection rules do not determine the stated ordered finite-termination iff. Brust and Saunders provide finite-termination results for the stronger accumulated-history projection system solver PLSS (arXiv:2207.07615), which does not imply a criterion for an update that retains only one preceding row. The tridiagonal-precision and partial-correlation statements here are consequences specifically of the minimal-memory KO structure, not of the general existence of direct projection solvers.

## Limitations

The result is for exact arithmetic, real invertible square systems, a fixed first-sweep row order, and unthresholded updates. It does not assert finite termination after subsequent cyclic visits for matrices violating the criterion, nor does it include overdetermined/inconsistent systems, finite-precision cancellation, or skips triggered by the published algorithm's tolerance. Publication-priority certainty is limited by unindexed equivalent statements and inaccessible full text of some early direct-projection literature; absence from searches is not proof of absence.

## References

1. W. Li, Q. Wang, W. Bao, and L. Liu, *On Kaczmarz method with oblique projection for solving large overdetermined linear systems*, arXiv:2106.13368 (first submitted 25 June 2021), Algorithm 2.1, Theorem 2.1, Example 2.1. https://arxiv.org/abs/2106.13368
2. F. Wang et al., *Greedy randomized and maximal weighted residual Kaczmarz methods with oblique projection*, arXiv:2106.13606 (2021); Electronic Research Archive 30 (2022), 1158–1177. https://arxiv.org/abs/2106.13606
3. J. J. Brust and M. A. Saunders, *PLSS: A Projected Linear Systems Solver*, arXiv:2207.07615 (2022). https://arxiv.org/abs/2207.07615
