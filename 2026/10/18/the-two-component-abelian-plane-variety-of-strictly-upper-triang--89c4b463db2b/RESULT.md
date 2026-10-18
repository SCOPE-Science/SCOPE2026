# The two-component abelian-plane variety of strictly upper-triangular four-by-four matrices and its characteristic-three split

## Finding
Let \(k\) be any field, let \(L=\mathfrak u_4(k)\) be the six-dimensional Lie algebra of strictly upper-triangular \(4\times4\) matrices, and let \(X\) be the **reduced** closed subvariety of \(\operatorname{Gr}(2,L)\) parametrizing two-dimensional abelian Lie subalgebras. Then \(X\) has exactly **two geometrically irreducible components**, both of dimension five. Their intersection is geometrically irreducible of dimension four. The two components have different natural geometries: one comes from the five-dimensional Heisenberg subalgebra, and the other from planes having at most one-dimensional image in the abelianization of \(L\).

For every finite field \(\mathbb F_q\), including even characteristic, the exact number of such two-planes is
\[
\#X(\mathbb F_q)=2q^5+3q^4+2q^3+2q^2+q+1.
\]
This formula holds over every finite extension. Hence the Hasse–Weil zeta function is
\[
Z(X/\mathbb F_q,T)=\bigl((1-T)(1-qT)(1-q^2T)^2(1-q^3T)^2(1-q^4T)^3(1-q^5T)^2\bigr)^{-1}.
\]

There is also a **small-characteristic structural jump** for elementary subalgebras. In characteristic at least five, every element of \(L\) has zero restricted \(p\)-power, so the reduced rank-two elementary-subalgebra variety \(\mathbb E(2,L)_{\mathrm{red}}\) equals \(X\) and has the two components above. In characteristic three, \(\mathbb E(2,L)_{\mathrm{red}}\) has exactly **four** geometrically irreducible components, one of dimension five and three of dimension four. Over every \(\mathbb F_q\) of characteristic three,
\[
\#\mathbb E(2,L)(\mathbb F_q)=q^5+4q^4+3q^3+q^2+q+1.
\]
These statements describe reduced geometric support; no assertion about the nilpotent structure of an unreduced defining scheme is made.

## Assumptions and scope
Write
\[
 a=E_{12},\quad b=E_{23},\quad c=E_{34},\quad d=E_{13},\quad e=E_{24},\quad f=E_{14}.
\]
The only nonzero independent brackets of basis vectors are
\[
[a,b]=d,\quad[b,c]=e,\quad[a,e]=f,\quad[d,c]=f.
\]
Set \(D=[L,L]=\langle d,e,f\rangle\) (an abelian ideal), \(V=L/D=\langle\bar a,\bar b,\bar c\rangle\), and \(H=\langle a,c,d,e,f\rangle\), a five-dimensional Heisenberg Lie subalgebra with center \(kf\). Let \(\pi:L\to V\) denote projection. Every two-dimensional abelian vector subspace is automatically a Lie subalgebra. Geometric-component claims mean components after extending \(k\) to an algebraic closure, and all incidence varieties are considered with reduced structure. The restricted Lie \(p\)-operation for positive characteristic is the ordinary matrix \(p\)-th power.

Define two closed loci
\[
X_H=\{W\in X:W\subset H\},\qquad
Y=\{W\in X:\dim\pi(W)\leq 1\}.
\]
The statements include \(k\) of characteristic two for the abelian-plane classification, and positive characteristic three or at least five for the elementary-subalgebra statements. The case of characteristic two is not assigned an elementary-subalgebra component classification.

