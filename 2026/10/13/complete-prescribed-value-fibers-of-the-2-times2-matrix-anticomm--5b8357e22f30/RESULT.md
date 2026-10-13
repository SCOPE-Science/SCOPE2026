# Complete prescribed-value fibers of the \(2\times2\) matrix anticommutator over odd finite fields

## Finding

For every odd prime power \(q\), let \(k=\mathbb F_q\) and let
\[
F_q(B)=\#\{(X,Y)\in M_2(k)^2:XY+YX=B\}.
\]
For a nonscalar matrix \(B\), let \(e(B)\) be the number of \(k\)-rational lines in \(k^2\) preserved by \(B\); let \(z(B)\) count those lines on which \(B\) acts by zero. Then
\[
\boxed{F_q(B)=q^4-q^2+q(q-1)\bigl(qz(B)-e(B)\bigr).}
\]
At the two scalar types, the exact counts are
\[
\boxed{F_q(0)=q^5+3q^4-2q^3-2q^2+q,\qquad
F_q(\beta I)=q^5+q^4-2q^3-q^2+q\quad(\beta\in k^\times).}
\]
Consequently there are exactly **seven distinct possible fiber sizes**, all attained for every odd \(q\):

| Conjugacy type of the prescribed target \(B\) | \((e(B),z(B))\) if nonscalar | Fiber size |
| --- | --- | --- |
| Zero scalar | not applicable | \(q^5+3q^4-2q^3-2q^2+q\) |
| Nonzero scalar | not applicable | \(q^5+q^4-2q^3-q^2+q\) |
| Irreducible quadratic characteristic polynomial | \((0,0)\) | \(q^4-q^2\) |
| Two distinct nonzero eigenvalues in \(k\) | \((2,0)\) | \(q^4-q^2-2q(q-1)\) |
| One nonzero eigenvalue, nontrivial Jordan block | \((1,0)\) | \(q^4-q^2-q(q-1)\) |
| Distinct eigenvalues, one zero and one nonzero | \((2,1)\) | \(q^4-q^2+q(q-1)(q-2)\) |
| Nonzero nilpotent Jordan block | \((1,1)\) | \(q^4-q^2+q(q-1)^2\) |

Every \(B\) is attainable (take \(X=I\) and \(Y=B/2\)); the theorem determines its *multiplicity*, not mere attainability.

## Assumptions and scope

All matrices, eigenlines, and pair counts are over the finite field \(k=\mathbb F_q\), where \(q\) is an arbitrary odd prime power. Both factors \(X,Y\) range independently over the entire \(4\)-dimensional space \(M_2(k)\). The count treats ordered pairs. In characteristic \(2\), the operation coincides with the commutator, and no characteristic-two claim is made here. Under the normalized Jordan product \(X\circ Y=(XY+YX)/2\), the fiber over \(B\) is \(F_q(2B)\).

For a scalar \(B\), the definitions \(e(B),z(B)\) still make sense: \(e(B)=q+1\), while \(z(B)=q+1\) at zero and \(z(B)=0\) at nonzero scalars. The separated scalar formulas account for extra Fourier mass.

## Proof

**1. Fourier reduction.** Fix a nontrivial additive character \(\psi:k\to\mathbb C^\times\). The trace pairing on \(M_2(k)\) is nondegenerate. Orthogonality gives
\[
F_q(B)=q^{-4}\sum_{Z,X,Y\in M_2(k)}
\psi\bigl(\operatorname{tr}(Z(XY+YX-B))\bigr).
\]
Cyclicity of trace makes the \(X\)-sum equal to \(q^4\) when \(ZY+YZ=0\), and zero otherwise. Hence
\[
F_q(B)=\sum_{Z\in M_2(k)}\psi(-\operatorname{tr}(ZB))q^{d(Z)},
\qquad d(Z)=\dim_k\ker(Y\mapsto ZY+YZ).
\]

**2. Exact kernel-dimension classification.** In odd characteristic,
\[
d(Z)=\begin{cases}
4&Z=0,\\
2&Z\ne0,\ \operatorname{tr}Z=0,\\
1&\operatorname{tr}Z\ne0,\ \det Z=0,\\
0&\operatorname{tr}Z\ne0,\ \det Z\ne0.
\end{cases}
\]
To verify all cases, pass to an algebraic closure (kernel dimension does not change on field extension). The linear operator \(Y\mapsto ZY+YZ\) has eigenvalues \(2\lambda,\lambda+\mu,\lambda+\mu,2\mu\) when \(\lambda,\mu\) are the eigenvalues of \(Z\), counting algebraic multiplicities; for repeated eigenvalues, all the listed values are nonzero unless \(Z\) is nilpotent. If \(Z\) is a nonzero nilpotent Jordan block, a direct substitution of \(Z=E_{12}\) gives output \(\begin{psmallmatrix}c&a+d\\0&c\end{psmallmatrix}\) for \(Y=\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}\), and therefore a two-dimensional kernel. If \(Z\) has trace zero and is nonsingular, its two nonzero roots are opposite, giving a two-dimensional kernel; if trace is nonzero and determinant zero, exactly one eigenvalue of the Sylvester operator vanishes. Thus
\[
q^{d(Z)}=1+(q^2-1){\bf1}_{\operatorname{tr}Z=0}
+(q-1){\bf1}_{\operatorname{tr}Z\ne0,\det Z=0}
+(q^4-q^2){\bf1}_{Z=0}.
\]
(The last expression also gives \(q^4\) at \(Z=0\).)

