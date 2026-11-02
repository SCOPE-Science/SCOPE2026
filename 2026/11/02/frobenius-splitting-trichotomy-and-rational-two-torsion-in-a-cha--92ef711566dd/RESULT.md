# Frobenius splitting trichotomy and rational two-torsion in a characteristic-three dihedral genus-two family

## Finding
Let \(K=\mathbb F_q\), where \(q=3^n\), \(n\geq1\), and let \(r,c\in K^\times\). Consider the smooth projective model \(C_{r,c}\) of
\[
 c y^2=x^6+r x^4+r x^2+r.
\]
Write \(W(C_{r,c})\) for its six geometric Weierstrass points and \(J_{r,c}\) for its Jacobian. Exactly one of the following three cases occurs:

| Condition | Frobenius cycle type on \(W(C_{r,c})\) | Smallest splitting field | \(\#J_{r,c}[2](K)\) | Number of parameters \(r\in K^\times\) |
| --- | --- | --- | --- | --- |
| \(-1/r\) is a square, and a square root \(\beta\) has \(\operatorname{Tr}_{K/\mathbb F_3}(\beta)=0\) | \(1^6\) | \(K\) | \(16\) | \((q-3)/6\) |
| \(-1/r\) is a nonsquare | \(2^3\) | \(\mathbb F_{q^2}\) | \(4\) | \((q-1)/2\) |
| \(-1/r\) is a square, and its square roots have nonzero absolute trace | \(3^2\) | \(\mathbb F_{q^3}\) | \(1\) | \(q/3\) |

The counts are for **literal nonzero parameters** \(r\), not for isomorphism classes, and hold for **every** nonzero quadratic-twist coefficient \(c\). In particular, no six-cycle and no rational-two-torsion order other than \(1,4,16\) occurs in this family. The order-three automorphism acts wildly, while every curve remains ordinary.

## Assumptions and scope
All fields have characteristic three. The equation is the characteristic-three specialization of the Booher–Howe–Sutherland–Voloch genus-two family; unlike their generic-characteristic moduli classification, this statement permits every \(r,c\ne0\), including parameters with extra geometric automorphisms. “Splitting field” means the minimal finite extension of \(K\) over which all six geometric Weierstrass points individually become rational. The quadratic twist \(c\) affects rational point counts on the curve but not the Weierstrass-point field or rational two-torsion specified here.

## Proof
**1. Smoothness and the wild presentation.** In characteristic three,
\[
 c y^2=x^6+(r-18)x^4+(81-2r)x^2+r
       =x^6+r(x^2-1)^2.
\]
The derivative of the polynomial on the right is \(r(x^3-x)\). Its only geometric zeros are \(x=0,1,-1\), where the polynomial takes values \(r,1,1\), respectively; thus the degree-six polynomial is separable for \(r\ne0\). Its smooth projective double cover is genus two and has six finite branch points. On setting \(t=1/x\), \(v=y/x^3\), the same curve has the birational model
\[
 c v^2=1+r(t^3-t)^2. \tag{1}
\]
The transformations \((t,v)\mapsto(t+1,v)\), \((t,v)\mapsto(-t,-v)\), and the hyperelliptic involution \((t,v)\mapsto(t,-v)\) generate a rational dihedral subgroup of order twelve. The quotient by translation \(t\mapsto t+1\) is the smooth genus-zero conic \(c v^2=1+r u^2\), where \(u=t^3-t\). This Artin–Schreier covering is wildly ramified above the two geometric simple poles of \(u\). Equivalently, the Cartier–Manin coefficient matrix of the original sextic has diagonal \(r,r\) (the \(x^2\) and \(x^4\) coefficients) and zero off-diagonal entries, hence invertible for \(r\ne0\). Thus \(C_{r,c}\) is ordinary. The dihedral action, conic quotient, and ordinarity are included as context, not asserted to be independently new.

**2. Exact branch equations.** The hyperelliptic branch condition in (1) is
\[
 (t^3-t)^2=-1/r.
\]
Choose \(\beta\) in an algebraic closure with \(\beta^2=-1/r\). The six branch coordinates are the three distinct solutions of each of
\[
 t^3-t=\beta,\qquad t^3-t=-\beta. \tag{2}
\]
The two root triples are disjoint because \(\beta\ne0\); each is an orbit under translation by \(\mathbb F_3\). This also verifies that (2) exhausts all six Weierstrass points.

**3. Frobenius trichotomy.** Suppose first \(\beta\in K\). For \(a\in K\), the additive equation \(T^3-T=a\) has three solutions in \(K\) if and only if \(\operatorname{Tr}_{K/\mathbb F_3}(a)=0\). Indeed its image is the kernel of the trace: the map has kernel \(\mathbb F_3\) and both image and trace kernel have \(q/3\) elements. If the trace is zero, both triples in (2) split in \(K\), giving cycle type \(1^6\). Otherwise the two monic cubics in (2) are irreducible over \(K\), giving cycle type \(3^2\), with minimal common splitting field \(\mathbb F_{q^3}\). The criterion is independent of the sign of \(\beta\).

Now suppose \(\beta\notin K\). Its minimal polynomial is \(Z^2+1/r\), so \(\beta^q=-\beta\). Consequently \(\operatorname{Tr}_{\mathbb F_{q^2}/\mathbb F_3}(\beta)=\operatorname{Tr}_{K/\mathbb F_3}(\beta+\beta^q)=0\), and both triples split over \(\mathbb F_{q^2}\). There is no branch point over \(K\), since \((t^3-t)^2=-1/r\) would make \(-1/r\) a square. Frobenius is therefore a fixed-point-free involution on the six points: its cycle type is \(2^3\), and the splitting extension is precisely quadratic. There are no other possibilities.

**4. Rational two-torsion.** For a genus-two hyperelliptic curve over a field of odd characteristic, the fifteen nonzero geometric Jacobian two-torsion classes are canonically represented by unordered pairs of distinct Weierstrass points. Frobenius fixes such a class precisely when it fixes its pair as a set. A permutation of type \(1^6\) fixes all fifteen pairs; one of type \(2^3\) fixes exactly its three two-cycles; one of type \(3^2\) fixes no pair. Adjoining the identity yields respective rational two-torsion orders \(16,4,1\). These are elementary abelian \(2\)-groups of ranks \(4,2,0\).

**5. Counting actual parameters.** The map \(\beta\mapsto r=-1/\beta^2\) identifies the nonzero trace-zero elements of \(K\) in pairs \(\{\beta,-\beta\}\). The trace-zero subspace has \(q/3\) elements, so the number of parameters in the \(1^6\) case is \((q/3-1)/2=(q-3)/6\). Exactly \((q-1)/2\) choices of \(r\) make \(-1/r\) nonsquare and give \(2^3\). Subtracting from \(q-1\) gives \(q/3\) parameters with type \(3^2\). The three counts add to \(q-1\), including the boundary case \(q=3\), for which the first class is empty.

## Verification
The independent exact finite-field checker `verify_wild_d6.py` uses only Python's standard library. It constructs \(\mathbb F_{3^n}\) for \(n=1,2,3,4\), verifies field arithmetic, enumerates all \(q-1\) nonzero parameters, checks all rational sextic branch roots directly, and computes the degrees \(\deg\gcd(f(T),T^{q^d}-T)\) for \(d=1,2,3,6\), independently certifying the three cycle types and exact parameter counts. It passed all \(2+8+26+80=116\) parameter tests. In the defining equation of the checker \(f(T)=1+r(T^3-T)^2\), so its input does not require choosing a square root. The uniform proof is the field-theoretic argument above; 116 finite tests are not an infinite proof.

## Relationship to prior work
Booher, Howe, Sutherland, and Voloch (2024, arXiv:2402.08853, Section 5.3) **already give** the characteristic-three presentation \(y^2=(t^3-t)^2+a\), identify the ordinary genus-two curves, and state the criterion \(a=-(d^3-d)^2\) for the sextic to split completely over the ground field. Those known facts are not claimed as discoveries here. The present exact classification adds the **previously unstated intermediate arithmetic alternatives**: non-split Frobenius types \(2^3\) and \(3^2\), minimal splitting degrees \(2\) and \(3\), rational Jacobian two-torsion ranks \(2\) and \(0\), and the three exact parameter frequencies. The earlier Cardona–Quer dihedral classification excludes characteristic three and does not determine these quantities.

## Limitations
The arithmetic trichotomy follows from elementary Artin–Schreier theory once the motivating paper's characteristic-three model is known; it is a specific exact classification, not a new general ramification theorem. It counts literal \(r\)-parameters, not geometrically distinct isomorphism classes, rational curves, or distinct quadratic twists. It does not determine Weil polynomials, Jacobian isogeny classes, full automorphism groups at exceptional parameters, or non-two-primary torsion. Historical priority risk remains for equivalent complete Frobenius decompositions in literature not indexed by the searches used here.

## References
- J. Booher, E. W. Howe, A. V. Sutherland, J. F. Voloch, *Doubly isogenous curves of genus two with a rational action of \(D_6\)*, arXiv:2402.08853 (first public posting 2024-02-13), especially Sections 2, 3, and 5.3.
- G. Cardona and J. Quer, *Curves of genus 2 with group of automorphisms isomorphic to \(D_8\) or \(D_{12}\)*, arXiv:math/0203165 (2002), characteristic restriction in the abstract.
- Standard additive-polynomial trace exact sequence over finite fields and the description of hyperelliptic genus-two Jacobian two-torsion by unordered pairs of branch points.
