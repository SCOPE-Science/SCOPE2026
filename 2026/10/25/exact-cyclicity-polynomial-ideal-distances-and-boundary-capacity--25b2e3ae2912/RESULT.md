# Exact cyclicity, polynomial-ideal distances and boundary capacity for monomial circles on complex ellipsoids

## Finding

Let \(p>1\), let \(a,b\geq1\) be integers, and put \(d=a+b\). In the complex ellipsoid
\[
\Omega_p=\{(z_1,z_2)\in\mathbb C^2:|z_1|^{2p}+|z_2|^{2p}<1\},
\]
consider the Poletsky–Stessin Dirichlet-type Hilbert space \(D_\beta(\Omega_p)\), \(\beta\in\mathbb R\), with the exact monomial norm in the next section. Define
\[
\lambda=\left(\frac{d^d}{a^ab^b}\right)^{1/(2p)},\qquad
w(z)=\lambda z_1^az_2^b,\qquad f(z)=1-w(z).
\]
The polynomial \(f\) has no zeros in \(\Omega_p\). Its boundary zero set is a disjoint union of \(\gcd(a,b)\) circles. Set
\[
M_n=\lambda^{2n}\frac{\Gamma(1+an/p)\Gamma(1+bn/p)}{\Gamma(2+dn/p)}(dn+2)^\beta,
\qquad S_N=\sum_{n=0}^N M_n^{-1}.
\]
For every nonnegative integer \(L\), put \(N=\lfloor L/d\rfloor\). The **unrestricted** optimal polynomial error is exactly
\[
\boxed{\min_{\deg Q\le L}\|1-fQ\|_{D_\beta(\Omega_p)}^2=S_{N+1}^{-1}.}
\]
The minimum is attained by an explicit polynomial \(Q=P_N(w)\), given below; allowing arbitrary monomials outside the one-generator algebra cannot improve it. In particular,
\[
\boxed{f\text{ is cyclic in }D_\beta(\Omega_p)\quad\Longleftrightarrow\quad \beta\le\frac32.}
\]
For the kernel energy and capacity normalized by this Hilbert space, the exact capacity of the one-dimensional boundary zero set \(Z\) is
\[
\boxed{\operatorname{Cap}_\beta(Z)
=\left(\sum_{n=0}^\infty M_n^{-1}\right)^{-1}
=\operatorname{dist}(1,f\mathbb C[z_1,z_2])^2,}
\]
with the convention \(1/\infty=0\). The normalized Haar measure on \(Z\) minimizes the energy whenever it is finite, and also has the minimum infinite energy in the zero-capacity regime.

Finally, with
\[
\kappa_{p,a,b,\beta}=\sqrt{2\pi p a b}\,d^{\beta-3/2},
\]
the sharp degree laws as \(N=\lfloor L/d\rfloor\to\infty\) are
\[
\min_{\deg Q\le L}\|1-fQ\|^2\sim
\begin{cases}
\kappa_{p,a,b,\beta}(3/2-\beta)N^{\beta-3/2},&\beta<3/2,\\
\kappa_{p,a,b,3/2}/\log N,&\beta=3/2.
\end{cases}
\]
For \(\beta>3/2\), writing \(S_\infty=\sum_{n\ge0}M_n^{-1}<\infty\), the positive limiting error is approached by
\[
\min_{\deg Q\le L}\|1-fQ\|^2
=\frac1{S_\infty}+
\frac{N^{3/2-\beta}}{(\beta-3/2)\kappa_{p,a,b,\beta}S_\infty^2}
+o(N^{3/2-\beta}).
\]

## Assumptions and scope

The defining norm, with no implicit renormalization, is
\[
\left\|\sum_{j,k\ge0}c_{jk}z_1^jz_2^k\right\|^2_\beta
=\sum_{j,k\ge0}|c_{jk}|^2m_{jk},\qquad
m_{jk}=\frac{\Gamma(1+j/p)\Gamma(1+k/p)}{\Gamma(2+(j+k)/p)}(j+k+2)^\beta.
\]
It is the monomial coefficient realization of the complex-ellipsoid spaces given by Torkinejad Ziarati [1, Section 4]. A polynomial is cyclic when its polynomial multiples are dense. In the finite-degree problem \(\deg Q\) is **total degree**. The boundary kernel energy of a Borel probability measure \(\mu\) supported on \(Z\) is
\[
I_\beta(\mu)=\sum_{j,k\ge0}
\frac{\left|\int_Z\zeta_1^j\zeta_2^k\,d\mu(\zeta)\right|^2}{m_{jk}}
\in[0,\infty],
\qquad \operatorname{Cap}_\beta(Z)=\bigl(\inf_\mu I_\beta(\mu)\bigr)^{-1}.
\]
This coefficient-wise definition is the nonnegative Fourier expansion of the kernel-energy convention of [1, Section 3.2]. It avoids assigning a potentially divergent pointwise boundary kernel. The theorem concerns this family of monomial polynomials on **nonball ellipsoids** \(p>1\); it does not classify arbitrary boundary-zero polynomials.

