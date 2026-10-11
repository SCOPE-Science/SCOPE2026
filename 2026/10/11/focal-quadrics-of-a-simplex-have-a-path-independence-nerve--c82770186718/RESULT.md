# Focal quadrics of a simplex have a path-independence nerve

## Finding

Let a nondegenerate simplex in \(\mathbb R^n\), with \(n\ge2\), have a John ellipsoid whose squared semiaxes in principal coordinates are
\[
d_1>d_2>\cdots>d_n>0.
\]
Eydelzon associates to the simplex the focal sets
\[
\mathcal F_k
=
\left\{
x\in\mathbb R^n:
x_k=0,\quad
\sum_{j\ne k}\frac{x_j^2}{d_j-d_k}=1
\right\},
\qquad
2\le k\le n.
\]

For every index set \(S\subseteq\{2,\ldots,n\}\),
\[
\boxed{
\bigcap_{k\in S}\mathcal F_k\ne\varnothing
\quad\Longleftrightarrow\quad
S\text{ contains no consecutive integers}.
}
\]
Every such \(S\) occurs as the exact focal-membership set of some point.

Thus the nerve of
\[
\{\mathcal F_2,\ldots,\mathcal F_n\}
\]
is exactly the independence complex of the path on \(n-1\) vertices. Consequently,
\[
\max_x\#\{k:x\in\mathcal F_k\}
=
\left\lfloor\frac n2\right\rfloor,
\]
and the number of indexed nonempty \(r\)-fold intersections is
\[
\binom{n-r}{r},
\qquad
0\le r\le\left\lfloor\frac n2\right\rfloor.
\]
At a point lying in exactly the focal sets indexed by \(S\), the Jacobian in Eydelzon's construction has exactly \(|S|\) distinct repeated eigenvalues, each of multiplicity two.

For the four-dimensional example printed in the source,
\[
D=\operatorname{diag}(10,6,3,1),
\]
the only nonempty pairwise focal intersection is
\[
\mathcal F_2\cap\mathcal F_4.
\]
It consists of exactly four points,
\[
\boxed{
\left(\pm\frac6{\sqrt7},\,0,\,\pm\sqrt{\frac67},\,0\right),
}
\]
with independent signs. At each point,
\[
\operatorname{spec}(D-xx^{\mathsf T})=\{6,6,1,1\},
\]
and the Jacobian spectrum is
\[
\{3,3,-2,-2\}.
\]

## Assumptions and scope

The squared semiaxes are assumed pairwise distinct. No statement is made for coincident semiaxes.

Write
\[
M(x)=D-xx^{\mathsf T}.
\]
Eydelzon's Jacobian is
\[
J(x)
=
D-xx^{\mathsf T}
-\frac12\|x\|^2 I
=
M(x)-\frac12\|x\|^2 I.
\]
The scalar shift does not change eigenvalue multiplicities, so it is enough to study \(M(x)\).

The theorem classifies nonemptiness and exact incidence patterns. It does not classify connected components, diffeomorphism types, or projective closures of higher intersections.

## Proof

Let the eigenvalues of \(M(x)\), in decreasing order with multiplicity, be
\[
\mu_1\ge\mu_2\ge\cdots\ge\mu_n.
\]
Because \(M(x)\) is a negative rank-one perturbation of \(D\), Cauchy interlacing gives
\[
d_1\ge\mu_1\ge d_2\ge\mu_2\ge\cdots\ge d_n\ge\mu_n.
\]

Eydelzon proves that \(x\in\mathcal F_k\) exactly when \(M(x)\) has the repeated eigenvalue \(d_k\). In the simple-spectrum setting that repeated eigenvalue has multiplicity exactly two. Once \(x_k=0\), the vector \(e_k\) is one eigenvector with eigenvalue \(d_k\). On the complementary coordinate subspace the shifted matrix is an invertible diagonal matrix plus a rank-one perturbation, whose nullity is at most one. Hence the total eigenspace at \(d_k\) has dimension exactly two.

If \(x\in\mathcal F_k\), interlacing forces
\[
\mu_{k-1}=\mu_k=d_k.
\]
If \(x\) also belonged to \(\mathcal F_{k+1}\), then
\[
\mu_k=\mu_{k+1}=d_{k+1},
\]
contradicting \(d_k\ne d_{k+1}\). Thus every simultaneous focal index set has no consecutive integers.

Conversely, fix
\[
S\subseteq\{2,\ldots,n\}
\]
with no consecutive integers. For \(1\le i<n\), define
\[
\mu_i
=
\begin{cases}
d_i,& i\in S,\\
d_{i+1},& i+1\in S,\\
\dfrac{d_i+d_{i+1}}2,& i\notin S,\ i+1\notin S.
\end{cases}
\]
The cases cannot conflict. Finally, choose any \(\delta>0\) and set
\[
\mu_n
=
\begin{cases}
d_n,&n\in S,\\
d_n-\delta,&n\notin S.
\end{cases}
\]
Then
\[
d_i\ge\mu_i\ge d_{i+1}
\]
for \(i<n\), and
\[
\mu_n\le d_n.
\]
For each \(k\in S\),
\[
\mu_{k-1}=\mu_k=d_k,
\]
and there are no other repetitions at a value \(d_j\).

