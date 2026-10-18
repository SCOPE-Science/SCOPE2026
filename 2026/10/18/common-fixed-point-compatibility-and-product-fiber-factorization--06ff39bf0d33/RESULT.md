# Common-fixed-point compatibility and product-fiber factorization for Catalan monoid idempotents

## Finding
For every integer \(n\ge1\), let \(C_n\) be the Catalan monoid of weakly increasing, order-decreasing transformations \(f:[n]\to[n]\): \(i\le j\implies f(i)\le f(j)\), and \(f(i)\le i\). Write products as ordinary composition, with the rightmost map applied first. Every idempotent of \(C_n\) has the unique form
\[
e_F(i)=\max\{j\in F:j\le i\},\qquad F\subseteq[n],\quad 1\in F.
\]
For ordered idempotent pairs \((e_F,e_G)\), put \(H=F\cap G\). They commute if and only if, in each open integer gap between consecutive elements of \(H\), as well as after its largest member, one of the two sets \(F\setminus G\) and \(G\setminus F\) is absent. When they commute, their product is exactly \(e_H\).

More precisely, let \(H=\{h_1=1<h_2<\cdots<h_k\}\), and put \(\ell_i=h_{i+1}-h_i-1\) for \(i<k\) and \(\ell_k=n-h_k\). The exact number of **ordered commuting idempotent pairs with prescribed product** \(e_H\) is
\[
\boxed{N_n(H)=\prod_{i=1}^{k}(2^{\ell_i+1}-1).}
\]
This is a product-fiber formula, which distinguishes idempotent products of identical rank: for \(n=4\), the fibers over \(e_{\{1,2\}}\) and \(e_{\{1,3\}}\) have sizes \(7\) and \(9\), respectively.

Let \(c_{n,k}\) count such commuting pairs for which their product has rank \(k\). Then
\[
\boxed{\sum_{n\ge1}\sum_{k=1}^{n}c_{n,k}y^kz^{n-1}
=\frac{y}{1-(3+y)z+2z^2},}
\]
and the exact coefficient formula is
\[
\boxed{c_{n,k}=[z^{n-k}](1-z)^{-k}(1-2z)^{-k}.}
\]
The total counts for \(n=1,2,\ldots,10\) are \(1,4,14,48,164,560,1912,6528,22288,76096\). These totals and the coefficient triangle occur in earlier numerical databases (OEIS A007070 and A206306); they are not claimed as new integer sequences.

## Assumptions and scope
The ground object is the finite ordered set \([n]=\{1,\ldots,n\}\), for every \(n\ge1\). All transformation maps are total, order-preserving and regressive. All pairs are ordered, each map is idempotent, and product rank means cardinality of the image of the composition. No field, characteristic, approximation, or asymptotic hypothesis is used. The specific product \(e_H\), rather than merely its rank, is fixed in the principal counting theorem.

## Proof
**1. Parametrization of idempotents.** If \(e\) is an idempotent in \(C_n\), its image equals its fixed-point set \(F\), which must contain \(1\) because every regressive transformation fixes \(1\). For \(i\in[n]\), the element \(e(i)\) is fixed and does not exceed \(i\). Conversely, if \(j\in F\) and \(j\le i\), monotonicity implies \(e(i)\ge e(j)=j\). Hence \(e(i)\) is the largest fixed point no greater than \(i\). Conversely, every \(e_F\) displayed above is manifestly monotone, regressive and idempotent. This establishes a bijection between idempotents and subsets \(F\ni1\).

**2. Commutation criterion.** Let \(H=F\cap G\). Its successive points partition \([n]\) into half-open integer blocks \([h_i,h_{i+1})\) and a last block \([h_k,n]\). Suppose a block contains both an \(F\)-exclusive point and a \(G\)-exclusive point. Among such points choose a later point \(x\) of one type having an earlier point of the opposite type in the same block. If \(x\in F\setminus G\), then \(e_G(e_F(x))=e_G(x)=u\), where \(u\in G\setminus F\) lies strictly above the block's left common endpoint (there is an earlier \(G\)-exclusive point). Consequently \(e_F(e_G(x))=e_F(u)<u\), and the maps fail to commute. The case \(x\in G\setminus F\) is symmetric.

Conversely, suppose each block contains exclusive fixed points of at most one type. Within a block whose left endpoint is \(h\in H\), either \(G\) has no fixed point other than \(h\), or \(F\) has none. The corresponding retraction sends every point of that block to \(h\), and the other retraction fixes \(h\). Hence both compositions send the entire block to \(h\). The composite on \([n]\) is therefore \(e_H\) in both orders. These two implications prove the criterion and the product formula.

