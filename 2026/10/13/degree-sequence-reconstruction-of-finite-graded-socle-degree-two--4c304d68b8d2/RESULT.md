# Degree-sequence reconstruction of finite graded socle-degree-two Gorenstein rings

## Finding

Let \(k=\mathbb F_q\) be any finite field, let \(d\ge2\), and let \(B\) be a nondegenerate symmetric bilinear form on \(V=k^d\). Form the standard graded, commutative, associative local algebra
\[
A(B)=k\oplus V\oplus kz,
\qquad \deg(V)=1,\quad\deg(z)=2,
\qquad vw=B(v,w)z,\quad vz=z^2=0.
\]
Every standard graded commutative Artinian Gorenstein \(k\)-algebra with Hilbert vector \((1,d,1)\) arises this way. Its *ordinary simple zero-divisor graph* \(\Gamma(A(B))\) has vertices the nonzero elements of its maximal ideal; distinct vertices are adjacent when their product is zero.

**The full degree multiset of \(\Gamma(A(B))\) determines the isomorphism class of \(A(B)\) as a ring, including its finite field and its multiplication-form similarity class.** Equivalently, for any two algebras in this class, their zero-divisor graphs are isomorphic if and only if their rings are isomorphic, and the same equivalence holds with “degree multisets agree” in place of “graphs are isomorphic.”

More precisely, put \(Z(B)=|\{v\in V:B(v,v)=0\}|\), including the zero vector. The complete degree distribution consists of
\[
\begin{array}{c|c}
\text{degree}&\text{multiplicity}\\\hline
q^{d+1}-2&q-1\\
q^d-2&q\bigl(Z(B)-1\bigr)\\
q^d-1&q\bigl(q^d-Z(B)\bigr)
\end{array}
\]
with zero-multiplicity rows omitted. The isotropic-vector count is
\[
Z(B)=
\begin{cases}
q^{d-1},&q\text{ odd},\ d\text{ odd},\\
q^{d-1}+(q-1)q^{(d-2)/2}\eta\bigl((-1)^{d/2}\det B\bigr),&q\text{ odd},\ d\text{ even},\\
q^d,&q\text{ even},\ B\text{ alternating},\\
q^{d-1},&q\text{ even},\ B\text{ nonalternating}.
\end{cases}
\]
Here \(\eta:k^\times\to\{-1,1\}\) is the quadratic character; the alternating case requires even \(d\). In odd characteristic and even \(d\), the sign in this formula distinguishes both similarity classes. In even characteristic and even \(d\), the last two lines distinguish the alternating and nonalternating classes. There is one similarity class when \(d\) is odd, in either characteristic.

## Assumptions and scope

The coefficient field is finite of prime-power order \(q\); the dimension \(d\) is an integer at least two. The rings are standard graded, commutative, associative, unital and Artinian, with degree-zero part exactly \(k\), maximal ideal \(\mathfrak m=A_1\oplus A_2\), and Hilbert vector \((1,d,1)\). The Gorenstein hypothesis means the socle \((0:\mathfrak m)\) has \(k\)-dimension one. The graph is the *simple* graph on nonzero zero divisors; loops from square-zero elements are excluded. Ring isomorphism need not respect any chosen bases or the chosen coefficient-field embedding.

## Proof

**1. The form is the complete multiplication datum.** Since the algebra is generated in degree one and the degree-two component is one-dimensional, choosing its generator \(z\) gives a symmetric form \(B:V\times V\to k\) with \(vw=B(v,w)z\). Products of total degree three or more vanish. If \(B(v,w)=0\) for all \(w\), then \(v\) annihilates the maximal ideal and is an extra socle vector. Thus the Gorenstein condition is equivalent to the nondegeneracy of \(B\); conversely nondegeneracy makes the socle exactly \(kz\). Associativity is automatic because triple products in the maximal ideal vanish. This yields exactly the claimed class of rings.

