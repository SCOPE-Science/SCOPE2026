# Sharp sign-variation failure of overimplicit time stepping on every birth-death chain

## Finding
For every finite irreducible birth-death generator, the overimplicit \(\theta\)-method preserves entrywise nonnegativity, stochastic mass, and positive real spectrum for every \(\theta\ge1\) and every step size \(h>0\). It nevertheless preserves the stronger ordered variation-diminishing property for every initial vector **exactly when** \(\theta=1\), once there are at least three states. In two states, every \(\theta\ge1\) has that property.

More precisely, let \(n\ge3\). For every adjacent triple indexed by \(1\le i\le n-2\), put \(G=(I-\theta hQ)^{-1}\). The following exact minor identity holds:
\[
\det P[\{i,i+1\},\{i+1,i+2\}]
=-\frac{\theta-1}{\theta^2}G_{i,i+2}.
\]
All entries of \(G\) are strictly positive. Consequently this minor is negative for every \(\theta>1\), regardless of transition-rate heterogeneity or step size. A two-coordinate vector with one sign change is explicitly constructed below whose image has at least two. For \(\theta=1\), every minor of \(P\) is nonnegative.

## Assumptions and scope
Fix an integer \(n\ge2\). The states are numbered \(1,\ldots,n\) in their physical linear order. The real matrix \(Q\in\mathbb R^{n\times n}\) has \(Q_{i,i+1}=u_i>0\), \(Q_{i+1,i}=d_i>0\) for \(1\le i<n\), no other nonzero off-diagonal entries, and diagonal entries chosen so that every row sum is zero. Let \(h>0\) and \(\theta\ge1\). The one-step matrix for \(\dot x=Qx\) is
\[
P=P_{\theta,h}=(I-\theta hQ)^{-1}(I+(1-\theta)hQ).
\]
A real matrix is **totally nonnegative (TN)** when every ordered square minor, of any size, is nonnegative. For a real vector \(v\), let \(s^-(v)\) count sign changes after deleting zero entries; by convention the zero vector has zero changes. A matrix is **variation diminishing** if \(s^-(Pv)\le s^-(v)\) for every real vector \(v\). A standard consequence of total nonnegativity is variation diminution. Here failure of variation diminution is also proved directly, not inferred merely from a negative minor. There is no assumption of uniform rates, bounded condition number, or bounded step size.

## Proof
**1. Resolvent and positivity.** Set \(M=I-\theta hQ\), \(G=M^{-1}\), \(\alpha=(\theta-1)/\theta\), and \(\beta=1/\theta\). Since \(Q\) is an irreducible continuous-time Markov generator and \(\theta h>0\), \(M\) is an irreducible nonsingular tridiagonal \(M\)-matrix. Its inverse is strictly positive; for example, the Laplace representation
\[
G=\int_0^\infty e^{-t}e^{\theta htQ}\,dt
\]
has strictly positive entries because the connected birth-death semigroup does. Also \(G\mathbf1=\mathbf1\). The identity \(G\theta hQ=G-I\) gives
\[
P=G\bigl(I-(\theta-1)hQ\bigr)=\alpha I+\beta G.
\]
For \(\theta\ge1\), \(\alpha\ge0\) and \(\beta>0\), so \(P\) is strictly positive and row-stochastic.

Birth-death detailed balance supplies \(\pi_i>0\) with \(\pi_iQ_{i,i+1}=\pi_{i+1}Q_{i+1,i}\). Conjugating with the positive diagonal \(\operatorname{diag}(\sqrt{\pi_i})\) makes \(Q\) symmetric negative semidefinite. If \(\lambda\ge0\) is an eigenvalue of \(-Q\), the corresponding eigenvalue of \(P\) is
\[
\frac{1+(\theta-1)h\lambda}{1+\theta h\lambda}>0.
\]
Thus \(P\) is positively diagonally similar to a symmetric positive-definite matrix. In particular, all its principal minors are positive.

