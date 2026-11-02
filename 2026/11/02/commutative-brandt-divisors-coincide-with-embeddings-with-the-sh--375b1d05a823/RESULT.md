# Commutative Brandt divisors coincide with embeddings, with the sharp matrix index

## Finding
Let \(S\) be a **nonempty finite commutative semigroup**. The following assertions are equivalent.

1. \(S\) is a divisor of some finite Brandt semigroup, meaning a surjective homomorphic image of a subsemigroup of \(B_m(G)\) for some finite group \(G\) and integer \(m\ge1\).
2. \(S\) embeds into some finite Brandt semigroup.
3. Either \(S\) is a finite abelian group (without an external absorbing zero), or \(S\) has an absorbing zero \(z\) and admits the disjoint union
   \[S=\{z\}\sqcup H_1\sqcup\cdots\sqcup H_t\sqcup X,\qquad t\ge0,\]
   in which each \(H_i\) is a finite abelian group, distinct groups multiply into \(z\), and \(xS=Sx=\{z\}\) for every \(x\in X\). The set \(X\) may be empty. The case \(t=0\), \(X=\varnothing\) is the one-element zero semigroup.

There is an exact, sharp **minimal Brandt index**: letting \(b(S)\) be the least number of matrix indices of a finite Brandt semigroup containing \(S\), one has \(b(S)=1\) if \(S\) is a group, and \(b(S)=1\) for the one-element zero semigroup. For every other semigroup in alternative (3),
\[b(S)=t+2\mathbf{1}_{X\ne\varnothing}.\]
In particular, the minimum depends on the number of nonzero group components and the presence of an annihilator element, **not on the sizes** of the components or of \(X\). The nonzero group components and the annihilator set are intrinsically determined by \(S\).

## Assumptions and scope
All semigroups and groups are finite and nonempty, except that the auxiliary set \(X\) and the index set of groups may be empty. No identity is assumed for \(S\). In the Brandt semigroup
\[B_m(G)=\{0_B\}\sqcup\{(i,g,j):1\le i,j\le m,\ g\in G\},\]
\[(i,g,j)(k,h,\ell)=\begin{cases}(i,gh,\ell)&j=k,\\0_B&j\ne k.\end{cases}\]
The zero \(0_B\) absorbs all elements. An external zero of a semigroup is a distinct absorbing element added to an existing group. A divisor requires a *subsemigroup* followed by a *surjective homomorphism*; it does not mean a subgroup or an arbitrary quotient of the whole Brandt semigroup.

## Proof
**Step 1: A divisor without ambient zero is a group.** Suppose \(T\subseteq B_m(G)\) is a nonempty subsemigroup. If \(0_B\notin T\), no off-diagonal \((i,g,j)\), \(i\ne j\), can belong to \(T\), since its square is \(0_B\). Two different diagonal positions cannot occur, since their product is \(0_B\). Therefore \(T\) lies in a single copy of \(G\). Every nonempty finite subsemigroup of a group is a subgroup, and every commutative homomorphic image of it is an abelian group.

**Step 2: Diagonal images of a divisor with zero are groups with disjoint nonzero supports.** Now assume \(0_B\in T\), and let \(\phi:T\twoheadrightarrow S\) be a homomorphism with \(S\) commutative. Write \(z=\phi(0_B)\); it is absorbing in \(S\). For each position \(i\), the set \(T_i=T\cap\{(i,g,i):g\in G\}\), if nonempty, is a finite subgroup. Its image \(K_i=\phi(T_i)\) is an abelian subgroup of \(S\), possibly the singleton \(\{z\}\). If \(i\ne j\), then \(uv=0_B\) for \(u\in T_i,v\in T_j\). Thus any common element \(c\in K_i\cap K_j\) satisfies \(c^2=z\). Since \(c\in K_i\) and \(c^2\in K_i\), the global zero belongs to this group. A group containing the absorbing zero of \(S\) must be \(\{z\}\). Hence \(K_i\cap K_j\subseteq\{z\}\), and all nonzero group images from distinct indices are disjoint. In particular, distinct nontrivial \(K_i\) multiply into \(z\).

**Step 3: Off-diagonal images annihilate everything.** Fix \(a=(i,g,j)\in T\) with \(i\ne j\), and write \(s=\phi(a)\). Then \(s^2=z\). For any \(b=(k,h,\ell)\in T\), if either \(ab=0_B\) or \(ba=0_B\), commutativity of \(S\) implies \(s\phi(b)=z\). Otherwise both products are nonzero; necessarily \(k=j\) and \(\ell=i\), with \(ab\in T_i\) and \(ba\in T_j\). Commutativity makes their common image \(c=\phi(ab)=\phi(ba)\). Since \((ab)(ba)=0_B\) for \(i\ne j\), one has \(c^2=z\). But \(c\) lies in the group \(K_i\), so the argument from Step 2 gives \(c=z\). Thus \(s\phi(b)=z\) in all cases. The same holds for \(b=0_B\). Moreover, no nonzero off-diagonal image can also lie in a diagonal group image, since its square is \(z\). This proves the disjoint decomposition in (3), grouping the nonzero diagonal images and placing the remaining nonzero off-diagonal images in \(X\).

