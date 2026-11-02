# Fourfold tangent multiplicity and three tangent-cone regimes for modular four-moment varieties

## Finding

Fix a prime \(p\geq 5\), an integer \(2\leq r<p\), and \(n=p+r\). Over \(k=\overline{\mathbb F}_p\), define the projective **four-moment complete intersection**
\[
X_{p,r}^{(4)}=\biggl\{[x_1:\cdots:x_n]\in\mathbb P_k^{n-1}:\ \sum_{i=1}^n x_i^j=0\quad (1\leq j\leq 4)\biggr\}.
\]
It is a geometrically integral normal complete intersection of multidegree \((1,2,3,4)\), degree \(24\), and dimension \(n-5\). The support of its geometric singular locus consists of **exactly** \(\binom{n}{p}\) points. These are the projective coordinate permutations of the vector with exactly \(p\) entries equal to \(1\) and exactly \(r\) entries equal to \(0\). All are rational over \(\mathbb F_p\).

At every singular point \(P\), the associated graded ring of the local ring is
\[
\operatorname{gr}_{\mathfrak m_P}\mathcal O_{X_{p,r}^{(4)},P}
 \cong
 k[u_1,\ldots,u_{p-2},v_1,\ldots,v_{r-1}]/(q_{p-2}(\mathbf u),q_{r-1}(\mathbf v)),
\]
where
\[
q_m(z_1,\ldots,z_m)=\sum_{i=1}^m z_i^2+\biggl(\sum_{i=1}^m z_i\biggr)^2.
\]
These are nondegenerate quadratic forms of ranks \(p-2\) and \(r-1\), respectively. Thus every singular point has **Hilbert–Samuel multiplicity \(4\)**. The tangent cone is nonreduced when \(r=2\), reduced but reducible when \(r=3\), and geometrically integral and normal when \(4\leq r<p\). The statement about the singular locus is **set-theoretic**, not an assertion that its Jacobian singular scheme is reduced.

## Assumptions and scope

The base field \(k\) is algebraically closed of prime characteristic \(p\geq5\). The number of variables is \(p+r\), with \(2\leq r<p\). The defining equations are precisely the first four *consecutive* ordinary power sums with zero right-hand sides; all coordinates have unit coefficient. Tangent cone means \(\operatorname{Spec}\operatorname{gr}_{\mathfrak m_P}\mathcal O_{X,P}\), with its full scheme structure. Geometric integrality and normality refer to the projective variety over \(k\).

## Proof

**Regularity and degree.** Write \(e_j\) for the elementary symmetric polynomials and \(s_j=\sum_i x_i^j\). Newton identities imply successively that \(s_1,\ldots,s_4\) and \(e_1,\ldots,e_4\) generate the same ideal, because \(1,2,3,4\) are units in \(k\). The symmetric polynomial algebra is the polynomial ring \(k[e_1,\ldots,e_n]\), and \(k[x_1,\ldots,x_n]\) is free (in particular flat) over it. Hence \(e_1,\ldots,e_4\), and therefore \(s_1,\ldots,s_4\), form a regular sequence. Their projective zero locus has dimension \(n-5\) and degree \(1\cdot2\cdot3\cdot4=24\).

**Entire singular support.** The Jacobian matrix has entries \(j x_i^{j-1}\) for \(1\leq j\leq4\). Since the integers \(1,\ldots,4\) are units, its rank is the minimum of \(4\) and the number of distinct coordinate values, by the Vandermonde minors. Thus a singular point has at most three distinct coordinate values. Denote its distinct *nonzero* values by \(t_1,\ldots,t_s\), where \(s\leq3\), with integer multiplicities \(m_1,\ldots,m_s\). The first \(s\) power-sum equations become \(\sum_{h=1}^s m_h t_h^j=0\) for \(1\leq j\leq s\). Their coefficient determinant is nonzero, equal up to sign to \((\prod_h t_h)\prod_{a<b}(t_b-t_a)\). Consequently \(m_h=0\) in \(k\), i.e. \(p\mid m_h\), for all \(h\). As \(p\leq n<2p\), there is exactly one nonzero coordinate value, occurring exactly \(p\) times; all other \(r\) coordinates vanish. Projective scaling makes the nonzero value \(1\). Conversely these indicator points satisfy all four equations, and their Jacobian has rank \(2\), so they are singular. Distinct supports give distinct projective points, accounting for \(\binom{n}{p}\) points.

**Global normality and irreducibility.** The complete intersection is Cohen–Macaulay, hence satisfies Serre's \(S_2\). Its singular support is finite, and its dimension \(n-5\geq2\), so it is regular in codimension one (\(R_1\)). It is therefore normal. Positive-dimensional projective complete intersections are connected; a connected normal Noetherian scheme is irreducible. Thus \(X_{p,r}^{(4)}\) is geometrically integral and normal.