## Proof
**1. A complete two-stratum alternative.** For two spanning vectors \(x,y\) of \(W\), denote their \(2\times2\) coordinate minors by \(p_{ij}=x_i y_j-x_j y_i\). Direct matrix multiplication gives
\[
[x,y]=p_{ab}d+p_{bc}e+(p_{ae}-p_{cd})f.
\]
If \(\operatorname{rank}\pi(W)=2\), then \(p_{ab}=p_{bc}=0\) and at least one of \(p_{ab},p_{ac},p_{bc}\) is nonzero. Consequently \(p_{ac}\ne0\). The vanishing of the two minors with index \(b\) forces both spanning vectors' \(b\)-coordinates to vanish: explicitly, \((x_b,y_b)\) is simultaneously proportional to independent \((x_a,y_a)\) and \((x_c,y_c)\), hence equals zero. Thus \(W\subset H\). If the projection has rank at most one, by definition \(W\in Y\). Therefore \(X=X_H\cup Y\), without exclusions or characteristic assumptions.

**2. The first irreducible component.** The center of \(H\) is \(kf\), and \(H/kf\) is a four-dimensional symplectic space: its nonzero pairings, in the indicated basis, are between \(a,e\) and \(d,c\). Planes \(W\subset H\) not containing \(f\) project isomorphically to isotropic two-planes of \(H/kf\); their lifts are graphs of linear maps from the two-plane to \(kf\). Thus this open set is the total space of a rank-two vector bundle on the three-dimensional irreducible Lagrangian Grassmannian \(\operatorname{LG}(2,4)\). It is geometrically irreducible of dimension five. Every plane containing \(kf\) is a limit of such planes: for \(W=\langle f,w\rangle\), choose \(z\) independent of \(w\) modulo \(kf\) with \([z,w]=0\), and specialize \(\langle w,f+t z\rangle\) at \(t=0\). Hence \(X_H\) is the closure of the described open set, geometrically irreducible of dimension five. Its locus where the \(a,c\)-projection is an isomorphism is a five-dimensional affine space: the two lifted generators have six \(d,e,f\)-coordinates, subject to one nonzero linear commutator equation.

**3. The second irreducible component.** A rank-one projection plane \(W\) uniquely determines a line \(ku\subset V\) and a line \(kv=W\cap D\subset D\). Choosing any lift of \(u\) to \(L\), the abelian condition is \([u,v]=0\), or
\[
u_a v_e-u_c v_d=0.
\]
The incidence base
\[
I=\bigl\{([u_a:u_b:u_c],[v_d:v_e:v_f])\in\mathbb P^2\times\mathbb P^2:\;u_a v_e-u_c v_d=0\bigr\}
\]
is geometrically irreducible of dimension three. Indeed, outside the single line \(u=kb\) the allowed \(v\)'s form a projective line bundle over the irreducible surface \(\mathbb P^2\setminus\{[0:1:0]\}\); the fiber over \(kb\) is in the closure (approach \(kb\) through a direction \((u_a,u_c)\) annihilating the prescribed \((v_d,v_e)\)). At each point of \(I\), the possible plane \(W\) corresponds to a lift of \(ku\) into the three-space \(L/kv\), up to \(kv\), and these choices form an affine two-space. Hence the rank-one projection stratum is an affine rank-two bundle over \(I\), and is irreducible of dimension five. Its closure contains every rank-zero plane \(W\subset D\): with a basis \(v,w\) of \(W\), choose any nonzero \(u\in\langle a,c\rangle\) satisfying \([u,v]=0\), and use the family \(\langle v,w+t u\rangle\). The locus \(Y\) is therefore geometrically irreducible of dimension five. The witnesses \(\langle a,c\rangle\in X_H\setminus Y\) and \(\langle b,d\rangle\in Y\setminus X_H\) show these are different maximal components.

**4. Their intersection.** A rank-one plane lies in \(H\) precisely when \(u_b=0\). The corresponding dense intersection stratum has incidence base a \(\mathbb P^1\)-bundle over \(\mathbb P^1\): for each nonzero \((u_a,u_c)\), the condition \(u_a v_e-u_c v_d=0\) cuts out one projective line of \(v\)'s. The affine rank-two lifts make the stratum irreducible of dimension four. Every rank-zero plane in \(D\) lies in its closure, by the preceding degeneration with \(u\in\langle a,c\rangle\); thus the entire intersection \(X_H\cap Y\) is geometrically irreducible, of dimension four.

