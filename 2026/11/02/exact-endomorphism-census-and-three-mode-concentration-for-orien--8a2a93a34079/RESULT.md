# Exact endomorphism census and three-mode concentration for oriented-star Hecke–Kiselman monoids

## Finding
For each integer \(m\ge 1\), let \(S_m\) be the oriented star with vertices \(c,u_1,\ldots,u_m\) and precisely the arrows \(c\to u_i\). Let \(H_m=\operatorname{HK}(S_m)\) denote its Hecke–Kiselman monoid, and count identity-preserving monoid endomorphisms. Put
\[
 K_{m,a}=2^a+2^{m-a}-1\qquad(0\le a\le m).
\]
Then the exact number of endomorphisms is
\[
 \boxed{E_m=|\operatorname{End}(H_m)|=
 \sum_{a=0}^m\binom ma\left[2^m K_{m,a}^{m}+
 (K_{m,a}+2^{m-a})^{m}\right].}
\]
The first five values are \(15,339,22233,4780047,4058199945\). In addition,
\[
 \boxed{E_m=3\cdot 2^{m(m+1)}\left(1+O(m2^{-m})\right)}
 \quad\text{as }m\to\infty.
\]
There are three disjoint, explicitly defined families of endomorphisms, each of cardinality exactly \(2^{m(m+1)}\), whose union has asymptotic density one. Consequently, a uniformly selected endomorphism lies in each family with limiting probability \(1/3\).

## Assumptions and scope
The integer \(m\) is arbitrary and positive. The source and target are the **same** monoid \(H_m\) defined by the finite presentation
\[
 c^2=c,\qquad u_i^2=u_i,\qquad u_i u_j=u_j u_i,
 \qquad c u_i c=u_i c u_i=c u_i
 \quad(1\le i,j\le m).
\]
The vertices and generators are labeled, and endomorphisms preserve the identity. For \(U\subseteq[m]\), let \(u_U\) be the product of the commuting leaf generators indexed by \(U\), with \(u_\varnothing=1\). Every idempotent is uniquely represented by exactly one of \(u_U\) or \(c u_U\). The latter notation uses the outgoing-star orientation, not an undirected star or a complete acyclic tournament.

For an endomorphism \(f\), write \(b_i=1\) if the unique idempotent \(f(u_i)\) contains the generator \(c\), and \(b_i=0\) otherwise. Write \(b_0\) similarly for \(f(c)\). The three distinguished families are
\[
 \mathcal F_1:\ b_1=\cdots=b_m=0,\ b_0=0;\qquad
 \mathcal F_2:\ b_1=\cdots=b_m=0,\ b_0=1;\qquad
 \mathcal F_3:\ b_1=\cdots=b_m=1,\ b_0=1.
\]
Each family contains exactly \(2^{m(m+1)}\) endomorphisms. The analogous inward-star count is the same by passage to opposite monoids, but the theorem's explicit family definitions refer to the outward orientation.

## Proof
**1. Canonical words and idempotents.** By the defining relations, all leaves commute and are idempotent. Repeated occurrences of \(c\) can be eliminated using \(c u_U c=c u_U\); occurrences of a leaf on both sides of the remaining \(c\) can be eliminated on the left using \(u_i c u_i=c u_i\). Hence every element is represented by either \(u_U\) or
\[
 u_P c u_Q\qquad(P,Q\subseteq[m],\ P\cap Q=\varnothing).
\]
These are distinct normal forms: each has no cancellable repetition, and the normal-form theorem for Hecke–Kiselman monoids says that equivalent normal forms differ only by swaps of disconnected generators. The only disconnected pairs here are pairs of leaves, whose swaps cannot change \(P\) or \(Q\) across \(c\). Thus these representations are unique. In particular \(|H_m|=2^m+3^m\). Direct use of the defining relations gives
\[
 (u_P c u_Q)^2=c u_{P\cup Q}.
\]
For disjoint \(P,Q\), this equals \(u_P c u_Q\) precisely when \(P=\varnothing\), by uniqueness of normal forms. Accordingly all the idempotents are \(u_U\) and \(c u_U\), one of each type for every \(U\subseteq[m]\).

