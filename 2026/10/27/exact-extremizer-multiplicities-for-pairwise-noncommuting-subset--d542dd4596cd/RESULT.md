# Exact extremizer multiplicities for pairwise noncommuting subsets of four-dimensional unitriangular groups

## Finding

Let \(q\) be any prime power, and let \(G=UT_4(\mathbb F_q)\), the group of upper unitriangular four-by-four matrices. A *noncommuting set* is a subset \(X\subseteq G\) in which every two **distinct** elements fail to commute. Write \(\mathcal M_q\) for the number of noncommuting sets of maximum possible cardinality (with subsets regarded as unlabelled, and no conjugacy quotient).

Define the nondegenerate alternating form on \(V=\mathbb F_q^4\), written in coordinates \(v=(a,b,e,f)\), by
\[
\omega(v,w)=aE+bF-Ae-Bf,\qquad w=(A,B,E,F).
\]
Let \(L\subseteq\mathbb P(V)\) be the projective line \(a=f=0\). A *partial ovoid* of the symplectic generalized quadrangle \(W(3,q)\) means a set of projective points such that distinct points are not orthogonal under \(\omega\). Define \(\beta_q\) as the largest size of such a set avoiding \(L\), and \(h_q\) as the number of such maximum-size sets, both finite and nonzero. Then
\[
\alpha_q=q^3-q+1+\beta_q,
\qquad
\mathcal M_q=h_q\,[q(q-1)]^{\beta_q}\,[(q-1)q^2]^{q(q^2-1)}\,(q-1)q^3.
\]
Here \(\alpha_q\) is the maximum possible noncommuting-set size. In particular, the natural bijection of extremizers described below holds for every prime power and not only for odd primes.

In the ternary case, an exhaustive enumeration of the forty projective points gives \(\beta_3=7\), with exactly \(2880\) seven-point partial ovoids in the whole symplectic quadrangle and exactly \(864\) of them avoiding \(L\). Consequently
\[
\boxed{\alpha_3=32,\qquad\mathcal M_3=2^{37}3^{61}.}
\]
The size-seven partial-ovoid enumeration for the full quadrangle is established earlier in the geometric literature; its use here is not a novelty claim.

## Assumptions and scope

Let \(g=(a,b,c,d,e,f)\) abbreviate the matrix having coordinates \(a\) in position \((1,2)\), \(b\) in \((1,3)\), \(c\) in \((1,4)\), \(d\) in \((2,3)\), \(e\) in \((2,4)\), and \(f\) in \((3,4)\). The field is arbitrary finite \(\mathbb F_q\), including characteristic two. The graph convention is that noncommuting pairs form edges, so maximum noncommuting sets are maximum cliques of that graph, equivalently independent sets of the commuting graph. No restriction to conjugacy classes or central cosets is imposed.

The parameters \(\beta_q,h_q\) are ordinary exact finite-geometry invariants. The general counting formula does not purport to evaluate these quantities for every \(q\); the fully numerical conclusion is for \(q=3\). The theorem classifies *all* extremizers in terms of them.

## Proof

