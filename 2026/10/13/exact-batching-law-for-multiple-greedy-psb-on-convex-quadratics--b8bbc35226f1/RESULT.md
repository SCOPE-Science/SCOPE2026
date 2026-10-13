# Exact batching law for multiple greedy PSB on convex quadratics
## Finding

Consider the multiple greedy Powell--Symmetric--Broyden scheme on the strongly convex quadratic
\[
f(x)=\frac12\langle Ax,x\rangle-\langle b,x\rangle,
\qquad
\mu I\preceq A\preceq LI,
\]
with the source initialization
\[
G_0=LI.
\]
Let \(e_1,\ldots,e_n\) be the fixed orthogonal basis used by the greedy rule, write
\[
p_i=\frac{e_i}{\|e_i\|},
\qquad
d_i=L-p_i^TAp_i,
\]
and let
\[
s=\#\{i:d_i>0\}.
\]

For every set \(S\) of basis directions already chosen by nontrivial greedy PSB updates, the Hessian error has the exact form
\[
G-A=P_{S^c}(LI-A)P_{S^c},
\qquad
P_{S^c}=I-\sum_{i\in S}p_ip_i^T.
\]
Therefore an unselected direction \(p_i\) has greedy score exactly
\[
p_i^T(G-A)p_i=d_i,
\]
whereas every selected direction has score zero. Hence the nontrivial greedy updates select the positive deficits \(d_i\) in nonincreasing order, with arbitrary tie breaking. The order is fixed at initialization: it is independent of the primal iterates, the linear term \(b\), and all off-diagonal entries of \(A\) except insofar as those entries affect positive semidefiniteness.

Exactly \(s\) nontrivial greedy PSB updates are necessary and sufficient to recover the Hessian:
\[
G=A.
\]
Directions with \(d_i=0\) need no update, because positive semidefiniteness of \(LI-A\) implies
\[
p_i^T(LI-A)p_i=0
\quad\Longrightarrow\quad
(LI-A)p_i=0.
\]

Now specialize the source multiple-update scheme to the quadratic. Its strong self-adjointness constant can be taken as zero, so its correction factor is one. Each completed outer iteration therefore performs exactly \(t+1\) greedy PSB updates against the same matrix \(A\), until \(A\) has been identified. Consequently, after \(q\) completed outer iterations the number of nontrivial updates is
\[
\min\{q(t+1),s\},
\]
and, for \(s>0\), the first outer index with an exact Hessian is
\[
q_*=\left\lceil\frac{s}{t+1}\right\rceil.
\]
If \(s=0\), then \(G_0=A\) already and \(q_*=0\).

Once \(G_{q_*}=A\), the next primal step is Newton's step and reaches the exact minimizer:
\[
x_{q_*+1}
=x_{q_*}-A^{-1}(Ax_{q_*}-b)
=A^{-1}b.
\]
Thus the exact worst-case optimizer-step count when all \(n\) deficits are positive is
\[
\left\lceil\frac{n}{t+1}\right\rceil+1.
\]

This cutoff is sharp. Take a diagonal quadratic with distinct eigenvalues
\[
0<a_1<a_2<\cdots<a_s<L
\]
in the active basis directions, choose \(b=0\), and initialize the primal error entirely in the direction whose deficit is processed last. Before that final matrix update, the corresponding preconditioner entry is still \(L\), so every preceding primal step multiplies that coordinate by
\[
1-\frac{a_s}{L}>0.
\]
The iterate is therefore still nonoptimal immediately before the exact Hessian becomes available. The following Newton step is the first forced exact solve.

The multiple strategy consequently has a precise quadratic interpretation: it can reduce the number of outer quasi-Newton solves by batching up to \(t+1\) predetermined Hessian-identification updates per iteration, but it does not reduce the total number \(s\) of nontrivial PSB matrix updates.

## Assumptions and scope

The statement uses exactly the source PSB update and its coordinate-greedy rule. The basis may be any fixed orthogonal basis; normalization to \(p_i\) only removes the denominator from the source Rayleigh quotient.

The initialization \(G_0=LI\) and the spectral assumption \(A\preceq LI\) imply
\[
R_0:=G_0-A=LI-A\succeq0.
\]
That positive semidefiniteness is essential for the assertion that a zero diagonal deficit marks an already exact basis direction.

The source multiple-update scheme is defined for general nonlinear objectives. The present result concerns its exact behavior on constant-Hessian strongly convex quadratics. It does not claim that the update order remains predetermined for varying Hessians.

## Proof

For a unit basis direction \(p\), write
\[
R=G-A.
\]
The PSB formula gives the exact error update
\[
R^+
=R-Rpp^T-pp^TR+(p^TRp)pp^T
=(I-pp^T)R(I-pp^T).
\]

For distinct orthonormal basis directions, the coordinate projectors commute. Hence after updating the directions indexed by \(S\), repeated substitution gives
\[
R_S
=P_{S^c}R_0P_{S^c},
\qquad
P_{S^c}=I-\sum_{i\in S}p_ip_i^T.
\]
For \(i\notin S\), orthogonality gives \(P_{S^c}p_i=p_i\), so
\[
p_i^TR_Sp_i
=p_i^TR_0p_i
=L-p_i^TAp_i
=d_i.
\]
For \(i\in S\), \(P_{S^c}p_i=0\), so the score is zero.

