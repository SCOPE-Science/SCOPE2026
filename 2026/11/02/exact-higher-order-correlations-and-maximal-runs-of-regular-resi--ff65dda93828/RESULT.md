# Exact higher-order correlations and maximal runs of regular residues

## Finding

An integer \(z\) is **regular modulo \(n\)** if some integer \(y\) satisfies \(z^2y\equiv z\pmod n\). For an integer \(n\ge2\) and a nonempty finite set \(H\subset\mathbb Z\), count simultaneous regular translates by
\[
C_n(H)=\#\{x\bmod n:\ x+h\text{ is regular modulo }n\text{ for every }h\in H\}.
\]
For a prime power \(p^a\Vert n\), let \(r_p(H)\) be the number of residue classes modulo \(p\) represented by \(H\). Let \(t_{p,a}(H)\) be the number of represented classes \(c\bmod p\) for which all elements of \(H\) congruent to \(c\bmod p\) are also mutually congruent modulo \(p^a\). Then, for **every** \(n\ge2\) and every nonempty finite \(H\),
\[
\boxed{C_n(H)=\prod_{p^a\Vert n}\left((p-r_p(H))p^{a-1}+t_{p,a}(H)\right).}
\tag{1}
\]
Here and below, \(p^a\Vert n\) means that \(p^a\) is the full power of \(p\) dividing \(n\). This is an exact simultaneous-shift counting law, including colliding shifts, negative offsets, arbitrary patterns, and arbitrary prime exponents.

For the interval \(H_L=\{0,1,\ldots,L-1\}\) with integer \(L\ge1\), put \(B_n(L)=C_n(H_L)\). The local factor is
\[
 b_{p,a}(L)=\begin{cases}
 p,&a=1;\\
 (p-L)p^{a-1}+L,&a\ge2,\ 1\le L\le p;\\
 2p-L,&a\ge2,\ p\le L\le2p;\\
 0,&a\ge2,\ L\ge2p.
 \end{cases}
\qquad B_n(L)=\prod_{p^a\Vert n}b_{p,a}(L).
\tag{2}
\]
The formulas agree at overlapping boundary values. If \(n\) is squarefree, every residue is regular and \(B_n(L)=n\) for all \(L\). Otherwise, letting \(q=\min\{p:p^2\mid n\}\),
\[
\boxed{B_n(L)>0\iff1\le L\le2q-1.}
\tag{3}
\]
Thus the *longest consecutive run* of regular integers modulo \(n\) has exactly \(2q-1\) terms; its exact number of possible starting residues is \(B_n(2q-1)\).

More precisely, for nonsquarefree \(n\), the number \(E_n(L)\) of cyclic runs of **exactly** \(L\) regular residues, each bounded on both sides by nonregular residues, is
\[
\boxed{E_n(L)=B_n(L)-2B_n(L+1)+B_n(L+2),\qquad 1\le L\le2q-1.}
\tag{4}
\]
Here one counts the starting positions modulo \(n\), not translations of run types. No runs of larger length exist. Consequently, equations (2) and (4) determine the entire distribution of maximal run lengths in the periodic indicator of regularity. They also give, for uniform \(x\bmod n\), the exact joint probability \(\Pr(x+h\text{ regular for all }h\in H)=C_n(H)/n\).

## Assumptions and scope

The modulus is any integer \(n\ge2\), with no restriction on its prime-factorization type. The shifts are distinct integers forming a nonempty finite set; repeated inputs may simply be reduced to a set. Regularity is the von Neumann regularity condition in \(\mathbb Z/n\mathbb Z\), not a statement about units alone. All counts are of residues, so the starting integer may be interpreted cyclically modulo \(n\). The formula for exact run lengths concerns nonsquarefree moduli; for squarefree moduli the regularity indicator is identically one and there is no finite maximal run bounded by failures.

## Proof

