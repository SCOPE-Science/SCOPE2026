# Sharp affine Bernstein positivity threshold on the three-sphere

## Finding

Let \(\mathbb S^3\subset\mathbb R^4\) be the unit sphere. For every integer \(n\ge1\), let the ordinary *affine* Bernstein operator on the dot-product variable be
\[
(\mathcal B_n f)(t)=\sum_{j=0}^{n}\binom nj
\left(\frac{1+t}{2}\right)^j
\left(\frac{1-t}{2}\right)^{n-j}
 f\left(-1+\frac{2j}{n}\right),\qquad -1\le t\le1.
\]
A continuous real function \(f\) is zonal positive definite on \(\mathbb S^3\) when every matrix \([f(x_i\cdot x_j)]_{i,j}\) is positive semidefinite. Then
\[
\boxed{\mathcal B_n\text{ preserves every such }f\quad\Longleftrightarrow\quad 1\le n\le4.}
\]
In particular, the borderline degree four preserves positive definiteness on \(\mathbb S^3\), in contrast to its failure on \(\mathbb S^2\). At degree four, the fourth normalized spherical coefficient of the image of a single even spherical mode is zero exactly at input degrees \(0,2,6\) and is positive for every other even input degree. For odd input degrees, the third coefficient vanishes exactly at input degree \(1\).

The positive degree-four result and the resulting complete three-sphere threshold are the focus; the general high-degree obstruction is included with an independent derivation for completeness, not claimed as new.

## Assumptions and scope

The dimension is exactly three (the ambient Euclidean space is four-dimensional); \(n\) is a positive integer, and \(f\) is any continuous real zonal positive-definite function, with no smoothness or pointwise nonnegativity assumption. The claim concerns positive semidefinite kernels, not *strictly* positive-definite kernels. Normalization \(f(1)=1\) can be imposed without loss of generality for nonzero positive-definite functions, but is unnecessary for the preservation assertion.

Write \(U_m\) for the Chebyshev polynomial of the second kind and put \(R_m(t)=U_m(t)/(m+1)\). Then \(R_m(1)=1\), \(R_m(\cos\theta)=\sin((m+1)\theta)/((m+1)\sin\theta)\), and Schoenberg's characterization is
\[
f(t)=\sum_{m=0}^{\infty}a_m R_m(t),\qquad a_m\ge0,\qquad \sum_{m=0}^{\infty}a_m<\infty.
\]
The series converges uniformly. Thus it suffices to show nonnegative \(R_k\)-coefficients for every \(\mathcal B_n R_m\), for all \(m\ge0\) and \(n\le4\).

## Proof

**Degrees one and two.** Parity gives \(\mathcal B_1R_m=R_0\) for even \(m\) and \(\mathcal B_1R_m=R_1\) for odd \(m\). For degree two, odd modes give \(\mathcal B_2R_m=R_1\). For even \(m\), letting \(b=R_m(0)\), the expansion is
\[
\mathcal B_2R_m=\frac{5+3b}{8}R_0+\frac{3(1-b)}8R_2.
\]
Here \(|b|\le1\), so both coefficients are nonnegative.

**Degree three.** Put \(a=R_m(1/3)\). Exact Bernstein-basis expansion gives, when \(m\) is even,
\[
\mathcal B_3R_m=\frac{7+9a}{16}R_0+\frac{9(1-a)}{16}R_2,
\]
and, when \(m\) is odd,
\[
\mathcal B_3R_m=\frac{7+3a}{8}R_1+\frac{1-3a}{8}R_3.
\]
At \(m=0\) the image is \(R_0\); at \(m=1\) it is \(R_1\). For every \(m\ge2\), the trigonometric formula yields
\[
|a|\le\frac{3}{2\sqrt2\,(m+1)}.
\]
This ensures \(7+9a>0\) for even \(m\ge2\), and for odd \(m\ge3\) gives \(3a\le9/(8\sqrt2)<1\). All remaining displayed coefficients are manifestly nonnegative because \(|a|\le1\). Therefore degrees one through three preserve the cone.

**The borderline degree four.** Set \(A=R_m(1/2)\) and \(B=R_m(0)\). If \(m\) is odd, \(B=0\), and the complete expansion is
\[
\mathcal B_4R_m=\left(\frac34+\frac A2\right)R_1+\left(\frac14-\frac A2\right)R_3.
\]
The trigonometric formula at \(\theta=\pi/3\) yields \(|A|\le1/(m+1)\). Since \(m+1\ge2\), both coefficients are nonnegative. Equality in the \(R_3\)-coefficient occurs only for \(m=1\): when \(m\ge3\), \(|A|\le1/4<1/2\).

