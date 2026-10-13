# Characteristic-three finite-plane specializations of two free conic–line arrangements

## Finding

Two conic–line arrangements of Pokora undergo a related arithmetic specialization: the characteristic-\(3\) reductions of his \(\mathcal{CL}_{15}\) and \(\mathcal{CL}_{16}\) become the full \(13\)-line arrangement of \(\mathbb P^2(\mathbb F_3)\) with two or one lines removed. They remain reduced and logarithmically free, but their homogeneous free-basis degrees change from the characteristic-zero values.

Writing \(n_m\) for the number of geometric points where exactly \(m\) distinct lines meet, the reductions have the following exact incidence spectra:

| Integral arrangement | Removed \(\mathbb F_3\)-lines | Number of reduced components | \((n_2,n_3,n_4)\) | Logarithmic exponents in characteristic \(3\) |
| --- | --- | ---: | --- | --- |
| \(\mathcal{CL}_{15}\) | \(z=0\), \(x+y=0\) | \(11\) | \((1,6,6)\) | \((1,3,7)\) |
| \(\mathcal{CL}_{16}\) | \(x+y=0\) | \(12\) | \((0,4,9)\) | \((1,3,8)\) |

In both cases, the entire geometric singular support consists of the \(13\) rational points of \(\mathbb P^2(\mathbb F_3)\). Here *ordinary* means an arrangement of distinct transverse line branches, and freeness refers to the module of derivations logarithmic along the reduced divisor.

## Assumptions and scope

Let \(\mathbb Z[x,y,z]\) be the homogeneous coordinate ring and define

\[
q=-x^2+xy-y^2+z^2,\qquad
L=xy(x-z)(x+z)(y+z)(y-z)(y-x-z)(y-x+z)(y-x).
\]

Set \(F_{15}=Lq\) and \(F_{16}=zLq\). These are the source's explicitly printed defining polynomials for \(\mathcal{CL}_{15}\) and \(\mathcal{CL}_{16}\), of respective degrees \(11\) and \(12\). All positive-characteristic statements concern their fixed coefficientwise reductions over \(\mathbb F_3\), and hence hold geometrically over any algebraic extension of that field. There is no assertion about different integral presentations, other characteristics, or freeness of a nonreduced divisor.

Let \(\mathcal P\) be the projective collection of \(13\) distinct linear forms \(a x+b y+c z\) with \([a:b:c]\in\mathbb P^2(\mathbb F_3)\), up to nonzero scalar. Let \(H\) denote \(x+y\). A logarithmic derivation is a polynomial vector field \(\theta\) satisfying \(\theta(\ell)\in(\ell)\) for each defining linear form \(\ell\); its degree is the common homogeneous coefficient degree.

## Proof

**1. The two special fibers are projective-plane deletions.** In characteristic \(3\),

\[
q=z^2-(x+y)^2=(z-x-y)(z+x+y).
\]

Define

\[
P=y(y+z)(y-z)(y-x-z)(y-x+z)(y-x)(z-x-y)(z+x+y).
\]

The reduced specializations are exactly

\[
f_{15}=x(x-z)(x+z)P,\qquad f_{16}=z f_{15}.
\]

All \(11\) or \(12\) indicated linear factors are pairwise nonproportional over \(\mathbb F_3\). Enumerating the nonzero coefficient triples in \(\mathbb F_3^3\) modulo scalar gives \(13\) projective classes, and their complements relative to the factors of \(f_{15}\), respectively \(f_{16}\), are precisely \(\{z,H\}\), respectively \(\{H\}\). Thus these are the claimed deletions, not merely arrangements with the same line counts.

**2. All singularities and incidence counts.** The full projective plane of order \(3\) has \(13\) points and \(13\) lines; each point belongs to \(4\) lines, and each line contains \(4\) points. After removing \(H\), its four points have multiplicity \(3\), while the other nine retain multiplicity \(4\). This yields \((n_2,n_3,n_4)=(0,4,9)\). Removing the additional line \(z\), exactly one point \(H\cap\{z=0\}\) loses two incidences, six other points lose one incidence, and six points lose none. Hence \((n_2,n_3,n_4)=(1,6,6)\). Every pair of lines with coefficients in \(\mathbb F_3\) meets at an \(\mathbb F_3\)-point; all \(13\) such points still have multiplicity at least two, so there are no further geometric singularities. As checks, \(4\cdot3+9\cdot6=66=\binom{12}{2}\) and \(1+6\cdot3+6\cdot6=55=\binom{11}{2}\).

**3. A free basis for the \(12\)-line fiber.** Work in \(S=\mathbb F_3[x,y,z]\). Set