Put
\[
p_D(t)=\prod_{j=1}^n(t-d_j),
\qquad
p_\mu(t)=\prod_{j=1}^n(t-\mu_j),
\]
and define
\[
x_i^2
=
\frac{p_\mu(d_i)}{p_D'(d_i)}.
\]
If \(i\notin S\), interlacing gives the same sign
\[
(-1)^{i-1}
\]
to numerator and denominator, so \(x_i^2>0\). If \(i\in S\), then \(d_i\) is a repeated target eigenvalue and
\[
p_\mu(d_i)=0,
\]
so \(x_i=0\). Thus all \(x_i\) are real.

The rational functions
\[
\frac{p_\mu(t)}{p_D(t)}
\quad\text{and}\quad
1+\sum_{i=1}^n\frac{x_i^2}{t-d_i}
\]
have the same residues at all poles and both tend to \(1\) at infinity. Hence
\[
\frac{p_\mu(t)}{p_D(t)}
=
1+\sum_{i=1}^n\frac{x_i^2}{t-d_i}.
\]
The matrix determinant lemma now gives
\[
\det\!\left(tI-(D-xx^{\mathsf T})\right)
=
p_\mu(t).
\]
Therefore the constructed \(x\) has exactly the target repeated values. Eydelzon's theorem gives
\[
x\in\mathcal F_k
\quad\Longleftrightarrow\quad
k\in S.
\]
This proves both sufficiency and exact realization.

Independent sets of size \(r\) in a path on \(n-1\) vertices are counted by
\[
\binom{n-r}{r},
\]
and the independence number is
\[
\left\lfloor\frac n2\right\rfloor.
\]

For
\[
D=\operatorname{diag}(10,6,3,1),
\]
the equations for \(\mathcal F_2\cap\mathcal F_4\) reduce to
\[
\frac{x_1^2}{4}-\frac{x_3^2}{3}=1,
\qquad
\frac{x_1^2}{9}+\frac{x_3^2}{2}=1.
\]
They give
\[
x_1^2=\frac{36}{7},
\qquad
x_3^2=\frac67.
\]
Thus there are four points. Their squared norm is \(6\), and
\[
\det(tI-M(x))
=
(t-6)^2(t-1)^2.
\]
Subtracting \(3I\) gives the stated Jacobian spectrum.

## Verification

The bundled checker performs exact rational verification of the residue reconstruction for every independent focal index set in dimensions \(2\) through \(10\). It also verifies the path independent-set counts through dimension \(14\) and checks the four-dimensional determinant identity exactly.

These finite checks are supplementary. The all-dimensional theorem is proved by the interlacing and residue argument above.

The primary full text was checked for the John-ellipsoid matrix, the cubic field, the Jacobian, the repeated-eigenvalue theorem, its proof, and the printed four-dimensional focal equations.

## Relationship to prior work

Eydelzon proves that, when the squared semiaxes are distinct, the repeated-eigenvalue locus of the cubic-field Jacobian is the union of the focal sets
\[
\mathcal F_2,\ldots,\mathcal F_n.
\]
The paper treats the focal quadrics individually and gives low-dimensional examples. It does not classify simultaneous intersections, the incidence nerve, the maximum number meeting at one point, or the number of indexed multiple intersections.

General rank-one perturbation theory, including work of Dobosevych and Hryniv, gives broad spectral and inverse-spectral descriptions. Multiplicity restrictions and interlacing are standard background. The contribution here is not the standalone fact that a repeated eigenvalue is double; it is the exact geometric translation of all simultaneous degeneracies into
\[
\operatorname{Nerve}\{\mathcal F_2,\ldots,\mathcal F_n\}
=
\operatorname{Ind}(P_{n-1}),
\]
together with exact realization of every allowed pattern.

Targeted searches for focal-quadric intersections, nonconsecutive repeated eigenvalues, path-independence formulations, and the source identifier found no prior statement of this classification.

## Limitations

The theorem assumes pairwise distinct semiaxes and does not treat their collision limits. It classifies incidence, not the topology of each higher intersection.

Classical confocal-quadric literature may encode related intersection restrictions under different terminology. No such statement was found in the targeted comparison, but the result does not claim a survey-complete historical classification of all synonymous formulations.

## References

1. Anatoly Eydelzon, *Focal Sets of the John Ellipsoid of a Simplex from Its Vertices*, arXiv:2609.37448v1, 25 September 2026.
2. Oles Dobosevych and Rostyslav Hryniv, *Spectra of rank-one perturbations of self-adjoint operators*, Linear Algebra and its Applications 609 (2021), 339--364, DOI: 10.1016/j.laa.2020.09.027.
