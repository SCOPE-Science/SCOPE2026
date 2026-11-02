# Sharp quadratic coercivity constant for the Gaussian Fock squaring map

## Finding

Let \(d\gamma(z)=\pi^{-1}e^{-|z|^2}\,dA(z)\) be normalized Gaussian area measure on \(\mathbb C\). For a polynomial \(F\), put
\[
U(F)=\int_{\mathbb C}|F(z)^2-F(0)^2|^2\,d\gamma(z),\qquad
V(F)=\inf_{t\in\mathbb R}\int_{\mathbb C}(|F(z)|^2-t)^2\,d\gamma(z).
\]
There is an exact optimal constant on the space of complex polynomials of degree at most two:
\[
\boxed{U(F)\le K V(F),\qquad 7K^3+9K^2-108K+108=0,\quad 2.4440873<K<2.4440874.}
\]
Here \(K=2.444087335815\ldots\) is the **unique root in the indicated interval**, and the optimal norm (rather than squared-norm) constant is \(\sqrt K=1.563357712046\ldots\). The zero polynomial and all nonzero constants have \(U=V=0\); for a nonconstant polynomial \(V>0\).

The nonconstant equality cases are precisely the functions obtained from
\[
F_*(z)=1+\sqrt{x_*}\,z-u_*z^2
\]
by multiplication by a nonzero complex scalar and rotation \(z\mapsto e^{i\theta}z\). The parameters are explicit algebraic numbers:
\[
u_* =\frac{13K^3-74K^2+132K-72}{44K^3-168K^2+144K}
=0.176395492888\ldots,\quad
x_* =\frac{-2(K-2)+8(K-1)u_*-(20K-24)u_*^2}{2(K-2)}
=0.422737290585\ldots.
\]
For an arbitrary nonconstant degree-at-most-two polynomial \(F(z)=a+bz+cz^2\), equality is thus equivalently characterized by \(|c|/|a|=u_*\), \(|b|^2/|a|^2=x_*\), and \(b^2\overline{ac}<0\) real (so necessarily \(abc\ne0\)).

In particular, the unrestricted Fock-space constant in the corresponding square-restricted estimate, if denoted \(C_{\mathrm{all}}\), satisfies the rigorous lower bound \(C_{\mathrm{all}}\ge\sqrt K>\sqrt2\). Its exact unrestricted value is **not** determined here.

## Assumptions and scope

All coefficients are complex and all integrals use the stated Gaussian probability measure. The infimum defining \(V\) is over *real constants* and is attained at \(t=\int|F|^2\,d\gamma\). This normalization matters: \(\int z^m\overline{z}^n\,d\gamma=\delta_{mn}\,n!\). The statement covers the entire complex vector space \(\{a+bz+cz^2:a,b,c\in\mathbb C\}\), including every coefficient boundary. There is no restriction to real coefficients or to an asymptotic/local neighborhood.

## Proof

**1. Exact fourth moments and the angular phase.** Write \(A=|a|\), \(B=|b|\), \(C=|c|\), and when \(ABC>0\) put \(\sigma=\operatorname{Re}(b^2\overline{ac})/(AB^2C)\in[-1,1]\). The Gaussian monomial orthogonality identity gives
\[
\begin{aligned}
U&=4A^2B^2+2B^4+8A^2C^2+8AB^2C\sigma+24B^2C^2+24C^4,\\
V&=2A^2B^2+B^4+4A^2C^2+8AB^2C\sigma+20B^2C^2+20C^4.
\end{aligned}
\]
Indeed the coefficients of \(F^2\) are \(a^2,2ab,b^2+2ac,2bc,c^2\), whose squared Fock norm is the sum of \(n!\) times their squared moduli, while \(V=\int|F|^4\,d\gamma-(\int|F|^2\,d\gamma)^2\). For nonconstant \(F\),
\[
U-V=(A^2+B^2+2C^2)^2-A^4>0.
\]
For fixed \((A,B,C)\) with \(ABC>0\), differentiation of \(U/V\) with respect to \(\sigma\) has sign \(V-U<0\). Therefore the greatest ratio occurs only at \(\sigma=-1\). There is no implicit assumption that phases can be chosen independently: \(\sigma=-1\) is attainable, for example with positive real \(a,b\) and negative real \(c\).

**2. Every coefficient boundary is subordinate.** If \(c=0\) and \(b\ne0\), then \(U=2V\). If \(a=0\), the formulas give \(U-2V=-16B^2C^2-16C^4\le0\). If \(b=0\), they give \(U-2V=-16C^4\le0\). Thus a ratio greater than two must have \(ABC>0\) and \(\sigma=-1\).

**3. Reduction to an algebraic positivity certificate.** Since the ratio is scale invariant, normalize \(A=1\), and set \(u=C/A>0\), \(x=B^2/A^2>0\). For an arbitrary real \(k>2\), let
\[
h=k-2,\qquad e=20k-24,\qquad
\beta_k(u)=-2h+8(k-1)u-eu^2.
\]
At the maximizing phase \(\sigma=-1\), the proposed deficit is
\[
\frac{kV-U}{A^4}=Q_k(u,x)
=h x^2-\beta_k(u)x+4hu^2+eu^4.
\]
If \(\beta_k(u)\le0\), the right side is positive for \(u>0,x\ge0\). If \(\beta_k(u)>0\), completing the square shows
\[
Q_k(u,x)=h\left(x-\frac{\beta_k(u)}{2h}\right)^2
-\frac{F_k(u)}{4h},\qquad
F_k(u)=\beta_k(u)^2-4h(4hu^2+eu^4).
\]
It therefore suffices to prove \(F_K(u)\le0\) on the region where \(\beta_K(u)>0\).

