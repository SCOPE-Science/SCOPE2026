# The characteristic-seven flex divisor of the four-nodal Wiman sextic

## Finding
Let \(k=\overline{\mathbb F}_7\). For the Wiman four-nodal plane sextic \(C=V(F)\), where
\[
F=X^6+Y^6+Z^6+(X^2+Y^2+Z^2)(X^4+Y^4+Z^4)-12X^2Y^2Z^2,
\]
the smooth flex divisor cut out by the projective Hessian has exactly \(30\) distinct points. Six have tangent-line intersection multiplicity \(6\) and flex weight \(4\); twenty-four have ordinary tangent contact \(3\) and weight \(1\). The six exceptional points are
\[
[0:a:1],\quad[a:0:1],\quad[1:a:0],\qquad a^2=-1.
\]
Their minimal field is \(\mathbb F_{7^2}\). The other twenty-four flexes each have minimal field \(\mathbb F_{7^3}\). Therefore Frobenius has orbit profile \(2^3 3^8\) and all flexes are rational over \(\mathbb F_{7^6}\), with \(6\) minimal as a common extension degree. The weighted smooth flex divisor has degree \(6\cdot4+24=48\).

## Assumptions and scope
All computations use the displayed model in characteristic \(7\), not the *different* smooth \(A_6\)-invariant genus-ten sextic also called a Wiman sextic. By the four-nodal model and its known nonsingularity away from nodes for characteristic at least \(7\), \(C\) is reduced and irreducible with precisely the four ordinary nodes \([\pm1:\pm1:1]\). Its normalization has genus \(6\). A flex means a smooth point where the embedded tangent line has contact at least \(3\); its weight here is the contact order minus \(2\). The Hessian is \(H=\det(\partial_i\partial_j F)\). Because the characteristic exceeds the plane degree, the classical Hessian flex criterion holds. No claim concerns flexes in other characteristics or moduli of abstract genus-six curves.

## Proof
Set \(U=X^2\), \(V=Y^2\) in the affine chart \(Z=1\), and let \(f(U,V)=F(X,Y,1)\), \(h(U,V)=H(X,Y,1)\). The exact resultant over \(\mathbb F_7\) is
\[
\operatorname{Res}_V(f,h)=U^2(U+1)^2(U-1)^6 A(U)B(U),
\]
where \(A(U)=U^3-3U^2+U-1\) and \(B(U)=U^3-U^2+3U-1\). Both cubics are irreducible: checking their seven possible roots gives none. For \(U=0,1,-1\), respectively, the monic greatest common divisor of \(f(U,V)\) and \(h(U,V)\) is \(V+1\), \((V-1)^2\), and \(V^2\). For each root \(u\) of \(A\), their common zero is uniquely \(v=1+4u+6u^2\); for each root of \(B\), it is uniquely \(v=1+2u+6u^2\). The two cubic factors are distinct, and these latter common zeros are simple because the resultant has simple zeros in \(U\). In addition, in chart \(X=1,Z=0\), the greatest common divisor in \(V=Y^2\) is \(V+1\). These are exact identities in \(\mathbb F_7\), checked by the included script.

For the two cubic factors, \(\operatorname{Norm}_{\mathbb F_{7^3}/\mathbb F_7}(u)=\operatorname{Norm}(v)=1\). Because the quadratic character of an element in a finite extension of odd degree is the quadratic character of its norm, every such \(u\) and \(v\) is a nonzero square in \(\mathbb F_{7^3}\). Each of the six roots \(u\) consequently lifts to four \((X,Y)\) choices. This gives \(24\) smooth points, each of exact degree \(3\) and local Hessian intersection length \(1\). At \((U,V)=(1,1)\), the resultant has order \(6\), and the squaring map is étale; the four sign lifts are precisely the four ordinary nodes, each of length \(6\), giving total length \(24\) at the singular locus.

