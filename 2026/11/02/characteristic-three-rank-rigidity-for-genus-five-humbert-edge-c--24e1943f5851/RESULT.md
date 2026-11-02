# Characteristic-three rank rigidity for genus-five Humbert–Edge curves

## Finding

Let \(k\) be an algebraically closed field of characteristic \(3\). For distinct \(\lambda,\mu\in k\setminus\{0,1\}\), let \(C_{\lambda,\mu}\) be the smooth complete intersection in \(\mathbf P^4_k\) given by
\[
\begin{aligned}
X_1^2+X_2^2+X_3^2&=0,\\
\lambda X_1^2+X_2^2+X_4^2&=0,\\
\mu X_1^2+X_2^2+X_5^2&=0.
\end{aligned}
\]
This is a genus-five Humbert–Edge curve with its five branch points ordered as \((\infty,0,1,\lambda,\mu)\). Let \(f(C)\) denote its Jacobian \(3\)-rank and \(a(C)=\dim_k\operatorname{Hom}(\alpha_3,J(C)[3])\) its \(a\)-number.

**Theorem.** Exactly two pairs of invariants occur:
\[
(f(C_{\lambda,\mu}),a(C_{\lambda,\mu}))=
\begin{cases}
(4,1),& (\lambda+1)(\mu+1)(\lambda+\mu)(\lambda+\mu+1)
(\lambda\mu+\lambda+\mu)=0,\\
(5,0),&\text{otherwise.}
\end{cases}
\]
On the ordered parameter surface
\[
U=\{(\lambda,\mu)\in\mathbf A^2_k:\lambda\mu(\lambda-1)(\mu-1)(\lambda-\mu)\ne0\},
\]
the nonordinary locus is the **disjoint union of five smooth curves**
\[
\lambda+1=0,\quad \mu+1=0,\quad \lambda+\mu=0,\quad
\lambda+\mu+1=0,\quad \lambda\mu+\lambda+\mu=0.
\]
Each component is isomorphic to \(\mathbf P^1\setminus\{\infty,0,1,-1\}\). Hence the Jacobian Newton slopes are exactly either \(0^{\times5},1^{\times5}\) or \(0^{\times4},(1/2)^{\times2},1^{\times4}\). In particular, no curve in this family has \(3\)-rank at most \(3\), and none is supersingular.

For every integer \(m\ge2\), set \(q=3^m\). Among ordered normalized parameter pairs \((\lambda,\mu)\in U(\mathbf F_q)\), exactly
\[
5(q-3)\quad\text{give }(f,a)=(4,1),\qquad
(q-3)(q-7)\quad\text{give }(f,a)=(5,0).
\]
These are **parameter-pair counts**, not counts of abstract isomorphism classes. For \(q=9\) the respective counts are \(30\) and \(12\); for \(q=27\) they are \(120\) and \(480\).

## Assumptions and scope

The base field is algebraically closed of characteristic exactly \(3\) for the geometric statement. The parameters \(\lambda,\mu\) are distinct and neither equals \(0\) nor \(1\); no assertion is made on the discriminant boundary. Finite-field counts require ordered, individually rational branch points and the indicated normalization. The curves are smooth and geometrically integral because the four square classes \(t,t-1,t-\lambda,t-\mu\) are independent in \(k(t)^*/k(t)^{*2}\), and because the resulting tame multiquadratic cover is smooth with five distinct branch points. More explicitly, the three quadrics form the canonical diagonal model of the function field
\[
k(t)(\sqrt t,\sqrt{t-1},\sqrt{t-\lambda},\sqrt{t-\mu}).
\]
The projection is \(t=-X_2^2/X_1^2\). The cover has Galois group \((\mathbf Z/2\mathbf Z)^4\), degree \(16\), and branch points \(\infty,0,1,\lambda,\mu\), each with inertia order \(2\). Riemann–Hurwitz gives \(2g(C)-2=-32+5\cdot8=8\), hence \(g(C)=5\).

## Proof

