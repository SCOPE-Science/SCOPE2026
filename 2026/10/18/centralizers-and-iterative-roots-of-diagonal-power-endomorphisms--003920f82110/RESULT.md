# Centralizers and iterative roots of diagonal power endomorphisms of free semigroups

## Finding

Fix a finite alphabet \(\Sigma=\{a_1,\ldots,a_n\}\), where \(n\ge1\), and positive integers \(N_1,\ldots,N_n\). On the free semigroup of nonempty words \(\Sigma^+\), define the diagonal power endomorphism
\[
\Phi(a_i)=a_i^{N_i}.
\]
All endomorphisms in this note are nonerasing. Put \(\Sigma_m=\{a_i:N_i=m\}\) and \(t_m=|\Sigma_m|\); only nonempty level sets are used.

**Centralizer theorem.** The condition \(\Psi\Phi=\Phi\Psi\) holds if and only if, independently for each generator \(a_i\),
\[
\Psi(a_i)\in
\begin{cases}
\Sigma_1^+,&N_i=1,\\
\{a_j^{e}:N_j=N_i,\ e\ge1\},&N_i>1.
\end{cases}
\]
In particular, the full centralizer decomposes levelwise into an unrestricted free-semigroup endomorphism monoid on the exponent-one letters and weighted full transformation monoids on every exponent level greater than one. No assumption of monomial images is imposed in advance.

**Iterative-root theorem.** For every \(k\ge1\), the equation \(\Psi^{\circ k}=\Phi\) has exactly the solutions
\[
\Psi(a_i)=a_{\pi(i)}^{e_i},\qquad e_i\ge1,
\]
where \(\pi\) is a permutation of the letters preserving every level \(\Sigma_m\), and each cycle \(C\) of \(\pi\), of length \(d\), satisfies
\[
d\mid k,\qquad\left(\prod_{i\in C}e_i\right)^{k/d}=m
\quad\text{if }C\subseteq\Sigma_m.
\]
Conversely, these conditions imply \(\Psi^{\circ k}=\Phi\).

For positive integers \(d,s\), let \(D_d(s)\) count ordered positive integer factorizations of \(s\) into \(d\) factors. Explicitly, writing the prime factorization as \(s=\prod_p p^{v_p}\),
\[
D_d(s)=\prod_{p^{v_p}\parallel s}\binom{v_p+d-1}{d-1},\qquad D_d(1)=1.
\]
Define
\[
c_d(m,k)=\begin{cases}
D_d(s),&d\mid k\text{ and }m=s^{k/d}\text{ for an integer }s\ge1,\\
0,&\text{otherwise}.
\end{cases}
\]
There are exactly
\[
\boxed{R_k(\mathbf N)=\prod_{m:t_m>0}t_m!\,[z^{t_m}]
\exp\!\left(\sum_{d\mid k}\frac{c_d(m,k)}d z^d\right)}
\]
iterative roots. This uses a formal exponential series; only degrees at most \(t_m\) enter the coefficient. The number is finite despite the infinitude of the ambient endomorphism monoid.

For example, when \(k=2\) and all \(n\) exponents equal a nonsquare positive integer \(m\), only \(2\)-cycles are allowed. The root count is zero for odd \(n\) and
\[
\frac{n!}{2^{n/2}(n/2)!}\,\tau(m)^{n/2}
\]
for even \(n\), where \(\tau(m)=D_2(m)\) is the positive-divisor count. If \(m\) is square, fixed points are also allowed; then the count is
\[
n!\sum_{j=0}^{\lfloor n/2\rfloor}
\frac{\tau(m)^j}{2^j j!(n-2j)!}.
\]
Thus \((n,m,k)=(2,2,2),(3,4,2),(4,6,2),(3,8,3)\) have respectively \(2,10,48,21\) roots.

## Assumptions and scope

The alphabet is finite and nonempty; every \(N_i\) and every factor exponent is a *positive integer*. There are no erasing morphisms and no empty generator images. Composition is function composition, \(\Psi^{\circ k}\) means the \(k\)-fold composition of \(\Psi\) with itself, and \(\Phi\) is the specified diagonal power morphism. In the centralizer theorem \(\Psi\) is completely unrestricted subject to being a nonerasing endomorphism; for the root theorem \(k\) is an arbitrary positive integer. The formulas count *distinct endomorphisms on the fixed labeled alphabet*, not conjugacy classes.

## Proof

**1. Word-run rigidity.** For a nonempty word \(w\), let \(r(w)\) be its number of maximal constant-letter runs. Because each \(N_i\ge1\), substituting \(a_i\mapsto a_i^{N_i}\) preserves all run boundaries: \(r(\Phi(w))=r(w)\). If the first and last letters of \(w\) differ, \(r(w^h)=h r(w)\). If they agree, \(r(w^h)=h r(w)-(h-1)\). Hence, whenever \(h>1\) and \(r(w)>1\), \(r(w^h)>r(w)\). This is a word-level statement, not an argument from an incidence matrix.

**2. Exact centralizer.** Write \(w_i=\Psi(a_i)\). Commutation on a generator is equivalent to
\[
\Phi(w_i)=\Psi(a_i^{N_i})=w_i^{N_i}.
\]
For \(N_i>1\), step 1 forces \(r(w_i)=1\), so \(w_i=a_j^{e_i}\). Equality of exponents yields \(N_j=N_i\). If \(N_i=1\), then \(\Phi(w_i)=w_i\). Since \(\Phi\) does not shorten words, equality of lengths forces all letters in \(w_i\) to have power exponent one, exactly \(w_i\in\Sigma_1^+\). Conversely, substituting any of the stated images into the displayed equality proves commutation. The generator equations suffice because both maps are endomorphisms.

