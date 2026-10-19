# Exact idempotent-free census and automorphism dichotomy for two-dimensional perfect evolution algebras

## Finding
Fix any prime power \(q\) and \(K=\mathbb F_q\). A two-dimensional evolution algebra has a natural basis \((e_1,e_2)\) with \(e_1e_2=0\). Write its products as
\[
e_1^2=a e_1+b e_2,\qquad e_2^2=c e_1+d e_2.
\]
Call the algebra **perfect** if \(E^2=E\), and **idempotent-free** if \(z^2=z\) implies \(z=0\). Define \(f(T)=cT^3-dT^2+aT-b\).

**Theorem.** The following statements hold for every finite field, without restrictions on characteristic.

1. The algebra is perfect and idempotent-free if and only if \(f\) is irreducible over \(K\).
2. The number of coefficient quadruples \((a,b,c,d)\in K^4\) with this property is
   \[
   N_q=\frac{q(q-1)^2(q+1)}{3}=\frac{|\operatorname{GL}_2(K)|}{3}.
   \]
   Thus exactly one third of the perfect structure matrices on a specified ordered natural basis are idempotent-free.
3. The number of \(K\)-algebra isomorphism classes among these tables is
   \[
   I_q=\begin{cases}
      \dfrac{q(q+1)+4}{6},&q\equiv1\pmod 3,\\
      \dfrac{q(q+1)}6,&q\not\equiv1\pmod 3.
   \end{cases}
   \]
4. Every such algebra has trivial automorphism group except when \(q\equiv1\pmod3\), in which case precisely one isomorphism class has automorphism group \(C_3\); all other classes have trivial automorphism group.

For instance, \(q=4\) gives \(60\) qualifying marked tables, \(4\) classes, and one order-three symmetry class; \(q=9\) gives \(1920\) tables, \(15\) classes, all rigid. The smallest-dimension existence problem is not claimed here; the contribution is the complete count, the one-third law, and the sharp symmetry distribution.

## Assumptions and scope
An evolution algebra here is a commutative, not necessarily associative, \(K\)-algebra with a basis satisfying \(e_i e_j=0\) for distinct indices. A *marked table* means a structure matrix relative to a specified ordered natural basis, counted with coefficients rather than modulo basis change. Isomorphism classes and automorphisms are over the fixed field \(K\); the field is not allowed to move under an automorphism. There is no assumption that \(q\) is odd.

## Proof
**1. The fixed-point criterion.** The product is encoded by the homogeneous quadratic squaring map
\[
Q(x,y)=(a x^2+c y^2,\ b x^2+d y^2).
\]
The algebra is perfect precisely when \(ad-bc\ne0\), since its two basis squares then span \(E\). For a perfect algebra, \(Q(v)\ne0\) for every nonzero vector \(v\), so \(Q\) induces a well-defined endomorphism of \(\mathbb P^1(K)\). A fixed projective point \([v]\) has \(Q(v)=\lambda v\) for some nonzero \(\lambda\). Since \(Q\) is homogeneous of degree two, \(Q(\lambda^{-1}v)=\lambda^{-1}v\), giving a nonzero idempotent. Conversely, a nonzero idempotent gives a fixed projective point. Therefore a perfect algebra is idempotent-free exactly when the induced projective squaring map has no rational fixed point.

The point at infinity \([0:1]\) is fixed exactly when \(c=0\). A finite projective point \([1:t]\) is fixed exactly when
\[
b+d t^2=t(a+c t^2),\quad\text{equivalently}\quad
f(t)=c t^3-d t^2+a t-b=0.
\]
Consequently, a perfect algebra is idempotent-free if and only if \(c\ne0\) and \(f\) has no root in \(K\). A cubic over a field has no root exactly when it is irreducible. Conversely, irreducibility of \(f\) implies \(c\ne0\) and
\[
f(d/c)=\frac{ad-bc}{c}\ne0,
\]
so \(ad-bc\ne0\) automatically. This proves assertion 1, including characteristic two.

