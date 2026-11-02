# A uniform normalization theorem for diminished-Fermat companion surfaces

## Finding

For every integer \(m\ge 3\) over \(\mathbb C\), put \(d=2m-1\) and define six forms of degree \(d\) in \(a,b,c\):
\[
\begin{aligned}
u_1&=a^{m-1}(dc^m-a^m), &u_2&=b^{m-1}(b^m-dc^m),\\
u_3&=c^{m-1}(c^m-da^m), &u_4&=c^{m-1}(db^m-c^m),\\
u_5&=d b^{m-1}(a^m-c^m), &u_6&=d a^{m-1}(c^m-b^m).
\end{aligned}
\]
Let \(\phi_m:\mathbb P^2\to\mathbb P^5\) be their projective map, and let \(Y_m\) be its reduced scheme-theoretic image. Then **\(\phi_m:\mathbb P^2\to Y_m\) is finite and birational**, hence is the normalization. The degree is
\[
\deg Y_m=(2m-1)^2.
\]
The image \(E_m=\phi_m(\{c=0\})\) is a rational curve of degree \(2m-1\), and \(Y_m\) is **nonnormal at the generic point of \(E_m\)**. This applies uniformly to every integer \(m\ge3\); the genuinely new range relative to the closest accessible special-case computations is \(m\ge4\).

## Assumptions and scope

The ground field is \(\mathbb C\), or any algebraically closed characteristic-zero field. The six coordinates are exactly the coefficient forms in Kabat--Strycharz-Szemberg's diminished-Fermat unexpected-curve construction. The statement concerns the **image surface** of this specific complete six-coordinate morphism, not the singularities of its individual unexpectedly singular plane curves. The reduced image is integral as the image of \(\mathbb P^2\).

## Proof

**1. Base-point freeness and finiteness.** Suppose all six forms vanished. If \(a=0\), then \(u_3=c^{2m-1}=0\) implies \(c=0\), and \(u_2=b^{2m-1}=0\) implies \(b=0\), a contradiction. Otherwise \(a\ne0\). Vanishing of \(u_6\) gives \(c^m=b^m\). If \(b=0\), then \(c=0\) and \(u_1=-a^d\ne0\). If \(b\ne0\), then \(u_2=(1-d)b^d\ne0\) since \(m\ge3\) and the characteristic is zero. Thus \(\phi_m\) is a morphism, with \(\phi_m^*\mathcal O_{\mathbb P^5}(1)=\mathcal O_{\mathbb P^2}(d)\). A positive-dimensional fiber would contain a projective curve on which this ample line bundle has degree zero, which is impossible. Hence the proper, quasi-finite map \(\phi_m\) is finite onto its image.

**2. A uniquely lifted image divisor.** On the line \(L=\{c=0\}\) the coordinate forms become
\[
(-a^d,\ b^d,\ 0,\ 0,\ da^m b^{m-1},\ -da^{m-1}b^m).
\]
At its generic point \([1:t:0]\), \(t\) is transcendental and the image-rational function
\[
T=-u_6/u_5
\]
restricts to \(t\). Thus \(\phi_m|_L\) is generically injective, and \(E_m=\phi_m(L)\) is an integral rational curve. Moreover, no generic point of any other source divisor maps to \(E_m\). Indeed, any point with \(u_3=u_4=0\) and \(c\ne0\) must satisfy \(c^m=da^m=db^m\), whence \(a^m=b^m\). On this locus the same output ratio has \(T=b/a\) (all denominators are nonzero), so \(T^m=1\). This is impossible at the generic point of \(E_m\), where \(T=t\) is transcendental. Points with \(c=0\) are distinguished generically by \(T=b/a\). Therefore the divisorial valuation of \(\mathbb C(Y_m)\) associated with \(E_m\), taken on its normalization, has a **unique extension** to the function field \(\mathbb C(\mathbb P^2)\), centered on \(L\).

**3. Adjacent orders force birationality.** Work on \(a=1\) with \(b=t,c=s\) and take the order \(v=\operatorname{ord}_{s=0}\) on \(\mathbb C(t,s)\). The output functions
\[
G=u_3/u_1=\frac{s^{m-1}(s^m-d)}{ds^m-1},
\qquad
T=-u_6/u_5=\frac{t^m-s^m}{t^{m-1}(1-s^m)}
\]
satisfy \(v(G)=m-1\) and \(T\bmod s=t\). A second function in \(\mathbb C(Y_m)\) is
\[
H=1+d\frac{u_1}{u_5}T^{m-1}.
\]
Writing \(z=s^m\), one has the exact identity
\[
H=\frac{t^{m(m-1)}(1-z)^m+(dz-1)(t^m-z)^{m-1}}{t^{m(m-1)}(1-z)^m}.
\]
The numerator has constant term zero and coefficient of \(z\) equal to
\[
(m-1)t^{m(m-1)}(1+t^{-m}),
\]
which does not vanish in \(\mathbb C(t)\). Hence \(v(H)=m\). Since \(\gcd(m-1,m)=1\), the restriction of \(v\) to \(\mathbb C(Y_m)\) has ramification index one. Its residue field already contains \(T\bmod s=t\), so the residue degree is also one. There is only one extension of the corresponding divisorial valuation, by Step 2. The defect-free fundamental equality for finite extensions of characteristic-zero discrete-valuation fields therefore gives
\[
[\mathbb C(\mathbb P^2):\mathbb C(Y_m)]=1.
\]
Thus \(\phi_m\) is birational, and since \(\mathbb P^2\) is normal it is the normalization of \(Y_m\).

