# Sharp two-mechanism threshold for directional fourth-cumulant sectors in a four-heading active walker

## Finding
A planar velocity-jump walker taking the four cardinal headings can have an *isotropic* long-time displacement covariance but fourth cumulants of **opposite signs along axes and diagonals**. Both clockwise-turn bias and sufficiently frequent direct reversals can create this effect, and the full three-rate transition boundary and angular sectors are explicit.

Let the nonnegative right-angle turn rates be \(a,b>0\), the direct reversal rate be \(c\geq0\), and the speed be \(v>0\). Put
\[
s=a+b,\qquad d=\frac{a-b}{s},\qquad r=\frac{c}{s},\qquad H=(1+2r)^2+d^2.
\]
Define
\[
N_{\rm ax}=(1+2r)\big[(3+2r)d^2+(1+2r)^2(2r-1)\big],
\]
\[
N_{\rm diag}=d^4+(4r^2-1)d^2+16r^3+24r^2+12r+2>0.
\]
For displacement projected along \(u_\theta=(\cos\theta,\sin\theta)\), the second and fourth cumulant rates are
\[
\lim_{T\to\infty}\frac{\kappa_2(u_\theta\!\cdot R_T)}{T}
=\frac{v^2(1+2r)}{sH},
\]
\[
\boxed{\lim_{T\to\infty}\frac{\kappa_4(u_\theta\!\cdot R_T)}{T}
=\frac{3v^4}{s^3H^3}\left[N_{\rm ax}\cos^2(2\theta)-N_{\rm diag}\sin^2(2\theta)\right].}
\]
The fourth rate is **strictly negative on every diagonal** \(\theta=\pi/4+j\pi/2\), for all allowed rates. Positive directions exist exactly when \(N_{\rm ax}>0\). For \(0\leq r<1/2\), this is equivalent to
\[
\boxed{|d|>(1+2r)\sqrt{\frac{1-2r}{3+2r}}.}
\]
For \(r=1/2\), it holds exactly when \(d\ne0\); for \(r>1/2\), it holds for all \(|d|<1\). When \(N_{\rm ax}>0\), strictly positive fourth rates occur **only** in the four open angular sectors about cardinal axes, determined by
\[
|\tan(2\theta)|<\sqrt{N_{\rm ax}/N_{\rm diag}}
\]
with the inequality interpreted within the quarter-plane neighborhoods of each axis; equivalently the angular distance from an axis is less than
\[
\theta_c=\frac12\arctan\sqrt{N_{\rm ax}/N_{\rm diag}}\quad(0<\theta_c<\pi/4).
\]
Every other direction has a negative fourth rate, except the eight boundary rays where it is exactly zero. If \(N_{\rm ax}=0\), only the four cardinal axes have zero fourth rate; all other directions have a negative one. If \(N_{\rm ax}<0\), all fourth rates are negative. The zero-rate statements refer to the coefficient of linear growth, not necessarily to the sign of the finite-time fourth cumulant.

At zero direct reversal rate, the transition is the sharp chirality ratio condition \(a/b>2+\sqrt3\) or \(a/b<2-\sqrt3\). At equal turning rates \(a=b\), a distinct threshold occurs at \(c=(a+b)/2\). Independent isotropic translational Brownian noise changes the second rate by its Gaussian variance rate but leaves the fourth rate unchanged.

## Assumptions and scope
Let \(S_t\) be the continuous-time irreducible chain on \(\{0,1,2,3\}\), with clockwise jumps \(j\mapsto j+1\pmod4\) at rate \(a>0\), counterclockwise jumps at rate \(b>0\), and opposite-direction jumps \(j\mapsto j+2\pmod4\) at rate \(c\geq0\). Write \(e_0=(1,0),\ e_1=(0,1),\ e_2=(-1,0),\ e_3=(0,-1)\). Start \(S_0\) uniformly (the unique stationary heading distribution) and set \(R_T=v\int_0^T e_{S_t}\,dt\). The coordinate axes are the preferred heading directions. All limits hold for every \(a,b>0,c\ge0,v>0,\theta\in\mathbb R\); the stationary initial distribution only removes initial transients and is not needed for the asymptotic rates.

The fourth cumulant of the real projected displacement \(Z_T=u_\theta\cdot R_T\) is \(\kappa_4(Z_T)=\mathbb E[Z_T^4]-3\mathbb E[Z_T^2]^2\), since its mean is zero. For any additional independent Brownian motion \(\sqrt{2D}W_T\), with \(D\ge0\), the formula for \(\kappa_4\) holds unchanged; the second cumulant rate gains \(2D\).

## Proof
**1. Exact tilted characteristic polynomial.** The row generator has \(Q_{j,j}=-(a+b+c)\), \(Q_{j,j+1}=a\), \(Q_{j,j-1}=b\), and \(Q_{j,j+2}=c\), with indices modulo four. For the two-component exponential tilt \(k=(k_x,k_y)\), let \(G(k)=Q+v\operatorname{diag}(k_x,k_y,-k_x,-k_y)\). A direct four-by-four determinant calculation yields, for eigenvalue variable \(z\),
\[
\det(zI-G(k))=z(z+2s)\big[(z+s+2c)^2+(a-b)^2\big]
-v^2(k_x^2+k_y^2)(z+s+2c)(z+s)+v^4k_x^2k_y^2.
\]
At \(k=0\), the other eigenvalues are \(-2s\) and \(-(s+2c)\pm i(a-b)\), all in the open left half-plane. Consequently the eigenvalue \(\lambda(k)\) issuing from zero is analytic around \(k=0\), uniquely dominates there, and determines the scaled cumulant-generating function.

