# Exact count and direct null-homotopy for complete height-two maps into longer crowns
## Finding
For integers \(p,q\ge 2\) and \(n\ge 3\), let \(P_{p,q}=A_p\oplus B_q\) be the complete height-two finite \(T_0\)-space with \(|A_p|=p\), \(|B_q|=q\), and every point of \(A_p\) below every point of \(B_q\). Let \(\mathfrak C_n\) be the \(2n\)-point crown with minimal points \(x_i\), maximal points \(y_i\), indices in \(\mathbb Z/n\), and covers \(x_i<y_i\) and \(x_{i+1}<y_i\).

Then
\[
|\operatorname{Map}(P_{p,q},\mathfrak C_n)|=n\bigl(3^p+3^q-2\bigr),
\]
and every continuous map \(P_{p,q}\to\mathfrak C_n\) is homotopic, as a map of finite spaces, to a constant map. Thus the unbased homotopy set \([P_{p,q},\mathfrak C_n]\) has exactly one element. The condition \(n\ge3\) is sharp: when \(p=q=n=2\), the source and target are both the four-point crown, and its identity is not homotopic to a constant.

## Assumptions and scope
Finite \(T_0\)-spaces are identified with their specialization posets, so continuity is equivalent to order preservation. The crown convention is that each target maximum \(y_i\) covers exactly \(x_i\) and \(x_{i+1}\). The theorem concerns direct continuous maps between these finite models; it does not assert that all classical homotopy classes between their order complexes are represented without subdivision.

For \(p,q\ge2\), the order complex of \(P_{p,q}\) is the complete bipartite graph \(K_{p,q}\), hence has first Betti number \((p-1)(q-1)\). The order complex of \(\mathfrak C_n\) is a cycle and is weakly equivalent to a circle. The finding is therefore a direct-realization obstruction: although the associated classical source and target have many nontrivial maps, every direct finite-space map to a crown of length at least six is null-homotopic in the finite-space sense.

## Proof
Write \(A=A_p\), \(B=B_q\), and let \(f:P_{p,q}\to\mathfrak C_n\) be order preserving. Since every \(a\in A\) satisfies \(a<b\) for every \(b\in B\), every value in \(f(A)\) must be below every value in \(f(B)\).

First suppose some \(a\in A\) has \(f(a)=y_i\). Then \(y_i\le f(b)\) for every \(b\in B\), hence \(f(b)=y_i\) for all \(b\in B\). Every value on \(A\) lies in \(\{x_i,x_{i+1},y_i\}\) and at least one equals \(y_i\). There are therefore
\[
n\bigl(3^p-2^p\bigr)
\]
maps of this type. Moreover \(f\le c_{y_i}\) pointwise, where \(c_{y_i}\) is the constant map at \(y_i\), so \(f\simeq c_{y_i}\).

Now assume no point of \(A\) maps to a target maximum, but some \(b\in B\) has \(f(b)=x_i\). Then every \(a\in A\) must map to \(x_i\), while every value on \(B\) lies in \(\{x_i,y_{i-1},y_i\}\), with at least one value equal to \(x_i\). This gives
\[
n\bigl(3^q-2^q\bigr)
\]
maps, and \(c_{x_i}\le f\), so again \(f\) is homotopic to a constant.

It remains to count rank-preserving maps, for which \(f(A)\subseteq\{x_i\}\) and \(f(B)\subseteq\{y_i\}\). Let \(S=f(A)\). If \(|S|=1\), say \(S=\{x_i\}\), then each point of \(B\) can independently map to either \(y_{i-1}\) or \(y_i\). This gives \(n2^q\) maps, all satisfying \(c_{x_i}\le f\).