**2. Relations among idempotents.** Label an idempotent by its center bit \(b\in\{0,1\}\) and leaf subset \(U\subseteq[m]\): \(e(0,U)=u_U\) and \(e(1,U)=c u_U\). For arbitrary idempotents \(x=e(b,U)\) and \(y=e(d,V)\), direct multiplication shows:

- If \(b=d\), the elements commute and their product is an idempotent.
- If \(b=1,d=0\), the ordered product \(xy\) is always an idempotent; moreover the directed Hecke–Kiselman relations \(xyx=yxy=xy\) hold.
- If \(b=0,d=1\), the ordered product \(xy\) is idempotent, and satisfies \(xyx=yxy=xy\), **if and only if** \(U\subseteq V\).
- If \(b\ne d\), then \(xy=yx\) **if and only if** the leaf subset on the center-free factor is contained in that on the center-containing factor.

For example, when \(b=0,d=1\), the normal form of \(xy=u_U c u_V\) is \(u_{U\setminus V}c u_V\), which is idempotent exactly when \(U\setminus V=\varnothing\). The other cases follow from the same normal forms and \(c u_W c=c u_W\). Thus these are necessary **and sufficient** tests for the defining relations under any map of the generators to idempotents.

**3. Independent leaf-coordinate count.** For \(f\in\operatorname{End}(H_m)\), let \(I\subseteq[m]\) be the indices \(i\) for which \(f(u_i)\) contains \(c\), and set \(a=|I|\), \(t=m-a\). There are \(\binom ma\) choices of \(I\). The source leaf generators commute. Consequently, for each target leaf coordinate \(j\), the membership bits in the \(a\) images with center bit one and the \(t\) images with center bit zero must have this property: either **all** \(t\) zero-center bits at coordinate \(j\) vanish, with the \(a\) other bits arbitrary, or at least one zero-center bit is one, in which case **all** \(a\) one-center bits must equal one. There are precisely
\[
 2^a+(2^t-1)=K_{m,a}
\]
choices, also valid when \(a=0\) or \(t=0\). Since the target leaf coordinates are independent, the images of the \(m\) source leaves have exactly \(K_{m,a}^m\) possibilities for this fixed \(I\).

**4. Incorporating the center image.** If \(f(c)\) contains target \(c\), each of its \(m\) leaf-membership bits is completely unrestricted: the \(m\) arrows \(c\to u_i\) impose no additional condition. This gives \(2^mK_{m,a}^m\) endomorphisms for the fixed \(I\) in this case.

If \(f(c)\) does not contain target \(c\), the arrow condition requires its leaf set to be contained in the leaf set of each \(f(u_i)\) with \(i\in I\). At one target-leaf coordinate there are \(K_{m,a}\) choices if the center-image bit is zero. If that bit is one, all \(a\) bits in the one-center leaf images must be one, and the remaining \(t\) bits are arbitrary: \(2^t\) possibilities. Hence the second case gives \((K_{m,a}+2^t)^m\) possibilities. Adding the two cases and then summing over \(I\) proves the displayed exact formula.

**5. Three dominant families.** The contributions \((a,b_0)=(0,0),(0,1),(m,1)\) are each exactly \(2^{m(m+1)}\): in each case, the relevant leaf-membership bits of all \(m+1\) generator images are free. The three families are disjoint because \(m\ge1\).

Put \(B_m=2^{m(m+1)}\). The one remaining endpoint contribution \((a,b_0)=(m,0)\) divided by \(B_m\) is
\[
 \left(\frac{2^m+1}{2^{m+1}}\right)^m=O(2^{-m}).
\]
For interior indices \(1\le a\le m-1\), the two per-coordinate factors, normalized by \(2^{m+1}\), satisfy
\[
 \frac{2K_{m,a}}{2^{m+1}}=2^{-a}+2^{-(m-a)}-2^{-m},
 \qquad
 \frac{K_{m,a}+2^{m-a}}{2^{m+1}}
 =2^{-a}+2^{-(m-a)-1}-2^{-m-1}.
\]
The second is bounded by the first. Write \(j=\min(a,m-a)\). If \(j\le m/4\), the first factor is at most \(2^{-j}(1+2^{-m/2})\), and summing the binomial weights over both tails gives at most a constant multiple of
\[
 \sum_{j\ge1}\binom mj2^{-jm}
 =(1+2^{-m})^m-1=O(m2^{-m}).
\]
If \(j>m/4\), the factor is at most \(2^{1-m/4}\). Even after summing all at most \(2^m\) binomial weights, the resulting normalized contribution is at most \(O(2^{2m-m^2/4})\), which is \(o(m2^{-m})\). Consequently the sum of all non-distinguished contributions is \(O(B_m m2^{-m})\). This proves the asymptotic formula and the limiting proportions \(1/3\).

