# A Lyons–Zumbrun axis-counting proof of the higher-order radial Frobenius formula
## Finding

Let \(d\ge2\), \(n\ge1\), let \(f(x)=g(|x|)\) be a smooth radial function on \(\mathbb R^d\), and define
\[
Dg(r)=\frac{g'(r)}{r}.
\]
The homogeneous-derivative identity of Lyons and Zumbrun gives a direct proof of
\[
\|\nabla^n f(x)\|_F^2
=
\sum_{q=0}^{\lfloor n/2\rfloor}
\alpha^d_{n,q}
\left[(D^qg)^{(n-2q)}(|x|)\right]^2,
\]
with
\[
\alpha^d_{n,0}=1,
\qquad
\alpha^d_{n,q}
=
\binom{n}{2q}(2q-1)!!
\prod_{k=0}^{q-1}(d-1+2k)
\quad (q\ge1).
\]
This supplies an affirmative solution to the first open problem stated by Mihula and Vybíral: their Theorem 1 follows from the Lyons–Zumbrun formula by an axis reduction and one central-binomial generating-function identity.

## Assumptions and scope

The dimension satisfies \(d\ge2\), the derivative order satisfies \(n\ge1\), and \(f\) is a smooth real-valued radial function. For \(r>0\), the radial profile is \(g(r)=f(re_1)\), and \(Dg(r)=g'(r)/r\). Smooth radiality implies that \(g\) is even at the origin and that every iterate \(D^qg\) extends smoothly there.

The Frobenius norm is taken over the full ordered derivative tensor:
\[
\|\nabla^n f(x)\|_F^2
=
\sum_{i_1,\ldots,i_n=1}^d
\left(\partial_{i_1}\cdots\partial_{i_n}f(x)\right)^2.
\]
The convention \((-1)!!=1\) is used when a transverse multiplicity is zero.

## Proof

The Lyons–Zumbrun identity says that, for every multi-index \(\alpha\) with \(|\alpha|=n\),
\[
\partial^\alpha f(x)
=
\sum_{k=0}^{\lfloor n/2\rfloor}
\frac{1}{2^k k!}
\Delta^k(x^\alpha)\,D^{n-k}g(|x|).
\]

The tensor \(D^nf\) transforms orthogonally under rotations, so its Frobenius norm is rotation invariant. It is therefore enough to work at \(x=re_1\) with \(r>0\).

Write a multi-index as
\[
\alpha=(a,\alpha_2,\ldots,\alpha_d).
\]
If some transverse exponent \(\alpha_i\), \(i\ge2\), is odd, every term \(\Delta^k(x^\alpha)\) remains divisible by \(x_i\); hence
\[
\partial^\alpha f(re_1)=0.
\]

Suppose instead that
\[
\alpha=(a,2m_2,\ldots,2m_d),
\qquad
q=m_2+\cdots+m_d,
\qquad
a=n-2q.
\]
Expanding \(\Delta^k=(\partial_1^2+\cdots+\partial_d^2)^k\), a term can survive at \(re_1\) only when every transverse power is completely removed. Thus \(k=q+\ell\), where \(0\le\ell\le\lfloor a/2\rfloor\), and a direct multinomial calculation gives
\[
\frac{1}{2^{q+\ell}(q+\ell)!}
\Delta^{q+\ell}(x^\alpha)(re_1)
=
\left(\prod_{i=2}^d(2m_i-1)!!\right)
\frac{a!}{2^\ell\ell!(a-2\ell)!}
r^{a-2\ell}.
\]
Consequently,
\[
\partial^\alpha f(re_1)
=
\left(\prod_{i=2}^d(2m_i-1)!!\right)
\sum_{\ell=0}^{\lfloor a/2\rfloor}
\frac{a!}{2^\ell\ell!(a-2\ell)!}
r^{a-2\ell}D^{a+q-\ell}g(r).
\]
The final sum is exactly the one-dimensional Lyons–Zumbrun identity applied to the profile \(D^qg\), and therefore
\[
\partial^\alpha f(re_1)
=
\left(\prod_{i=2}^d(2m_i-1)!!\right)
(D^qg)^{(a)}(r).
\]

Passing from ordered derivative indices to multi-indices contributes the multiplicity \(n!/\alpha!\). Hence the coefficient of
\[
\left[(D^qg)^{(n-2q)}(r)\right]^2
\]
in \(\|\nabla^nf(re_1)\|_F^2\) is
\[
C_{n,q,d}
=
\frac{n!}{(n-2q)!}
\sum_{m_2+\cdots+m_d=q}
\prod_{i=2}^d
\frac{((2m_i-1)!!)^2}{(2m_i)!}.
\]
Since
\[
\frac{((2m-1)!!)^2}{(2m)!}
=
\frac{(2m-1)!!}{2^m m!}
=
\frac{1}{4^m}\binom{2m}{m},
\]
the generating function is
\[
\sum_{m\ge0}
\frac{1}{4^m}\binom{2m}{m}z^m
=
(1-z)^{-1/2}.
\]
Therefore
\[
\sum_{m_2+\cdots+m_d=q}
\prod_{i=2}^d
\frac{1}{4^{m_i}}\binom{2m_i}{m_i}
=
[z^q](1-z)^{-(d-1)/2}
=
\frac{\prod_{k=0}^{q-1}(d-1+2k)}{2^q q!}.
\]
It follows that
\[
C_{n,q,d}
=
\frac{n!}{(n-2q)!}
\frac{\prod_{k=0}^{q-1}(d-1+2k)}{2^q q!}
=
\binom{n}{2q}(2q-1)!!
\prod_{k=0}^{q-1}(d-1+2k)
=
\alpha^d_{n,q}.
\]
This proves the desired identity for \(r>0\). Because the radial profile and all \(D^qg\) extend smoothly at the origin, continuity gives the identity also at \(x=0\).

## Verification

The proof was checked independently at the two first nontrivial orders. For \(n=2\), the coefficient of \((Dg)^2\) is \(d-1\), giving the classical Hessian identity
\[
\|\nabla^2f\|_F^2=(g'')^2+(d-1)(g'/r)^2.
\]
For \(n=3\), the coefficient of \(((Dg)')^2\) is \(3(d-1)\), agreeing with the displayed third-order formula in the focal source.

The coefficient reduction was also checked symbolically for \(1\le n\le8\) and \(2\le d\le6\), but those finite checks are only sanity checks. The proof for all \(n\) and \(d\) is the exact multinomial and generating-function argument above.

## Relationship to prior work

Mihula and Vybíral prove the same closed formula by a different induction based on identities for the Frobenius norms of derivatives of functions of the form \(G(x)x_j\). In their open-problems section, they explicitly ask whether the earlier Lyons–Zumbrun partial-derivative formula can instead be used to prove their Theorem 1.

Lyons and Zumbrun prove the homogeneous differential-operator identity used at the first step above. Their paper does not sum the squared derivative tensor or derive the coefficients \(\alpha^d_{n,q}\).

Ostermann uses the Lyons–Zumbrun identity to characterize radial Sobolev spaces. That work establishes norm equivalences and derivative expansions, but it does not state or imply the exact Frobenius identity with the coefficients above.

The new step is the axis classification of the surviving multi-indices, followed by the central-binomial convolution
\[
[z^q](1-z)^{-(d-1)/2}.
\]
That converts the componentwise Lyons–Zumbrun identity into the exact tensor-norm formula.

## Limitations

The argument is Euclidean and uses the rotational invariance of the Frobenius norm. It does not address the focal paper's separate questions about higher-order tensor spectral interpretations, non-Euclidean radial symmetry, or hyperbolic Sobolev characterizations.

The originality comparison found no prior statement of this alternative proof, but an equivalent derivation could exist in older isotropic-tensor literature under different terminology.

## References

1. Z. Mihula and J. Vybíral, *Higher-order derivatives of radially symmetric functions*, arXiv:2608.20941v1, 2026.
2. R. Lyons and K. Zumbrun, *Homogeneous partial derivatives of radial functions*, Proc. Amer. Math. Soc. 121 (1994), 315–316, DOI 10.1090/S0002-9939-1994-1227524-9.
3. M. Ostermann, *A characterization of the subspace of radially symmetric functions in Sobolev spaces*, arXiv:2209.02286v2; Commun. Contemp. Math. 27 (2025), Paper No. 2450018.
