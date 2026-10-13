# Equianharmonic hyperflex geometry of the order-\(48\) quartic
## Finding
Over \(\mathbb C\), consider the smooth plane quartic
\[
C_48:x^4+y^4+xz^3=0.
\]
Its hyperflex divisor is the four-point scheme
\[
H=C_48\cap\{y=0\}=\{[a:0:1]:a^4+a=0\}.
\]
For every root \(a\) of \(a^4+a\), the tangent line is
\[
L_a:x-az=0,
\]
and restriction of the quartic equation to \(L_a\) is exactly \(y^4\). Hence \(L_a\) has intersection multiplicity four with \(C_48\) at \([a:0:1]\).

These are all hyperflexes. The four hyperflex points are collinear on \(y=0\), while their tangent lines are concurrent at \([0:1:0]\). Writing the roots as \(0,-1,\alpha,1-\alpha\) with \(\alpha^2-\alpha+1=0\), their cross-ratio is \(\alpha\). Thus the four-point divisor is equianharmonic and its projective stabilizer on \(y=0\cong\mathbb P^1\) is \(A_4\).

The action of \(\operatorname{Aut}(C_48)\) on this intrinsic hyperflex divisor yields the exact sequence
\[
1\longrightarrow C_4\longrightarrow\operatorname{Aut}(C_48)\longrightarrow A_4\longrightarrow1,
\]
with kernel
\[
C_4=\{[x:y:z]\mapsto[x:\zeta y:z]:\zeta^4=1\}.
\]
Thus the abstract \(C_4\)-by-\(A_4\) structure recorded for this quartic is realized geometrically by the tetrahedral symmetry of its equianharmonic hyperflex divisor.

## Assumptions and scope
The ground field is \(\mathbb C\). Automorphisms are projective automorphisms of the canonical plane quartic. The input from the literature is that this quartic is smooth, has automorphism group of order \(48\) with abstract structure \(C_4\mathbin{\odot}A_4\), and has exactly four hyperosculating lines. The assertions locating the four contact points, proving that no other hyperflex occurs, identifying the equianharmonic cross-ratio, and identifying the kernel and quotient action are established here directly.

## Proof
Work first on the affine chart \(z=1\), where
\[
f(x,y)=x^4+y^4+x.
\]
At a point \((a,b)\in C_48\), use the tangent direction \((4b^3,-(4a^3+1))\). Substitution into \(f\) makes the coefficient of the linear parameter vanish. The quadratic coefficient is
\[
6b^2\bigl(16a^6+8a^3+16a^2b^4+1\bigr),
\]
and the cubic coefficient is
\[
-4b\bigl(64a^9+48a^6+12a^3-64ab^8+1\bigr).
\]
If \(b\ne0\), the curve equation gives \(b^4=-a^4-a\). The vanishing of the quadratic coefficient then becomes \(1-8a^3=0\). Under that relation the remaining cubic factor reduces to \(-27/4\), so it cannot vanish. Therefore every affine hyperflex has \(b=0\), hence \(a^4+a=0\).

Conversely, if \(a^4+a=0\), the tangent is \(x-az=0\), and substitution gives \(y^4\), so the contact order is four. At infinity, on the chart \(x=1\), the equation is \(1+u^4+v^3=0\). Each point with \(v=0\) has tangent \(u=\text{constant}\), and restriction to that tangent is \(v^3\), so those points are flexes of contact order three, not hyperflexes. This proves the exact hyperflex set.

Factor
\[
a^4+a=a(a+1)(a^2-a+1).
\]
If \(\alpha^2-\alpha+1=0\), the four parameters are \(0,-1,\alpha,1-\alpha\), and the cross-ratio \((0,-1;\alpha,1-\alpha)\) equals \(\alpha\). This is the equianharmonic case. Among the \(24\) permutations of four marked points, exactly \(12\) preserve the resulting cross-ratio class, so the projective stabilizer is the unique order-\(12\) subgroup of \(S_4\), namely \(A_4\).

Finally, every automorphism preserves hyperflexes and therefore acts on \(H\). An automorphism fixing all four points fixes the line \(y=0\) pointwise. After a scalar normalization its matrix has the form
\[
[x:y:z]\longmapsto[x+py:qy:z+ry].
\]
Preservation of \(x^4+y^4+xz^3\) forces successively \(p=0\) from the \(x^3y\) coefficient, \(r=0\) from the \(xz^2y\) coefficient, and \(q^4=1\). Thus the kernel has order four and is exactly the displayed central \(C_4\). Since the full automorphism group has order \(48\), the image on \(H\) has order \(12\); it is therefore the full \(A_4\) stabilizer of the equianharmonic four-set.

## Verification
The bundled script `verification/verify.py` uses exact symbolic arithmetic. It checks the tangent expansion, the elimination proving there is no affine hyperflex with \(b\ne0\), the contact orders at the four finite points and at infinity, the equianharmonic cross-ratio identity, and the coefficient comparison determining the kernel. Running it with SymPy \(1.14.0\) prints `VERIFY_OK hyperflexes=4 collinear=y=0 tangents=4_concurrent equianharmonic=A4 kernel=C4`.

## Relationship to prior work
Janasz determines the quartic \(C_48\), recalls \(\operatorname{Aut}(C_48)=C_4\mathbin{\odot}A_4\), computes the dual curve, concludes that there are exactly four hyperosculating lines, gives equations for all \(28\) bitangents, and notes that the four hyperosculating lines are concurrent. The inspected paper does not locate the four hyperflex contact points as a divisor, identify their cross-ratio as equianharmonic, or realize the abstract \(A_4\) quotient as the projective action on that divisor. The earlier Janasz--Pokora--Zieliński paper studies bitangent arrangements of symmetric quartics and provides the closest arrangement-level context, but the inspected material does not imply this divisor-and-action description.

Targeted searches using the exact quartic equation, the names \(C_48\), hyperflex/hyperosculating aliases, equianharmonic four-point terminology, and the \(C_4\)-by-\(A_4\) action found no published statement equivalent to the claim.

## Limitations
The result concerns the complex canonical plane model and the induced action on the hyperflex divisor. It does not classify reductions in positive characteristic, determine the full bitangent permutation representation, or claim that the abstract group structure itself is new. An older equivalent description in classical genus-three terminology remains a residual originality risk.

## References
1. M. Janasz, *On symmetric plane quartic curves*, arXiv:2406.07015v1, first posted 2024-06-11; Taiwanese Journal of Mathematics 29 (2025), DOI:10.11650/tjm/240707.
2. M. Janasz, P. Pokora, M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, arXiv:2308.16514, first posted 2023-08-31; Fundamenta Mathematicae 268 (2025), DOI:10.4064/fm240105-13-12.
3. C. T. C. Wall, *Geometry of quartic curves*, Math. Proc. Cambridge Philos. Soc. 117 (1995), 415--423.
