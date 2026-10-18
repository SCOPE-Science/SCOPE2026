# Necklace-support spectra and inverse rigidity for finite Boolean dynamical algebras

## Finding
**Theorem (complete quantifier-free spectrum, homogeneity threshold, and inverse classification).** For integers \(d,m\geq1\), let \(X\) consist of \(m\) disjoint cycles, each of length \(d\), and let \(\sigma\) be the automorphism of the nontrivial Boolean algebra \(B=\mathcal P(X)\) induced by rotating all cycles by one step. Work in the language \(\{0,1,\wedge,\vee,\neg,\sigma\}\), and let \(T_k(d,m)\) be the number of complete quantifier-free types realized by ordered \(k\)-tuples of elements of \(B\), for \(k\geq1\). Set \(q=2^k\) and
\[
N_d(q)=\frac1d\sum_{r\mid d}\varphi(r)q^{d/r},
\]
where \(\varphi\) is Euler's totient function (so \(N_d(q)\) counts length-\(d\) necklaces over a \(q\)-letter alphabet). Then
\[
\boxed{T_k(d,m)=\sum_{j=1}^{\min(m,N_d(2^k))}\binom{N_d(2^k)}{j}.}
\]
The number of distinct parameter-free quantifier-free definable \(k\)-ary relations on \(B\) is exactly \(2^{T_k(d,m)}\). The number of \(\operatorname{Aut}(B,\sigma)\)-orbits of ordered \(k\)-tuples is
\[
\boxed{O_k(d,m)=\binom{N_d(2^k)+m-1}{m}.}
\]
In **every positive arity**, every automorphism-invariant relation is quantifier-free definable exactly when \(m\leq2\). If \(m\geq3\), already an invariant unary relation fails to be quantifier-free definable.

Among all systems with uniform-length atom cycles, equality \(T_k(d,m)=T_k(d',m')\) for **every** \(k\geq1\) implies \((d,m)=(d',m')\), with precisely one exceptional unordered pair:
\[
\boxed{\{(d,m),(d',m')\}=\{(1,2),(2,1)\}.}
\]
For this pair both numerical spectra are \(T_k=(2^{2k}+2^k)/2\), although the Boolean algebras with named automorphism are not isomorphic. The collision is numerical only: it does **not** assert that the realized syntactic types or quantifier-free formulas agree between the two algebras.

## Assumptions and scope
The Boolean algebra is the full powerset algebra of \(md\) nonempty atoms; the named operation is a Boolean automorphism whose atom permutation has precisely \(m\) cycles, each of the same positive length \(d\). Constants and Boolean negation are part of the language, formulas are parameter-free, and an invariant relation means a union of orbits under automorphisms that commute with \(\sigma\). Tuples are ordered, and arity is positive. Mixed cycle lengths, infinite atom spaces, and quantifier-bearing definability are not covered.

For a tuple \(\mathbf a=(A_1,\ldots,A_k)\in B^k\), color each atom \(x\in X\) by its binary membership vector \((\mathbf1_{x\in A_1},\ldots,\mathbf1_{x\in A_k})\in\{0,1\}^k\). Each atom-cycle acquires a length-\(d\) word over \(q=2^k\) colors, well-defined up to cyclic rotation. Let \(S(\mathbf a)\) be the **set**, rather than the multiset, of necklaces appearing on the \(m\) atom cycles.

## Proof
**Step 1: quantifier-free types are exactly necklace supports.** Every term in the language is a Boolean combination of \(\sigma^s(A_i)\) for \(0\leq s<d\), because \(\sigma^d=\mathrm{id}\) and \(\sigma\) preserves Boolean operations. At an atom \(x\), evaluation of such a term depends only on the periodic color word read around its \(d\)-cycle from \(x\). Hence an equation between two terms holds as an equality of subsets of \(X\) exactly when it holds for every phase of every necklace in \(S(\mathbf a)\). Therefore equal supports imply equal complete quantifier-free types.

Conversely, let \(w=(w_0,\ldots,w_{d-1})\) be a word of \(d\) binary \(k\)-colors. Define a Boolean term
\[
e_w(\mathbf A)=\bigwedge_{s=0}^{d-1}\ \bigwedge_{i=1}^{k}
\begin{cases}
\sigma^s(A_i),&\text{if the \(i\)-th bit of \(w_s\) is \(1\)},\\
\neg\sigma^s(A_i),&\text{otherwise.}
\end{cases}
\]
At an atom \(x\), membership in \(e_w(\mathbf a)\) holds if and only if the clockwise/reverse-clockwise conventionally oriented word starting at \(x\) is \(w\). Consequently the atomic formula \(e_w(\mathbf a)=0\) holds exactly when the necklace of \(w\) is **absent** from \(S(\mathbf a)\). Every differing support is distinguished by such an atomic formula. This proves the type classification. The orientation convention is fixed by \(x\in\sigma^s(A_i)\iff\sigma^{-s}(x)\in A_i\); rotation of starting point does not reverse orientation.

**Step 2: exact counts.** Burnside's lemma for rotations of length \(d\) gives \(N_d(q)=d^{-1}\sum_{r\mid d}\varphi(r)q^{d/r}\). Every nonempty set of at most \(m\) such necklace types occurs as a support: assign one necklace to each of its members on distinct cycles, and use any one of those types to fill the remaining cycles. Thus the number of supports, hence realized complete quantifier-free types, is the asserted truncated binomial sum. Because the tuple set is finite, each type is isolated by a finite conjunction of atomic or negated atomic formulas, and arbitrary unions of types are quantifier-free definable. Hence there are \(2^{T_k(d,m)}\) definable relations.

