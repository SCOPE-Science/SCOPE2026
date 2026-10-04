# The diminished-Fermat quintic companion map normalizes a degree-25 surface
## Finding
Over \(\mathbb C\), consider the six quintics
\[
\begin{aligned}
u_1&=a^2(5c^3-a^3),&u_2&=b^2(b^3-5c^3),&u_3&=c^2(c^3-5a^3),\\
u_4&=c^2(5b^3-c^3),&u_5&=5b^2(a^3-c^3),&u_6&=5a^2(c^3-b^3).
\end{aligned}
\]
They define the base-point-free system \(\Lambda\) from the initial diminished-Fermat example of Kabat and Strycharz-Szemberg. Let
\[
\phi_\Lambda:\mathbb P^2\longrightarrow\mathbb P^5,
\qquad [a:b:c]\longmapsto[u_1:\cdots:u_6],
\]
and let \(X=\phi_\Lambda(\mathbb P^2)\). Then \(\phi_\Lambda\) is finite and birational. Consequently it is the normalization morphism of \(X\), and
\[
\deg X=25.
\]
A concrete degree-one certificate is
\[
\phi_\Lambda([1:2:1])=[4:12:-4:39:0:-35],
\]
whose scheme-theoretic fiber is a reduced singleton.

## Assumptions and scope
The ground field is \(\mathbb C\). The six displayed quintics and their base-point freeness are taken from the cited source. The claim concerns the companion surface attached to the source's initial case \(m=3\), not the whole later family \(\Lambda_m\). It determines finiteness, birationality, normalization, and degree; it does not determine the singular locus of \(X\), whether \(\phi_\Lambda\) is injective everywhere, or whether this six-dimensional subsystem is very ample.

## Proof
Because the source proves that \(\Lambda\) is base-point free, the six sections define a morphism and
\[
\phi_\Lambda^*\mathcal O_{\mathbb P^5}(1)\simeq\mathcal O_{\mathbb P^2}(5).
\]
The latter line bundle is ample. If an irreducible curve \(C\subset\mathbb P^2\) were contracted, then the pullback of \(\mathcal O(1)\) would have degree zero on \(C\), whereas \(\deg(\mathcal O(5)|_C)=5\deg C>0\). Thus no curve is contracted. Since a positive-dimensional projective fiber would contain a curve, all fibers are zero-dimensional; properness then makes \(\phi_\Lambda\) finite onto its image.

It remains to determine its generic degree. At \(p=[1:2:1]\), direct substitution gives
\[
(u_1,\ldots,u_6)(p)=(4,12,-4,39,0,-35).
\]
Let \(q=[A:B:C]\) lie in the same projective fiber. Since the third target coordinate is nonzero, \(C=0\) is impossible because \(u_3(A,B,0)=0\). Hence set \(C=1\). Cross-multiplication against the third coordinate gives, among the exact fiber equations,
\[
\begin{aligned}
0&=4(A-1)(A^4+A^3+6A^2+A+1),\\
0&=4(15A^3-B^5+5B^2-3),\\
0&=5(39A^3-4B^3-7),\\
0&=-20B^2(A-1)(A^2+A+1).
\end{aligned}
\]
If \(A\ne1\), the first and fourth equations force either \(B=0\) or \(A^2+A+1=0\). In the first case the next two equations give simultaneously \(A^3=1/5\) and \(A^3=7/39\), impossible. In the second case \(A^3=1\), while
\[
A^4+A^3+6A^2+A+1=-4(A+1)
\]
modulo \(A^2+A+1\); this cannot vanish at a primitive cube root. Therefore \(A=1\). The third equation gives \(B^3=8\), and the second then gives \(B^2=4\), hence \(B=2\). Thus the set-theoretic fiber is \(\{p\}\).

It is reduced there: using the first equation divided by \(4\) and the third divided by \(5\), their Jacobian determinant at \((A,B)=(1,2)\) is \(-480\neq0\). A finite morphism with a reduced length-one fiber has generic degree one, so \(\phi_\Lambda\) is birational.

Finally, for a finite map of projective surfaces,
\[
(\phi_\Lambda^*H)^2=\deg(\phi_\Lambda)\deg X.
\]
Here \(\phi_\Lambda^*H=5L\) with \(L^2=1\), and \(\deg(\phi_\Lambda)=1\). Hence \(\deg X=25\). Since \(\mathbb P^2\) is normal and the map is finite birational, it is the normalization of \(X\).

## Verification
The accompanying `verify.py` reconstructs the six quintics on the affine chart \(c=1\), checks the target vector at \([1:2:1]\), verifies all five cross-multiplication identities and their stated factorizations, checks the branch exclusions used in the singleton-fiber proof, and verifies the nonzero Jacobian determinant \(-480\). It returns `VERIFY_OK` using exact integer polynomial arithmetic.

## Relationship to prior work
Kabat and Strycharz-Szemberg write down the six quintics, prove their system base-point free, and explicitly say that it would be interesting to investigate the companion surface, namely the image of \(\mathbb P^2\) in \(\mathbb P^5\) under this morphism. Their paper does not state the map's degree, birationality, normalization property, or the degree of that image. A later paper of Di Gennaro, Ilardi, Miró-Roig, Szemberg, and Szpond develops companion varieties for several root-system and Fermat-arrangement constructions; the inspected text and targeted searches did not locate this diminished-Fermat six-quintic map or the degree-25 normalization statement. The accepted claim is restricted to this explicit system.

## Limitations
No assertion is made that \(X\) is normal or smooth; indeed, identifying \(\mathbb P^2\) as its normalization leaves those questions open. No defining equations, singular-locus classification, conductor, or very-ampleness statement is claimed. The originality comparison is limited by the possibility of an unindexed source containing the same short calculation.

## References
1. J. Kabat and B. Strycharz-Szemberg, *Diminished Fermat-type arrangements and unexpected curves*, arXiv:2003.02596; C. R. Math. 358 (2020), 603--608, DOI:10.5802/crmath.77.
2. R. Di Gennaro, G. Ilardi, R. M. Miró-Roig, T. Szemberg, J. Szpond, *Companion varieties for root systems and Fermat arrangements*, arXiv:2101.07346; J. Pure Appl. Algebra 226 (2022), 107055.
