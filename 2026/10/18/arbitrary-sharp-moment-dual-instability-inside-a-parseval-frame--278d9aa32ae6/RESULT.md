# Arbitrary sharp moment-dual instability inside a Parseval frame

## Finding

For every nondecreasing sequence \((b_j)_{j\ge1}\) of real numbers with \(b_j\ge2\) and \(b_j\to\infty\), there exists one Parseval frame and a nested family of finite coordinate-moment constraints with the following exact profile:

\[
\inf_{\substack{U\in\mathcal B(H,K)\\T^*U=I,\ A_NU=0}}\|U\|^2=b_N\qquad(N\ge1).
\]

Every finite constraint is feasible; the infinite constraint is impossible for bounded dual analysis operators even though the infinite constraint row subspace and the frame-analysis range have zero intersection. The finite optimal duals can be chosen so that their infinite moment defects converge strongly to zero, but

\[
\inf_{\substack{U\in\mathcal B(H,K)\\T^*U=I}}\|A_\infty U\|=1,
\qquad \|A_\infty U_N\|=1\quad(N\ge1).
\]

In particular, arbitrarily fast Bessel-bound divergence is compatible with a fixed Parseval reference frame and strong convergence of the moment defects. This is a realization and sharp-instability statement, not a claim that the elementary positive-angle criterion is new.

## Assumptions and scope

All Hilbert spaces may be real or complex. Set \(H=\ell^2(\mathbb N)\), \(K=H\oplus H\), and use the standard orthonormal basis \((e_j)_{j\ge1}\). Choose an arbitrary nondecreasing real sequence with \(b_j\ge2\) and \(b_j\to\infty\). Define positive numbers and diagonal operators by

\[
 d_j=b_j^{-1/2},\qquad c_j=(1-b_j^{-1})^{1/2},
 \qquad De_j=d_je_j,\quad Ce_j=c_je_j.
\]

The two-channel frame is \(F=\{c_je_j:j\ge1\}\cup\{d_je_j:j\ge1\}\), with analysis \(T:H\to K\) given by \(Tx=(Cx,Dx)\). Its coefficient moments are the bounded maps \(A_N:K\to H\), \(A_N(y,z)=P_Ny\), where \(P_N\) is the projection onto the first \(N\) basis vectors. The limiting moment map is \(A_\infty(y,z)=y\). The restricted duals are bounded analysis operators \(U=(U_0,U_1):H\to K\) satisfying \(T^*U=I\) and \(A_NU=0\), where \(\|U\|^2\) is precisely the least upper Bessel bound of the associated dual frame. A bounded dual automatically has a positive lower frame bound because \(T^*U=I\) and \(\|T^*\|=1\).

The quantity \(\inf\|U\|^2\) is taken over *all* bounded dual analysis operators meeting each constraint, including operators that couple different coordinates; it is not an optimization limited to diagonal duals. The row subspace of \(A_N\) means \(W_N=\operatorname{Ran}(A_N^*)=P_NH\oplus\{0\}\); the infinite row subspace is \(W_\infty=H\oplus\{0\}\). Strong convergence refers to convergence on every vector of \(H\), not convergence in operator norm.

## Proof

**Step 1 (Parseval property).** As \(c_j^2+d_j^2=1\), the operators satisfy \(C^2+D^2=I\), hence

\[
\|Tx\|^2=\|Cx\|^2+\|Dx\|^2=\|x\|^2.
\]

Thus \(T\) is an isometry, and \(F\) is Parseval for every admissible profile.

**Step 2 (universal finite-moment lower bound).** Fix \(N\ge1\), and let \(U=(U_0,U_1)\) be any bounded dual analysis operator with \(P_NU_0=0\). The reconstruction identity is

\[
C U_0+D U_1=I.
\]

Apply it to \(e_N\) and take the \(e_N\) coordinate. Since \(\langle U_0e_N,e_N\rangle=0\), we obtain \(d_N\langle U_1e_N,e_N\rangle=1\). Consequently

\[
\|U\|^2\ge \|Ue_N\|^2\ge d_N^{-2}=b_N.
\]

This step rules out improvement even by nondiagonal duals.

**Step 3 (attaining the finite bound).** Define

\[
U_Nx=\big(C(I-P_N)x,\ D^{-1}P_Nx+D(I-P_N)x\big),
\]

where \(D^{-1}P_N\) is bounded because it acts on a finite-dimensional range. Directly,

\[
CU_{N,0}+DU_{N,1}
=(C^2+D^2)(I-P_N)+P_N=I,
\qquad A_NU_N=0.
\]

Different basis coordinates have mutually orthogonal analysis images. Their squared norms are exactly \(b_j\) for \(j\le N\) and exactly \(1\) for \(j>N\). Since \((b_j)\) is nondecreasing,

\[
\|U_N\|^2=\max\{1,b_1,\ldots,b_N\}=b_N.
\]

This proves the exact optimum and exhibits an attaining dual frame for every finite constraint. The dual lower frame bound is at least \(1\), since \(\|x\|=\|T^*U_Nx\|\le\|U_Nx\|\).

**Step 4 (algebraic transversality does not persist quantitatively).** Every \(W_N\) and \(W_\infty\) intersects \(T(H)\) trivially: if \((Cx,Dx)\in H\oplus\{0\}\), then \(Dx=0\), and positivity of all \(d_j\) forces \(x=0\). For \(Q_N\), the orthogonal projection onto \(\ker A_N\), the restriction of \(Q_NT\) has exactly the minimum modulus