**3. Rigidity of an iterative root.** Suppose \(\Psi^{\circ k}=\Phi\). The morphism \(\Psi\) commutes with its own power \(\Phi\), so step 2 applies. On the letters in \(\Sigma_1\), the equality \(\Psi^{\circ k}(a_i)=a_i\) forces \(|\Psi(a_i)|=1\): lengths cannot decrease under any nonerasing endomorphism. Hence these letters also have monomial images, with weight one. For every exponent level \(m\), the resulting underlying letter map \(f:\Sigma_m\to\Sigma_m\) satisfies \(f^{\circ k}=\mathrm{id}\), because \(\Psi^{\circ k}(a_i)=a_i^m\). Thus \(f\) is a permutation \(\pi\) and every cycle has length \(d\mid k\). Iteration around a cycle multiplies its positive weights, so \(\Psi^{\circ k}(a_i)\) has exponent \((\prod_{j\in C}e_j)^{k/d}\). It equals \(a_i^m\) if and only if the cycle equation in the statement holds. This proves necessity and sufficiency.

**4. Counting cycles.** For a labeled \(d\)-cycle in exponent level \(m\), the cycle condition is feasible precisely when \(m\) is a positive integer \((k/d)\)-th power \(s\); its weights form ordered factorizations of \(s\). For each prime-power factor \(p^{v_p}\) of \(s\), stars-and-bars allocates its exponent among the \(d\) weights in \(\binom{v_p+d-1}{d-1}\) ways. Therefore the exact multiplicity per cycle is \(c_d(m,k)\). The labeled cycle-index formula for permutations, with weight \(c_d\) per \(d\)-cycle, is
\[
t_m!\,[z^{t_m}]\exp\!\left(\sum_{d\mid k}\frac{c_d(m,k)}d z^d\right).
\]
Distinct exponent levels cannot mix and contribute independently, giving the product. The special square-root formulas result by restricting to the allowed cycle sizes one and two; a fixed point contributes one choice of its integer square-root weight, whereas a transposition contributes \(D_2(m)=\tau(m)\) choices. This completes the proof.

## Verification

Run `python3 verify.py` with an ordinary Python 3 interpreter. The provided program enumerates **all** nonerasing word-morphisms with generator-image lengths at most four on two letters (\(900\) morphisms), and lengths at most three on three letters (\(59{,}319\) morphisms). It tests every diagonal target profile with entries respectively from one through four (\(16\) profiles) and one through three (\(27\) profiles), for iteration exponents two and three. It also tests exact centralizer membership on \(196\) two-letter morphisms across six profiles and \(1{,}728\) three-letter morphisms across five profiles, compares independent permutation enumeration with the weighted-cycle recurrence, and checks the four explicit counts \(2,10,48,21\). All checks passed. For those target profiles, the finite image-length cutoffs are exhaustive: a nonerasing morphism cannot reduce the length of a generator image under iteration. No finite experiment is used as a substitute for the all-parameter proof.

## Relationship to prior work

Bell, Foster and Reidenbach [1] examine irreducibility, factorization and commutation of arbitrary endomorphisms of finitely generated free semigroups. Their Section 4 gives sufficient commutativity conditions and notes the difficulty of general commutation; the present statement concerns the *complete* centralizer of a particular diagonal-power family, and then solves its iterative-root equation exactly. Honkala [2] gives a full commutation treatment for **upper triangular binary** free-monoid morphisms; in particular, his Example 4.1 already exhibits commuting diagonal power morphisms for any alphabet, and binary cases of the present centralizer can be consequences of his characterization. The present theorem adds an all-alphabet necessary-and-sufficient centralizer description, and an exact enumeration of every compositional root over every positive integer exponent profile. Petrich [3] studies monogenic endomorphisms whose ranges lie in a single cyclic word submonoid; this is not the multiple-generator diagonal-power centralizer studied here. Weighted-cycle enumeration uses classical permutation cycle-index and integer-factorization facts; those tools themselves are not claimed as novel.

## Limitations

The findings concern the specific family \(a_i\mapsto a_i^{N_i}\), not the centralizer of arbitrary substitutions. They require nonerasing morphisms; permitting images of empty words changes the problem. The formula counts labeled roots, not roots modulo relabeling. The result has received a self-review only; no independent audit is claimed. A mathematically equivalent description may exist in literature on monoid centralizers, nonnegative monomial matrix roots, or combinatorics on words that is not captured by the inspected sources. In particular, the binary restriction is closely related to Honkala's preceding characterization and is not asserted to be wholly unprecedented.

## References

[1] Paul C. Bell, Eva Foster and Daniel Reidenbach, *Irreducibility of Endomorphisms of Finitely Generated Free Semigroups*, arXiv:2603.15177, first submitted March 16, 2026, version 3 revised July 15, 2026. https://arxiv.org/abs/2603.15177 .

[2] Juha Honkala, *Commuting Upper Triangular Binary Morphisms*, Fundamenta Informaticae **191** (2024), 285–298; arXiv:2302.06158, https://arxiv.org/abs/2302.06158 .

[3] Mario Petrich, *Monogenic endomorphisms of a free monoid*, Glasgow Mathematical Journal **31** (1989), 87–101; https://doi.org/10.1017/S0017089500007588 .