**1. Commutation equations.** Direct multiplication gives the exact equivalence for \(g=(a,b,c,d,e,f)\) and \(g'=(A,B,C,D,E,F)\):
\[
gg'=g'g\iff aD=dA,\quad dF=fD,\quad aE+bF=Ae+Bf.
\]
Neither central coordinate \(c,C\) occurs.

**2. The stratum \(d\ne0\).** Assign to its elements the direction \((r,s)=(a/d,f/d)\). When \((r,s)\ne(0,0)\), also assign
\[
t=r(e/d)-s(b/d)\in\mathbb F_q.
\]
The commutation equations prove that two such elements commute **if and only if** their labels \((r,s,t)\) coincide. Each resulting fiber has size \((q-1)q^2\): choose \(d\ne0\), one free normalized coordinate of \((b,e)\), and \(c\). The exceptional direction \((r,s)=(0,0)\) gives one commuting fiber containing \((q-1)q^3\) elements. Distinct fibers contain **no commuting cross-pairs**. There are exactly
\[
q(q^2-1)+1=q^3-q+1
\]
fibers. Thus a noncommuting subset of this stratum has at most one point in each fiber; all such independent choices are compatible with one another.

**3. The stratum \(d=0\).** If \((a,f)\ne(0,0)\), the commutation test reduces to \(\omega((a,b,e,f),(A,B,E,F))=0\). The nonzero four-vectors here represent the projective points outside the isotropic line \(L\), with \(q(q-1)\) elements of \(G\) over each such projective point: \(q-1\) scalar representatives and \(q\) values of \(c\). Distinct elements over the same projective point commute. Hence noncommuting subsets of this stratum correspond exactly to partial ovoids avoiding \(L\), together with one independent choice of lift per point. Every element here fails to commute with **every** element of the \(d\ne0\) stratum: the first two commutation equations would require its \((a,f)\) pair to vanish. This proves attainability of size \(q^3-q+1+\beta_q\).

**4. Excluding the residual stratum.** Elements with \(d=a=f=0\) commute pairwise, so a noncommuting set includes at most one. If that element has \(b=e=0\), it is central and cannot occur in any set with at least two elements. Otherwise, among the \(d\ne0\) fibers it commutes with precisely those whose direction obeys \(re-sb=0\). These consist of the exceptional zero-direction fiber plus \(q(q-1)\) nonzero-direction fibers, hence leave at most \(q^3-q^2\) eligible fibers. Even allowing \(\beta_q\) elements with \(d=0\) and \((a,f)\ne(0,0)\), the total is at most \(q^3-q^2+\beta_q+1\), strictly smaller than \(q^3-q+1+\beta_q\), since \(q^2-q>0\). Thus no maximum set meets the residual stratum.

**5. All equality cases and their count.** Since the bounds for the two compatible principal strata add, attaining the global maximum requires exactly one choice from each of the \(q^3-q+1\) commuting fibers and exactly one lift of each point of a maximum partial ovoid avoiding \(L\). These choices have no cross-restrictions, are uniquely recoverable from the resulting subset, and produce the displayed factorization for \(\mathcal M_q\).

**6. The ternary incidence count.** For \(q=3\), the complete list of projective points is obtained from the \(3^4-1\) nonzero vectors modulo the two nonzero scalar multiples, giving forty points. The script `verify.py` builds adjacency from \(\omega(v,w)\ne0\), enumerates **every** clique by adding indices in increasing order, finds \(2880\) seven-cliques and no eight-cliques, and confirms each projective point lies in \(504\) seven-cliques. The isotropic line \(L\) has four points, and no seven-clique meets that line in more than one point. Therefore precisely \(2880-4\cdot504=864\) seven-cliques avoid \(L\). This yields \(\beta_3=7\), \(h_3=864\), and
\[
\mathcal M_3=864\cdot6^7\cdot18^{24}\cdot54=2^{37}3^{61}.
\]

## Verification

Run `python3 verify.py` using only the Python standard library. The verifier computes all forty projective points, enumerates all cliques (including the empty one), checks the exact size distribution and absence of size-eight cliques, independently checks the intersection counts with the designated line, constructs a size-32 subset of \(UT_4(\mathbb F_3)\), checks all of its distinct pairs against the three matrix-commutation equations, and checks the integer factorization. The exhaustive clique recursion considers all larger-index candidates at every extension, so the finite conclusion is an exhaustive calculation, not an empirical sample. The unrestricted-field factorization is proved algebraically in the preceding paragraphs.

## Relationship to prior work

Kaur, Sharma and Singh [1] classified branching rules and enumerated commuting tuples for upper unitriangular groups; their section 6 supplies the \(UT_4\) context but not maximum-noncommuting-set counts. Majeed and Ramkumar [2, Theorem 6.4] already gave the decomposition of the **maximum cardinality** into a large-fiber contribution and an auxiliary induced graph; that cardinality reduction is **not claimed as new** here. The new quantity is the number of *all equality cases* and its canonical all-field factorization, using the extra symplectic reduction and an exact ternary evaluation. Lansdown [3, Chapter 4, Table 4.1] enumerated \(2880\) size-seven partial ovoids in \(W(3,3)\); that pre-existing geometric enumeration is also explicitly credited. The conversion to \(864\) avoiding a specified isotropic line and the exact group extremizer count are the parts assessed here.

## Limitations

The general formula leaves \(\beta_q\) and \(h_q\) as symplectic partial-ovoid parameters for arbitrary \(q\). Thus it is **not** an all-fields closed numerical evaluation, nor a classification of the finite-geometric orbits of all partial ovoids. Full external independent audit is not asserted. An unlocated general extremal-group-graph result may subsume the equality-case factorization; literature checks are documented in the accompanying review, not treated as an absolute uniqueness certificate.

## References

[1] D. Kaur, U. B. Sharma, A. Singh, *Branching rules and commuting probabilities for Triangular and Unitriangular matrices*, arXiv:2006.01493v1 (public June 2, 2020), Section 6. https://arxiv.org/abs/2006.01493

[2] M. Majeed, C. Ramkumar, *Commuting Graph of Unitriangular Group UT(4,p)*, arXiv:2608.09235v1 (2026), Theorems 5.6 and 6.4, Sections 5–6. https://arxiv.org/abs/2608.09235

[3] C. Lansdown, *Designs in finite geometry*, thesis, Chapter 4, Table 4.1 (the enumeration of maximum partial ovoids of \(W(3,3)\)). https://publications.rwth-aachen.de/record/808714/files/808714.pdf
