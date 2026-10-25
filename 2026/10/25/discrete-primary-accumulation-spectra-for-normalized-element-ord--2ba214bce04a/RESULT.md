# Discrete primary accumulation spectra for normalized element-order moments

## Finding

Fix a prime \(p\). For each positive integer \(k\) and each finite abelian \(p\)-group \(G\), define the normalized element-order moment

\[
F_k(G)=\frac{1}{|G|^{k+1}}\sum_{g\in G}\operatorname{ord}(g)^k,
\qquad
c_{p,k}=\frac{(p-1)p^k}{p^{k+1}-1}.
\]

**Theorem (exact primary accumulation spectrum).** For any fixed \(p\) and \(k\), the set of limits along sequences of pairwise nonisomorphic finite abelian \(p\)-groups is exactly

\[
\mathcal L_{p,k}=\{0\}\ \cup\ \{c_{p,k}p^{-bk}:b=0,1,2,\ldots\}.
\]

The positive values are strictly decreasing, so this set has the unique accumulation point zero. The stronger **joint rigidity statement** holds: for any sequence \((G_j)\) of finite abelian \(p\)-groups with \(|G_j|\to\infty\), existence of a positive limit of \(F_k(G_j)\) for just one \(k\ge1\) is equivalent to eventual constancy of

\[
b(G_j)=\log_p\bigl(|G_j|/\exp(G_j)\bigr)
\]

at an integer \(b\). In that case \(F_m(G_j)\to c_{p,m}p^{-bm}\) for **every** positive integer \(m\). If instead \(b(G_j)\to\infty\), then \(F_m(G_j)\to0\) for every fixed \(m\).

## Assumptions and scope

The prime \(p\) is held fixed; the result does not assert a discrete spectrum when the prime is allowed to vary. All groups are finite abelian \(p\)-groups and all moment orders are positive integers. A sequence is pairwise nonisomorphic in the scalar accumulation statement; equivalently its group orders must tend to infinity after passing to any infinite subsequence, since only finitely many abelian groups exist up to a given order. The joint rigidity statement assumes directly that group orders tend to infinity.

Write \(|G|=p^n\) and \(\exp(G)=p^\ell\). The integer \(b(G)=n-\ell\) measures the exponent defect: it is the logarithmic size of the product of all invariant factors other than one of largest order. In particular, \(b(G)\ge0\).

## Proof

**1. Exponent bound.** Every element of \(G\) has order at most \(p^\ell\), so

\[
0<F_k(G)\le\frac{|G|p^{k\ell}}{|G|^{k+1}}=p^{-kb(G)}.
\tag{1}
\]

Consequently, any sequence with \(b(G_j)\to\infty\) has all fixed normalized moments converging to zero. Conversely, if \(F_k(G_j)\) has a positive limit, (1) forces its exponent defects \(b(G_j)\) to remain bounded.

**2. Uniform cyclic-dominance identity.** If \(b=b(G)\) and \(\ell>b\), the invariant-factor decomposition permits writing

\[
G\cong C_{p^\ell}\times H,
\qquad |H|=p^b,
\qquad\exp H\le p^b.
\]

The element orders in \(C_{p^\ell}\times H\) whose first coordinate has order exceeding \(p^b\) are just the first-coordinate orders, independent of the choice of \(h\in H\). Their contribution to \(\psi_k(G)=\sum_g\operatorname{ord}(g)^k\) is therefore \(p^b(\psi_k(C_{p^\ell})-\psi_k(C_{p^b}))\). The remaining elements have first coordinate in \(C_{p^b}\) and contribute \(\psi_k(C_{p^b}\times H)\). Thus the **exact identity** is

\[
\psi_k(G)=p^b\bigl(\psi_k(C_{p^\ell})-\psi_k(C_{p^b})\bigr)
+\psi_k(C_{p^b}\times H).
\tag{2}
\]

The cyclic formula, valid for every integer \(r\ge0\), is

\[
\psi_k(C_{p^r})=\sum_{i=0}^r\varphi(p^i)p^{ki}
=c_{p,k}p^{(k+1)r}+d_{p,k},
\quad d_{p,k}=\frac{p^k-1}{p^{k+1}-1},
\tag{3}
\]

where \(\varphi(1)=1\). Inserting (3) into (2) and dividing by \(p^{(k+1)(\ell+b)}\) gives

\[
F_k(G)=c_{p,k}p^{-kb}
+\frac{E_{p,k}(H)}{p^{(k+1)(\ell+b)}},
\quad E_{p,k}(H)=p^b d_{p,k}+\psi_k(C_{p^b}\times H)-p^b\psi_k(C_{p^b}).
\tag{4}
\]

