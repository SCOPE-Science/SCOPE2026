# Two-branch concentration spectrum for biharmonic functions on a ball

## Finding

Let \(d\ge3\) be an integer and \(0<R<1\). In the complex Hilbert space \(\mathcal B_2(\mathbb B^d)\) of square-integrable biharmonic functions on the Euclidean unit ball, let \(T_R\) be the positive concentration operator defined by
\[
\langle T_Ru,v\rangle=\int_{|x|<R}u(x)\overline{v(x)}\,dx.
\]
Put \(t=R^2\), \(p_m=2m+d\), and
\[
U_m=(p_m+2)^2(1-t)^2+8t.
\]
For every integer \(m\ge0\), the two eigenvalues in the spherical-harmonic degree-\(m\) block are exactly
\[
\boxed{\lambda_{m,\pm}=\frac{t^{p_m/2}}8\left(U_m\pm\sqrt{U_m^2-64t^2}\right).}
\]
Each occurs with angular multiplicity
\[
h_{m,d}=\binom{m+d-1}{d-1}-\binom{m+d-3}{d-1},
\]
where binomial coefficients with invalid nonnegative lower entries are interpreted as zero. If numerical eigenvalues from different blocks coincide, their global multiplicities add. Both sequences are strictly decreasing in \(m\), and \(0<\lambda_{m,-}<\lambda_{m,+}<1\). Their product obeys the exact identity
\[
\boxed{\lambda_{m,+}\lambda_{m,-}=t^{2m+d+2}.}
\]
The two branches split by reciprocal quadratic powers:
\[
\lambda_{m,+}\sim t^{d/2}(1-t)^2m^2t^m,\qquad
\lambda_{m,-}\sim\frac{t^{d/2+2}}{(1-t)^2}\,m^{-2}t^m.
\]
Define \(N_\pm(\varepsilon)=\sum_{m\ge0}h_{m,d}\mathbf1_{\{\lambda_{m,\pm}>\varepsilon\}}\), \(L=\log(1/\varepsilon)\), and \(\ell=\log(1/t)\). Then, as \(\varepsilon\downarrow0\),
\[
\boxed{N_+(\varepsilon)-N_-(\varepsilon)=
\frac8{(d-2)!\,\ell^{d-1}}L^{d-2}\log L+O_{d,t}(L^{d-2}),}
\]
and the total counting function satisfies
\[
\boxed{N_+(\varepsilon)+N_-(\varepsilon)=
\frac4{(d-1)!\,\ell^{d-1}}L^{d-1}+O_{d,t}(L^{d-2}).}
\]
In particular, the opposite logarithmic shifts in the two spectral branches cancel in the total count, but their difference has a nonzero sharp \(L^{d-2}\log L\) coefficient.

## Assumptions and scope

The Laplacian is the ordinary Euclidean Laplacian, and biharmonic means \(\Delta^2u=0\) in distributions, hence smoothly, throughout \(\mathbb B^d=\{x\in\mathbb R^d:|x|<1\}\). The inner product is the unweighted Lebesgue \(L^2\) inner product. Complex-valued functions are allowed. No boundary condition is imposed. The cutoff is a centered Euclidean ball, and \(d\) and \(t\) are fixed in the counting asymptotics. Only integer dimensions \(d\ge3\) are claimed. The eigenvalue-counting functions count multiplicity and use a strict cutoff; changing to a non-strict cutoff affects only lower-order terms.

The distinction between two branches is intrinsic: in each spherical-harmonic degree there are exactly two independent regular radial solutions \(r^m\) and \(r^{m+2}\). The ordinary harmonic space has only the former. Thus counting the two branches separately measures a genuine phenomenon of the fourth-order elliptic equation, not a double repetition of ordinary harmonic eigenvalues.

## Proof

**1. Complete degreewise decomposition.** By the Almansi decomposition for regular biharmonic functions, followed by the orthogonal spherical-harmonic expansion, the degree-\(m\) component has the form
\[
u(r\omega)=r^m(a+br^2)Y_{m,j}(\omega),\qquad a,b\in\mathbb C,
\]
where \(Y_{m,j}\) is an orthonormal spherical harmonic of degree \(m\) on \(S^{d-1}\). The \(L^2\)-closure of these components exhausts \(\mathcal B_2(\mathbb B^d)\), with different \((m,j)\) orthogonal. Indeed, regular biharmonic functions are sums of a harmonic function and \(|x|^2\) times a harmonic function, and spherical-harmonic partial sums converge on compact subballs and in the radial \(L^2\) decomposition. Angular orthogonality is unchanged by the radial characteristic function. There are \(h_{m,d}\) choices of \(j\).

