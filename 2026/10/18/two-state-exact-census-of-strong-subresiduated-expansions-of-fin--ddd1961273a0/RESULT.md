# Two-state exact census of strong subresiduated expansions of finite weak-order lattices

## Finding

Let \(h\ge1\) and let \(\mathbf n=(n_1,\ldots,n_h)\) be any vector of positive integers. Let \(P=A_1\oplus\cdots\oplus A_h\) be the ordinal sum of labeled antichains \(|A_i|=n_i\), and set \(L=\operatorname{Up}(P)\), with union and intersection as lattice operations. A **strong subresiduated expansion** is an operation \(\to\) on this fixed bounded distributive lattice for which a bounded sublattice \(D\subseteq L\) satisfies
\[
a\to b=\max\{d\in D:a\cap d\subseteq b\},\qquad
\Box a:=1\to a,\qquad
\Box(a\cup b)=\Box a\cup\Box b.
\]

There is a bijection from these expansions to order-preserving, regressive, idempotent maps \(f:P\to P\), given by
\[
\Box U=f^{-1}(U),\qquad a\to b=\Box(a\Rightarrow_L b),
\]
where \(\Rightarrow_L\) denotes the Heyting implication of the finite upset lattice. The map is uniquely determined by its fixed-point subset \(S\subseteq P\). Specifically, the complete fixed subsets are exactly those for which (i) \(S\cap A_1=A_1\), and (ii) whenever \(A_j\not\subseteq S\) for \(j>1\), the greatest index \(i<j\) with \(S\cap A_i\ne\varnothing\) satisfies \(|S\cap A_i|=1\).

The resulting numbers of expansions \(N(\mathbf n)\) and their isomorphism classes \(U(\mathbf n)\) admit exact **two-state recurrences**. For labeled expansions initialize
\[
(s_1,m_1)=\begin{cases}(1,0)&n_1=1,\\(0,1)&n_1\ge2.\end{cases}
\]
On reading a subsequent level of size \(n\), update
\[
\begin{array}{ll}
n=1:&(s',m')=(2s+m,0),\\[2pt]
n\ge2:&(s',m')=((n+1)s,(2^n-n-1)s+m).
\end{array}
\]
Then \(N(\mathbf n)=s_h+m_h\). For isomorphism classes use the same initialization but instead the transitions
\[
\begin{array}{ll}
n=1:&(s',m')=(2s+m,0),\\[2pt]
n\ge2:&(s',m')=(2s,(n-1)s+m),
\end{array}
\qquad U(\mathbf n)=s_h+m_h.
\]
The recurrences take \(O(h)\) arithmetic operations, without enumeration of subsets or expansion tables. In the uniform family \(\mathbf n=(1,m,\ldots,m)\) with \(t\ge0\) copies of \(m\ge2\), they specialize to
\[
N(1,\underbrace{m,\ldots,m}_{t})=
\frac{(2^m-1)(m+1)^t-(2^m-m-1)}{m},\qquad
U(1,\underbrace{m,\ldots,m}_{t})=m2^t-(m-1).
\]
For \(m=2\) and \(t=0,1,2,3\), the labeled counts are \(1,4,13,40\), whereas the isomorphism-class counts are \(1,3,7,15\).

## Assumptions and scope

All posets, lattices, maps and expansions in this result are finite; every layer size is a **positive integer**. "Labeled" means that points in each layer of the fixed poset are distinguished, and different binary operations on the fixed lattice are counted separately. "Isomorphism class" means isomorphism of the expanded algebra, including the bounded lattice; because the ordered layers are intrinsic to \(P\), its automorphism group is precisely \(\prod_{i=1}^h\operatorname{Sym}(A_i)\). No claim is made for general posets, non-strong subresiduated lattices, infinite lattices, or arbitrary algebraic signatures beyond the one stated.

## Proof

