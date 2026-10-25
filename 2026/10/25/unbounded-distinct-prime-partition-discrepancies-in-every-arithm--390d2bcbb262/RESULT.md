# Unbounded distinct-prime partition discrepancies in every arithmetic progression

## Finding

For every positive integer \(n\), let \(L(n)\) be the greatest number of distinct primes with sum \(n\). Let \(K(n)\) be the cardinality of the unique partition of \(n\) into distinct primes whose product is largest. When no such partition exists, set both numbers to zero. Product uniqueness follows from uniqueness of integer prime factorization.

**Theorem.** For every integer \(m\ge1\), every residue class \(c\pmod m\), and every \(R\ge1\), there are infinitely many positive integers \(n\) satisfying
\[
n\equiv c\pmod m,\qquad L(n)-K(n)\ge R.
\]
The class \(c\) need not be coprime to \(m\). The construction gives a finite list of fixed positive offsets depending on \(m,R\) and arbitrarily large prime-prefix sums from which to subtract the offsets. No effective bound for the first such \(n\) is claimed.

## Assumptions and scope

All prime partitions are **sets of pairwise distinct positive rational primes**, with sum exactly the specified integer. Write \(s(A)=\sum_{p\in A}p\), \(v(A)=\prod_{p\in A}p\), \(s(\varnothing)=0\), and \(v(\varnothing)=1\). A nonempty set of primes \(A\) is *product-minimal* if \(v(A)\) is least among the prime sets of sum \(s(A)\). Such a minimizer is unique by the fundamental theorem of arithmetic. Let \(\mathcal B_x\) be all primes at most a prime \(x\), \(\sigma_x=s(\mathcal B_x)\), and \(\pi(x)=|\mathcal B_x|\).

The proof uses Dirichlet's theorem for primes in reduced residue classes and Vinogradov's three-prime theorem (in its sufficiently-large **distinct** prime-summand form). The latter follows also from the asymptotic representation count, since triples containing a repeated prime are lower order.

## Proof

**Lemma 1 (isolated primes in a specified unit class).** Fix \(m,H\ge1\) and \(a\pmod m\) with \(\gcd(a,m)=1\). There are infinitely many primes \(q\equiv a\pmod m\) for which every integer \(q+h\) with \(1\le|h|\le H\) is composite.

*Proof.* For each such nonzero \(h\), choose a different auxiliary prime \(\ell_h>H\) with \(\ell_h\nmid m\). The Chinese remainder theorem combines \(q\equiv a\pmod m\) with \(q\equiv-h\pmod{\ell_h}\). The combined residue is prime to the combined modulus because \(a\) is a unit and \(0<|h|<\ell_h\). Dirichlet's theorem gives infinitely many primes in that class. For all sufficiently large ones, each positive \(q+h\) is strictly greater than its specified proper prime divisor \(\ell_h\), hence composite. \(\square\)

**Lemma 2 (preservation of product minimality).** If \(A\) is product-minimal, \(M=v(A)\), and a prime \(q>s(A)\) is the sole prime in \([q-4M^2,q+4M^2]\), then \(A\cup\{q\}\) is product-minimal.

*Proof.* If a distinct-prime competitor \(B\) of sum \(q+s(A)\) has product at most \(qM\), put \(k=|B|\), \(b=\max B\), \(T=v(B\setminus\{b\})\), and \(u=s(B\setminus\{b\})\). Since \(b\ge(q+s(A))/k>q/k\), we obtain \(T<kM\). Also \(T\ge2^{k-1}\), and \(k\le2\sqrt T\) for all \(k\ge1\); hence \(T<4M^2\). The elementary sum-product inequality \(s(F)\le v(F)\) for sets of integers at least two gives \(u\le T\) and \(s(A)\le M\). Therefore \(|b-q|=|s(A)-u|<4M^2\). Isolation implies \(b=q\), and minimality of \(A\) then implies \(B=A\cup\{q\}\). \(\square\)

