# Uniform orbit count for five-branch elementary-abelian rank-three curve actions

## Finding
For every odd prime \(p\), consider topological equivalence classes of faithful holomorphic \(G=(\mathbb Z/p)^3\)-actions on connected compact Riemann surfaces, where the quotient has genus zero and exactly five branch values, all with inertia order \(p\). The number of classes is
\[
N(p)=\frac{\binom{p+4}{5}+p\sum_{\substack{d\mid(p-1)\\d>1}}\varphi(d)\sum_{j=0}^{\lfloor5/d\rfloor}\binom{(p-1)/d+j-1}{j}+(p-1)\mathbf 1_{p=5}}{p(p-1)}-2.
\]
In particular \(N(3)=3\), \(N(5)=7\), \(N(7)=12\), \(N(11)=29\), and \(N(13)=42\). Every curve in this family has genus \(1+(3p^3-5p^2)/2\).

## Assumptions and scope
The ground field is \(\mathbb C\). A topological equivalence identifies orientation-preserving surface actions after an abstract automorphism of \(G\) and an orientation-preserving homeomorphism of surfaces; branch values are not marked or ordered. Every local monodromy is nonzero in \(G\), the five monodromies sum to zero, and their linear span is \(G\). The claim counts topological types, not individual holomorphic isomorphism classes at fixed branch-point positions.

## Proof
The Riemann existence theorem identifies the required actions with surjective monodromy homomorphisms from the five-punctured sphere, up to the mapping class/braid action and \(\operatorname{Aut}(G)=\operatorname{GL}_3(\mathbb F_p)\). Since \(G\) is abelian, braid moves merely permute the five local monodromies. Thus an action is represented by a rank-three \(3\times5\) matrix \(M\) over \(\mathbb F_p\), with every column nonzero and with column sum zero, modulo left \(\operatorname{GL}_3\) and column \(S_5\).

Let \(H=\{(x_1,\ldots,x_5)\in\mathbb F_p^5:\sum_i x_i=0\}\), a four-dimensional space. The row space of \(M\) is a three-dimensional hyperplane in \(H\); conversely every such hyperplane yields a rank-three sum-zero matrix, unique up to left \(\operatorname{GL}_3\). Such hyperplanes are parametrized by nonzero linear forms \(\ell\in H^*\) modulo nonzero scalar. The restriction map identifies \(H^*\cong\mathbb F_p^5/\langle(1,1,1,1,1)\rangle\): represent \(\ell\) by \((a_1,\ldots,a_5)\), modulo simultaneous additive translation of all five entries, and nonzero scalar multiplication. After the \(S_5\) quotient, this is precisely the orbit set of five-element multisets of \(\mathbb F_p\) under \(\operatorname{AGL}_1(\mathbb F_p)\), except that the all-equal multisets represent zero forms and are excluded.

The \(i\)-th column of \(M\) vanishes if and only if the \(i\)-th coordinate functional vanishes throughout its row space; because that row space is a hyperplane of \(H\), this occurs precisely when \(\ell\) is proportional to the restriction of that coordinate functional. Such a form has coefficient multiset \((a,a,a,a,b)\) with \(a\ne b\). All five forbidden coordinate points belong to one \(S_5\)-orbit; equivalently all such multisets form one affine orbit, of multiplicity pattern \((4,1)\). Consequently the desired number is the number of affine orbits on all five-element multisets, minus exactly two.

Apply Burnside's lemma to the \(p(p-1)\) affine maps \(x\mapsto ux+v\). The identity fixes \(\binom{p+4}{5}\) multisets. For \(u=1\), \(v\ne0\), the permutation on the field is a single \(p\)-cycle; it fixes a five-element multiset exactly if \(p=5\), in which case the only fixed multiset contains every field element once. There are \(p-1\) such translations. For \(u\ne1\) of multiplicative order \(d>1\), the map has a unique fixed point and \((p-1)/d\) cycles of length \(d\). Its fixed multisets have generating function \((1-z)^{-1}(1-z^d)^{-(p-1)/d}\), and their number is
\[
F_d=\sum_{j=0}^{\lfloor5/d\rfloor}\binom{(p-1)/d+j-1}{j}.
\]
There are exactly \(p\varphi(d)\) such affine transformations of order type \(d\). Summation and the subtraction of two excluded orbits give the formula.

Riemann–Hurwitz yields \(2g-2=p^3(-2+5(1-1/p))=3p^3-5p^2\), proving the genus formula.

## Verification
The accompanying standalone `check_rank3_five.py` enumerates the affine orbits on unordered five-tuples directly for the primes \(3,5,7,11,13\), and independently compares them with the divisor-sum expression. The general proof is Burnside's lemma together with the row-space equivalence; finite enumeration alone would not prove the result for arbitrary primes.

## Relationship to prior work
Disney-Hogg and Zuev discuss topological equivalence and computational classification of surface actions. Broughton and Wootton develop the generating-vector method for finite abelian actions, with detailed special counts for three and four branch points. Weaver counts zero-sum multisets arising from rank-two elementary abelian groups. The present result evaluates the first five-branch rank-three case uniformly in odd prime order, reducing its classification to affine orbits on a field.

## Limitations
This counts topological equivalence classes only, not moduli components with a chosen labelling, holomorphic isomorphism classes at specified cross-ratios, or rank-three actions with more than five branch points. Existing general generating-vector theory supplies the underlying reduction, and an unlocated earlier specialization of its orbit calculation cannot be excluded.

## References
- L. Disney-Hogg and M. Zuev, *Deep Learning of Topological Equivalence Classes*, arXiv:2610.21981v1 (2026).
- S. A. Broughton and A. Wootton, *Finite abelian subgroups of the mapping class group*, arXiv:math/0611650v1 (2006).
- A. Weaver, *Zero-sum multisets mod p with an application to surface automorphisms*, arXiv:1703.02147v5.
