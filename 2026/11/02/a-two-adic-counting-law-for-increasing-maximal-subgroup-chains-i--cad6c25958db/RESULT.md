# A two-adic counting law for increasing maximal subgroup chains in generalized dihedral groups

## Finding
Let \(A\) be a finite abelian group, with \(A_{\mathrm{odd}}\) its unique subgroup of odd order, and let \(G=\operatorname{Dih}(A)=A\rtimes C_2\) be the generalized dihedral group in which the nonidentity element of \(C_2\) acts on \(A\) by inversion. Write \(I(G)\) for the number of unrefinable chains
\[
  1=G_0<G_1<\cdots<G_s=G
\]
whose successive indices \(\lvert G_i:G_{i-1}\rvert\) are nondecreasing. Different chains are counted as different whenever their actual subgroups differ.

For a finite abelian \(p\)-group \(P\), define \(f(P)\) as the number of unrefinable chains from \(1\) to \(P\). It is computable by \(f(1)=1\) and
\[
  f(P)=\sum_{\substack{H\le P\\\lvert P:H\rvert=p}} f(H)
  \quad(P\ne1).
\]
For the Sylow subgroups \(A_p\) of \(A\), put \(F(A)=\prod_{p\mid\lvert A\rvert}f(A_p)\), with an empty product equal to \(1\).

**Theorem.** For every finite abelian \(A\), including \(A=1\),
\[
  \boxed{I(\operatorname{Dih}(A))=F(A)\bigl(2\lvert A\rvert-\lvert A_{\mathrm{odd}}\rvert\bigr).}
\]
There is also an exact formula for the number \(T(G)\) of *all* unrefinable subgroup chains of \(G\), without an index-order restriction:
\[
  \boxed{T(\operatorname{Dih}(A))
    =\sum_{H\le A}\lvert A:H\rvert\,b(H)\,b(A/H),}
\]
where \(b(B)\) is the total number of unrefinable subgroup chains from \(1\) to the finite abelian group \(B\).

**Consequences.** For the ordinary dihedral group \(D_{2n}=\operatorname{Dih}(C_n)\), write \(n_{\mathrm{odd}}\) for the largest odd divisor of \(n\). Then
\[
  \boxed{I(D_{2n})=2n-n_{\mathrm{odd}}.}
\]
For \(A=C_p^r\), one has \(F(A)=\prod_{j=1}^{r}(p^j-1)/(p-1)\), so the general formula is explicit in \(p\) and \(r\). Moreover, for odd squarefree \(n\) with \(k\) distinct prime factors, precisely \(n\) maximal chains of \(D_{2n}\) have nondecreasing indices, while
\[
  \frac{I(D_{2n})}{T(D_{2n})}\le\frac{1}{k!}.
\]
Thus the proportion of increasing maximal chains can decay at least factorially with the number of distinct prime divisors even in a family where increasing chains always exist.

## Assumptions and scope
All groups are finite. We use an *unrefinable* or *maximal* subgroup chain to mean a saturated chain in the full subgroup lattice, beginning at the trivial subgroup and ending at the whole group. The subgroup steps, rather than chains modulo conjugacy, are counted. No restriction is imposed on the exponent, rank, or parity of the finite abelian kernel \(A\). The inversion action may have a kernel when \(A\) has elements of order two; the semidirect product definition remains valid. In the degenerate case \(A=1\), \(G=C_2\) and the formula returns one chain.

For a finite abelian group \(B\), every maximal inclusion of subgroups has prime index. Hence every unrefinable chain of \(B\) has exactly one step for each prime factor of \(\lvert B\rvert\), counted with multiplicity. Its steps can be chosen in nondecreasing order of indices exactly by independently choosing full subgroup flags of the Sylow subgroups \(B_p\). Consequently \(F(B)\) is precisely the number of index-nondecreasing chains from \(1\) to \(B\).

## Proof
Write the operation of \(G\) additively on \(A\): its elements are \((a,\varepsilon)\), for \(a\in A\) and \(\varepsilon\in\{0,1\}\), with
\[
  (a,\varepsilon)(b,\delta)
    =(a+(-1)^\varepsilon b,\varepsilon+\delta\pmod{2}).
\]

