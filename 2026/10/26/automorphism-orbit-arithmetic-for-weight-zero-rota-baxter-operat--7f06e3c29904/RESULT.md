# Automorphism-orbit arithmetic for weight-zero Rota–Baxter operators on chain evolution algebras

## Finding

Let \(q=p^s\) be an odd prime power and \(n\ge 3\). Define the \(n\)-dimensional evolution algebra \(E_n\) over \(\mathbb F_q\) by a natural basis \(e_1,\ldots,e_n\), with \(e_i^2=e_{i+1}\) for \(1\le i<n\), \(e_n^2=0\), and \(e_i e_j=0\) for \(i\ne j\). A weight-zero Rota–Baxter operator is a linear map \(R:E_n\to E_n\) satisfying
\[
R(x)R(y)=R(R(x)y+xR(y))\quad(x,y\in E_n).
\]
Two operators are equivalent when conjugate by an algebra automorphism of \(E_n\). Write \(\mathcal O_n(q)\) for the number of equivalence classes.

Put \(L=2^{n-1}\) (as a positive integer), and \(w_i=L-2^{i-1}\) for \(1\le i<n\). For \(2\le k<n\), define
\[
B_k(q)=\frac1{q-1}\sum_{d\mid(q-1)}\varphi(d)q^{\#\{i:2\le i\le k,\ d\mid w_i\}},
\]
where \(\varphi\) is Euler's totient function, and define
\[
C_n(q)=\frac1{q-1}\sum_{d\mid(q-1)}\varphi(d)q^{\#\{i:1\le i<n,\ d\mid w_i\}}.
\]
Define the resonance factor
\[
T_n(q)=\begin{cases}1,&p\nmid (L-1),\\1+\gcd(L-1,q-1),&p\mid(L-1).\end{cases}
\]
Then the exact finite-field automorphism-orbit count is
\[
\boxed{\mathcal O_n(q)=(q-1)\left(T_n(q)+\sum_{k=2}^{n-1}B_k(q)+B_{n-1}(q)\right)+C_n(q).}
\]
In particular, an unexpectedly short all-dimension formula holds over the smallest odd field:
\[
\boxed{\mathcal O_n(3)=7\cdot3^{n-2}+(-1)^{n-1}.}
\]
There are exactly \(2q^n-q\) labelled weight-zero Rota–Baxter operators. The orbit formula detects the modular resonance \(p\mid(2^{n-1}-1)\), which changes the orbit geometry of the full-rank stratum.

## Assumptions and scope

The field has \(q=p^s\) elements with odd characteristic \(p\). Integers \(L,w_i,d\) in the divisor conditions are ordinary integers; the condition \(p\mid L-1\) refers to the field characteristic. Conjugation means \(R\mapsto\phi R\phi^{-1}\) with \(\phi\in\operatorname{Aut}_{\mathbb F_q}(E_n)\), not arbitrary similarity in the ambient matrix algebra. The displayed count is for the pure chain, without additional long-range structure constants. No analogous characteristic-two claim is made.

## Proof

**1. All operators have a small normal form, over every odd-characteristic field.** The basis squares \(e_1^2,\ldots,e_{n-1}^2\) are independent. Applying the Rota–Baxter equation to \((e_n,e_n)\) shows that \(R(e_n)^2=0\), and hence \(R(e_n)\in\mathbb F_q e_n\). Descending induction now shows that \(R(e_i)\in\operatorname{span}(e_i,\ldots,e_n)\): since \(R(e_i)^2=2r_{ii}R(e_{i+1})\), its components along \(e_2,\ldots,e_i\) vanish, forcing the coefficients of \(e_1,\ldots,e_{i-1}\) of \(R(e_i)\) to vanish.

Put \(d_i=r_{ii}\). The coefficient of \(e_{i+1}\) in the diagonal identity gives \(d_i^2=2d_id_{i+1}\) for \(i<n\). Suppose an internal off-diagonal coefficient \(r_{ji}\ne0\) occurs with \(i<j<n\). The coefficient of \(e_{j+1}\) in the identity for \((e_i,e_j)\) gives \(r_{ji}d_j=r_{ji}d_{j+1}\), so \(d_j=d_{j+1}\). Combined with \(d_j^2=2d_jd_{j+1}\), this implies \(d_j=0\). The diagonal recurrence forces \(d_i=0\), whence \(R(e_i)^2=0\). Independence of the basis squares then forces \(r_{ji}=0\), contradiction. Consequently
\[
R(e_i)=d_i e_i+b_i e_n\quad(i<n),\qquad R(e_n)=d_n e_n.
\]
The Rota–Baxter identity is now equivalent, by checking all ordered basis pairs, to
\[
d_i^2=2d_id_{i+1}\quad(1\le i<n),\qquad d_i b_{i+1}=0\quad(1\le i<n-1).
\]
All mixed-basis equations vanish identically. Because \(2\) is invertible, the solutions split disjointly into: (a) an annihilator-valued stratum, with \(d_1=\cdots=d_{n-1}=0\), arbitrary \(d_n\), and arbitrary \(b_1,\ldots,b_{n-1}\); and (b) threshold strata indexed by \(1\le k<n\), with \(d_1=\cdots=d_{k-1}=0\), \(d_k\in\mathbb F_q^\times\), \(d_j=2^{-(j-k)}d_k\) for \(j>k\), arbitrary \(b_1,\ldots,b_k\), and \(b_{k+1}=\cdots=b_{n-1}=0\). These strata contain respectively \(q^n\) and \((q-1)q^k\) operators. Summing gives \(q^n+(q-1)\sum_{k=1}^{n-1}q^k=2q^n-q\).

**2. The full automorphism group has two parameters.** The recursively defined annihilator filtration \(\operatorname{ann}_1(E_n)=\operatorname{ann}(E_n)\) and \(\operatorname{ann}_{j+1}(E_n)=\{x:xE_n\subseteq\operatorname{ann}_j(E_n)\}\) has terms \(\operatorname{span}(e_{n-j+1},\ldots,e_n)\); it is invariant under every algebra automorphism. Thus every automorphism is triangular. Its images of distinct natural basis vectors have disjoint nonannihilator coordinate supports, because their products vanish and the squares \(e_2,\ldots,e_n\) are independent. Nonzero diagonal entries then force \(\phi(e_i)=a_i e_i+t_i e_n\) for \(i<n\) and \(\phi(e_n)=a_n e_n\). Comparing \(\phi(e_i^2)\) with \(\phi(e_i)^2\) gives \(a_i=a^{2^{i-1}}\) for \(a=a_1\in\mathbb F_q^\times\), \(a_n=a^L\), and \(t_i=0\) for \(i\ge2\). Thus all automorphisms, and no others, are
\[
\phi_{a,t}(e_1)=ae_1+te_n,\quad \phi_{a,t}(e_i)=a^{2^{i-1}}e_i\ (2\le i\le n),
\]
with \(a\in\mathbb F_q^\times\), \(t\in\mathbb F_q\). In particular \(|\operatorname{Aut}(E_n)|=q(q-1)\).

**3. Compute the conjugation action exactly.** The diagonal entries \(d_i\) remain fixed under conjugation. For \(R\) in the displayed normal form, a direct substitution into \(\phi_{a,t}R\phi_{a,t}^{-1}\) gives
\[
b'_1=a^{w_1}b_1+\frac{d_1-d_n}{a}t,\qquad b'_i=a^{w_i}b_i\quad(2\le i<n).
\]
If \(d_1\ne d_n\), translations in \(t\) normalize \(b_1\) to zero, and the remaining equivalence is precisely simultaneous multiplication of each \(b_i\), \(i\ge2\), by \(a^{w_i}\). In a threshold stratum \(2\le k<n\), the surviving tuple is \((b_2,\ldots,b_k)\); there are \(q-1\) choices of the invariant \(d_k\). The annihilator-valued stratum with \(d_n\ne0\) likewise leaves \((b_2,\ldots,b_{n-1})\) and has \(q-1\) possible \(d_n\).

In the threshold \(k=1\) stratum, \(d_1/d_n=2^{n-1}=L\) interpreted in \(\mathbb F_q\). If \(p\nmid L-1\), translations act transitively on \(b_1\). If \(p\mid L-1\), translations vanish, and the multiplicative group acts on \(b_1\) by \(a^{L-1}\). This has one zero orbit and \(\gcd(L-1,q-1)\) nonzero orbits, since \(\mathbb F_q^\times\) is cyclic. Thus every fixed nonzero \(d_1\) contributes exactly \(T_n(q)\) orbits. Finally, in the annihilator-valued stratum with \(d_n=0\), the translation is absent and all \(b_1,\ldots,b_{n-1}\) transform with the respective weights \(w_i\).

**4. Count the remaining scalar orbits.** If a cyclic multiplicative group of size \(q-1\) acts on coordinates \((b_i)_{i\in I}\) by \(b_i\mapsto a^{w_i}b_i\), an element of multiplicative order \(d\mid(q-1)\) fixes exactly \(q^{\#\{i\in I:d\mid w_i\}}\) vectors. There are \(\varphi(d)\) elements of order \(d\). Burnside's lemma therefore gives the divisor sum defining \(B_k(q)\) for \(I=\{2,\ldots,k\}\), and \(C_n(q)\) for \(I=\{1,\ldots,n-1\}\). Combining the disjoint cases in Step 3 proves the boxed formula.

For \(q=3\), every \(w_i\) with \(i\ge2\) is even, while \(w_1=L-1\) is odd. Thus \(B_k(3)=3^{k-1}\) and \(C_n(3)=2\cdot3^{n-2}\). The characteristic-three resonance condition is equivalent to \(n\) being odd, so \(T_n(3)=2\) for odd \(n\) and \(T_n(3)=1\) for even \(n\). Substitution and summation of a geometric series prove \(\mathcal O_n(3)=7\cdot3^{n-2}+(-1)^{n-1}\).

## Verification

The accompanying standalone Python checker (`verify.py`) uses explicit finite-field coordinate multiplication and tests the Rota–Baxter identity on all ordered basis pairs for every operator in the claimed normal forms. It also constructs conjugation orbits from every automorphism parameter and independently compares their number with the divisor-sum formula. Tested prime-field pairs are \((n,q)=(3,3),(3,5),(4,3),(4,5),(5,3),(5,5),(4,7),(5,7)\). In the \((3,3)\) case it additionally exhausts all \(3^9\) linear maps, proving equality with the parametrized family in that instance. The obtained orbit counts, in the same order, are \(22,36,62,176,190,880,376,2054\). All runs return `VERIFY_OK` or the indicated exhaustive success marker. Computations check finite instances; Steps 1–4 prove the statement for all odd prime powers and all \(n\ge3\).

Reproduce from the directory containing the file with `python3 verify.py` (standard library only). The checker uses ordinary modular arithmetic, so its enumerated fields are prime fields; extension fields are covered by the symbolic proof, not by those tests.

## Relationship to prior work

Qaralleh–Mukhamedov–Khakimov classified weight-zero and weight-one Rota–Baxter operators on maximal-nilindex evolution algebras in characteristic zero (arXiv:2601.08669, first posted January 13, 2026), providing the characteristic-zero normal-form context. Mukhamedov–Khakimov–Omirov–Qaralleh classified automorphisms of such algebras (arXiv:1805.10285, 2018). Qaralleh–Mukhamedov–Khakimov later studied local operators and the *commuting* conditions for individual automorphisms (arXiv:2606.22623, first posted June 21, 2026). Those sources are credited; the present result changes the question to complete finite-field conjugacy-orbit moduli and proves the result independently in every odd characteristic. The pointwise commutant equations in the later paper provide potentially strong ingredients for an alternative derivation, but do not explicitly give the orbit arithmetic or the characteristic-dependent count stated here.

## Limitations

No characteristic-two classification, weight-one orbit formula, or classification for arbitrary maximal-nilindex evolution algebras with long-range structure constants is proved. The exact divisor sums may be expensive to evaluate for very large \(n\) and \(q\), but are finite and unambiguous. Prior results on individual automorphisms and operator normal forms make implicit earlier derivations possible; originality is assessed relative to the inspected sources and is not a proof of uniqueness in all literature. The finite computational checks are supplementary and have no bearing on cases outside the enumerated prime fields.

## References

1. I. Qaralleh, F. Mukhamedov, O. Khakimov, *Rota-Baxter operators of nilpotent evolution algebras with maximal nilindex*, arXiv:2601.08669 (first posted January 13, 2026), https://arxiv.org/abs/2601.08669.
2. I. Qaralleh, F. Mukhamedov, O. Khakimov, *Local Rota--Baxter operators of weight zero on nilpotent evolution algebras with maximal nilindex*, arXiv:2606.22623 (first posted June 21, 2026), https://arxiv.org/abs/2606.22623.
3. F. Mukhamedov, O. Khakimov, B. Omirov, I. Qaralleh, *Derivations and automorphisms of nilpotent evolution algebras with maximal nilindex*, arXiv:1805.10285 (first posted May 25, 2018), https://arxiv.org/abs/1805.10285.