**4. Degrees and a nonnormal divisor.** For a finite birational map, two general target hyperplanes pull back to two curves of degree \(d\) on \(\mathbb P^2\), giving \(\deg Y_m=d^2\). The restriction to \(L\) is generically of degree one and pulls back \(\mathcal O(1)\) to \(\mathcal O_L(d)\), so \(\deg E_m=d\). At a generic point of \(L\), each affine coordinate ratio of the image varies transversally to \(L\) only in powers of \(s^{m-1}\) or \(s^m\). Because \(m\ge3\), all transverse first derivatives vanish. The derivative of \(T|_L=t\) along \(L\) is nonzero, so \(\operatorname{rank}(d\phi_m)=1\) at its generic point. Were \(Y_m\) normal at the generic point of \(E_m\), its finite birational normalization would be an isomorphism there, contradicting this rank drop. Thus \(E_m\) lies in the codimension-one nonnormal locus.

## Verification

The standalone script `verify_valuation.py` checks the exact numerator and coefficient identities with rational arithmetic for all integers \(3\le m\le18\) and several generic rational values of \(t\). It reports `VALUATION_IDENTITY_OK`. A separately implemented finite-field script `verify_finite_images.py` enumerates all of \(\mathbb P^2(\mathbb F_{101})\) for \(3\le m\le7\) and checks the claimed uniqueness of boundary fibers whenever \(t^m\ne1\); it reports `FINITE_IMAGE_CHECK_OK`. Both tests were run against the delivered file paths. Their finite ranges are **checks**, not an infinite proof; the unrestricted proof is Steps 1--4 above.

## Relationship to prior work

Kabat and Strycharz-Szemberg proved base-point freeness of these six forms for arbitrary \(m\ge3\) (their Lemma 9) and raised questions about companion surfaces. That statement alone does not imply birationality, surface degree, or nonnormality. A separately indexed result establishes normalization and degree \(25\) for the first case \(m=3\). A prior special-case calculation also describes its differential rank-drop locus and generic cusp singularities. Thus the \(m=3\) normalization and nonnormality assertions are not claimed as original here. Neither special-case statement implies the uniform theorem for every \(m\ge4\); the proof uses the two adjacent divisorial valuations for arbitrary \(m\). Di Gennaro et al. study other Fermat and root-system companion maps; their inspected constructions do not contain this six-coordinate arbitrary-\(m\) family. Szpond's work on a different unexpected-quartic companion surface supplies related background, not the present six-form family. Priority against unindexed earlier calculations remains subject to further bibliographic checking.

## Limitations

No assertion is made about the complete singular locus or conductor of \(Y_m\), analytic cusp normal forms, positive characteristic, projective normality, or the images of other coordinate lines. The proved nonnormality is at the generic point of the explicitly described curve \(E_m\). The self-review is not an independent external audit.

## References

1. J. Kabat and B. Strycharz-Szemberg, *Diminished Fermat-type arrangements and unexpected curves*, arXiv:2003.02596, first posted 2020-03-05; *Comptes Rendus Mathématique* 358 (2020), 603--608, DOI: 10.5802/crmath.77. See Lemma 9 and Sections 2.1, 3.1.
2. J. Szpond, *Unexpected curves and Togliatti-type surfaces*, *Mathematische Nachrichten* 293 (2020), 158--168, DOI: 10.1002/mana.201800455 (different companion construction).
3. *The diminished-Fermat quintic companion map normalizes a degree-25 surface*, indexed mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-the-diminished-fermat-quintic-companion-map-normalizes-a-degree--f47df59b3142 (specific case \(m=3\); indexed summary consulted).
4. R. Di Gennaro, G. Ilardi, R. M. Miró-Roig, T. Szemberg, and J. Szpond, *Companion varieties for root systems and Fermat arrangements*, arXiv:2101.07346; *Journal of Pure and Applied Algebra* 226 (2022), 107055, DOI: 10.1016/j.jpaa.2022.107055 (different companion constructions).
