# Six affine conjugacy types of Rota–Baxter maps on the canonical Heisenberg Lie affgebra

## Finding
Let \(K\) be any field and let \(H=Kx\oplus Ky\oplus Kz\) be the three-dimensional Heisenberg Lie algebra, with \([x,y]=z\) and \(z\) central. Give the underlying affine space the canonical Lie-affgebra bracket \(\{u,v\}=[u,v]+v\). An affine map \(P:H\to H\) is called a weight-minus-one affine Rota–Baxter map when
\[
 P\bigl(\{P(u),v\}-\{u,v\}+\{u,P(v)\}\bigr)=\{P(u),P(v)\}
\]
for every \(u,v\in H\). (The signed affine combination of the three brackets has coefficient sum one.)

**Classification theorem.** Under conjugation by *all affine automorphisms* of this Lie affgebra, there are exactly six such maps, represented by \(P(u)=R(u)+p\) in the following table. Each matrix is given by its values on \(x,y,z\):

| Type | \(R(x)\) | \(R(y)\) | \(R(z)\) | \(p\) |
|:--|:--|:--|:--|:--|
| A | \(0\) | \(0\) | \(0\) | \(0\) |
| B | \(0\) | \(0\) | \(0\) | \(x\) |
| C | \(x\) | \(0\) | \(0\) | \(0\) |
| D | \(x\) | \(0\) | \(z\) | \(0\) |
| E | \(x\) | \(0\) | \(z\) | \(y\) |
| F | \(x\) | \(y\) | \(z\) | \(0\) |

If \(K=\mathbb F_q\), these six affine-conjugacy classes have, in the same order, exact sizes
\[
 q,\quad q^3-q,\quad q^3(q+1),\quad q^2(q+1),\quad(q-1)q^2(q+1),\quad1.
\]
In particular the number of all affine Rota–Baxter maps is exactly
\[
 \boxed{2q^4+3q^3+1}.
\]
Their linear-part rank distribution (ranks \(0,1,2,3\)) is \((q^3,q^3(q+1),q^3(q+1),1)\). In every characteristic, every such affine Rota–Baxter map is idempotent.

## Assumptions and scope
All fields are allowed, including characteristic two. The Heisenberg bracket is bilinear, alternating, and satisfies \([x,y]=z\), \([x,z]=[y,z]=0\). Affine equivalence means conjugacy by affine maps preserving \(\{u,v\}=[u,v]+v\); it is *not* merely Lie-algebra automorphism equivalence. In the finite-field formulas \(q\) is any prime power. The classification concerns affine Rota–Baxter maps of weight \(-1\) on this canonical Lie affgebra, not all linear Rota–Baxter maps on \(H\) for arbitrary weights.

## Proof
**1. Reduction to projections, without a characteristic-zero hypothesis.** Write \(P(u)=R(u)+p\). Expanding the displayed identity into constant, terms linear in each variable, and bilinear terms gives
\[
 R(p)=0,\qquad R^2=R,\qquad
 R([p,u])=[p,R(u)],\qquad
 [R(u),R(v)]=R([R(u),v]+[u,R(v)]-[u,v]).
\]
Indeed the constant coefficient is \(R(p)\). The coefficient depending only on \(u\) gives commutation of \(R\) with \(\operatorname{ad}_p\); substitution in the coefficient depending only on \(v\) then gives \(R^2=R\). The bilinear coefficient is the usual weight-minus-one Rota–Baxter identity. Conversely the four displayed equations reconstruct the original affine identity. Every step is polynomial, so no division by two or characteristic restriction is involved.