**5. Exact enumeration.** Over \(\mathbb F_q\), the rank-zero projection locus is \(\operatorname{Gr}(2,D)\cong\mathbb P^2\), of cardinality \(q^2+q+1\). For rank one, \(u=kb\) gives \(q^2+q+1\) possible projective \(v\)'s, whereas each of the other \(q^2+q\) projective \(u\)'s admits \(q+1\) such \(v\)'s. Accordingly
\[
\#I(\mathbb F_q)=q^3+3q^2+2q+1,
\]
and each pair has exactly \(q^2\) affine lifts. For projection rank two, all planes lie in \(H\) and their \(a,c\)-projection is an isomorphism. The six lift coefficients satisfy one independent linear condition, yielding precisely \(q^5\) planes. The three disjoint strata therefore contribute
\[
(q^2+q+1)\; +\; q^2(q^3+3q^2+2q+1)\; +\;q^5
=2q^5+3q^4+2q^3+2q^2+q+1.
\]
More finely, the component and intersection counts are
\[
\begin{aligned}
\#X_H(\mathbb F_q)&=q^5+q^4+2q^3+2q^2+q+1,\\
\#Y(\mathbb F_q)&=q^5+3q^4+2q^3+2q^2+q+1,\\
\#(X_H\cap Y)(\mathbb F_q)&=q^4+2q^3+2q^2+q+1.
\end{aligned}
\]
The zeta function follows by inserting this polynomial into the exponential definition of the Hasse–Weil zeta function and using \(\exp(\sum_{m\ge1}(q^iT)^m/m)=(1-q^iT)^{-1}\).

**6. Restricted characteristic changes.** In characteristic \(p\ge5\), every strictly upper-triangular four-by-four matrix satisfies \(x^p=0\), since \(x^4=0\), so \(\mathbb E(2,L)_{\mathrm{red}}=X\). In characteristic three,
\[
x^3=x_a x_b x_c f.
\]
For an abelian plane of projection rank two, \(b\)-coordinates vanish, so all its elements have cube zero. For projection rank at most one, all elements have cube zero precisely when the projective projection line \(ku\) satisfies \(u_a u_b u_c=0\); this follows either directly or from the cube-additivity of commuting matrices in characteristic three.

Among rank-one planes, the allowed projection lines are the union of the three coordinate lines \(u_a=0\), \(u_b=0\), \(u_c=0\) in \(\mathbb P^2\). Those with \(u_b=0\) are already in \(X_H\). The closures of the other three families give exactly three additional irreducible components: one has \(u=kb\) and arbitrary \(kv\in\mathbb P(D)\); the other two have generic \(u\) on \(u_a=0\) or \(u_c=0\), and respectively require \(v_d=0\) or \(v_e=0\). Each has an irreducible two-dimensional incidence base and an affine rank-two lift, hence dimension four. Each contains every rank-zero plane in its closure (choose \(v\in W\cap\langle e,f\rangle\) or \(v\in W\cap\langle d,f\rangle\), or choose \(u=b\) for the first family). These three have distinct generic projection lines and are not contained in \(X_H\). This proves there are precisely four reduced components, one of dimension five and three of dimension four.

For a finite field \(\mathbb F_q\) of characteristic three, the number of admissible rank-one incidence-base points equals
\[
(q+1)^2+2(q-1)(q+1)+(q^2+q+1)=4q^2+3q.
\]
The terms correspond respectively to \(u_b=0\), the two other coordinate lines away from their mutual intersection \(u=b\), and the common intersection line \(u=b\). Multiplying by \(q^2\) affine lifts and adding the unchanged rank-zero and rank-two contributions gives
\[
\#\mathbb E(2,L)(\mathbb F_q)=q^5+4q^4+3q^3+q^2+q+1.
\]