**4. Rigorous root isolation.** Let \(P(k)=7k^3+9k^2-108k+108\). Direct rational evaluations give
\(P(24440873/10000000)<0<P(24440874/10000000)\); moreover \(P'(k)=21k^2+18k-108>0\) throughout this interval, defining exactly one real \(K\) there. Put
\[
R(k)=\frac{13k^3-74k^2+132k-72}{44k^3-168k^2+144k}.
\]
Polynomial division of the numerators modulo \(P(k)\) gives the exact identities
\[
F_K(R(K))=0,\qquad \partial_uF_K(R(K))=0.
\]
In addition, exact rational interval arithmetic over the isolating interval of \(K\) verifies
\[
0.176<R(K)<0.177,\qquad
F_K(0.077)>0>F_K(0.078),\qquad
F_K(0.569)<0<F_K(0.571),
\]
\[
\beta_K(0.097)<0<\beta_K(0.098),\qquad
\beta_K(0.367)>0>\beta_K(0.368).
\]
These are **strict rational sign certificates**, not floating-point assertions: `CHECK.py` implements the interval operations using exact rational numbers and verifies the polynomial reductions. Since \(F_K\) is a quartic with positive leading coefficient \(16(K-1)(20K-24)\), the two disjoint sign-changing intervals isolate distinct simple roots \(\alpha\in(0.077,0.078)\), \(\gamma\in(0.569,0.571)\); the distinct root \(u_*=R(K)\in(0.176,0.177)\) has multiplicity at least two. All four roots of the quartic are now accounted for, so its sign on \((\alpha,\gamma)\) is nonpositive, and it vanishes there only at \(u_*\). Meanwhile the concave quadratic \(\beta_K\) has exactly two roots, one in \((0.097,0.098)\) and another in \((0.367,0.368)\); its strictly positive interval lies entirely within \((\alpha,\gamma)\). Consequently \(F_K\le0\) wherever \(\beta_K>0\), proving \(Q_K\ge0\) for all nonnegative \(u,x\).

**5. Sharpness and full equality classification.** Since \(\beta_K(u_*)>0\) (its root interval contains \(u_*\)), the positive minimizer \(x_*=\beta_K(u_*)/(2(K-2))\) satisfies \(Q_K(u_*,x_*)=0\). The equality analysis in steps 1–4 shows no other nonconstant equality cases: strict phase monotonicity forces \(\sigma=-1\), the completed square forces \(x=x_*\), and the quartic root structure forces \(u=u_*\). The boundary ratios are at most \(2<K\). This proves both the optimal constant and all asserted extremizers.

## Verification

The supplementary script `CHECK.py` (Python 3 with SymPy) reproduces the exact discriminant factorization
\[
\operatorname{disc}_uF_k=-268435456(k-2)^5(k-1)^3(5k-6)(7k^3+9k^2-108k+108),
\]
checks the two root identities modulo \(P\), all rational isolating interval inequalities and five independent exact Gaussian fourth-moment samples. Executing `python3 CHECK.py` reports `CHECK_OK 29`. The infinite and continuum quantifiers are justified by the quartic root exhaustion and the polynomial-sign argument above, not by the finite sample tests. The standalone symbolic script is a reproducibility aid; all essential calculations and their mathematical implications are specified here.

## Relationship to prior work

Bortolotto and Ramos [1, §1–3], in their preprint first publicly available on 2026-08-26, prove the corresponding **qualitative** Fock-space square-restricted coercivity inequality with an unspecified universal multiplicative constant. Their argument is not an exact optimization on the degree-two polynomial subspace; the present theorem determines the sharp coefficient on the first genuinely nonlinear three-dimensional Fock section and its complete equality set. It neither contradicts nor independently reproves their universal bound. Bertolini, de Dios Pont, Pineau, Ramos, and Taylor [2, §1.2 and §2] establish related local STFT modulus stability in a different comparison functional, again without this quadratic squared-coercivity optimization. The exact algebraic constant and phase condition do not follow merely by specializing either quoted theorem. The elementary Gaussian polynomial moment identities used in the proof are standard; their use alone is not claimed to be novel.

## Limitations

The sharp constant is proved **only** for complex polynomials of degree at most two. It is a lower bound, not an exact determination, for the unrestricted Fock-space constant. No result is asserted about sharp constants for degree three or larger, other Gaussian variances without rescaling, or stability away from the stated square-restricted functional. An earlier uncatalogued exact Gaussian quartic optimization may exist; the novelty conclusion depends on the inspected literature and is not an independent audit.

## References

[1] C. Bortolotto and J. P. G. Ramos, *A complex-analytic proof of square-restricted stable phase retrieval in Fock space*, arXiv:2608.26365v1 (first posted 2026-08-26), https://arxiv.org/html/2608.26365v1 .

[2] S. Bertolini, J. de Dios Pont, B. Pineau, J. P. G. Ramos, and M. A. Taylor, *L²-Stability for STFT phase retrieval*, arXiv:2605.20527v1 (first posted 2026-05-19), https://arxiv.org/html/2605.20527v1 .