**Local characterization.** For any prime power \(p^a\) and integer \(z\), the congruence \(z^2y\equiv z\pmod {p^a}\) holds for some \(y\) exactly when either \(p\nmid z\) or \(p^a\mid z\). Indeed, in the first case \(z\) is invertible and \(y=z^{-1}\) works; in the second case both sides are zero. If \(0<v_p(z)<a\), then \(v_p(z^2y-z)=v_p(z)\) for any integer \(y\) because \(zy-1\equiv-1\pmod p\), so the required divisibility is impossible. This argument is valid also for \(a=1\), when all residues are either units or zero.

**An arbitrary family of shifts.** Fix \(p^a\Vert n\) and a possible starting residue \(x\bmod p\). If none of the shifts \(h\in H\) gives \(x+h\equiv0\pmod p\), then all translates are units, and each of the \(p^{a-1}\) lifts \(x\bmod p^a\) succeeds. There are precisely \(p-r_p(H)\) such choices of \(x\bmod p\). Otherwise exactly one residue class \(c\bmod p\) of shifts satisfies \(x+c\equiv0\pmod p\). Every shift in that class must then be congruent to \(-x\pmod {p^a}\), since a nonunit regular translate must be zero modulo \(p^a\). Such a lift exists and is unique exactly when these shifts all have the same residue modulo \(p^a\); if two disagree, no lift exists. There are \(t_{p,a}(H)\) successful represented classes. Summing gives the factor in (1). Since regularity modulo \(n\) is equivalent to regularity at each full prime-power factor, the Chinese remainder theorem multiplies the local counts and proves (1).

**Consecutive shifts.** Suppose \(H=H_L\). If \(a=1\) every residue is regular, so the factor is \(p\). For \(a\ge2\) and \(L\le p\), exactly \(L\) distinct classes are represented and each contains one shift; hence \(r_p=t_{p,a}=L\) and (1) gives the first nonsquarefree branch of (2). If \(p<L\le2p\), all \(p\) classes are represented; exactly \(2p-L\) occur once and \(L-p\) occur twice. The two shifts in a repeated class differ by \(p\), which is nonzero modulo \(p^a\), so \(t_{p,a}=2p-L\). If \(L\ge2p\), every class contains at least two shifts differing by \(p\); thus \(t_{p,a}=0\). This proves (2) including the endpoints. Every local factor is positive exactly when either \(a=1\), or \(L\le2p-1\). Taking the minimum over squared-prime divisors gives (3). Moreover \(B_n(2q-1)>0\), since the factor for \(q\) equals one and all other factors are positive, so this upper bound is attained rather than just a necessary condition.

**Exact maximal-run histogram.** For \(n\) nonsquarefree, there is at least one nonregular residue, so every run in the cyclic indicator has well-defined preceding and following failures. Let \(I(x)\) denote the indicator that \(x\bmod n\) is regular. The indicator of a run of exactly \(L\) terms starting at \(x\) equals
\[
(1-I(x-1))\,\Big(\prod_{j=0}^{L-1}I(x+j)\Big)\,(1-I(x+L)).
\]
Expand the first and last factors and sum over \(x\bmod n\). Translation invariance of the count of consecutive blocks gives the four terms \(B_n(L),-B_n(L+1),-B_n(L+1),B_n(L+2)\), proving (4). This is a complete count, not a finite search bound.