**Local equations and associated graded ring.** By permutation symmetry, take \(P=[1:\cdots:1:0:\cdots:0]\), with \(p\) ones. In the affine chart where the first \(1\) stays \(1\), write the remaining \(p-1\) former ones as \(1+a_i\) and the \(r\) former zeroes as \(b_j\). Set \(L_a=\sum a_i\), \(L_b=\sum b_j\), \(U=\sum a_i^2\), \(V=\sum b_j^2\). Because \(p=0\) in \(k\), the constant terms of all four equations vanish; their linear terms are \(jL_a\) for \(j=1,2,3,4\), except the first equation has \(L_a+L_b\). Hence the first two equations have independent linear terms and can be eliminated formally; their tangent linear equations imply \(L_a=L_b=0\).

Let \(F_j\) denote the local \(j\)-th moment equation, and take two remaining defining equations
\[
G_3=F_3-\tfrac32 F_2,\qquad G_4=F_4-2F_3+F_2.
\]
Their quadratic initial terms on the common tangent linear subspace are, respectively,
\[
\tfrac32(U-V),\qquad U+V.
\]
The change-of-basis matrix from \((U,V)\) has determinant \(3\), which is nonzero in characteristic \(p\geq5\). Thus their quadratic initial ideal is exactly \((U,V)\), modulo the first two linear equations. Solving \(L_a=L_b=0\) expresses one of the \(p-1\) variables \(a_i\), and one \(b_j\), as minus the sum of the others. The restrictions of \(U,V\) become \(q_{p-2}(\mathbf u)\) and \(q_{r-1}(\mathbf v)\), respectively. Their Gram matrices are \(I_m+J_m\), with determinant \(m+1\); these determinants equal \(p-1=-1\ne0\) and \(r\ne0\), respectively, in \(k\).

The forms \(q_{p-2},q_{r-1}\) are a homogeneous regular sequence in disjoint sets of variables: the first is irreducible since its rank \(p-2\geq3\), and the second is nonzero in the quotient domain. The two independent linear initial forms followed by these quadratic initial forms are a homogeneous regular sequence. By the filtered regular-sequence (initial-form) criterion, the associated graded quotient is precisely the quotient by these four initial forms, giving the displayed tangent-cone ring with no unaccounted initial equations. The local multiplicity is the product of the initial degrees of the remaining forms, namely \(2\cdot2=4\).

**Three tangent-cone regimes.** For \(r=2\), the second form has rank \(1\) and is the square of a linear form up to a unit, so the cone is nonreduced. For \(r=3\), the nondegenerate binary quadratic factors into two *distinct* linear forms over \(k\), giving a reduced union of two irreducible components. For \(r\geq4\), both forms have rank at least \(3\); each defines a geometrically integral normal affine quadric cone (the singularity of such a cone has codimension at least \(2\)), and the product of these two cones over the algebraically closed field is geometrically integral and normal. This proves the trichotomy.

## Verification

Run `python3 checks/verify.py` from the directory containing the accompanying checker. It uses only the Python standard library. It verifies the quadratic jet identities and Gram determinants at nine parameter pairs (characteristics \(5,7,11\) and \(r=2,3,4\)); it independently enumerates all projective \(\mathbb F_5\)-points in the two smallest cases and checks that the singular points among solutions coincide exactly with the predicted \(21\) and \(56\) indicator points. Successful output ends with `VERIFY_OK`. Finite-field enumeration checks only rational points, and these computations do not substitute for the general proof over \(\overline{\mathbb F}_p\).

## Relationship to prior work

Giménez, Gottig, Palacios, Pérez and Privitelli study the geometry and arithmetic of power-sum varieties over finite fields [1]. Their regular-sequence results encompass the broad complete-intersection background here, while the characteristic hypothesis in the published normality criterion for four consecutive moments is \(p>n-2\), which fails throughout the present range \(n=p+r\), \(r\geq2\). The exact finite singular support, multiplicity-four tangent cones and three degeneration regimes here are not deductions from that normality criterion. Conca, Krattenthaler and Watanabe [2] study regular sequences of symmetric power sums, supplying a characteristic-zero point of comparison, but not the asserted modular local geometry. This work builds on the established literature rather than claiming the regular-sequence observation as novel.

## Limitations

The singular locus is classified set-theoretically, not with the full scheme structure of the Jacobian ideal. The theorem does not determine higher-order completed analytic normal forms, exceptional resolutions, or \(r=1\), where the second quadratic block disappears. It applies only to the first four unit-weight moments in prime characteristic at least five, with \(p<n<2p\). The existence of earlier implicit descriptions of these local singularities cannot be excluded by the literature search alone. Independent mathematical validation has not been performed.

## References

[1] N. Giménez, J. F. Gottig, M. Palacios, M. Pérez and M. Privitelli, *Power Sum Varieties over Finite Fields*, arXiv:2610.32056v1 (first public version October 23, 2026). https://arxiv.org/html/2610.32056v1 .

[2] A. Conca, C. Krattenthaler and J. Watanabe, *Regular sequences of symmetric polynomials*, arXiv:0801.2662 (2008); Rend. Sem. Mat. Univ. Padova **121** (2009), 179–199. https://arxiv.org/abs/0801.2662 .