**2. Exact marked-table count.** The number of monic irreducible cubic polynomials over \(\mathbb F_q\) is \((q^3-q)/3\). Indeed, the elements of \(\mathbb F_{q^3}\) not lying in \(\mathbb F_q\) have Galois orbit length three, and their orbits biject with monic irreducible cubics. Every such polynomial can be multiplied by any of the \(q-1\) nonzero leading coefficients \(c\), and the coefficients uniquely recover \((a,b,c,d)\). Hence
\[
N_q=(q-1)\frac{q^3-q}{3}=\frac{q(q-1)^2(q+1)}{3}.
\]
The number of invertible two-by-two structure matrices is \(|\operatorname{GL}_2(q)|=q(q-1)^2(q+1)\); this gives the one-third law.

**3. Why the monomial group gives all isomorphisms.** In any perfect two-dimensional evolution algebra, \(e_1^2,e_2^2\) are independent. If \(u=r e_1+s e_2\) and \(v=t e_1+w e_2\) are distinct elements of another natural basis, then
\[
0=uv=rt\,e_1^2+sw\,e_2^2
\]
forces \(rt=sw=0\). As the basis change is invertible, it is diagonal or anti-diagonal. Thus all isomorphisms arise from
\[
G=(K^\times)^2\rtimes S_2,
\qquad |G|=2(q-1)^2.
\]
Under \((e_1,e_2)\mapsto(s e_1,t e_2)\), the coefficient quadruple transforms as
\[
(a,b,c,d)\longmapsto
\left(sa,\frac{s^2}{t}b,\frac{t^2}{s}c,td\right).
\]
Under \((e_1,e_2)\mapsto(s e_2,t e_1)\), it transforms as
\[
(a,b,c,d)\longmapsto
\left(sd,\frac{s^2}{t}c,\frac{t^2}{s}b,ta\right).
\]
The irreducible-cubic locus is invariant under this action, since being perfect and idempotent-free is invariant under isomorphism. The stabilizer of a marked table is its algebra automorphism group.

**4. Stabilizers and the exceptional class.** Irreducibility gives \(b,c\ne0\), since otherwise \(f(0)=0\) or \(c=0\) and \(f\) is not cubic. A diagonal basis change fixing a table must satisfy
\[
t=s^2,\qquad s=t^2,\qquad (s-1)a=(t-1)d=0.
\]
Either \(s=t=1\), or \(s^3=1\) with \(s\ne1\); in the latter case \(a=d=0\) and \(t=s^2\). Two distinct nonidentity cube roots exist in \(K\) exactly when \(q\equiv1\pmod3\).

No anti-diagonal basis change can fix a qualifying table. Indeed, fixedness of \(b,c\ne0\) yields \(st=1\), \(b=s^3c\); fixedness of \(a,d\) gives \(a=sd\). Then \(f(s)=cs^3-ds^2+as-b=0\), contradicting irreducibility.

When \(q\equiv1\pmod3\), a qualifying table fixed by either nonidentity diagonal cube-root change has \(a=d=0\) and
\[
f(T)=cT^3-b.
\]
This is irreducible precisely when \(b/c\) is not a cube in \(K^\times\): a cubic over a field is irreducible exactly when it has no root. There are \(2(q-1)/3\) choices for the noncube ratio \(b/c\) and \(q-1\) choices for \(c\), giving \(2(q-1)^2/3\) exceptional tables. Every such table has stabilizer of order exactly three, and thus lies in an orbit of size \(2(q-1)^2/3\). Consequently these exceptional tables make up exactly one isomorphism class. All remaining tables have trivial stabilizer.