**1. Five elliptic quotients and a prime-to-three isogeny.** Let \(G=(\mathbf Z/2\mathbf Z)^4\) be the sign-change group of the cover, and let \(s_1,\dots,s_5\) denote inertia at the five branch points. These involutions satisfy \(s_1\cdots s_5=1\); any four form a basis. A nontrivial character \(\chi:G\to\{\pm1\}\) has an even number of negative values among the five \(s_i\). There are ten characters negative at precisely two branch points and five characters negative at precisely four. The corresponding double quotients have genus \(0\) and \(1\), respectively, by Riemann–Hurwitz. Write \(E_i\), for \(1\le i\le5\), for the genus-one quotient associated with the character whose four negative inertia elements are all but the \(i\)-th. Its double cover of \(\mathbf P^1\) is branched at that four-point subset.

Let \(\pi_i:C\to E_i\) be the quotient map, of degree \(8\), and consider
\[
\Phi=\sum_i\pi_i^*:\prod_{i=1}^5J(E_i)\longrightarrow J(C),
\qquad\Psi=(\pi_{1*},\ldots,\pi_{5*}).
\]
For \(i=j\), the norm/pullback identity gives \(\pi_{i*}\pi_i^*=[8]\). For \(i\ne j\), choose \(h\in\ker(\chi_i)\) with \(\chi_j(h)=-1\). The norm \(\pi_{i*}\) is invariant under \(h\), whereas \(h\) acts as negation on \(\pi_j^*J(E_j)\); hence \(\pi_{i*}\pi_j^*=0\) (a connected abelian image cannot be killed by \(2\)). Therefore \(\Psi\Phi=[8]\) diagonally. Since source and target both have dimension \(5\), \(\Phi\) is an isogeny, with kernel killed by \(8\). Its kernel is thus prime to \(3\), and it identifies the \(3\)-divisible groups of the product and of \(J(C)\). Both \(3\)-rank and \(a\)-number are additive across the five elliptic quotients.

**2. The unique supersingular fourth branch point.** Given three distinct points of \(\mathbf P^1_k\), a unique projective linear coordinate sends them to \(\infty,0,1\). A fourth point is then some \(r\in k\setminus\{0,1\}\), and the resulting elliptic double cover has Legendre equation
\[
y^2=x(x-1)(x-r).
\]
In characteristic \(3\), the Hasse invariant is the coefficient of \(x^2\) in \(x(x-1)(x-r)\), namely \(-1-r\). Hence the elliptic curve is supersingular exactly when \(r=-1\); otherwise it is ordinary. Thus **a fixed triple of branch points has exactly one possible supersingular fourth point**. Any two four-element subsets of a five-element set share a triple. If both gave supersingular quotients, their fourth points would therefore coincide, contradicting distinctness. Consequently at most one of the five \(E_i\) is supersingular. Each ordinary elliptic factor contributes \((f,a)=(1,0)\), and a supersingular factor contributes \((0,1)\), proving that the pair for \(C\) is either \((5,0)\) or \((4,1)\).

**3. Equations of the five divisors.** Applying the preceding Legendre criterion to the four-point subsets obtained by omitting respectively \(\mu,\lambda,1,0,\infty\) gives
\[
\begin{array}{c|c}
\text{omitted point}&\text{supersingular condition}\\\hline
\mu&\lambda=-1\\
\lambda&\mu=-1\\
1&\mu=-\lambda\\
0&\mu-1=-(\lambda-1)\\
\infty&\lambda(\mu-1)=-\mu(\lambda-1).
\end{array}
\]
In characteristic \(3\), these are precisely the five displayed equations. In the last row, the cross-ratio equation simplifies to \(\lambda\mu+\lambda+\mu=0\). The uniqueness of the supersingular completion of a triple proves pairwise disjointness of the divisors **at every geometric point of \(U\)**. Each equation is a line or a rational graph parametrized by one of \(\lambda,\mu\); in all five cases the permitted parameter values are exactly \(k\setminus\{0,1,-1\}\). This proves the component structure and the complete geometric stratification.

