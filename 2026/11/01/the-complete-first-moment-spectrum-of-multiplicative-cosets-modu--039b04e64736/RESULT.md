# The complete first-moment spectrum of multiplicative cosets modulo powers of two

## Finding

For each integer \(a\ge 2\), set \(m=2^a\) and \(G=(\mathbb Z/m\mathbb Z)^\times\). If \(H\le G\) and \(C=uH\) is a multiplicative coset, let \(h=|H|\) and define its *centered residue-sum defect*
\[
\Delta(C)=\sum_{x\in C}\langle x\rangle_m-\frac{mh}{2},
\]
where \(\langle x\rangle_m\in\{1,\ldots,m-1\}\) is the least positive representative.

**Theorem (complete dyadic coset-moment spectrum).** Every subgroup belongs to exactly one of the following types.

1. If \(-1\in H\), then every coset has \(\Delta(C)=0\).
2. Otherwise, for a unique \(j\) with \(0\le j\le a-2\), put \(h=2^j\) and \(L=m/h\). In the *unsigned type* \(H=U_j=\{x\in G:x\equiv1\pmod L\}\), the multiset of defects, one per coset, is
   \[
   \{\Delta(C):C\in G/H\}_{\mathrm{multi}}
   =\{h(r-L/2):r=1,3,\ldots,L-1\}.
   \]
   In particular it consists of distinct odd multiples of \(h\) ranging from \(-(m/2-h)\) through \(m/2-h\).
3. Otherwise, \(1\le j\le a-2\), \(h=2^j\), \(L=m/h\), and \(H=V_j=\langle-5^{2^{a-2-j}}\rangle\). In this *signed type*, the multiset consists of exactly \(L/4\) copies each of \(-m/2\) and \(+m/2\).

Consequently, for **every** multiplicative subgroup of \(G\), the following are equivalent: some coset has centered residue sum; every coset has centered residue sum; and \(-1\in H\). Moreover, the classical *half-interval balance* condition (every coset has equally many representatives in \((0,m/2)\) and \((m/2,m)\)) holds exactly when \(-1\in H\) or \(1+m/2\in H\). Hence, at dyadic moduli, half-interval balance need not imply centered first moments.

## Assumptions and scope

All assertions are exact for every integer \(a\ge2\), without restrictions on the index, generator, or coset. The sum includes each distinct member of a coset once; it is not a sum over repeated powers or over nonunits. The multiset records one defect for each distinct multiplicative coset, not for each coset representative. When \(j=0\), the unsigned subgroup is \(U_0=\{1\}\); the signed type does not exist. The identity \(L=m/h\ge4\) holds in both noncentral types.

## Proof

**1. Exhaustion of subgroups.** The familiar dyadic unit-group decomposition is
\[
G=\langle-1\rangle\times\langle5\rangle,
\qquad |\langle5\rangle|=2^{a-2}.
\]
For completeness, the order formula follows from \(\nu_2(5^{2^k}-1)=k+2\), proved by induction: \(5-1=4\); squaring a number congruent to \(1\pmod4\) raises the valuation of its difference from one by exactly one. Thus \(5\) generates all units congruent to \(1\pmod4\), and every odd residue is uniquely \(\pm5^s\).

If \(-1\notin H\), projection of \(H\) onto \(\langle5\rangle\) is injective. Its image is the unique subgroup of order \(h=2^j\), for some \(0\le j\le a-2\). The subgroup \(H\) is the graph of a homomorphism from that cyclic image to \(\{\pm1\}\). For \(j=0\) only the trivial homomorphism exists. For \(j\ge1\) there are exactly two: the trivial map and the nontrivial sign map. They give precisely \(U_j\) and \(V_j\) as stated. In the trivial case, \(U_j\) has order \(h\), and since \(5^{2^{a-2-j}}\equiv1\pmod L\), cardinality identifies it with all the units congruent to one modulo \(L\). In the nontrivial case the generator is the negative of that power of five.

**2. Unsigned-type spectrum.** Fix \(U_j\). Every coset is indexed uniquely by an odd \(r\in\{1,3,\ldots,L-1\}\), and its least positive representatives are
\[
  r,\; r+L,\;r+2L,\;\ldots,\;r+(h-1)L.
\]
Therefore
\[
\sum_{x\in rU_j}\langle x\rangle_m=hr+\frac{Lh(h-1)}2,
\qquad
\Delta(rU_j)=h(r-L/2).
\]
Since \(L\ge4\) is divisible by four, \(r\) is odd and \(L/2\) even. Consequently none of these differences vanishes; the displayed values are distinct and exhaust all \(L/2\) cosets.