If \(m\) is even, the complete expansion is
\[
\mathcal B_4R_m=
\frac{21+28A+15B}{64}R_0+
\frac{81-36A-45B}{128}R_2+
\frac{5(1-4A+3B)}{128}R_4.
\]
For even \(m\), \(|A|\le1/(m+1)\) and \(|B|=1/(m+1)\). When \(m\ge8\), these inequalities make all three coefficients *strictly* positive: their numerators are bounded below respectively by \(21-43/(m+1)\), \(81-81/(m+1)\), and \(5(1-7/(m+1))\). The remaining even input degrees are exactly checked by
\[
\begin{aligned}
\mathcal B_4R_0&=R_0,\\
\mathcal B_4R_2&=\tfrac14R_0+\tfrac34R_2,\\
\mathcal B_4R_4&=\tfrac{23}{80}R_0+\tfrac{99}{160}R_2+\tfrac3{32}R_4,\\
\mathcal B_4R_6&=\tfrac5{14}R_0+\tfrac9{14}R_2.
\end{aligned}
\]
All coefficients are nonnegative, proving degree-four preservation and the stated exact vanishing pattern.

**Every degree five and higher fails.** For \(n\ge5\), choose the normalized positive-definite input \(R_{n+2}\). Its \(R_n\)-coefficient after Bernstein approximation is
\[
\boxed{\eta_n=\frac{n!}{n^n}\frac{(n+1)^2(4-n)}{3n(n+3)}<0.}
\]
Here is an independent derivation. Let \(t_j=-1+2j/n\) and
\[
S_p=\sum_{j=0}^{n}(-1)^{n-j}\binom nj t_j^p.
\]
The exponential generating function is
\[
\sum_{p\ge0}S_p\frac{s^p}{p!}
=\bigl(2\sinh(s/n)\bigr)^n
=\left(\frac{2s}{n}\right)^n\left(1+\frac{s^2}{6n}+O(s^4)\right).
\]
Consequently, \(S_n=n!(2/n)^n\) and \(S_{n+2}/S_n=(n+1)(n+2)/(6n)\). The two leading terms of \(U_{n+2}(t)\) are \(2^{n+2}t^{n+2}-(n+1)2^n t^n\). The coefficient of \(t^n\) in \(\mathcal B_nR_{n+2}\) is therefore
\[
\frac{2^{-n}}{n+3}\bigl(2^{n+2}S_{n+2}-(n+1)2^n S_n\bigr)
=\frac{n!}{n^n}\frac{2^n(n+1)(4-n)}{3n(n+3)}.
\]
Since the leading coefficient of \(R_n\) is \(2^n/(n+1)\), division yields \(\eta_n\). Its negativity excludes positive definiteness by the uniqueness of the Schoenberg coefficients. At \(n=5\), for example, \(\eta_5=-36/3125\). The two implications establish the classification.

## Verification

The standalone file `verify.py` performs exact rational arithmetic using only Python's standard library. It independently expands the Bernstein images into the normalized Chebyshev basis for \(1\le n\le4\), \(0\le m\le120\), checks the degree-four coefficient formulas, and compares the negative top coefficient against its closed form for \(5\le n\le25\). Run `python3 verify.py` after extracting that file. These finite checks support but do not replace the preceding proof, which treats all \(m\) and all \(n\).

## Relationship to prior work

Otten, Nguyen, and Watts (arXiv:2608.04836, first public August 5, 2026) prove positive-definiteness preservation for an *angular* Bernstein operator on \(\mathbb S^1\), and in their Section 4 give an affine degree-four negative example on \(\mathbb S^2\). Their article does not settle the ordinary affine operator on \(\mathbb S^3\). Beatson and zu Castell (arXiv:1510.08658) study different positivity-preserving dimension-hopping operators; their differentiation and integration operators are not this affine Bernstein map. The classical Schoenberg expansion and Chebyshev identities are used with attribution. The all-dimensional high-degree obstruction is an antecedent calculation, not the novelty claimed here. The new step is the positive borderline degree-four classification on \(\mathbb S^3\), completing the threshold in that dimension.

## Limitations

The conclusion applies only to the ordinary affine Bernstein operator in the dot-product coordinate and to the three-sphere. No claim is made for the angular Bernstein operator on higher spheres, for strict positive-definiteness preservation, or for the converse threshold in sphere dimensions four and above. Searching literature and public mathematical records cannot certify historical priority exhaustively; independent scientific assessment has not been performed.

## References

1. M. Otten, N. Nguyen, T. W. Watts, *Preservation of Positive-Definiteness by Bernstein Operators on the Circle*, arXiv:2608.04836v1 (August 5, 2026), especially Section 4. https://arxiv.org/abs/2608.04836
2. R. K. Beatson and W. zu Castell, *Dimension hopping and families of strictly positive definite zonal basis functions on spheres*, arXiv:1510.08658v2 (2015), Sections 1–2. https://arxiv.org/abs/1510.08658
3. I. J. Schoenberg, *Positive definite functions on spheres*, Duke Math. J. **9** (1942), 96–108.
4. T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, Bernoulli **19** (2013), 1327–1349; arXiv:1111.7077. https://arxiv.org/abs/1111.7077
