# The three-rank two-sided ideal order of finite magma monoids

## Finding

Let \(X\) be a nonempty finite set of size \(n\), and let \(\mathcal M(X)\) be the monoid of binary operations on \(X\) with multiplication
\[
  (f\triangleleft g)(x,y)=g(f(x,y),f(y,x)).
\]
For an operation \(f\), its pair map \(T_f:X^2\to X^2\) is
\[
 T_f(x,y)=(f(x,y),f(y,x)).
\]
Write \(\Delta=\{(x,x):x\in X\}\), and let \(\iota(x,y)=(y,x)\). Define three integers:
\[
 c(f)=|T_f(\Delta)|,\qquad
 d(f)=|T_f(X^2)\cap\Delta|,\qquad
 a(f)=\tfrac12|T_f(X^2)\setminus\Delta|.
\]
(The last set is a union of two-point \(\iota\)-orbits.) For any \(f,h\in\mathcal M(X)\), the following is an exact test for two-sided ideal containment:
\[
 \boxed{\;h\in\mathcal M(X)f\mathcal M(X)
 \iff c(h)\le c(f),\quad a(h)\le a(f),\quad
 d(h)+a(h)\le d(f)+a(f).\;}
\]
Consequently, the Green \(\mathcal J\)-classes are **precisely** the fibers of \((c,d,a)\). If \(N=\binom n2\), the occurring triples are precisely
\[
 1\le c\le d\le n,\qquad 0\le a\le N,\qquad d-c+a\le N.
\]
The number of \(\mathcal J\)-classes, equivalently of distinct principal two-sided ideals, is
\[
 \boxed{\;J(n)=\frac{n(n+1)(3n^2-5n+8)}{12}\;}.
\]
A class is regular if and only if \(c=d\). In particular there are \(n(\binom n2+1)\) regular classes. Since the monoid is finite, \(\mathcal D=\mathcal J\) also holds.

## Assumptions and scope

The result concerns every positive integer \(n\) and every set \(X\) of that size. There are no field, associativity, commutativity, or idempotence assumptions on the binary operations themselves. In the Green preorder convention used here, \(h\le_{\mathcal J}f\) means \(h\in\mathcal M(X)f\mathcal M(X)\). The number \(d\) counts fixed points of the involution **in the full image**, while \(c\) counts fixed points arising specifically from the diagonal input; confusing them loses the nonregular classes. When \(n=1\), the monoid consists of its identity and the formula gives \(J(1)=1\).

## Proof

**1. Equivariant representation.** The maps \(T_f\) commute with \(\iota\), and every transformation \(T:X^2\to X^2\) commuting with \(\iota\) has the form \(T_f\), taking \(f(x,y)\) as the first coordinate of \(T(x,y)\). Moreover \(T_{f\triangleleft g}=T_g\circ T_f\). Thus the magma monoid is exactly the endomorphism monoid of the finite involutive set \((X^2,\iota)\). This involutive set has \(n\) fixed points and \(N=\binom n2\) free two-point orbits.

**2. Necessary inequalities.** Let \(H=U\circ T_f\circ V\), where \(U,V\) commute with \(\iota\). Such maps send fixed points to fixed points, and each free orbit to either a free orbit or a fixed point. Thus the number of fixed images originating in the fixed-point domain cannot exceed \(c(f)\); the number of free image orbits cannot exceed \(a(f)\); and the total number of image orbits cannot exceed \(d(f)+a(f)\). This proves the three inequalities for \(H\).

**3. Sufficiency: orbit-resource factorization.** Write \(C',D',A'\) for the fixed-image-from-fixed set, the entire fixed image, and the free image-orbit set of \(T_h\); their respective cardinalities are \(c',d',a'\). Let the corresponding sets for \(T_f\) have sizes \(c,d,a\). Assume \(c'\le c\), \(a'\le a\), and \(d'+a'\le d+a\). Choose distinct intermediate image orbits of \(T_f\), one for each image orbit of \(T_h\), as follows:

