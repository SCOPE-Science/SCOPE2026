# Quadratic multiplication-rank spectra of two-variable monomial complete intersections

## Finding

Let \(m\ge 3\), let \(q=p^f\) be a prime power, and put \(A=\mathbb F_q[x,y]/(x^m,y^m)\). For every \((a,b,c)\in\mathbb F_q^3\), let \(L_{a,b,c}\) be multiplication by \(Q=ax^2+bxy+cy^2\) on the complete, ungraded underlying vector space of \(A\). Write \(m_0=m/p^{v_p(m)}\) and
\[
 h_{m,q}=\frac{\gcd(m_0,q-1)+\gcd(m_0,q+1)}2-\mathbf1_{p\nmid m},\qquad
 B_{m,q}=2(q-1)+(q-1)^2 h_{m,q}.
\]
Then \(h_{m,q}\) is a nonnegative integer, and the entire multiplication-rank enumerator is
\[
 \boxed{\sum_{(a,b,c)\in\mathbb F_q^3}T^{\operatorname{rank}L_{a,b,c}}
 =1+B_{m,q}T^{(m-1)^2-1}+(q^3-1-B_{m,q})T^{(m-1)^2}.}
\]
In particular, apart from the zero form, **exactly two adjacent ranks occur**, and the count of the exceptional rank is controlled by the arithmetic of \(m\)-th roots of unity in groups of orders \(q-1\) and \(q+1\). No characteristic restrictions are imposed.

## Assumptions and scope

The algebra is standard graded by total degree, with homogeneous components \(A_d\). All coefficients of \(Q\) range independently over the base finite field, including zero; hence the enumerator has \(q^3\) terms counted with multiplicity. The operator is multiplication on all \(m^2\) dimensions, not merely on the middle graded component. The \(p\)-free part \(m_0\) is the unique positive divisor of \(m\) not divisible by \(p\) such that \(m/m_0\) is a power of \(p\). The conventions include \(v_p(m)=0\) if \(p\nmid m\).

## Proof

**1. Only the central graded map can lose rank.** The Hilbert function is \(\dim A_d=d+1\) for \(0\le d\le m-1\), and \(\dim A_d=2m-1-d\) for \(m\le d\le 2m-2\); all other pieces vanish. If \(Q\ne0\) and \(0\le d\le m-3\), then \(L_Q:A_d\to A_{d+2}\) is injective: before degree \(m\), reduction modulo \((x^m,y^m)\) does not affect \(Qf\), and polynomial multiplication by nonzero \(Q\) is injective. The socle multiplication pairing \(A_d\times A_{2m-2-d}\to A_{2m-2}\cong\mathbb F_q\) is perfect, pairing monomials with complementary exponents. Thus multiplication maps in complementary degrees are transposes, so all maps in degrees \(d\ge m-1\) are surjective. Only \(L_Q:A_{m-2}\to A_m\), a square map of order \(m-1\), can fail maximal rank. Summing the maximal possible block ranks gives \(2\sum_{i=1}^{m-2}i+(m-1)=(m-1)^2\).

**2. Its rank drops by at most one.** With monomial bases in increasing powers of \(x\), the central map has tridiagonal Toeplitz matrix of size \(m-1\), with main diagonal \(b\) and its two adjacent diagonals \(a,c\) (their positions depend on basis orientation). If \(a\ne0\) or \(c\ne0\), a homogeneous three-term recurrence shows that a kernel vector is determined by at most one initial coordinate. If \(a=c=0\) and \(Q\ne0\), then \(b\ne0\) and the matrix is invertible. Consequently a vanishing determinant is equivalent to nullity exactly one. Let \(D_j\) be its order-\(j\) leading determinant. Laplace expansion gives \(D_0=1\), \(D_1=b\), \(D_j=bD_{j-1}-acD_{j-2}\), and the exceptional forms are precisely those satisfying \(D_{m-1}=0\).

**3. Count the exceptional forms with \(ac=0\).** Here \(D_{m-1}=b^{m-1}\), so \(b=0\). Excluding \((a,b,c)=(0,0,0)\), this leaves exactly \(2(q-1)\) forms, with either \(a\ne0,c=0\) or \(a=0,c\ne0\).

**4. Count the exceptional forms with \(ac\ne0\).** Let \(z=ac\in\mathbb F_q^\times\) and let \(\lambda,\mu\) be the roots in an algebraic closure of \(u^2-bu+z\). If \(\lambda\ne\mu\), the determinant recurrence gives \(D_{m-1}=(\lambda^m-\mu^m)/(\lambda-\mu)\). Therefore the determinant vanishes precisely when \(\xi=\lambda/\mu\ne1\) is an \(m\)-th root of unity. If \(\lambda=\mu\), the recurrence gives \(D_{m-1}=m\lambda^{m-1}\), so the repeated-root parameter contributes precisely when \(p\mid m\). All roots of unity of order dividing \(m\) equal those of order dividing \(m_0\), because the field has characteristic \(p\).