**2. Exact two-by-two generalized eigenproblem.** Put \(p=2m+d\). For coefficient vectors \((a,b)\), the full-ball and restricted squared norms have Gram matrices
\[
G_p=\begin{pmatrix}\frac1p&\frac1{p+2}\\[3pt]\frac1{p+2}&\frac1{p+4}\end{pmatrix},\qquad
H_{p,t}=t^{p/2}\begin{pmatrix}\frac1p&\frac{t}{p+2}\\[3pt]\frac{t}{p+2}&\frac{t^2}{p+4}\end{pmatrix}.
\]
The eigenvalues of the concentration operator on this angular component are the generalized eigenvalues of \(H_{p,t}v=\lambda G_pv\). Direct calculation yields
\[
\det G_p=\frac4{p(p+4)(p+2)^2},\quad
\frac{\det H_{p,t}}{\det G_p}=t^{p+2},\quad
\operatorname{tr}(G_p^{-1}H_{p,t})=\frac{t^{p/2}}4\big((p+2)^2(1-t)^2+8t\big).
\]
Solving the characteristic quadratic gives the displayed formulas, including their product. Since \((p+2)^2(1-t)^2>0\), one has \(U_m>8t\), so the discriminant \(U_m^2-64t^2\) is strictly positive. Strict positivity and strict contraction follow from both the inner and outer balls having positive measure against every nonzero polynomial \(a+br^2\). Moreover \(\lambda_{m,+}\to0\); therefore the full operator is compact and the stated blocks give its complete positive spectrum.

**3. Strict monotonicity in the harmonic degree.** For any fixed nonzero coefficient vector \(v=(a,b)\), its Rayleigh quotient in degree \(m\) equals
\[
\mathcal R_m(v)=\frac{\int_0^R r^{2m+d-1}|a+br^2|^2\,dr}{\int_0^1 r^{2m+d-1}|a+br^2|^2\,dr}.
\]
The probability density in this quotient, when \(m\) is incremented, is multiplied by the strictly increasing function \(r^2\) and renormalized. The resulting probability of \(r<R\) strictly decreases: the covariance between the increasing factor \(r^2\) and the decreasing indicator \(\mathbf1_{\{r<R\}}\) is strictly negative because both sides of \(R\) carry positive mass. Hence \(\mathcal R_{m+1}(v)<\mathcal R_m(v)\) for every nonzero \(v\). Min-max on the two-dimensional coefficient space yields strict decrease of both maximal and minimal generalized eigenvalues. This establishes the ordered branches without assuming the eigenvalue formula is monotone term-by-term.

**4. Opposite polynomial factors.** Write \(S_m=\lambda_{m,+}+\lambda_{m,-}=t^{p_m/2}U_m/4\) and \(P_m=t^{p_m+2}\). As \(m\to\infty\),
\[
S_m=t^{m+d/2}(1-t)^2m^2(1+O_{d,t}(m^{-1})),\qquad
P_m/S_m^2=O_{d,t}(m^{-4}).
\]
Therefore \(\lambda_{m,+}=S_m(1+O_{d,t}(m^{-4}))\) and \(\lambda_{m,-}=P_m/\lambda_{m,+}\), giving the asserted reciprocal quadratic asymptotics. In particular, the ratio \(\lambda_{m,+}/\lambda_{m,-}\) grows like \(m^4(1-t)^4/t^2\).

**5. Sharp branch counting and cancellation.** Since the branches strictly decrease to zero, their cutoff degrees \(M_\pm(L)=\max\{m:\lambda_{m,\pm}>e^{-L}\}\) are well-defined for large \(L\). Step 4 implies
\[
\log\lambda_{m,\pm}=-\ell m\pm2\log m+\log C_\pm+O_{d,t}(m^{-1}),
\]
where \(C_+=t^{d/2}(1-t)^2\) and \(C_-=t^{d/2+2}/(1-t)^2\). Substitution into these monotone cutoffs gives
\[
M_\pm(L)=\frac{L\pm2\log L}{\ell}+O_{d,t}(1).
\]
Here the \(O(1)\) absorbs the constants \(\log C_\pm\), \(\log\ell\), and integer rounding. The spherical-harmonic dimension satisfies
\[
h_{m,d}=\frac{2}{(d-2)!}m^{d-2}+O_d(m^{d-3}),\qquad
\sum_{m=0}^M h_{m,d}=\frac{2}{(d-1)!}M^{d-1}+O_d(M^{d-2}).
\]
Consequently the difference of the two cumulative sums over the interval of length \((4/\ell)\log L+O(1)\) has coefficient \(\frac8{(d-2)!\ell^{d-1}}L^{d-2}\log L\), with remainder \(O_{d,t}(L^{d-2})\). Adding the two cumulative counts instead cancels their opposite \(\log L\) displacements at first order; Taylor expansion of the polynomial cumulative dimension gives the second displayed formula with remainder \(O_{d,t}(L^{d-2})\). These deductions hold for every fixed \(d\ge3\) and \(t\in(0,1)\).