## Proof

**1. Geometry.** Weighted arithmetic–geometric mean gives
\[
|z_1|^{2a}|z_2|^{2b}
\le\left(\frac ad\right)^{a/p}
\left(\frac bd\right)^{b/p}
(|z_1|^{2p}+|z_2|^{2p})^{d/p}.
\]
Consequently \(|w(z)|<1\) in \(\Omega_p\). Equality \(w(\zeta)=1\) on the boundary requires the exact radii
\[
|\zeta_1|=(a/d)^{1/(2p)},\qquad
|\zeta_2|=(b/d)^{1/(2p)}
\]
and the phase constraint \(\zeta_1^a\zeta_2^b=\lambda^{-1}\). This is the compact subgroup orbit
\[
Z=\{(r_1\eta_1,r_2\eta_2):\eta\in H\},\qquad
H=\{(\eta_1,\eta_2)\in\mathbb T^2:\eta_1^a\eta_2^b=1\}.
\]
Its \(\gcd(a,b)\) connected components are circles because the phase homomorphism has that many components.

**2. Exact reduction to one variable.** Coordinatewise rotation by \(H\) acts unitarily on \(D_\beta(\Omega_p)\): the monomials are orthogonal and their norms depend only on exponents. Since both \(1\) and \(f=1-w\) are \(H\)-invariant, averaging \(Q\) over normalized Haar measure on \(H\) cannot increase \(\|1-fQ\|\) and does not raise polynomial total degree. A character \(\eta_1^j\eta_2^k\) is trivial on \(H\) precisely if \((j,k)\) is an integer multiple of \((a,b)\) (the annihilator of the kernel of the torus character \((a,b)\)). For \(j,k\ge0\), only nonnegative multiples occur. Thus every invariant polynomial of total degree at most \(L\) is \(P(w)\), \(\deg P\le N=\lfloor L/d\rfloor\). This argument remains valid when \(a,b\) are not coprime, because the **full** disconnected group \(H\) is averaged.

Write \(e(w)=1-(1-w)P(w)=\sum_{n=0}^{N+1}e_nw^n\). Since \(e(1)=1\), \(\sum_{n=0}^{N+1}e_n=1\). Conversely, any such coefficients yield a unique \(P\) of degree at most \(N\). Orthogonality gives \(\|e(w)\|^2=\sum_{n=0}^{N+1}M_n|e_n|^2\). The weighted Cauchy–Schwarz inequality yields
\[
1=\left|\sum_{n=0}^{N+1}e_n\right|^2
\le\left(\sum_{n=0}^{N+1}M_n|e_n|^2\right)
\left(\sum_{n=0}^{N+1}\frac1{M_n}\right).
\]
Equality holds uniquely at
\[
e_n=\frac{M_n^{-1}}{S_{N+1}},\qquad
P_N(w)=\sum_{j=0}^N
\frac{\sum_{n=j+1}^{N+1}M_n^{-1}}{S_{N+1}}\,w^j.
\]
The formula proves the **global**, not restricted-class, minimization theorem.

**3. Asymptotic and cyclicity.** Stirling's formula applied separately to the three Gamma factors gives, for every fixed admissible parameter tuple,
\[
M_n=\sqrt{2\pi p a b}\,d^{\beta-3/2}
 n^{\beta-1/2}(1+O(n^{-1})).
\]
The exponential factors cancel *exactly* against \(\lambda^{2n}\). Consequently \(S_\infty=\infty\) if and only if \(\beta\le3/2\). Integral comparison (or standard partial-sum asymptotics for a regularly varying sequence) proves the stated three degree laws; when \(\beta>3/2\), use
\[
S_\infty-S_{N+1}=\frac{N^{3/2-\beta}}{(\beta-3/2)\kappa_{p,a,b,\beta}}
+o(N^{3/2-\beta})
\]
and expand \(1/S_{N+1}\) about \(S_\infty\).

Every coordinate multiplier is bounded: for example, the ratio \(m_{j+1,k}/m_{jk}\) equals a bounded power-weight ratio times two Gamma quotients, whose respective growth is bounded by constants times \((j+1)^{1/p}\) and \((j+k+1)^{-1/p}\). This ratio is uniformly bounded in \(j,k\ge0\), and similarly for the other coordinate. Polynomials are dense by definition of the coefficient norm. Hence convergence of polynomial multiples to \(1\) is equivalent to cyclicity: any polynomial can be approximated by multiplying the convergent approximants with that polynomial. The exact distance formula therefore proves the asserted threshold.

