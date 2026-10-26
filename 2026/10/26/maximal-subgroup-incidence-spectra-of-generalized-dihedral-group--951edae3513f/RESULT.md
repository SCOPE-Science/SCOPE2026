# Maximal-subgroup incidence spectra of generalized dihedral groups

## Finding

Let \(A\) be any **nontrivial finite abelian group**. Write it as its direct product of Sylow subgroups \(A=\prod_{p\in\pi(A)} A_p\), where \(\pi(A)\) is the set of primes dividing \(|A|\). Put
\[
r_p=\dim_{\mathbb F_p}(A_p/pA_p),\qquad
h_p=\frac{p^{r_p}-1}{p-1},\qquad
b_p=|pA_p|=\frac{|A_p|}{p^{r_p}},
\]
\[
M=1+\sum_{p\in\pi(A)}p h_p,\qquad
H=\sum_{p\in\pi(A)}h_p.
\]
For the generalized dihedral group \(G=\operatorname{Dih}(A)=A\rtimes\langle s\rangle\) with \(s^2=1\) and \(sas=-a\) (additive notation), let \(\mathcal M(G)\) denote the distinct maximal subgroups, and set
\[
\delta(g)=|\{K\in\mathcal M(G):g\in K\}|.
\]
Then \(|\mathcal M(G)|=M\), \(\Phi(G)=\prod_p pA_p\), and **the complete incidence-degree enumerator** is
\[
\boxed{\sum_{g\in G}z^{\delta(g)}
=|A|z^H+\sum_{S\subseteq\pi(A)}
 \left(\prod_{p\in S}(|A_p|-b_p)\prod_{p\notin S}b_p\right)
 z^{M-\sum_{p\in S}p^{r_p}}.}
\]
Here the first summand counts all reflections; the second counts rotations classified by nonzero Sylow–Frattini residues. In particular,
\[
\boxed{\operatorname{ui}(G)=M+1-\min_{p\in\pi(A)}p^{r_p}
=2+\sum_{p\in\pi(A)}\frac{p(p^{r_p}-1)}{p-1}
  -\min_{p\in\pi(A)}p^{r_p}.}
\]
The formula includes **even-order kernels**, for which inversion can have fixed points, as well as kernels of odd order.

## Assumptions and scope

The group \(A\) is finite, abelian and nontrivial; no restriction on its exponent, number of Sylow factors, or parity is imposed. The semidirect-product action is inversion. The notation \(pA_p\) denotes the subgroup of multiples of \(p\), and \(r_p\geq1\).

The Frattini subgroup \(\Phi(G)\) is the intersection of all maximal subgroups. The uniform intersection number \(\operatorname{ui}(G)\) is the least positive integer \(k\) for which **every** set of \(k\) distinct maximal subgroups has intersection \(\Phi(G)\). All intersection assertions concern the actual subgroups, not their isomorphism types.

## Proof

**1. Complete maximal-subgroup classification.** Regard \(A\) as the normal index-two subgroup of \(G\). It is maximal. Let \(K\) be any other maximal subgroup of \(G\), so \(K\not\subseteq A\); put \(L=K\cap A\). Pick a reflection \(as\in K\). Then \(K=L\sqcup(as)L\). If \(L\) were not maximal in \(A\), we could choose \(L<J<A\) and obtain \(K<J\sqcup(as)J<G\), contrary to maximality of \(K\). Conversely, if \(L\) is maximal in \(A\), the union \(L\sqcup(as)L\) is a subgroup because inversion preserves \(L\); its index in \(G\) is the prime \([A:L]\), so it is maximal. Two choices \(a,a'\) give the same maximal subgroup for fixed \(L\) exactly when \(a+L=a'+L\). Therefore **all** maximal subgroups, without omission or duplication, are
\[
A\quad\text{and}\quad K(L,a+L)=L\sqcup(as)L,
\qquad L\text{ maximal in }A,
\quad a+L\in A/L.
\]
(The equality \((as)L=(a+L)s\) is valid because \(-L=L\).)

