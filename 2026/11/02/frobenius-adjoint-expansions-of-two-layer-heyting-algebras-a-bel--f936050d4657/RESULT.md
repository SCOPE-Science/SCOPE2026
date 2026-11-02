# Frobenius-adjoint expansions of two-layer Heyting algebras: a Bell-product census

## Finding

Let \(a,b\ge1\) be integers and let \(P_{a,b}=L\sqcup U\) be the finite poset with \(|L|=a\), \(|U|=b\), every point in \(L\) below every point in \(U\), and no other strict comparabilities. On the Heyting algebra \(H_{a,b}=\operatorname{Up}(P_{a,b})\), let \(f,g:H_{a,b}\to H_{a,b}\) satisfy the five Frobenius-adjoint conditions stated below, with the residuated multiplication equal to meet.

**Classification.** Every such ordered pair belongs to exactly one of the following disjoint types.

1. The collapsed pair: \(f(x)=1\) exactly when \(x=1\), and \(g(x)=0\) exactly when \(x=0\), with \(f(x)=0\) and \(g(x)=1\) otherwise.
2. Independently choose set partitions \(\pi_U\) of \(U\) and \(\pi_L\) of \(L\). Let \(S_{\pi_U,\pi_L}\) consist of the upsets \(A\subseteq U\) for which \(A\) is a union of \(\pi_U\)-blocks and the upsets \(U\cup B\), where \(B\subseteq L\) is a union of \(\pi_L\)-blocks. Then \(f(x)\) is the largest member of \(S_{\pi_U,\pi_L}\) below \(x\), and \(g(x)\) is the least member above \(x\).

Writing \(B_k\) for the Bell number (the number of partitions of a labelled \(k\)-element set), the exact number of expansions of this fixed labelled algebra is
\[
\boxed{E(a,b)=1+B_aB_b.}
\]
The number of isomorphism classes, with the carrier automorphisms allowed to permute each of \(L\) and \(U\), is \(1+p(a)p(b)\), where \(p(k)\) is the integer partition number. Ordered by inclusion of their common fixed-point sets, the expansions form a new minimum adjoined to the product of the two set-partition refinement lattices.

## Assumptions and scope

The upset algebra contains \(2^a+2^b-1\) elements: its elements are precisely the subsets \(A\subseteq U\) and \(U\cup B\) for \(B\subseteq L\), identifying the repeated set \(U\). The bottom is \(0=\varnothing\), the top is \(1=L\cup U\), and the lattice operations are intersection and union. The implication \(x\to y\) is the largest upset \(z\) with \(x\cap z\subseteq y\).

The five required axioms, for every \(x,y\in H_{a,b}\), are
\[
\begin{aligned}
& f(x)\le x,\\
& g(x)\le y\iff x\le f(y),\\
& f(g(x)\to y)=g(x)\to f(y),\\
& f(g(x)\vee y)=g(x)\vee f(y),\\
& g(x\wedge g(y))=g(x)\wedge g(y).
\end{aligned}
\]
These are the FARL1–FARL5 conditions of Wang, Shi and Wang (2026), restricted to an idempotent, distributive, integral residuated lattice. All counts are for a fixed labelled poset with both layers nonempty. The result is not a count of all finite Frobenius-adjoint residuated lattices.

## Proof

**1. A common fixed-point image.** By the adjunction, \(x\le f(g(x))\) and \(g(f(x))\le x\). Since \(f\le\operatorname{id}\), the first inequality implies \(x\le g(x)\). Taking \(y=0\) in the join-Frobenius axiom gives \(f(g(x))=g(x)\), because \(f(0)=0\). For \(u=f(x)\), the adjunction gives \(g(u)\le x\). Therefore monotonicity of \(f\) and the preceding identity yield \(g(u)=f(g(u))\le f(x)=u\); combined with extensivity of \(g\), this gives \(g(f(x))=f(x)\). Thus \(f\) and \(g\) are respectively an idempotent interior and closure operator with the same image \(S\). The adjunction forces \(f(x)=\max\{s\in S:s\le x\}\) and \(g(x)=\min\{s\in S:x\le s\}\). The maps preserve meets and joins respectively, so \(S\) contains \(0,1\) and is a sublattice. For \(s,t\in S\), the residual Frobenius identity gives \(f(s\to t)=s\to t\); hence \(S\) is also closed under Heyting implication.

**2. The middle-cut dichotomy.** Put \(c=U\), the common top of the lower Boolean interval and bottom of the upper one. Suppose \(S\ne\{0,1\}\), and choose \(s\in S\setminus\{0,1\}\). If \(s\subseteq U\), then either \(s=c\), or \(s\) is a nonempty proper subset of \(U\). In the latter case, \(s\to0=U\setminus s\in S\); consequently \(c=s\vee(s\to0)\in S\). If instead \(s=U\cup B\) with \(\varnothing\ne B\subsetneq L\), set \(t=U\cup(L\setminus B)\). As \(s\vee t=1\), join-Frobenius and \(f(1)=1\) imply \(1=s\vee f(t)\). Since \(f(t)\le t\), covering every point of \(L\setminus B\) forces \(f(t)=t\); now \(c=s\wedge t\in S\). Therefore either \(S=\{0,1\}\) or \(c\in S\).