**4. Uniform finite-field counts.** Over \(\mathbf F_q\), the number of ordered normalized parameter pairs is \((q-2)(q-3)\): first select \(\lambda\notin\{0,1\}\), then \(\mu\notin\{0,1,\lambda\}\). Each of the five disjoint nonordinary components contains exactly \(q-3\) rational parameter points, as all its parametrizations are defined over \(\mathbf F_3\). Subtraction yields \(5(q-3)\) nonordinary pairs and \((q-3)(q-7)\) ordinary pairs, for every \(q=3^m\) with \(m\ge2\). The stated Newton slopes follow from the prime-to-three elliptic decomposition.

## Verification

The standalone verifier `verify_loci.py` checks in characteristic \(3\), for every one of the ten pairs of proposed divisor equations \(D_i,D_j\), that
\[
(D_i,D_j,z\lambda\mu(\lambda-1)(\mu-1)(\lambda-\mu)-1)=(1).
\]
This Gröbner ideal certificate excludes *all* common geometric points in \(U\), not merely points over a tested finite field. Running with SymPy 1.14.0 produced `PAIRWISE_SATURATION_OK 10` and `COUNT_POLYNOMIAL_OK`.

The independent, standard-library-only verifier `verify_finite_fields.py` constructs \(\mathbf F_9\) and \(\mathbf F_{27}\) from irreducible polynomials, directly normalizes each four-point cross ratio, checks the five algebraic equations, and enumerates all permitted ordered parameter pairs. It produced

```text
FINITE_FIELD_OK q= 9 ordinary= 12 rank4= 30 five_loci= [6, 6, 6, 6, 6]
FINITE_FIELD_OK q= 27 ordinary= 480 rank4= 120 five_loci= [24, 24, 24, 24, 24]
```

Finite enumeration is a consistency check, not a substitute for the geometric or isogeny arguments. To replay: `python verify_loci.py` (requires `sympy==1.14.0`) and `python verify_finite_fields.py` (Python standard library).

## Relationship to prior work

The genus-five Humbert curve and its ordered five-branch-point model are classical. Hidalgo's work on hyperelliptic quotients (arXiv:1705.09337, initially public May 25, 2017) discusses the five-point presentation over the complex numbers. Auffarth, Lucchini Arteche and Rojas (arXiv:1905.12690, initially public May 29, 2019) prove a five-elliptic-factor Jacobian decomposition and its two-primary isogeny kernel; that decomposition is **prior work, not part of the originality claim**. Martínez-Núñez (arXiv:2303.18056, initially public March 31, 2023) develops a more general Jacobian-decomposition theory over the complex numbers. The additional result here is the characteristic-three arithmetic consequence: the *pairwise-disjoint* five-component nonordinary locus, the complete \(3\)-rank/\(a\)-number spectrum, the Newton polygon restriction, and the uniform ordered finite-field counts. The proof supplies the characteristic-three transfer argument independently rather than assuming that a complex-analytic statement automatically extends to positive characteristic.

## Limitations

This theorem concerns the smooth **ordered** type-four Humbert–Edge family and characteristic exactly \(3\). It neither classifies curves up to abstract isomorphism nor determines their full zeta functions or all extension-field point counts. It makes no assertion about non-normalized descent configurations where not all five geometric branch points are rational over the ground field, nor about boundary degenerations. An unindexed earlier characteristic-three arithmetic stratification remains a possible originality risk.

## References

1. R. A. Hidalgo, *Hyperelliptic quotients of generalized Humbert curves*, arXiv:1705.09337 (first version May 25, 2017), https://arxiv.org/abs/1705.09337.
2. R. Auffarth, G. Lucchini Arteche, A. M. Rojas, *A decomposition of the Jacobian of a Humbert-Edge curve*, arXiv:1905.12690 (first version May 29, 2019), https://arxiv.org/abs/1905.12690.
3. G. Martínez-Núñez, *Decomposition of Jacobians of generalized Fermat curves*, arXiv:2303.18056 (first version March 31, 2023), https://arxiv.org/abs/2303.18056.
