# Energy-perfect phase aliases in quadruple-angle Taylor restoration

## Finding

For each fixed Taylor degree \(m\geq1\), simultaneous cosine/sinc restoration can return an **exactly energy-preserving oscillator matrix at maximal phase error**, even when both scalar Taylor seed errors vanish. This is a property of the fixed-degree, freely scaled recurrence, not of the forward-error-controlled choice of parameters in any particular software implementation.

Put
\[
 P_m(x)=\sum_{k=0}^{m}\frac{(-x)^k}{(2k)!},\qquad
 Q_m(x)=\sum_{k=0}^{m}\frac{(-x)^k}{(2k+1)!}.
\]
For an integer \(s\geq1\), start with \(C_0=P_m(x)\), \(S_0=Q_m(x)\), and for \(0\leq j<s\) apply
\[
 C_{j+1}=2C_j^2-1,\qquad S_{j+1}=C_jS_j.
\]
At the target argument \(z=4^s x\), form the oscillator propagator
\[
 \widehat R_{m,s}(x)=
 \begin{pmatrix}C_s&2^s\sqrt x\,S_s\\-2^s\sqrt x\,S_s&C_s\end{pmatrix},\qquad
 R(z)=\begin{pmatrix}\cos\sqrt z&\sin\sqrt z\\-\sin\sqrt z&\cos\sqrt z\end{pmatrix}.
\]
Here \(\|\cdot\|_2\) is the operator 2-norm.

**Universal maximal alias.** Define
\[
 \beta_m=\bigl(\pi(2m+2)!\bigr)^{2/(2m+1)},\qquad
 \rho_m=\frac{\sqrt{\beta_m}}{\pi}.
\]
For each sufficiently large integer \(s\), let \(q_s\) be a positive odd integer nearest to \(\rho_m2^{2ms/(2m+1)}\), set \(\alpha_s=q_s\pi/2^s\), and take the unique sufficiently small positive root \(x_s\) of \(P_m(x_s)=\cos\alpha_s\). Then
\[
 x_s\sim\beta_m2^{-2s/(2m+1)},\qquad
 \widehat R_{m,s}(x_s)=-I_2,
\]
\[
 \lim_{s\to\infty}R(4^s x_s)=I_2,\qquad
 \lim_{s\to\infty}\|\widehat R_{m,s}(x_s)-R(4^s x_s)\|_2=2.
\]
The two seed errors satisfy
\[
 |P_m(x_s)-\cos\sqrt{x_s}|=O_m(x_s^{m+1}),\qquad
 |Q_m(x_s)-\operatorname{sinc}\sqrt{x_s}|=O_m(x_s^{m+1}).
\]
The limiting error \(2\) is the maximum possible distance between planar rotation matrices.

**Exact energy-zero census for degree one.** For \(m=1\), the energy defect
\[
 D_s(x)=1-C_s(x)^2-4^s x S_s(x)^2
\]
has **exactly \(2^s\) distinct positive roots** for each \(s\geq1\). These are
\[
 x=3,\qquad
 x=2\left(1-\cos\frac{(2k+1)\pi}{2^{j+1}}\right)
 \quad(0\leq j<s,\ 0\leq k<2^j).
\]
At all these roots, \(\widehat R_{1,s}(x)\) is exactly orthogonal but differs from \(R(4^sx)\). Thus a zero energy defect is never, at these positive test parameters, a certificate of correct phase.

## Assumptions and scope

The scalar Taylor series are evaluated in exact real arithmetic; \(m\) and \(s\) are positive integers, and \(x>0\). The map is the exactly specified simultaneous \(\phi_0\)/\(\phi_1\) restoration with \(\phi_0(x)=\cos\sqrt x\) and \(\phi_1(x)=\sin\sqrt x/\sqrt x\). The oscillator matrix is written in energy-normalized coordinates, so orthogonality is equivalent to preservation of the standard quadratic oscillator energy. No general finite-precision claim is implied.

## Proof

