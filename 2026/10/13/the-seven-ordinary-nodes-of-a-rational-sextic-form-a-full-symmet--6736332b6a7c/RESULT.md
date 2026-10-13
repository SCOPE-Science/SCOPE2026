# The seven ordinary nodes of a rational sextic form a full symmetric Galois orbit

## Finding
Let \(C\subset\mathbb P^2_{\mathbb Q}\) be the integral rational sextic of Gimigliano and Idà, Example 6.1, with normalization parametrization
\[
\phi([s:t])=[s^6+t^6:-s^5t+3st^5-s^3t^3:9s^2t^4+s^4t^2-s^3t^3].
\]
Its known geometric singularity basket is one \(A_5\) and seven ordinary nodes \(A_1\). **The seven nodes form a single orbit of the absolute Galois group of \(\mathbb Q\), each with residue-field degree \(7\). The minimum common field of definition of all seven individual nodes is a Galois extension with group \(S_7\).** The \(A_5\) point is the rational point \([1:0:0]\).

More precisely, for each ordinary node let \(a,b\) denote the two parameters on the affine chart \(t\ne0\) of its normalization fiber, where \(a=s/t\) and \(b=s/t\) on the respective preimages. The symmetric product \(v=ab\) takes the seven distinct roots of
\[
P(v)=412v^7+680v^6+1083v^5-2647v^4-9077v^3-14481v^2-14886v-3708.
\]
For a node \(Q_v\), its residue field satisfies \(\mathbb Q(Q_v)=\mathbb Q(v)\). Therefore the common node-splitting field is precisely the splitting field of \(P\).

## Assumptions and scope
Everything is over characteristic zero, with the displayed proper, base-point-free parametrization. The ordinary-node and \(A_5\) labels are geometric singularities over \(\overline{\mathbb Q}\), not real-point counts. The source proves the normalization is generically one-to-one and the singular locus has exactly those eight points; its singularity census is prior work. The new arithmetic result classifies fields of definition and Galois action on that entire finite singular configuration. It makes no claim about other rational sextics or about Galois groups of the individual normalization parameters \(a\) and \(b\).

## Proof
Write \(z=s/t\) and
\[
f(z)=(1+z^6,\ 3z-z^3-z^5,\ 9z^2-z^3+z^4).
\]
The affine chart omits the single normalization parameter at infinity. Its image is \(\phi(\infty)=\phi(0)=[1:0:0]\), the known \(A_5\) point; \(\gcd(3z-z^3-z^5,9z^2-z^3+z^4)=z\) confirms there are no further finite parameters over this point. For distinct finite parameters \(a,b\), equality \([f(a)]=[f(b)]\) means the three coordinates of \(f(a)\wedge f(b)\) vanish. Dividing each coordinate by \(a-b\) gives symmetric polynomials. In \(u=a+b\), \(v=ab\), they are exactly
\[
\begin{aligned}
H_{01}&=3u^4v+u^4-u^2v^3-9u^2v^2-3u^2v+u^2-v^5+v^4+3v^3+v^2-v-3,\\
H_{02}&=9u^3v^2-u^3-u^2v^3+u^2+uv^4-18uv^3+2uv-9u+v^4-v,\\
H_{12}&=-v(9u^2v+3u^2-uv^2-3u+v^3-10v^2+6v+27).
\end{aligned}
\]
Exact rational polynomial division and a reduced lexicographic Gröbner-basis calculation for \(\langle H_{01},H_{02},H_{12}\rangle\subset\mathbb Q[u,v]\), with \(u\) preceding \(v\), yield the monic basis \(\{u+Q(v)/51168936,\ P(v)/412\}\), where
\[
\begin{aligned}
Q(v)={}&8644996v^6+9291068v^5+43497417v^4-54802504v^3\\
&-181768175v^2-392557278v-458223588.
\end{aligned}
\]
Thus the finite unordered coincident-parameter pairs have coordinate ring \(\mathbb Q[v]/(P)\), with \(u=-Q(v)/51168936\). Exact polynomial greatest-common-divisor calculations give
\[
\gcd\big(P,\operatorname{numerator}(u(v)^2-4v)\big)=1,
\]
so their two parameters are genuinely distinct. Irreducibility below shows \(P\) has seven different roots. By the established geometric singularity census, each of the resulting seven pairs is exactly the normalization fiber over one ordinary node, and the seven nodes are distinct. Equivalently, this also follows from the source's seven-node count and the genus budget \(\delta(A_5)+7\delta(A_1)=3+7=10=p_a(C)\).

