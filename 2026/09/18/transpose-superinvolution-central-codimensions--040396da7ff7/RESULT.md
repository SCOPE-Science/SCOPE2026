# Exact central codimensions for the transpose superinvolution on $M_2$

Let $F$ be a field of characteristic zero and let $\mathbb M=M_{1,1}(F)=M_2(F)$ carry its canonical $\mathbb Z_2$-grading and the transpose superinvolution. Write $P_n^*$ for the multilinear degree-$n$ free $*$-space, $Id^*(\mathbb M)$ for the $*$-identities, and $Id^{z,*}(\mathbb M)$ for the central $*$-polynomials. Define
\[
c_n^*(\mathbb M)=\dim \frac{P_n^*}{P_n^*\cap Id^*(\mathbb M)},\qquad
c_n^{z,*}(\mathbb M)=\dim \frac{P_n^*}{P_n^*\cap Id^{z,*}(\mathbb M)}.
\]
Also set
\[
z_n^*(\mathbb M)=\dim \frac{P_n^*\cap Id^{z,*}(\mathbb M)}{P_n^*\cap Id^*(\mathbb M)}
=c_n^*(\mathbb M)-c_n^{z,*}(\mathbb M),
\]
the dimension of the nonidentity central layer.

## Theorem

For every $n\ge1$,
\[
\boxed{c_n^*(\mathbb M)=\binom{2n+2}{n+1}-2^n,}
\]
\[
\boxed{z_n^*(\mathbb M)=\binom{2n}{n}-2^{n-1},}
\]
and hence
\[
\boxed{c_n^{z,*}(\mathbb M)
=\binom{2n+2}{n+1}-\binom{2n}{n}-2^{n-1}
=\frac{3n+1}{n+1}\binom{2n}{n}-2^{n-1}.}
\]
Consequently,
\[
c_n^*(\mathbb M)\sim \frac4{\sqrt\pi}\frac{4^n}{\sqrt n},\qquad
z_n^*(\mathbb M)\sim \frac1{\sqrt\pi}\frac{4^n}{\sqrt n},\qquad
c_n^{z,*}(\mathbb M)\sim \frac3{\sqrt\pi}\frac{4^n}{\sqrt n},
\]
so
\[
\boxed{\frac{z_n^*}{c_n^*}\to\frac14,\qquad
\frac{c_n^{z,*}}{c_n^*}\to\frac34.}
\]
In particular the central $*$-codimension exponent is $4$.

## Proof

The recent computation of Bezerra dos Santos and Reis gives
\[
c_n^*(\mathbb M)
=2^n\left(2\sum_{j=0}^n\binom nj\binom{j}{\lfloor j/2\rfloor}2^{-j}-1\right).
\]
Put $a_j=2^{-j}\binom{j}{\lfloor j/2\rfloor}$ and $S_n=\sum_j\binom nj a_j$. Splitting $a_j$ into even and odd indices and using
\[
\sum_{k\ge0}\binom{2k}{k}\frac{t^k}{4^k}=(1-t)^{-1/2}
\]
gives
\[
A(z):=\sum_{j\ge0}a_jz^j
=\frac{1+z}{\sqrt{1-z^2}}-\frac{1-\sqrt{1-z^2}}{z}.
\]
The ordinary generating function of the binomial transform $S_n$ is therefore
\[
\sum_{n\ge0}S_nx^n
=\frac1{1-x}A\!\left(\frac{x}{1-x}\right)
=\frac{(1-2x)^{-1/2}-1}{x}.
\]
Hence
\[
S_n=[x^{n+1}](1-2x)^{-1/2}
=2^{-n-1}\binom{2n+2}{n+1},
\]
which proves the first boxed formula and sharpens the previously stated order estimate.

