# Sharp lower fourth moments and Clifford rigidity for complex quadratic spherical harmonics

## Finding

Let \(n\ge2\) be an integer, let \(d\sigma_n\) be the probability surface measure on \(S^{n-1}\subset\mathbb R^n\), and let \(Y\not\equiv0\) be a complex-valued spherical harmonic of degree two. Then

\[
\boxed{\quad
\int_{S^{n-1}}|Y|^4\,d\sigma_n\ \ge\
\frac{2(n+2)}{n+6}
\left(\int_{S^{n-1}}|Y|^2\,d\sigma_n\right)^2.
\quad}
\]

For **every even** \(n=2m\), the coefficient \(2(n+2)/(n+6)\) is optimal. In those dimensions, equality for a nonzero \(Y\) holds **if and only if** there exist a complex number \(c\ne0\) and a real orthogonal coordinate transformation \(\omega\mapsto x\) such that

\[
\boxed{\quad Y(\omega)=c\sum_{j=1}^{m}(x_j+i x_{m+j})^2.\quad}
\]

For **every odd** \(n\ge3\), the displayed inequality is strict for every nonzero \(Y\); no assertion of its sharp odd-dimensional constant is made.

There is also an exact *sum-of-squares deficit*. Write \(Y(\omega)=\omega^T A\omega\) uniquely with a complex symmetric trace-free matrix \(A=B+iC\), where \(B,C\) are real symmetric. Put

\[
 t=\operatorname{tr}(AA^*)>0,\qquad X=B^2+C^2,
 \qquad D_n=n(n+2)(n+4)(n+6).
\]

Here \(A^*=\overline A^{\,T}=\overline A\) and \(\|\cdot\|_F\) denotes Frobenius norm. Then, **in every dimension \(n\ge2\)**,

\[
\boxed{\begin{aligned}
 &\int |Y|^4\,d\sigma_n
 -\frac{2(n+2)}{n+6}\left(\int |Y|^2\,d\sigma_n\right)^2\\
 &=\frac{4|\operatorname{tr}(A^2)|^2
 +16\|A^2\|_F^2
 +32\|X-\tfrac{t}{n}I_n\|_F^2}{D_n}.
\end{aligned}}
\]

In particular, the three nonnegative terms give an exact quantitative certificate of departure from an extremizing Clifford quadratic.

## Assumptions and scope

All integrals are with normalized probability surface measure, not unnormalized area. The functions are arbitrary **complex-valued** degree-two spherical harmonics, with no boundedness, sign, or real-valuedness assumption. Such a harmonic has the unique form \(Y(\omega)=\omega^T A\omega\), with \(A=A^T\) and \(\operatorname{tr}A=0\), because \(\Delta(x^TAx)=2\operatorname{tr}A\). The dimension \(n=2\) is included. The sharpness and equality-orbit statements concern even \(n\), while the nonattainment statement for odd \(n\) does not give that dimension's optimal coefficient.

## Proof

**1. Exact spherical moments.** Let \(G\) have independent real standard Gaussian entries and write \(G=R\omega\), where \(\omega\) is uniform on \(S^{n-1}\) and independent of \(R\). Then

\[
\mathbb E R^4=n(n+2),\quad
\mathbb E R^8=D_n.
\]

For the symmetric trace-free matrix \(A\), the Gaussian quadratic-form generating identity, initially for small real formal parameters and then as a power series, is

\[
 \mathbb E\exp\!\left(uG^TAG+vG^TA^*G\right)
 =\exp\!\left(\sum_{k\ge1}\frac{2^{k-1}}{k}
 \operatorname{tr}(uA+vA^*)^k\right).
\]

The linear term vanishes. Extracting the coefficient of \(u^2v^2\) from the second and fourth powers and multiplying by \(2!2!\) gives