**4. Exact capacity.** For every probability measure \(\mu\) on \(Z\), the identity \(w(\zeta)=1\) forces
\[
\int_Z\zeta_1^{an}\zeta_2^{bn}\,d\mu=\lambda^{-n}
\quad(n\ge0).
\]
Inserting only these terms into the nonnegative energy series gives \(I_\beta(\mu)\ge\sum_{n\ge0}M_n^{-1}=S_\infty\). The normalized Haar probability measure on the full \(H\)-orbit \(Z\) has moments zero at every exponent pair \((j,k)\) outside \(\mathbb Z(a,b)\), by character orthogonality. Its nonzero moments are precisely \(\lambda^{-n}\) at \((an,bn)\). It therefore has energy exactly \(S_\infty\), including when the series diverges. Thus \(\operatorname{Cap}_\beta(Z)=1/S_\infty\), which equals the limiting squared distance obtained in Step 2.

## Verification

A standalone `CHECK.py` independently evaluates the source monomial norm and \(M_n\) in logarithmic Gamma arithmetic, checks the Stirling coefficient for nonintegral and integral ellipsoid exponents, verifies the finite-degree minimizer's coefficient constraint and its predicted squared norm, and checks the exact boundary normalization. The checker is diagnostic, not a replacement for the infinite-dimensional Haar-averaging, Stirling, or capacity arguments. The latter are proved above for all parameters, not extrapolated from finite computation.

## Relationship to prior work

Torkinejad Ziarati [1] defines these ellipsoid coefficient spaces, proves cyclicity criteria when the boundary zero set is finite (Theorem 34), and explicitly poses the **real-one-dimensional boundary zero-set case** as Open Problem 2. The exact monomial coefficient formula and capacity definition are inputs from [1], not new claims. The result here addresses one naturally motivated, fully parameterized family of real-one-dimensional boundary-zero sets rather than claiming a general answer to that open problem.

Kosiński and Vavitsas [2] classify cyclic polynomial behavior on the **unit ball** \(\Omega_1\), including the threshold \(3/2\) for one-dimensional boundary zero sets. Vavitsas [3] proves ball model-polynomial results using diagonal reductions and studies capacities. The agreement of the numerical threshold, the underlying cyclicity/duality ideas, and the reduction philosophy are therefore explicitly recognized as prior. The present theorem's nonball \(p>1\) exact **all-polynomial total-degree** error, \(p,a,b,\beta\)-dependent leading constants, and exact Poletsky–Stessin kernel capacity are not implications of the unit-ball statements without additional coefficient and group analysis. In particular the matching ball threshold **is not itself claimed as new**.

Published mathematical-index comparisons included the nearby radial-Dirichlet-polydisk result [4], which derives one-generator approximation thresholds for a linear average on a **different domain with different monomial norms**. Its summary does not cover these complex-ellipsoid monomial-circle capacities or the unrestricted total-degree optimum. Comparison was made at the level of the objects and conclusions, not merely the titles. This priority assessment is limited to the inspected accessible literature and indexed summaries.

## Limitations

This is a classification of the explicitly stated monomial-circle family, not all stable polynomials with one-dimensional boundary zeros. The coincidence of the cyclicity exponent with that already known on the unit ball should not be mistaken for discovery of a new universal threshold. The capacity is for the exact normalized coefficient kernel specified here; rescaling that kernel rescales capacity and distances. Uniformity is not asserted when \(p,a,b,\beta\) vary with degree. The character argument uses the full, possibly disconnected, subgroup \(H\); averaging only its identity component would not suffice for noncoprime \(a,b\). Earlier unindexed ellipsoid-model calculations or extensions of unit-ball methods could have overlapping conclusions; no exhaustive historical-priority assertion is made.

## References

[1] P. Torkinejad Ziarati, *Cyclicity in Poletsky-Stessin Weighted Bergman Spaces*, arXiv:2507.03767 (first public 4 July 2025), version 2 (24 September 2026), especially Sections 3.2, 4 and 6.

[2] Ł. Kosiński and D. Vavitsas, *Cyclic Polynomials in Dirichlet-Type Spaces in the Unit Ball of \(\mathbb C^2\)*, Constructive Approximation **58** (2023), 343–361, doi:10.1007/s00365-022-09610-4.

[3] D. Vavitsas, *A Note on Cyclic Vectors in Dirichlet-Type Spaces in the Unit Ball of \(\mathbb C^n\)*, Canadian Mathematical Bulletin **66** (2023), 886–902, doi:10.4153/S0008439523000085.

[4] *Exact one-generator approximation threshold in radial Dirichlet polydisk spaces*, publicly indexed mathematical research record, October 2026.
