# A dependence reversal in two-row stochastic successive overrelaxation

## Finding
Consider a two-coordinate successive-overrelaxation (SOR) sweep for a real symmetric positive-definite reference system. Two random effective off-diagonal factors have **identical individual laws** under two choices of dependence: shared random choices or oppositely coupled random choices. At ordinary Gauss–Seidel relaxation, opposite coupling yields the better exact mean-square contraction. At the overrelaxation parameter \(\omega=187/100\), the same opposite coupling becomes mean-square unstable, whereas shared coupling remains exponentially stable. Every individual realized sweep matrix in either scheme has spectral radius \(87/100\), so the instability is caused by random products, not an unstable individual sweep.

This constitutes one explicit dependence-reversal result. The exact parameters are \(r=3/5\), \(h=1/5\), and the two effective factor values \(r-h=2/5\) and \(r+h=4/5\). The strict phenomena persist in an open neighborhood of these values.

## Assumptions and scope
Let \(A=\begin{psmallmatrix}1&r\\r&1\end{psmallmatrix}\), \(r=3/5\). Then \(A\) is positive definite with eigenvalues \(2/5\) and \(8/5\). Study the homogeneous equation \(Ae=0\) under a model in which each SOR coordinate equation is evaluated with a random effective transfer factor in place of \(r\). Thus, for relaxation \(\omega>0\), one sweep acts on \(e=(e_1,e_2)^\mathsf T\) by
\[
 e_1'=(1-\omega)e_1-\omega b e_2,\qquad
 e_2'=(1-\omega)e_2-\omega c e_1',
\]
so the exact sweep matrix is
\[
 M(b,c;\omega)=
 \begin{pmatrix}
 a&-\omega b\\
 -\omega ac&a+\omega^2bc
 \end{pmatrix},\qquad a=1-\omega.
\]
At every sweep choose an independent fresh equiprobable pair from one of the following **two different laws**:
\[
 \mathcal L_{\rm shared}:\quad (b,c)\in\{(2/5,2/5),(4/5,4/5)\};
 \qquad
 \mathcal L_{\rm anti}:\quad (b,c)\in\{(2/5,4/5),(4/5,2/5)\}.
\]
Both laws give each factor the same two-point marginal, with mean \(3/5\). Mean-square stability means \(\mathbb E\|e_k\|_2^2\to0\) for **every deterministic** \(e_0\in\mathbb R^2\). All operations following the draw are exact. These random transfer factors model deliberately dependent coefficient approximation; they need not be actual adjacent IEEE floating-point rounding outcomes. The system is homogeneous to isolate the multiplicative error dynamics; no assertion about the inhomogeneous rounding-error floor is made.

## Proof
For \(\omega=1\), \(a=0\), and one sweep maps \((e_1,e_2)\) to \((-be_2,bc e_2)\). Thus each successive second component is multiplied by the fresh independent product \(bc\), and the sharp mean-square asymptotic factor is \(\mathbb E(bc)^2\). Under opposite coupling \(bc=8/25\) deterministically, so the factor is \(64/625\). Under shared coupling it is
\[
\frac12\bigl((2/5)^4+(4/5)^4\bigr)=136/625.
\]
Both are less than one, and \(64/625<136/625\). This determines the asymptotic factor of the full vector as well: its first coordinate in sweep \(k\) is a bounded random multiple of the preceding second coordinate, and independence between sweeps gives the same exponential second-moment factor.

Now set \(\omega=187/100\), so \(a=-87/100\). For **both** laws and every permitted pair,
\[
\det M=a^2,\qquad \operatorname{tr}M=2a+\omega^2bc.
\]
As \(0<bc\le16/25\), the discriminant
\[
(\operatorname{tr}M)^2-4\det M
=\omega^2bc(4a+\omega^2bc)<0
\]
because \(4a=-87/25\) and \(\omega^2bc\le(187/100)^2(16/25)<87/25\). Thus every realized matrix has conjugate eigenvalues of modulus \(\sqrt{\det M}=87/100<1\).

For shared coupling consider the integer symmetric matrix
\[
H=\begin{pmatrix}5&4\\4&7\end{pmatrix},\quad H\succ0.
\]
Let \(\mathcal D_{\rm shared}(H)\) be its exact average pullback \(\mathbb E[M^\mathsf THM]\). Direct rational multiplication gives
\[
H-\mathcal D_{\rm shared}(H)=
\begin{pmatrix}
149596073/250000000&59086577/195312500\\
59086577/195312500&2936244641/7812500000
\end{pmatrix}=:D.
\]
Here \(D_{11}>0\) and
\[
\det D=1302500101420780141/9765625000000000000>0.
\]
Therefore \(D\succ0\). The conditional identity
\(\mathbb E[e_{k+1}^\mathsf THe_{k+1}\mid e_k]=e_k^\mathsf T(H-D)e_k\)
and positive definiteness give a fixed \(\eta>0\) such that
\(\mathbb E[e_k^\mathsf THe_k]\le(1-\eta)^k e_0^\mathsf THe_0\); equivalence of Euclidean and \(H\)-norms proves exponential mean-square stability for every deterministic start.