**2. Ring isomorphisms classify bilinear similarity.** A ring isomorphism preserves the unique maximal ideal and its powers and hence induces semilinear isomorphisms of \(\mathfrak m/\mathfrak m^2\) and of \(\mathfrak m^2\). Its action on the residue field is some finite-field automorphism \(\sigma\). Multiplication in the associated graded ring forces
\[
B'(Tv,Tw)=\lambda\,\sigma(B(v,w))
\]
for an invertible \(\sigma\)-semilinear \(T\) and \(\lambda\in k^\times\). Conversely such \(T,\lambda,\sigma\) extend to a ring isomorphism by sending \(a+v+cz\) to \(\sigma(a)+Tv+\lambda\sigma(c)z'\). Thus ring isomorphism is similarity of \(B\) up to field automorphism. Finite-field automorphisms preserve quadratic-character classes, and also preserve alternatingness, so they do not merge the similarity types listed below.

**3. Degree counts.** The ring is local and its nonunits are exactly \(\mathfrak m\). Every nonzero socle element \(cz\) is adjacent to every other vertex. Hence exactly \(q-1\) vertices have degree \(q^{d+1}-2\). For \(v\ne0\), nondegeneracy gives \(|v^\perp|=q^{d-1}\), so precisely \(q^d-1\) nonzero vertices have zero product with \(v+cz\) when the possible self-pair is included. The self-pair must be deleted precisely when \(B(v,v)=0\). The resulting degree is \(q^d-2\) for isotropic \(v\), and \(q^d-1\) otherwise. Each fixed nonzero \(v\) admits exactly \(q\) lifts, proving the displayed degree multiset. Its three possible degree values are distinct since \(d\ge2\).

**4. Compute the isotropic count.** When \(q\) is odd, diagonalize \(B\) and write \(Q(v)=B(v,v)\). Choose a nontrivial additive character \(\psi\) of \(k\). Character orthogonality and the quadratic Gauss sum \(G=\sum_{x\in k}\psi(x^2)\) give
\[
Z(B)=q^{-1}\sum_{t\in k}\sum_{v\in V}\psi(tQ(v)),
\qquad G^2=\eta(-1)q.
\]
For every nonzero \(t\), the inner sum is \(\eta(t)^d\eta(\det B)G^d\). For odd \(d\) the sum over \(t\ne0\) vanishes. For even \(d\) it gives exactly the sign-and-power correction in the stated formula. When \(q\) is even, \(Q(v+w)=Q(v)+Q(w)\) and \(Q(av)=a^2Q(v)\). Because the finite field is perfect, \(Q(v)=L(v)^2\) for a \(k\)-linear functional \(L\). If \(B\) is alternating, \(L=0\), and all vectors are isotropic; otherwise \(L\ne0\), and exactly \(q^{d-1}\) vectors are isotropic.

**5. The form type is recovered.** Over a finite field of odd order, nondegenerate symmetric forms have two isometry classes in each positive dimension, distinguished by the determinant square class. Multiplication of \(B\) by a nonzero scalar preserves determinant class when \(d\) is even, but interchanges the classes when \(d\) is odd; hence the similarity class is unique for odd \(d\), and there are exactly two for even \(d\). For even \(d\), the sign of the correction in step 4 separates them. Over a finite field of even order, every nondegenerate alternating form of even dimension is isometric to a symplectic form; every nondegenerate nonalternating symmetric form of any dimension is isometric to the identity form (over a perfect field). One elementary reduction splits off norm-one lines and uses the three-space change \(\langle1\rangle\perp H\cong\langle1,1,1\rangle\) to eliminate any remaining hyperbolic planes; every nonzero element of \(k\) has a square root. Hence in odd dimension there is one class and in even dimension there are two, distinguished by alternatingness and therefore by \(Z(B)\).

**6. Reconstruction.** The maximum vertex degree identifies precisely the universal socle vertices and recovers \(q\) as one plus their multiplicity. The graph has \(q^{d+1}-1\) vertices, so \(d\) is recovered. Its number of degree-\(q^d-2\) vertices recovers \(Z(B)\) by \(Z(B)=1+\#\{\deg=q^d-2\}/q\). Step 5 therefore recovers the similarity class of \(B\), and step 2 recovers the isomorphism class of the ring. Any ring isomorphism induces a graph isomorphism, which of course preserves degrees. This proves all equivalences.

## Verification

A standalone, standard-library Python program `verify.py` enumerates nonzero elements of the maximal ideal, directly computes graph adjacency from the bilinear multiplication, and compares the entire degree distribution with the theorem's formulas. It also checks \(Z(B)\) by exhaustive vector enumeration and the appropriate finite-field formula. The cases include both classes in dimensions two and four over \(\mathbb F_2\), both classes in dimensions two and four over \(\mathbb F_3\), and both classes in dimension two over \(\mathbb F_5\), plus odd-dimensional examples. The actual execution ended in `VERIFY_OK`. This finite check corroborates but is not substituted for the general proof.

For example, over \(\mathbb F_3\) in dimension two, \(B=\operatorname{diag}(1,1)\) gives degree multiplicities \(24\) at degree \(8\) and \(2\) at degree \(25\), whereas \(B'=\operatorname{diag}(1,2)\) gives \(12\) at degree \(7\), \(12\) at degree \(8\), and \(2\) at degree \(25\). Thus a graph degree multiset distinguishes the two nonisomorphic rings despite identical field, length, and Hilbert function.

## Relationship to prior work

Kadu and Tanpure, *Zero-divisors of Gorenstein rings* (arXiv:2609.36021v1, first posted September 28, 2026), compare the usual, associate-class and annihilator-compressed zero-divisor graphs of Artinian rings. Their main characterization detects whether an Artinian ring is Gorenstein from a comparison of two compressed graphs, rather than recovering the isomorphism type from the ordinary graph's degree multiset in this finite-field family.

Kadu, *On the problem of the finiteness of the clique number of compressed zero-divisor graphs of Artinian rings* (arXiv:2010.06924v1), Proposition 3.6, already establishes the bilinear zero-product correspondence and that Gorensteinness is nondegeneracy when the maximal ideal has principal square and cube zero. These are prior facts, not newly claimed. The present result is the *additional reconstruction step*: the simple graph's degree split remembers diagonal isotropy, which distinguishes the relevant finite-field form types and thereby identifies the whole ring in the specified class. The classical classification and isotropic counts of finite-field forms are also prior mathematics.

Arunkumar, Cameron, Kavaskar and Tamizh Chelvam, *Induced subgraphs of zero-divisor graphs* (arXiv:2207.11741v1), establish universality of induced subgraphs for broad ring families and investigate threshold graphs. This does not supply the degree-sequence reconstruction theorem for the stated Gorenstein class.

## Limitations

The result does **not** assert that arbitrary Artinian rings, or even arbitrary finite Gorenstein local rings without the given standard grading and Hilbert vector, are determined by their zero-divisor graphs. In particular, the general orthogonality reduction was known, and no claim of novelty is made for finite-field quadratic-form classification or Gauss sums. Though the sources above and several closely related published research records were compared, it remains possible that an equivalent reconstruction statement exists under different terminology in earlier literature.

## References

1. G. S. Kadu and V. B. Tanpure, *Zero-divisors of Gorenstein rings*, arXiv:2609.36021v1 (September 28, 2026), https://arxiv.org/html/2609.36021v1.
2. G. S. Kadu, *On the problem of the finiteness of the clique number of compressed zero-divisor graphs of Artinian rings*, arXiv:2010.06924v1 (2020), Proposition 3.6, https://arxiv.org/html/2010.06924v1.
3. G. Arunkumar, P. J. Cameron, T. Kavaskar and T. Tamizh Chelvam, *Induced subgraphs of zero-divisor graphs*, arXiv:2207.11741v1 (2022), https://arxiv.org/html/2207.11741v1.