**3. Independent partitions.** Suppose \(c\in S\). The sets \(S_U=\{A\subseteq U:A\in S\}\) and \(S_L=\{B\subseteq L:U\cup B\in S\}\) are bounded sublattices of the respective powerset Boolean algebras. For \(A\in S_U\), the complement \(U\setminus A\) belongs to \(S\): for nonempty \(A\), it is \(A\to0\), and for \(A=0\), it equals \(c\). For \(B\in S_L\), its complement \(L\setminus B\) belongs to \(S_L\), since \((U\cup B)\to c=U\cup(L\setminus B)\). Thus both are Boolean subalgebras. A finite Boolean subalgebra of a labelled powerset is exactly the family of unions of blocks of a unique partition. This proves the necessity and uniqueness of \((\pi_U,\pi_L)\).

**4. Converse.** For any two partitions, let \(S\) be the displayed two-tier union of their block-Boolean subalgebras. On either Boolean interval the floor map is blockwise interior (union of blocks contained in its argument), and the ceiling map is blockwise saturation (union of blocks meeting its argument). These satisfy the adjunction and the Frobenius distributivity of floor over union with a fixed block union, and of ceiling over intersection with a fixed block union. Cross-tier joins and meets reduce to the higher and lower operand respectively, verifying the join and meet identities in every cross-tier case. For implication, an antecedent \(s\in S\) not above the cut acts in its own Boolean interval by union with its blockwise complement; for \(s\) above the cut and consequent below it, \(s\to y=y\); for an antecedent below the cut and consequent above it, \(s\to y=1\). Finally \(s\to y=1\) whenever \(s\le y\), and \(s\le f(y)\) in this case. These cases give \(f(s\to y)=s\to f(y)\), including endpoints. The collapsed image \(\{0,1\}\) yields the displayed unique pair, and direct substitution into the same identities verifies it.

**5. Enumeration and orbit types.** Partition choices in the two labelled layers are independent, giving \(B_aB_b\), with one extra collapsed image. Every order automorphism of the two-level poset preserves its two layers and acts by arbitrary permutations in each; its orbits on set partitions are classified by their block-size integer partitions, giving \(1+p(a)p(b)\). Under inclusion of images, refinement of either partition is exactly inclusion of its block-union Boolean algebra, while \(\{0,1\}\) lies below every other image.

## Verification

The accompanying `checker.py` independently enumerates every candidate image closed under lattice joins and meets, derives its exact floor and ceiling maps, and directly evaluates all five axioms. For \((a,b)=(1,1),(1,2),(2,1),(1,3),(3,1),(2,2),(2,3),(3,2),(3,3)\), it obtains respectively \(2,3,3,6,6,5,11,11,26\). A second enumerator searches all deflationary meet-preserving maps \(f\) (without assuming the common-image theorem), constructs their potential left adjoints, then directly checks the axioms for \((a,b)=(1,1),(1,2),(2,1),(2,2),(2,3)\). Both methods reproduce the theorem. These finite checks do not constitute the general proof.

## Relationship to prior work

Wang, Shi and Wang (2026), Definition 3.8, supply precisely the five axioms, and Proposition 3.13 gives general algebraic consequences of them. Their categorical and algebraization results apply to the larger class but do not enumerate expansions of this fixed two-tier Heyting reduct. Earlier work on Gödel chains treats the totally ordered case; even with one layer having more than one point, the present reduct generally is not a chain. Classical monadic-Heyting and finite-Esakia representation results motivate the Boolean partition comparison but do not by themselves give this sharp Frobenius-adjoint census. The classification is a concrete specialization, not a new general algebraic equivalence.

## Limitations

No statement is made for posets with incomplete cross-layer incidence, three or more layers, arbitrary non-idempotent residuated multiplication, or infinite carriers. The verification enumerates finite small instances only. An equivalent historical statement in the literature on monadic Heyting algebras, Boolean ordinal sums, or Esakia partition duality remains possible despite targeted source comparisons; absence from searches is not a proof of historical priority. Independent external validation has not been performed.

## References

Wang, Juntao; Shi, Jieqiong; Wang, Mei, *Frobenius–Galois expansions of substructural logics: Algebraization, Kalman equivalence and positive-cone semantics*, arXiv:2609.09529v1 (publicly submitted 8 September 2026), especially Definition 3.8 and Proposition 3.13, https://arxiv.org/html/2609.09529v1.

*Frobenius-adjoint and monadic expansions coincide on Gödel algebras*, public mathematical research record, 2026 (comparison: totally ordered reduct only).

Bezhanishvili, *Varieties of Monadic Heyting Algebras*, 1998 (background on monadic Heyting representation; priority risk, not used for the proof).
