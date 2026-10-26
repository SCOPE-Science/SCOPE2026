# Product-rank renewal law for commuting monotone idempotents

## Finding

Let \(\mathcal O_n\) be the monoid of all nondecreasing self-maps of the chain \([n]=\{1,\ldots,n\}\), for \(n\ge1\). For each \(1\le k\le n\), let \(c_{n,k}\) count **ordered** pairs \((e,f)\in\mathcal O_n^2\) with \(e^2=e\), \(f^2=f\), \(ef=fe\), and \(|\operatorname{im}(ef)|=k\). Composition is ordinary composition; commutativity makes the choice of right-to-left convention immaterial.

Define the rational functions
\[
L(t)=\frac{1-t+t^2}{(1-t)(1-3t+t^2)},\qquad B(t)=tL(t)^2.
\]
Then the **complete product-rank series** is
\[
\boxed{\sum_{n\ge1}\sum_{k=1}^{n}c_{n,k}\,u^k t^n
 =\frac{uB(t)}{1-uB(t)}.}
\]
In particular, \(c_{n,k}=[t^{n-k}]L(t)^{2k}\). The total number \(c_n=\sum_k c_{n,k}\) has generating function
\[
\boxed{\sum_{n\ge1}c_nt^n=
\frac{t(1-t+t^2)^2}{1-9t+26t^2-37t^3+26t^4-9t^5+t^6}.}
\]
Its first nine values are \(1,7,40,213,1111,5768,29929,155315,806088\).