**1. From a strong expansion to a lattice endomorphism.** For any bounded sublattice \(D\) defining a subresiduated expansion, \(\Box a=\max\{d\in D:d\le a\}\). Thus \(\Box 0=0\), \(\Box1=1\), \(\Box a\le a\), \(\Box^2a=\Box a\), and
\[
\Box(a\cap b)=\Box a\cap\Box b.
\]
The last equality follows because the right-hand side is in \(D\) below \(a\cap b\) and every element of \(D\) below \(a\cap b\) is below both \(\Box a\) and \(\Box b\). The defining strong identity provides preservation of unions. Consequently \(\Box\) is an idempotent, contractive, bounded-lattice endomorphism of \(\operatorname{Up}(P)\).

Conversely, for any such endomorphism \(\Box\), its fixed-point set \(D=\operatorname{im}\Box\) is a bounded sublattice and \(\Box a\) is the greatest element of \(D\) below \(a\): for \(d\in D\) with \(d\le a\), \(d=\Box d\le\Box a\). Defining \(a\to b=\Box(a\Rightarrow_L b)\) gives the required maximum, since \(a\cap d\subseteq b\) iff \(d\le a\Rightarrow_L b\). Thus the transformations are inverse; one expansion corresponds to each such \(\Box\).

**2. Finite duality.** A bounded-lattice endomorphism of a finite upset lattice is uniquely the inverse-image operator \(U\mapsto f^{-1}(U)\) of an order-preserving \(f:P\to P\) (finite distributive lattice duality). Its contractivity is equivalent to \(f(x)\le x\): for every upset \(U\), \(f^{-1}(U)\subseteq U\) if and only if every upset containing \(f(x)\) also contains \(x\). Idempotence of \(\Box\) is equivalent to \(f^2=f\). This proves the announced bijection.

**3. Fixed-set normal form.** Let \(S=\{x:f(x)=x\}\). For every \(x\in P\), the set \(S\cap\downarrow x\) has greatest element \(f(x)\): indeed, \(f(x)\in S\cap\downarrow x\); if \(y\in S\cap\downarrow x\), then \(y=f(y)\le f(x)\). Conversely, any subset \(S\) for which these greatest elements exist defines an order-preserving, regressive, idempotent map by taking \(f(x)=\max(S\cap\downarrow x)\). Every minimal point must be fixed, so \(A_1\subseteq S\).

For \(x\in A_j\setminus S\), the fixed points below \(x\) consist of fixed points in lower layers only. They have a greatest member exactly when the **highest lower layer with fixed points contains a singleton of fixed points**. If \(x\in S\), then \(x\) itself is the greatest fixed point below \(x\), with no restriction on earlier layers. This proves both necessity and sufficiency of (i)–(ii). The resulting \(f\) is unique even when several layers are skipped.

**4. Labeled transfer.** After processing the first \(j\) layers, let \(s_j\) count admissible fixed subsets whose highest occupied layer has exactly one fixed point, and let \(m_j\) count those whose highest occupied layer has at least two. The first layer is entirely fixed, giving the stated initialization. Suppose the next layer has size \(n\). A partial layer (including the empty layer) can occur only from state \(s\). For \(n=1\), choosing no new fixed point (one choice) or fixing its point (one choice from either state) gives \((2s+m,0)\). For \(n\ge2\), the empty fixed set and the \(n\) singleton choices contribute \((n+1)s\) to the singleton state. All selections of size at least two contribute \((2^n-n-1)s\) from state \(s\), and the completely fixed new layer also contributes \(m\) from state \(m\). This is precisely the labeled recurrence, with no double counting because the fixed set determines the map.

**5. Orbits and the unlabelled transfer.** An automorphism of the base poset permutes points independently inside each antichain. It takes a fixed subset to another if and only if their numbers of fixed points in every layer agree. Therefore the orbits are precisely the admissible integer vectors \((k_1,\ldots,k_h)\) with \(k_j=|S\cap A_j|\). For \(n\ge2\) an occupied next layer can have sizes \(1,2,\ldots,n\) (one orbit each), or it can be empty. The two singleton-state successors are the empty and singleton choices; the \(n-1\) choices of sizes \(2,\ldots,n\) enter the multiple state, with only size \(n\) permitted after a multiple state. This proves the unlabelled recurrence. For \(n=1\) the earlier computation applies without binomial weights.