**Lemma 3 (product-minimal sums in every residue class at fixed cardinality).** Given any modulus \(m\ge1\), take an integer \(t\ge m+1\), \(t\ge5\). For every residue \(r\pmod m\), there is an arbitrarily large integer \(d_r\equiv r\pmod m\) whose unique product-minimal prime set \(A_r\) has exactly \(t\) members.

*Proof.* Both singleton prime sets \(\{2\}\) and \(\{3\}\) are product-minimal. Starting with either seed \(s\in\{2,3\}\), append \(t-1\) successively larger primes isolated as in Lemma 2, choosing each appended prime to be \(+1\) or \(-1\) modulo \(m\). The two classes are units for every modulus, and Lemma 1 makes every choice possible at arbitrarily large size. If precisely \(j\) appended primes have residue \(-1\), the final prime-sum residue equals
\[
s+(t-1)-2j\pmod m,\qquad 0\le j\le t-1.
\]
For odd \(m\), multiplication by \(2\) permutes residues, and varying \(j\) covers all classes. For even \(m\), varying \(j\) covers one parity class for either seed, while changing the seed changes parity; their union covers all classes. The choice of the last appended prime can be arbitrarily large while its residue is held fixed. \(\square\)

**Lemma 4 (at most four prime summands).** Each sufficiently large integer \(d\) is a sum of at most four *distinct* primes. For large odd \(d\), Vinogradov's theorem yields three distinct odd primes. For even \(d\), write \(d=2+(d-2)\) and represent the sufficiently large odd integer \(d-2\) by three distinct odd primes. Thus for every residue \(r\) we may take \(d_r\) in Lemma 3 large enough to admit some set \(C_r\) with \(s(C_r)=d_r\) and \(|C_r|\le4\). \(\square\)

**Lemma 5 (prime-prefix exchange).** Suppose \(A\) is product-minimal of sum \(d>0\) and product \(M\); let \(x>d\) be prime and let the next prime \(y\) satisfy \(G=y-x>11M\). Then the unique maximum-product prime partition of \(\sigma_x-d\) is \(\mathcal B_x\setminus A\).

*Proof.* Its product is \(T_x/M\), where \(T_x=v(\mathcal B_x)\). Given another distinct-prime partition \(E\) with the same sum, write \(U=\mathcal B_x\setminus E\) and \(V=E\setminus\mathcal B_x\), so \(s(U)-s(V)=d\). If \(V=\varnothing\), product-minimality forces \(v(U)\ge M\), with equality only when \(U=A\). If \(V\ne\varnothing\), let \(h=|V|\) and \(a=|U|-h\ge1\): this follows because all primes in \(U\) are at most \(x\), and all primes in \(V\) are at least \(y\). Order \(U=\{u_1<\dots<u_{a+h}\}\), \(V=\{v_1<\dots<v_h\}\), and set \(\tau=\sum_{i=1}^{a}u_i\). Pairing large removed primes with added primes gives
\[
\tau-d=\sum_{j=1}^{h}(v_j-u_{a+j})\ge hG,
\]
so \(\tau\ge d+G\). As \(u_{a+j}\ge u_a\) and \(\tau\le a u_a\),
\[
\sum_{j=1}^{h}\frac{v_j}{u_{a+j}}
\le h+\frac{\tau-d}{u_a}\le h+a.
\]
The arithmetic-geometric mean inequality gives \(\prod_{j=1}^{h}v_j/u_{a+j}\le(1+a/h)^h\le e^a\). Since the \(u_i\) are distinct integers at least two,
\[
\prod_{i=1}^{a}u_i\ge(a-1)!\tau.
\]
Consequently
\[
\frac{v(U)}{v(V)}\ge\frac{(a-1)!}{e^a}\tau
\ge\frac{2}{e^3}(d+G)>\frac{G}{11}>M,
\]
where \((a-1)!e^{-a}\ge2e^{-3}>1/11\) for all integers \(a\ge1\). Therefore \(v(E)=T_xv(V)/v(U)<T_x/M\), proving unique optimality. \(\square\)

