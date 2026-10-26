# Sharp least fourth moment and isotropy deficit for real cubic spherical harmonics

## Finding
Let \(d\sigma\) be probability surface measure on \(S^2\). For every nonzero **real-valued** spherical harmonic \(Y\) of degree three,
\[
\boxed{\frac{\int_{S^2}Y^4\,d\sigma}{(\int_{S^2}Y^2\,d\sigma)^2}\geq\frac{315}{143}.}
\]
This constant is sharp, attained by \(Y(x,y,z)=xyz\). More precisely, there is an exact nonnegative tensor-isotropy deficit identity; it characterizes **all** equality cases without a choice of coordinates.

## Assumptions and scope
Every real degree-three harmonic is uniquely \(Y_T(\omega)=\sum_{i,j,k=1}^3T_{ijk}\omega_i\omega_j\omega_k\) for a real, fully symmetric, trace-free tensor \(T\), meaning \(\sum_iT_{iik}=0\) for each \(k\). Set
\[
M_{ij}=\sum_{p,q=1}^3T_{ipq}T_{jpq},\qquad t=\operatorname{tr}M,\qquad u=\operatorname{tr}(M^2).
\]
Here \(t>0\) for nonzero \(T\), and \(M\) is a real positive-semidefinite \(3\times3\) matrix. All integrals are with respect to probability surface measure, not area measure. No complex-valued extension or higher-degree generalization is asserted.

## Proof
**Exact moments.** A complete homogeneous harmonic-cubic basis is
\[
\begin{aligned}
&z(5z^2-3r^2),\quad x(5z^2-r^2),\quad y(5z^2-r^2),\\
&z(x^2-y^2),\quad 2xyz,\quad x(x^2-3y^2),\quad y(3x^2-y^2),
\end{aligned}
\]
where \(r^2=x^2+y^2+z^2\). Each polynomial is harmonic; their coefficient matrix has rank seven, matching the full real harmonic-cubic dimension.

For any nonnegative integers \(p,q,s\), the exact spherical monomial rule is
\[
\int_{S^2}x^{2p}y^{2q}z^{2s}\,d\sigma
=\frac{(2p-1)!!(2q-1)!!(2s-1)!!}{(2p+2q+2s+1)!!},
\]
with \((-1)!!=1\); an integrand with an odd power of any coordinate has zero mean. Substitute an arbitrary linear combination of the seven basis functions and calculate \(T_{ijk}=\partial_i\partial_j\partial_kY/6\). Coefficientwise expansion gives two **polynomial identities valid for all seven real coefficients**:
\[
\int_{S^2}Y_T^2\,d\sigma=\frac{2t}{35},\qquad
\int_{S^2}Y_T^4\,d\sigma=\frac4{5005}(7t^2+6u).
\]
The supplementary `verify.py` reproduces this finite algebraic derivation using exact rational operations: the seven basis vectors are checked for harmonicity and independence, and **every one of the 210 quartic coefficient slots** is compared. This is an exhaustive finite polynomial-identity calculation, not numerical sampling or partial enumeration. It can also be reproduced by expanding the displayed basis directly with the displayed monomial rule.

**Deficit and equality.** Subtracting the proposed sharp multiple of the squared second moment yields the exact identity
\[
\boxed{
\int Y_T^4\,d\sigma-\frac{315}{143}\left(\int Y_T^2\,d\sigma\right)^2
=\frac{24}{5005}\left(u-\frac{t^2}{3}\right)
=\frac{24}{5005}\left\|M-\frac t3I_3\right\|_F^2.}
\]
The last expression is nonnegative. Equality holds **if and only if** \(M=(t/3)I_3\). This is a complete tensor-invariant criterion, not a claim that the equality set consists of a single rotation orbit.

**Sharpness.** For \(Y=xyz\), the only nonzero tensor entries are \(T_{\pi(1)\pi(2)\pi(3)}=1/6\), for the six permutations \(\pi\). Thus \(M=I_3/18\). Explicit spherical moments give \(\int Y^2\,d\sigma=1/105\) and \(\int Y^4\,d\sigma=1/5005\); their ratio is \(315/143\). Rotation and nonzero real scaling preserve the ratio.

## Verification
Run `python3 verify.py` with Python 3 and SymPy. The packaged `verification_output.txt` records the exact-rational checks: seven independent harmonic cubics, the degree-two polynomial identity, all 210 quartic coefficient comparisons, and the sharp \(xyz\) witness. No floating-point tolerance, random sample, unbounded search, or external data are required. The exact algebraic proof above identifies which finite calculations suffice for the universal statement.

## Relationship to prior work
Stanton and Weinstein (1981), in §6(c), explicitly discussed the question of the minimum of the degree-\(\ell\) \(L^4/L^2\) ratio; their paper proves highest-weight **local maxima** and asymptotic upper bounds rather than this cubic lower bound. Kwon and Lee (2017) establish scale-sharp bounds for spherical harmonic **projection operators**, not the exact least fourth moment in one real eigenspace. Flock and Stovall (2022), a contemporary spherical Fourier-analysis source, establish extension-operator profile decompositions and extremizer-existence criteria, not this fixed-degree \(L^4\) minimum. Related published degree-two spherical-harmonic moment results concern a different harmonic representation; no implication of the degree-three tensor identity follows merely from the degree-two case.

## Limitations
The claim covers real degree-three spherical harmonics on the two-sphere with normalized surface measure only; it does **not** determine the sharp maximum, classify equality tensors into rotation orbits, treat complex harmonics, or extend to other degrees/dimensions. An unlocated equivalent tensor-invariant identity in older invariant-theory or octupole literature remains possible; database non-detection alone cannot establish worldwide priority. Independent scientific audit has not been performed.

## References
1. R. J. Stanton and A. Weinstein, *On the L4 norm of spherical harmonics*, Math. Proc. Cambridge Philos. Soc. **89** (1981), 343–358, DOI:10.1017/S0305004100058229; especially §6(c).
2. Y. Kwon and S. Lee, *Sharp \(L^p\)-\(L^q\) estimates for the spherical harmonic projection*, arXiv:1709.09795v1, first posted 2017-09-28.
3. T. C. Flock and B. Stovall, *On extremizing sequences for adjoint Fourier restriction to the sphere*, arXiv:2204.10361v1, first posted 2022-04-21; MSC 42B20.
4. F. Dai, H. Feng and S. Tikhonov, *Reverse Hölder's inequality for spherical harmonics*, arXiv:1408.1877v1 (2014), asymptotic norm comparisons.