Suppose instead \(|S|\ge2\). Every target maximum in \(f(B)\) must lie above every point of \(S\). Since \(n\ge3\), two distinct target minima have a common upper neighbor only when they are consecutive, and then that common upper neighbor is unique. Because each target maximum covers exactly two minima, nonempty \(f(B)\) forces
\[
S=\{x_i,x_{i+1}\}
\]
for a unique \(i\), and every point of \(B\) must map to \(y_i\). For a fixed \(i\), the number of maps \(A\to\{x_i,x_{i+1}\}\) using both values is \(2^p-2\). Hence this case contributes \(n(2^p-2)\) maps, and every one satisfies \(f\le c_{y_i}\).

Summing the four disjoint cases gives
\[
\begin{aligned}
|\operatorname{Map}(P_{p,q},\mathfrak C_n)|
&=n(3^p-2^p)+n(3^q-2^q)+n2^q+n(2^p-2)\\
&=n(3^p+3^q-2).
\end{aligned}
\]
Every map has been shown pointwise comparable with a constant map. Pointwise comparable maps between finite spaces are homotopic. The constant maps form a copy of the connected crown \(\mathfrak C_n\), so all constants are homotopic to one another. Therefore all maps \(P_{p,q}\to\mathfrak C_n\) lie in one homotopy class.

For sharpness, \(\mathfrak C_2=P_{2,2}\) is a minimal finite space with no beat points. Stong's rigidity theorem for cores implies that the only self-map of a minimal finite space homotopic to its identity is the identity itself. Hence the identity of \(\mathfrak C_2\) is not homotopic to a constant.

## Verification
The standalone script `artifacts/verify.py` exhaustively enumerates all functions for every \(1\le p,q\le3\) and \(3\le n\le5\), keeps exactly the order-preserving ones, verifies the formula, classifies every surviving map into one of the four proof cases, and checks the claimed pointwise comparison with a constant map. It also computes the comparability components of \(\operatorname{Map}(\mathfrak C_2,\mathfrak C_2)\): there are \(36\) maps, with component sizes \(32,1,1,1,1\), and the identity is outside the constant component. The replay ends with:

`VERIFY_OK exhaustive_parameter_triples=27 sharp_n2_maps=36 sharp_n2_components=[1, 1, 1, 1, 32]`

These finite checks test the case partition and boundary behavior. They are not used as an infinite proof.

## Relationship to prior work
Barmak and Minian establish the finite-space/poset framework used here, including that continuous maps of finite spaces are precisely order-preserving maps, and they characterize minimal finite models of finite graphs. Their first public arXiv version is dated 2006-11-06. May's finite-space notes identify homotopy classes with path components of finite function spaces, identify the compact-open specialization order with pointwise order for finite spaces, and show that pointwise comparable maps are homotopic.

Farley's 1995 paper gives exact enumerations for maps between fences and crowns. Its stated scope is the class whose source and target are fences or crowns; a complete height-two source \(P_{p,q}\) is not in that class except for the special four-point case \(p=q=2\). Thus Farley's formulas do not give the general count above, and the paper does not address the finite-space homotopy collapse proved here.

The closest previously recorded findings in the present corpus concern maps in the opposite direction from crowns to complete height-two spaces, maps between crowns, and counts for maps between complete height-two spaces. None implies the present source-target direction or the formula \(n(3^p+3^q-2)\).

## Limitations
The theorem is about direct finite-space maps. It does not classify maps after subdividing the source, nor does it identify the full homotopy type or Stong core of the mapping space. The exact formula uses the local incidence property of a crown with \(n\ge3\); it does not extend unchanged to the four-point crown. The originality search cannot exclude unpublished or poorly indexed observations, so the residual originality risk is bibliographic rather than mathematical.

## References
1. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156v1, first public 2006-11-06; later Journal of Homotopy and Related Structures 2 (2007), 127-140.
2. J. P. May, *Finite Spaces and Larger Contexts*, Chapter 2, especially the sections on function spaces, pointwise order, and homotopies.
3. J. D. Farley, *The Number of Order-Preserving Maps between Fences and Crowns*, Order 12 (1995), 5-44, DOI: 10.1007/BF01108588.