\[
\begin{aligned}
 \mathbb E |G^TAG|^4={}&
 4|\operatorname{tr}A^2|^2+8(\operatorname{tr}AA^*)^2\\
 &+32\operatorname{tr}(A^2(A^*)^2)
 +16\operatorname{tr}(AA^*AA^*).
\end{aligned}
\]

For clarity, the terms from the square of the quadratic trace expression are respectively \(4|\operatorname{tr}A^2|^2\) and \(8(\operatorname{tr}AA^*)^2\); the six cyclic words containing two \(A\)'s and two \(A^*\)'s yield the last two terms. Dividing by \(D_n\), and using the second Gaussian moment, yields

\[
\int|Y|^2\,d\sigma_n=\frac{2t}{n(n+2)}
\]

and

\[
 D_n\int |Y|^4\,d\sigma_n
 =4|\operatorname{tr}A^2|^2+8t^2+32r+16s,
\]

where \(r=\operatorname{tr}(A^2(A^*)^2)=\|A^2\|_F^2\) and \(s=\operatorname{tr}((AA^*)^2)\).

**2. The nonstandard matrix identity.** Because \(B,C\) are real symmetric, cyclicity of trace gives

\[
\begin{aligned}
 r&=\operatorname{tr}(B^4+C^4)+2\operatorname{tr}(BCBC),\\
 s&=\operatorname{tr}(B^4+C^4)+4\operatorname{tr}(B^2C^2)
 -2\operatorname{tr}(BCBC).
\end{aligned}
\]

Thus

\[
\boxed{r+s=2\operatorname{tr}(B^2+C^2)^2=2\operatorname{tr}X^2.}
\]

Substitute this into the fourth-moment formula to obtain

\[
 D_n\int |Y|^4\,d\sigma_n
 =4|\operatorname{tr}A^2|^2+8t^2+16r+32\operatorname{tr}X^2.
\]

Since \(X\) is real symmetric and \(\operatorname{tr}X=t\), the identity

\[
\operatorname{tr}X^2=\frac{t^2}{n}
 +\|X-\tfrac{t}{n}I_n\|_F^2
\]

is exact. The normalized fourth-moment difference in the Finding therefore equals its claimed three-term sum of squares; note that the proposed constant times the squared second moment, multiplied by \(D_n\), is \(8(n+4)t^2/n\). This proves the inequality and the deficit for every \(n\ge2\).

**3. Sharpness, parity and all equality cases.** For nonzero \(A\), equality in the deficit holds precisely when

\[
 A^2=0,\qquad B^2+C^2=(t/n)I_n.
\]

The condition \(A^2=0\) is equivalent to \(B^2=C^2\) and \(BC+CB=0\). Hence both \(B^2\) and \(C^2\) equal \(\kappa I_n\), where \(\kappa=t/(2n)>0\). Dividing by \(\sqrt\kappa\) produces real symmetric involutions \(J,K\) with \(JK=-KJ\). As \(K\) maps the \(+1\) and \(-1\) eigenspaces of \(J\) bijectively onto each other, their dimensions are equal. Therefore \(n\) must be even.

Conversely, if \(n=2m\), take the block matrices

\[
 B_0=\begin{pmatrix}I_m&0\\0&-I_m\end{pmatrix},\qquad
 C_0=\begin{pmatrix}0&I_m\\I_m&0\end{pmatrix}.
\]

These are trace-free real symmetric matrices, \(B_0^2=C_0^2=I_n\), and \(B_0C_0+C_0B_0=0\). Thus \(A_0=B_0+iC_0\) is trace-free, has \(A_0^2=0\), and makes the deficit zero. Its harmonic is \(\sum_{j=1}^{m}(x_j+ix_{m+j})^2\).