**2. The Green-column identity.** For any tridiagonal invertible \(M\) with nonzero off-diagonals, its inverse \(G\) has a rank-one factorization above the diagonal: there are numbers \(a_i,b_j\) such that \(G_{ij}=a_i b_j\) whenever \(i\le j\). Indeed, for fixed column \(j\), the homogeneous three-term recurrence \(M G_{\cdot j}=0\) on rows \(1,\ldots,j-1\), together with the left boundary condition, leaves a one-dimensional solution space; the relation at row \(j-1\) determines the value at row \(j\). Every column therefore agrees up to scale with the same left-boundary solution through its diagonal position. Applied to \(i<i+1<i+2\), this yields
\[
G_{i,i+1}G_{i+1,i+2}
=G_{i,i+2}G_{i+1,i+1}.
\]
For the two ordered rows \(i,i+1\) and columns \(i+1,i+2\), substitute \(P=\alpha I+\beta G\) into the determinant:
\[
\begin{aligned}
&\det\begin{pmatrix}
\beta G_{i,i+1}&\beta G_{i,i+2}\\
\alpha+\beta G_{i+1,i+1}&\beta G_{i+1,i+2}
\end{pmatrix}\\
&=\beta^2\bigl(G_{i,i+1}G_{i+1,i+2}-G_{i,i+2}G_{i+1,i+1}\bigr)-\alpha\beta G_{i,i+2}\\
&=-\frac{\theta-1}{\theta^2}G_{i,i+2}.
\end{aligned}
\]
For every \(\theta>1\) this is strictly negative, proving failure of total nonnegativity, independently of the size of \(h\).

**3. Explicit creation of an additional sign change.** Fix any adjacent triple \(i,i+1,i+2\) when \(n\ge3\) and \(\theta>1\). All denominators below are positive. Define
\[
 a=\frac{P_{i,i+1}}{P_{i,i+2}},\quad
 b=\frac{P_{i+1,i+1}}{P_{i+1,i+2}},\quad
 c=\frac{P_{i+2,i+1}}{P_{i+2,i+2}}.
\]
The negative minor in step 2 implies \(a<b\). Positivity of the principal minor on \(\{i+1,i+2\}\), proved in step 1, implies \(c<b\). Choose any real \(t\) with \(\max(a,c)<t<b\), and let \(v=e_{i+1}-t e_{i+2}\). Then \(s^-(v)=1\). The three consecutive entries of its image satisfy
\[
(Pv)_i<0,\qquad (Pv)_{i+1}>0,\qquad (Pv)_{i+2}<0.
\]
Therefore \(s^-(Pv)\ge2\). This is a direct, constructive violation of variation diminution even though \(P\) is strictly stochastic and has positive real eigenvalues.

**4. Backward Euler is TN.** At \(\theta=1\), \(P=(I-hQ)^{-1}\). Write the nonsingular tridiagonal \(M=I-hQ\) in ordinary \(LDU\) form. All diagonal pivots are strictly positive: \(M\) is positively diagonally similar to a symmetric positive-definite tridiagonal matrix, so its leading principal determinants and pivots are positive. The unit lower bidiagonal \(L\) and unit upper bidiagonal \(U\) have nonpositive nontrivial off-diagonals; the positive diagonal matrix \(D\) contains the pivots. The inverses \(L^{-1}\) and \(U^{-1}\) each factor as products of nearest-neighbor elementary shears \(I+sE_{j+1,j}\) or \(I+sE_{j,j+1}\), with \(s\ge0\); each elementary shear is TN. The diagonal \(D^{-1}\) is TN. By Cauchy–Binet, products of TN matrices are TN, hence
\[
P=M^{-1}=U^{-1}D^{-1}L^{-1}
\]
is TN. It is therefore variation diminishing for every input vector.

**5. Dimension two.** For \(n=2\), all entries of \(P\) are strictly positive by step 1. Its determinant is the product of its positive eigenvalues and is strictly positive. These are all the minors required in dimension two, so \(P\) is TN for every \(\theta\ge1\). Dimension three is therefore the first possible obstruction. Combining steps 2, 4, and 5 proves the sharp classification.

