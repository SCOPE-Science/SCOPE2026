# Exact characteristic-five rank strata in a genus-five Howe family

## Finding

Let \(k=\overline{\mathbb F}_5\). For \((a,b)\in k^2\) with \(\Delta=(a-b)(a^2-4)(b^2-4)\ne0\), let \(H_{a,b}\) be the smooth projective curve with function field
\[
k(x,u,v),\qquad u^2=x^4+a x^2+1,\quad v^2=x^4+b x^2+1.
\]
It is a nonhyperelliptic genus-five Howe curve. Define five functions on the parameter plane:
\[
\begin{aligned}
P_1&=a^2+2, &P_2&=b^2+2,\\
P_3&=a^2-ab+b^2-1+2(a+b),\\
P_4&=a^2-ab+b^2-1-2(a+b),\\
P_5&=a^2b^2+2(a^2+b^2)-2ab+1.
\end{aligned}
\]
All coefficients are interpreted in characteristic five. Writing \(f_5\) for Jacobian \(5\)-rank and \(\alpha\) for Jacobian \(a\)-number, the exact stratification is
\[
\boxed{ f_5(H_{a,b})=\#\{i\in\{1,2,3,4,5\}:P_i(a,b)\ne0\},\qquad
\alpha(H_{a,b})=5-f_5(H_{a,b}). }
\]
At most two of the five functions vanish at any admissible parameter. Consequently the only ranks are \(3,4,5\), and each occurs. The minimum-rank stratum comprises exactly **twenty distinct ordered geometric parameter pairs**, all rational over \(\mathbb F_{25}\) and none over \(\mathbb F_5\). It consists of ten disjoint two-point pairwise intersections of the divisors \(P_i=0\). This is a count of parameters, not of isomorphism classes.

## Assumptions and scope

The ground field is algebraically closed of characteristic \(5\); rank and \(a\)-number are geometric invariants. The discriminant exclusion \(\Delta\ne0\) ensures the two quartics have four distinct roots each and no root in common. The smooth projective normalization of their fiber product is understood. No claim is made for characteristic other than five, or for all genus-five Howe curves outside this two-parameter family.

## Proof

**Geometry and decomposition.** The quartic \(F_a=x^4+a x^2+1\) is squarefree if and only if \(a^2\ne4\), and \(F_a\) and \(F_b\) have a common root only if \(a=b\). Therefore the associated \((\mathbb Z/2)^2\)-cover of \(\mathbb P^1\) is connected and has eight branch points of inertia order two. Riemann–Hurwitz gives \(2g(H)-2=4(-2)+8\cdot2=8\), so \(g(H)=5\). The intermediate quotients are two elliptic curves \(E_a:u^2=F_a\) and \(E_b:v^2=F_b\), and a genus-three hyperelliptic curve \(D_{a,b}:w^2=F_aF_b\). Their Jacobians give a \(2\)-power-degree isogeny
\[
J(H_{a,b})\longrightarrow J(E_a)\times J(E_b)\times J(D_{a,b}),
\]
up to reversing the indicated arrow. Since the degree is prime to \(5\), its effect on \(5\)-divisible groups is an isomorphism; both \(5\)-rank and the dimension of \(\operatorname{Hom}(\alpha_5,J[5])\) are additive. The family is nonhyperelliptic by the genus-five Howe criterion for disjoint elliptic branch divisors.

**Hasse–Witt calculation.** For a smooth hyperelliptic curve \(y^2=f(x)\) in characteristic \(5\), a Hasse–Witt matrix for the basis \(dx/y,x\,dx/y,\ldots\) is formed from coefficients \(c_{5i-j}\) of \(f(x)^2\). The elliptic components have scalar entries \(P_1\) and \(P_2\). Write
\[
h_2=2(a+b),\quad h_4=a^2-ab+b^2-1,\quad
h_8=a^2b^2+2(a^2+b^2)-2ab+1.
\]
As \(F_aF_b\) is an even reciprocal polynomial, the genus-three matrix is
\[
M_D=\begin{pmatrix}h_4&0&h_2\\0&h_8&0\\h_2&0&h_4\end{pmatrix}.
\]
The constant change-of-basis vectors \((1,0,1),(1,0,-1),(0,1,0)\) diagonalize this matrix over \(\mathbb F_5\). Thus the Cartier operator, including its Frobenius semilinearity, decomposes into five stable one-dimensional eigenspaces with coefficients \(P_1,\ldots,P_5\). In a one-dimensional semilinear space over an algebraically closed field, a nonzero coefficient gives stable rank one and a zero coefficient gives stable rank zero. Therefore stable Cartier rank is the number of nonzero \(P_i\), and its kernel dimension is the number of zeros. This proves the displayed formulas for \(f_5\) and \(\alpha\).