For each \((x,h)\in C_{p^b}\times H\) one has \(\operatorname{ord}(x,h)^k\ge\operatorname{ord}(x)^k\), so \(E_{p,k}(H)\ge p^b d_{p,k}>0\). Since this product group has \(p^{2b}\) elements, all of order at most \(p^b\), we also obtain

\[
0<E_{p,k}(H)\le p^b+p^{(k+2)b}
\le2p^{(k+2)b}.
\tag{5}
\]

The error bound (5) is independent of \(\ell\) and of the isomorphism type of \(H\). Therefore, for any sequence with \(b(G_j)=b\) fixed and \(|G_j|\to\infty\) (hence \(\ell_j\to\infty\)), equation (4) proves \(F_k(G_j)\to c_{p,k}p^{-kb}\), simultaneously for all positive integers \(k\).

**3. Exhaustion and rigidity of positive limits.** Suppose \(F_k(G_j)\to L>0\). By (1), \(b(G_j)\) belongs to a finite set. Every value \(b\) occurring infinitely often defines a subsequence with limit \(c_{p,k}p^{-kb}\) by Step 2. As these candidate limits are pairwise distinct for distinct integers \(b\), at most one \(b\) can occur infinitely often. The sequence of integer exponent defects is therefore eventually constant. Step 2 establishes the asserted simultaneous limits of all moments. Conversely, eventual constancy of \(b\) implies the positive limit in Step 2.

For an arbitrary convergent scalar sequence of normalized moments, either the limit is positive and described above, or it is zero. Every stated positive candidate is actually attained as a limit: for fixed \(b\), take

\[
G_\ell=C_{p^\ell}\times(C_p)^b,
\qquad \ell\to\infty,
\]

and apply (4) for \(\ell>b\). The value zero is obtained from \(G_r=(C_p)^r\) as \(r\to\infty\), because then \(b(G_r)=r-1\). These families consist of pairwise nonisomorphic groups. This proves the complete spectrum and the joint rigidity theorem. \(\square\)

## Verification

A standalone exact-rational checker (`verification/check_moments.py`) enumerates all integer partitions of group-order exponents through 10, covers primes \(2,3,5\) and powers \(k=1,2,3,4\), and checks (4) whenever \(\ell>b\). It also directly verifies the positivity and error bound over independent parameter families. The checker reports `VERIFY_OK exact_partition_cases= 624  and uniform error bounds`. Computations are finite corroboration; the proof establishes the infinite statements.

## Relationship to prior work

Chatterjee, Das and Poddar, *A generalization of the sum of element orders function* (arXiv:2610.11804; first posted 2026-10-08), introduce and study precisely the normalization \(F_k\), including density questions across broad classes of finite groups. Lazorec and Tărnăuceanu (arXiv:1911.10557) established global density for \(k=1\), and explicitly gave the cyclic prime-power formula. Theorem 1.4 and Lemma 2.3 of Dey and Mondal (arXiv:2208.05161) provide the power-moment recurrence and cyclic formula for finite abelian \(p\)-groups. Amiri (2026, DOI 10.1007/s10801-026-01554-3) treats how a single unnormalized order sum distinguishes finite abelian groups of the same order. The present finding **does not claim those moment formulas or the cyclic limit as new**: it isolates the exact fixed-prime accumulation set across arbitrary changing invariant-factor types, gives an explicit uniform exponent-defect estimate, and proves simultaneous rigidity of all normalized moments. Global density when varying primes and discrete fixed-prime limits concern different quantified families.

## Limitations

Primes must remain fixed for the discrete spectrum. Only finite abelian \(p\)-groups and positive integral moments are classified; neither nonabelian \(p\)-groups nor sequences with varying primes are covered. This is an asymptotic classification, not an injectivity theorem for values on individual finite groups. Pointwise finite-group power-moment formulas predate this statement; equivalence to an unlocated earlier asymptotic classification remains a priority risk. No independent validation is claimed.

## References

1. S. Chatterjee, A. Das, S. Poddar, *A generalization of the sum of element orders function*, arXiv:2610.11804, v1 (2026-10-08), https://arxiv.org/abs/2610.11804 .
2. H. K. Dey, A. Mondal, *An exact upper bound for the sum of powers of element orders in non-cyclic finite groups*, arXiv:2208.05161, v1 (2022), https://arxiv.org/html/2208.05161v1 .
3. M.-S. Lazorec, M. Tărnăuceanu, *A density result on the sum of element orders of a finite group*, arXiv:1911.10557 (2019), https://arxiv.org/abs/1911.10557 .
4. M. Amiri, *On the sum of element orders in finite abelian groups*, Journal of Algebraic Combinatorics 63 (2026), article 65, https://doi.org/10.1007/s10801-026-01554-3 .