Burnside's lemma gives, if \(q\not\equiv1\pmod3\),
\[
I_q=\frac{N_q}{2(q-1)^2}=\frac{q(q+1)}6;
\]
and if \(q\equiv1\pmod3\), two nonidentity diagonal group elements each fix \(2(q-1)^2/3\) tables, while every other group element has none, so
\[
I_q=\frac{N_q+2\cdot(2(q-1)^2/3)}{2(q-1)^2}
=\frac{q(q+1)+4}{6}.
\]
This proves assertions 2–4.

## Verification
The accompanying standalone \(\texttt{verify.py}\) implements arithmetic in ten explicit finite fields without third-party packages. For \(q=2,3,4,5,7,8,9,11,13,16\), it enumerates all four-parameter tables, checks the one-third formula, enumerates every orbit under both monomial change-of-basis types, and determines the stabilizer-size census. In all cases it agrees with the displayed class formula and the unique possible order-three stabilizer. For \(q\le9\), it additionally tests every nonzero vector against the idempotent equation for every perfect table, independently checking the cubic criterion. Running \(\texttt{python3 verify.py}\) prints the ten field cases and \(\texttt{VERIFY_OK}\). These finite computations are supplementary: the proof applies to all finite fields.

## Relationship to prior work
Hu and Wen (2026) motivate idempotent-free nonsolvable evolution algebras, particularly the difference between complex and finite-field phenomena. Their principal three-dimensional complex-family result does not count two-dimensional perfect idempotent-free algebras over finite fields. Cabrera Casado, Martín Barquero and Martín González (2023) give the general two-dimensional perfect-algebra classification and the monomial basis-change mechanism used in this proof. The special off-diagonal cube-root symmetry is visible in that pre-existing classification; it is not claimed separately as a new mechanism. Wei and Zou (2023) enumerate isomorphism classes of perfect (there called "idempotent") evolution algebras; their fully accessible arXiv version (Sections 1–4) proves a Burnside count for **all** perfect evolution algebras, but does not impose the no-nonzero-idempotent condition or enumerate its subclass. In Section 4.1 they count all \( (q-1)^2 \) tables fixed by each primitive-cubic diagonal action, whereas the present restriction retains exactly \(2(q-1)^2/3\) of those tables. The journal version was not separately inspected. A separately reported finite-field construction already proves the existence of two-dimensional idempotent-free perfect examples in every characteristic. The claims here are the sharp finite-field **distribution within all perfect tables**, the **exact idempotent-free subclass isomorphism count**, and the **full stabilizer distribution**, not existence or general monomial classification.

## Limitations
The results concern precisely two-dimensional, perfect evolution algebras over finite fields. They do not classify all two-dimensional evolution algebras, or arbitrary-dimensional idempotent-free algebras. The marked-table one-third fraction counts multiplication tables in a fixed natural basis, not isomorphism classes. The isomorphism-count formula uses algebra isomorphisms linear over \(K\), not semilinear isomorphisms allowing field automorphisms. The accessible complete arXiv text by Wei and Zou was inspected; it covers all perfect classes, not the present idempotent-free subclass census. A distinct final journal version or unindexed equivalent statement could still affect priority. Independent mathematical and bibliographic review remains to be performed.

## References
1. Xing-Yu Hu and Ran Wen, *Idempotent-free non-solvable evolution algebras over C* (2026), arXiv:2609.25023, https://arxiv.org/abs/2609.25023 (also publicly posted as Preprints.org manuscript 202609.0078 on 2026-09-01, the earliest verified public posting).
2. Yolanda Cabrera Casado, Dolores Martín Barquero and Cándido Martín González, *Two-dimensional perfect evolution algebras over domains*, Journal of Algebraic Combinatorics 58 (2023), 569–587, https://doi.org/10.1007/s10801-022-01196-1 (open full text inspected).
3. Yangjiang Wei and Yi Ming Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, Linear Algebra and Its Applications 675 (2023), 142–178, https://doi.org/10.1016/j.laa.2023.06.006 (full open arXiv text arXiv:2310.12368 inspected, including Sections 1–4; journal version not separately inspected).
