# Near-minimal frame spread can coexist with maximal entropy nonidentifiability
## Finding
Let \(\nu\) be a rank-one POVM on \(\mathbb C^d\) normalized by
\[
\int P_z\,d\nu(z)=\frac{I}{d},
\qquad
F_\nu(A)=d\int \operatorname{{tr}}(AP_z)P_z\,d\nu(z).
\]
Write \(F_{{\nu,0}}\) for the restriction to trace-zero Hermitian matrices, \(r_\nu=\operatorname{{rank}}F_{{\nu,0}}\), and
\[
\kappa_\nu=(d+1)\lVert F_{{\nu,0}}\rVert_{{2\to2}}.
\]
Then
\[
\boxed{{\kappa_\nu\ge \frac{{d^2-1}}{{r_\nu}}}}.
\]
Equality holds exactly when all nonzero eigenvalues of \(F_{{\nu,0}}\) are equal.

Suppose now that \(d\) is a prime power and choose any \(m\) bases from a complete set of \(d+1\) mutually unbiased bases. Let \(\nu_m\) be uniform on the resulting \(md\) rank-one projectors. Then
\[
r_{{\nu_m}}=m(d-1),
\qquad
\kappa_{{\nu_m}}=\frac{{d+1}}m,
\]
so every such MUB subset attains the rank-sensitive bound exactly.

For every \(1\le m\le d\), however, entropy is not identifiable from this measurement. For every number \(n\) of independent samples,
\[
\boxed{{R^*_{{n,d}}(\nu_m)=\frac14\log^2 d}},
\]
where the minimax loss is squared error for von Neumann entropy. In particular,
\[
\kappa_{{\nu_d}}=1+\frac1d\longrightarrow1
\]
while the exact minimax entropy risk stays at its largest possible constant-estimator value for all \(n\).

## Assumptions and scope
The measurement model is exactly the fixed, independently repeated rank-one measurement model of arXiv:2610.00270v1. The logarithm convention is the same throughout the entropy loss; changing base rescales both entropy and squared error consistently. The MUB construction requires a complete set of \(d+1\) mutually unbiased bases, hence the stated prime-power assumption. No claim is made for adaptive, collective, or shared-randomness measurement protocols.

For a complete MUB family \(\{{\mathcal B_\alpha\}}_{{\alpha=1}}^{{d+1}}\), mutual unbiasedness means
\[
\operatorname{{tr}}(P_{{\alpha k}}P_{{\beta \ell}})=\frac1d
\quad(\alpha\ne\beta).
\]
For each basis define the trace-zero diagonal subspace
\[
S_\alpha=\operatorname{{span}}\left\{{P_{{\alpha k}}-\frac Id:1\le k\le d\right\}}.
\]
Each \(S_\alpha\) has dimension \(d-1\).

## Proof
The frame operator is positive semidefinite and self-adjoint in the Hilbert--Schmidt inner product. Its superoperator trace is
\[
\operatorname{{Tr}}_{{\mathrm{{HS}}}}F_\nu
=d\int\operatorname{{tr}}(P_z^2)\,d\nu(z)=d.
\]
Also \(F_\nu(I)=I\), so the identity direction contributes the eigenvalue \(1\). Therefore
\[
\operatorname{{Tr}}F_{{\nu,0}}=d-1.
\]
If the nonzero eigenvalues of \(F_{{\nu,0}}\) are \(\lambda_1,\ldots,\lambda_{{r_\nu}}\), positivity gives
\[
\lVert F_{{\nu,0}}\rVert_{{2\to2}}
=\max_j\lambda_j
\ge \frac{{d-1}}{{r_\nu}}.
\]
Multiplying by \(d+1\) proves the rank-sensitive bound. Equality in maximum-at-least-average holds exactly when all positive eigenvalues equal \((d-1)/r_\nu\).

For the MUB subset, let \(\Delta_\alpha\) denote pinching in basis \(\mathcal B_\alpha\). Uniformity gives
\[
F_{{\nu_m}}=\frac1m\sum_{{\alpha=1}}^m\Delta_\alpha.
\]
On trace-zero matrices, \(\Delta_\alpha\) is the Hilbert--Schmidt orthogonal projection onto \(S_\alpha\). For \(\alpha\ne\beta\),
\[
\operatorname{{tr}}\left[\left(P_{{\alpha k}}-\frac Id\right)
\left(P_{{\beta\ell}}-\frac Id\right)\right]=0,
\]
so the spaces \(S_\alpha\) are pairwise orthogonal. Consequently
\[
F_{{\nu_m,0}}=\frac1m P_{{S_1\oplus\cdots\oplus S_m}},
\]
and its spectrum is \(1/m\) with multiplicity \(m(d-1)\) and \(0\) on the orthogonal complement. This proves the formulas for rank and frame spread and shows equality in the universal rank-sensitive bound.