**2. Count and Frattini subgroup.** A maximal subgroup \(L\) of the finite abelian group \(A\) has prime index \(p\) and is the inverse image of a hyperplane of \(V_p=A_p/pA_p\), containing all \(A_q\) for \(q\ne p\). The number of such hyperplanes is \(h_p=(p^{r_p}-1)/(p-1)\). For each \(L\) of index \(p\), the classification in Step 1 gives exactly \(p\) maximal subgroups \(K(L,a+L)\). Hence \(|\mathcal M(G)|=1+\sum_p p h_p=M\). Since \(A\) itself is maximal, \(\Phi(G)\subseteq A\), and for any rotation \(x\in A\), membership in \(K(L,a+L)\) is precisely membership in \(L\), independent of \(a\). Thus
\[
\Phi(G)=\bigcap_{L\text{ maximal in }A}L
=\prod_p pA_p.
\]

**3. Degrees of reflections and rotations.** Fix a reflection \(as\). For each maximal \(L\leq A\), the reflection belongs to exactly one of the \(p\) groups \(K(L,a'+L)\), namely the one with \(a'+L=a+L\). It does not belong to \(A\), so \(\delta(as)=H=\sum_p h_p\).

Now let \(x\in A\), and write \(\bar x_p\in V_p\) for its residue. If \(\bar x_p=0\), all \(h_p\) hyperplanes contain \(\bar x_p\). If \(\bar x_p\ne0\), exactly \((p^{r_p-1}-1)/(p-1)=h_p-p^{r_p-1}\) hyperplanes contain it. Each such hyperplane contributes \(p\) maximal subgroups containing \(x\), and the maximal subgroup \(A\) contributes one more. If \(S(x)=\{p:\bar x_p\ne0\}\), it follows that
\[
\delta(x)=1+\sum_p p h_p-\sum_{p\in S(x)}p^{r_p}
=M-\sum_{p\in S(x)}p^{r_p}.
\]
For a prescribed subset \(S\subseteq\pi(A)\), there are exactly
\[
\prod_{p\in S}(|A_p|-b_p)\prod_{p\notin S}b_p
\]
rotations with \(S(x)=S\), by independence of the Sylow components. Adding the \(|A|\) reflections proves the stated enumerator.

**4. Sharp uniform intersection threshold.** In every finite group,
\[
\operatorname{ui}(G)=1+\max_{g\notin\Phi(G)}\delta(g).
\]
Indeed, a family of maximal subgroups has intersection strictly larger than \(\Phi(G)\) if and only if some element outside \(\Phi(G)\) lies in every subgroup in the family. Taking all maximal subgroups containing a degree-maximizing such element gives a family of the maximum possible size with non-Frattini intersection; one additional arbitrary distinct subgroup always forces the Frattini intersection.

Every rotation outside \(\Phi(G)\) has \(S(x)\ne\varnothing\), so the greatest possible rotation degree is \(M-\min_p p^{r_p}\). This is attained: choose a nonzero residue in just one Sylow component whose \(p^{r_p}\) is minimal, and zero residues in all other components. The reflection degree is \(H\). If \(p_*\) realizes the minimum, then
\[
M-p_*^{r_{p_*}}-H
=\sum_{p\ne p_*}(p^{r_p}-1)\ge0.
\]
Thus a rotation attains a degree at least as large as any reflection. The maximum is precisely \(M-\min_p p^{r_p}\), proving the boxed uniform-intersection formula.

## Verification

The accompanying standard-library Python file `verify_incidence.py` reconstructs the full finite group from the semidirect-product multiplication law, enumerates **all subgroups**, extracts maximal subgroups by inclusion, computes their actual intersection and every element's maximal-subgroup incidence degree, and compares the outputs to the theorem. It does not build the maximal subgroups using the theorem's classification.

Sixteen exact examples were checked, with abelian kernels specified by cyclic-factor orders:
\[
(2),\ (4),\ (2,2),\ (2,2,2),\ (4,2),\ (4,4),\
(2,3),\ (2,3,3),\ (3),\ (9),\ (3,3),\ (9,3),\
(3,5),\ (3,3,3),\ (3,3,5),\ (5,5).
\]
All passed (`VERIFY_OK`). In particular, the noncyclic odd kernel \(A=C_3\times C_3\times C_5\) has incidence-degree profile
\[
32z^4+45z^5+8z^9+4z^{13}+z^{18}
\]
and \(\operatorname{ui}(G)=14\). For the even kernel \(A=C_2\times C_2\), the group is \(C_2^3\), and the profile is \(7z^3+z^7\) with \(\operatorname{ui}(G)=4\).

These finite checks calculate the examples directly; they are not a substitute for the unrestricted argument of Steps 1–4.

## Relationship to prior work

Choudhury and Khanra (2026, arXiv:2610.22268v1, Theorem 2.6) determine the uniform intersection number of the **ordinary dihedral group with cyclic rotation kernel**. Our formula specializes to theirs when each \(r_p=1\): if \(p_*\) is the smallest prime divisor of \(|A|\), then
\[
\operatorname{ui}(\operatorname{Dih}(A))=2+\sum_{p\ne p_*}p.
\]
The cyclic-kernel case is prior work, not an original special case. Their paper's general Frattini-quotient lemma is compatible with our rank-dependence, but does not supply the maximal-subgroup incidence spectrum or formula for arbitrary noncyclic abelian kernels.

Archer, Bautista Serrano, Cook, Lauderdale, Perez and Villalobos (2019, arXiv:1907.02898v1, Proposition 4.1) determine the **minimum** number of maximal subgroups in an intersection for classical dihedral groups; this differs from the uniform invariant, and they do not establish the noncyclic incidence distribution.

For the same generalized-dihedral class, the published finding *Minimum-size independence graphs of odd generalized dihedral groups* treats the pair-extendibility graph of minimal generating sets, not the maximal-subgroup incidence profile. *Subgroup commutativity of odd generalized dihedral groups* calculates permutation probabilities of pairs of subgroups. Neither statement gives the displayed incident-maximal-subgroup counts or the uniform-intersection formula.

## Limitations

The result covers only finite abelian kernels with inversion action, not arbitrary kernels or arbitrary order-two automorphisms. The cyclic-kernel formula and the general Frattini-quotient lemma were known; the substantive new claims are the complete incidence enumerator and sharp uniform threshold for all noncyclic abelian kernels, including even-order examples.

Exhaustive finite computations do not certify novelty or the infinite family. Prior general results on finite-group subgroup lattices or Frattini quotients could conceivably imply the same formula without naming generalized dihedral groups. No claim of exhaustive global uniqueness or independent mathematical audit is made.

## References

1. Projesh Nath Choudhury and Biswaranjan Khanra, *Uniform Intersection Numbers and Subgroup-Based Generating Graphs of Groups*, arXiv:2610.22268v1 (first public 15 October 2026), Theorem 2.6 and Lemma 2.4. https://arxiv.org/html/2610.22268v1
2. Kassie Archer, Humberto Bautista Serrano, Kayla Cook, L.-K. Lauderdale, Yansy Perez and Vincent Villalobos, *On the Intersection Numbers of Finite Groups*, arXiv:1907.02898v1 (first public 5 July 2019), Proposition 4.1. https://arxiv.org/html/1907.02898v1
3. *Minimum-size independence graphs of odd generalized dihedral groups*, published mathematical finding (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-minimum-size-independence-graphs-of-odd-generalized-dihedral-gro--04272a18f391
4. *Subgroup commutativity of odd generalized dihedral groups*, published mathematical finding (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-subgroup-commutativity-of-odd-generalized-dihedral-groups--61e304c46710
