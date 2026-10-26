# Exact additive commutator fibers over finite chain rings

## Finding
Let \(R\) be any finite commutative chain ring with maximal ideal \((\pi)\), residue-field cardinality \(q\), and length \(m\ge1\), so \(\pi^m=0\) and \(|R|=q^m\). For a trace-zero matrix \(C\in M_2(R)\), put \(s(C)=\min\{\nu(C_{ij}):1\le i,j\le2\}\), with \(\nu(0)=m\). Define
\[
\Phi_R(C)=\#\{(X,Y)\in M_2(R)^2:XY-YX=C\}.
\]
For every \(C\ne0\), \(0\le s=s(C)<m\), and the **exact fiber size** is
\[
\boxed{\Phi_R(C)=(q+1)\bigl(q^{5m+s-1}-q^{5m-2}\bigr).}
\]
For the zero target, the same complete distribution has
\[
\boxed{\Phi_R(0)=q^{5m}+\sum_{a=0}^{m-1}\left(q^{3(m-a)}-q^{3(m-a-1)}\right)q^{3m+2a}.}
\]
Every trace-zero target is represented; all other targets have empty fibers. In particular the entire additive commutator distribution depends only on \(q,m\) and the common entry valuation of the target, not on the isomorphism type or characteristic of the chain ring.

## Assumptions and scope
A finite commutative chain ring means a finite commutative unital local ring whose ideals are the powers \(R,(\pi),\ldots,(\pi^m)=0\) with nonzero successive quotients of size \(q\). Every element has a unique valuation \(\nu(x)\in\{0,\ldots,m\}\), with \(\nu(0)=m\); an element of valuation \(a<m\) belongs to \(\pi^aR\setminus\pi^{a+1}R\). Matrix commutators here are additive, not multiplicative commutators of invertible matrices. There is no restriction on characteristic: the proof applies equally to \(\mathbb F_q[t]/(t^m)\), \(\mathbb Z/p^m\mathbb Z\), and more general finite commutative chain rings.