Finally, for any equality pair \(J,K\), an orthogonal change of basis makes \(J=\operatorname{diag}(I_m,-I_m)\). Anticommutation and symmetry force \(K\) to have off-diagonal blocks \(U,U^T\). Since \(K^2=I_n\), \(U\) is orthogonal, and a further block-diagonal orthogonal change makes \(U=I_m\). The original scalar \(\sqrt\kappa\) can be incorporated into the nonzero complex factor. These changes prove that **every** nonzero equality harmonic has the displayed canonical form, up to orthogonal coordinates and complex scaling. In odd dimensions equality is impossible; compactness of the unit sphere of the finite-dimensional harmonic space even implies a strict (unspecified) improvement over the displayed bound.

## Verification

The standalone program `verify.py` uses exact Gaussian-integer arithmetic and rational fractions. It constructs the fourth-order polynomial \((\omega^TA\omega)^2(\omega^TA^*\omega)^2\), integrates its monomials using exact spherical even moments, and compares the resulting integer numerator with the trace formula and the sum-of-squares deficit. It checks 80 deterministic trace-free complex quadratic matrices in dimensions \(2,3,4,5,6\), plus the four canonical equality matrices in dimensions \(2,4,6,8\). The stored `verify_output.txt` records the successful run. These finitely many examples are not substitutes for the universally quantified proof above.

To reproduce: run `python3 verify.py` with Python 3; no third-party packages are required.

## Relationship to prior work

Speckbacher and Hrycak (arXiv:1909.01670v1, first public 2019-09-04) study concentration of band-limited spherical harmonics through local large-sieve bounds, not the global normalized fourth-moment minimum within one quadratic harmonic eigenspace. Flock and Stovall (arXiv:2204.10361v1, first public 2022-04-21) study compactness and existence of extremizers for the spherical Fourier *extension operator*, whose output is measured in Euclidean space; that operator norm does not imply this finite-dimensional input-sphere lower fourth moment.

Dai, Feng and Tikhonov (arXiv:1408.1877v1, 2014) prove asymptotic **upper** reverse-Hölder ratios as harmonic degree grows. Stanton and Weinstein (1981) address local **maximization** of \(L^4\) norms of spherical harmonics. A later published sharp degree-two **upper** fourth-moment theorem (public published-finding corpus record identified by `d4106097159f`, 2026) determines the supremum and its real zonal extremizers. Its inspected result and proof do not give the lower constant, the Clifford-form equality characterization, or this sum-of-squares lower deficit: upper bounds alone do not imply a sharp lower bound. None of these inspected statements dominates the new lower bound; exact older matrix-invariant reformulations remain a possible originality risk.

## Limitations

The exact lower coefficient is shown optimal only when ambient dimension is even. The odd-dimensional optimal constant is not determined. No assertion is made for higher harmonic degrees, real-valued quadratic harmonics alone, or nonuniform measures. The 1981 article's public abstract, rather than its entire text, was available for inspection; older matrix-moment and Clifford-system literature could conceivably contain an equivalent statement. The original mathematical priority and an independent full scientific review remain unconfirmed.

## References

1. M. Speckbacher and T. Hrycak, *Concentration estimates for band-limited spherical harmonics expansions via the large sieve principle*, arXiv:1909.01670v1 (2019), https://arxiv.org/abs/1909.01670 .
2. T. C. Flock and B. Stovall, *On extremizing sequences for adjoint Fourier restriction to the sphere*, arXiv:2204.10361v1 (2022), https://arxiv.org/abs/2204.10361 .
3. F. Dai, H. Feng and S. Tikhonov, *Reverse Hölder's inequality for spherical harmonics*, arXiv:1408.1877v1 (2014), https://arxiv.org/abs/1408.1877 .
4. R. J. Stanton and A. Weinstein, *On the L4 norm of spherical harmonics*, Math. Proc. Cambridge Philos. Soc. 89 (1981), 343–358, https://doi.org/10.1017/S0305004100058229 .
5. *Sharp L4/L2 norm and extremizers for degree-two spherical harmonics*, public published-finding corpus mathematical-results record `d4106097159f` (2026), compared for upper-versus-lower logical coverage.