For opposite coupling, let \(\mathcal T_{\rm anti}(Q)=\mathbb E[M Q M^\mathsf T]\). Define
\[
Q=\begin{pmatrix}1500&-748\\-748&1305\end{pmatrix}\succ0,
\qquad
\lambda=12503553/12500000>1.
\]
Indeed, \(Q_{11}>0\) and \(\det Q=1397996>0\). Direct rational multiplication gives the **exact** identity
\[
\mathcal T_{\rm anti}(Q)=\lambda Q.
\]
As sweeps are independent, \(\mathcal T_{\rm anti}^k(Q)=\lambda^kQ\). Decompose the positive-definite matrix \(Q\) into a finite positive sum of rank-one matrices \(v_jv_j^\mathsf T\). If every deterministic initialization \(v_j\) had mean-square error tending to zero, the positive sum would also tend to zero, contradicting \(\operatorname{tr}\mathcal T_{\rm anti}^k(Q)=\lambda^k\operatorname{tr}Q\). In fact one deterministic rank-one contribution has exponential growth along a subsequence. Hence opposite coupling is not mean-square stable for all starts.

Both strict matrix inequalities remain valid in a neighborhood of the stated parameters: positive definiteness of \(D,Q\), the eigenmatrix's spectral eigenvalue exceeding one, and the sample discriminant inequalities are strict; the shared moment operator's stability and the antithetic moment operator's spectral instability persist by continuity of eigenvalues and the moment operators. Thus the reversal is robust, not an isolated equality.

## Verification
Run `python verify.py` with Python 3 (standard library only). It independently constructs the two rational sweep matrices for each coupling, checks the exact \(\omega=1\) mean-square factors, verifies all four individual sweep characteristic discriminants, checks the strict Lyapunov matrix \(D\), and checks \(\mathcal T_{\rm anti}(Q)=\lambda Q\) by exact rational arithmetic. The successful execution produces `VERIFY_OK`. These finite algebraic identities are the inputs to the above all-iteration proof; the code is not a substitute for that proof.

## Relationship to prior work
Lindquist, Appelhans, Jackson, and Derlaga (2026) motivate the sensitivity of stationary matrix-splitting iterations to precision and conditioning. Their publicly indexed abstract concerns a mixed-precision deterministic technique and iterative refinement; the complete primary text was inaccessible at this review, so it is **not** asserted that their full paper fails to cover this exact example. Connolly, Higham, and Mary (2021) analyze standard stochastic rounding and the conditional mean-independence of its errors; the paired dependent choices here expressly do not satisfy those assumptions and are a different model. Fox and Parker (2017) analyze stochastic Gibbs/linear-system matrix-splitting analogies and their convergence rates; their additive sampling mechanism is different. General stochastic fixed-point and covariance-matrix methods explain how to formulate second-moment tests, but no inspected source gives this same-marginal shared-versus-antithetic SOR reversal with the exact rational certificates above. A previously derived exact delay-distribution law for randomized two-coordinate Gauss–Seidel varies coordinate choices and stale-read times, not the within-sweep joint law of effective coefficients.

## Limitations
This is a mathematically exact randomized effective-coefficient model, **not** a prediction for IEEE standard stochastic rounding, real hardware, or inhomogeneous systems. The pairs across sweeps are i.i.d.; within each sweep their dependence is prescribed. The result is a robust two-dimensional counterexample, not a sharp general stability phase diagram for arbitrary dimensions, relaxation parameters or noise laws. While all individual sweep matrices are spectrally stable, this alone does not decide behavior of their products. The motivating 2026 primary full text was unavailable; an equivalent older exact example in random matrix product or stochastic SOR literature remains an originality risk.

## References
1. N. Lindquist, D. Appelhans, C. W. Jackson, and J. M. Derlaga, *A Mixed-Precision Model for Matrix-Splitting Methods*, arXiv:2610.06414, first public 2026-10-05. https://arxiv.org/abs/2610.06414
2. M. P. Connolly, N. J. Higham, and T. Mary, *Stochastic Rounding and Its Probabilistic Backward Error Analysis*, SIAM J. Sci. Comput. 43 (2021), A566–A585, DOI:10.1137/20M1334796. https://doi.org/10.1137/20M1334796
3. C. Fox and A. Parker, *Accelerated Gibbs sampling of normal distributions using matrix splittings and polynomials*, Bernoulli 23 (2017), 3711–3743, arXiv:1505.03512. https://arxiv.org/abs/1505.03512
4. P. Richtárik and M. Takáč, *Stochastic Reformulations of Linear Systems: Algorithms and Convergence Theory*, SIAM J. Matrix Anal. Appl. (2019), DOI:10.1137/18M1179249. https://doi.org/10.1137/18M1179249
