# Alternating center curvature of every finite Hermite half-line concentration defect

## Finding

For each integer \(q\geq 1\), take the first \(q\) normalized Hermite functions, and let \(A_q(t)\) be their compression of the half-line indicator \(\mathbf 1_{[t,\infty)}\). Put
\[
V_q(t)=\operatorname{tr}\bigl(A_q(t)(I_q-A_q(t))\bigr),\qquad
c_k=\frac{\binom{2k}{k}}{4^k},\qquad
m=\left\lceil\frac q2\right\rceil.
\]
Then \(V_q\) is a smooth even real function, and its center curvature is exactly
\[
\boxed{\displaystyle V_q''(0)=(-1)^q\frac{2}{\pi}
\sum_{k=0}^{m-1}\frac{\binom{2k}{k}^{2}}{16^{k}}.}
\]
In particular, **the center is a strict local maximum at every odd order and a strict local minimum at every even order**. No finite order has a degenerate centered stationary point. The strength of this alternating curvature grows logarithmically:
\[
\boxed{\displaystyle V_q''(0)=(-1)^q\left(\frac{2}{\pi^2}\log q+O(1)\right)}
\qquad(q\longrightarrow\infty).
\]
These statements concern local stationary behavior and do not assert global extremality for general \(q\).

## Assumptions and scope

The physicists' Hermite polynomial \(H_j\) and normalized Hermite function are
\[
h_j(x)=\frac{H_j(x)e^{-x^2/2}}{\sqrt{2^j j!\sqrt\pi}},
\quad j\in\mathbb N_0,\qquad x\in\mathbb R.
\]
For all \(t\in\mathbb R\), the finite real symmetric concentration matrix is
\[
A_q(t)_{jk}=\int_t^\infty h_j(x)h_k(x)\,dx,
\qquad 0\leq j,k<q.
\]
Because the Hermite functions are orthonormal, \(0\leq A_q(t)\leq I_q\), and the trace defect \(V_q(t)\) is well-defined and nonnegative. This same matrix occurs as the Hermite-fiber symbol of half-plane localization on full polyanalytic Fock space; no scale conversion is needed for the stated Hermite coordinate \(t\). All claims hold for every positive integer \(q\) with no large-order assumption except the final asymptotic formula.

## Proof

**1. Hermite boundary data and Wronskians.** Hermite functions solve
\[
h_j''(x)=(x^2-2j-1)h_j(x).
\]
For \(j<q\), integrating the Wronskian derivative on \([0,\infty)\) gives
\[
\int_0^\infty h_j(x)h_q(x)\,dx
=\frac{h_q'(0)h_j(0)-h_q(0)h_j'(0)}{2(q-j)}.
\tag{1}
\]
Parity and the Hermite recurrence yield
\[
h_{2k+1}(0)=h_{2k}'(0)=0,
\quad h_{2k}(0)^2=\frac{c_k}{\sqrt\pi},
\quad h_{2k+1}'(0)^2=\frac{2(2k+1)c_k}{\sqrt\pi}.
\tag{2}
\]

