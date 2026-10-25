# Two-quadrature recovery and exact arithmetic blind spaces for separated Hermite ladders

## Finding

Let \(d\ge2\), let \(r\) be a positive integer with
\[
r>2\left\lfloor\frac{d-1}{2}\right\rfloor,
\]
and consider the \(d\)-dimensional Hermite/Fock subspace
\[
\mathcal H_{d,r}=\operatorname{span}\{h_0,h_r,\ldots,h_{(d-1)r}\}\subset L^2(\mathbb R).
\]
For real phases \(\theta_0,\theta_1\), let \(\mathcal M\) map a Hermitian \(d\)-by-\(d\) matrix to its two entire quadrature probability-density functions, restricted to \(\mathcal H_{d,r}\). Set \(\Delta=\theta_1-\theta_0\). Then its **exact real kernel dimension** is
\[
\boxed{\dim_{\mathbb R}\ker\mathcal M
=\sum_{k=1}^{d-1}(d-k)\,\mathbf1_{\{rk\Delta\in\pi\mathbb Z\}}.}
\]
Every element of the kernel is traceless, so the same nullity holds for reconstruction of trace-one density matrices. In particular, two phases are informationally complete **if and only if** \(\sin(rk\Delta)\ne0\) for every integer \(1\le k<d\); any one phase is never complete for \(d\ge2\). Thus two is the **sharp minimum number of continuously resolved phases** for this family, at all dimensions.

If \(\Delta/\pi\) is irrational, the nullity is zero. If \(\Delta/\pi=a/b\) is in lowest terms, with \(b\ge1\), set \(B=b/\gcd(b,r)\) and \(m=\lfloor(d-1)/B\rfloor\). Then the nullity simplifies to
\[
\boxed{md-\frac{Bm(m+1)}2.}
\]
These formulas include coincident phases, phases separated by \(\pi\), and every rational resonance. They concern exact continuous-distribution data, not statistical stability or noisy finite-sample accuracy.

## Assumptions and scope

The physicists' Hermite polynomials are fixed by \(e^{2xt-t^2}=\sum_{n\ge0}H_n(x)t^n/n!\). Let \(h_n(x)=(2^n n!\sqrt\pi)^{-1/2}H_n(x)e^{-x^2/2}\). The quadrature distribution at phase \(\theta\) is the diagonal of the density matrix in the rotated oscillator basis, with rotation \(h_n\mapsto e^{-in\theta}h_n\). The unknown is an arbitrary trace-one positive semidefinite operator supported on \(\mathcal H_{d,r}\). Equivalently, for linear injectivity one considers all Hermitian matrices (or its traceless real subspace). All angle statements concern phases modulo \(\pi\), because a \(\pi\)-rotation reverses the quadrature variable without providing a new independent view.

The spacing condition is a transparent sufficient condition for independence of all unordered Hermite products. **It is not claimed necessary**, and the theorem does not optimize the maximum occupied photon number. For even \(d\), the sufficient inequality allows \(r=d-1\); for odd \(d\), it allows \(r=d\). The claim includes all \(d\ge2\) and all phases satisfying the stated hypotheses.

## Proof

**Step 1: Hermite-product independence.** The elementary Hermite linearization identity is
\[
H_m(x)H_n(x)=\sum_{k=0}^{\min(m,n)}
2^k k!\binom{m}{k}\binom{n}{k}H_{m+n-2k}(x).
\]
We prove the family \(\{H_{ri}(x)H_{rj}(x):0\le i\le j<d\}\) is linearly independent over \(\mathbb R\). Assume a nonzero linear relation and choose the *largest* index sum \(s=i+j\) for which some coefficient is nonzero. The allowed \(i\) at this sum range from \(\max(0,s-d+1)\) to \(\lfloor s/2\rfloor\), giving \(t_s\) distinct unordered pairs. One has \(t_s\le\lfloor(d-1)/2\rfloor+1\).

For \(0\le k<t_s\), the Hermite coefficient in degree \(rs-2k\) of the product with pair \((i,s-i)\) is
\[
 c_k(i)=\frac{2^k}{k!}\prod_{j=0}^{k-1}
\left(r^2i(s-i)-jrs+j^2\right).
\]
This is a polynomial of **exact degree \(k\)** in \(u_i=i(s-i)\), with nonzero leading coefficient. The numbers \(u_i\) are pairwise distinct because \(i\mapsto i(s-i)\) strictly increases on \(0\le i\le s/2\). Hence the square matrix \((c_k(i))_{0\le k<t_s,\ i\text{ allowed}}\) is an invertible triangular change of basis times a Vandermonde matrix.

Moreover, \(rs-2(t_s-1)>r(s-1)\), by the spacing assumption. Consequently, none of these \(t_s\) high-degree Hermite coefficients can be contributed by any product from a smaller index sum. In the assumed zero relation they all vanish, so the Vandermonde matrix forces every coefficient at sum \(s\) to be zero, a contradiction. This proves linear independence for **every** admissible \(d,r\), including the boundary spacing.

**Step 2: Extract individual matrix entries from each quadrature.** Let \(\rho=(\rho_{ij})\) be Hermitian. Up to positive known normalization factors \(c_i=(2^{ri}(ri)!\sqrt\pi)^{-1/2}\), its quadrature density is
\[
p_\theta(x)=e^{-x^2}\biggl(\sum_{i=0}^{d-1} c_i^2\rho_{ii}H_{ri}(x)^2
+2\sum_{0\le i<j<d}c_ic_j\operatorname{Re}\bigl(e^{ir(j-i)\theta}\rho_{ij}\bigr)H_{ri}(x)H_{rj}(x)\biggr).
\]
The sign choice of the rotation convention is immaterial to the ranks. By Step 1 the coefficients of **every unordered product** in this polynomial can be extracted uniquely from the *entire* function \(p_\theta\). Thus one phase identifies each diagonal \(\rho_{ii}\), and one real linear combination of the real and imaginary parts of every off-diagonal \(\rho_{ij}\).