\[
\inf_{\|x\|=1}\|Q_NTx\|=d_N=b_N^{-1/2}.
\]

Indeed its squared norm is \(\sum_{j\le N}d_j^2|x_j|^2+\sum_{j>N}|x_j|^2\), with equality at \(e_N\). In contrast, \(Q_\infty Tx=(0,Dx)\) has minimum modulus zero because \(d_j\to0\). More explicitly,

\[
W_\infty+T(H)=H\oplus D(H)
\]

is dense but not closed in \(K\): the positive diagonal \(D\) is compact, injective and has nonclosed dense range. Thus zero intersection alone gives no bounded extension in this infinite-dimensional situation.

**Step 5 (impossibility of the infinite moment condition).** Were \(U\) a bounded dual with \(A_\infty U=U_0=0\), then \(D U_1=I\). But \(d_j\langle U_1e_j,e_j\rangle=1\), which forces \(\|U_1\|\ge d_j^{-1}\) for every \(j\), impossible as \(d_j\downarrow0\). Equivalently, the compact operator \(D\) cannot have a bounded right inverse on infinite-dimensional \(H\).

**Step 6 (sharp strong-versus-uniform gap).** For the concrete finite optimizers,

\[
A_\infty U_N=C(I-P_N)\xrightarrow[N\to\infty]{\mathrm{strong}}0.
\]

Yet \(c_j\to1\), so \(\|A_\infty U_N\|=\|C(I-P_N)\|=1\) for every \(N\). If \(U=(U_0,U_1)\) is *any* bounded dual, then \(CU_0=I-DU_1\). The operator \(DU_1\) is compact because \(D\) is compact. Applied to the weakly null basis \(e_j\), this implies \(\|CU_0e_j\|\to1\). Hence \(\|U_0\|\ge\|CU_0\|\ge1\), because \(\|C\|=1\). Taking \(U=T\), whose first channel is \(C\), attains \(\|U_0\|=1\). Therefore the uniform defect minimum equals exactly one. The proof is complete.

## Verification

The analytic argument derives the lower bound from one forced coefficient and the upper bound from an explicitly bounded diagonal dual, so no finite enumeration is used to establish an infinite-dimensional infimum. In the optional standalone `checker.py`, exact rational Pythagorean coefficients satisfy \(c_j^2+d_j^2=1\) and verify reconstruction, finite constraints, monotonicity and exact optimal diagonal costs for finite truncations. The code uses only the Python standard library. To run: `python checker.py`.

The checker deliberately does **not** certify that no untested nondiagonal dual improves the bound; that assertion is proved in Step 2. Nor do finite matrices establish nonclosed range or strong-operator convergence; Steps 4–6 are infinite-dimensional proofs.

## Relationship to prior work

Han, Mondal, Liu and Nour (arXiv:2610.11043v1, Section 3, Theorem 3.1) characterize finite-dimensional duals with prescribed vanishing moments through trivial intersection between row and analysis subspaces. Their concluding discussion (Section 5) specifically raises infinite-dimensional extensions and quantitative optimization of such duals. The present realization concerns those open-ended infinite-dimensional and quantitative issues; it does not assert that finite-dimensional transversality or standard dual-operator identities are new.

Koo and Lim (2015, Sections 2–3) develop the classical positive-angle and closed-sum framework for oblique dual frame sequences. In particular, positive angles rather than mere trivial intersection are already standard in the infinite-dimensional theory. Our theorem uses this pre-existing conceptual boundary, but contributes one Parseval-frame construction realizing **any prescribed sharp sequence** of optimal constrained-dual Bessel bounds, along with the exact coexistence of strong defect convergence, uniform gap and infinite infeasibility.

Mondal, Verma and Mohapatra (arXiv:2502.09862v1, Sections 3–4) treat minimal redundancy, infinite frames and finite erasures. Their conclusions concern preservation of the frame property after deletion rather than optimizing nested moment-annihilating duals with a prescribed arbitrary rate. Related published mathematical records on Bessel dual obstructions and on pointwise versus global duality are likewise not statements about this profile-realization invariant.

## Limitations

This is an existence and sharp quantitative boundary theorem for a specifically constructed two-channel diagonal Parseval frame. It does not characterize arbitrary frames, prescribe geometric moment rows beyond coordinate projections, or optimize other measures of robustness. The positive-angle criterion is classical; the novelty claim is confined to the joint sharp realization across every diverging profile and the strong-versus-uniform phenomenon. Relevant earlier infinite-dimensional oblique-duality literature may contain reducible constructions, so independent assessment of publication priority remains appropriate. Finite arithmetic tests are ancillary to the full proof.

## References

1. D. Han, S. Mondal, Y. Liu and M. Nour, *Vanishing Moment Dilations and Applications to Balanced and Graph Frames*, arXiv:2610.11043v1 (first submitted 2026-10-08), https://arxiv.org/html/2610.11043v1.
2. Y. Y. Koo and J. K. Lim, *Extension of Bessel Sequences to Oblique Dual Frame Sequences and the Minimal Projection*, Electronic Journal of Linear Algebra 30 (2015), 51–65, https://journals.uwyo.edu/index.php/ela/article/download/1505/1505/1505.
3. S. Mondal, G. Verma and R. N. Mohapatra, *Robustness of Infinite Frames and Besselian Structures*, arXiv:2502.09862v1 (2025), https://arxiv.org/html/2502.09862v1.
