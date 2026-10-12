# Fixed-space spectrum of automorphisms of the two-generator exterior algebra over odd finite fields
## Finding
Let \(q\) be an odd prime power and let
\[
E_q=\Lambda_{\mathbb F_q}(\mathbb F_q^2)
\]
be the exterior algebra on a two-dimensional vector space. Thus \(E_q\) has basis \(1,x,y,z\), where \(z=x\wedge y\), \(x^2=y^2=z^2=0\), and \(yx=-xy\). For \(d\in\{1,2,3,4\}\), write \(N_d(q)\) for the number of \(\mathbb F_q\)-algebra automorphisms with \(d\)-dimensional fixed subspace. Then
\[
N_1(q)=q^3(q+1)(q-2)^2,
\]
\[
N_2(q)=2q^5-q^4-4q^3-q^2+q,
\]
\[
N_3(q)=(q+1)(q^2-1),\qquad N_4(q)=1.
\]
There are no other fixed-space dimensions. The four multiplicities sum to
\[
|\operatorname{Aut}(E_q)|=q^2|\operatorname{GL}_2(\mathbb F_q)|
=q^3(q-1)^2(q+1).
\]
Moreover Burnside's lemma gives exactly
\[
3q
\]
automorphism orbits on the elements of \(E_q\).

## Assumptions and scope
The field is an arbitrary finite field of odd characteristic. The restriction to odd characteristic matches the classical exterior-algebra automorphism literature inspected here and keeps the anticommutation relation \(yx=-xy\) distinct from the characteristic-two case. No algebraic closure or primeness of \(q\) is assumed.

An automorphism fixes the identity. If \(V=\langle x,y\rangle\) and \(z=x\wedge y\), then every automorphism is uniquely determined by a matrix \(A\in\operatorname{GL}_2(\mathbb F_q)\) and a linear functional \(u\in V^*\): for \(v\in V\),
\[
\phi(v)=Av+u(v)z,\qquad \phi(z)=\det(A)z.
\]
Hence \(|\operatorname{Aut}(E_q)|=q^2|\operatorname{GL}_2(q)|\).

## Proof
Write \(\delta=\det(A)\). A general element of the radical is \(v+t z\) with \(v\in V\) and \(t\in\mathbb F_q\). It is fixed by \(\phi\) exactly when
\[
(A-I)v=0,\qquad u(v)+(\delta-1)t=0.
\]
The scalar line \(\mathbb F_q1\) is always fixed, so the fixed-space dimension in the whole algebra is one plus the nullity of this system on \(V\oplus\mathbb F_qz\).

First suppose \(\delta\ne1\). Then \(t\) is uniquely determined by \(v\in\ker(A-I)\). Thus the radical fixed-space nullity is \(\dim\ker(A-I)\). For each fixed \(\delta\ne1\), matrices with eigenvalue \(1\) are conjugate to \(\operatorname{diag}(1,\delta)\); there are \(q(q+1)\) of them. Since every determinant fiber in \(\operatorname{GL}_2(q)\) has \(q(q^2-1)\) elements, across the \(q-2\) values of \(\delta\ne1\) the counts are
\[
q(q+1)(q-2)
\]
with one-dimensional \(1\)-eigenspace and
\[
q(q+1)(q-2)^2
\]
with no \(1\)-eigenvectors. Multiplying by the \(q^2\) choices of \(u\) contributes respectively to \(N_2\) and \(N_1\).

Now suppose \(\delta=1\). If \(A=I\), then \(u=0\) gives radical nullity \(3\), while each of the \(q^2-1\) nonzero functionals gives radical nullity \(2\). If \(A\ne I\) is unipotent, then \(\ker(A-I)\) is a line. There are \(q^2-1\) such matrices in \(\operatorname{SL}_2(q)\). Exactly \(q\) functionals vanish on that line, giving radical nullity \(2\); the other \(q^2-q\) give radical nullity \(1\). Finally, the remaining
\[
q(q^2-q-1)
\]
matrices in \(\operatorname{SL}_2(q)\) have no nonzero fixed vector, and for every \(u\) the radical nullity is \(1\).