## Verification
The standalone `verify.py` exhaustively enumerates two-dimensional subspaces of \(\mathbb F_q^6\) in unique reduced row-echelon form for \(q=2,3,5\). It reconstructs the three commutator coordinates and independently tests projection ranks and membership in each geometric component. The observed number of all two-planes examined is respectively \(651\), \(11011\), and \(508431\). The commuting rank-zero/rank-one/rank-two counts are respectively \((7,100,32)\), \((13,549,243)\), and \((31,5275,3125)\), giving totals \(139\), \(805\), and \(8431\). In characteristic three it additionally tests the cube of each spanning generator, finding elementary-subalgebra rank counts \((13,405,243)\), total \(661\), as predicted. The program prints `VERIFY_OK` if and only if all asserted tests pass. These finite tests support the symbolic proof but do not prove statements for arbitrary fields or extensions.

## Relationship to prior work
Carlson, Friedlander and Pevtsova initiated the study of elementary-subalgebra varieties and explicitly identified \(\mathbb E(2,\mathfrak u_3)\cong\mathbb P^1\) (Example 1.7 of their 2012 preprint). Their general theory supplies the natural setting, but the inspected sections do not give this four-by-four two-component abelian-plane decomposition, its finite-field polynomial, or the characteristic-three four-component refinement. In particular, the adjacent case \(\mathfrak u_3\) has an irreducible plane variety, while \(\mathfrak u_2\) has none; four-by-four is the first reducible case within the strictly upper-triangular sequence.

Chang's 2016 dissertation discusses elementary-subalgebra varieties for restricted Lie algebras and their connectedness. The inspected material does not determine these components for \(\mathfrak u_4\). Ceballos, Núñez and Tenorio study maximal dimensions and algorithms for abelian subalgebras of upper-triangular matrix algebras; an extremal-dimension or algorithmic statement alone does not determine the scheme-theoretic component geometry or the characteristic-three transition. The latter papers may contain additional relevant enumerative material and this is an explicit residual literature risk. The new calculation is not a claim of novelty of Lagrangian Grassmannians, incidence fibrations, or the basic definitions of elementary subalgebras.

## Limitations
Only the **reduced** abelian-plane and elementary-subalgebra varieties are classified; the proof makes no claim about embedded components, nilpotents of the scheme defined by the Grassmannian bracket equations, tangent cones, or singular loci. The characteristic-three elementary refinement assumes an actual restricted Lie algebra from matrices; characteristic two is excluded from its component classification. No all-ranks or higher triangular-size classification is claimed. An unlocated equivalent component classification in the specialized literature remains a possibility; mathematical-record searches cannot establish worldwide priority.

## References
1. J. F. Carlson, E. M. Friedlander, J. Pevtsova, *Elementary subalgebras of Lie algebras*, arXiv:1207.5898, first submitted 25 July 2012, especially Example 1.7 and the definition of \(\mathbb E(r,\mathfrak g)\). https://arxiv.org/abs/1207.5898 ; full preprint https://sites.math.washington.edu/~julia/Preprints/Elementary_Lie_subalgebras/elemLie.pdf .
2. H. Chang, *Varieties of Elementary Lie Algebras*, doctoral thesis, 2016, especially connectedness and general restricted-Lie-variety background. https://d-nb.info/1105472140/34 .
3. M. Ceballos, L. Núñez, Á. F. Tenorio, *Computing abelian subalgebras for linear algebras of upper-triangular matrices from an algorithmic perspective*, 2016, DOI:10.1515/auom-2016-0032. https://doi.org/10.1515/auom-2016-0032 .
4. J. C. Benjumea, L. Núñez, Á. F. Tenorio, *The maximal Abelian dimension of linear algebras of upper triangular matrices*, 2007, DOI:10.1007/s11232-007-0107-z. Abstract consulted; full text not inspected. https://doi.org/10.1007/s11232-007-0107-z .