* Assign the \(c'\) elements of \(C'\) injectively to the \(c\) fixed points in \(T_f(\Delta)\).
* Assign the \(a'\) free image orbits of \(T_h\) injectively to the \(a\) free image orbits of \(T_f\).
* Assign the remaining \(d'-c'\) fixed image points of \(T_h\) injectively to distinct unused image orbits of \(T_f\), either fixed or free. There are \((d+a)-(c'+a')\ge d'-c'\) available.

Define \(U\) on each chosen intermediate orbit to hit its assigned target orbit, equivariantly; a free orbit may be collapsed to a fixed point. Extend \(U\) to the rest of \(X^2\) by mapping unused orbits to any fixed point (one exists as \(n\ge1\)). For each input orbit of \(T_h\), choose \(V\) so that \(T_f\circ V\) reaches the selected intermediate image orbit. This is possible for a free input orbit because every image orbit of \(T_f\) has a preimage orbit, necessarily free when the image orbit is free. For a fixed input, the assigned intermediate point lies in \(T_f(\Delta)\), so a fixed-point preimage exists. The freely chosen signs on two-point orbits ensure the required orientations. The selections yield \(U\circ T_f\circ V=T_h\). Thus the inequalities are sufficient.

**4. Classes and enumeration.** Mutual domination forces equality of \(c\), \(a\), and \(d+a\), hence equality of \((c,d,a)\). Conversely equal triples give mutual domination by Step 3. A triple can occur only if \(1\le c\le d\le n\), \(0\le a\le N\), and the \(N\) free input orbits can cover the \(d-c\) fixed outputs absent from the diagonal image together with the \(a\) free image orbits: \(d-c+a\le N\). These conditions are also sufficient by assigning the \(n\) fixed inputs surjectively to \(c\) fixed outputs and assigning distinct free inputs to the \(d-c+a\) remaining required image orbits. Hence, with \(k=d-c\),
\[
 J(n)=\sum_{k=0}^{n-1}(n-k)(N-k+1)
 =\frac{n(n+1)(3n^2-5n+8)}{12}.
\]
Here \(N\ge n-1\) for \(n\ge1\), including equality at \(n=1,2\).

**5. Regularity.** An equivariant map \(T_f\) is regular precisely when its image admits an equivariant section through \(T_f\). For every fixed image point such a section requires a fixed-point preimage, so regularity implies \(d=c\). Conversely, when \(d=c\), select fixed preimages of all fixed image points and one free preimage orbit of each free image orbit, extending these choices equivariantly. Extend the resulting partial section arbitrarily to \(X^2\) using a fixed target point. This gives an inner inverse. Since each allowed \((c,a)\) with \(d=c\) occurs, there are \(n(N+1)\) regular classes. Standard finiteness of the monoid gives \(\mathcal D=\mathcal J\).

## Verification

A standalone, dependency-free Python program at `artifacts/verify.py` implements the equivariant-map coordinates directly. It exhaustively evaluates all two-sided products and compares the exact inequalities for \(n=1,2\). It also enumerates all \(19{,}683\) maps at \(n=3\), confirms exactly \(20\) distinct rank triples, constructs \(109{,}902\) explicit factorizations between one representative of each triple and every dominated target at \(n=3\), and tests thousands of seeded randomly sampled comparable pairs for \(n=3,4,5\). Run `python artifacts/verify.py` from this document's directory; the expected final output is `VERIFY_OK`. Finite computation is **not** the proof of the infinite-parameter theorem; Steps 1–5 are.

The class numbers from the formula are \(J(1)=1\), \(J(2)=5\), \(J(3)=20\), and \(J(4)=60\). The nonregular classes are those with \(d>c\), where a fixed image point is hit only from a two-point orbit. The two-sided order is not determined by ordinary image cardinality alone.

## Relationship to prior work

Baiduk and Kozerenko (2026, initially public 15 July 2026) identify the pairmorph embedding and characterize principal **left** and **right** ideals and their Green classes, as well as idempotents and regularity. Their Theorem 3 supplies the equivariant representation used here; Theorem 4 treats left ideals and Theorem 11 treats right ideals. The present statement instead gives the full **two-sided** preorder in three numerical invariants, explicitly describes its class poset, and counts all principal two-sided ideals by a polynomial. The left/right characterizations offer ingredients, but the necessary-and-sufficient two-sided factorization and its rank-triple enumeration require an additional orbit-allocation argument.

López-Permouth (2026) characterizes idempotents and enumerates them, not the Green \(\mathcal J\)-poset. Castillo-Ramirez and Ruiz-Medina (2023) investigate relative generating rank for endomorphism monoids of finite group-sets. That more general setting includes this involutive set but the studied invariant is different. The earlier 2022 magma-monoid paper develops units, submonoids, and ideals, but only its publicly accessible abstract and later detailed descriptions were checked; potential uninspected stronger coverage remains a priority risk.

## Limitations

The theorem treats the finite magma monoid, not arbitrary infinite underlying sets or the arity-\(s\) generalizations. It counts **principal two-sided ideals / Green classes**, not all ideals (downward-closed unions), not their cardinalities, and not minimal generating sets. Literature comparison is bounded and cannot establish global priority; the full 2022 predecessor was not available for direct inspection. Independent mathematical validation has not been performed.

## References

1. Y. Baiduk and S. Kozerenko, *Transformation semigroup perspective on the magma monoid*, arXiv:2607.13746v1 (15 July 2026); *Semigroup Forum* **113** (2026), 335–356, doi:10.1007/s00233-026-10659-x. https://arxiv.org/html/2607.13746
2. S. R. López-Permouth, *Idempotent elements in binary and s-ary magma monoids*, *São Paulo Journal of Mathematical Sciences* **20** (2026), article 14, doi:10.1007/s40863-025-00519-x. https://link.springer.com/article/10.1007/s40863-025-00519-x
3. A. Castillo-Ramirez and R. H. Ruiz-Medina, *The relative rank of the endomorphism monoid of a finite G-set*, arXiv:2203.12158v3 (2023). https://arxiv.org/html/2203.12158v3
4. S. R. López-Permouth, I. Owusu-Mensah and A. Rafieipour, *A monoid structure on the set of all binary operations over a fixed set*, *Semigroup Forum* **104** (2022), 667–688, doi:10.1007/s00233-022-10280-8.