Adding these disjoint strata gives
\[
N_3=(q^2-1)+q(q^2-1)=(q+1)(q^2-1),
\]
\[
N_2=q^3(q+1)(q-2)+q^3(q^2-q-1)+q(q-1)(q^2-1)
=2q^5-q^4-4q^3-q^2+q,
\]
and the formulas for \(N_1\) and \(N_4\) above. Their sum is the full automorphism-group order.

For the orbit statement, the scalar part of an element is invariant. Fix a scalar \(c\). In the radical, zero is one orbit. Every nonzero multiple of \(z\) lies in one orbit because \(\det:\operatorname{GL}_2(q)\to\mathbb F_q^\times\) is surjective. Finally, every radical element whose image in \(V\) is nonzero lies in one orbit: \(\operatorname{GL}_2(q)\) is transitive on \(V\setminus\{0\}\), and the free functional \(u\) adjusts the \(z\)-coordinate. Thus there are exactly three radical orbit types for each of the \(q\) scalar parts, hence \(3q\) element-orbits. Equivalently,
\[
\frac{N_1q+N_2q^2+N_3q^3+N_4q^4}{|\operatorname{Aut}(E_q)|}=3q.
\]

## Verification
The standalone verifier exhaustively enumerates all automorphisms over the prime fields \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\). For each \(A\in\operatorname{GL}_2\) and each \(u\in V^*\), it builds the induced linear map on \(\langle x,y,z\rangle\), computes the nullity of \(\phi-I\), and checks the four formulas, the full group order, and the Burnside orbit count. It also directly enumerates element-orbits for \(q=3\). These computations are finite consistency checks; the proof above establishes the theorem for every odd prime power.

## Relationship to prior work
Djoković's 1978 paper studies automorphisms of finite-dimensional exterior algebras over arbitrary fields of characteristic different from \(2\). In its automorphism section it proves the split exact-sequence description of the full automorphism group and, later, its finer semidirect decomposition. That work supplies the classical structural context, but it does not enumerate finite-field automorphisms by fixed-space dimension.

Bavula's 2007 Grassmann-algebra paper, first public on 29 April 2007, treats derivations, skew derivations, the \(\operatorname{Aut}\)-module of derivations, and certain automorphism orbits of normal elements. Its indexed classification begins with MSC \(15A75\), which places the anchor in exterior/Grassmann algebra. The inspected statements do not give the four fixed-space fibers above.

A recent published-finding corpus finding on weight-zero Rota--Baxter operators on the four-dimensional exterior algebra over \(\mathbb F_2\) concerns conjugacy classes of operators rather than the fixed-space distribution of the algebra's own automorphisms. Targeted published-finding corpus searches for Grassmann/exterior automorphism fixed spaces and element-orbit counts returned no equivalent or stronger statement.

## Limitations
The theorem is restricted to the two-generator exterior algebra and odd finite fields. It does not classify automorphism conjugacy classes, and it does not address higher exterior rank, where the unipotent part of the automorphism group is much larger. Characteristic two is intentionally excluded rather than inferred from the odd-characteristic argument. The computational verifier tests prime fields only; extension fields are covered by the symbolic field-independent proof, not by enumeration.

## References
1. D. Ž. Djoković, “Derivations and automorphisms of exterior algebras,” Canadian Journal of Mathematics 30 (1978), 1336–1344, DOI 10.4153/CJM-1978-111-5.
2. V. V. Bavula, “Derivations and skew derivations of the Grassmann algebras,” arXiv:0704.3850, first submitted 29 April 2007; Journal of Algebra and Its Applications 8 (2009), 805–827, DOI 10.1142/S0219498809003655.
