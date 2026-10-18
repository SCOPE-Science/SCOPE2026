# Sharp angular criterion for balanced two-circle phaseless polynomial sampling

## Finding

**Theorem (exact balanced two-ring phase retrieval).** Fix an integer \(d\ge1\), distinct radii \(0<r_1<r_2\le1\), and angular offsets \(\theta_1,\theta_2\in\mathbb R\). For each \(j\in\{1,2\}\) and \(k\in\{0,\ldots,2d-1\}\), measure
\[
I_{j,k}=\bigl|f(r_j e^{i(\theta_j+\pi k/d)})\bigr|^2,
\qquad f(z)=\sum_{m=0}^{d} a_mz^m.
\]
The resulting \(4d\) intensities identify **every** complex polynomial of degree at most \(d\), up to a single global unimodular multiplier, **if and only if**
\[
\sin\bigl(d(\theta_2-\theta_1)\bigr)\ne0.
\]
If the condition holds, the data also reconstruct the **entire squared modulus on each circle** by an explicit linear Fourier algorithm. If it fails, a pair of non-equivalent polynomials with identical samples exists on every choice of distinct positive radii.

The sole Nyquist de-aliasing matrix has singular values
\[
\sigma_{\pm}=\sqrt{1\pm\bigl|\cos(d(\theta_2-\theta_1))\bigr|}.
\]
Consequently its exact Euclidean condition number is
\[
\kappa_2=\sqrt{\frac{1+|\cos(d(\theta_2-\theta_1))|}{1-|\cos(d(\theta_2-\theta_1))|}}.
\]
Among admissible offsets, the optimally conditioned configurations are precisely
\[
\theta_2-\theta_1\equiv\frac{\pi}{2d}\pmod{\pi/d},
\]
for which \(\kappa_2=1\). This condition number refers **only to the normalized Nyquist linear subsystem**, not to stability of the nonlinear phase-reconstruction map.

## Assumptions and scope

Measurements are exact squared magnitudes of complex polynomial point evaluations. The exponent upper bound is \(d\), including polynomials whose constant or leading coefficient vanishes and including the zero polynomial. The sampled circles are concentric about zero, have strictly positive distinct radii, and each carries exactly \(2d\) equally spaced points. All phases are interpreted modulo the sampling polygon period \(\pi/d\). The recovered polynomial is defined only up to multiplication by a complex scalar of modulus one, which no intensity experiment can distinguish.

The number of measurements is \(4d\), corresponding to \(4(d+1)-4\) for \(d+1\) complex coefficients. No universal minimality claim among arbitrary complex phase-retrieval measurements is asserted. The result additionally fails in general if the two radii coincide, irrespective of offsets: \(f(z)=z\) and \(g(z)=r\) have identical modulus on the sole circle of radius \(r>0\) and are not unimodular multiples.

## Proof

**1. Fourier structure.** Write \(t_{j,k}=\theta_j+\pi k/d\) and \(N=2d\). On a circle of radius \(r\), the intensity is the real trigonometric polynomial
\[
|f(re^{it})|^2=\sum_{m=-d}^{d}c_m(r)e^{imt},\qquad
c_m(r)=r^m\sum_{h=0}^{d-m}a_{h+m}\overline{a_h}\,r^{2h}\quad(0\le m\le d),
\]
with \(c_{-m}(r)=\overline{c_m(r)}\). Taking the discrete transform
\[
\widehat I_{j,m}=\frac1N\sum_{k=0}^{N-1}I_{j,k}e^{-imt_{j,k}}
\]
recovers \(c_m(r_j)\) exactly for \(0\le m<d\); negative coefficients follow by conjugation. Indeed, only frequencies congruent modulo \(2d\) alias, and among \([-d,d]\) the only collision is the pair \(\pm d\).

**2. Resolve the sole alias.** The highest positive coefficient has the radius-separated form
\[
c_d(r_j)=r_j^d C,\qquad C=a_d\overline{a_0}.
\]
The two real Nyquist alternating sums satisfy
\[
B_j=\frac{1}{2Nr_j^d}\sum_{k=0}^{N-1}(-1)^k I_{j,k}
=\operatorname{Re}(Ce^{id\theta_j}).
\]
For \(C=u+iv\), this is exactly
\[
\begin{pmatrix}B_1\\B_2\end{pmatrix}
=\begin{pmatrix}\cos(d\theta_1)&-\sin(d\theta_1)\\
\cos(d\theta_2)&-\sin(d\theta_2)\end{pmatrix}
\begin{pmatrix}u\\v\end{pmatrix}.
\]
The determinant is \(-\sin(d(\theta_2-\theta_1))\). Under the stated nondegeneracy condition the pair \((u,v)\), hence both coefficients \(c_{\pm d}(r_j)\), is recovered. All coefficients of both real trigonometric polynomials are therefore known, so their full intensities \(|f(r_j e^{it})|^2\) are reconstructed for **every** real \(t\), not merely at the samples.