For the central layer, use the explicit multilinear normal forms in the same paper. For a composition $n=n_1+n_2+n_3+n_4$, the quotient by identities is zero unless $|n_3-n_4|\le1$. If $n_3=n_4=0$, it is one-dimensional. Its representative evaluates into the center precisely when the number $n_2$ of even skew variables is even. If $n_3=n_4=k>0$, the quotient is two-dimensional, represented by the two alternating odd-variable orders; the central subspace is exactly one-dimensional, spanned by their sum when $n_2$ is even and by their difference when $n_2$ is odd. If $|n_3-n_4|=1$, the surviving class evaluates in an off-diagonal homogeneous component and has no nonzero central class. Thus
\[
z_n^*
=\sum_{\substack{n_1+n_2=n\\ n_2\text{ even}}}\binom n{n_2}
+\sum_{1\le k\le n/2}\ \sum_{n_1+n_2=n-2k}
\frac{n!}{n_1!n_2!k!k!}.
\]
For $n\ge1$ the first sum is $2^{n-1}$. The second is
\[
\sum_{k\ge1}\binom n{2k}\binom{2k}{k}2^{n-2k}.
\]
Including $k=0$, this is the constant term of
\[
(2+x+x^{-1})^n=x^{-n}(1+x)^{2n},
\]
namely $\binom{2n}{n}$. Removing the $k=0$ term $2^n$ gives
\[
z_n^*=2^{n-1}+\binom{2n}{n}-2^n
=\binom{2n}{n}-2^{n-1}.
\]
Subtracting from $c_n^*$ gives the formula for $c_n^{z,*}$. The asymptotics follow from the central-binomial estimate
\[
\binom{2n}{n}\sim \frac{4^n}{\sqrt{\pi n}},
\]
and the exact ratio
\[
\frac{\binom{2n}{n}}{\binom{2n+2}{n+1}}
=\frac{n+1}{2(2n+1)}\longrightarrow\frac14.
\]

## Central cocharacter consequence

The proof also identifies the central part composition-by-composition. In the one-row multipartition notation of the source paper, a nonidentity central constituent occurs with multiplicity one exactly when either (i) $n_3=n_4=0$ and $n_2$ is even, or (ii) $n_3=n_4>0$. No central constituent survives when $|n_3-n_4|=1$. Thus the central layer is multiplicity-free at every fixed composition even though the full cocharacter has multiplicity two when $n_3=n_4>0$.

## Context and limitations

Bezerra dos Santos and Reis (arXiv:2609.20458v1, 17 September 2026) determine the $*$-identities, the full $*$-codimension sum, the cocharacters, and the generators of the central $*$-polynomials for this superinvolution. The formulas above extract a closed central-binomial form for their full codimension sum and, using their central-polynomial normal forms, compute the central codimension and central cocharacter layer explicitly.

Central codimension exponents for superalgebras with superinvolution were established in earlier work of Giordani--Ioppolo--dos Santos--Vieira, and proper central exponents were studied by La Mattina--dos Santos--Vieira; those general exponent results are prior work and are not claimed here. The novelty claim is limited to the exact three sequences above, the exact central-layer multiplicities, and the asymptotic $1:3$ split between central nonidentities and noncentral classes for this specific transpose-superinvolution algebra. Originality is to the best of our knowledge. The recent source preprint may be revised. For the two older exponent papers, abstracts and indexed records were inspected but not complete article text, leaving a residual risk of an equivalent special-case computation under different notation.

## References

1. R. Bezerra dos Santos and L. Reis, *Polynomial identities, central polynomials and cocharacters of $M_2(F)$ with transpose superinvolution*, arXiv:2609.20458v1 (2026).
2. G. Giordani, A. Ioppolo, A. dos Santos and A. Vieira, *On the central exponent of superalgebras with superinvolution*, Canadian Mathematical Bulletin 69 (2026), 472--489, DOI 10.4153/S0008439525101276.
3. D. La Mattina, R. B. dos Santos and A. C. Vieira, *Proper central exponent of superalgebras with graded involution or superinvolution*, Mathematische Zeitschrift 309 (2025), DOI 10.1007/s00209-025-03689-8.