## Verification
The standalone `verify.py` uses only standard-library exact fractions, not floating-point approximations. It checks all minors when \(\theta=1\), the strict negative adjacent-minor identity and constructible sign-change witness for \(\theta>1\), positivity, stochasticity, and the resolvent identity across 192 rational parameter choices with sizes \(2\) through \(5\), several heterogeneous rates, three stepsizes, and four theta values. It also checks the following independent, explicit three-state example.

Take \(n=3\), unit rates in both directions, \(h=1\), \(\theta=2\), and
\[
Q=\begin{pmatrix}-1&1&0\\1&-2&1\\0&1&-1\end{pmatrix},\qquad
P=\frac1{21}\begin{pmatrix}16&3&2\\3&15&3\\2&3&16\end{pmatrix}.
\]
The adjacent minor using rows \(1,2\) and columns \(2,3\) equals \(-1/21\). Moreover,
\[
P\begin{pmatrix}0\\1\\-4\end{pmatrix}
=\frac1{21}\begin{pmatrix}-5\\3\\-61\end{pmatrix},
\]
so a single input sign change becomes two. These finite checks are supplementary; the preceding argument proves the statements for arbitrary positive real rates, every \(n\), and every \(h>0\).

## Relationship to prior work
Fallat and Tsatsomeros (2002), Section 4 and Theorem 4.5, already establish total nonnegativity of tridiagonal \(M\)-matrix inverses and a Cayley-transform factorization of totally nonnegative matrices under suitable hypotheses. The backward-Euler part of the present theorem is therefore classical, not a new contribution. Their Cayley statement concerns a distinct factorization regime with a TN explicit factor; it does not assert the universal negative-minor identity for \(\theta>1\).

Jin, Lazarov, Thomée, and Zhou (2015) study nonnegativity preservation under finite-element discretization of diffusion/subdiffusion. Higueras and Roldán (2023) analyze entrywise positivity and maximum-norm contractivity of Crank–Nicolson for the heat equation, explicitly defining numerical positivity by nonnegative matrix entries. Neither inspected treatment establishes the stronger \(\theta>1\) ordered sign-variation boundary for every birth-death generator. The present contribution is specifically the exact sharp obstruction and an explicit additional-sign-change witness, not positivity of the resolvent itself.

## Limitations
The theorem applies to finite, irreducible, nearest-neighbor birth-death generators with strictly positive rates in both directions and to the \(\theta\ge1\) family only. It does not classify \(0\le\theta<1\), higher-dimensional graph generators, nontridiagonal matrices, spatially discretized PDEs with general mass matrices, or eventual sign variation after repeated steps. Its originality is compared against the primary sources listed; an equivalent statement may exist elsewhere in the older total-positivity literature. Public availability of the 2002 source is verified at the month/year level, not a trustworthy original online calendar day; the date field accompanying this record uses the earliest separately verified day-resolved arXiv source.

## References
1. S. M. Fallat and M. J. Tsatsomeros, “On the Cayley transform of positivity classes of matrices,” Electronic Journal of Linear Algebra 9 (September 2002), 190–196. DOI: 10.13001/1081-3810.1086; Section 4, Theorem 4.5. Full text: https://journals.uwyo.edu/index.php/ela/article/download/173/173.
2. B. Jin, R. Lazarov, V. Thomée, and Z. Zhou, “On Nonnegativity Preservation in Finite Element Methods for Subdiffusion Equations,” arXiv:1510.02825v1, first submitted 2015-10-09 UTC, Sections 3–4. https://arxiv.org/abs/1510.02825.
3. I. Higueras and T. Roldán, “A new insight on positivity and contractivity of the Crank–Nicolson scheme for the heat equation,” arXiv:2301.01066v1, first submitted 2023-01-03 UTC, Sections 2–3. https://arxiv.org/abs/2301.01066.
