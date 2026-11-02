# Degree-bounded mixed-moment obstruction for finite Blaschke pairs

## Finding

For every pair of nonconstant finite Blaschke products \(B,C\) of respective degrees \(d,e\ge1\), normalized by \(B(0)=C(0)=0\), the mixed boundary moments
\[
M_{m,n}=\int_{\mathbb T} B(\zeta)^m\overline{C(\zeta)^n}\,dm(\zeta)
\]
satisfy the explicit **finite and quantitative obstruction**
\[
\boxed{\max_{1\le m\le e,\;1\le n\le d}|M_{m,n}|\ge\frac{1}{de}.}
\]
Here \(dm(e^{i\theta})=d\theta/(2\pi)\) is normalized arc measure. Thus the first \(e\) positive powers of \(B\) cannot all be even approximately orthogonal to the first \(d\) positive powers of \(C\) beyond the degree-dependent numerical threshold.

The two rectangular exponent cutoffs are each unimprovable without extra hypotheses, even if arbitrary moments in the *other* exponent are permitted: for coprime positive integers \(d,e\), the choices \(B(z)=z^d\) and \(C(z)=z^e\) obey
\[
M_{m,n}=\mathbf 1_{\{dm=en\}}=\mathbf 1_{\{(m,n)=(e,d)\}}
\quad (1\le m\le e,\;1\le n\le d).
\]
In particular a universal assertion using only \(m\le e-1\), or only \(n\le d-1\), would be false. The factor \(1/(de)\) is attained for \(d=e=1\), but its optimality in general degrees is not asserted.

## Assumptions and scope

A finite Blaschke product of degree \(d\) is an analytic function of the form
\[
B(z)=\eta\prod_{j=1}^d\frac{z-a_j}{1-\overline{a_j}z},\qquad |\eta|=1,\quad a_j\in\mathbb D,
\]
with zeros counted with multiplicity. Its boundary values have modulus one everywhere on \(\mathbb T\), and it is analytic past the closed unit disk. Both products are required to vanish at zero; the degree of \(B\) is \(d\), and that of \(C\) is \(e\). The statement concerns only the specified mixed powers and normalized arc measure. It neither classifies independent infinite Blaschke products nor bounds their finite-degree approximants uniformly across unbounded degrees.

## Proof

**1. Bidegree-controlled algebraic dependence.** Write \(B(z)=p(z)/q(z)\) and \(C(z)=r(z)/s(z)\) in reduced polynomial fractions. The numerator degrees are \(\deg p=d\), \(\deg r=e\), while \(\deg q\le d\), \(\deg s\le e\); the denominators have no zeros in \(\overline{\mathbb D}\). Introduce two independent indeterminates \(u,v\) and the polynomial resultant
\[
R(u,v)=\operatorname{Res}_z\bigl(p(z)-u q(z),\;r(z)-v s(z)\bigr).
\]
The resultant is homogeneous of degree \(e\) in the coefficients of the first polynomial and degree \(d\) in those of the second. As every coefficient of the first polynomial has degree at most one in \(u\), and every coefficient of the second at most one in \(v\),
\[
\deg_u R\le e,\qquad \deg_v R\le d.
\]
This resultant is not the zero polynomial: fix a generic complex value \(u\). There are finitely many roots \(z\) of \(p(z)-u q(z)\); avoiding the finitely many corresponding values of \(C(z)\) when choosing \(v\), as well as the finite exceptional choices causing a loss of leading degree, gives polynomials with no common root. Hence their resultant is nonzero. Substituting \(u=B(z),v=C(z)\) makes \(z\) a common root, so \(R(B(z),C(z))=0\) for all \(z\in\mathbb D\).

Consequently the \(N=(e+1)(d+1)\) functions
\[
F_{jk}(z)=B(z)^jC(z)^k,\qquad 0\le j\le e,\quad0\le k\le d,
\]
are linearly dependent over \(\mathbb C\) in the Hardy space \(H^2(\mathbb D)\). By innerness each has squared norm \(\|F_{jk}\|_{H^2}^2=1\).

**2. Sparse off-diagonal Gram matrix.** For two distinct indices \((j,k)\) and \((j',k')\), their inner product is zero if both exponent differences are nonnegative or both are nonpositive, including cases where one difference is zero. Indeed, cancellation of the unimodular inner factors on \(\mathbb T\) then leaves the boundary integral of a nonconstant analytic product of positive powers of \(B\) and \(C\), or its conjugate; its constant term vanishes because \(B(0)=C(0)=0\). Nonzero off-diagonal entries are therefore possible only when \((j-j')(k-k')<0\), and they are then one of \(M_{m,n}\) or its conjugate for \(1\le m\le e,1\le n\le d\).

