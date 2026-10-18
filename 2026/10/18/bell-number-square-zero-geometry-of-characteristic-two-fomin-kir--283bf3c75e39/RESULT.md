# Bell-number square-zero geometry of characteristic-two Fomin–Kirillov algebras

## Finding
For every field \(k\) of characteristic \(2\) and integer \(n\ge2\), the reduced affine variety \(X_n\) of degree-one square-zero elements of the Fomin–Kirillov quadratic algebra \(\mathcal E_n(k)\) is a finite union of explicitly described linear subspaces. Every \(a\in(\mathcal E_n)_1\) with \(a^2=0\) has a unique weighted set-partition description: partition \([n]\) into blocks, assign a nonzero scalar to each block of size at least two, give every edge inside that block this scalar, and give all edges joining blocks coefficient zero. Conversely every such assignment squares to zero.

For every power \(q\) of two, the exact number of degree-one square-zero elements is
\[
N_n(q)=\sum_{\pi\in\Pi_n}(q-1)^{b_{\ge2}(\pi)},\qquad
\sum_{n\ge0}N_n(q)\frac{t^n}{n!}=\exp\!\left(t+(q-1)(e^t-1-t)\right),
\]
where \(b_{\ge2}(\pi)\) counts blocks of size at least two. In particular \(N_n(2)\) is the \(n\)-th Bell number.

For a set partition \(\pi\), write \(s_B=\sum_{i<j,\ i,j\in B}x_{ij}\) and \(L_\pi=\operatorname{span}_k\{s_B: B\in\pi,\ |B|\ge2\}\). Then
\[
X_n=\bigcup_{\pi\in\Pi_n}L_\pi.
\]
Its irreducible components are **exactly** the distinct linear spaces \(L_\pi\) for partitions having at most one singleton block. The component has dimension \(b_{\ge2}(\pi)\), the largest dimension is \(\lfloor n/2\rfloor\), and the component-count exponential generating series is
\[
\sum_{n\ge0}c_n\frac{t^n}{n!}=(1+t)\exp(e^t-1-t).
\]
For \(n\ge4\), the reduced variety is non-equidimensional. The number of components of maximal dimension is \(n!/(2^m m!)\) if \(n=2m\), and \(n!/(2^m m!)+n!/(3!\,2^{m-1}(m-1)!)\) if \(n=2m+1\).

## Assumptions and scope
Work over an arbitrary field \(k\) of characteristic exactly \(2\). The quadratic Fomin–Kirillov algebra \(\mathcal E_n(k)\) has generators \(x_{ij}\) for distinct \(i,j\in[n]\) with \(x_{ij}=-x_{ji}\), square relations \(x_{ij}^2=0\), disjoint-edge commutations \(x_{ij}x_{kl}=x_{kl}x_{ij}\), and triangle relations \(x_{ij}x_{jk}+x_{jk}x_{ki}+x_{ki}x_{ij}=0\) for pairwise distinct indices. In characteristic two, \(x_{ij}=x_{ji}\). The degree-one part \(V\) is freely spanned by \(x_{ij}\), \(i<j\). The quadratic equations defining \(X_n\) are the coordinates of \(a^2\in(\mathcal E_n)_2\); \(X_n\) denotes their **reduced** zero locus, not the potentially nonreduced equation scheme. The set-partition description holds for \(k\)-points over every such field, and the asserted geometric irreducible components hold after any algebraic closure.

## Proof
**1. Independent triple constraints.** Write \(a=\sum_{i<j}\lambda_{ij}x_{ij}\). The square of a basis generator vanishes. Contributions from two disjoint edges cancel because those generators commute and the field has characteristic two. The quadratic relations preserve the multiset of labels supporting a length-two word; hence contributions indexed by different unordered triples cannot cancel one another. In the degree-two subspace for one triple \(i<j<k\), abbreviate \(A=x_{ij},B=x_{ik},C=x_{jk}\), with coefficients \(u,v,w\). The defining triangle relations are exactly
\[
AC+CB+BA=0,\qquad CA+AB+BC=0.
\]
These two relations are independent, and their coefficients on the separate words \(AC\) and \(CA\) are respectively one and zero, zero and one. Therefore the images of \(AB+BA\) and \(BC+CB\) are linearly independent in the degree-two quotient: any relation among them in the span of the two defining triangle relations would force both triangle-relation coefficients to vanish. (No other quadratic relation uses just this unordered triple.) Eliminating \(AC\) and \(CA\) yields
\[
(a^2)_{\{i,j,k\}}=u(v+w)(AB+BA)+w(u+v)(BC+CB).
\]
Thus \(a^2=0\) if and only if, for every unordered triple, the three edge coefficients are either all zero, have precisely one nonzero entry, or are all equal and nonzero. This is equivalently \(u(v+w)=w(u+v)=0\) on every triple.

**2. From triples to colored blocks.** Put an edge between \(i\) and \(j\) when \(\lambda_{ij}\ne0\). Two adjacent edges force their third edge to exist and all three coefficients to agree, by Step 1. In any connected component, repeated closure of length-two paths produces every missing edge: if two vertices are joined by a shortest path of length at least two, its first two edges give a shorter path. Hence each connected component of size at least two is complete. Triangle equalities propagate a unique common coefficient across its edges (for a two-vertex component this is immediate). Between components all coefficients vanish. Each square-zero coefficient vector therefore gives exactly one set partition (its connected components) and one nonzero scalar on every nonsingleton block. Conversely any such weighted partition satisfies the triple constraints. This proves the classification and the formula for \(N_n(q)\).

