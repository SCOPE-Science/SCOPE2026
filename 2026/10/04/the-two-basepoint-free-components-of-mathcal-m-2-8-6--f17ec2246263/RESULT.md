# The two basepoint-free components of \(\mathcal M^2_{8,6}\)

## Finding
Over \(\mathbf C\), the Brill--Noether locus \(\mathcal M^2_{8,6}\) has exactly two irreducible components whose general point admits a basepoint-free \(g^2_6\). The first is the Severi component: its general curve is the normalization of an irreducible degree-six plane curve with exactly two nodes. The second is the trigonal component \(\mathcal M^1_{8,3}\), on which twice the trigonal pencil supplies a basepoint-free \(g^2_6\) mapping three-to-one onto a conic. The general curve of the Severi component has gonality \(4\), so the two components are distinct.

## Assumptions and scope
Work is over \(\mathbf C\). The notation \(\mathcal M^r_{g,d}\) denotes the locus of smooth genus-\(g\) curves admitting a \(g^r_d\). The claim classifies only irreducible components whose general curve possesses a basepoint-free \(g^2_6\); it does not assert that the full locus has only two components, because components supported on curves for which the relevant \(g^2_6\) has basepoints are not excluded.

## Proof
The Brill--Noether number is
\[
\rho(8,2,6)=8-3(8-6+2)=-4,
\]
so the expected dimension of \(\mathcal M^2_{8,6}\) is \(3\cdot8-3-4=17\). A plane sextic has arithmetic genus \(10\), hence a sextic of geometric genus \(8\) has total delta invariant \(2\). By irreducibility of the Severi variety, its image in \(\mathcal M_8\) gives the birational, basepoint-free component described by Haburcak--Teixidor i Bigas. Its dimension is \(25-8=17\): the Severi variety has dimension \(3\cdot6+8-1=25\), and quotienting by \(\operatorname{PGL}_3\) removes \(8\) dimensions.

For the general two-nodal plane sextic, the Coppens--Kato gonality criterion applies. For even degree \(d\), their nodal-plane criterion gives gonality \(d-2\) under the numerical bound used here; at \(d=6\) the threshold is \(6(6-4)/4-1=2\), well below genus \(8\). Thus the general normalization in the Severi component has gonality \(4\), in particular it is not trigonal.

Now let \(\Xi\) be any other irreducible component whose general curve \(C\) has a basepoint-free \(g^2_6\), and suppose its associated map is non-birational. Since \(\rho(8,2,6)=-4>-7=-8+1\), the cover-dimension lemma of Haburcak--Teixidor i Bigas forces the plane image to have geometric genus \(0\). If the map has degree \(k\) and the rational plane image has degree \(e\), then \(ek=6\) with \(e,k\ge2\), leaving \((e,k)=(3,2)\) or \((2,3)\). Their rational-image dimension estimate specializes to
\[
17\le 2\cdot8-5+2k=11+2k.
\]
The case \(k=2\) would give \(17\le15\), impossible. Hence \(k=3\) and \(e=2\): the map is a triple cover of a conic. Therefore the generic curve of \(\Xi\) is trigonal.

Conversely, if \(A\) is a trigonal pencil on a genus-eight curve, the pullback of the three-dimensional space \(H^0(\mathbf P^1,\mathcal O(2))\) inside \(H^0(C,2A)\) is a basepoint-free \(g^2_6\) and factors through the conic Veronese map. Thus \(\mathcal M^1_{8,3}\subset\mathcal M^2_{8,6}\). The simply-branched degree-three Hurwitz space has \(2g+2k-2=20\) branch points; modulo \(\operatorname{PGL}_2\), its image is irreducible of dimension \(20-3=17\). Hence every non-birational basepoint-free component is the trigonal component. Since the Severi component is generically tetragonal, these are distinct, and they are exactly the two components with generic basepoint-free \(g^2_6\).

## Verification
The embedded checker recomputes \(\rho=-4\), the expected dimension \(17\), the two-node count, the Severi and trigonal dimensions, the two factorizations \(6=2\cdot3=3\cdot2\), exclusion of the degree-two cover by the dimension bound, and the numerical Coppens--Kato threshold. Its recorded output is `VERIFY_OK rho=-4 expected=17 delta=2 severi=17 trigonal=17 only_nonbirational_k=3 gonality_severi=4`.

## Relationship to prior work
Haburcak--Teixidor i Bigas prove a unique basepoint-free component for \(d>(g+4)/2\), and at equality when \(d\) is odd. They explicitly exhibit reducibility at the even equality boundary for \(\mathcal M^2_{12,8}\), but their listed examples and their general reducibility corollary do not include \(\mathcal M^2_{8,6}\); the latter assumes \(g>8\) and a strict degree inequality. Specializing their cover-dimension argument to \((g,d)=(8,6)\), together with the classical gonality theorem for nodal plane models, isolates the omitted low-genus even-boundary cell and classifies all basepoint-free components there. Exact public and semantic searches for \(\mathcal M^2_{8,6}\), genus-eight \(g^2_6\)'s, trigonal sextic components, and the corresponding Brill--Noether number did not locate an earlier statement of this classification.

## Limitations
The result does not classify possible components whose generic \(g^2_6\) has basepoints. The originality check covered the recent source, its cited structural ingredients, targeted public searches, and the available semantic research index; a classical low-genus classification not exposed by those searches remains a residual bibliographic risk.

## References
1. R. Haburcak and M. Teixidor i Bigas, *Some reducible and irreducible Brill--Noether loci*, arXiv:2503.16255v1 (2025); Math. Z. 312, 102 (2026).
2. M. Coppens and T. Kato, *The gonality of smooth curves with plane models*, Manuscripta Math. 70 (1991), 5--26; correction, Manuscripta Math. 71 (1991), 337--338.
3. J. Harris, *On the Severi problem*, Invent. Math. 84 (1986), 445--461.