**2. Coefficient extraction.** Put \(k=t u_\theta\) and \(\lambda=A_2t^2+A_4t^4+O(t^6)\). Equating coefficients of \(t^2\) and \(t^4\) in the exact determinant gives
\[
A_2=\frac{v^2(1+2r)}{2sH},\qquad
A_4=\frac{v^4}{8s^3H^3}\big[N_{\rm ax}\cos^2(2\theta)-N_{\rm diag}\sin^2(2\theta)\big].
\]
The cumulant-generating function of \(Z_T\) is \(\log\mathbb E e^{tZ_T}=T\lambda(tu_\theta)+O(1)\) locally with all derivatives through order four: irreducibility gives a simple positive Perron eigenprojection with nonzero analytic amplitude at the origin, and the remaining spectrum stays uniformly separated. Hence the rates are \(2!A_2\) and \(4!A_4\), exactly as claimed. This proves the infinite-time statements, not merely finite-time numerical observations.

**3. Global sign classification.** First,
\[
N_{\rm diag}=d^4-d^2+2+4d^2r^2+16r^3+24r^2+12r>0,
\]
since \(d^4-d^2+2\ge7/4\). The factorization
\[
N_{\rm ax}=(1+2r)\left[(3+2r)d^2+(1+2r)^2(2r-1)\right]
\]
immediately gives the threshold: for \(r<1/2\), rearrange the bracket and take its nonnegative square root; for \(r\ge1/2\), inspect its two nonnegative summands and their equality case. Because \(\cos^2(2\theta),\sin^2(2\theta)\ge0\), the signs follow globally, and if \(N_{\rm ax}>0\), solving its strict inequality for \(\tan^2(2\theta)\) gives exactly the stated sectors. No assumptions on particular numerical values are used.

## Verification
The standalone `verify.py` derives the four-by-four characteristic polynomial with exact SymPy arithmetic and independently substitutes the analytic second/fourth coefficients for arbitrary projection components. A separate \(20\times20\) moment-evolution system numerically differentiates moments through order four for 24 combinations of parameters and orientations; the fourth-cumulant slope from two long observation times agrees with the theorem. The packaged code reports 31 passing exact identities and independent finite-time comparisons. The analytic spectral and sign arguments, not finite sampling, establish all-parameter claims.

## Relationship to prior work
Mallikarjun and Pal (2022), *Chiral run-and-tumble walker: transport and optimizing search* (arXiv:2209.05912), already treat **the same three-rate four-heading master-equation family**, derive its long-time diffusion coefficient and leading fourth moment, and give a general Fourier–Laplace matrix/resolvent in Appendix A (their equations (37)–(38) in the accessible text). These prior results, including the ability to compute full moments from the resolvent, are **not claimed as new**. Their printed fourth moment supplies the leading Gaussian \(T^2\) term; the present statement instead isolates the subleading connected fourth cumulant of order \(T\), its full angular sign sectors, and the sharp two-mechanism parameter boundary. The general resolvent is a significant implicit-priority risk: it algebraically encodes the claimed statistic, even though the inspected paper does not state this angular classification.

Loewe and Shendruk (2023), *Anisotropic run-and-tumble-turn dynamics* (arXiv:2305.03663v1; later published with Kozhukhov), analyze equal left/right \(90^\circ\) turning and fourth-order anisotropy but not independent chirality and reversal-rate tuning. Their equal-rate setting is included here only as a known baseline. Larralde (1997) considers a chiral **discrete-step** persistent walk and diffusivity, not the explicit continuous-time angular fourth-cumulant sign boundary in the accessible abstract; its full text was not accessible in the available literature route. This absence of an accessible full text is an originality risk, not evidence of novelty.

## Limitations
The calculation is specific to a single noninteracting particle with four cardinal headings, constant speed, exponential independent jump clocks, and a stationary heading start for the clean finite-time formula. It does not assert the sign of finite-time fourth cumulants at parameter directions where the asymptotic coefficient vanishes. It does not extend automatically to continuous-angle dynamics, interacting particles, arbitrary turning kernels, nonlinear confinement, or an infinite-dimensional kinetic limit. A general published characteristic function may imply the displayed formulas after nontrivial coefficient extraction; the self-review does not constitute an independent publication-priority determination. The fourth cumulant grows linearly but standardized kurtosis vanishes as observation time grows, consistent with ordinary asymptotic Gaussian diffusion.

## References
1. R. Mallikarjun and A. Pal, *Chiral run-and-tumble walker: transport and optimizing search*, arXiv:2209.05912 (first posted 2022-09-13), https://arxiv.org/html/2209.05912v1 (or https://arxiv.org/abs/2209.05912); Physica A 2023, DOI 10.1016/j.physa.2023.128821.
2. B. Loewe and T. N. Shendruk, *Anisotropic run-and-tumble-turn dynamics*, arXiv:2305.03663v1 (first posted 2023-05-05), https://arxiv.org/html/2305.03663v1; published with T. Kozhukhov in Soft Matter, DOI 10.1039/D3SM00589E.
3. H. Larralde, *Transport properties of a two-dimensional “chiral” persistent random walk*, Phys. Rev. E 56 (1997), 5004, DOI 10.1103/PhysRevE.56.5004; available abstract https://journals.aps.org/pre/abstract/10.1103/PhysRevE.56.5004.