**3. Enumeration.** A singleton block has exponential weight \(t\); for a block of cardinality at least two the nonzero scalar has \(q-1\) choices and contributes \((q-1)t^j/j!\). The labeled exponential formula gives the stated generating function, with \(q=2\) recovering all set partitions. This is exact for all prime powers \(q=2^f\) and all \(n\ge0\) (the latter convention sets \(N_0(q)=1\)).

**4. Linear components.** Fixing a partition but allowing each nonsingleton-block weight to vary freely, including zero, gives exactly the linear subspace \(L_\pi\). Every square-zero point lies in such a space and every point of that space is square-zero. For partitions \(\pi,\rho\), one has \(L_\pi\subseteq L_\rho\) if and only if every block of \(\pi\) of size at least two is also a block of \(\rho\): indeed \(s_B\) has support on all edges of the complete graph on \(B\), so it cannot be represented by disjoint clique-edge sums other than the identical block \(B\). In particular \(L_\pi\) is maximal if and only if \(\pi\) has zero or one singleton (with two or more singletons one can merge two into a new block without changing the existing generators). Finite unions of linear spaces are reduced unions of geometrically irreducible closed sets, so these and only these maximal spaces are the geometric irreducible components. Their dimensions are their numbers of nonsingleton blocks, since the supports of the generators \(s_B\) are disjoint and nonempty.

**5. Component profile.** The label-species description with any number of nonsingleton blocks but at most one singleton yields \((1+t)\exp(e^t-1-t)\). The largest possible number of nonsingleton blocks is \(\lfloor n/2\rfloor\). For even \(n=2m\), maximal-dimensional components correspond exactly to pair partitions; for odd \(n=2m+1\), to pair partitions with one singleton or to one triple together with \(m-1\) pairs. These give the stated factorial counts. For every \(n\ge4\) the one-block partition produces a one-dimensional component, while pairing as many labels as possible gives dimension at least two, proving non-equidimensionality.

## Verification
The accompanying standalone `verify.py` independently constructs all defining quadratic relations and reduces squares against their full degree-two linear span over \(\mathbf F_2\) and \(\mathbf F_4\); it does not assume the triple lemma. Exhaustive coefficient-vector checks were performed for \((n,q)=(2,2),(3,2),(3,4),(4,2),(4,4),(5,2),(6,2)\). Counts were respectively \(2,5,13,15,61,52,203\). Additional exhaustive set-partition subspace-inclusion tests for \(2\le n\le6\) found component counts \(1,4,8,31,107\). The local reduction and support argument above are proofs for every \(n\), not inductions inferred from these computations. Replay: `python3 verify.py`; success marker: `VERIFY_OK_FK_CHARACTERISTIC_TWO`.

## Relationship to prior work
The generators and quadratic relations are those of the classical Fomin–Kirillov algebra (Fomin and Kirillov, 1997; Kirillov's publicly archived 1997 paper). Blasiak, Liu and Mészáros study its subalgebras, Hilbert series and the grading by set partitions; those structural investigations do not give the weighted Bell count of degree-one square-zero elements or the stated characteristic-two reduced-component decomposition in the material inspected. Liu's *commutative quotient* differs from the noncommutative algebra in which the square condition is evaluated: in characteristic two every degree-one element in the quotient squares to zero, so that quotient's classification cannot imply the stricter locus here. Kirillov's later survey develops broader quadratic-algebra constructions, and Ștefan–Vay compute cohomology for the three-generator algebra under hypotheses excluding characteristic two. The explicit result here is the original-algebra square-zero locus and its reduced geometry, not a claim to rediscover the quadratic presentation, the standard set-partition grading, or the Bell numbers.

## Limitations
No statement is made about square-zero elements of degree greater than one, the entire algebra's dimension or Hilbert series, the unreduced defining scheme, nilpotent elements of index greater than two, or characteristics other than two. Earlier equivalent results might exist under descriptions of Nichols algebras or quadratic algebra nilpotent loci; the original 1997 paper and lengthy later survey were not exhaustively read from start to finish, so absolute priority is not certified. A self-review does not constitute independent validation.

## References
1. S. Fomin and A. N. Kirillov, *Quadratic Algebras, Dunkl Elements, and Schubert Calculus* (1997), foundational algebra presentation (earliest public day not established).
2. A. N. Kirillov, *On Some Quadratic Algebras*, arXiv:q-alg/9705003 (first publicly archived 6 May 1997), especially the defining quadratic relations and later degree-two combinatorics. https://arxiv.org/abs/q-alg/9705003
3. J. Blasiak, R. I. Liu and K. Mészáros, *Subalgebras of the Fomin–Kirillov Algebra*, arXiv:1310.4112 (2013), especially Section 2 and the set-partition grading. https://arxiv.org/abs/1310.4112
4. R. I. Liu, *On the Commutative Quotient of Fomin–Kirillov Algebras*, arXiv:1409.4872 (2014). https://arxiv.org/abs/1409.4872
5. A. N. Kirillov, *On Some Quadratic Algebras I 1/2*, arXiv:1502.00426 (2015). https://arxiv.org/abs/1502.00426
6. D. Ștefan and C. Vay, *The Cohomology Ring of the 12-Dimensional Fomin–Kirillov Algebra*, arXiv:1404.5101 (2014). https://arxiv.org/abs/1404.5101