The coordinate sum \(f(a)+f(b)\) represents their common projective image whenever it is nonzero. Its first component is
\[
u^6-6u^4v+9u^2v^2-2v^3+2,
\]
and its numerator after substituting \(u(v)\) is relatively prime to \(P\). Hence every node \(Q_v\) is defined over \(\mathbb Q(v)\). Conversely, the normalization and its map to \(C\) are defined over \(\mathbb Q\). Since \(Q_v\) is an ordinary node, its inverse-image fiber is a unique reduced unordered pair, defined as a degree-two scheme over \(\mathbb Q(Q_v)\). Its elementary symmetric functions, in particular \(v=ab\), lie in that field. This proves \(\mathbb Q(Q_v)=\mathbb Q(v)\), rather than merely a divisibility statement on residue degrees.

For the Galois group, reduction of \(P\) modulo \(79\) is irreducible of degree \(7\). Therefore \(P\) is irreducible over \(\mathbb Q\), and its Galois group acts transitively on seven roots. Modulo \(199\) one has the squarefree factorization
\[
P(v)\equiv412(v+35)(v+68)(v+80)(v-60)(v-39)(v^2-7v+94)\pmod{199}.
\]
The quadratic discriminant is \(71\) modulo \(199\), a nonsquare since \(71^{99}\equiv-1\pmod{199}\). The factor degrees therefore give a Frobenius permutation of cycle type \((2,1,1,1,1,1)\), a transposition. A transitive group of prime degree \(7\) is primitive; the conjugates of a transposition in a primitive permutation group generate the full symmetric group (their transposition-edge graph must be connected). Consequently \(\operatorname{Gal}(P/\mathbb Q)=S_7\), and the same holds for the common node-splitting field. The point \([1:0:0]\) is plainly rational.

## Verification
Run the included file `verify.py` with Python 3 and SymPy: `python verify.py`. It regenerates the divided wedge polynomials, checks their exact symmetric expressions, recomputes the Gröbner basis and the resultant degree-seven polynomial, checks separability and absence of diagonal parameter pairs, proves the relevant coordinate sum is nonzero, verifies irreducibility over \(\mathbb F_{79}\), and checks the explicit factorization and quadratic nonsquareness over \(\mathbb F_{199}\). The calculations are exact rational and finite-field identities; the Galois-theoretic argument above converts them into a theorem over \(\mathbb Q\). The source provides an independent geometric count and local-type verification.

## Relationship to prior work
Gimigliano and Idà construct the sextic, establish its \(A_5\) point, prove the normalization is birational, and classify the other seven singular points as nodes. Those geometric facts are **not** new here. Their Example 6.1 and the corresponding open-access version do not give the residue fields or arithmetic permutation action of those seven nodes. The new conclusion distinguishes the geometry of seven points from their arithmetic descent: the number and local types alone cannot determine whether the node scheme consists of rational points, smaller Galois orbits, or a single \(S_7\)-orbit.

## Limitations
The finding concerns this exact rational sextic, not a Zariski-open family or an arbitrary curve with basket \(A_5+7A_1\). It determines the splitting field of the **node coordinates**, not the potentially larger field splitting all fourteen individual normalization preimages. The claimed bibliographic novelty is based on the inspected primary sources and targeted searches, not a proof that every historical or unindexed treatment was found. The proof uses exact computable Gröbner and finite-field certificates, with supplied executable checks; no independent external audit has been performed.

## References
1. A. Gimigliano and M. Idà, *Remarks on double points of plane curves*, arXiv:2201.06032v1, first posted 2022-01-16, especially §6, Example 6.1. https://arxiv.org/html/2201.06032v1
2. A. Gimigliano and M. Idà, *Remarks on double points of plane curves*, *Geometriae Dedicata* **217**, article 5 (2023), online 2022-10-28, DOI:10.1007/s10711-022-00732-4. https://link.springer.com/article/10.1007/s10711-022-00732-4
3. A. Bernardi, A. Gimigliano and M. Idà, *Singularities of plane rational curves via projections*, *Journal of Symbolic Computation* **86** (2018), 189–212, used as geometric background and cited by [1]; its content is not claimed as a separately inspected originality exclusion.