If \(m\le d\), choose an omitted MUB \(\mathcal B_\beta\) and a vector \(|\beta,j\rangle\) in it. Every measured projector has overlap \(1/d\) with this pure state. Thus the complete outcome law under \(\nu_m\) is uniform on the \(md\) outcomes, exactly as for the maximally mixed state \(I/d\). The two indistinguishable states have entropies \(0\) and \(\log d\).

For any estimator \(T\), both endpoint states induce the same data law \(P\), and hence
\[
\max\left\{{\mathbb E_P T^2,\mathbb E_P(T-\log d)^2\right\}
\ge \frac12\mathbb E_P\left[T^2+(T-\log d)^2\right]
\ge \frac14\log^2 d.
\]
Conversely, the constant estimator \(T=(\log d)/2\) has squared error at most \((\log d)^2/4\) for every quantum state because entropy lies in \([0,\log d]\). The minimax identity follows for every \(n\).

## Verification
The proof is symbolic and finite-dimensional; no sampling experiment or numerical search is used to establish it. The critical normalizations were checked directly: the rank-one frame has Hilbert--Schmidt superoperator trace \(d\), the identity is an eigenvector of eigenvalue \(1\), and therefore the trace-zero restriction has trace \(d-1\). For MUBs, the projector identity \(\operatorname{{tr}}(P_{{\alpha k}}P_{{\beta\ell}})=1/d\) makes the trace-zero diagonal subspaces exactly orthogonal, so the displayed spectrum follows without approximation.

The decision-theoretic lower bound uses two states with exactly identical full outcome distributions, not merely nearby distributions. Its matching upper bound is the constant midpoint estimator, so the minimax value is exact for every finite or infinite sample size.

## Relationship to prior work
Song, arXiv:2610.00270v1, introduces the normalized trace-zero frame spread \(\kappa_\nu\), proves a finite-sample entropy lower bound in terms of it, and records \(\operatorname{{Tr}}F_{{\nu,0}}=d-1\). That paper also gives a single-orthonormal-basis example where entropy remains unidentifiable, but that example has the extreme spread \(\kappa_\nu=d+1\). It does not state the rank-sensitive lower bound, its equality condition, or a near-unit-spread nonidentifiability example.

Rehacek et al., arXiv:1509.07614v1, develop incomplete tomography with mutually unbiased bases and exhibit the orthogonality of the corresponding trace-zero diagonal subspaces. Their work addresses reconstruction principles for unmeasured probabilities; it does not give the fixed-measurement entropy minimax identity above or connect incomplete MUBs to the recent frame-spread parameter.

Klappenecker and Roetteler, arXiv:quant-ph/0502031, show that a complete set of \(d+1\) MUBs is a complex projective \(2\)-design. This explains the full-family endpoint \(\kappa=1\), but does not state the sharp rank-spread law or the all-but-one-basis entropy obstruction. Wang and Cui, arXiv:2310.09644, likewise treat complete MUBs as minimal informationally complete measurements in shadow tomography rather than the entropy minimax boundary for incomplete subsets.

## Limitations
The sharp example is confined to prime-power dimensions where a complete MUB family is available. The theorem does not assert that every non-informationally-complete rank-one measurement with \(\kappa\) close to \(1\) has large entropy risk, nor does it determine the smallest possible \(\kappa\) among all non-informationally-complete rank-one POVMs. It concerns fixed independent measurements only. The exact minimax obstruction comes from an omitted MUB direction and therefore does not address protocols that alter the measurement between copies using data-dependent choices.

## References
1. X. Song, *A Frame-Spread Lower Bound for Quantum Entropy Estimation under Fixed Rank-One Measurements*, arXiv:2610.00270v1, first public 2026-08-25.
2. J. Rehacek, Z. Hradil, Y. S. Teo, L. L. Sanchez-Soto, H. K. Ng, J. H. Chai, and B.-G. Englert, *Least-bias state estimation with incomplete unbiased measurements*, arXiv:1509.07614v1.
3. A. Klappenecker and M. Roetteler, *Mutually Unbiased Bases are Complex Projective 2-Designs*, arXiv:quant-ph/0502031.
4. Y. Wang and W. Cui, *Classical Shadow Tomography with Mutually Unbiased Bases*, arXiv:2310.09644.