Finally, setting \(L=1\) recovers the known one-point count: each \(p^a\) contributes \(\varphi(p^a)+1\), so \(B_n(1)=\prod_{p^a\Vert n}(\varphi(p^a)+1)=\sum_{d\Vert n}\varphi(d)\) (Morgado's formula). Equations (1)--(4) therefore extend the classical one-point invariant to all finite translate correlations and the complete run histogram.

## Verification

The accompanying standalone standard-library program `verify.py` directly tests regularity using the independent criterion \(\gcd(z^2,n)=\gcd(z,n)\), and compares exhaustive residue enumeration with the formulas. The executed output was:

```
VERIFY_OK moduli=319 arbitrary_patterns=3828 consecutive_patterns=3903 exact_run_histograms=612 example_cases=6 exact_integer=yes
```

The program checks all moduli \(2\le n\le320\), 3,828 arbitrary finite-pattern cases, 3,903 consecutive-block cases, and 612 exact-run histogram cases, all by exact integers. It includes negative offsets, repeated classes modulo primes, and the squarefree and nonsquarefree regimes. For instance, \(B_4(3)=1\), \(B_8(3)=1\), \(B_9(5)=1\), \(B_{12}(3)=3\), \(B_{36}(3)=3\), and \(B_{25}(9)=1\). These computations corroborate the proof but do not substitute for the unrestricted CRT argument.

## Relationship to prior work

Morgado's classical regularity criterion and one-point formula provide the starting local notion. Haukkanen and Tóth studied a regular-integer version of Ramanujan sums and a Fourier transform of the regularity indicator, supplying broad harmonic methods but not, in the inspected paper, this collision-sensitive local formula for *simultaneous arbitrary shifts*, the sharp largest consecutive run, or the exact run-length histogram.

Dohmen and Lange-Geisler's 2023 arXiv paper (later published in 2026 in the Journal of Integer Sequences) gives four combinatorial proofs for the number \(\varrho(n)\) of individual regular residues and discusses success of a *single* randomly selected message. Their 2025 IACR preprint introduces an arbitrary-modulus multi-prime/multi-power RSA variant whose correct-message class consists of regular residues. A 2026 companion IACR preprint (2026/1589) likewise states one-message correctness in its accessible abstract. These works motivate the natural simultaneous-message question, but the inspected accessible claims do not give equations (1)--(4). Equation (1) recovers the known single-message result when \(H\) has one element; the additional interactions of occupied classes, particularly repeated classes modulo \(p\), are necessary for the multi-shift law. A general Fourier identity might alternatively recover the correlations after a separate calculation; no claim of methodological uniqueness is made.

## Limitations

The statements count residue patterns mathematically, not dependent data in a cryptographic protocol. They do not address security, key-generation choices, nonuniform messages, statistical independence of messages, or algorithms for finding factorizations of large moduli. The primary IACR preprint's complete PDF was not accessible during the literature comparison; its public abstract and publication history were checked. Some older literature on finite-ring regular elements may imply the formulas under different terminology, so historical priority is not independently settled. Independent proof and priority review have not been performed. Finite verification alone cannot establish the theorems for unbounded moduli.

## References

1. J. Morgado, *Inteiros regulares módulo n*, Gazeta de Matemática (Lisboa) 33 (1972), nos. 125--128, 1--5.
2. P. Haukkanen and L. Tóth, *An analogue of Ramanujan's sum with respect to regular integers (mod r)*, arXiv:1008.5239 (2010), later Ramanujan Journal 27 (2012), 71--88; https://arxiv.org/abs/1008.5239.
3. K. Dohmen and M. Lange-Geisler, *On the Number of Regular Integers Modulo n and Its Significance for Cryptography*, arXiv:2304.02471v7 (original 2023; version 2025), Journal of Integer Sequences 29 (2026), Article 26.2.4; https://arxiv.org/html/2304.02471v7.
4. K. Dohmen and M. Lange-Geisler, *General Multi-Prime Multi-Power RSA — A Generalization of RSA and CRT-RSA to Regular Integers Modulo n*, Cryptology ePrint Archive 2025/1157, first public version 2025-06-18; https://eprint.iacr.org/2025/1157.
5. K. Dohmen and M. Lange-Geisler, *The Role of Regular Integers Modulo n in RSA Cryptography*, Cryptology ePrint Archive 2026/1589; https://eprint.iacr.org/2026/1589.
6. OEIS Foundation, *A055653*, the number of regular residues modulo an integer; https://oeis.org/A055653.
