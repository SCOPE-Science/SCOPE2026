# The first four period fibers of modular energy: a sharp prime-window law

## Finding

For integers \(m\ge18\), let \(L_m=\operatorname{lcm}(1,2,\ldots,m)\) and define the modular energy
\[
E_m(n)=\sum_{k=1}^{m}(n\bmod k),\qquad 0\le n<L_m,
\]
using the least nonnegative remainder. Write
\[
r_m=\#\{p\text{ prime}:m/2<p\le m\}=\pi(m)-\pi(m/2),
\qquad
s_m=\#\{p\text{ prime}:m/3<p\le m/2\}=\pi(m/2)-\pi(m/3).
\]
The exact multiplicity of each of the first four positive energy levels is
\[
\boxed{c_m(j)=\binom{r_m+j-1}{j}\quad(0\le j\le3),\qquad
c_m(4)=\binom{r_m+3}{4}+s_m,}
\]
where \(c_m(j)=\#\{n\pmod{L_m}:E_m(n)=j\}\). Equivalently, with \(F_m(z)=\sum_{n=0}^{L_m-1}z^{E_m(n)}\),
\[
F_m(z)\equiv (1-z)^{-r_m}+s_m z^4\pmod{z^5}.
\]
The cutoff \(m\ge18\) is sharp as a uniform threshold: at \(m=17\), the third fiber already differs from this formula.

## Assumptions and scope

Here \(m\) is an arbitrary integer at least \(18\), the variable \(n\) ranges over exactly one complete period modulo \(L_m\), and \(\pi(x)\) counts primes no larger than the real number \(x\). All calculations use ordinary integer congruences, with no probabilistic assumptions. No formula is asserted for energy levels above \(4\) or for \(m<18\). Bertrand's theorem ensures \(r_m\ge1\).

## Proof

**Step 1: divisibility by small prime powers.** Suppose \(E_m(n)\le4\). If a prime \(p\) does not divide \(n\), then every multiple of \(p\) up to \(m\) has a nonzero remainder; consequently \(E_m(n)\ge\lfloor m/p\rfloor\). Since \(m\ge18\), we must have \(2\mid n\) and \(3\mid n\).

We claim that **every** prime power \(p^a\le m\), with \(a\ge2\), divides \(n\). Otherwise take the least such exponent \(a\ge2\) for a fixed prime \(p\). Then \(p^{a-1}\mid n\) while \(p^a\nmid n\). Every multiple of \(p^a\) at most \(m\) contributes a remainder at least \(p^{a-1}\), hence
\[
E_m(n)\ge p^{a-1}\left\lfloor\frac m{p^a}\right\rfloor.
\]
For \(p\ge5\), this is at least \(5\). For \(p=2,a=2\), it is at least \(2\lfloor18/4\rfloor=8\); for \(p=2,a=3\), at least \(4\lfloor18/8\rfloor=8\); and for \(p=2,a\ge4\), at least \(8\). For \(p=3,a=2\), it is at least \(3\lfloor18/9\rfloor=6\), and for \(p=3,a\ge3\), at least \(9\). Every possibility contradicts \(E_m(n)\le4\). Note that the lower bounds for larger exponents use only \(\lfloor m/p^a\rfloor\ge1\), as \(p^a\le m\).

**Step 2: restriction of possible prime residues.** Assume \(p\nmid n\) and \(p\ge5\). If \(p\le m/4\), then the four multiples \(p,2p,3p,4p\) contribute at least \(4\). Equality would force the remainder modulo \(2p\) to equal \(1\), contradicting \(2\mid n\); hence \(p>m/4\).

If \(m/4<p\le m/3\), write \(u=n\bmod p\). The positive remainders at \(p,2p,3p\) sum to at most \(4\), so \(1\le u\le2\). As \(n\) is even, the remainder modulo \(2p\) can be at most \(4\) only if it is \(u\), forcing \(u\) even. As \(3\mid n\), the remainder modulo \(3p\) can be at most \(4\) only if it is \(u\), forcing \(3\mid u\). This is impossible for \(u\in\{1,2\}\). Therefore every prime not dividing \(n\) lies above \(m/3\).

If \(m/3<p\le m/2\), the only multiples of \(p\) among \(1,\ldots,m\) are \(p\) and \(2p\). With \(u=n\bmod p\), the two nonzero contributions are \(u\) and either \(u\) or \(u+p\). Because \(p\ge7\), the second case exceeds energy \(4\). Thus both remainders equal \(u\); parity forces \(u\) even, and \(2u\le4\) gives \(u=2\). Such a prime consumes exactly four energy units.

If \(m/2<p\le m\), there is just one multiple of \(p\), and its remainder can take any value from \(0\) through \(4\) under the energy bound. All such primes exceed \(4\).

**Step 3: realization and counting.** Every integer \(k\le m\) divides \(L_m\). Step 1 and the divisibility restrictions of Step 2 show that all positive remainders in a residue class with energy at most four arise either from a prime \(p\in(m/2,m]\), appearing once with an arbitrary nonnegative contribution, or from a single prime \(p\in(m/3,m/2]\), appearing at \(p\) and \(2p\) with contributions \(2+2\). Because \(m\ge18\), every prime greater than \(m/3\) appears to exponent one in \(L_m\). Their congruences modulo \(p\) are independent of one another and of the conditions \(n\equiv0\pmod{q^a}\) at the other prime-power factors of \(L_m\), by the Chinese remainder theorem.

Conversely, each assignment with total cost at most four gives exactly one residue class modulo \(L_m\) and yields precisely those remainders at all \(k\le m\): primes in the upper interval occur in no composite modulus at most \(m\), and primes in the middle interval occur only at \(p\) and \(2p\), where the prescribed residue \(2\) is compatible with \(2\mid n\).

The independent upper-interval primes contribute the generating series \((1-z)^{-r_m}\) through degree four. One middle-interval prime contributes an additional \(z^4\), and two would already exceed degree four. Therefore
\[
F_m(z)\equiv(1-z)^{-r_m}+s_mz^4\pmod{z^5},
\]
which proves every claimed multiplicity.

**Sharpness.** For \(m=17\), the three primes in \((17/2,17]\) are \(11,13,17\), providing \(\binom{3+2}{3}=10\) independent upper-prime solutions of energy three. In addition, put \(L_{17}=12252240\) and \(n=2L_{17}/3=8168160\). Every integer \(k\le17\) other than \(9\) divides \(n\), whereas \(n\bmod9=3\). Hence \(E_{17}(n)=3\), and this class is distinct from the ten upper-prime classes. Thus \(c_{17}(3)\ge11>10\): the uniform threshold \(18\) cannot be decreased.

## Verification

A standalone exact-integer verifier is supplied in `verify.py`. It exhaustively counts all fibers through energy four over the full least-common-multiple periods for \(m=16,17,18\), including the boundary \(m=17\) and the first valid value \(m=18\). It separately checks all CRT-constructed low-energy classes for \(m\in\{18,19,23,37,64,100\}\). The observed counts at \(m=18\) are \((1,3,6,10,16)\), as the theorem predicts; at \(m=17\) they are \((1,3,6,11,19)\), showing the predicted third coefficient fails there. Run `python verify.py` in an environment with NumPy. The proof above, not finite enumeration, establishes the unbounded claim.

## Relationship to prior work

En-naoui's September 2025 preprint introduces the modular-energy notation and proves basic algebraic identities, extremal levels, and complement symmetry; its Section 10 explicitly identifies distributional questions as a direction for further study. The present result gives closed prime-window formulas for the first four positive fibers and a sharp starting cutoff, which do not follow from the cited extremal identities alone.

Petty's 2026 study of weighted compatible remainders proves a general covariance identity and weighted \(L^2\) law; that powerful second-moment framework does not enumerate these thin small-value fibers. Older OEIS records concern diagonal remainder sums or existential relations, not these fixed-cutoff period-fiber multiplicities. Earlier or unindexed exact fiber formulas cannot be ruled out absolutely.

## Limitations

The result concerns \(m\ge18\), energy at most four, and a complete residue period; it does not provide the full energy distribution or a uniform description of all exceptional values for smaller \(m\). Its connection with prime counts is an exact identity, not an algorithm for faster prime counting. Source coverage was extensive but is not an independent priority certification.

## References

1. Es-said En-naoui, *The Modular Energy Function: Exact Identities and a Primality Equivalence*, arXiv:2509.10592v1 (first public September 12, 2025), https://arxiv.org/pdf/2509.10592 .
2. Alexander S. Petty, *Conservation and Profinite Dynamics in Digit-Collision Energy* (July 31, 2026, revised September 11, 2026), https://www.alexpetty.com/paper/conservation-and-profinite-dynamics-in-digit-collision-energy .
3. OEIS A004125, diagonal sum of modular remainders, https://oeis.org/A004125 .
4. OEIS A283565, existence of equality between an integer and a sum of modular remainders, https://oeis.org/A283565 .