**1. The defect propagates multiplicatively.** Direct expansion gives
\[
\begin{aligned}
D_{j+1}&=1-(2C_j^2-1)^2-4^{j+1}x(C_jS_j)^2\\
&=4C_j^2\bigl(1-C_j^2-4^jxS_j^2\bigr)=4C_j^2D_j.
\end{aligned}
\]
Therefore
\[
 D_s=4^sD_0\prod_{j=0}^{s-1}C_j^2,\qquad
 C_j=T_{2^j}(P_m(x)),
\]
where \(T_n\) denotes the first-kind Chebyshev polynomial. The matrix identity \(\widehat R^{\mathsf T}\widehat R=(1-D_s)I_2\) follows immediately.

**2. Construction of the maximal alias.** Taylor expansion at zero yields
\[
 P_m(x)-\cos\sqrt x=\frac{(-1)^m}{(2m+2)!}x^{m+1}+O_m(x^{m+2}).
\]
Because \(P_m'(0)=-1/2\), the inverse-function theorem gives a unique small positive \(x\) satisfying \(P_m(x)=\cos\alpha\) whenever \(\alpha>0\) is small. In that regime \(\sqrt x/\alpha\to1\). With \(q_s\) as stated, \(q_s=\rho_m2^{2ms/(2m+1)}+O(1)\), hence
\[
 \alpha_s\sim\sqrt{\beta_m}\,2^{-s/(2m+1)},\qquad
 x_s\sim\alpha_s^2\sim\beta_m2^{-2s/(2m+1)}.
\]
The oddness of \(q_s\) yields
\[
 C_{s-1}=\cos(2^{s-1}\alpha_s)=0,
\]
using \(C_j=T_{2^j}(P_m(x_s))\). Consequently, \(C_s=-1\), \(S_s=0\), and \(\widehat R=-I_2\) **identically for each constructed input**, regardless of the initial \(S_0\).

To determine the true phase, let \(\theta_m(x)=\arccos P_m(x)\) on the small positive branch. Subtracting the Taylor polynomials and using the mean-value theorem for cosine, or Taylor inversion at \(\sqrt x\), gives
\[
 \sqrt x-\theta_m(x)=\frac{(-1)^m}{(2m+2)!}x^{m+1/2}+O_m(x^{m+3/2}).
\]
Indeed, \(P_m(x)-\cos\sqrt x\) equals \(\cos\theta_m(x)-\cos\sqrt x\), whose first variation is \(\sin\sqrt x\,(\sqrt x-\theta_m(x))\), with \(\sin\sqrt x\sim\sqrt x\). Thus
\[
 2^s(\sqrt{x_s}-\alpha_s)
 \longrightarrow\frac{(-1)^m\beta_m^{m+1/2}}{(2m+2)!}=(-1)^m\pi.
\]
Since \(2^s\alpha_s=q_s\pi\) and each \(q_s\) is odd, the exact phase \(2^s\sqrt{x_s}\) approaches an even multiple of \(\pi\) modulo \(2\pi\), proving \(R(4^sx_s)\to I_2\). For two rotations separated by angle \(\delta\), their operator-norm difference is \(2|\sin(\delta/2)|\), so the operator error tends to \(2\). The seed-error estimates follow from the omitted first term in the respective convergent Taylor series.

**3. Degree-one root census and distinctness.** For \(m=1\), \(P_1=1-x/2\), \(Q_1=1-x/6\), and an exact calculation gives
\[
 D_0(x)=\frac{x^2(3-x)}{36}.
\]
For \(x>0\), the only root of \(D_0\) is \(x=3\). Every remaining positive root of \(D_s\) must satisfy \(T_{2^j}(1-x/2)=0\) for some \(j<s\). All its simple Chebyshev roots are \(\cos((2k+1)\pi/2^{j+1})\), \(0\le k<2^j\), producing exactly the displayed parameters. The odd-numerator dyadic angle fractions at different \(j\) are unequal, and none equals \(\arccos(-1/2)=2\pi/3\). Therefore all these values are distinct, numbering \(1+\sum_{j=0}^{s-1}2^j=2^s\).

At a Chebyshev-factor root, the next restoration has \(C_{j+1}=-1\) and \(S_{j+1}=0\); after any additional restoration the result is \(I_2\). Each such \(x\) is a strictly positive **algebraic** number (cosines of rational multiples of \(\pi\) are algebraic). Therefore \(2^s\sqrt x\) is positive algebraic and cannot be an integer multiple of the transcendental number \(\pi\). Hence the true rotation cannot equal the approximate \(\pm I_2\).

At \(x=3\), the seed is exactly a rotation of angle \(2\pi/3\) because \(P_1(3)=-1/2\) and \(\sqrt3\,Q_1(3)=\sqrt3/2\). Its restored rotation has angle \(2^s(2\pi/3)\), whereas the exact rotation has algebraic angle \(2^s\sqrt3\). Equality modulo \(2\pi\) would equate a nonzero algebraic number to a nonzero rational multiple of \(\pi\), again impossible. These exhaust all positive zero-defect inputs.

## Verification

Run `python verify.py` after installing the version in `requirements.txt`. The checker replays 11,669 deterministic assertions, including exact rational defect propagation, distinctness and numerical vanishing of the degree-one energy roots, plus 250-digit high-precision checks for degrees \(m\in\{1,2,4,20\}\) and scaling counts through \(s=512\). Illustratively, at \(m=1,s=24\), the alias has \(x\approx0.00027232516905869\), \(q=88129\), and spectral-norm error \(1.9999999998150\) despite the tiny cosine seed error. The numerical checker does not certify the asymptotic theorem or transcendence step; those are proved above.

## Relationship to prior work

Li, Wang and Zhang (2024, arXiv:2406.06008, v1) give the \(\phi\)-function Taylor seeds, the quadruple-angle recurrence, a forward-error analysis and an adaptive parameter-selection procedure. Al-Mohy (2017/2018, arXiv:1708.08360) develops Taylor/Chebyshev recovery for trigonometric matrix-function actions. These are foundational methods, not claimed here. Earlier work on oscillator integrators distinguishes energy preservation from phase accuracy. The contribution here is the specified all-degree exact-energy/maximal-phase alias family, its sharp seed scaling and the complete degree-one zero-energy root census. These are implication-level comparisons, not a proof of priority.

## Limitations

The theorem concerns **deliberately chosen fixed-degree overscaled inputs**, rather than the parameters selected by the cited article's certified forward-error controller. The target arguments \(4^sx_s\) grow with \(s\), so small seed error alone is not a complete error bound; the cited controller anticipates amplification from restoration. Exact algebraic energy zeros may be perturbed by floating-point rounding, and the theorem does not assert the same pathology occurs under ordinary practical tolerance selection. The limiting constant is a supremum, not necessarily attained at finite scaling. The root census is complete only at degree one. Publication priority remains subject to unindexed literature, particularly specialized earlier quadruple-angle algorithms.

## References

1. Dongping Li, Xue Wang, Xiuying Zhang, *Efficient algorithm for the oscillatory matrix functions*, arXiv:2406.06008v1 (first submitted 2024-06-10), especially equations (8), (9), (18), (20), (42), (44), and Algorithm 3. https://arxiv.org/html/2406.06008v1
2. Awad H. Al-Mohy, *A New Algorithm for Computing the Actions of Trigonometric and Hyperbolic Matrix Functions*, arXiv:1708.08360v1 (first submitted 2017-08-28), Sections 1–3. https://arxiv.org/html/1708.08360v1
3. W. Shi, X. Wu, K. Liu, *Efficient implementation of the ARKN and ERKN integrators for multi-frequency oscillatory systems with multiple time scales*, Applied Numerical Mathematics 151 (2020), 13–26. DOI:10.1016/j.apnum.2019.12.014. Referenced in [1] as prior simultaneous quadruple-angle implementation; complete text not inspected here.
4. Nicholas J. Higham, *Functions of Matrices: Theory and Computation*, SIAM, 2008 (standard matrix-function and Chebyshev background).
