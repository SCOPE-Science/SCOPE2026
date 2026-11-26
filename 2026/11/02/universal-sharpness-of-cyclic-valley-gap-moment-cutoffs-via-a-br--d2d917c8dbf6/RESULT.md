# Universal covariance cutoff sharpness for cyclic valley gaps via a Brownian-bridge trace

## Finding
In a uniform cyclic permutation, let \(D_{i,K}\) count successive valleys separated by clockwise distance \(i+1\). For all positive integers \(i,j\), at \(K_0=i+j+6\) the covariance per site exceeds the exact slope \(c_{ij}\) valid for \(K\ge i+j+7\). Specifically, with integral kernels on \([0,1]^2\)
\[
A_i(s,t)=\frac{(s+t)^i-|s-t|^i}{2i!},\qquad M(s,t)=\min(s,t),\qquad B(s,t)=M(s,t)-st,
\]
the discrepancy is
\[
K_0^{-1}\operatorname{Cov}(D_{i,K_0},D_{j,K_0})-c_{ij}=\operatorname{tr}(A_iBA_jB)>0.
\]
This proves optimality of the mixed covariance cutoff \(i+j+7\) and of the variance cutoff \(2i+7\) for every index. As a companion calculation, the known mean-cutoff defect admits the explicit evaluation \(\mathbb E D_{i,i+3}=(i+4)a_i\), where \(a_i=i2^{i+1}/[i!(i+1)(i+2)(i+4)]\). Universal *mean sharpness* is credited to Matijasevick, arXiv:2610.21094v2, Remark 3.2.

## Assumptions and scope
Take \(K\ge3\) i.i.d. continuous priorities (equivalently independent uniform priorities on \([0,1]\) as far as ranks are concerned) on cyclic sites. A valley has strictly smaller priority than its immediate neighbors. Count gaps between distinct successive valleys in the clockwise direction, including those crossing the origin, and use zero if only one valley exists. The operator convention is \((Af)(s)=\int_0^1 A(s,t)f(t)dt\), with real inner product below. Set \(u(s)=s\), \(a_i=\langle u,A_i u\rangle\), \(\nu_{ij}=\langle u,A_iA_j u\rangle\), and \(v_{ij}=\langle u,A_i M A_j u\rangle\). The established slope is
\[
c_{ij}=\mathbf1_{i=j}a_i+2\nu_{ij}+2v_{ij}-(i+j+7)a_i a_j .
\]

## Proof
Condition on the two endpoint priorities \(1-s,1-t\). Successive valleys imply a single increasing-then-decreasing excursion between them, with the peak at an interior site. If the peak is at priority \(1-v\) and there are \(k\) interior sites to its left, the probability for the two monotone sides, conditional on that peak value, is \((s-v)^k(t-v)^{i-1-k}/[k!(i-1-k)!]\) for \(0<v<\min(s,t)\). Summing over the peak position and integrating gives \(A_i\). The outside neighbors give a factor \(st\) if distinct or \(M(s,t)\) if shared. At \(K=i+3\) they are shared, so the per-site mean defect is \(\iint A_i B\). On the triangle \(s<t\), put \(s=tz\), use \(B=s(1-t)\), then double by symmetry:
\[
\iint A_iB=\frac{\int_0^1 z[(1+z)^i-(1-z)^i]dz}{i!(i+3)(i+4)}=\frac{a_i}{i+3}.
\]
The middle integral equals \(i2^{i+1}/[(i+1)(i+2)]\); the same triangular substitution with \(st\) in place of \(B\) gives the stated \(a_i\). Multiplying by \(i+3\) gives the displayed mean value.

Write \(g=i+1,h=j+1\). Fix the first gap at start zero. A second gap can coincide only if \(i=j\), giving weight \(a_i\); share an endpoint by starting at \(g\) or \(-h\), each giving \(\nu_{ij}\); or use distinct endpoints on the complementary arc. In the last case the two separating arcs have lengths at least two because neighboring valleys cannot be adjacent. At \(K_0=g+h+4\), the lengths must therefore both be two, at the single offset \(g+2\equiv-h-2\). No other overlap is possible because a start or end strictly inside the other gap would be an intervening valley. In the last configuration the gaps occur cyclically as \(g,2,h,2\), and each length-two excursion has kernel \(A_1=M\). Integrating the four endpoints gives \(q_{ij}=\operatorname{tr}(A_i M A_j M)\). For a shared endpoint, the two unconstrained outside neighbors are distinct and the integral is \(\nu_{ij}\), with symmetry giving the same weight in reverse order.

For comparison at \(K\ge g+h+5\), the offsets of possible dependence form \([-h-2,g+2]\) modulo \(K\), with no identifications. The same coincident and consecutive cases contribute as above; the two endpoint offsets give \(v_{ij}\) each, because on one side a single outside site is shared and on the other side the outside sites are distinct. All other offsets in that interval are incompatible; offsets outside it have disjoint indicator windows and contribute zero covariance. Subtracting \((g+h+5)a_i a_j\) thus recovers the established slope formula.

At \(K_0\) the individual gap means per site are still \(a_i,a_j\). Translation invariance and the offset list give
\[
K_0^{-1}\operatorname{Cov}(D_{i,K_0},D_{j,K_0})=\mathbf1_{i=j}a_i+2\nu_{ij}+q_{ij}-K_0a_i a_j.
\]
Since \(B=M-u\otimes u\), expanding the trace and using symmetry and cyclicity gives \(q_{ij}-2v_{ij}+a_i a_j=\operatorname{tr}(A_iBA_jB)\). The kernels are bounded Hilbert–Schmidt, so the trace identity applies. Each kernel \(A_i\) and \(B\) is strictly positive on the interior, so the integrand \((A_iB)(s,t)(A_jB)(t,s)\) in the trace pairing is strictly positive there. This proves the all-index strict correction without assuming positive semidefiniteness of the excursion operators.

## Verification and limits
The accompanying `verify.py` enumerates permutations at selected sizes through ten, checks exact rational moment discrepancies, and optionally compares 200-node quadratures using NumPy. `verification_output.txt` records 26 finite checks. In particular the covariance discrepancies for \((1,1),(1,2),(1,3),(2,2)\) are \(29/28350,2/2835,47/155925,1/2025\). The all-index conclusion uses the proof, not these diagnostics. This result concerns only the first subthreshold size for each moment; it does not treat all smaller sizes, nonuniform ranks, or new limit laws.

## Relationship to prior work
Mateo Matijasevick, *Gaps between roots in ballistic deposition on a strip: linear variance, Gaussian limits and a Poisson regime*, [arXiv:2610.21094v2](https://arxiv.org/abs/2610.21094v2) (30 October 2026), Proposition 3.1 gives linearity and Remark 3.2 proves strict mean failure for all indices by the shared-neighbor integral; the explicit mean evaluation above follows by integrating that identity. The remark checks covariance sharpness in finite ranges but does not provide the all-pair covariance defect or its positivity proof. The [first version](https://arxiv.org/abs/2610.21094v1) reported finite mean checks. The earlier model and finite-gap results appear in Mansour, Rastegar and Roitershtein, [arXiv:1903.12548v2](https://arxiv.org/abs/1903.12548v2). The new claim advanced here is the universal covariance correction and its strictness, including the diagonal. Historical priority beyond the compared sources is not asserted.
