# An exact census of bases admitting a negative-power congruence

## Finding
For \(m\ge3\), let \(B(m)\) be the number of invertible residues \(a\pmod m\) for which there is an integer \(n\ge1\) such that \(a^n\equiv-1\pmod m\). Factor
\[
m=2^e\prod_{i=1}^r p_i^{f_i},\qquad
\varphi(p_i^{f_i})=2^{s_i}u_i,\quad s_i\ge1,\quad 2\nmid u_i,
\]
where the \(p_i\) are distinct odd primes and \(e\ge0\).
If \(e\le1\), then \(r\ge1\), and
\[
\boxed{B(m)=\left(\prod_{i=1}^r u_i\right)
\sum_{j=0}^{s_*-1}2^{rj},\qquad s_*=\min_i s_i.}
\]
The contribution indexed by \(j\) counts precisely the bases with
\(\nu_2(\operatorname{ord}_{p_i^{f_i}}(a))=j+1\) for every \(i\).
If \(e\ge2\), then
\[
\boxed{B(m)=\prod_{i=1}^r u_i,}
\]
with empty product \(1\). Here the allowable bases are exactly those with
\(a\equiv-1\pmod{2^e}\) and
\(\nu_2(\operatorname{ord}_{p_i^{f_i}}(a))=1\) for all odd local factors.
If \(e\le1\), any admitted base has first negative exponent \(\operatorname{ord}_m(a)/2\). If \(e\ge2\), its first negative exponent is also half the full order and is odd.

## Assumptions and scope
The modulus \(m\) is an integer at least \(3\), and \(a\) is considered as a reduced residue class modulo \(m\). The local order is the least positive exponent giving residue \(1\). The valuation \(\nu_2(k)\) is the exponent of \(2\) in positive integer \(k\). The count includes all reduced residue classes, not just prime or positive small bases. A modulus divisible by exactly one factor \(2\) imposes no restriction beyond its odd part.

## Proof
**Odd prime-power lemma.** Let \(q=p^f\) for an odd prime \(p\). The unit group modulo \(q\) is cyclic of order \(\varphi(q)=2^su\), where \(u\) is odd. For an element of multiplicative order \(h\), the congruence \(a^n\equiv-1\pmod q\) is soluble if and only if \(h\) is even. Indeed \(-1\) is the unique order-two element in this cyclic group, and the unique element of order two in \(\langle a\rangle\), when it exists, is \(a^{h/2}\). Every suitable exponent satisfies \(n\equiv h/2\pmod h\). For \(1\le t\le s\), exactly \(2^{t-1}u\) units have \(\nu_2(h)=t\): choose one of the \(\varphi(2^t)=2^{t-1}\) elements of exact order \(2^t\) in the cyclic Sylow-two subgroup, and independently any of \(u\) odd-order components.

**Odd local compatibility.** For \(r\ge1\) odd prime-power factors, write \(h_i=\operatorname{ord}_{p_i^{f_i}}(a)\). If \(a^n=-1\) modulo every factor, then \(n\equiv h_i/2\pmod{h_i}\). In particular \(\nu_2(n)=\nu_2(h_i)-1\), so the valuations \(\nu_2(h_i)\) must all agree. Conversely, if their common value is \(t\ge1\) and \(H=\operatorname{lcm}(h_1,\ldots,h_r)\), then each ratio \(H/h_i\) is odd, and \(a^{H/2}=(a^{h_i/2})^{H/h_i}=-1\pmod{p_i^{f_i}}\). Thus the condition is sufficient and the least exponent is \(H/2\). If \(e=1\), the extra modulus \(2\) imposes no condition because every odd base has \(-1\equiv1\pmod2\). For common valuation \(t\), the local counting lemma gives \(\prod_i 2^{t-1}u_i\). Summation over \(1\le t\le s_*\) gives the first displayed formula.

**The higher two-primary factor.** Suppose \(e\ge2\) and \(a^n=-1\pmod{2^e}\). Reduction modulo \(4\) forces \(a\equiv3\pmod4\) and \(n\) odd. Since the unit group \((\mathbb Z/2^e\mathbb Z)^\times\) is a finite group of exponent a power of \(2\), the map \(x\mapsto x^n\) with \(n\) odd is a bijection on it. Thus \(a^n=-1\) implies \(a=-1\pmod{2^e}\). Conversely, this single local base satisfies the congruence for every odd exponent. At each odd prime power, the negative exponent is odd if and only if the local order has \(2\)-adic valuation \(1\). The odd local compatibility lemma supplies a common odd exponent, namely \(H/2\). Consequently the independent choices at odd prime powers number exactly \(\prod_i u_i\), and the CRT determines one global residue for each choice. For \(r=0\), just the residue \(-1\pmod{2^e}\) remains. This establishes the second formula. Since the exponent \(H/2\) is odd here and the local \(2\)-adic order equals \(2\), it also equals half of the full multiplicative order, completing the assertion about least exponents.

## Verification
The independent brute-force enumerator in `verify.py` compares the formula to direct cyclic-orbit tests for every integer modulus from \(3\) through \(400\), without relying on order formulas to decide individual residues. It checks \(398\) different moduli and prints `VERIFY_OK` if all comparisons match. The computation is supplementary; the proof above covers every modulus.

## Relationship to prior work
Klaška (2023) studies the least exponent in \(a^n\equiv-1\pmod m\), proves the prime-power order criterion and a local compatibility criterion for odd composite moduli (Theorems 9 and 10). Those theorems concern a **fixed base** and do not provide the aggregate number of admissible bases as the modulus varies. The present census uses their rank context while additionally counting cyclic-group order strata, combining the strata across prime-power factors, and handling the single distinguished \(2\)-power residue. The existence criterion itself is not claimed to be new.

## Limitations
This is an elementary exact counting theorem, not a new algorithm for factoring moduli or a result on the distribution of prime moduli. The input factorization is assumed known. The count does not determine the distribution of exact least negative exponents or the average of \(B(m)\) over varying \(m\). A source deriving this same count from the familiar cyclic-group criterion could exist outside the inspected literature; the general group-theoretic tools are classical.

## References
1. Jiří Klaška, “Jakóbczyk's Hypothesis on Mersenne Numbers and Generalizations of Skula's Theorem,” *Journal of Integer Sequences* **26** (2023), Article 23.3.8, published March 17, 2023, especially Theorems 9 and 10. https://cs.uwaterloo.ca/journals/JIS/VOL26/Klaska/klaska6.pdf
2. Classical cyclicity of \((\mathbb Z/p^f\mathbb Z)^\times\) for odd prime \(p\), and the Chinese remainder theorem, as standard background facts in elementary algebraic number theory.