**3. Two complete concentric moduli determine a polynomial.** Suppose two polynomials \(f,g\) have identical squared moduli on both distinct circles. If one is zero, the other vanishes at infinitely many points and is also zero. Otherwise \(R=f/g\) is a nonzero rational function. For \(r>0\) define its rational circle reflection
\[
R_r^{\#}(z)=\overline{R(r^2/\overline z)}.
\]
The circle modulus equality implies the rational identity \(R(z)R_r^{\#}(z)=1\): it holds on all circle points avoiding poles and extends as a rational identity. Applying it at both radii gives \(R_{r_1}^{\#}=R_{r_2}^{\#}\) and hence
\[
R(z)=R(\lambda z),\qquad \lambda=r_2^2/r_1^2>1.
\]
Every nonzero finite pole or zero would then generate an infinite dilation orbit, impossible for a nonzero rational function. Thus \(R(z)=cz^q\) for some integer \(q\), and dilation invariance gives \(q=0\). The circle modulus equality forces \(|c|=1\). Hence \(f=cg\), establishing universal phase retrieval.

**4. Necessity and sharp Nyquist conditioning.** If \(\sin(d(\theta_2-\theta_1))=0\), then all sampled powered phases \(e^{id t_{j,k}}\) lie on the same real line through \(e^{id\theta_1}\). The polynomials
\[
f(z)=z^d+i e^{id\theta_1},\qquad
g(z)=z^d-i e^{id\theta_1}
\]
therefore have equal magnitude at every sample for **every** radius, although they are not constant unimodular multiples. This proves failure for the entire polynomial class.

For the real \(2\times2\) matrix above, the row vectors are unit vectors with inner-product magnitude \(|\cos(d(\theta_2-\theta_1))|\). Its Gram matrix has eigenvalues \(1\pm|\cos(d(\theta_2-\theta_1))|\), proving the stated singular values. The ratio of these singular values is minimized uniquely when the cosine vanishes, exactly at the staggered half-Nyquist offsets.

## Verification

The accompanying standalone script `verify_two_circle_nyquist.py` implements the measurement arrays and checks the Fourier coefficient formulas, alternating-sum de-aliasing, reconstructed top coefficient, singular-value formulas, and explicit counterexamples. With Python 3 and NumPy, run `python verify_two_circle_nyquist.py`; the stored script reports 990 passing numerical comparisons for degrees 1 through 15 and multiple angular choices. The arbitrary-degree statements follow from the displayed algebraic and rational-function proofs, not from the finite numerical tests.

## Relationship to prior work

Bodmann and Hammen [1] study low-redundancy polynomial phase retrieval, including a 2013 construction on **intersecting**, not concentric, circles using circle-to-line transformations. Pohl, Li, and Boche [2] give a particularly close **concentric** two-circle construction with \(4d\) total samples, allocated **asymmetrically** as \(2d+1\) exterior plus \(2d-1\) interior samples. That result is not an explicit balanced \(2d+2d\) polygon scheme, and its sampling theorem neither implies nor states the necessary-and-sufficient angular criterion and optimal Nyquist offset above. Chalendar and Partington [3] prove continuous two-circle modulus uniqueness for wider analytic function classes; their result explains the continuous uniqueness component but, without a finite sampling alias analysis, does not establish which balanced finite grids recover those continuous moduli. The contribution here is the **exact balanced finite-grid phase-retrieval classification**, together with full-modulus de-aliasing, aligned-grid counterexamples, and sharp conditioning of the remaining two-dimensional linear subsystem. No claim is made that the underlying discrete Fourier alias identity or continuous two-circle uniqueness alone is new.

## Limitations

Only concentric **regular** polygons with the stated equal allocation are classified; arbitrary node sets, nonconcentric circles, other sampling counts, or nonpolynomial analytic functions are not covered. The Nyquist subsystem is well-conditioned at a halfstep, but the complete nonlinear inverse can become poorly conditioned for nearly equal radii or near-zero polynomial values; global noise stability is **not** established. The construction does not specify a globally stable polynomial coefficient-recovery algorithm from reconstructed continuous moduli, although algebraic uniqueness is proved. A potentially implicit earlier equivalent classification in analytic phase-retrieval or signal-processing literature remains possible; publication priority is not independently established.

## References

[1] B. G. Bodmann and N. Hammen, *Stable phase retrieval with low-redundancy frames*, arXiv:1302.5487, first posted February 22, 2013. https://arxiv.org/pdf/1302.5487

[2] V. Pohl, N. Li, and H. Boche, *Phase retrieval in spaces of analytic functions on the unit disk*, SampTA 2017, DOI:10.1109/SAMPTA.2017.8024411. Open presentation, especially pages 17–18: https://www.ce.cit.tum.de/fileadmin/w00cgn/lti/pdf/vortraege/Pohl-Phase_Retrieval_in_Spaces_of_Analytic_Functions_on_the_Unit_Disk.pdf

[3] I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255, 2024, especially Theorems 2.6 and 2.11. https://arxiv.org/pdf/2403.16255
