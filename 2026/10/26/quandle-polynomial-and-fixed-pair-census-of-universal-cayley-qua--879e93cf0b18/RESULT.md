# Quandle polynomial and fixed-pair census of universal Cayley quandles

## Finding

Let \(n\geq1\), and let \(Q_n=[n]\times S_n\) carry the quandle operation introduced for the universal Cayley-type embedding of finite quandles:
\[
(x,g)\triangleleft(y,h)=(x^{g^{-1}h},h^{-1}gh).
\]
Here permutations act on the right, so \(x^{ab}=(x^a)^b\). For a finite quandle \(Q\), define
\[
 c(a)=\#\{b\in Q:b\triangleleft a=b\},\qquad
 r(a)=\#\{b\in Q:a\triangleleft b=a\},\quad
 \operatorname{qp}_Q(s,t)=\sum_{a\in Q}s^{c(a)}t^{r(a)}.
\]
For any partition \(\lambda=(1^{m_1}2^{m_2}\cdots)\vdash n\), put
\[
 z_\lambda=\prod_{d\geq1}d^{m_d}m_d!,\qquad
 k_\lambda=\#\{d:m_d>0\}.
\]
Then the **entire two-variable quandle polynomial** is
\[
 \boxed{\operatorname{qp}_{Q_n}(s,t)=
 \sum_{\lambda\vdash n}\frac{n!}{z_\lambda}
 \sum_{d:m_d>0}d m_d\,
 s^{z_\lambda k_\lambda}t^{n z_\lambda/(d m_d)}.}
\]
Equivalently, the number of ordered pairs \((a,b)\in Q_n^2\) with \(a\triangleleft b=a\) is exactly
\[
 \boxed{n\,n!\sum_{j=0}^{n-1}p(j),}
\]
where \(p(0)=1\) and \(p(j)\) denotes the ordinary partition number. Thus the fixed-pair probability is
\[
 \boxed{\frac{\sum_{j=0}^{n-1}p(j)}{n\,n!}
 \sim\frac{\sqrt{6}}{\pi}\frac{p(n)}{\sqrt n\,n!}}
 \quad (n\to\infty).
\]
For \(n\ge3\), the coefficient of \(s^n t^n\) is exactly \(n!\), contributed precisely by elements whose permutation coordinate is an \(n\)-cycle.

## Assumptions and scope

All groups and sets considered below are finite, and sets on which they act are nonempty. No transitivity or faithfulness hypothesis is imposed in the general lemma. The polynomial is the ordinary \((1,1)\) quandle polynomial, not the full family of generalized \((m,k)\) polynomials. All equalities and counts are exact for every positive integer \(n\).

For a right action of \(G\) on \(X\), write \(G_x=\{g\in G:x^g=x\}\), \(C_G(g)=\{h\in G:hg=gh\}\), and \(o_g\) for the number of orbits of \(C_G(g)\) acting on \(X\). Form the action quandle \(Q(X,G)=X\times G\) with the multiplication displayed above, with \(G\) in place of \(S_n\).

## Proof

**General action-quandle formula.** Fix \(a=(x,g)\in Q(X,G)\). For \(b=(y,h)\), the equality \(a\triangleleft b=a\) means simultaneously that \(h\in C_G(g)\) and \(g^{-1}h\in G_x\). Multiplication by \(g^{-1}\) is a bijection of \(C_G(g)\), while \(y\) is arbitrary. Hence
\[
 r(x,g)=|X|\,|C_G(g)\cap G_x|.
\]
For the reverse relation \(b\triangleleft a=b\), the conditions are \(h\in C_G(g)\) and \(y^{h^{-1}g}=y\). As \(h\) varies over the centralizer, \(h^{-1}g\) varies bijectively over that centralizer. Burnside's orbit-counting lemma therefore gives
\[
 c(x,g)=\sum_{k\in C_G(g)}|\operatorname{Fix}_X(k)|
       =|C_G(g)|\,o_g.
\]
Consequently
\[
 \operatorname{qp}_{Q(X,G)}(s,t)=
 \sum_{g\in G}\sum_{x\in X}
 s^{|C_G(g)|o_g}\,t^{|X|\,|C_G(g)\cap G_x|}.
\]
These equations include trivial and nonfaithful actions without modification.

**Specialization to the symmetric group.** If \(g\in S_n\) has cycle type \(\lambda=(1^{m_1}2^{m_2}\cdots)\), standard disjoint-cycle counting gives \(|C_{S_n}(g)|=z_\lambda\) and \(n!/z_\lambda\) permutations of this type. The centralizer acts transitively on the union of all cycles of each fixed length \(d\), and it preserves cycle length. Its orbits on \([n]\) therefore have sizes \(d m_d\) for \(m_d>0\), and their number is \(k_\lambda\). If \(x\) belongs to a \(d\)-cycle, orbit-stabilizer gives
\[
 |C_{S_n}(g)\cap (S_n)_x|=\frac{z_\lambda}{d m_d}.
\]
Inserting these into the general formula, and counting the \(d m_d\) choices of \(x\), proves the displayed partition sum for \(\operatorname{qp}_{Q_n}\).