An automorphism of \((B,\sigma)\) is exactly a permutation of atoms commuting with the given cycle permutation. It independently rotates each of the \(m\) cycles and permutes the cycles, giving the wreath product \(C_d\wr S_m\). Its orbits on tuples are classified by **multisets** of \(m\) necklaces. Stars-and-bars yields \(O_k(d,m)=\binom{N_d(q)+m-1}{m}\). For \(m=1,2\), a support uniquely determines this multiset, so automorphism orbits and quantifier-free type classes agree. For \(m\geq3\), use two distinct necklace types (e.g. constant-zero and constant-one words): multiplicities \((1,m-1)\) and \((2,m-2)\) give different automorphism orbits with identical support. Thus already for \(k=1\) an invariant orbit relation is not quantifier-free definable.

**Step 3: inverse rigidity.** The necklace polynomial \(N_d(q)\) has degree \(d\) and leading coefficient \(1/d\). Therefore, for fixed \(d,m\) and \(k\to\infty\),
\[
T_k(d,m)=\frac{2^{kdm}}{d^m m!}+O(2^{k(dm-1)}).
\]
In particular, the spectrum determines \(n=dm\) and \(c=(d^m m!)^{-1}\) from
\[
n=\lim_{k\to\infty}\frac{\log_2 T_k}{k},\qquad
c=\lim_{k\to\infty}2^{-kn}T_k.
\]
At a fixed positive integer \(n\), write \(d=n/m\). The reciprocal leading coefficient is \(F_n(m)=(n/m)^m m!\). For successive integers \(m\),
\[
\frac{F_n(m+1)}{F_n(m)}=n\left(\frac m{m+1}\right)^m.
\]
For \(n\geq3\), this exceeds \(n/e\geq3/e>1\). Thus \(F_n(m)\) is strictly increasing, including when restricted to divisors \(m\mid n\), and the pair \((d,m)\) is uniquely determined. When \(n=1\), only \((1,1)\) exists. When \(n=2\), the possible pairs \((1,2)\) and \((2,1)\) both have leading coefficient \(1/2\), and their *entire* formulas agree:
\[
\sum_{j=1}^{2}\binom{2^k}{j}
=\frac{2^{2k}+2^k}{2}
=N_2(2^k).
\]
This proves the unique numerical collision.

## Verification
The standalone `verify.py` computes realized Boolean minterm signatures directly on every atom, compares these with independent necklace-support and orbit-multiset descriptions, and checks exact counts for 26 small parameter/arity cases (77,230 tuples). Separately, direct enumeration of permutations in \(C_d\wr S_m\) and Burnside averaging confirms the automorphism-orbit counts in 26 cases. Exhaustion of uniform cycle parameters with at most eight atoms checks that the two-atom pair is the sole collision in this finite range. These are corroborative finite computations: the proof above establishes the all-parameter and all-arity statements.

To reproduce, run `python3 verify.py` with Python's standard library; expected output begins with `VERIFY_OK independent_minterm_assignments=77230`.

## Relationship to prior work
Campercholi, Tellechea, and Ventura (2023) characterize quantifier-free definability on finite algebras via isomorphisms of generated substructures and provide general algorithms. The present result specializes the general question to a natural cyclic Boolean-automorphism class but goes beyond decision procedures: it obtains a closed necklace-support spectrum, an exact automorphism-invariance threshold, and an all-arity inverse classification with a unique collision.

Areces, Campercholi, Penazzi, and Ventura (2019) study quantifier-free definability complexity for finite relational structures; their general problem framing does not determine the cyclic Boolean-algebra spectra. Separate work on orbit-supports of countable filtered Boolean powers treats a different, atomless structure and automorphism-orbit counts, not quantifier-free types of these finite dynamical Boolean algebras. A known finite-Boolean-algebra quantifier-rank threshold concerns quantified sentences of the **unexpanded** Boolean language; it does not imply the uniform-cycle inverse theorem. Burnside's necklace formula is classical and is not itself claimed as original.

## Limitations
The theorem concerns only uniform-length atom cycles, not arbitrary cycle mixtures. It classifies numerical quantifier-free type counts; equal numerical spectra need not mean equality of realized syntactic types or logical equivalence. Its originality assessment compares pertinent accessible primary text and mathematical records but cannot exclude unindexed equivalent work or folklore. No outside independent validation or publication-priority certification is claimed.

## References
1. M. Campercholi, M. Tellechea and P. Ventura, *Two algorithms to decide Quantifier-free Definability in Finite Algebraic Structures*, arXiv:2303.17017, first posted 2023-03-29, https://arxiv.org/abs/2303.17017.
2. C. Areces, M. Campercholi, D. Penazzi and P. Ventura, *The Complexity of Definability by Open First-Order Formulas*, arXiv:1904.04637, first posted 2019-04-09, https://arxiv.org/abs/1904.04637.
3. G. Pólya and R. C. Read, *Combinatorial Enumeration of Groups, Graphs, and Chemical Compounds*, Springer, 1987 (classical Burnside/necklace counting reference).