**Subgroup parametrization.** Every subgroup contained in \(A\) is an ordinary subgroup \(H\le A\). Every subgroup \(K\not\le A\) intersects \(A\) in some \(H\le A\) and is uniquely expressible as
\[
 K(H,a)=\{(h,0):h\in H\}\cup\{(a+h,1):h\in H\},
 \qquad a+H\in A/H.
\]
Indeed, the product of two elements in the second coset lies in \(H\), and an outside element conjugates \(H\) by inversion. The subgroup is determined by its intersection with \(A\) and its outside coset. In particular, for fixed \(H\), there are exactly \(\lvert A:H\rvert\) distinct outside subgroups \(K(H,a)\).

**Cover relations.** For every \(H\le A\), the inclusion \(H<K(H,a)\) has index \(2\), hence is maximal. Given \(H\le L\le A\), the unique outside subgroup with intersection \(L\) that contains \(K(H,a)\) is \(K(L,a)\), since its outside coset must contain \(a+H\). Thus \(K(H,a)<K(L,a)\) is maximal precisely when \(H<L\) is maximal in the subgroup lattice of \(A\). Finally, any saturated chain that first leaves \(A\) at \(H<K(L,a)\) must have \(L=H\): otherwise \(H<L<K(L,a)\) would interpolate. Therefore there is exactly one index-\(2\) transition from a subgroup of \(A\) to an outside subgroup in every full maximal chain of \(G\).

**All-chain enumeration.** Fix its transition subgroup \(H\le A\). There are \(b(H)\) complete flags from \(1\) to \(H\), exactly \(\lvert A:H\rvert\) choices of the outside subgroup \(K(H,a)\), and exactly \(b(A/H)\) flags of outside subgroups from \(K(H,a)\) to \(K(A,0)=G\), by the cover correspondence. The choices are independent and uniquely recoverable from a chain, so summing over \(H\) gives the stated formula for \(T(G)\).

**Nondecreasing-index enumeration.** Every step besides the transition has an index equal to the index of a maximal inclusion in \(A\), hence a prime. A chain's sequence is the sequence of indices in a full subgroup flag of \(A\), with one additional index \(2\) inserted at its transition position. Such a sequence is nondecreasing if and only if the flag of \(A\) has nondecreasing prime indices and the insertion takes place within or immediately adjacent to its initial block of \(2\)'s. Let \(e=v_2(\lvert A\rvert)\). For any one of the \(F(A)\) nondecreasing flags of \(A\), there are \(e+1\) possible transition positions: after exactly \(j\in\{0,\ldots,e\}\) index-\(2\) steps. The transition subgroup \(H\) then has order \(2^j\), and the number of outside-coset choices is exactly \(\lvert A:H\rvert=\lvert A\rvert/2^j\). Accordingly,
\[
 I(G)=F(A)\sum_{j=0}^{e}\frac{\lvert A\rvert}{2^j}
     =F(A)\bigl(2\lvert A\rvert-\lvert A\rvert/2^e\bigr)
     =F(A)\bigl(2\lvert A\rvert-\lvert A_{\mathrm{odd}}\rvert\bigr).
\]
Uniqueness of the transition and flag ensures no overcounting.

For cyclic \(A=C_n\), every Sylow subgroup has exactly one complete maximal flag, proving the cyclic formula. For \(A=C_p^r\), each \(j\)-dimensional vector subspace has \((p^j-1)/(p-1)\) hyperplanes, and downward counting yields the stated product. If \(n\) is odd and squarefree, \(I(D_{2n})=n\). Among the total maximal chains, already the chains with transition \(H=1\) contribute \(n\,b(C_n)=n\,k!\), because the \(k\) distinct prime-index steps in \(C_n\) may appear in any of the \(k!\) orders. Hence \(T(D_{2n})\ge n\,k!\) and the probability bound follows. \(\square\)