**Fixed-pair census.** Summing \(c(a)\) over \(a\in Q_n\) counts each ordered pair satisfying \(b\triangleleft a=b\) once. By the preceding formulas,
\[
 \sum_{a\in Q_n}c(a)
 =\sum_{\lambda\vdash n}\frac{n!}{z_\lambda}\,n\,z_\lambda k_\lambda
 =n\,n!\sum_{\lambda\vdash n}k_\lambda.
\]
Counting pairs \((\lambda,d)\) with \(d\) a part size present in \(\lambda\) yields
\[
 \sum_{\lambda\vdash n}k_\lambda
 =\sum_{d=1}^n p(n-d)=\sum_{j=0}^{n-1}p(j),
\]
since deleting one part of size \(d\) is a bijection onto partitions of \(n-d\). As \(|Q_n|=n\,n!\), division by \(|Q_n|^2\) proves the exact probability.

For the asymptotic, the Hardy–Ramanujan formula \(p(n)\sim e^{\pi\sqrt{2n/3}}/(4\sqrt3\,n)\), together with its uniform local ratio for \(j=O(\sqrt n\log n)\), gives
\[
 \frac{1}{p(n)}\sum_{j=0}^{n-1}p(j)
 \sim \sum_{k\ge1}\exp\left(-\frac{\pi k}{\sqrt{6n}}\right)
 \sim\frac{\sqrt{6n}}{\pi}.
\]
The omitted tail is negligible by the same partition-growth bound. Substitution establishes the claimed fixed-pair probability asymptotic.

**Minimal bidegree.** The \(C_{S_n}(g)\)-orbits on \([n]\) have total size \(n\), and each has size at most \(z_\lambda\). Hence \(n\le k_\lambda z_\lambda=c(x,g)\). For \(n\ge3\), equality requires a single \(n\)-cycle. Indeed, when at least two cycle lengths occur, a nontrivial rotation of one length fixes every point in another length's orbit, making at least one orbit smaller than the centralizer. With only one cycle length \(d\) and multiplicity \(m\), the sole orbit has size \(dm=n\), while the centralizer has order \(d^m m!\); equality for \(n\ge3\) forces \(m=1\). Conversely an \(n\)-cycle has \(z_\lambda=n\), \(k_\lambda=1\), and \(r(x,g)=n\). There are \((n-1)!\) such permutations and \(n\) marked points, proving the coefficient \(n!\).

## Verification

The accompanying standalone `verify.py` constructs \(Q_n\) directly for \(1\le n\le5\), counts both fixing relations for each element by enumerating all ordered pairs, and compares every monomial coefficient with the partition formula. It additionally checks the total fixed-pair count and the minimal-bidegree coefficient. Its observed output ends with:

`VERIFY_OK degrees=5 operation_comparisons=739114`

The comparison count includes both orientations of each ordered-pair test. The general proof, not this finite enumeration, establishes the theorem for arbitrary \(n\). Running `python3 verify.py` requires only the Python standard library.

For instance,
\[
 \operatorname{qp}_{Q_3}(s,t)=
 6s^3t^3+6s^4t^3+3s^4t^6+3s^6t^6,
\]
and precisely \(72\) of the \(18^2\) ordered pairs in \(Q_3^2\) satisfy the fixing relation.

## Relationship to prior work

The action quandle \(X\times_{\Phi}G\) and the universal quandle \(Q_n\) are due to R. Kai, *Quandles associated with group actions*, arXiv:2609.17438 (first public version 15 September 2026). That paper proves the embedding theorem and classifies the connected components by a cycle type and a distinguished cycle length, but does not give Nelson's quandle polynomial or a fixed-pair partition formula. The present calculation uses the same quandle operation and adds the pointwise fixing statistics required by the polynomial.

The polynomial invariant itself is due to S. Nelson; its standard \((m,k)\) definition is reviewed in T. Carrell and S. Nelson, *On rack polynomials*, arXiv:0809.5075, Section 2. The singleton-action case of the general lemma recovers the elementary conjugation-quandle centralizer formula; that special case is not claimed as new. Earlier generalized polynomial work and the source's orbit classification provide tools, but neither inspected text states the complete polynomial of \(Q_n\) or its partition-number fixing density.

## Limitations

This determines only the ordinary two-variable quandle polynomial and first-iterate fixing relation. It does not determine generalized higher-iterate quandle polynomials, link-coloring enhancements, or the number of embeddings of a given quandle into \(Q_n\). The asymptotic invokes the classical partition asymptotic rather than proving it anew. Direct computations were performed only for \(n\le5\); the proof is the basis of the arbitrary-\(n\) claims. A residual literature risk is the possibility of an unindexed calculation of the same polynomial for the equivalent matrix-rack-to-quandle construction.

## References

1. R. Kai, *Quandles associated with group actions*, arXiv:2609.17438, first posted 2026-09-15, revised 2026-09-22, https://arxiv.org/abs/2609.17438.
2. T. Carrell and S. Nelson, *On rack polynomials*, arXiv:0809.5075, 2008, https://arxiv.org/abs/0809.5075.
3. S. Nelson, *A polynomial invariant of finite quandles*, arXiv:math/0702038, 2007, https://arxiv.org/abs/math/0702038.
4. G. H. Hardy and S. Ramanujan, *Asymptotic formulae in combinatory analysis*, Proceedings of the London Mathematical Society (1918), the classical partition asymptotic.
