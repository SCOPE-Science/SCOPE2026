# Retracts and idempotents of odd extraspecial groups in every rank

## Finding

Fix an odd prime \(p\) and an integer \(n\ge1\). Let \(G_+(p,n)\) be the extraspecial group of order \(p^{2n+1}\) and exponent \(p\), and let \(G_-(p,n)\) be the extraspecial group of the same order and exponent \(p^2\).

An endomorphism \(f:G\to G\) is **idempotent** when \(f^2=f\). Its image \(H=f(G)\) is then a **retract**: the restriction of \(f\) to \(H\) is the identity. Conversely, a retraction onto a subgroup is an idempotent endomorphism.

Define \(I(m,r)=0\) when \(r<0\) or \(r>m\), and otherwise
\[
I(m,r)=\binom{m}{r}_p\prod_{j=0}^{r-1}(p^{m-j}+1),
\]
where the Gaussian binomial coefficient is
\[
\binom{m}{r}_p=
\prod_{j=0}^{r-1}\frac{p^{m-j}-1}{p^{r-j}-1}.
\]
Empty products equal one. Put
\[
B(n,r)=I(n-1,r-1)+p^rI(n-1,r).
\]

**Complete idempotent and retract profile.** For every \(0\le r\le n\), the number of idempotent endomorphisms with image of order \(p^r\) is
\[
\boxed{c_r^+(p,n)=p^{r(2n-r+1)}I(n,r)}
\]
for \(G_+(p,n)\), and
\[
\boxed{c_r^-(p,n)=p^{r(2n-r+1)}B(n,r)}
\]
for \(G_-(p,n)\). All these proper images are elementary abelian, and there is exactly one further idempotent, namely the identity on the whole group. No other image sizes occur.

The numbers of distinct retract subgroups of order \(p^r\) are respectively
\[
\boxed{t_r^+(p,n)=p^rI(n,r),\qquad t_r^-(p,n)=p^rB(n,r).}
\]
Each such subgroup is the image of exactly \(p^{r(2n-r)}\) different retractions.

In particular,
\[
\boxed{c_1^+(p,n)-c_1^-(p,n)=p^{4n-1},}
\]
so the rank-one idempotent spectrum distinguishes the two extraspecial types with the same order.

For the smallest dimension \(n=1\), the respective complete idempotent counts are
\[
2+p^2(p+1),\qquad 2+p^2.
\]

## Assumptions and scope

The prime \(p\) is odd, and \(n\) is any positive integer. The two extraspecial groups are the standard central products of \(n\) order-\(p^3\) extraspecial factors, with one exponent-\(p^2\) factor in the second type. The quotient of either group by its center is a \(2n\)-dimensional symplectic vector space over \(\mathbf F_p\).

The underlying 2019 paper of Anil Kumar and Pradhan gives explicit formulas for all endomorphisms and computes their total number, including the numbers of isotropic subspaces used as known input here. Its first public arXiv version is dated 1 August 2019 and its primary Mathematics Subject Classification is 20D15. The present theorem classifies and enumerates the **idempotent** subsemigroup and all retracts, not the already-known total endomorphism set.

## Proof

Let \(G\) denote either group, with
\[
Z=Z(G)=[G,G]\cong C_p,
\qquad W=G/Z\cong\mathbf F_p^{2n}.
\]
Fix \(z\) generating \(Z\). The equation
\[
[g,h]=z^{\langle \overline g,\overline h\rangle}
\]
defines a nondegenerate alternating form on \(W\).

**Step 1: Every proper retract is elementary abelian and avoids the center.** Suppose \(f^2=f\), and write \(H=f(G)\), so \(f|_H=\operatorname{id}_H\). If \(H\) is nonabelian, then
\[
f(Z)=f([G,G])=[H,H]\ne1.
\]
Because \(Z\) has order \(p\), it follows that \(\ker f\cap Z=1\). On the other hand, for every normal subgroup \(N\) of this class-two extraspecial group,
\[
[N,G]\subseteq N\cap Z.
\]
If \(N\cap Z=1\), then \(N\) centralizes \(G\), so \(N\subseteq Z\) and hence \(N=1\). Applied to \(N=\ker f\), this makes \(f\) injective, hence an automorphism. An idempotent automorphism is the identity. Thus every proper retract is abelian.

For a proper retract, \(H\) is abelian and therefore \(f(Z)=[H,H]=1\). Since \(f|_H\) is the identity, \(H\cap Z=1\). Every \(g\in G\) has \(g^p\in Z\), so every \(h\in H\) satisfies \(h^p=1\). Thus \(H\) is elementary abelian; its image \(S=HZ/Z\subset W\) has dimension \(r=\log_p|H|\) and is totally isotropic. Consequently \(0\le r\le n\).

**Step 2: The power obstruction.** The map
\[
\ell:W\longrightarrow\mathbf F_p,
\qquad g^p=z^{\ell(\overline g)}
\]
is well defined, because the center has exponent \(p\). It is linear: since \(p\) is odd and \(G\) has class two, the commutator term in the Hall–Petrescu power formula has exponent divisible by \(p\). For \(G_+\), the power map is zero, while for \(G_-\) it is nonzero. Every proper retract satisfies
\[
S\subseteq\ker\ell
\]
because its elements have order dividing \(p\).

Conversely, let \(S\subseteq W\) be an isotropic subspace of dimension \(r\), with \(S\subseteq\ker\ell\) if \(\ell\ne0\). Its full preimage \(\pi^{-1}(S)\) in \(G\) is abelian by isotropy and has exponent \(p\) by the power condition. It is therefore an elementary abelian group of order \(p^{r+1}\), containing \(Z\) as a one-dimensional subspace. Its complements \(H\) to \(Z\) are precisely the graphs of linear maps \(S\to Z\), so there are
\[
p^r
\]
choices of \(H\) above each \(S\).