For a fixed index \((j,k)\), the number of indices with opposite-sign differences is exactly
\[
j(d-k)+(e-j)k\le de,
\]
where the inequality holds because the expression is affine in each of \(j\) and \(k\) on the rectangle and takes its maximum \(de\) at the corners \((e,0)\) and \((0,d)\). Thus each off-diagonal Gram row has at most \(de\) potentially nonzero entries.

**3. Forced nonzero correlation and quantitative bound.** Put
\[
\varepsilon=\max_{1\le m\le e,\;1\le n\le d}|M_{m,n}|.
\]
The Gram matrix \(G=(\langle F_{jk},F_{j'k'}\rangle)\) is Hermitian, has every diagonal entry equal to one, and satisfies \(\max_{(j,k)}\sum_{(j',k')\ne(j,k)}|G_{(j,k),(j',k')}|\le de\varepsilon\). Its singularity follows from the nontrivial resultant relation. If \(de\varepsilon<1\), the Gershgorin circle theorem (or the triangle inequality applied to a normalized null-vector's largest coordinate) makes \(G\) nonsingular, a contradiction. Hence \(de\varepsilon\ge1\), which proves the bound.

**4. Coordinatewise sharpness of the exponent cutoffs.** When \(B(z)=z^d,C(z)=z^e\), normalized Fourier orthogonality gives \(M_{m,n}=1\) exactly if \(dm=en\), and zero otherwise. If \(\gcd(d,e)=1\), the least strictly positive solution is \((m,n)=(e,d)\). Thus no smaller universal ceiling in either exponent can locate a nonzero moment for all such pairs. When \(d=e=1\), necessarily \(B(z)=\eta z\), \(C(z)=\xi z\) with unimodular constants, and \(|M_{1,1}|=1=1/(de)\).

## Verification

The argument is a complete analytic and algebraic proof for all positive integer degrees. Its only nontrivial algebraic input is the standard degree rule for resultants; its only operator estimate is strict diagonal dominance of a singular Gram matrix. A finite consistency check is reproducible without external packages: for \(B(z)=z^2,C(z)=z^3\), elimination of \(z\) from \(z^2=u,z^3=v\) gives \(R(u,v)=v^2-u^3\) up to sign. The unique nonzero mixed moment in the prescribed rectangle is \(M_{3,2}=1\), while the bound reads \(1/6\). Similarly, for every \(1\le d,e\le20\), the combinatorial row count \(j(d-k)+(e-j)k\) has maximum \(de\); the accompanying optional checker executes this finite cross-check. Neither finite check substitutes for the infinite-degree proof above.

## Relationship to prior work

Nakazi and Watanabe (2002), Proposition 1, proved the **qualitative** result that statistically independent inner functions cannot include a finite Blaschke product. That result already rules out perfect all-orders independence for this class. The present assertion instead identifies a **degree-controlled finite rectangle** where nonorthogonality must appear and supplies a **positive, uniform lower bound** for a mixed moment, with the exponent ceilings shown optimal by coprime monomials. The latter quantitative claim does not follow from the cited qualitative statement without further argument.

Fu, Guo, Li and Qiu (2026), first publicly posted October 21, construct statistically independent inner functions, even Blaschke products, with both functions vanishing at the origin. Their publicly accessible abstract identifies an infinite iterative existence construction. The finite-degree obstruction here quantifies an analytic distinction between those infinite constructions and pairs of prescribed finite degree. A complete comparison to the unaccessible 2026 full preprint remains outstanding; the current assertion is assessed against its accessible abstract rather than the entire paper. No claim is made that the qualitative impossibility is new.

## Limitations

The numerical coefficient \(1/(de)\) is guaranteed but is not asserted globally optimal when \(de>1\). The sharpness assertion applies to the rectangular exponent ceilings, not to the numerical constant. Both inner functions must have finite degree and vanish at zero. The proof gives no lower bound that is uniform in unbounded degrees, and no result for general nonrational inner functions. Historical or implicit appearances of the same quantitative argument in inaccessible literature remain possible; the most relevant 2026 full preprint could not be examined.

## References

1. X. Fu, K. Guo, D. Li and Y. Qiu, *On the existence of independent inner functions*, arXiv:2610.29198, version 1, first posted October 21, 2026. https://arxiv.org/abs/2610.29198
2. T. Nakazi and T. Watanabe, *Properties of a Rudin's orthogonal function which is a linear combination of two inner functions*, Scientiae Mathematicae Japonicae Online **7** (2002), 347–352, Proposition 1. https://www.jams.jp/scm/contents/Vol-7-5/7-41.pdf
