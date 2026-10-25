# A rigid seven-point harmonic extremum and its genus-forty-nine Jacobian in characteristic three

## Finding

Let \(k\) be an algebraically closed field of characteristic \(3\), and let \(B\subset\mathbb P^1(k)\) contain seven distinct points. Call a four-subset *harmonic* if its cross-ratio is \(-1\) (independent of ordering in characteristic \(3\)); equivalently, the genus-one double cover branched over it is supersingular. Write \(h(B)\) for the number of these four-subsets. Then
\[
\boxed{h(B)\le5.}
\]
Equality holds **if and only if** \(B\) is projectively equivalent over \(k\) to a seven-point subset of \(\mathbb P^1(\mathbb F_9)\). All equality sets form one \(\operatorname{PGL}_2(k)\)-orbit. An explicit representative is
\[
 B_*=\{\infty,0,1,1-z,-z,-1,z\},\qquad z^2-z-1=0\quad\text{in }\mathbb F_9.
\]

For the connected maximal elementary abelian double cover \(C_B\to\mathbb P^1\) of group \((\mathbb Z/2)^6\), branched with inertia two at exactly the seven points, the curve has genus \(49\). Its \(35\) elliptic double quotients correspond to the four-subsets of \(B\), so the theorem says at most five of those elliptic quotients can be supersingular, with exactly one projective branch configuration attaining five. For \(B=B_*\), each of the remaining seven genus-two double quotients is ordinary, and
\[
\boxed{f_3(J(C_{B_*}))=44,\quad a(J(C_{B_*}))=5,\quad
\mathrm{NP}(J(C_{B_*}))=0^{44},(1/2)^{10},1^{44}.}
\]
The bound concerns the number of supersingular *elliptic quotients*, not a global lower bound on the \(3\)-rank of every genus-\(49\) curve in the family.

## Assumptions and scope

All projective equivalences and Jacobian invariants are geometric over \(k\). A harmonic four-subset is defined by the vanishing of the expression \([a,c][b,d]+[a,d][b,c]\), where \([a,b]\) is the determinant of homogeneous coordinates for projective points. In characteristic \(3\), permuting the four points preserves its zero locus. For any three distinct points, exactly one fourth point completes a harmonic quadruple. Therefore two different harmonic four-subsets of \(B\) cannot share three points.

For genus \(49\), the cover is the connected maximal tame multiquadratic cover with inertia generators associated with the seven branch points and their sole relation that the sum is zero. The construction is smooth after normalization and has degree \(64\). Its genus follows from Riemann–Hurwitz:
\[2g-2=64(-2+7/2)=96.\]

## Proof

**1. A finite incidence classification.** Number the seven points by \(0,\dots,6\). Any collection of distinct harmonic four-subsets is a clique in the graph whose vertices are the \(\binom74=35\) four-subsets and in which two vertices are compatible when they intersect in at most two elements. An exact finite enumeration (standalone verifier) shows that this graph has precisely \(1050\) five-cliques, in exactly two \(S_7\)-orbits of sizes \(420\) and \(630\). Their representatives, in concatenated index notation, are
\[
\begin{aligned}
 \mathcal A&=\{0125,0146,0356,1236,2345\}, &&\text{orbit size }420,\\
 \mathcal F&=\{0126,0145,0235,1234,1356\}, &&\text{orbit size }630.
\end{aligned}
\]
This finite verification examines every compatible five-subset of the 35 labeled candidates and every relabeling of both displayed representatives; it is exhaustive as a finite incidence statement, independent of the field and of any search heuristic.

**2. The second incidence type is algebraically impossible.** Normalize labeled points \(p_0=\infty,p_1=0,p_2=1\), and write \((p_3,p_4,p_5,p_6)=(u,v,w,z)\). For the five harmonic conditions in \(\mathcal F\), the first three give \(z=-1\), \(w=-v\), \(u=v-1\). The last two become
\[
2v^2-v+1=0,\qquad v^2-v-1=0.
\]
Subtracting twice the second equation from the first yields \(v=0\), contradicting the second equation. Thus \(\mathcal F\) cannot occur even as a partial configuration of five harmonic quadruples.

