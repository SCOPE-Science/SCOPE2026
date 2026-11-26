# Exactly 32 complete mappings of the nine-element Brandt semigroup over \(C_2\)

## Finding

The nine-element Brandt semigroup \(B_2(C_2)\) has exactly **32 complete mappings** as permutations of its labeled elements. A complete mapping is a bijection \(\alpha\) for which \(\theta(x)=x\alpha(x)\) is also a bijection. The count includes the zero element, which every complete mapping fixes; it is not a count up to automorphisms.

## Assumptions and scope

For an index set \(I\) of size \(n\), the elements of \(B_n(C_2)\) are a zero and the triples \((i,g,j)\) with \(i,j\in I\), \(g\in C_2\). A product involving zero is zero; otherwise
\[
(i,g,j)(k,h,\ell)=\begin{cases}(i,g+h,\ell)&j=k,\\0&j\ne k.\end{cases}
\]
Group-coordinate sums are in \(C_2\). The enumeration concerns only \(n=2\).

## Proof of the count

Since \(\theta(0)=0\), its injectivity forces every nonzero input to have a nonzero product. Thus \(\alpha(i,g,j)=(j,h,k)\) for some \(h,k\), and \(\alpha(0)=0\) by bijectivity. For each fixed \(j\), the map \((i,g)\mapsto(h,k)\) is a permutation of the four local pairs. For each fixed \(i\), the map \((g,j)\mapsto(g+h,k)\) has the same permutation property. These two conditions are also sufficient.

Identify \(I=C_2\). Fix \(i,j\). The two choices of \(g\) must lead to different right indices \(k\): otherwise injectivity of \(\alpha\) makes their \(h\) bits distinct, which makes their \(g+h\) bits equal and violates injectivity of \(\theta\). There is consequently a bit \(s_{ij}\) with \(k=g+s_{ij}\). Fix \(j,k\). Each \(i\) has a unique input bit reaching \(k\), and the two corresponding \(h\)'s must differ. Thus \(h=i+f_{jk}\) for some bit \(f_{jk}\). Conversely these formulas always give a bijection \(\alpha\) fixing zero.

At fixed \(i,k\), the two product bits, one from each \(j\), must differ. They are \(k+s_{ij}+i+f_{jk}\), so the remaining conditions are
\[
s_{i0}+s_{i1}+f_{0k}+f_{1k}=1\qquad(i,k\in C_2).
\]
They hold exactly when there is a common bit \(d\) with \(s_{i1}=s_{i0}+d\) for both \(i\), and \(f_{1k}=f_{0k}+1+d\) for both \(k\). The five bits \(s_{00},s_{10},f_{00},f_{01},d\) are free, and each resulting permutation determines them uniquely. This gives \(2^5=32\).

## Known existence criterion and an explicit specialization

The all-index existence criterion, \(B_n(C_2)\) has a complete mapping if and only if \(n\) is even, follows from Theorem 10.1 of Araújo et al. [1]. Indeed, the nonzero \(\mathcal J\)-class has \(n\) \(\mathcal L\)-classes and maximal subgroup \(C_2\), which has no complete mapping. The case of even \(n\) is constructive already in Theorem 7.5 and Corollary 7.6 of [1].

For clarity, one direct specialization is as follows. Write \(n=2t\), \(I=C_2\times\mathbb Z/t\mathbb Z\), \(i=(a,u)\), \(j=(b,v)\). The routing in Theorem 7.5 sends \((i,j)\) to \((j,(a+b+1,u+v))\). This is a bijection, and keeping \(i\) instead of \(j\) in the first coordinate also gives a bijection, so the routing is admissible for the identity sandwich. Choose the involution that flips the bit in the right index and omitted row \(a+b\) in the local group table. The routing pairs \((i,(b,v))\) with \((i,(b+1,v))\), whose omitted-row bits differ as required. As the local group is \(C_2\), the nonomitted input uses output bit 1 and right index \((a+b+1,u+v)\), while the omitted input uses output bit 0 and right index \((a+b,u+v)\). The resulting specialization is
\[
\alpha(0)=0,\qquad \alpha((a,u),g,(b,v))=((b,v),a+b+g,(g,u+v)).
\]
The sums \(u+v\) are modulo \(t\). From the nonzero output of \(\alpha\) one recovers \(j,g,u,a\) in that order. Its associated product is \(((a,u),a+b,(g,u+v))\), from which one recovers \(i,b,g,v\) in that order. This verifies the specialization, including \(t=1\); it is not asserted as a new construction.

## Verification

Running `python3 verify.py` from the source package enumerates admissible local blocks and, separately, the \(8!\) permutations of the nonzero elements. The count is 32, with 16 first blocks and two followers for each. The same script checks the explicit specialization at \(n=2,4,6,8,10\). The finite checks corroborate the five-bit classification and do not establish a general counting formula.

## Relationship to prior work and limitations

Proposition 6.5 of [1] counts complete mappings of the **combinatorial** Brandt semigroup by Latin squares. Its value 2 at \(n=2\) concerns the five-element semigroup with trivial maximal subgroup, not the nine-element semigroup over \(C_2\). The even-index construction in Theorem 7.5 provides witnesses, not an enumeration of the nine-element semigroup. For example, the five-bit classification above includes maps with \(h=i+j\) independently of \(g\); by contrast, the direct construction on the even column side in Theorem 7.5 uses both values of \(h\) at every \((i,j)\). The count 32 is the sole contribution claimed here. It addresses the first admissible Brandt index over the smallest nontrivial maximal subgroup, at the boundary where the group itself has no complete mapping. No count for larger indices or claim of absolute bibliographic priority is made.

[1] J. Araújo, W. Bentz, P. J. Cameron, K. Hendrey, M. Kinyon, *Complete Mappings of Semigroups*, arXiv:2608.25092v1. https://arxiv.org/abs/2608.25092