For any such \(\xi\), put \(t=b^2/(ac)=(\xi+1)^2/\xi=\xi+\xi^{-1}+2\). This invariant is unchanged under \(\xi\leftrightarrow\xi^{-1}\). Conversely, \(\xi\) is a root of \(X^2-(t-2)X+1\), so each fiber of \(\xi\mapsto t\) is precisely one inversion orbit, including the fixed points. As \(\xi\) is a root of unity, \(t\in\mathbb F_q\) if and only if \(\xi^q=\xi\) or \(\xi^q=\xi^{-1}\), equivalently \(\xi^{q-1}=1\) or \(\xi^{q+1}=1\). Denote their two subsets of \(\mu_{m_0}\) by \(U\) and \(W\). The cardinalities are \(|U|=\gcd(m_0,q-1)\) and \(|W|=\gcd(m_0,q+1)\). Their intersection consists solely of inversion-fixed roots, because \(\gcd(q-1,q+1)\mid2\). Therefore the number of inversion orbits in \(U\cup W\) equals \((|U|+|W|)/2\): every non-fixed orbit contributes two elements to the sum, while each fixed orbit occurs in both sets. Delete the orbit \(\xi=1\) if \(p\nmid m\), but retain it if \(p\mid m\). This gives exactly \(h_{m,q}\) allowed values of \(t\).

For each allowed \(t\in\mathbb F_q\), precisely \((q-1)^2\) triples \((a,b,c)\) with \(ac\ne0\) satisfy \(b^2/(ac)=t\). If \(t=0\), choose \(b=0\), then choose \(a,c\) independently nonzero. If \(t\ne0\), choose \(a,b\) independently nonzero, with unique \(c=b^2/(at)\). Hence there are \((q-1)^2h_{m,q}\) exceptional triples with \(ac\ne0\).

**5. Complete the rank enumerator.** The preceding cases give \(B_{m,q}=2(q-1)+(q-1)^2h_{m,q}\) exceptional nonzero forms. Every other nonzero form has full possible rank \((m-1)^2\), the exceptional forms have rank one less, and the zero form has rank zero. This proves the formula and its integrality simultaneously. All arguments hold in characteristic two, including when the repeated-root parameter is \(t=0\).

## Verification

Execute `python3 VERIFY.py` in the same directory as this result. The dependency-free verifier enumerates all \(q^3\) coefficient triples and independently evaluates the central determinant recurrence for finite fields of orders \(2,3,4,5,7,8,11,13\), with \(3\le m\le60\) (464 cases). It also constructs the entire graded multiplication operator directly, row-reduces over the corresponding finite field, and compares the rank distributions for a separate collection of smaller \((m,q)\). Successful execution prints `VERIFY_OK_QUADRATIC_LEFSCHETZ`. These finite computations are corroboration, not substitutes for the unrestricted proof above.

## Relationship to prior work

The rank problem belongs to the Lefschetz theory of Artinian complete intersections. Cook (arXiv:1111.4979) studies strong and weak Lefschetz properties of monomial complete intersections in positive characteristic, principally for multiplication by powers of linear forms; this does not enumerate the ranks of multiplication by every arbitrary quadratic coefficient triple over every finite field. Boij–Migliore–Miró-Roig–Nagel (arXiv:1609.00952) study non-Lefschetz **linear** forms, and Marangone (arXiv:2404.16238) studies the **conic** non-Lefschetz locus, principally for general ternary characteristic-zero complete intersections, without an all-field two-variable rank enumerator. Numata (arXiv:2002.12649) gives determinants for multiplication by products of linear forms in two-variable monomial complete intersections, a closely related and potentially stronger determinant-level predecessor. The tridiagonal determinant recurrence and characteristic-root identities are classical. The specific arithmetic fiber count for all degree-two forms, using both split and nonsplit Frobenius tori and exceptional repeated roots, is the contribution asserted here; no claim of invention of these preceding techniques is made.

## Limitations

The formula concerns only homogeneous quadratic multiplication in the explicitly named balanced two-variable monomial complete intersections, not arbitrary degree-two deformations, higher embedding dimension, or higher-degree forms. The comparison with Numata's determinant paper rests on its verified abstract rather than an inspection of its full text, so an equivalent formulation within it or in specialist Toeplitz enumerations remains a bibliographic risk. Literature searches do not establish absolute novelty. All claimed proofs are mathematical arguments, not independently audited certificates; no independent audit has been performed.

## References

1. David Cook II, *The Lefschetz properties of monomial complete intersections in positive characteristic*, arXiv:1111.4979v1 (first public 2011-11-21).
2. Mats Boij, Juan Migliore, Rosa Miró-Roig, and Uwe Nagel, *The non-Lefschetz locus*, arXiv:1609.00952v1 (2016).
3. Emanuela Marangone, *The non-Lefschetz locus of conics*, arXiv:2404.16238v1 (2024).
4. Yasuhide Numata, *On the determinant of multiplication map of a monomial complete intersection ring*, arXiv:2002.12649v1 (2020).
5. Somphong Jitman and Yosita Sricharoen, *Determinants of tridiagonal matrices over some commutative finite chain rings*, DOI:10.1515/spma-2023-0114 (2024).