At \((U,V)=(0,-1)\), the squared-coordinate intersection has length \(2\), and the ramification \(U=X^2\) doubles this length at each of the two lifts. Analogously \((-1,0)\) gives two more smooth points of length \(4\), and by coordinate symmetry the line at infinity gives two more. Thus the six axial points have local Hessian intersection length \(4\). For a representative \([0:a:1]\) with \(a^2=-1\), the tangent line is \(Y=aZ\) (the corresponding gradient component is nonzero), and substitution yields \(F(X,a,1)=2X^6\) in characteristic \(7\). The tangent therefore meets the curve with exact multiplicity \(6\); the same is true at all six by coordinate symmetry. The points have exact degree \(2\), since \(-1\) is not a square in \(\mathbb F_7\).

There is no common curve component between \(F\) and \(H\): the nonzero affine resultant rules out an affine component, and \(F\) has no component contained in the line at infinity. Bézout gives total intersection number \(6\cdot12=72\). The nodes account for \(4\cdot6=24\), and the listed smooth intersections account for \(6\cdot4+24=48\); hence this is exhaustive. In characteristic \(7\), Hessian order at a smooth plane-curve point is the inflection weight. The \(24\) length-one intersections are ordinary flexes. Their degrees and the axial degree-two points give exactly the claimed Frobenius cycles and least common extension.

## Verification
Run `python verify_wiman7.py` with SymPy installed. All arithmetic identities are exact integer polynomial operations reduced modulo \(7\); no numerical sampling, randomized steps, or finite-field point enumeration stand in for exhaustiveness. The checker asserts the resultant and special fibers, irreducibility of both cubics, the unique cubic-root formulas, norms, infinity-chart behavior, and tangent order. The proof above supplies the local flat/étale length arguments, Bézout exhaustion, and Hessian criterion; the script independently reproduces the polynomial certificates.

## Relationship to prior work
Inoue and Kato give the defining equation, classical four-nodal model and construction of the Wiman curve, without the characteristic-seven flex divisor computed here. Giulietti–Kawakita–Lia–Montanucci study finite-field maximality and automorphisms of this genus-six model, including characteristic \(7\), without this Hessian/Frobenius calculation. Kaneta–Marcugini–Pambianco's named *Wiman sextic* has \(A_6\) symmetry and a \(72\)-point flex arc; it is the different smooth genus-ten model, not the four-nodal \(S_5\) curve studied here. No source inspected gave the displayed characteristic-seven decomposition or implication thereof. Searches do not establish absolute absence from all historical work.

## Limitations
The result classifies flexes of this particular plane *model*, not Weierstrass points for all linear systems on its normalization or intrinsic equivalence classes. The published modular/Hessian literature is not exhaustively indexed, so an equivalent older computation cannot be ruled out beyond the recorded comparisons. The Kyoto institutional preprint is catalogued under \(2005\) without a verified day of initial availability; the available full calendar-date bibliographic record is \(2006\)-\(07\)-\(14\), which must not be mistaken for a proven first preprint posting date. The result has undergone self-review only, not independent audit.

## References
1. N. Inoue and F. Kato, *On the geometry of Wiman’s sextic*, Kyoto Mathematics preprint 2 (2005), https://www.math.kyoto-u.ac.jp/preprint/2005/2inoue.kato.pdf ; DOI: 10.1215/kjm/1250281655.
2. M. Giulietti, M. Kawakita, S. Lia, M. Montanucci, *An \(\mathbb F_{p^2}\)-maximal Wiman sextic and its automorphisms*, arXiv:1805.06317, https://arxiv.org/abs/1805.06317.
3. H. Kaneta, S. Marcugini, F. Pambianco, *On arcs and curves with many automorphisms*, Mediterranean Journal of Mathematics 2 (2005), 71–102; DOI: 10.1007/s00009-005-0031-0 (a distinct smooth \(A_6\)-invariant sextic).