**3. The first incidence type is rigid.** For \(\mathcal A\), the first three equations give \(w=-1\), \(v=-z\), \(u=1-z\). Each remaining condition is then equivalent, up to a nonzero scalar in \(\mathbb F_3\), to
\[z^2-z-1=0.\]
This polynomial is irreducible over \(\mathbb F_3\), because it is nonzero at each of \(0,1,-1\); it has two distinct roots in \(\mathbb F_9\). Both choices make the seven displayed points distinct. Direct substitution into all \(35\) harmonic determinants (reproduced by the verifier) shows that *exactly five* four-subsets are harmonic, namely those of \(\mathcal A\). Therefore any seven-point configuration with at least five harmonic four-subsets equals an instance of \(B_*\) after projective normalization and relabeling, and it cannot have six or more. The bound is attained. Every seven-subset of \(\mathbb P^1(\mathbb F_9)\) is projectively equivalent to \(B_*\), since the complement has three points and \(\operatorname{PGL}_2(\mathbb F_9)\) acts sharply transitively on ordered triples of distinct points. This proves both maximality and uniqueness.

**4. The genus-\(49\) arithmetic consequence.** The \(63\) nontrivial characters of the cover group correspond to the even nonempty subsets of the seven inertia labels: \(21\) subsets of size two, \(35\) of size four and \(7\) of size six. Their double quotient genera are, respectively, \(0,1,2\). Pullbacks from the positive-genus quotients give an isogeny onto the genus-\(49\) Jacobian: the quotient maps have degree \(32\); the matrix of pushforwards composed with pullbacks is diagonal with entries \([32]\) and all off-diagonal entries zero by character orthogonality. Hence the kernel is killed by \(32\), so this isogeny induces an isomorphism on \(3\)-divisible groups. This argument is valid in characteristic \(3\) and does not transfer a complex-analytic isogeny without justification.

The Legendre elliptic curve with four branch points has supersingular reduction in characteristic \(3\) precisely when its parameter is \(-1\), equivalently when the branch set is harmonic. Thus exactly five elliptic quotients of \(C_{B_*}\) are supersingular and the other thirty ordinary. Each of the seven six-point subsets of \(B_*\) contains one of its five harmonic four-subsets, as is seen from \(\mathcal A\). Normalize that quadruple to \(\{\infty,0,1,-1\}\) and write the two other points \(u,v\). The genus-two quotient then has a model
\[y^2=(x^3-x)(x-u)(x-v).\]
Its Cartier–Manin determinant, computed from the coefficients of the right-hand side, is \(-(u-v)^2\ne0\), so every one of the seven genus-two quotients is ordinary. The prime-to-three isogeny therefore yields \(30+7\cdot2=44\) ordinary elliptic dimensions and five supersingular elliptic dimensions. Their \(3\)-ranks, \(a\)-numbers, and Newton slopes give the stated formulas.

## Verification

Run `python3 verify_harmonic_seven.py` using only the Python standard library. It exhaustively constructs the \(35\)-vertex compatibility graph, enumerates all \(1050\) compatible five-block systems, verifies their two exact relabeling orbits, computes the five harmonic four-subsets of the canonical seven-point set in \(\mathbb F_9\), and checks all \(120\) seven-subsets of \(\mathbb P^1(\mathbb F_9)\). The characteristic-three polynomial elimination and the prime-to-three character decomposition are given symbolically above; neither conclusion rests on finite-field extrapolation.

## Relationship to prior work

The 2015 decomposition of Carvacho, Hidalgo and Quispe gives the general character-quotient geometry of generalized Fermat curves, including the \(35\) elliptic plus \(7\) genus-two factors for the genus-\(49\) case. These factors and that decomposition are not claimed as new. Hirschfeld's finite-geometry treatment classifies harmonic tetrads and related configurations within \(\operatorname{PG}(1,9)\). Its \(30\) harmonic tetrads and the fact that three points lie in a unique one are established inputs. The finding here is the **global** upper bound for arbitrary seven distinct points over an algebraically closed field of characteristic three, its rigid equality classification, and the consequent explicitly determined extremal branch configuration and Jacobian invariants. A result hidden under another name in classical projective-line geometry remains a priority risk.

## Limitations

The result does not classify nonmaximal harmonic configurations, nor the full Newton stratification of the four-dimensional genus-\(49\) family. The arithmetic consequence is geometric over an algebraic closure; it asserts no specific descent of the curve or of the quotient maps to a smaller finite field. No independent audit has been carried out.

## References

1. M. Carvacho, R. A. Hidalgo, S. Quispe, *Isogenous decomposition of the Jacobian of generalized Fermat curves*, arXiv:1507.02903v1 (10 July 2015), especially Theorem 4.4 and Section 5.4.
2. J. W. P. Hirschfeld, *Projective Geometries over Finite Fields*, 2nd ed., Oxford University Press (1998), especially Section 6.4(vii) and Section 14.7 on \(\operatorname{PG}(1,9)\), ISBN 9780198502951.