## Proof
**Reduction to a cross product.** Every matrix \(X\) decomposes uniquely as \(X=\alpha I+U(b,c,d)\), where
\[
U(b,c,d)=\begin{pmatrix}0&b\\c&d\end{pmatrix},\qquad \alpha,b,c,d\in R.
\]
Writing \(Y=\beta I+U(b',c',d')\), direct multiplication gives
\[
[X,Y]=\begin{pmatrix}e&f\\g&-e\end{pmatrix},\quad e=bc'-b'c,\quad f=bd'-b'd,\quad g=dc'-d'c.
\]
The three coordinates \((e,f,g)\) are obtained from \((b,c,d)\wedge(b',c',d')\) by a signed permutation. This is an invertible linear identification of \(\bigwedge^2R^3\) with the free rank-three trace-zero module, even in characteristic two. Each pair of vectors has exactly \(q^{2m}\) scalar lifts \((\alpha,\beta)\). Thus it remains to count pairs \((u,v)\in(R^3)^2\) with prescribed cross product \(h\in R^3\).

**Valuation orbits.** The group \(\operatorname{SL}_3(R)\) acts transitively on primitive vectors, as well as on primitive elements of \(\bigwedge^2R^3\) under its exterior-square action. Therefore all nonzero target forms with valuation \(s\) have the same fiber size, and we may count \(h=\pi^s e_3\). The claim follows alternatively by elementary invertible row changes on the target form.

**Nonzero target.** Let \(u\in R^3\) have valuation \(a\). If \(a>s\), then \(u\wedge v=h\) is impossible. For \(0\le a\le s\), write \(u=\pi^a u_0\), with primitive \(u_0\in(R/(\pi^{m-a}))^3\). The map \(v\mapsto u\wedge v\) has image of size \(q^{2(m-a)}\), kernel of size \(q^{m+2a}\), and its image consists precisely of \(\pi^a\)-divisible two-forms whose divided image annihilates \(u_0\) under the perfect wedge pairing. For \(h=\pi^s e_3\), the condition is that the third coordinate of \(u_0\) be divisible by \(\pi^{m-s}\) in \(R/(\pi^{m-a})\). The first two coordinates must not both be nonunits. Hence exactly
\[
q^{s-a}\bigl(q^{2(m-a)}-q^{2(m-a-1)}\bigr)
\]
vectors \(u\) of valuation \(a\) allow this target. Each admits \(q^{m+2a}\) choices of \(v\). Summing over \(a\) gives
\[
\begin{aligned}
\#\{(u,v):u\wedge v=h\}&=\sum_{a=0}^s q^{s-a}\bigl(q^{2(m-a)}-q^{2(m-a-1)}\bigr)q^{m+2a}\\
&=(1-q^{-2})q^{3m+s}\sum_{a=0}^s q^{-a}\\
&=(q+1)\bigl(q^{3m+s-1}-q^{3m-2}\bigr).
\end{aligned}
\]
Multiplication by \(q^{2m}\) proves the asserted nonzero fiber law.

**Zero target.** For \(u=0\), there are \(q^{3m}\) possibilities for \(v\). For each \(a<m\), there are \(q^{3(m-a)}-q^{3(m-a-1)}\) vectors \(u\) of valuation \(a\); for each, the same wedge map has kernel of size \(q^{m+2a}\). Thus the zero cross-product fiber equals
\[
q^{3m}+\sum_{a=0}^{m-1}\bigl(q^{3(m-a)}-q^{3(m-a-1)}\bigr)q^{m+2a}.
\]
The scalar lift factor \(q^{2m}\) gives the displayed zero-target expression. All powers are nonnegative in the actual finite sum. Conversely, additive commutators have trace zero. Every displayed nonzero fiber is positive, completing the classification. \(\square\)

## Verification
The accompanying standalone `verify.py` computes additive and multiplicative tables for both \(\mathbb Z/p^m\mathbb Z\) and \(\mathbb F_p[t]/(t^m)\), directly enumerates the cross-product fibers for all targets, and compares them with the two proved formulas. It passes all targets for \((p,m)=(2,1),(3,1),(2,2),(3,2),(2,3)\) for both types of ring. The corresponding zero-matrix commutator fibers are respectively \(88,945,6400,741393,434176\). These finite checks test boundary cases and distinct characteristics, but do not replace the general ring-theoretic proof.

## Relationship to prior work
Stasinski (2012) proves that every trace-zero matrix over a principal ideal ring is one additive commutator; this establishes the **support** of the map but not its multiplicity distribution. Earlier work of Lissner and Albert--Muckenhoupt establishes existence in more restricted settings. Britnell and Wildon (2011) consider commutation of similarity classes over fields, a different orbit-pair problem. Yuen (2006) studies the jet schemes of rank-one determinantal varieties; their geometry constrains the **zero fiber** after the cross-product reduction but does not give the nonzero target-by-target valuation distribution here, nor the universal mixed-characteristic fiber law. The signed-wedge identification, the valuation-fiber count and the ring-independent closed nonzero profile are the specific assertion assessed here.

## Limitations
The result does not classify multiplicative group commutators, matrices of size greater than two, or fibers over arbitrary non-chain rings. Determining priority against every earlier local-ring character-sum or cross-product enumeration remains open; no claim of independent certification is made. Its proof is purely elementary and finite, not evidence of novelty by itself.

## References
1. A. Stasinski, *Similarity and commutators of matrices over principal ideal rings*, arXiv:1211.6872 (first public posting 2012-11-29), https://arxiv.org/abs/1211.6872.
2. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, Journal of the London Mathematical Society 83 (2011), https://doi.org/10.1112/jlms/jdq088.
3. C. Yuen, *Jet schemes of determinantal varieties*, arXiv:math/0608632 (2006), https://arxiv.org/abs/math/0608632.
4. A. Stasinski, *Commutators of trace zero matrices over principal ideal rings*, arXiv:1607.07205 (2016), https://arxiv.org/abs/1607.07205.