**3. Signed-type spectrum.** Fix \(V_j\), where \(j\ge1\). Again write \(h=2^j\), \(L=m/h\), and \(g=5^{2^{a-2-j}}\). The exact valuation \(\nu_2(g-1)=a-j\) gives
\[
 g\equiv1+L\pmod{2L},\qquad -g\equiv L-1\pmod{2L}.
\]
Furthermore,
\[
V_j=U_{j-1}\;\sqcup\;(-g)U_{j-1},
\qquad U_{j-1}=\{x\in G:x\equiv1\pmod{2L}\}.
\]
For a coset represented by an odd \(u\), let \(r\in\{1,3,\ldots,2L-1\}\) represent \(u\pmod{2L}\). Its two constituent arithmetic progressions, each of length \(h/2\) and step \(2L\), begin at \(r\) and the odd residue \(r'\equiv L-r\pmod{2L}\). Exactly one of
\[
r+r'=L\quad\text{or}\quad r+r'=3L
\]
holds; the former occurs if \(r<L\), the latter if \(r>L\). Summing both progressions and subtracting \(mh/2\) gives
\[
\Delta(uV_j)=\frac h2(r+r'-2L)
=\begin{cases}-m/2,&r<L,\\+m/2,&r>L.\end{cases}
\]
There are \(L/2\) cosets altogether. Within either half of \(\{1,3,\ldots,2L-1\}\), the involution \(r\mapsto r'\) partitions its \(L/2\) odd residues into \(L/4\) distinct cosets. Thus each sign occurs with multiplicity \(L/4\); in particular no defect vanishes.

**4. Central subgroups.** If \(-1\in H\), the fixed-point-free involution \(x\mapsto-x\) pairs every coset into \(h/2\) pairs whose representatives sum to \(m\). This gives \(\Delta(C)=0\) for all cosets. The other cases prove the equivalences concerning centered first moments.

**5. Half-interval balance and separation.** A subgroup containing either \(-1\) or \(1+m/2\) has half-interval balance in every coset: multiplication by either involution exchanges the two open halves, and has no fixed points on the units. Conversely, a subgroup without \(-1\) is one of the two types above. For \(U_j\) with \(j\ge1\), its unique involution is \(1+m/2\), so it is half-interval balanced; for \(U_0\) the singleton identity coset is not. For \(V_j\) with \(j\ge2\), its unique involution is again \(1+m/2\) and it is half-interval balanced. For \(V_1\), its identity coset consists of \(1\) and \(m/2-1\), both below \(m/2\), so it is not balanced. This exhausts the cases and proves the final criterion.

## Verification

The included standalone `verify.py` uses exact integer arithmetic only. It independently enumerates all multiplicative subgroups of \((\mathbb Z/2^a\mathbb Z)^\times\), every coset, their exact centered sums, and their half-interval cardinalities, for \(2\le a\le10\). It checks the formula including all signs and multiplicities and the half-interval classification. A successful execution reports 126 subgroups and 4043 cosets checked. Those checks corroborate the formulas in finite ranges but are not a proof of the theorem for all \(a\); the proof above handles the unrestricted quantifiers.

For a concrete contrast, modulo \(16\), \(H=\{1,9\}\) is half-interval balanced, while its coset defects, in increasing order, are \(-6,-2,2,6\). Thus not even one coset has centered first moment. A different behavior occurs for \(V_2=\langle-5\rangle=\{1,3,9,11\}\) modulo \(16\): its two coset defects are \(-8,+8\), illustrating the rigid signed-type spectrum.

## Relationship to prior work

Ma, Merca and Zhang investigate centered sums of multiplicative subgroups modulo a product of *two distinct odd primes* and compare that notion with half-interval balance; their article supplies the immediate motivation for understanding the missing dyadic endpoint. Their character expansion and the earlier general half-interval treatment do not state the two explicit dyadic coset spectra established here. Pomerance and Ulmer introduced the half-interval notion, including the known sufficient symmetries \(-1\) and \(1+m/2\); the present theorem determines the precise difference between that notion and first-moment balance in every dyadic subgroup. Girstmair's work studies residue-distribution and moment vectors more generally; a prior implicit derivation via that general framework cannot be excluded.

## Limitations

The theorem is restricted to moduli that are powers of two and to multiplicative subgroups of the unit group. It makes no analogous universal assertion for general even composite moduli or for additive cosets. It gives first moments but does not estimate higher moments, discrepancy of incomplete sums, or computational complexity beyond the explicit formulas. The dyadic group decomposition and valuation identity are standard; the contribution claimed is the complete explicit two-type coset spectrum and its balance distinction, not those ingredients.

## References

1. H. Ma, M. Merca and W. Zhang, *Residue Sums Modulo Products of Two Distinct Odd Primes*, arXiv:2610.29608v1, first posted 21 October 2026, https://arxiv.org/html/2610.29608v1 .
2. C. Pomerance and D. Ulmer, *On balanced subgroups of the multiplicative group*, arXiv:1204.6705v1, 2012, https://arxiv.org/pdf/1204.6705 .
3. K. Girstmair, *Power residues, digit expansions, and relative class numbers*, Surveys in Mathematics and its Applications 21 (2026), pp. 157–176, https://www.utgjiu.ro/math/sma/v21/p21_06.pdf .
4. K. Girstmair, *Class number factors and distribution of residues*, Abh. Math. Sem. Univ. Hamburg 67 (1997), pp. 65–104, DOI:10.1007/BF02940820 (bibliographic record and abstract consulted; full text not inspected).
