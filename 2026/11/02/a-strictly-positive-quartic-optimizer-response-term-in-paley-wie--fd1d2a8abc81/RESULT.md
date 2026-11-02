# A strictly positive quartic optimizer-response term in Paley–Wiener concentration

## Finding

Fix \(s>0\), write \(a=s/2\), and let \(PW\) be the bandlimited Hilbert space with Fourier support \([-1/2,1/2]\), in the \(e^{-2\pi i x\xi}\) convention. Let \(P\) be the orthogonal projection onto \(PW\), \(T_F=P\mathbf1_FP|_{PW}\), and let \(\lambda_0\) and \(\psi\) be the leading eigenvalue and the real, even, positive-at-zero, globally \(L^2\)-normalized leading eigenfunction of \(T_{(-a,a)}\). Put \(u=\psi^2\). The classical first-prolate properties give \(u'(a)<0\) and a positive spectral gap between \(\lambda_0\) and the remainder of the spectrum.

For every \(0<m<a\), define the symmetric equal-measure endpoint-exchange set
\[
E_m=(-a-m,-a)\cup(-a+m,a-m)\cup(a,a+m).
\]
Then \(|E_m|=2a=s\), and the optimal spectral loss and optimized prolate-weighted loss are
\[
\eta(E_m)=\lambda_0-\|T_{E_m}\|,\qquad
\mathcal D(E_m)=\lambda_0-\sup_{t\in\mathbb R}\int_{E_m}|\psi(x-t)|^2\,dx.
\]
There is an exact strictly positive coefficient \(W_s\) such that
\[
\boxed{\mathcal D(E_m)-\eta(E_m)=W_s m^4+O_s(m^6),\qquad W_s>0.}
\]
Specifically, on \(PW\), let \(Q_s\) be the bounded self-adjoint finite-rank operator defined by the sesquilinear form
\[
\langle Q_sf,g\rangle=(f\overline g)'(a)-(f\overline g)'(-a),
\]
where the inner product is linear in the first variable. Let \(\Pi=I-|\psi\rangle\langle\psi|\) and let \(R_s=(\lambda_0-T_{(-a,a)})^{-1}\) on \(\psi^\perp\). Then
\[
\boxed{W_s=\langle R_s\Pi Q_s\psi,\Pi Q_s\psi\rangle>0.}
\]
Equivalently, for any complete real prolate eigenbasis \((\psi_j)_{j\ge0}\) of \(T_{(-a,a)}\), with \(\psi_0=\psi\) and \(\psi_j\) of parity \((-1)^j\),
\[
W_s=4\sum_{k=1}^{\infty}\frac{[\psi'(a)\psi_{2k}(a)+\psi(a)\psi'_{2k}(a)]^2}{\lambda_0-\lambda_{2k}}.
\]
This series converges absolutely and is strictly positive. In particular, using the fixed positive boundary slope, one obtains the nonzero normalized limit
\[
\boxed{\lim_{m\downarrow0}\frac{\mathcal D(E_m)-\eta(E_m)}{\mathcal D(E_m)^2}=
\frac{W_s}{4[u'(a)]^2}>0.}
\]
Thus the quadratic order in the existing spectral-versus-weighted discrepancy bound is attained asymptotically; it cannot be replaced by a uniform little-oh of squared discrepancy.

## Assumptions and scope

Every statement above holds for each fixed real \(s>0\) and the one-dimensional Paley–Wiener band \([-1/2,1/2]\). Open versus closed interval endpoints are immaterial. All Hilbert norms are whole-line \(L^2(\mathbb R)\) norms, not norms restricted to the observation set. The resolvent is the bounded inverse on the orthogonal complement of the simple leading eigenvector. The estimate is a small-\(m\) expansion with \(s\) fixed, not uniform as \(s\) approaches zero or infinity. The operator \(Q_s\) is defined by bounded point and derivative evaluations on \(PW\), so no unbounded differential operator is involved.

## Proof

**1. Norm-analytic endpoint exchange.** For \(f,g\in PW\) put \(H=f\overline g\). The Fourier-band derivative bounds imply that every \(H^{(j)}\) is uniformly bounded by a constant (depending only on \(j\)) times \(\|f\|_2\|g\|_2\). Directly integrating over the two removed and two added boundary pieces gives
\[
\begin{split}
\langle(T_{E_m}-T_I)f,g\rangle
&=\int_a^{a+m}H-\int_{a-m}^aH
+\int_{-a-m}^{-a}H-\int_{-a}^{-a+m}H\\
&=m^2\{H'(a)-H'(-a)\}+
\frac{m^4}{12}\{H'''(a)-H'''(-a)\}+O(m^6)\|f\|_2\|g\|_2,
\end{split}
\]
where \(I=(-a,a)\) and the integrals in the first line have the displayed limits in the obvious Lebesgue sense. The Taylor remainder is uniform for unit vectors and hence is in operator norm. In particular,
\[
T_{E_m}=T_I+m^2Q_s+m^4U_s+O_{\mathrm{op}}(m^6)
\]
with \(\langle U_sf,g\rangle=[H'''(a)-H'''(-a)]/12\). The same derivative estimates yield an operator-norm analytic expansion in \(t=m^2\) around zero.

**2. Isolated-eigenvalue perturbation.** The top eigenvalue \(\lambda_0\) is simple and separated from the other eigenvalues by a positive gap. Standard one-variable analytic perturbation, or the elementary Rayleigh–Schrödinger calculation using the decomposition \(PW=\mathbb C\psi\oplus\psi^\perp\), yields
\[
\lambda(m):=\|T_{E_m}\|
=\lambda_0+m^2\langle Q_s\psi,\psi\rangle
+m^4\big(\langle U_s\psi,\psi\rangle+W_s\big)+O_s(m^6).
\]
Indeed, writing a normalized perturbed eigenvector as \(\psi+m^2h+O(m^4)\) with \(h\perp\psi\), the complementary eigenvalue equation at order \(m^2\) reads \((\lambda_0-T_I)h=\Pi Q_s\psi\), so \(h=R_s\Pi Q_s\psi\). Substitution into the scalar eigenvalue equation gives the asserted positive resolvent term. The spectral gap makes the inverse bounded and justifies the expansion.

**3. The fixed-center weighted loss.** Evenness of \(\psi\) implies \(u'(-a)=-u'(a)\) and \(u'''(-a)=-u'''(a)\). The preceding Taylor formula with \(f=g=\psi\) gives
\[
\lambda_0-\int_{E_m}u
=-2u'(a)m^2-\frac16u'''(a)m^4+O_s(m^6).
\]
The coefficient of \(m^2\) is strictly positive. The spectral eigenvalue and the fixed-center test value thus differ by
\[
\lambda(m)-\int_{E_m}u=W_sm^4+O_s(m^6).
\]

**4. The optimized center is exactly zero for all sufficiently small \(m\).** Set \(\Phi_m(t)=\int_{E_m}u(x-t)\,dx\). It is even, because both \(E_m\) and \(u\) are even. For \(m=0\), \(\Phi_0\) has a unique strict global maximum at zero: the first prolate's boundary-level inequalities imply the interval \((-a,a)\) uniquely maximizes the integral of \(u\) among sets of measure \(2a\), and translating this interval gives strict inequality away from zero. Moreover \(\Phi_0''(0)=2u'(a)<0\). Because \(|E_m\triangle I|=4m\) and \(u,u',u''\) are bounded, \(\Phi_m\), \(\Phi_m'\), and \(\Phi_m''\) converge uniformly to their \(m=0\) counterparts. The functions \(\Phi_0\) and \(\Phi_m\) also vanish at infinity. Consequently all maximizers of \(\Phi_m\) lie in a fixed small neighborhood of zero for small \(m\), on which \(\Phi_m''<0\). Strict concavity and evenness force their unique maximum to be \(t=0\). Thus \(\mathcal D(E_m)=\lambda_0-\int_{E_m}u\) for small \(m\), proving the quartic expansion for the optimized discrepancy.

**5. Strict positivity of the quartic coefficient.** The reduced resolvent \(R_s\) is strictly positive on \(\psi^\perp\); thus \(W_s>0\) precisely when \(\Pi Q_s\psi\ne0\). Let \(k_x(y)=\sin(\pi(y-x))/(\pi(y-x))\) be the reproducing kernel and \(\partial_xk_x\) its parameter derivative. Direct evaluation of the defining form gives
\[
Q_s\psi=\psi'(a)(k_a+k_{-a})+\psi(a)(\partial_xk_x|_{x=a}-\partial_xk_x|_{x=-a}).
\]
Here \(\psi(a)>0\) is a classical ground-state boundary fact. Suppose \(Q_s\psi=c\psi\) for a scalar \(c\). On the Fourier band, the transform of the left side is the transform of a compactly supported distribution consisting of nonzero first derivatives of Dirac masses at \(\pm a\), plus point masses. The identity \(T_I\psi=\lambda_0\psi\) makes the Fourier transform of the right side equal to the transform of the absolutely continuous compactly supported distribution \((c/\lambda_0)\psi(x)\mathbf1_I(x)\,dx\). Both transforms are entire functions of the complex frequency, hence equality on \([-1/2,1/2]\) implies equality everywhere by analytic continuation. Injectivity of the Fourier transform of compactly supported distributions would then identify nonzero boundary Dirac derivatives with an absolutely continuous measure, impossible. Therefore \(\Pi Q_s\psi\ne0\) and \(W_s>0\).

**6. The convergent spectral coefficient and sharpness.** Compactness and injectivity of \(T_I\) give the complete prolate eigenbasis with \(0<\lambda_j<\lambda_0\) for \(j\ge1\). Taking inner products with \(\psi_j\), odd parity makes the coefficient zero for odd \(j\); for even \(j\) it equals \(2(\psi'(a)\psi_j(a)+\psi(a)\psi_j'(a))\). The spectral theorem yields the displayed convergent series. Finally, \(\mathcal D(E_m)=-2u'(a)m^2+O_s(m^4)\), so division by \(\mathcal D(E_m)^2\) gives the positive normalized limit. All steps concern actual infinite-dimensional operators; finite truncations are not used as proofs.

## Verification

The operator-norm Taylor expansion, spectral-gap perturbation equation, and distribution-based nonvanishing argument furnish a self-contained analytical certificate, conditional only on classical first-prolate eigenfunction properties explicitly identified above. The optional `verify.py` program constructs a quadrature discretization of the Fourier-space concentration operator, computes the reduced-resolvent coefficient, and checks the normalized fourth-order eigenvalue-versus-Rayleigh difference at multiple decreasing exchange widths. Its finite-dimensional tests are supplementary and do not certify the infinite-dimensional theorem.

## Relationship to prior work

Zelent's 2026 stability theorem introduces the optimized prolate-weighted discrepancy and proves the general upper estimate \(0\le\mathcal D(E)-\eta(E)\le C_s\mathcal D(E)^2\); see the discussion around its equation (22) and local Proposition 1. The source does not provide a positive lower-order saturation example or an exact resolvent coefficient for optimizer adaptation. A prior published detachment-crossover study obtains the leading spectral loss proportional to the boundary slope and detachment displacement for a one-sided shifted piece, but does not quantify the order-four difference between the fixed-prolate value and the reoptimized leading eigenvalue. The present claim is precisely that finer difference and proves the quadratic bound's exponent sharp. Spectral perturbation theory and the prolate eigenbasis are used as known tools, not claimed as inventions.

## Limitations

The sharpness construction is a natural symmetric three-component endpoint exchange, not a classification of all small boundary perturbations. The coefficient is given intrinsically by a reduced resolvent (or a convergent prolate series), not a closed elementary expression. The remainder is for fixed bandwidth product \(s\). The assertion concerns the optimized prolate discrepancy only for sufficiently small exchange width, as established in the proof. No global optimality of this coefficient over arbitrary sets is claimed; no independent audit has been performed.

## References

1. D. Zelent, *Stability of concentration in the Paley–Wiener space*, arXiv:2610.01299v1 (first public 2026-10-01), https://arxiv.org/html/2610.01299v1 .
2. L. D. Abreu and M. Speckbacher, *Optimal concentration in the Paley–Wiener space*, arXiv:2607.19192v1 (2026), https://arxiv.org/abs/2607.19192 .
3. *Exact detachment crossover for Paley–Wiener concentration*, published research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-detachment-crossover-for-paley-wiener-concentration--2c548bca48bc .
4. D. Slepian and H. O. Pollak, *Prolate spheroidal wave functions, Fourier analysis and uncertainty—I*, Bell System Technical Journal **40** (1961), 43–63.