**Step 4: Every listed semigroup embeds.** If \(S\) is a group, use its diagonal copy in \(B_1(S)\). The singleton embeds in \(B_1(\{1\})\). Otherwise take a finite group \(G\) containing *group embeddings* \(\iota_i:H_i\hookrightarrow G\), such as \(G=(\prod_i H_i)\times C_r\), with \(r\ge\max(1,|X|)\). Use indices \(1,\ldots,t\) for the groups and send \(h\in H_i\) to \((i,\iota_i(h),i)\). Send \(z\) to \(0_B\). If \(X\ne\varnothing\), reserve **two new, distinct** indices \(a,b\) outside \(\{1,\ldots,t\}\) and send each \(x\in X\) to \((a,g_x,b)\), with distinct labels \(g_x\in G\). All products involving an \(X\)-element vanish (since none of the group indices equals \(a\) or \(b\), and \(a\ne b\)), and products of group elements are preserved. This is injective and proves (3) implies (2). An embedding trivially implies divisibility, completing the equivalence.

**Step 5: Sharpness of the index.** In any embedding of a semigroup with at least two elements and absorbing zero \(z\), \(z\) must map to \(0_B\): a nonzero Brandt idempotent \((i,1,i)\) cannot absorb any different element of \(B_m(G)\), whereas \(z\) absorbs everything in the embedded subsemigroup. For each nonzero group component \(H_i\), its identity maps to a nonzero diagonal idempotent. Distinct group identities must have distinct Brandt indices, so \(m\ge t\). If \(X\ne\varnothing\), take \(x\in X\): its nonzero image squares to \(0_B\), hence is off-diagonal \((a,g,b)\) with \(a\ne b\). Since \(x\) annihilates every group identity on either side, neither endpoint can be one of the \(t\) group indices. Therefore \(m\ge t+2\). Step 4 attains the relevant lower bounds. The two singleton cases have minimum \(1\) by definition. Finally, all nonzero subgroup elements and all nonzero annihilators are intrinsic, giving uniqueness of the structural data.

## Verification
The included self-contained Python program `CHECK.py` enumerates all nonempty subsemigroups of the five-element Brandt semigroup over the trivial group, all congruences on each subsemigroup, and every commutative quotient. It checks the stated structural description directly from quotient multiplication tables. It also checks explicit embeddings for group-order lists \(()\), \((2)\), \((2,3)\), and \((1,2,2)\), with respectively \(4,0,3,1\) annihilator elements, testing every product rather than selected samples. Its recorded output concludes `VERIFY_OK`. This finite calculation corroborates but does not replace the general proof, and it does not check all finite groups or arbitrary indices.

## Relationship to prior work
Problem 1.2(1) of Bershadsky, Kublanovsky, and Mashevitzky's April 2026 collection explicitly asks for a description of divisors of finite Brandt semigroups [1]. This theorem settles **the commutative target class only**. Margolis, Rhodes, and Silva [2, Theorems 5.3–5.5] describe inverse and nilpotent components of subsemigroups of *aperiodic* Brandt semigroups. Their results neither assert the collapse of all off-diagonal images under arbitrary commutative quotients of Brandt semigroups with structure groups, nor give the sharp minimum matrix index in this target class. Standard Brandt multiplication is also recalled in [3]. No assertion is made that general Brandt divisor problems, Rees matrix divisor problems, or subsemigroup decompositions themselves are settled here.

## Limitations
The theorem classifies **only commutative** finite semigroup divisors. For noncommutative quotient targets the off-diagonal annihilation step fails. It permits the Brandt structure group to vary with \(S\), so it does not determine the minimal order of that group, or possible embeddings with a preassigned group. The finite tests cover a small ambient Brandt example and selected constructions, not infinite verification. A historical-equivalence risk remains: an older general divisor theorem may implicitly specialize to this criterion, even though no explicit equivalent and sharp-index result was identified in the inspected sources.

## References
[1] S. Bershadsky, S. Kublanovsky, G. Mashevitzky (eds.), *The Lyapin's notebook: a collection of unsolved problems in Semigroup Theory*, arXiv:2604.04763v1 (2026), Problem 1.2(1). https://arxiv.org/abs/2604.04763

[2] S. Margolis, J. Rhodes, P. V. Silva, *On the subsemigroup complex of an aperiodic Brandt semigroup*, arXiv:1705.04956v1 (2017), Theorems 5.3–5.5. https://arxiv.org/abs/1705.04956

[3] *\(\aleph_0\)-categoricity of semigroups*, *Semigroup Forum* (2019), Section 4 (Brandt multiplication and 0-direct unions). https://doi.org/10.1007/s00233-019-10002-7
