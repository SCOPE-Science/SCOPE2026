# Sharp local Dold repair and signed-orbit spectra for the Pell pair

## Finding

Let \(U_0=0,U_1=1\) and \(V_0=2,V_1=2\), each satisfying \(W_{n+2}=2W_{n+1}+W_n\). For a prime \(p\), let \(A_p(n)=p^{\nu_p(U_n)}\), \(B_p(n)=p^{\nu_p(V_n)}\), for \(n\ge1\), and write \(\mathcal L_n(F)=\sum_{d\mid n}\mu(n/d)F(d)\). We give the complete signed Möbius-transform spectra, smallest integer Dold repair factors, and realizability classifications of both prime-part sequences.

For odd \(p\), let \(r\) be the least positive index with \(p\mid U_r\), and let \(e=\nu_p(U_r)\). Then \(r\mid p-(2/p)\), \(r\ge3\), and the entire Möbius transform of \(A_p\) is
\[
\mathcal L_n(A_p)=\begin{cases}
1,&n=1,\\
p^e-1,&n=r,\\
p^{e+j-1}(p-1),&n=rp^j,\ j\ge1,\\
0,&\text{otherwise}.
\end{cases}
\]
Its least positive integral Dold repair factor is
\[
K_p=\frac r{\gcd(r,p-1)}.
\]
In particular \(A_p\) is Dold and realizable precisely when \(p\equiv1,7\pmod8\). For \(p=2\), its transform equals \(1\) at \(n=1\), equals \(2^{j-1}\) at \(n=2^j\) for \(j\ge1\), and vanishes otherwise; its least repair factor is \(2\).

If \(p\) is odd and \(r\) is odd, \(B_p(n)=1\) for all \(n\), and its least Dold repair is \(1\). If \(r\) is even, put \(t=r/2\), \(h=\nu_p(V_t)\); then \(t\ge2\), \(h\ge1\), and
\[
\mathcal L_n(B_p)=\begin{cases}
1,&n=1,\\
p^h-1,&n=t,\\
-(p^h-1),&n=2t,\\
p^{h+j-1}(p-1),&n=tp^j,\ j\ge1,\\
-p^{h+j-1}(p-1),&n=2tp^j,\ j\ge1,\\
0,&\text{otherwise}.
\end{cases}
\]
Its least Dold repair is also \(K_p\). Since \(\mathcal L_{2t}(B_p)=1-p^h<0\), \(B_p\) in this case is not realizable after **any** positive integral rescaling, although it is almost Dold. At \(p=2\), \(B_2(n)=2\) for all \(n\), hence is Dold and realizable.

Consequently, among odd primes, \(B_p\) is Dold exactly for \(p\equiv1,5,7\pmod8\); it is realizable exactly when \(r\) is odd, which holds for every \(p\equiv5\pmod8\), fails for every \(p\equiv3,7\pmod8\), and is rank-dependent for \(p\equiv1\pmod8\). The natural densities of odd primes for which \(A_p\) is Dold and \(B_p\) is Dold are \(1/2\) and \(3/4\), respectively. They are simultaneously Dold for density \(1/2\) of odd primes.

## Assumptions and scope

All indices are positive integers; the sequence \(V\) is normalized as \(V_0=V_1=2\), not the halved Pell–Lucas sequence. A sequence \(F\) is *Dold* when \(n\mid\mathcal L_n(F)\) for every \(n\ge1\); its least *repair factor* is the least \(K\ge1\) for which \(KF\) is Dold. A nonnegative integer-valued sequence is *realizable* when each \(\mathcal L_n(F)/n\) is a nonnegative integer; equivalently, the terms count fixed points of iterates of a map on a set with finite orbits. Here all terms are positive integers. We call a sequence *almost realizable* if some positive multiple is realizable.

The Legendre symbol \((2/p)\) is used only for odd \(p\). Rank existence and the closed spectra are unconditional for every such prime, including possible primes with \(e>1\). The statement does not assert a density for rank parity inside \(p\equiv1\pmod8\).

## Proof

**Ranks and valuations.** In the quadratic order \(\mathbb Z[\sqrt2]\), put \(\alpha=1+\sqrt2\), \(\beta=1-\sqrt2\), with \(\alpha\beta=-1\), \(U_n=(\alpha^n-\beta^n)/(2\sqrt2)\), \(V_n=\alpha^n+\beta^n\). For odd \(p\), the reduction of \(\sqrt2\) in \(\mathbb F_p\) or \(\mathbb F_{p^2}\) is nonzero, and \(\alpha,\beta\) are units. The element \(z=\alpha/\beta\) has order \(r\). The Frobenius automorphism gives \(z^p=z\) if \((2/p)=1\), and \(z^p=z^{-1}\) otherwise; hence \(r\mid p-(2/p)\). Because \(U_1=1\) and \(U_2=2\), \(r\ge3\). Moreover \(p\nmid r\).

The odd-prime lifting-the-exponent identity in the unramified quadratic extension, applied to \(\alpha^r-\beta^r\), gives
\[
\nu_p(U_n)=\begin{cases}e+\nu_p(n/r),&r\mid n,\\0,&r\nmid n.\end{cases}
\]
One can prove the lifting formula directly by expanding \((1+py)^m-1\) over the unramified local ring: for odd \(p\), its valuation is \(\nu_p(py)+\nu_p(m)\), and the denominator \(2\sqrt2\) is a unit.