**Completion.** Fix \(m,c,R\), and choose \(t\ge\max\{m+1,R+4,5\}\). By Lemmas 3 and 4 choose once and for all, for each \(r\pmod m\), sets \(A_r,C_r\) of common sum \(d_r\equiv r\pmod m\) with \(|A_r|=t\), \(A_r\) product-minimal, and \(|C_r|\le4\). Let \(M_*:=\max_r v(A_r)\), \(d_*:=\max_r d_r\). By Lemma 1 (modulus one), there are infinitely many primes \(x>d_*\) whose following prime gap exceeds \(11M_*\). For each such \(x\), choose \(r_x\equiv\sigma_x-c\pmod m\) and put \(n_x=\sigma_x-d_{r_x}\). Then \(n_x\equiv c\pmod m\). Lemma 5 supplies a maximum-product partition \(\mathcal B_x\setminus A_{r_x}\) with \(\pi(x)-t\) summands, whereas \(\mathcal B_x\setminus C_{r_x}\) is another partition of the same sum with at least \(\pi(x)-4\) summands. Therefore
\[
L(n_x)-K(n_x)\ge t-4\ge R.
\]
Since \(d_{r_x}\) takes values in a fixed finite set and \(\sigma_x\to\infty\), the \(n_x\) are unbounded, hence infinitely many distinct positive integers. \(\square\)

## Verification

The supplied standalone `verify.py` checks the exhaustive residue-programming assertion for moduli \(1\le m\le120\), the Chinese-remainder unit-class construction for every reduced class in moduli \(1\le m\le13\) and \(1\le H\le5\), and the factorial inequality used in Lemma 5 for \(1\le a\le99\). Its exact-output success marker is `VERIFY_OK`. These are finite consistency checks only. The theorem for all moduli and all discrepancy thresholds rests on the proofs, Dirichlet's theorem, and Vinogradov's theorem.

## Relationship to prior work

Campbell (2026, arXiv:2610.19534) proves that \(L(n)-K(n)\) is unbounded over **all** positive integers and supplies both the product-minimal extension and the prime-prefix exchange mechanisms used above. The new assertion establishes unboundedness within **every prescribed residue class**, including nonunits, through a uniform-cardinality residue-programming construction; global unboundedness does not imply this modular strengthening. A previously derived multiplicity theorem for prime-prefix offsets gives arbitrarily many distinct offsets and a global counting lower bound but does not require offsets covering all residue classes; it therefore does not imply the present theorem by its stated quantifiers. A prior sharper isolation-width criterion can be substituted for Lemma 2 but does not by itself supply the modular programming or the conclusion.

Deléglise and Nicolas (2015) examine maximum products with the weaker constraint that the sum of the distinct primes is at most a budget; the present exact-sum partition cardinalities are different invariants. Dirichlet's theorem gives the prescribed congruences of isolated primes but not the discrepancy theorem by itself.

## Limitations

The proof establishes existence in every fixed progression, not a density, asymptotic count, uniform effective least witness, or exact values of \(L(n)\) and \(K(n)\). It relies on classical deep results for the ternary Goldbach representation and on Dirichlet's theorem, not on finite experiments. The earliest-preprint source and selected adjacent literature were checked, but unindexed or otherwise inaccessible equivalences may still affect priority; no independent audit has been carried out.

## References

1. J. M. Campbell, *On a problem on partitions into distinct primes*, arXiv:2610.19534v1 (first posted October 14, 2026), https://arxiv.org/abs/2610.19534 .
2. M. Deléglise and J.-L. Nicolas, *On the Largest Product of Primes with Bounded Sum*, Journal of Integer Sequences **18** (2015), Article 15.2.8, https://www.maths.tcd.ie/EMIS/journals/JIS/VOL18/Deleglise/deleglise3.pdf .
3. I. M. Vinogradov, the classical three-prime theorem (1937); the asymptotic number of representations ensures sufficiently large odd targets have distinct prime summands.
4. P. G. L. Dirichlet, theorem on primes in arithmetic progressions (1837).