**3. Fourier sums.** The trace-zero hyperplane has \(q^3\) elements, and its annihilator under the trace pairing is the scalar line. Thus
\[
\sum_{\operatorname{tr}Z=0}\psi(-\operatorname{tr}(ZB))
=q^3\,{\bf1}_{B\text{ scalar}}.
\]
Every matrix with nonzero trace and zero determinant is uniquely \(Z=tP\), for \(t\in k^\times\) and a rank-one idempotent \(P\). These idempotents are projections onto one of \(q+1\) image lines along one of its \(q\) complementary kernel lines, so there are \(q(q+1)\) in total. Set
\[
u(B)=\#\{P:P^2=P,\ \operatorname{rank}P=1,\ \operatorname{tr}(PB)=0\}.
\]
For each \(P\), character orthogonality in \(t\) gives
\[
\sum_{\operatorname{tr}Z\ne0,\det Z=0}\psi(-\operatorname{tr}(ZB))
=q\,u(B)-q(q+1).
\]

**4. Projectors and eigenlines.** Fix an image line \(L\). If \(L\) is \(B\)-invariant, then \(\operatorname{tr}(PB)\) is the eigenvalue of \(B\) on \(L\), independent of the \(q\) complements: all \(q\) work when that eigenvalue is zero, and none works otherwise. If \(L\) is not invariant, varying its complementary kernel gives a nonconstant affine-linear scalar expression, vanishing for exactly one complement. Counting lines yields
\[
u(B)=q\,z(B)+(q+1-e(B)).
\]
Combining the character sums and noting \(\sum_Z\psi(-\operatorname{tr}(ZB))=q^4{\bf1}_{B=0}\) gives the single all-target identity
\[
F_q(B)=q^4-q^2+q^4{\bf1}_{B=0}
+q^3(q^2-1){\bf1}_{B\text{ scalar}}
+q(q-1)\bigl(qz(B)-e(B)\bigr).
\]
Substitute the scalar values of \(e,z\), or the five nonscalar rational canonical types, to obtain every formula in the finding.

**5. Exhaustiveness and distinctness.** Every nonscalar \(2\times2\) matrix is either irreducible over \(k\), semisimple with two distinct rational eigenvalues, or a nontrivial Jordan block with one rational eigenvalue. In the last two cases, the eigenvalues are zero or nonzero as shown in the table. All five nonscalar types exist for odd \(q\ge3\); their fiber values are strictly ordered as listed, after ordering the five sizes as distinct-nonzero, nontrivial-nonzero, irreducible, one-zero semisimple, nilpotent. Both scalar values are larger than all nonscalar values and distinct from each other. Thus exactly seven sizes occur.

## Verification

The bundled standalone `verify.py` exhaustively enumerates all ordered \((X,Y)\) and all \(B\in M_2(\mathbb F_q)\) at \(q=3\) and \(q=5\), independently calculating each fiber and its predicted eigenline statistic. Expected distinct fiber counts are \(60,66,72,78,84,264,417\) for \(q=3\) and \(560,580,600,660,680,3480,4705\) for \(q=5\). Running `python verify.py` must print `VERIFY_OK`. Those finite enumerations are checks, not the proof for arbitrary odd prime powers.

## Relationship to prior work

Bourgeois [1] studies the linear Sylvester/Jordan operator \(Y\mapsto AY+YA\), especially determinants, invertibility, and real-field conditions. His linear-operator viewpoint underlies the kernel-rank stratification above, but his main results do not give the sum over all left factors or the finite-field prescribed-target distribution. Huang [2] counts solutions of the *homogeneous* quantum-plane relation \(XY=\zeta YX\) over finite fields, including the anti-commuting equation \(XY+YX=0\) when \(\zeta=-1\). Consequently **the zero-target count above is not asserted to be new**. The new determination is the complete target-dependent fiber distribution, including six nonzero-target strata and the precise rational-eigenline dependence. The additive Fourier and rank-one-projector methods are elementary; they are tools rather than new claims. A nonzero-target count might conceivably occur elsewhere in the matrix-equation literature, so independent priority checking remains appropriate.

## Limitations

The classification is proved only for \(2\times2\) matrices and odd finite characteristic; it says nothing about dimensions at least \(3\). It is an exact algebraic counting statement, not a geometric irreducibility result, and no general formula for other bilinear matrix words is claimed. Earlier independent work on the identical nonzero-target fibers may remain to be found.

## References

[1] Gerald Bourgeois, *About the matrix function \(X\mapsto AX+XA\)*, arXiv:1210.0766v1, first posted 2012-10-02.

[2] Yifeng Huang, *Counting on the variety of modules over the quantum plane*, arXiv:2110.15570v1 (2021), *Algebraic Combinatorics* **5** (2022), 583–592, DOI 10.5802/alco.230.