For \(V_n\), the criterion is \(z^n=-1\). If \(r\) is odd there is no such index. If \(r=2t\), it holds exactly when \(n=tk\) with \(k\) odd. The identity \(\alpha^{tk}+\beta^{tk}\), with \(k\) odd, gives the analogous lifting valuation
\[
\nu_p(V_n)=\begin{cases}h+\nu_p(n/t),&n/t\text{ is odd and }t\mid n,\\0,&\text{otherwise}.\end{cases}
\]
Here \(t\ge2\) because \(U_2=2\).

**Exact Möbius transforms.** Write \(A_p(n)-1\) as the function supported on indices \(r m\), with value \(p^{e+\nu_p(m)}-1\). Möbius inversion of this divisibility-supported function is supported only at \(r\) and \(rp^j\) for \(j\ge1\), with values \(p^e-1\) and \(p^{e+j-1}(p-1)\). Likewise \(B_p(n)-1\), when \(r=2t\), is supported on indices \(t m\) with odd \(m\). Its Möbius transform is the tensor product of the odd-power \(p\)-increment and the signed \(2\)-increment, producing the displayed plus/minus pairs at \(tp^j\) and \(2tp^j\), including \(j=0\). For either function the constant \(1\) contributes solely at \(n=1\). This is an identity for *all* indices, not a finite enumeration.

**Sharp Dold repairs.** For odd \(p\), the only nonzero transform indices of \(A_p\) are \(r p^j\), so Dold integrality for \(KA_p\) is equivalent to
\[
r\mid K(p-1).
\]
Indeed \(p\nmid r\), \(p-1\mid p^e-1\), and \(n=rp\) forces the condition because \(\mathcal L_{rp}=p^e(p-1)\). In the even-rank trace case, the support indices \(tp^j,2tp^j\) similarly give the same condition \(r=2t\mid K(p-1)\), forced at \(n=2tp\). Therefore the least repair is \(r/\gcd(r,p-1)\). For odd-rank trace the constant sequence needs no repair. In the even-rank case the strictly negative \(\mathcal L_{2t}\) rules out realizability under every positive scaling, whereas all transforms of \(A_p\) are nonnegative.

**The prime two.** Each \(V_n\) is congruent to \(2\pmod4\) by the recurrence, hence \(\nu_2(V_n)=1\). The relation \(U_{2m}=U_mV_m\), together with oddness of \(U_n\) for odd \(n\), yields \(\nu_2(U_n)=\nu_2(n)\). Möbius inversion of \(2^{\nu_2(n)}\) is supported at \(1\) and powers of two, as claimed. Its value at \(2\) is \(1\), so the least repair is \(2\).

**Congruence classes and density.** For \(p\equiv1,7\pmod8\) the discriminant \(8\) is a square, so \(r\mid p-1\). For \(p\equiv3,5\pmod8\), \(r\mid p+1\) and \(\gcd(r,p-1)=\gcd(r,2)\). When \(p\equiv3\pmod8\), \(z^{(p+1)/2}=-1\) so \(r\) is even and greater than two; hence \(r\nmid p-1\). When \(p\equiv5\pmod8\), \(z^{(p+1)/2}=1\) and \((p+1)/2\) is odd, so \(r\) is odd, also greater than one. This classifies \(A_p\). For \(p\equiv7\pmod8\), \(z^{(p-1)/2}=-1\), so \(r\) is even; for \(p\equiv1\pmod8\), its parity need not be fixed. Thus \(B_p\) is always Dold on split primes and on \(p\equiv5\pmod8\), but not on \(p\equiv3\pmod8\). The four odd residue classes modulo eight each have prime density \(1/4\) by Dirichlet's theorem, giving the claimed densities.

## Verification

Run `python3 VERIFY.py` in this package. The pure-Python verifier builds the two sequences exactly, computes prime valuations and Möbius transforms directly, compares every transform with the closed formulas for the first 27 primes through 103 and all indices at most 320, verifies rank and parity rules, and checks 15,228 modular Dold comparisons. Its successful terminal line is `VERIFY_OK 27 primes; 15228 Dold modular comparisons; n<= 320`. These finite tests corroborate but do not replace the proof for all primes and indices.

## Relationship to prior work

Chuysurichay and coauthors, *The local Dold congruence for Fibonacci and Lucas sequences* (first publicly posted 2026-09-21, arXiv:2609.24544v1), study local Dold behavior of the classical Fibonacci and Lucas sequences and explicitly motivate extensions to general companion Lucas systems. The present result treats the nonsplit-discriminant-eight Pell system, gives both sequences' entire signed transform spectra, proves least repair factors, and separates Dold integrality from sign/realizability. The published record titled *All local prime parts are Dold for split companion Lucas sequences* requires a positive square discriminant, unlike the Pell discriminant eight. Results on equal periods of the two Lucas companions address a different invariant. This comparison is not a claim of absolute literature uniqueness.

## Limitations

There is no asserted density for prime classes characterized by the parity of \(r\) within \(p\equiv1\pmod8\). Prime-density statements use the standard Dirichlet theorem, not an elementary prime-counting proof. No independent mathematical audit has been conducted. A mathematically equivalent consequence of a broader general Lucas-sequence theorem not located in the inspected literature remains possible.

## References

1. S. Chuysurichay et al., *The local Dold congruence for Fibonacci and Lucas sequences*, arXiv:2609.24544v1 (2026-09-21).
2. J. Jaidee, P. Moss, T. Ward, *Local structure of classical sequences, regular primes, and dynamics*, DOI:10.1007/s40993-026-00740-3 (2026).
3. *All local prime parts are Dold for split companion Lucas sequences*, published published-finding corpus research record, 2026-10-04 (positive square-discriminant hypothesis).
4. Fiebig, Mbirika, and Spilker, work on periods of companion Lucas sequences with second parameter \(-1\); relevant to periods, not Dold prime parts.
