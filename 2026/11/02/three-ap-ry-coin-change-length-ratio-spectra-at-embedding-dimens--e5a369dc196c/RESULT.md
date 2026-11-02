# Three Apéry coin-change length-ratio spectra at embedding dimension \(m-3\)

## Finding
For every integer \(m\ge7\), if a numerical semigroup \(S\) has multiplicity \(m\) and embedding dimension \(e(S)=m-3\), then the set of elasticity ratios over its Apéry minima is precisely one of
\[
\mathcal R(S)=\{1\},\qquad \mathcal R(S)=\{1,3/2\},\qquad \mathcal R(S)=\{1,2\}.
\]
All three alternatives are attained for **each** integer \(m\ge7\). In coin-change terms, at the smallest attainable positive amount in each residue class modulo the smallest denomination, only these spectra of longest-to-shortest representation lengths can arise.

## Assumptions and scope
A numerical semigroup is a cofinite additive submonoid \(S\subseteq\mathbb N_0\); its multiplicity \(m\) is its smallest positive element and its embedding dimension \(e(S)\) is the number of its minimal positive additive generators (atoms). Its Apéry set is \(\operatorname{Ap}(S;m)=\{x\in S:x-m\notin S\}\), consisting of exactly one minimum in each residue modulo \(m\), including zero. Every factorization of \(x\) is an expression as a sum of atoms, repetitions allowed; \(L(x)\) denotes the finite set of its possible numbers of atoms. Set \(\rho(0)=1\) and \(\rho(x)=\max L(x)/\min L(x)\) for positive \(x\). Define \(\mathcal R(S)=\{\rho(x):x\in\operatorname{Ap}(S;m)\}\). No factorization of an Apéry element uses the atom \(m\).

## Proof
**1. Only three nonzero composite Apéry elements.** The Apéry set contains \(m-1\) nonzero elements, of which precisely \(e(S)-1=m-4\) are atoms. Thus exactly three nonzero elements of \(\operatorname{Ap}(S;m)\) are non-atoms. If \(x\in\operatorname{Ap}(S;m)\) and \(y\in S\) divides \(x\) additively (that is, \(x-y\in S\)), then \(y\) also lies in the Apéry set: otherwise \(y-m\in S\), which would imply \(x-m\in S\). Every partial sum in a factorization of \(x\) consequently belongs to the Apéry set. A factorization with \(k\) atoms gives \(k-1\) distinct non-atoms as its partial sums of sizes \(2,3,\ldots,k\); therefore \(k\le4\).

**2. A length-four factorization forces a single ladder.** Suppose \(x=a+b+c+d\), where all four terms are atoms. If \(b\ne c\), the four Apéry elements \(a+b\), \(a+c\), \(a+b+c\), \(x\) are pairwise distinct non-atoms: the pair sums are unequal; each is smaller than the triple sum; and the triple sum is smaller than \(x\). This contradicts the count three. Taking every choice of three of the four atoms shows that all four coincide. Hence \(x=4a\) and the three non-atom Apéry elements are exactly \(2a,3a,4a\). No factorization \(4a=u+v+w\) into three atoms can exist: each two-atom partial sum must be \(2a\) or \(3a\). From \(u+v\in\{2a,3a\}\), the case \(u+v=2a\) forces \(w=2a\), not an atom; the other case forces \(w=a\). Then \(u+w\) and \(v+w\) can only equal \(2a\), because equality \(3a\) would force one of \(u,v\) to be the nonatom \(2a\). Thus \(u=v=w=a\), giving \(3a\ne4a\), a contradiction. A length-two factorization of \(3a\) would, upon adding \(a\), induce the forbidden length-three factorization of \(4a\). Consequently the only possible nonunit elasticity when a length-four factorization exists is \(4/2=2\). If none exists, every length is at most three and the only possible nonunit elasticity is \(3/2\). This proves the universal three-option restriction.

**3. Explicit realization for every \(m\ge7\).** The following are finite generating sets of semigroups, and the lists give the Apéry minimum \(w_j\) at residue \(j\) for \(0\le j<m\), with \(w_0=0\). Every displayed generating set has exactly \(m-3\) atoms. The precise Apéry minima follow directly by reducing arbitrary nonnegative combinations of the displayed generators modulo \(m\): a generator of residue \(1\) can be repeated, while generators of residues \(j\ge5\) have the displayed costs; any sum of two higher-residue generators has cost at least the stated values and the only competitive wrap-around sums are identified below.