Put \(H_+=\operatorname{im}R\), \(H_-=\ker R\). Since \(R^2=R\), these are complementary vector subspaces. The last identity is equivalent to both being Lie subalgebras: for \(a,a'\in H_+\) it requires \(R[a,a']=[a,a']\), and for \(b,b'\in H_-\) it requires \(R[b,b']=0\); the mixed terms cancel. Moreover \(p\in H_-\), and \(R\operatorname{ad}_p=\operatorname{ad}_pR\) is equivalent to \([p,H_+]\subseteq H_+\), because \([p,H_-]\subseteq H_-\) already follows from the subalgebra property. Consequently all operators are uniquely parameterized by ordered Lie-subalgebra decompositions \(H=H_+\oplus H_-\) and translation vectors \(p\in H_-\) normalizing \(H_+\). This reproduces the characteristic-free algebraic part of the general parameterization, and independently establishes its validity over finite fields.

**2. Enumerate the decompositions.** The center is \(Z=Kz\). Every line is a Lie subalgebra. A plane is a Lie subalgebra exactly when it contains \(Z\): if it does not, its projection to \(H/Z\) is an isomorphism, and the bracket of two independent lifts is a nonzero multiple of \(z\), contradicting closure. Thus only four ranks occur. For rank zero, \(R=0\) and any \(p\in H\) works; for rank three, \(R=\mathrm{id}\) and \(p=0\).

For rank one, \(H_-\) is a plane containing \(Z\), and \(H_+\) is any complementary line. Because \(Z\subseteq H_-\), any \(p\in H_-\) satisfying \([p,H_+]\subseteq H_+\) must centralize \(H_+\), and the intersection \(H_-\cap C_H(H_+)\) is exactly \(Z\). Hence \(p\in Z\). For rank two, \(H_+\) is a plane containing \(Z\), \(H_-\) is a complementary line, and *every* \(p\in H_-\) works because \([H,H_+]\subseteq Z\subseteq H_+\).

Over \(\mathbb F_q\), the planes containing \(Z\) number \(q+1\). Each has exactly \(q^2\) complementary lines, since \((q^2+q+1)-(q+1)=q^2\). There are \(q\) translation choices for every such ordered decomposition in either orientation. Thus ranks one and two each contribute \(q^3(q+1)\) maps, alongside \(q^3\) constants and the identity.

**3. Full affine automorphism group and orbit classification.** An affine map \(\Phi(u)=G(u)+t\) preserves the canonical bracket exactly when \(G\in\operatorname{Aut}_{\mathrm{Lie}}(H)\) and \(t\in Z\). Indeed setting one input to zero forces \([t,G(u)]=0\) for all \(u\), and the bilinear part forces preservation of the Lie bracket. Explicitly, every linear Lie automorphism has
\[
 G(x)=a x+c y+u z,\qquad G(y)=b x+d y+v z,\qquad G(z)=(ad-bc)z,
 \qquad ad-bc\ne0.
\]
Conjugating \(P=R+p\) by \(\Phi=G+t\) sends \(R\) to \(R'=GRG^{-1}\) and \(p\) to \(p'=G(p)+(I-R')t\).

For constant maps, the central translations identify all constants \(p\in Z\), while the linear automorphism group is transitive on \(H\setminus Z\). This gives types A and B. For rank one, \(\operatorname{GL}_2(K)\) acts transitively on ordered distinct lines in \(H/Z\), and the central shear parameters align their lifts; all decompositions are equivalent to \(H_+=Kx\), \(H_-=Ky\oplus Kz\). The allowed \(p\in Z\) is eliminated by the central translation \(t=-p\), because \(R(t)=0\). This gives type C. For rank two, all ordered decompositions are equivalent to \(H_+=Kx\oplus Kz\), \(H_-=Ky\). Central affine translations have no effect on \(p\) because \(R(z)=z\). The stabilizer scales the generator of \(H_-\) by any nonzero scalar, so \(p=0\) and \(p\ne0\) give precisely D and E. The identity is F. Differences in rank, central/noncentral constant, or zero/nonzero permitted translation distinguish the six orbits.

Their finite-field cardinalities follow by dividing the rank-one group of \(q^3(q+1)\) maps into one orbit, by splitting rank two into \(q^2(q+1)\) operators with \(p=0\) and \((q-1)q^2(q+1)\) operators with \(p\ne0\), and by partitioning the constant maps into \(q\) central and \(q^3-q\) noncentral constants. Each claimed part is a single orbit by the preceding explicit transitivity arguments.

## Verification
Run \(\texttt{python3 artifacts/verify.py}\), using only Python's standard library. For both \(q=2\) and \(q=3\) the checker exhausts all \(q^9\) possible linear parts and all compatible translations by the independently derived coefficient conditions, then evaluates the original defining affine Rota–Baxter identity at *every ordered pair* of elements for every accepted map. It separately enumerates the full affine automorphism group and directly constructs the six pairwise disjoint conjugacy orbits from the displayed representatives. It obtains respectively \(57\) and \(244\) maps with orbit sizes \((2,6,24,12,12,1)\) and \((3,24,108,36,72,1)\). The classification for arbitrary fields is proved algebraically above; finite exhaustive tests do not establish infinite-field claims on their own.

## Relationship to prior work
Han–Khudoyberdiyev–Xie–Zhang (arXiv:2610.14838v1, publicly posted 10 October 2026) define the affine Rota–Baxter identity, prove the *general structural parameterization* of canonical Lie-affgebra operators in characteristic zero (Theorem 4.4), and give normal-form classifications only in dimensions at most two. The present result does not claim that this general structural parameterization is new. It provides a complete six-orbit normal-form classification in the first nonabelian nilpotent dimension three, plus exact finite-field counts and a characteristic-free verification of the reduction. Ji–Hua (2018) and Rathee (arXiv:2402.15428v1) classify **linear** Rota–Baxter maps on the Heisenberg Lie algebra, at different weight conventions; those results can cover linear projections, but not the affine translation strata or conjugacy by the full affine Lie-affgebra automorphism group. The finite-field and affine equivalence questions are not answered by those listed linear matrices alone.

## Limitations
The six conjugacy types concern only the canonical Lie affgebra of the three-dimensional Heisenberg Lie algebra. They do not classify general Lie affgebras, arbitrary three-dimensional Lie algebras, or maps of other weights. The definition is an affine-space identity, distinct from the classical *linear* Rota–Baxter identity. The proof is self-contained once these algebraic definitions are adopted; independent peer validation and a completely exhaustive search of unpublished literature have not occurred.

## References
1. JiaJia Han, Abror Khudoyberdiyev, Yunzhou Xie, Yi Zhang, *Rota-Baxter operators and factorization of Lie affgebras*, arXiv:2610.14838v1 (10 October 2026), especially Theorems 4.4 and 4.7.
2. Guangzhi Ji and Xiuying Hua, *Rota-Baxter operators of 3-dimensional Heisenberg Lie algebra*, Korean Journal of Mathematics 26 (2018), 53–60, DOI:10.11568/kjm.2018.26.1.53, Theorems 3.1–3.2.
3. Nishant Rathee, *Rota--Baxter operators and skew left brace structures over Heisenberg Group*, arXiv:2402.15428v1 (23 February 2024), Section 4.