**Step 3: Exact two-view nullity.** For fixed \(i<j\), the two extracted off-diagonal combinations at phases \(\theta_0,\theta_1\) have a \(2\)-by-\(2\) real coefficient matrix with determinant equal, up to sign and a strictly nonzero normalization, to \(\sin(r(j-i)\Delta)\). If that sine is nonzero, both components of \(\rho_{ij}\) are determined; if it vanishes, one real degree of freedom remains. The diagonal entries always are determined. There are exactly \(d-k\) pairs with \(j-i=k\). Summing their independent defects gives the first boxed nullity formula. It also shows one-phase nullity \(d(d-1)/2\), which proves the two-view minimum.

Every invisible Hermitian matrix has zero diagonal by Step 2, hence zero trace. For any nonzero such matrix \(K\), both matrices \(I/d+\varepsilon K\) and \(I/d-\varepsilon K\) are distinct positive-definite trace-one states for sufficiently small \(\varepsilon>0\), and their two quadrature distributions coincide. Thus the nullity is a genuine physical density-matrix ambiguity, not merely an algebraic artifact.

**Step 4: Rational phase arithmetic.** If \(\Delta/\pi=a/b\) is reduced, the resonance \(rk\Delta\in\pi\mathbb Z\) is equivalent to \(b\mid rk\), hence to \(B\mid k\), where \(B=b/\gcd(b,r)\). Summing \(d-Bj\) over \(1\le j\le m\) gives \(md-Bm(m+1)/2\). If \(\Delta/\pi\) is irrational, none of the finitely many positive integer multiples \(rk\) yields an integer, so there are no resonances. All four steps are exact and require no generic-position assumption.

## Verification

The accompanying `checker.py` reconstructs all unnormalized Hermite-product coefficient vectors with exact integer arithmetic, and independently constructs the two-angle real-linear measurement matrices in the Hermitian basis. Over the prime field of characteristic \(1000000007\), all seven tested parameter pairs (dimensions \(2\) through \(7\) at the sufficient gap boundary, plus \((d,r)=(4,4)\)) have the predicted full unordered-product rank. All fourteen resonant two-angle ranks at separations \(\pi/r\) and \(\pi/(2r)\) agree with the exact nullity formula. A separate exact algebraic check obtains full real rank \(16\) for \((d,r)=(4,4)\) with nonresonant phase separation \(\pi/16\). The program reports its results in `checker_output.txt`; run with `python checker.py` after installing `requirements.txt`. Modular rank checks are finite tests and do not prove the all-dimension theorem; the Vandermonde argument above does.

## Relationship to prior work

Leonhardt and Munroe (1996) investigate the number of homodyne phases for a **consecutive, fully populated** finite Fock band. Sych et al. (2012, original public preprint 21 November 2012) obtain the general band rank \(m(2d-m)\) for \(m\) quadratures and discuss a distinct **fixed four-step occupancy restriction**. The present statement instead treats an infinite family of growing-gap arithmetic Fock ladders and gives the exact rank defect for **each prescribed pair of phases**. Neither the consecutive-band count nor a fixed four-step model implies the stated Vandermonde independence over every admissible gap and the explicit denominator-dependent blind-space formula. Banaszek (1999) develops likelihood-based Wigner reconstruction with prior constraints rather than these phase-dependent operator-span ranks. The foundational quadrature model and polynomial linearization are classical; novelty, to the extent supported by the inspected sources, is the combined independence criterion, sharp two-angle result, and exact rational-phase defect law.

## Limitations

The spacing threshold is sufficient, not necessary. Exact informational completeness may be severely ill-conditioned when the spacing or dimension is large or a phase separation approaches a resonance; **no error-rate, noise-optimality, or finite-shot guarantee is proved**. The claim concerns only matrices exactly supported on the specified finite Hermite subspace and exact quadrature distributions. It does not imply that two phases reconstruct arbitrary continuously supported states. A potentially relevant 1997 paper of Leonhardt on equidistant reference angles was identifiable by abstract but not fully accessible in this run; an equivalent earlier result cannot be ruled out independently. The proof and the computational checks are not independent external certification.

## References

1. D. Sych, J. Řeháček, Z. Hradil, G. Leuchs, and L. L. Sánchez-Soto, *Informational completeness of continuous-variable measurements*, arXiv:1211.4967v1 (21 November 2012), especially Eq. (4)–(8). https://arxiv.org/html/1211.4967v1
2. U. Leonhardt and M. Munroe, *Number of phases required to determine a quantum state in optical homodyne tomography*, Phys. Rev. A 54, 3682–3684 (1996), DOI:10.1103/PhysRevA.54.3682.
3. K. Banaszek, *Quantum homodyne tomography with a priori constraints*, arXiv:quant-ph/9901064v1 (25 January 1999). https://arxiv.org/abs/quant-ph/9901064
4. U. Leonhardt, *Quantum and classical tomography with equidistant reference angles*, J. Mod. Opt. 44, 2271–2280 (1997), DOI:10.1080/095003497152492 (abstract inspected; full text unavailable).
