# The \(81\) sextactic secants of the Fermat cubic split into \(9+18+54\) projective-symmetry orbits
## Finding
Let \(F\subset\mathbb P^2_{\mathbb C}\) be the Fermat cubic \(x^3+y^3+z^3=0\), choose any flex \(O\) as elliptic-curve origin, let \(S=F[6]\setminus F[3]\) be its \(27\) sextactic points, and let \(\mathcal L\) be the \(81\) lines containing triples of points of \(S\). Under the full projective automorphism group \(G=\operatorname{Aut}_{\mathbb P^2}(F)\), of order \(54\), the set \(\mathcal L\) has exactly three orbits, of sizes \(9\), \(18\), and \(54\). For \(\ell\in\mathcal L\) with \(\ell\cap S=\{P,Q,R\}\), put \(D_\ell=\{2P,2Q,2R\}\subset F[3]\). If \(\rho\in\operatorname{Aut}(F,O)\) has order \(3\) and \(K=\ker(\rho-1:F[3]\to F[3])\), then the \(9\)-orbit consists exactly of lines for which \(D_\ell\) is a singleton; the \(18\)-orbit consists exactly of lines for which \(D_\ell\) is a coset of \(K\); and the \(54\)-orbit consists exactly of lines for which \(D_\ell\) is a coset of one of the other three order-\(3\) subgroups of \(F[3]\cong(\mathbb Z/3)^2\). The corresponding line-stabilizer orders are \(6\), \(3\), and \(1\).

The doubling-image classifier is intrinsic to the embedded elliptic curve. It refines the known \((81_3,27_9)\) incidence configuration into one symmetry-enhanced family, one complex-multiplication family, and one generic free orbit.

## Assumptions and scope
Work over \(\mathbb C\). Let
\[
F:\ x^3+y^3+z^3=0
\]
and choose a flex \(O\in F\) as the origin of its elliptic-curve group law. The plane embedding is the complete linear system \(|3O|\), so three points \(P,Q,R\in F\) are collinear, with multiplicity, exactly when \(P+Q+R=O\).

The source identifies the \(27\) sextactic points as
\[
S=F[6]\setminus F[3]
\]
and proves that there are exactly \(81\) lines through triples of points of \(S\), forming an \((81_3,27_9)\) configuration. The present statement concerns the action of the full projective automorphism group of this fixed plane cubic on those \(81\) lines.

## Proof
The projective automorphism group of the equianharmonic plane cubic is
\[
G=F[3]\rtimes\operatorname{Aut}(F,O),
\qquad |F[3]|=9,\qquad |\operatorname{Aut}(F,O)|=6,
\]
hence \(|G|=54\). The factor \(F[3]\) acts by translations preserving \(|3O|\), while \(\operatorname{Aut}(F,O)\cong\mu_6\) is the origin-fixing complex-multiplication group.

For \(\ell\in\mathcal L\), write \(\ell\cap S=\{P,Q,R\}\). Collinearity gives \(P+Q+R=O\), so
\[
2P+2Q+2R=O
\]
in \(F[3]\). Thus \(D_\ell=\{2P,2Q,2R\}\) is either a singleton or a three-point affine line in the affine plane \(F[3]\cong\mathbb F_3^2\). Indeed, if two doubled points agree, say \(2P=2Q=a\), then the third doubled point \(b\) satisfies \(2a+b=0\), whence \(b=a\) because \(3a=0\). Otherwise three distinct points of \(\mathbb F_3^2\) with sum zero are exactly an affine line.

For each \(a\in F[3]\), the fibre of doubling on \(F[6]\) contains four points. Exactly one is in \(F[3]\), so the remaining three lie in \(S\). If \(U\in F[3]\) is the unique point with \(2U=a\), those three sextactic points are \(U+t\) for the three nonzero \(t\in F[2]\). Their sum is zero because \(3U=0\) and the three nonzero points of \(F[2]\cong\mathbb F_2^2\) sum to zero. Hence every \(a\) gives exactly one secant with singleton doubling image. There are therefore exactly \(9\) such lines.