## Verification
The standalone Python 3 program `verify.py` uses no third-party dependencies. It constructs all normal forms, implements their multiplication, verifies closure and associativity, independently tests the defining relations for **every** possible choice of idempotent generator images at \(m=1,2,3\), and checks the exact formula and the finer \((a,b_0)\) counts. Its output includes

```
m= 1 monoid_size= 5 endomorphisms= 15 independent_strata=OK
m= 2 monoid_size= 13 endomorphisms= 339 independent_strata=OK
m= 3 monoid_size= 35 endomorphisms= 22233 independent_strata=OK
VERIFY_OK
```

It also independently evaluates the closed formula at \(m=4,5\), giving \(4780047\) and \(4058199945\), and prints convergence checks for \(m=10,20,30\). These finite tests are not used as a proof for unbounded \(m\); the combinatorial argument above supplies that proof.

## Relationship to prior work
The presentation and normal-form confluence principle follow Aragona and D'Andrea (2019/2020). Andrenšek (first posted April 16, 2026) proves a general Boolean-matrix description of homomorphisms of Hecke–Kiselman monoids on arbitrary finite simple oriented graphs, including this star. That general theorem *implicitly determines* every fixed star count by admissibility testing. The new contribution claimed here is the **uniform closed binomial-sum evaluation**, the **exact sizes of the three dominant subclasses**, and the **large-star concentration theorem**; the general existence/parametrization theorem itself is not new. Andrenšek's earlier complete-Kiselman endomorphism classification concerns complete acyclic orientations, which are different from stars with at least two leaves. Wiertel's 2024 semigroup-identity classification concerns a different invariant. The case \(m=1\) overlaps the two-generator Kiselman monoid and is included as a boundary check, not as an independent novelty claim.

## Limitations
The enumerated objects are labeled, identity-preserving endomorphisms; the count is not a count of conjugacy orbits, endomorphism images, idempotent endomorphisms, or arbitrary set maps. A general Boolean parametrization already determines the finite admissible set at each \(m\); the point of the new result is a closed uniform evaluation and asymptotic structure, not a claim that endomorphisms were previously unclassifiable. The asymptotic statement concerns growing numbers of leaves for the same star family. No result here addresses arbitrary orientations of general trees. Historical priority of the exact star enumeration cannot be guaranteed against unindexed terminology.

## References
1. Luka Andrenšek, *Homomorphisms of Hecke–Kiselman Monoids Associated to Simple Oriented Graphs*, arXiv:2604.15497, first posted April 16, 2026, updated version 3; in particular Definition 3.1, Theorems 4.5 and 5.4. https://arxiv.org/html/2604.15497v3
2. Riccardo Aragona and Alessandro D'Andrea, *Normal form in Hecke–Kiselman monoids associated with simple oriented graphs*, arXiv:1904.10745 (2019); Algebra and Discrete Mathematics 30 (2020), 161–171; especially Theorem 3.1. https://arxiv.org/html/1904.10745v1
3. Luka Andrenšek, *A complete classification of endomorphisms of Kiselman's semigroup*, Semigroup Forum 112 (2026), 706–715, published online September 17, 2025. https://doi.org/10.1007/s00233-025-10577-4
4. Magdalena Wiertel, *Identities of Hecke–Kiselman monoids*, Semigroup Forum 109 (2024), 457–466. https://doi.org/10.1007/s00233-024-10451-9