## Verification
The standalone file `verify_increasing_dihedral.py` implements the group law directly for each listed small finite abelian kernel, generates every subgroup by closure, computes all maximal cover relations in its subgroup lattice, and independently counts both nondecreasing-index and unrestricted full maximal chains. In parallel it enumerates all flags of the abelian kernel to compute \(F(A)\) and tests the theorem's formula. It reports `VERIFY_OK` on success.

The independent finite tests include cyclic kernels of orders \(2,3,4,5,6,8,10,12\), elementary abelian kernels \(C_2^2\), \(C_3^2\), \(C_2^3\), and mixed-exponent kernels \(C_2\times C_4\), \(C_2\times C_3\), \(C_4\times C_3\), and \(C_2^2\times C_3\). For example, the exact counts of increasing full chains are \(21\) for \(A=C_2^2\), \(75\) for \(A=C_2\times C_4\), \(36\) for \(A=C_3^2\), and \(63\) for \(A=C_2^2\times C_3\). These checks exercise both odd and even kernels, mixed prime factors, and noncyclic kernels.

The general theorem is proved by the subgroup-parametrization and cover-bijection argument above; finite enumeration is a diagnostic and does not constitute an infinite proof.

## Relationship to prior work
Monakhov and Sokhor studied nondecreasing-index maximal subgroup chains as a structural condition, proving consequences for supersolubility and classifying certain groups by chain-index behavior (Results in Mathematics, 2025). Their separate open-access 2025 paper gives Sylow-tower and supersolubility criteria for monotone prime-index chains, without the present exact counts. Sater's 2026 paper answered a related existence question negatively for some finite soluble groups and explicitly notes that finite nilpotent groups admit nondecreasing-index chains. The present theorem studies a distinct **enumerative** question for every generalized dihedral group, yielding a universal two-adic factor, the unrestricted-chain formula, and a factorial rarity bound. Those exact counts and densities are not stated in the inspected full Sater manuscript.

Sajedi, Moghaddam, and Darabi studied probabilities concerning normality among general subgroup chains and quoted earlier counts for all chains of dihedral groups. Such counts distinguish neither saturated maximal chains nor the nondecreasing-index restriction considered here. The present argument uses only the standard subgroup description of a generalized dihedral group and a direct cover correspondence.

## Limitations
The theorem is not a classification of increasing chains in arbitrary finite soluble groups, nor does it imply their existence outside the stated generalized dihedral class. The formula concerns actual labelled subgroup chains, not chains up to conjugacy. The factorial upper bound on the *proportion* is not asserted to be sharp. No nontrivial lower bound on that proportion is supplied. Novelty has been checked against accessible contemporary sources and mathematical records, but historical priority is not independently established: older work on subgroup flags and on maximal-index sequences could contain an equivalent theorem. The full text of the 2025 Monakhov–Sokhor article was not accessible for a comprehensive comparison, so its abstract and accessible first-page material cannot establish whole-document noncoverage.

## References
1. R. Sater, *Finite Soluble Groups Without Increasing Unrefinable Chains* (2026), arXiv:2609.26228; full manuscript source: https://github.com/RichieSater/monotone-maximal-chains/blob/main/paper/main.tex (inspected).
2. V. S. Monakhov and I. L. Sokhor, *On Indices of Maximal Chains in Finite Groups*, Results in Mathematics **80** (2025), article 155, https://doi.org/10.1007/s00025-025-02468-5 (abstract and accessible preview inspected; full text not inspected).
3. V. S. Monakhov and I. L. Sokhor, *To the Iwasawa and Huppert theorems on supersolvability of finite groups*, Siberian Electronic Mathematical Reports **22** (2025), 143–153, https://doi.org/10.33048/semi.2025.22.011 (full eleven-page paper inspected).
4. M. Sajedi, F. Moghaddam, and A. Darabi, *Probability of Normality of Chains in Finite Groups*, Journal of Mathematical Extension **17** (2023), issue 4, https://doi.org/10.30495/JME.2023.2593 (full accessible paper inspected for its distinct chain-counting notion).