There is a unique \(r\in(0,(3-\sqrt5)/2)\) with \(B(r)=1\), and, writing \(K=1/(rB'(r))\),
\[
c_n\sim K r^{-n},\qquad
\mathbb E\bigl[|\operatorname{im}(ef)|\mid (e,f)\text{ uniform among commuting idempotent pairs}\bigr]=Kn+O(1).
\]
Numerically, \(r\approx0.192666756007696\) and \(K\approx0.294874985807659\). Since the number of individual idempotents in \(\mathcal O_n\) is the classical Fibonacci number \(F_{2n}\), with \(F_0=0,F_1=1\), the commuting probability among two independently uniform idempotents obeys
\[
\boxed{\frac{c_n}{F_{2n}^2}\sim 5K\left(\frac{r^{-1}}{((3+\sqrt5)/2)^2}\right)^n.}
\]
The exponential base is approximately \(0.7573\), strictly below one.

## Assumptions and scope

No restriction besides \(n\ge1\) is imposed. All maps are total and order preserving; they need not be order decreasing, contractions, injective, or arbitrary set maps. A retraction is an idempotent map. The rank variable \(k\) is the size of the image of the *common product*, not the rank of either factor. The two maps are ordered, so swapping them generally produces a distinct counted pair.

## Proof

**1. Retractions of one anchored interval.** Every nondecreasing idempotent map has image equal to its fixed-point set, and its fibers are intervals containing their unique fixed point. Let \(H_a\) count order-preserving idempotents of \([a+1]\) fixing its right endpoint. The analogous count fixing a left endpoint is the same by reflection. A fixed-point list below the anchored right endpoint has a possibly empty initial unfixed segment, followed by positive gaps of lengths \(d_1,\ldots,d_j\) between consecutive fixed points. For a gap of length \(d\), precisely \(d\) monotone cuts distribute the intermediate points between its two fixed endpoints. Consequently, as a formal power series,
\[
H(t)=\sum_{a\ge0}H_a t^a
=\frac{1}{1-t}\frac{1}{1-\sum_{d\ge1}d t^d}
=\frac{1-t}{1-3t+t^2}.
\]
This gives \(H_0=1,H_1=2,H_2=5,H_3=13\) and \(H_a=3H_{a-1}-H_{a-2}\) for \(a\ge2\).

**2. Common-product fibers.** If \(e,f\) are commuting idempotents, then \(h=ef=fe\) is an idempotent and
\[
\operatorname{im}(h)=\operatorname{Fix}(e)\cap\operatorname{Fix}(f),
\qquad he=eh=h,\quad hf=fh=h.
\]
Indeed, both maps fix the output of \(h\), and every point fixed by both is fixed by \(h\). Thus every fiber of \(h\) is a common invariant interval for \(e,f\), and it contains exactly one common fixed point, namely the unique fixed point \(u\) of \(h\) in that fiber. On this interval both compositions equal the constant map \(u\).

**3. Side-exclusion lemma (both directions).** On an interval with \(e(u)=f(u)=u\), the relation \(ef=fe\equiv u\) holds if and only if on each of the two sides of \(u\), at most one of \(e,f\) has any fixed point other than \(u\). For necessity, suppose \(e\) fixes \(p<u\) and \(f\) fixes \(q<u\). If \(p\le q\), then \(f(p)\le f(q)=q<u\), yet \((fe)(p)=f(p)=u\), a contradiction. If \(q<p\), the symmetric argument with \((ef)(q)\) gives a contradiction. Reflecting the interval proves the right-side assertion. For sufficiency, an idempotent with no fixed point to the left of \(u\) must map the whole left side to \(u\): its image consists of fixed points and monotonicity prevents crossing \(u\). The same applies to the right side. On each side one of the maps is therefore constant \(u\), while the other fixes \(u\); both composition orders map that side to \(u\).

**4. Local weights and renewal.** If a fiber of \(h\) contains \(a\) points left of its root \(u\) and \(b\) right, there are \(H_a\) possible single-map retractions of the left half and \(H_b\) of the right half. The side-exclusion condition leaves \(2H_a-1\) possibilities for the *ordered pair* on the left (either map may have extra fixed points, with the both-constant case counted once), and \(2H_b-1\) on the right. The two sides are independent because monotonicity across a common fixed root is automatic. Put
\[
L(t)=\sum_{a\ge0}(2H_a-1)t^a=2H(t)-\frac1{1-t}
=\frac{1-t+t^2}{(1-t)(1-3t+t^2)}.
\]
The generating function for one invariant fiber, including its one root, is \(B(t)=tL(t)^2\). Every idempotent monotone \(h\) has an ordered partition of \([n]\) into nonempty consecutive fibers, each marked by its root. Conversely any ordered list of such marked blocks, decorated by side-compatible restrictions of \(e,f\), produces a unique commuting pair, with common product \(h\). The number of blocks is precisely \(|\operatorname{im}(h)|\). Ordinary generating functions for nonempty sequences now give
\[
\sum_{n,k}c_{n,k}u^kt^n=\sum_{k\ge1}u^kB(t)^k=\frac{uB(t)}{1-uB(t)}.
\]
The advertised rational denominator follows by expansion at \(u=1\).

**5. Asymptotics.** The coefficients of \(B(t)\) are strictly positive in every positive degree; in particular those of degrees one and two are nonzero. The denominator of \(L(t)\) has its first positive singularity at \(R=(3-\sqrt5)/2\). On \((0,R)\), \(B(t)\) increases strictly from zero to infinity, so \(B(r)=1\) has a unique solution there. Positivity and the presence of two consecutive powers force \(|B(z)|<B(r)=1\) when \(|z|=r\) and \(z\ne r\). Thus \(r\) is the sole singularity of minimum modulus of \(B/(1-B)\), and it is a simple pole. Singularity extraction yields \(c_n\sim r^{-n}/(rB'(r))=Kr^{-n}\).

Differentiating the bivariate series in \(u\) at \(u=1\) gives \(B(t)/(1-B(t))^2\). Its double pole at \(r\), divided coefficientwise by the simple-pole asymptotic for \(c_n\), gives the expected product rank \(Kn+O(1)\). Finally the standard formula \(F_{2n}\sim\varphi^{2n}/\sqrt5\), \(\varphi=(1+\sqrt5)/2\), proves the probability asymptotic. The base is less than one by an exact inequality: \(B(1/6)=5766/9025<1\), so the strict increase of \(B\) gives \(r>1/6\) and thus \(r^{-1}<6<\varphi^4\). This rules out relying only on numerical approximations for the exponential decay.

## Verification

The included standalone script `check_commuting_monotone.py` constructs all nondecreasing maps, filters idempotents by direct composition, and tests each ordered pair by explicit composition. Independently it computes the proposed \(c_{n,k}\) via an integer recurrence for anchored retractions and a renewal convolution. All product-rank profiles match for \(1\le n\le9\), covering \(7,817,630\) candidate ordered idempotent pairs. Run `python3 check_commuting_monotone.py`. Finite checks corroborate, but do not replace, the all-\(n\) argument above.

## Relationship to prior work

The basic monoid, its individual idempotent enumeration, and the Fibonacci identity \(|E(\mathcal O_n)|=F_{2n}\) are established in earlier literature; they are not claimed here. Fernandes–Jesus–Maltcev–Mitchell (2009/2010) characterize endomorphisms of \(\mathcal O_n\) by, among other things, pairs satisfying the *strictly stronger* relation \(ef=fe=f\). Li–Fernandes (arXiv:2204.07838v1, 2022) extend such endomorphism classifications to monotone transformations and use comparable idempotent pairs, but their published formulas do not directly enumerate all commuting pairs by the rank of their common product. Araújo–Konieczny (2013) characterize centralizers in the unrestricted full transformation semigroup, not this order-restricted enumerator. Existing formulas for unrestricted commuting idempotent transformations also do not retain the order-preservation constraint. The present claim is the exact product-rank renewal series and its asymptotic consequences, not general commutativity criteria for arbitrary transformations.

## Limitations

The theorem applies to full order-preserving idempotent maps of finite **chains**, not to all posets or to partial maps. It does not determine simultaneous individual ranks of both factors, nor classify the generated submonoids. The rank expectation and density are asymptotic statements as chain length grows. A 2006 paper by Laradji–Umar concerning individual rank/fixed-point counts was located but its complete text was not available during the literature comparison; an unexpectedly equivalent two-map count in that work or other older semigroup literature remains a priority risk. The novelty comparison is limited to the inspected sources and searches, not a proof of historical uniqueness.

## References

- De Biao Li and Vítor H. Fernandes, *Endomorphisms of semigroups of monotone transformations*, arXiv:2204.07838v1 (16 April 2022), https://arxiv.org/abs/2204.07838 and https://arxiv.org/pdf/2204.07838.
- V. H. Fernandes, M. M. Jesus, V. Maltcev, and J. D. Mitchell, *Endomorphisms of the semigroup of order-preserving mappings*, Semigroup Forum 81 (2010), 277–285, https://doi.org/10.1007/s00233-010-9220-7; accessible preprint https://www.dm.fct.unl.pt/sites/www.dm.fct.unl.pt/files/preprints/2009/6_09.pdf.
- J. Araújo and J. Konieczny, *Centralizers in the full transformation semigroup*, Semigroup Forum 86 (2013), 1–31, https://doi.org/10.1007/s00233-012-9424-0; open text https://repositorioaberto.uab.pt/bitstream/10400.2/3795/1/2013Centralizers.pdf.
- A. Laradji and A. Umar, *Combinatorial results for semigroups of order-preserving full transformations*, Semigroup Forum 72 (2006), 51–62, https://doi.org/10.1007/s00233-005-0553-6 (bibliographic abstract inspected; full text not available).