## Verification

The included `biharmonic_concentration_check.py` computes exact rational Gram determinants and traces, compares generalized eigenvalues with the closed formula, verifies monotonicity for finite families of dimensions and radii, and evaluates the asymptotic counting coefficients for several large cutoffs. Run `python biharmonic_concentration_check.py` with Python 3. The checker uses only the Python standard library and reports its assertion count. Finite assertions are independent consistency checks, not a proof of the all-degree statements; the preceding analytic argument proves the latter.

## Relationship to prior work

Grzebuła, *The Polyharmonic Bergman Space for the Union of Rotated Unit Balls*, arXiv:1912.02035v1 (first publicly posted 2019-12-04), develops polyharmonic Bergman spaces, reproducing kernels and zonal-polyharmonic decompositions. The inspected introduction and §§4–6 treat those kernels but do not give concentric-subball concentration spectra or their two-branch logarithmic counting separation. The present operator is specifically the ordinary real-ball biharmonic \(L^2\) concentration operator in dimensions at least three.

Barrera-Castelán, Maximenko and Ramos-Vazquez, *Radial Operators on Polyanalytic Weighted Bergman Spaces*, arXiv:2009.14301v1 (2020-09-29), give general matrix representations for radial Toeplitz operators on planar polyanalytic disk spaces. Such representations are closely related to the two-dimensional analogue of the block calculation, and preclude treating a bare planar matrix formula as an original general principle. They do not provide the higher-dimensional real biharmonic operator or the sharp, multiplicity-weighted excess-counting coefficient claimed here.

Pessoa and Santos, *Polyharmonic Bergman Spaces and Bargmann Type Transforms*, J. Math. Anal. Appl. 449 (2017), concerns polyharmonic spaces over the upper half-plane and their decomposition; its mathematical setting differs from the concentric-ball concentration operator. Buoso and Provenzano, *On the Eigenvalues of a Biharmonic Steklov Problem* (2015), study fourth-order boundary eigenvalue problems rather than compression of an \(L^2\)-Bergman space to a smaller concentric ball. Searches of closely relevant mathematical literature and mathematical-results records found no directly covering statement. Lack of a matching result is not a proof of first discovery; priority should be checked independently before publication.

## Limitations

The result is confined to Euclidean balls, concentric cutoffs, unweighted volume, and fixed dimension at least three. It does not address general domains, nonradial observations, general polyharmonic order, or full information about accidental cross-block eigenvalue coincidences. The asymptotic remainder is not claimed optimal. The finite checker is supplementary and cannot certify infinitely many cases or historical originality. No independent mathematical validation is asserted.

## References

1. H. Grzebuła, *The Polyharmonic Bergman Space for the Union of Rotated Unit Balls*, arXiv:1912.02035v1, 2019-12-04; later *Complex Analysis and Operator Theory* 14 (2020), article 15. https://arxiv.org/abs/1912.02035
2. R. M. Barrera-Castelán, E. A. Maximenko, G. Ramos-Vazquez, *Radial Operators on Polyanalytic Weighted Bergman Spaces*, arXiv:2009.14301v1, 2020-09-29. https://arxiv.org/abs/2009.14301
3. L. V. Pessoa and A. Moura Santos, *Polyharmonic Bergman Spaces and Bargmann Type Transforms*, *J. Math. Anal. Appl.* 449 (2017), 619–641, DOI:10.1016/j.jmaa.2016.12.034.
4. D. Buoso and L. Provenzano, *On the Eigenvalues of a Biharmonic Steklov Problem*, arXiv:1411.3250, 2014; in *Integral Methods in Science and Engineering* (2015), 81–89.