**6. Uniform closed forms.** When every appended level has size \(m\ge2\) and the first level has size one, the recurrence gives \(s_t=(m+1)^t\) and \(m_t=(2^m-m-1)\sum_{j=0}^{t-1}(m+1)^j\). The geometric sum yields the claimed \(N\). The orbit recurrence gives \(s_t=2^t\) and \(m_t=(m-1)(2^t-1)\), yielding the claimed \(U\). These formulas include the boundary \(t=0\) without a special exception.

## Verification

Run `python3 verify.py` with Python 3 and no external packages. The verifier exhaustively enumerates all regressive self-maps for every composition of \(1\) through \(7\) total points (127 level-size vectors), retains exactly the isotone idempotents, compares their unique fixed subsets with the normal form, and checks both recurrences. It separately enumerates bounded sublattices and the strong join-preservation identity for small upset lattices, checks literal conjugation orbits under products of level-permutation groups on several small instances, and checks extra selected instances up to nine points. The output ends with `DIRECT-LATTICE AGREEMENT OK`, `DP AND FIXED-POINT BIJECTION OK`, and `ALL UNLABELED-ORBIT RECURRENCES AGREED, INCLUDING LITERAL GROUP ACTIONS`.

These finite computations are cross-checks, **not** the proof for arbitrary \(h\) and \(n_i\). The six proof steps above establish the result for every finite positive level-size vector.

## Relationship to prior work

Celani and San Martín [1] defined and investigated the strong variety of subresiduated lattices and established structural frame characterizations; their Proposition 2.8 and Theorem 2.13 motivate considering fixed upset lattices. The generic fact that a regressive isotone idempotent of a finite poset is determined by its image is **not new**: it appears in Denton's dissertation [2, Proposition 3.3.5 and Proposition 3.3.9] and Hivert–Schilling–Thiéry [3, Proposition 2.4]. The contribution claimed here is restricted to the **exact two-state labeled and isomorphism-class recurrences for arbitrary level-size vectors in the strong subresiduated variety**, the explicit layerwise constraint, and their uniform closed forms. The already-known fixed-set principle is used as a premise, not claimed as an independent discovery.

## Limitations

The recurrences count expansions on a fixed underlying lattice and **not** all algebras of the strong variety with a given cardinality. No assertion is made that the corresponding numerical sequences, considered without their algebraic interpretations, are new. Relevant published work on generic poset retractions and order-preserving maps gives broader structural tools; a differently formulated prior counting theorem may exist. Independent mathematical validation and exhaustive worldwide literature coverage have not occurred.

## References

1. S. Celani and H. J. San Martín, *On the variety of strong subresiduated lattices*, Mathematical Logic Quarterly **69** (2023), 207–220, DOI: 10.1002/malq.202200067 (first public publisher date: 2023-07-11).
2. T. Denton, *Excursions into Algebra and Combinatorics at* \(q=0\), dissertation (2011), Chapter 3, Section 3.3.1, arXiv:1108.4379.
3. F. Hivert, A. Schilling and N. M. Thiéry, *The biHecke monoid of a finite Coxeter group and its representations*, Algebra & Number Theory **7** (2013), Proposition 2.4, page 604, DOI: 10.2140/ant.2013.7.595.
4. S. Celani, A. Nagy and H. J. San Martín, *Dualities for subresiduated lattices*, Algebra Universalis **82** (2021), article 59.
5. J. L. Castiglioni, V. Fernández, H. F. Mallea and H. J. San Martín, *On subreducts of subresiduated lattices and logic* (2022), arXiv:2211.02963.