**No triple intersections.** Saturate each pairwise ideal by \(\Delta\). Exact elimination over \(\mathbb F_5\), encoded in `verify_symbolic.py`, yields the following complete pairwise loci; each row specifies \(b\) and a quadratic satisfied by \(a\):

| Vanishing factors | Relation for \(b\) | Equation for \(a\) |
|---|---|---|
| \(P_1,P_2\) | \(b=-a\) | \(a^2+2=0\) |
| \(P_1,P_3\) | \(b=a+1\) | \(a^2+2=0\) |
| \(P_1,P_4\) | \(b=a-1\) | \(a^2+2=0\) |
| \(P_1,P_5\) | \(b=2a\) | \(a^2+2=0\) |
| \(P_2,P_3\) | \(b=a-1\) | \(a^2-2a-2=0\) |
| \(P_2,P_4\) | \(b=a+1\) | \(a^2+2a-2=0\) |
| \(P_2,P_5\) | \(b=-2a\) | \(a^2-2=0\) |
| \(P_3,P_4\) | \(b=-a\) | \(a^2-2=0\) |
| \(P_3,P_5\) | \(b=-a-2\) | \(a^2+2a-2=0\) |
| \(P_4,P_5\) | \(b=2-a\) | \(a^2-2a-2=0\) |

Each displayed quadratic is separable and irreducible over \(\mathbb F_5\), so it has exactly two distinct roots in \(\mathbb F_{25}\). The ten saturated pairwise ideals have no common points with any third divisor: equivalently, for every triple of indices the saturated ideal is the unit ideal. The attached symbolic verifier computes all ten triple Gröbner bases directly, rather than merely testing geometric points in a bounded finite field. Thus exactly twenty admissible geometric parameters have rank three, and no lower rank occurs. The examples below show all three ranks occur.

## Verification

Run `python verify_symbolic.py` (SymPy required) and `python verify_f25.py` (Python standard library). The symbolic checker expands the relevant powers in characteristic five, calculates all ten saturated pair intersections and ten triple-intersection ideals, and prints `SYMBOLIC_VERIFY_OK` on success. The independent arithmetic checker constructs \(\mathbb F_{25}=\mathbb F_5[\theta]/(\theta^2-2)\), loops over all \(625\) ordered parameter pairs, rejects \(119\) nonadmissible pairs, and obtains respectively \(20,180,306\) parameters of ranks \(3,4,5\). Every one of the ten factor pairs accounts for two rank-three parameters. It prints `F25_VERIFY_OK` on success.

Explicit witnesses are: \((a,b)=(2\theta,3\theta)\) for rank three, \((0,\theta)\) for rank four, and \((0,1)\) for rank five. Their respective \(a\)-numbers are \(2,1,0\). The finite-field enumeration checks examples and the twenty-point count, while the saturated-ideal calculation proves completeness over the algebraic closure.

## Relationship to prior work

Kudo's genus-five Howe construction (2024, preprint arXiv:2401.00760) establishes a plane-sextic description of nonhyperelliptic genus-five Howe curves arising from disjoint elliptic branch covers and classifies singularities of that plane model. It does not state the five-factor characteristic-five Cartier decomposition or the present complete two-parameter rank strata. Katsura and Takashima (2021, arXiv:2108.06936) establish the lower-genus-quotient Jacobian decomposition; that decomposition is used here, not claimed new. Chang and coauthors (2025, arXiv:2502.09540) treat broader bielliptic moduli and construct low-rank covers, but their statements do not determine this reciprocal-quartic subfamily's exact twenty-point minimum locus. The rank formula, excluded ranks and intersection classification are the contributions assessed here.

## Limitations

The parameter count does not quotient by curve isomorphisms or determine supersingularity/Newton polygons. It gives \(5\)-rank and \(a\)-number only. The argument requires the stated open parameter domain and characteristic five. A previously unindexed special-family arithmetic table remains a possible literature-overlap risk. No independent external audit has been performed.

## References

1. M. Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, II*, arXiv:2401.00760, first released 2024-01-01. https://arxiv.org/abs/2401.00760
2. T. Katsura and K. Takashima, *Decomposed Richelot isogenies of Jacobian varieties of hyperelliptic curves and generalized Howe curves*, arXiv:2108.06936, 2021. https://arxiv.org/abs/2108.06936
3. H. Chang, D. Dragutinović, A. Groen, J. Lin, D. Pacheco-Tallaj, A. Singhal, *The \(p\)-rank stratification of the moduli space of double covers of a fixed elliptic curve*, arXiv:2502.09540, 2025. https://arxiv.org/abs/2502.09540