\[
E=x\partial_x+y\partial_y+z\partial_z,\quad
D=x^3\partial_x+y^3\partial_y+z^3\partial_z,\quad
T_8=P\partial_y.
\]

The first two are logarithmic along every \(\mathbb F_3\)-rational line: for \(\ell=ax+by+cz\), the identities are \(E(\ell)=\ell\) and \(D(\ell)=\ell^3\). The last is logarithmic along all factors of \(f_{16}\): if the coefficient of \(y\) in \(\ell\) vanishes, then \(T_8(\ell)=0\), and all other factors divide \(P\). Direct expansion gives

\[
\det\begin{pmatrix}x&x^3&0\\y&y^3&P\\z&z^3&0\end{pmatrix}
=xz(x^2-z^2)P=f_{16}.
\]

Saito's criterion, valid over arbitrary fields for central hyperplane arrangements, proves that these fields form a basis of the logarithmic module of polynomial degrees \((1,3,8)\).

**4. A free basis for the \(11\)-line fiber.** Define \(B=-y^2(y-x)^2(x+y)\in S\). The exact identity

\[
P(x,y,0)=B\,y(y^2-x^2)
\]

implies that all coefficients of \(T_8+B(x^2E-D)\) are divisible by \(z\). Consequently,

\[
T_7=\frac{T_8+B(x^2E-D)}{z}
\]

is a polynomial derivation of homogeneous degree \(7\). Its numerator is logarithmic along the \(12\) lines, and division by \(z\) preserves logarithmicity along the remaining \(11\) coprime defining linear forms. Moreover,

\[
\det(E,D,T_7)=\det(E,D,T_8)/z=f_{15}.
\]

A second application of Saito's criterion gives a homogeneous logarithmic basis \((E,D,T_7)\) of degrees \((1,3,7)\).

**5. Comparison with characteristic zero.** The originating work proves that the complex curves \(F_{15}=0\) and \(F_{16}=0\) are free, both with minimal degree of a Jacobian relation \(4\). Since the polynomial degrees are \(11\) and \(12\), their characteristic-zero logarithmic basis degrees are \((1,4,6)\) and \((1,4,7)\). The characteristic-\(3\) exponents obtained above are therefore genuinely different. For \(f_{16}\), the total degree \(12\) is divisible by \(3\), so Euler's derivation itself annihilates \(f_{16}\); no characteristic-zero inference about minimal Jacobian syzygy degree is imported into that exceptional characteristic.

## Verification

The accompanying `verify.py` performs exact coefficient arithmetic over \(\mathbb F_3\), not floating-point sampling. It checks the original polynomial reductions, enumerates all \(13\) projective line classes and \(13\) projective point classes, certifies the exact missing-line sets and all \(\binom{12}{2}\) and \(\binom{11}{2}\) pairwise line intersections, tests that each of the six displayed derivations is logarithmic along its claimed factorization, and verifies both determinant identities. Execute with `python3 verify.py`; only the Python standard library is needed. The fully symbolic proof above establishes the universal geometric statement over the algebraic closure.

## Relationship to prior work

Pokora's first public arXiv version (December 20, 2023), Section 3, constructs both complex free conic–line arrangements and prints their equations and numerical data. The present statement does **not** claim those complex arrangements, their characteristic-zero freeness, or the abstract finite projective plane as discoveries. It identifies the *specific* characteristic-\(3\) reductions of those two integral models with the one- and two-line deletions of the complete ternary projective-plane arrangement, proves their singular-point spectra, and exhibits characteristic-\(3\) logarithmic bases and changed exponents. Palezzato–Torielli explain general characteristic-dependent exponent phenomena and Saito's criterion, but their reported examples do not assert these two identifications.

## Limitations

Only the fixed integral models and characteristic \(3\) are classified; there is no statement about other reduction primes or projectively transformed integral models. The \(13\) rational points are the geometric singular *support*, not a calculation of singular-scheme lengths. The free-basis exponents concern logarithmic derivations, not a claim that the characteristic-zero Jacobian-syzygy relation applies when the degree is divisible by the characteristic. An unindexed prior computation or observation of these modular identifications may exist. No independent scientific audit has been performed.

## References

1. P. Pokora, *Freeness of arrangements of lines and a conic with ordinary quasi-homogeneous singularities*, arXiv:2312.13052v1, first public 2023-12-20, Section 3 (equations for the two arrangements): https://arxiv.org/html/2312.13052v1 .
2. E. Palezzato and M. Torielli, *Free hyperplane arrangements over arbitrary fields*, arXiv:1803.09908v1, especially Section 3, Theorem 3.7 (Saito's criterion in all characteristics): https://arxiv.org/html/1803.09908v1 .