For any such \(H\), a retraction \(G\to H\) must kill \(Z=[G,G]\), hence factor through \(W\), and it is completely specified by a linear map \(P:W\to S\) whose restriction to \(S\) is the identity. Choosing a complement of \(S\) in \(W\) shows that there are
\[
p^{r(2n-r)}
\]
such maps. They all give group retractions by composing with the canonical inverse \(S\xrightarrow{\sim}H\) of the quotient map. Thus each \(S\) yields \(p^{r(2n-r+1)}\) idempotents and \(p^r\) retract subgroups. Distinct \(S\), distinct \(H\), and distinct \(P\) give distinct objects. The case \(r=0\) is the zero endomorphism; the identity was handled in Step 1.

**Step 3: Isotropic-subspace counts.** The number of \(r\)-dimensional totally isotropic subspaces of a nondegenerate symplectic space of dimension \(2n\) over \(\mathbf F_p\) is
\[
I(n,r)=\binom{n}{r}_p\prod_{j=0}^{r-1}(p^{n-j}+1).
\]
This formula follows by successively choosing an ordered independent isotropic basis and dividing by the number of ordered bases of an \(r\)-space. It also appears as an established enumeration in Anil Kumar–Pradhan, Theorem 5.2.

For the exponent-\(p^2\) case, nondegeneracy of the symplectic form identifies \(\ker\ell\) with \(R^\perp\) for a one-dimensional isotropic line \(R\). The radical of \(R^\perp\) is \(R\), and \(R^\perp/R\) is symplectic of dimension \(2n-2\). An isotropic \(r\)-subspace of \(R^\perp\) either contains \(R\), giving \(I(n-1,r-1)\) choices, or is disjoint from \(R\). In the latter case its image in the quotient is an isotropic \(r\)-space and the lifts are the \(p^r\) graphs of linear maps into \(R\), giving \(p^rI(n-1,r)\) choices. Hence their total is
\[
B(n,r)=I(n-1,r-1)+p^rI(n-1,r).
\]
Combining this with Step 2 proves all the enumerations.

For \(r=1\), the number of symplectic lines is \((p^{2n}-1)/(p-1)\), while the number contained in a hyperplane is \((p^{2n-1}-1)/(p-1)\). Their difference is \(p^{2n-1}\). Multiplying by the number \(p^{2n}\) of retractions per line proves
\[
c_1^+(p,n)-c_1^-(p,n)=p^{4n-1}.
\]

## Verification

The included dependency-free Python program `artifacts/verify.py` implements the closed isotropic-subspace and retraction formulas. It **independently** enumerates idempotent endomorphisms from generator images for both extraspecial groups of order \(p^3\) at \(p=3\) and \(p=5\). The resulting pairs of counts are
\[
(38,11)\quad\text{and}\quad(152,27),
\]
respectively. The program checks the group presentation relations for admissible generator images and verifies the idempotency of the induced maps, rather than substituting the claimed formulas to obtain these small-group counts.

For \(n=2\), it also independently enumerates all isotropic lines and planes and those contained in the relevant hyperplane for \(p=3,5\). At \(p=3\), the isotropic counts are \((40,40)\), and the corresponding hyperplane counts are \((13,4)\). The computed idempotent rank profiles for that prime are
\[
(1,3240,29160)\quad\text{and}\quad(1,1053,2916).
\]
Adding the identity gives totals \(32402\) and \(3971\).

The recorded output ends with `VERIFY_OK`. All finite checks are replay evidence, not a substitute for the general proof.

## Relationship to prior work

Anil Kumar and Pradhan (2019) describe all endomorphisms of both types of extraspecial groups in Theorems \(\Omega\) and \(\Sigma\), and count all endomorphisms in Theorems 5.2–5.3. In particular, the isotropic counts \(I(n,r)\) and their hyperplane analogues are **prior results** and are explicitly reused here. Their statements do not count idempotents, characterize retract subgroups, give the rank-by-rank idempotent profile, or deduce the rank-one distinction between exponent types.

The general equivalence between retracts and images of idempotent endomorphisms is standard; that equivalence alone does not classify the possible retracts of these groups or count distinct retractions. The new step is the exact lift-and-projection classification uniformly in both extraspecial types and all ranks. Searches under “idempotent endomorphism”, “retract”, “projection”, “endomorphism monoid”, symplectic equivalences, and the numerical fingerprints found no published covering statement. The earlier total-endomorphism classification makes this an explicit arithmetic refinement rather than an independent classification of all endomorphisms.

## Limitations

The theorem is restricted to odd primes. For \(p=2\), the power obstruction is quadratic rather than linear and the two extraspecial types need different treatment. The statement is about extraspecial centers of order \(p\), not the broader Heisenberg groups over arbitrary nonprime finite fields.

The first two moments of the idempotent spectrum are not asserted to determine every finite group or its complete endomorphism monoid. Possible equivalent retract enumerations under older terminology remain a literature risk; search failure is not a proof of historical novelty.

## References

1. C. P. Anil Kumar and S. S. Pradhan, “On the Endomorphism Semigroups of Extra-special \(p\)-groups and Automorphism Orbits,” first public version arXiv:1908.00331v1 (1 August 2019); revised arXiv:1908.00331v2 (3 October 2019); *International Journal of Group Theory* 11 (2022), 201–220, DOI `10.22108/IJGT.2021.129815.1708`.
2. “Retract (group theory),” standard group-theoretic definition and its equivalence with idempotent endomorphisms, `https://en.wikipedia.org/wiki/Retract_(group_theory)` (used only for terminology, not for the enumerations).