Thus every positive unselected score is invariant until selected. The greedy rule therefore processes the positive values \(d_i\) from largest to smallest, apart from ties.

If \(d_i=0\), then
\[
p_i^TR_0p_i=0.
\]
Since \(R_0\succeq0\), write \(R_0=B^TB\). Then
\[
0=p_i^TB^TBp_i=\|Bp_i\|^2,
\]
so \(R_0p_i=0\). Thus every zero-deficit coordinate is already in the kernel and requires no update.

Conversely, as long as some positive deficit remains, its greedy score is positive, so \(R_S\ne0\). After all \(s\) positive deficits have been selected, every basis vector belongs to the kernel of \(R_S\), hence \(R_S=0\). Therefore exactly \(s\) nontrivial updates are necessary and sufficient for \(G=A\).

For a quadratic Hessian, the source strong self-adjointness correction parameter can be chosen as \(M=0\). In one outer iteration of the multiple greedy scheme, the algorithm first applies \(t\) greedy PSB refinements to \(G_k\) against \(A\), then applies one further greedy PSB update when constructing \(G_{k+1}\). Hence each completed outer iteration contains \(t+1\) updates until the finite identification is complete. The counting formula and
\[
q_*=\left\lceil\frac{s}{t+1}\right\rceil
\]
follow immediately.

After identification, the next primal update uses \(G_{q_*}=A\), so
\[
x_{q_*+1}=A^{-1}b.
\]

For sharpness, use a diagonal \(A\) with distinct positive deficits. The greedy order is then unique. Place the initial primal error in the coordinate with the smallest positive deficit, which is processed last. Until its update, that diagonal entry of \(G\) remains \(L\); the primal coordinate is multiplied at every preceding outer step by \(1-a_s/L\), which is strictly between zero and one. It cannot vanish before the final identification update. Hence the following Newton step is genuinely required.

## Verification

The standalone script `artifacts/verify_psb_batching.py` uses exact rational arithmetic. It checks the PSB masking identity on a non-diagonal positive-definite example, verifies that unselected greedy scores remain invariant, and simulates a sharp diagonal case with \(n=5\) and \(t=1\). In that case five nontrivial matrix updates require exactly three completed outer iterations, and the fourth primal point is the first exact minimizer for the chosen initial error.

The computation is supporting evidence only. The exact formulas above prove the result for every dimension and every fixed orthogonal basis satisfying the stated assumptions.

## Relationship to prior work

The 2026 source proves finite Hessian recovery in at most \(n\) iterations for its single-update greedy PSB scheme on quadratics and separately introduces the multiple greedy PSB method for general nonlinear objectives. Its multiple-update analysis gives a faster local superlinear rate, but it does not state the exact quadratic batching law, the invariant coordinate scores, the reduced count \(s\), or the sharp outer-iteration cutoff above.

The 2023 greedy-PSB predecessor also proves finite quadratic termination, but its greedy rule maximizes a residual-vector norm rather than the diagonal Rayleigh score used by the 2026 source. It does not provide the present predetermined ordering or multiple-update count.

A 2025 projection-operator framework gives general sufficient conditions for quadratic termination of PSB and other quasi-Newton families. That broader termination theory does not specify this source algorithm's coordinate ordering, exact number \(s\) of nontrivial updates, or the batching law \(q_*=\lceil s/(t+1)\rceil\).

Multiple greedy updates have also been developed for other quasi-Newton families. Those results motivate repeated matrix refinements but do not imply the PSB-specific masking identity and exact outer-versus-matrix-update tradeoff proved here.

## Limitations

The finite batching law is a constant-Hessian result. For nonlinear objectives, the target Hessian changes with the iterate and the source correction factor need not equal one, so the selected directions need not follow a predetermined order.

The result counts nontrivial PSB matrix updates and outer primal solves separately. It does not assert a wall-clock speedup, because the relative cost of Hessian-vector information and primal linear solves depends on the implementation.

The exact cutoff uses the source initialization \(G_0=LI\) and a fixed orthogonal greedy basis. Different initial matrices or changing bases can have different identification laws.

## References

1. M. Du, Z. Liu, *The multiple greedy PSB method with faster superlinear convergence rate*, Optimization 75(13), 3579--3606, 2026. DOI: 10.1080/02331934.2026.2615215.
2. Z.-Y. Ji, Y.-H. Dai, *Greedy PSB methods with explicit superlinear convergence*, Computational Optimization and Applications 85, 753--786, 2023. DOI: 10.1007/s10589-023-00495-y.
3. Z. Ji, *Improving Quasi-Newton Methods via Image and Projection Operators*, arXiv:2508.10211v1, 2025.
4. Y. Du, K. You, *Distributed Adaptive Greedy Quasi-Newton Methods with Explicit Non-asymptotic Convergence Bounds*, arXiv:2311.18210v1, 2023.