(a) Define
\[
S_m^{(1)}=\langle m,\ m+1,\ 4m+5,4m+6,\ldots,5m-1\rangle.
\]
Then \(w_j=j(m+1)\) for \(1\le j\le4\) and \(w_j=4m+j\) for \(5\le j<m\). Each minimum has a unique representation length (indeed each has a unique factorization), so \(\mathcal R(S_m^{(1)})=\{1\}\).

(b) Define
\[
S_m^{(3/2)}=\langle m,\ m+1,\ m+5,m+6,\ldots,2m-1\rangle.
\]
Then \(w_1=m+1\), \(w_2=2m+2\), \(w_3=3m+3\), \(w_4=3m+4\), and \(w_j=m+j\) for \(5\le j<m\). The amount \(w_3\) admits both three copies of \(m+1\) and two larger generators (for \(m=7\), two copies of \(m+5\)); the other Apéry minima have a unique length. Thus \(\mathcal R(S_m^{(3/2)})=\{1,3/2\}\).

(c) Define
\[
S_m^{(2)}=\langle m,\ m+1,\ 2m+5,2m+6,\ldots,3m-2,\ 2m-1\rangle.
\]
Then \(w_j=j(m+1)\) for \(1\le j\le4\); for \(5\le j\le m-2\), \(w_j=2m+j\); and \(w_{m-1}=2m-1\). The amount \(w_4=4m+4\) is both four copies of \(m+1\) and \((2m+5)+(2m-1)\). All other Apéry minima have a unique length, so \(\mathcal R(S_m^{(2)})=\{1,2\}\). These three families complete the classification.

**Apéry-minimum check for (a)–(c).** Each proposed \(w_j\) is exhibited by generators. For (a), a combination consisting only of \(m+1\) has minimum cost \(j(m+1)\), and any generator of residue at least five costs at least \(4m+5\); its addition to a positive generator or another high-residue generator cannot improve any listed minimum. For (b), high-residue generators cost \(m+j\). One such generator cannot represent residues one through four without at least one wrap-around of positive residues, which exceeds the displayed \(w_j\). Two high-residue generators of residues summing to \(m+3\) or \(m+4\) attain respectively \(3m+3\) and \(3m+4\), and otherwise cost more than the displayed minimum at the resulting residue; three such generators cost at least \(3m+15\). For (c), the special residue \(-1\) generator costs \(2m-1\); pairing it with the residue-five generator produces \(4m+4\) at residue four, the only tie with the low-residue ladder. Every other mixed pair or repeated high-residue term has cost at least its proposed residue minimum. Adding copies of \(m\) never improves a minimum. These comparisons hold for every \(m\ge7\); the included checker verifies the exact residues, atoms, and all factorization lengths independently for \(7\le m\le99\).

## Verification
Execute `python verify.py` using Python 3. The script builds the shortest-path Apéry minima modulo \(m\) and computes all available atomic representation lengths by dynamic programming for the three families and all \(7\le m\le99\). The script reports `VERIFICATION_OK` after 279 instances. The finite check confirms the constructions in its tested range; the general claim follows from the proof for all integers \(m\ge7\), not from finite enumeration.

## Relationship to prior work
Autry, Gomes, O'Neill and Ponomarenko, *Elasticity in Apéry Sets* (arXiv:1908.06448, first publicly posted 2019-08-18), Theorem 2.1, show the Apéry-half-factorial conclusion for \(e\ge m-1\) and state that for \(e=m-2\) the elasticity set is either \(\{1\}\) or \(\{1,3/2\}\). Their discussion explicitly leaves other near-maximal embedding dimensions open. Their general realization theorem for arbitrary two-element elasticity sets does not constrain or cover the present fixed embedding dimension. Their examples can imply individual cases, but the three-option exclusion and realization for every \(m\ge7\) are not given there. The proof here uses nonnegative integer linear representations of Apéry minima, relating semigroup factorization to the coin-change Diophantine problem.

## Limitations
The classification is for \(m\ge7\), \(e=m-3\), and **only Apéry-minimal amounts**, not elasticity of the whole numerical semigroup. It asserts no new classification for \(e\le m-4\). Earlier equivalent statements could exist in semigroup factorization literature not located in the searched material. Primary subject is the coin-change integer-representation problem; semigroup factorizations provide equivalent terminology.

## References
1. Jackson Autry, Tara Gomes, Christopher O'Neill, Vadim Ponomarenko, *Elasticity in Apéry Sets*, arXiv:1908.06448 (2019), https://arxiv.org/abs/1908.06448.
2. *On the Set of Elasticities in Numerical Monoids* (2017), discussed in Autry et al., arXiv:1908.06448; this addresses elasticities of complete semigroups rather than fixed near-maximal embedding dimension for Apéry minima.