**3. Fibers of the prescribed product.** Fix \(H\ni1\). Every point outside \(H\) carries exactly one of three statuses: absent from both \(F,G\), present only in \(F\), or present only in \(G\). For any gap of length \(\ell\), the allowed words either use only the first and second statuses, or use only the first and third. There are \(2^\ell+2^\ell-1=2^{\ell+1}-1\) such words, subtracting the doubly counted all-absent word. Status choices in separate gaps are independent, and together with forced membership in both sets at each point of \(H\) give a unique commuting pair with product \(e_H\). Multiplication over the \(k\) gaps proves the exact expression \(N_n(H)\).

**4. Rank refinement.** The admissible gap-word generating function is
\[
B(z)=\sum_{\ell\ge0}(2^{\ell+1}-1)z^\ell
=\frac{1}{(1-z)(1-2z)}.
\]
The compulsory initial common fixed point contributes \(y\). Each additional common fixed point contributes \(yz\) followed by an admissible gap, while one terminal gap follows the last common point. Accordingly,
\[
\sum_{n\ge1}\sum_{k=1}^{n}c_{n,k}y^kz^{n-1}
=y B(z)\sum_{j\ge0}(yzB(z))^j
=\frac{y}{(1-z)(1-2z)-yz}.
\]
Selecting exactly \(k-1\) additional common fixed points gives \(c_{n,k}=[z^{n-k}]B(z)^k\), as stated. All manipulations are formal power-series identities over the integers and are valid for every \(n\). The total \(a_n=\sum_kc_{n,k}\) obeys \(a_1=1\), \(a_2=4\), and \(a_n=4a_{n-1}-2a_{n-2}\) for \(n\ge3\).

## Verification
The standalone program `verify_catalan.py` independently generates all idempotent retractions from their fixed-point sets, composes them as ordinary maps, and calculates exact product fibers for every \(1\le n\le10\). Every computed fiber is compared with the Mersenne-gap product formula. The resulting rank counts are independently compared with the binomial-coefficient expression and the second-order recurrence. For \(1\le n\le8\), an additional direct enumeration of all order-preserving regressive transformations independently confirms that the retractions are exactly the idempotents. Execute `python3 verify_catalan.py`; a successful run ends with `VERIFY_OK`. Finite computations are checks, not the proof for arbitrary \(n\).

## Relationship to prior work
Ganyushkin and Mazorchuk (2010, arXiv:1006.0316) prove the known Catalan-monoid identification and the number of idempotents; the parametrization used here is not presented as a new idempotent census. Pantazi and Spircu study descriptions of these idempotents, commuting segment idempotents, and decomposition of dominated elements. Their established segment relations are relevant antecedents, but the inspected material does not supply the stated full fixed-product fiber theorem.

The entire **rank-refined coefficient array** already appears as OEIS A206306 (Riordan/Mersenne convolution triangle, recorded in 2012), and the unrefined totals are OEIS A007070. Neither numerical array nor its arithmetic recurrence is claimed as new. The assessed claim is the intrinsic Catalan-monoid commutation criterion and exact assignment of multiplicities to each *specified idempotent product*, which explains a natural semigroup realization of the known array. The earlier classification of commuting idempotents in the full transformation monoid concerns a different monoid and does not determine these restricted fibers.

## Limitations
No claim is made that the numerical sequences or Riordan array are novel. Exhaustive literature uniqueness is not established: older specialized semigroup literature might contain an equivalent compatibility criterion or product-fiber formula. The result concerns pairs of idempotents in the regressive Catalan monoid, not arbitrary elements, higher tuples, or conjugacy classes. The verification covers finite \(n\) only; the complete theorem follows from the combinatorial proof.

## References
1. O. Ganyushkin and V. Mazorchuk, *On Kiselman quotients of 0-Hecke monoids*, arXiv:1006.0316 (first public arXiv posting 2 June 2010), https://arxiv.org/abs/1006.0316 .
2. S. V. Pantazi and T. Spircu, *Relations between consecutive Catalan monoids* (manuscript dated 10 February 2016), https://www.researchgate.net/publication/330567006_Relations_between_consecutive_Catalan_monoids .
3. OEIS Foundation, A206306, *Riordan array (1, x/(1-3*x+2*x^2))*; https://oeis.org/A206306 .
4. OEIS Foundation, A007070, linear-recurrence sequence; https://oeis.org/A007070 .