**2. A finite central-binomial identity.** For \(m\geq1\) write
\[
S_m=\sum_{k=0}^{m-1}c_k,\quad
R_m=\sum_{k=0}^{m-1}\frac{c_k}{2m-2k-1},\quad
H_m=\sum_{k=0}^{m-1}c_k^2.
\]
We claim
\[
S_m=2m c_m,\qquad S_m R_m=H_m.
\tag{3}
\]
The first identity telescopes \(2(k+1)c_{k+1}-2kc_k=c_k\). For the second, the convergent generating function of \(R_m\), for \(|z|<1\), is
\[
\sum_{m\geq1}R_m z^m
=\frac{\sqrt z\,\operatorname{arctanh}\sqrt z}{\sqrt{1-z}}.
\]
Differentiation gives \(2z(1-z)R'(z)=R(z)+z(1-z)^{-1/2}\); hence
\[
(2m-1)R_m=2(m-1)R_{m-1}+c_{m-1}\quad(m\ge2),\qquad R_1=1.
\tag{4}
\]
Because \(S_m=(2m-1)c_{m-1}\), \(H_m=H_{m-1}+c_{m-1}^2\), and \(S_{m-1}=2(m-1)c_{m-1}\), the sequence \(H_m/S_m\) satisfies exactly recurrence (4) and has initial value \(1\). This proves (3), including at \(m=1\).

**3. Add one Hermite level.** When passing from \(q\) to \(q+1\), use the block decomposition
\[
A_{q+1}(t)=\begin{pmatrix} A_q(t)&b(t)\\ b(t)^T&d(t)\end{pmatrix},
\quad b_j(t)=\int_t^\infty h_jh_q,\quad d(t)=\int_t^\infty h_q^2.
\]
Consequently
\[
V_{q+1}(t)-V_q(t)=d(t)(1-d(t))-2\sum_{j<q}b_j(t)^2.
\tag{5}
\]
The derivatives \(b_j'(t)=-h_j(t)h_q(t)\), \(b_j''(t)=-h_j'(t)h_q(t)-h_j(t)h_q'(t)\), \(d'(t)=-h_q(t)^2\), and \(d''(t)=-2h_q(t)h_q'(t)\) are exact.

If \(q=2m-1\) is odd, (1)–(3) applied to the second derivative of (5) at \(t=0\) give
\[
\begin{aligned}
V_{2m}''(0)-V_{2m-1}''(0)
&=2h_{2m-1}'(0)^2
  \sum_{k=0}^{m-1}\frac{h_{2k}(0)^2}{2m-1-2k}\\
&=\frac{4(2m-1)c_{m-1}R_m}{\pi}
=\frac{4H_m}{\pi}.
\end{aligned}
\tag{6}
\]

If \(q=2m\) is even, only the even-level derivatives \(b_j'(0)\) and the odd-level derivatives \(b_j''(0)\) survive. Defining
\[
T_m=\sum_{i=0}^{m-1}\frac{2(2i+1)c_i}{2m-2i-1}
=4mR_m-2S_m,
\]
(1)–(3) and the second derivative of (5) give
\[
\begin{aligned}
V_{2m+1}''(0)-V_{2m}''(0)
&=-\frac2\pi\bigl(c_m^2+2c_mS_m+c_mT_m\bigr)\\
&=-\frac2\pi\bigl(c_m^2+4mc_mR_m\bigr)
=-\frac2\pi\bigl(c_m^2+2H_m\bigr).
\end{aligned}
\tag{7}
\]
For \(q=1\), \(V_1(t)=d(t)(1-d(t))\) and \(V_1''(0)=-2/\pi\). Alternating (6) and (7), using \(H_{m+1}=H_m+c_m^2\), proves by induction that \(V_{2m-1}''(0)=-2H_m/\pi\) and \(V_{2m}''(0)=2H_m/\pi\) for every \(m\ge1\).

**4. Symmetry, strictness, and large order.** With \(D=\operatorname{diag}(1,-1,1,-1,\ldots)\), parity gives \(A_q(-t)=I_q-D A_q(t)D\); therefore \(V_q(-t)=V_q(t)\) and \(V_q'(0)=0\). Every \(H_m>0\), so the second derivative test yields the stated strict local extrema. Finally, Stirling's formula gives \(c_k^2=1/(\pi k)+O(k^{-2})\) for \(k\ge1\), and thus \(H_m=(\log m)/\pi+O(1)\). Since \(m=\lceil q/2\rceil\), the logarithmic curvature follows. \(\square\)

## Verification

The accompanying `check_curvature.py` independently evaluates the boundary-Wronskian double sum using exact fractions for every integer \(1\leq q\leq100\) and verifies identities (3) for \(1\leq m\leq80\). It reports 260 passed rational assertions. When SciPy is installed, it additionally evaluates the Gaussian half-line integrals directly for \(1\leq q\leq16\), and reports 16 successful numerical curvature comparisons. Run with `python check_curvature.py`. These finite checks support the algebra and normalization; the all-\(q\) theorem is established by the induction above.

## Relationship to prior work

Sánchez-Nungaray, González-Flores, López-Martínez, and Arroyo-Neri (2018) established the Hermite-matrix realization of horizontal-symbol Toeplitz operators on polyanalytic Fock spaces. Lee-Guzmán, Maximenko, Ramos-Vazquez, and Sánchez-Nungaray (2023) developed the higher-dimensional Fourier/Hermite decomposition. These are the structural starting points; neither source is credited here with a new variance formula. Forrester and Witte (2011) gave exact index-variance formulas at the fixed center for finite Gaussian unitary ensembles, an equivalent model for \(V_q(0)\). The assertion here concerns the **second derivative under a moving half-line threshold**, for all finite orders, rather than the centered variance itself. General results for centered Hermite spectral gaps and previously analyzed small orders do not, by their stated claims, determine this all-order curvature identity. The possibility of an equivalent older formula, particularly in random-matrix fluctuation literature, remains a priority limitation.

## Limitations

The theorem proves the complete sign and magnitude of the *centered second derivative* but neither counts all stationary points away from zero nor asserts global extremality for arbitrary \(q\). All threshold derivatives are in the specific normalized Hermite coordinate shown in the assumptions; a rescaling of the spatial coordinate rescales curvature quadratically. The relation to polyanalytic Toeplitz operators is via the standard Hermite fiber and should not be confused with a claim about the total trace of an infinite-dimensional half-plane Toeplitz operator. Verification programs are finite tests and do not establish independence or historical novelty. Independent mathematical validation has not been performed.

## References

1. A. Sánchez-Nungaray, C. González-Flores, R. R. López-Martínez, J. L. Arroyo-Neri, *Toeplitz Operators with Horizontal Symbols Acting on the Poly-Fock Spaces*, Journal of Function Spaces (2018), Article 8031259; first public version dated 2018-07-16. https://doi.org/10.1155/2018/8031259
2. E. Lee-Guzmán, E. A. Maximenko, G. Ramos-Vazquez, A. Sánchez-Nungaray, *Horizontal Fourier transform of the polyanalytic Fock kernel*, arXiv:2309.03410 (2023-09-07). https://arxiv.org/abs/2309.03410
3. N. S. Witte, P. J. Forrester, *On the Variance of the Index for the Gaussian Unitary Ensemble*, arXiv:1110.0119 (2011-10-01). https://arxiv.org/abs/1110.0119
