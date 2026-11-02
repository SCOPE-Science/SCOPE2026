# A genus-three tangent discriminant for plane-filling curves

## Finding
Let \(q\) be any odd prime power, \(k\in\mathbb F_q\), and set
\[
G_k(T)=T^7+kT^3-1,\qquad
C_{q,k}:\quad X^2(X^qY-XY^q)+Y^2(Y^qZ-YZ^q)+(Z^2+kX^2)(Z^qX-ZX^q)=0.
\]
Assume that \(G_k\) has no root in \(\mathbb F_q\). Let the dual plane have coordinates \([U:V:W]\), so that \([U:V:W]\) represents the line \(UX+VY-WZ=0\). Define
\[
D_k:\quad \Delta_k(U,V,W)=UW^3+V^3W-kUVW^2-kV^4-U^3V=0.
\]
Then \(D_k\) is a smooth geometrically integral plane quartic of genus three. Each \(\mathbb F_q\)-point of \(C_{q,k}\) is smooth. Its tangent contact with an \(\mathbb F_q\)-line is at most three. The \(\mathbb F_q\)-lines divide into \(N_j\) lines tangent at exactly \(j\) distinct \(\mathbb F_q\)-points, for \(j=0,1,2\). A one-contact line has contact order exactly three; a two-contact line is tangent of order exactly two at each of its two contact points. Their exact counts are
\[
N_1=\#D_k(\mathbb F_q),\qquad
N_0=N_2=\frac{q^2+q+1-\#D_k(\mathbb F_q)}2.
\]
In particular, the number of rational inflection points of \(C_{q,k}\) is \(\#D_k(\mathbb F_q)\), and the number of rational two-contact tangent lines satisfies
\[
\left|N_2-\frac{q^2}{2}\right|\leq 3\sqrt q.
\]
The smoothness statement for the quartic is a consequence of the stronger geometric fact: over every algebraically closed field of odd characteristic, \(D_k\) is smooth if and only if \(T^7+kT^3-1\) is squarefree.

## Assumptions and scope
The prime power \(q\) may be a nontrivial power of its characteristic (for example, \(9\), \(25\), or \(49\)); only odd characteristic is required. The coefficient \(k\) must be in the defining finite field and \(G_k\) must lack a defining-field root. The source proves that this root condition is equivalent to smoothness of \(C_{q,k}\) at every defining-field rational point, and that at least one such coefficient exists for every finite field. This theorem **does not assert** that \(C_{q,k}\) is geometrically smooth or integral: geometric smoothness of the entire plane-filling curve is the source's separate conjecture. All asserted tangent contacts are at smooth, rational points; geometric tangent lines lacking rational contacts are not counted. All algebraic curves are projective.

## Proof
**1. Residual quadratic on every rational line.** Write \(B(s,t)=s^qt-st^q\). For the line \(Z=uX+vY\), substitute \([X:Y:Z]=[s:t:us+vt]\), using \(u^q=u\) and \(v^q=v\). A direct expansion gives
\[
F_{q,k}|_{Z=uX+vY}=B(s,t)Q_{u,v}(s,t),
\]
where
\[
Q_{u,v}=(1-kv-u^2v)s^2-2uv^2st-(u+v^3)t^2.
\]
Its quadratic discriminant equals
\[
4\bigl(u+v^3-kuv-kv^4-u^3v\bigr)=4\Delta_k(u,v,1).
\]
For lines with \(V\neq0\), put \(V=1\) and use \(Y=-uX+wZ\), with \([X:Z]=[s:t]\). The corresponding quotient is
\[
Q'_{u,w}=(w-u^3-k)s^2+2u^2wst-(uw^2+1)t^2,
\]
whose discriminant is \(4\Delta_k(u,1,w)\). The sole line missed by these two charts is \(X=0\), on which the quotient is \(Y^2\) and \(\Delta_k(1,0,0)=0\). In both charts the quadratic is nonzero: in the first chart its middle coefficient can vanish only if \(u=0\) or \(v=0\), in which cases the remaining coefficients cannot both vanish; in the second chart the last coefficient is nonzero at \(w=0\), and when \(w\neq0\) the first chart applies. (Alternatively, this is Proposition 3.3 of the source.) Hence no rational line is an entire component.

The polynomial \(B(s,t)\) has exactly \(q+1\) distinct simple zeros in \(\mathbb P^1(\mathbb F_q)\). Thus every rational line contains all its \(q+1\) rational points on \(C_{q,k}\), and its residual intersection divisor is the zero divisor of the nonzero binary quadratic \(Q\). Since all those rational points are smooth by the source's Theorem 1.2, a rational point on the line is a tangent contact precisely when it is a root of \(Q\), with contact order one plus its root multiplicity in \(Q\). In odd characteristic, a nonzero binary quadratic has zero, one (a double root), or two distinct projective rational roots. Exactly one occurs precisely when its discriminant vanishes. The two dual-coordinate charts above, together with the exceptional line, show this is equivalent to \(\Delta_k=0\). Consequently \(N_1=\#D_k(\mathbb F_q)\), and precisely these one-contact lines are rational flex tangents.

**2. Smoothness of the discriminant quartic.** This part is geometric and does not depend on \(q\). On \(W=0\) one has \((\Delta_k)_W=V^3\), and when \(V=0\) the partial derivative \((\Delta_k)_V=-U^3\) is nonzero. So there are no singularities at infinity. Set \(W=1\) and write
\[
f(u,v)=u+v^3-kuv-kv^4-u^3v.
\]
In characteristic three, \(f_u=1-kv\) forces \(kv=1\) at a possible singularity. Substitution into \(f=0\) forces \(u=0\), whereas then \(f_v=-kv^3\neq0\); hence \(D_k\) is smooth. Also \(G'_k(T)=T^6\) in characteristic three, and \(G_k(0)=-1\), so \(G_k\) is squarefree.

Now suppose the odd characteristic is not three. The equations \(f=f_u=f_v=0\) imply \(v\neq0\). From \(f_u=0\), substitute \(k=(1-3u^2v)/v\) into \(f\), obtaining \(u^2v(2u+3v^3)=0\). If \(u=0\), the remaining derivative is \(f_v=-v^2\neq0\). Therefore
\[
u=-\frac32v^3,\qquad 81v^7+2=0,\qquad 6kv=7.
\]
Conversely these three equations imply \(f=f_u=f_v=0\). Put \(x=-1/(3v^2)\). The last two equations give \(x^7=-3/4\) and \(k=-7x^4/3\). Thus \(G_k(x)=G'_k(x)=0\). Conversely, any multiple root \(x\) of \(G_k\) is nonzero and satisfies those two identities. Taking \(v=2x^3/3\) and \(u=-3v^3/2\) gives a singular point of \(D_k\). The manipulations remain valid in characteristic seven (where the equations force \(k=0\)). Hence \(D_k\) is smooth exactly when \(G_k\) is squarefree, in every odd characteristic. A smooth plane quartic is geometrically integral by Bézout and has genus \((4-1)(4-2)/2=3\).

For \(k\in\mathbb F_q\), if \(G_k\) has a multiple root in characteristic distinct from three and seven, the equations for that root give \(x=-12k^2/49\in\mathbb F_q\); the case \(k=0\) is not multiple in these characteristics. In characteristic seven, a multiple root forces \(k=0\) and \(G_0(1)=0\). In characteristic three, no multiple root exists. Hence a root-free \(G_k\) is always squarefree, so the required quartic is smooth.

**3. Exact counts and Weil estimate.** Let \(M=q^2+q+1\). There are \(M\) rational points in the projective plane, all smooth on \(C_{q,k}\); each has exactly one rational tangent line. Counting point-tangent-line incidences gives \(N_1+2N_2=M\). Counting all rational lines gives \(N_0+N_1+N_2=M\). Subtracting shows \(N_0=N_2\), and the claimed exact formulas follow from the identification of \(N_1\). Hasse–Weil for the smooth genus-three curve \(D_k\) gives \(|N_1-(q+1)|\le6\sqrt q\), which yields \(|N_2-q^2/2|\le3\sqrt q\). Each rational flex has a unique tangent line, so the flex-point count is also \(N_1\).

## Verification
The self-contained script `verify_tangent.py` checks the two homogeneous discriminant identities symbolically, the polynomial relation linking singular quartics to repeated roots, and all admissible defining-field parameters in prime fields of characteristics \(3,5,7,11,13,17,19,23,29,31,37,41,43\). It also checks the full rational dual-point and tangent-multiplicity counts for the quadratic fields of orders \(9,25,49\), represented explicitly as polynomial residue fields. These are finite checks only; the universal assertions follow from the displayed proof. The script reports `PLANE_FILLING_TANGENT_DISCRIMINANT_VERIFIER_PASS` when all checks succeed.

## Relationship to prior work
Asgarli and Ghioca, *Plane-filling curves of small degree over finite fields* (arXiv:2307.03072v1, first posted 2023-07-06), introduce exactly \(C_{q,k}\), prove the rational-point smoothness test involving \(G_k\) (Theorem 1.2), prove existence of a root-free coefficient (Proposition 1.3), and prove absence of rational-line components (Proposition 3.3). Their results concern smoothness and existence; they do not give the genus-three dual-plane discriminant, the complete rational flex/two-contact line statistics, or the \(O(\sqrt q)\) error term. The polynomial root criterion and the rational-point count \(q^2+q+1\) are not claimed new. General facts about residual binary quadratics, tangencies, plane quartic genus, and Weil's bound are used rather than claimed new. Previously recorded rational two-contact counts for a different finite-field plane-curve family, \(X^{q-1}+Y^{q-1}+Z^{q-1}-3(X+Y+Z)^{q-1}=0\), have a different defining equation, degree, and incidence mechanism and do not imply this theorem.

## Limitations
The geometric smoothness of \(C_{q,k}\) away from the defining-field points is not established here; Conjecture 1.5 of Asgarli--Ghioca remains outside this result. The theorem is about rational tangent contacts, not the entire geometric dual or all geometric bitangents. The exact numerical count \(N_1\) depends on the zeta data of the particular smooth genus-three quartic \(D_k\); the result provides a closed geometric reduction and a universal sharp-order Weil error, not a residue-class table for all \(q,k\). The originality assessment is based on the inspected accessible sources and research-record searches, not a proof of priority; a general foliation discriminant treatment may contain an equivalent formulation.

## References
1. S. Asgarli and D. Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072v1, posted 2023-07-06; full text: https://arxiv.org/abs/2307.03072 and https://webpages.scu.edu/ftp/sasgarli/plane-filling-curves.pdf.
2. M. Homma, *Fragments of plane filling curves of degree \(q+2\) over the finite field of q elements, and of affine-plane filling curves of degree \(q+1\)*, Linear Algebra and its Applications 589 (2020), 9–27; https://doi.org/10.1016/j.laa.2019.12.012 (different-degree background).
3. Hasse–Weil bound for smooth projective curves over finite fields (standard theorem).
