# Antithetic stage pairing restores pathwise A-stability to randomized implicit Runge–Kutta updates

## Finding
For the randomized implicit two-stage Runge–Kutta schemes of Bochacik, Przybyłowicz and Stępień, the scalar test equation \(y'=\lambda y\), with \(z=h\lambda\), has one-step multiplier
\[
R(z,t)=1+\frac{z}{1-tz}=\frac{1+(1-t)z}{1-tz},\qquad 0\le t\le1.
\]
The original scheme independently samples \(t\) uniformly on \([0,1]\). Replace two consecutive independent stage fractions by \(T\) and \(1-T\), with independent blocks and \(T\sim\mathrm{Uniform}[0,1]\). Every individual stage retains exactly the original uniform marginal and the number of evaluations/implicit solves is unchanged.

**Paired-stage theorem.** For every \(z\in\mathbb C\) with \(\operatorname{Re}z<0\), and every \(t\in[0,1]\), the paired multiplier satisfies
\[
G(z,t)=R(z,t)R(z,1-t)
=\frac{1+z+t(1-t)z^2}{1-z+t(1-t)z^2},\qquad |G(z,t)|<1.
\]
For every purely imaginary \(z\), \(|G(z,t)|=1\). For each fixed \(\operatorname{Re}z<0\), there is a \(q_z<1\) such that \(|y_{2k}|\le q_z^k|y_0|\) for **every** choice of block fractions \(T_1,T_2,\ldots\in[0,1]\). Thus the paired scheme is pathwise A-stable at even steps and in particular mean-square A-stable, whereas the independent-uniform scheme is not.

**Sharp coupling characterization.** Let \((U,V)\) be any \([0,1]^2\)-valued random pair with \(\mathbb E U=\mathbb E V=1/2\), not necessarily independent or uniform. The condition that \(|R(z,U)R(z,V)|\le1\) for every \(\operatorname{Re}z\le0\), for almost every realization, holds **if and only if** \(U+V=1\) almost surely. In particular, with prescribed uniform stage marginals, the antithetic law is the unique coupling with this samplewise A-stability property.

For comparison, when independent stages have a common nondegenerate law on \([0,1]\) with mean \(1/2\), their one-step squared amplification satisfies \(\mathbb E|R(iy,T)|^2>1\) for every real \(y\ne0\). With the original uniform law it is exactly
\[
\mathbb E|R(iy,T)|^2=1+|y|\arctan|y|-\log(1+y^2)>1.
\]
Consequently independent sampling amplifies every nonzero imaginary mode in mean square, while complementary pairing preserves its magnitude at each completed pair.

## Assumptions and scope
The equation is the constant-coefficient scalar complex Dahlquist test equation, with fixed positive step \(h\), and the same complex \(\lambda\) for both updates. Each step uses exactly the original semi-implicit (S1) or implicit (S2) randomized RK2 formula on this linear test equation. The stage values are in \([0,1]\); antithetic consecutive pairs have fractions \((T_k,1-T_k)\), and uniformity is required only when preserving the source's stage marginal law. The exact-arithmetic assertions apply for all \(t,z\) in the domains stated. The uniqueness statement concerns couplings with half-valued stage expectations and **samplewise whole-half-plane** contraction at two-step endpoints; it does not assert uniqueness among couplings giving mean-square stability only.

## Proof
**1. Transfer function.** Substitution of \(f(y)=\lambda y\) in either source update gives \(y_{j+1}=R(z,t_j)y_j\), since the implicit intermediate stage is divided by \(1-t_jz\). On \(\operatorname{Re}z\le0\) the denominator is never zero for \(t_j\in[0,1]\).

**2. Antithetic factorization and exact contraction.** Write \(c=t(1-t)\in[0,1/4]\), \(N=1+z+cz^2\), and \(D=1-z+cz^2\). Multiplication gives \(G=N/D\). Direct complex multiplication yields the identity
\[
|D|^2-|N|^2=-4\operatorname{Re}(z)(1+c|z|^2).
\]
For \(\operatorname{Re}z<0\) this is strictly positive; on the imaginary axis it vanishes. Also \(D=(1-tz)(1-(1-t)z)\ne0\) throughout the closed left half-plane. For fixed \(\operatorname{Re}z<0\), continuity over compact \(t\in[0,1]\) gives \(q_z=\max_{t\in[0,1]}|G(z,t)|<1\). Multiplying successive pair factors proves the claimed bound without any stochastic independence assumptions. In particular every finite \(p\)-moment of the completed-pair solution decays geometrically for fixed \(z\) and finite deterministic initial state.

**3. Uniqueness under fixed stage means.** For any fixed \(u,v\in[0,1]\), direct substitution at \(z=iy\) gives
\[
|R(iy,u)R(iy,v)|^2
=1+2(1-u-v)y^2+O(y^4)\quad(y\to0).
\]
If this product were at most one for every imaginary \(iy\), then necessarily \(u+v\ge1\). The same necessary inequality follows if contraction is only asserted for all \(\operatorname{Re}z<0\), by continuity to the imaginary axis. If the property holds almost surely, \(U+V\ge1\) almost surely, and the mean condition \(\mathbb E(U+V)=1\) forces \(U+V=1\) almost surely. Conversely, \(V=1-U\) is sufficient by Step 2. This is an equivalence, including atoms at zero or one.

**4. Independent-stage obstruction.** For real \(y\ne0\),
\[
\mathbb E|R(iy,T)|^2
=1+y^2\,\mathbb E\!\left[\frac{1-2T}{1+y^2T^2}\right].
\]
Set \(g(t)=1-2t\) and \(f(t)=(1+y^2t^2)^{-1}\). Both are strictly decreasing on \([0,1]\). Since \(\mathbb E g(T)=0\),
\[
\mathbb E[g(T)f(T)]=\operatorname{Cov}(g(T),f(T))
=\frac12\mathbb E[(g(T)-g(T'))(f(T)-f(T'))]>0
\]
for a nondegenerate \(T\), where \(T'\) is an independent copy. For \(T\) uniform, elementary integration gives the displayed arctangent-logarithm identity. With iid fractions, expected squared magnitudes after \(2k\) stages equal \((\mathbb E|R(iy,T)|^2)^{2k}|y_0|^2\), which grows for every \(y\ne0\). Antithetic pairing instead gives exactly \(|y_{2k}|=|y_0|\) for imaginary \(z\).

**5. Concrete stiff-mode separation.** For \(z=-5\) and iid uniform fractions,
\[
\mathbb E|R(-5,T)|^2=1+\frac{25}{6}-2\log 6>1.
\]
For complementary pairing, \(c\in[0,1/4]\) and
\[
|G(-5,t)|=\left|\frac{-4+25c}{6+25c}\right|\le\frac23.
\]
The left side is maximal at \(c=0\). Thus the iid scheme grows in mean square while every realized antithetic block contracts by at least a factor \(2/3\) at that same test parameter.

## Verification
The standalone `verify.py` symbolically checks the factorization, imaginary-axis products, the small-imaginary coefficient used for uniqueness, and the exact left-half-plane modulus identity. It also checks 2,652 complex/stage combinations and the stiff-mode witness with independent-uniform mean-square growth. Run `python verify.py` with Python and SymPy; the packaged execution printed `VERIFY_OK symbolic identities, antithetic imaginary conservation, 2652 left-half-plane pairs, iid divergence at z=-5`. These finite checks are supplementary; all quantified statements above are proven algebraically.

## Relationship to prior work
Bochacik, Przybyłowicz and Stępień introduce the two randomized implicit schemes with independent uniform stage fractions and establish the failure of their mean-square A-stability. Their schemes have the same linear multiplier as used here. The result here changes **only the across-step stage coupling**, recovering pathwise full left-half-plane contraction at completed pairs while keeping both original per-step stage marginals. It also proves a converse within all centered two-stage couplings, not just an example.

General adjoint composition techniques and classical theta-method stability provide relevant deterministic context. The factor \(R(z,t)R(z,1-t)\) is the stability function of a theta-step paired with its adjoint; adjoint composition itself is known and is not claimed as a new construction. The specific probabilistic fixed-marginal repair and necessary-and-sufficient coupling characterization are the assessed findings. The source's publicly available preprint and accessible related sources were compared, but a specialized earlier equivalent may exist.

## Limitations
The result establishes scalar linear Dahlquist A-stability at **even** step endpoints, with a normal-matrix spectral consequence. Individual intermediate steps may amplify; no general nonlinear, nonautonomous, nonnormal, positivity, contractivity, or high-order global-error theorem is asserted. The second stage of an antithetic pair is not independent of the first, so independence-dependent error proofs from the source paper cannot simply be transferred. The paired multiplier tends to unit modulus along extreme imaginary or stiff directions; the claim is A-stability, not L-stability. Independent scientific validation and historical-priority verification have not been performed.

## References
1. T. Bochacik, P. Przybyłowicz and Ł. Stępień, *Convergence and stability of randomized implicit two-stage Runge–Kutta schemes*, BIT Numer. Math. 65, article 7 (2025). DOI: 10.1007/s10543-024-01050-9. Earliest public preprint: arXiv:2404.19059v1, 2024-04-29. https://arxiv.org/abs/2404.19059
2. S. Blanes, F. Casas and A. Murua, *Composition Methods for Differential Equations with Processing*, SIAM J. Sci. Comput. DOI: 10.1137/030601223. https://doi.org/10.1137/030601223
3. G. J. Barclay, D. F. Griffiths and D. J. Higham, *Theta method dynamics*, available at https://webhomes.maths.ed.ac.uk/~dhigham/Publications/P39.pdf
4. D. J. Higham, *Mean-square and asymptotic stability of the stochastic theta method*, SIAM J. Numer. Anal. 38 (2000), 753–769. DOI: 10.1137/S003614299834736X. [This reference concerns stochastic differential equations, a different stability model.]