Now let \(A=\{a_1,a_2,a_3\}\subset F[3]\) be an affine line. Write \(U_i\in F[3]\) for the unique point satisfying \(2U_i=a_i\). Since \(a_1+a_2+a_3=0\), also \(U_1+U_2+U_3=0\). A sextactic lift of \(a_i\) is \(U_i+t_i\) with \(t_i\) one of the three nonzero elements of \(F[2]\). The three lifts are collinear exactly when
\[
t_1+t_2+t_3=0.
\]
In \(\mathbb F_2^2\), this occurs exactly when \(t_1,t_2,t_3\) are the three distinct nonzero elements, in one of \(3!=6\) orders. Thus every affine line in \(F[3]\) has exactly \(6\) secants above it. Since \(\mathbb F_3^2\) has \(4\) directions and \(3\) affine lines in each direction, this gives \(12\cdot6=72\) non-singleton secants and recovers \(9+72=81\).

It remains to determine the \(G\)-orbits. Translation by \(T\in F[3]\) sends \(D_\ell\) to \(D_\ell+2T\), so it is transitive on the three affine cosets of each fixed direction. An order-\(3\) complex-multiplication element \(\rho\) acts on the four projective directions of \(F[3]\cong\mathbb F_3^2\) with one fixed direction
\[
K=\ker(\rho-1)
\]
and one three-cycle on the other directions. Hence the doubling images split into three invariant classes: the \(9\) singletons, the \(3\) affine cosets of \(K\), and the \(9\) affine lines in the other three directions.

The only remaining issue is whether the six sextactic lifts over each affine image can split further. The exact finite action of all \(54\) group elements on \(F[6]\cong(\mathbb Z/6)^2\) resolves this without sampling: the resulting line orbits have sizes \(9\), \(18\), and \(54\). Their stabilizer orders are therefore
\[
54/9=6,\qquad 54/18=3,\qquad 54/54=1.
\]
This also proves that the three doubling-image classes above are exactly the three \(G\)-orbits.

## Verification
The accompanying script `verify_sextactic_81_orbits.py` models \(F[6]\) as \((\mathbb Z/6)^2\), identifies \(F[3]\) with the even-coordinate subgroup, enumerates all triples in \(S=F[6]\setminus F[3]\) with sum zero, and constructs the full order-\(54\) affine action \(F[3]\rtimes\mu_6\). It exhaustively verifies:
\[
|S|=27,\qquad |\mathcal L|=81,\qquad 81\cdot3=27\cdot9,
\]
the \(9+18+54\) orbit decomposition, stabilizer orders \(6,3,1\), the singleton-versus-affine-line doubling classifier, six lifts over each affine line in \(F[3]\), and the unique complex-multiplication-fixed direction.

A fresh replay of the packaged script returned:
`VERIFY_OK points=27 lines=81 incidences=81x3=27x9 group=54 orbits=9+18+54 stabilizers=6,3,1 doubling=singleton+fixed_CM_direction+other_directions fibres=1_or_6`.

## Relationship to prior work
Szemberg and Szpond identify the sextactic locus with \(F[6]\setminus F[3]\) and prove the \((81_3,27_9)\) secant configuration, but do not decompose those \(81\) lines under the full projective automorphism group. Dimca, Ilardi, Malara, and Pokora explicitly study group actions on the \(27\) sextactic points and on associated hyperosculating conics; their results do not give an orbit decomposition of the \(81\) three-secants. Merta and Zięba study tangent lines at sextactic points and conic arrangements, which are different line and conic configurations.

The present refinement is therefore not a recount of the \(81\) lines: it identifies the canonical quotient invariant \(D_\ell\) and proves that its three symmetry types coincide exactly with the three projective line orbits.

## Limitations
The result is for the complex Fermat cubic in its standard plane embedding. It classifies orbits under projective automorphisms of the cubic; it does not claim that the abstract incidence structure has no additional combinatorial automorphisms. No positive-characteristic analogue is asserted. The originality comparison cannot exclude an obscure classical treatment phrased purely in equianharmonic theta-function or division-point language.

## References
1. T. Szemberg and J. Szpond, *Sextactic points on the Fermat cubic curve and arrangements of conics*, arXiv:2211.00494v1, 2022. In particular, Remark 4.1 and Lemma 4.8.
2. A. Dimca, G. Ilardi, G. Malara, and P. Pokora, *Construction of free curves by adding osculating conics to a given cubic curve*, arXiv:2311.08913v1, 2023. See Section 4.
3. M. Merta and M. Zięba, *Sextactic and type-9 points on the Fermat cubic and associated objects*, arXiv:2406.13802v1, 2024.
