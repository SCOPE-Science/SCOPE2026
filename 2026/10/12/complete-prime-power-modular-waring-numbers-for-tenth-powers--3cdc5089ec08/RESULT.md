# Complete prime-power modular Waring numbers for tenth powers

## Finding

For each positive integer \(m\), let \(\gamma(10,m)\) be the least positive integer \(t\) such that every residue modulo \(m\) is a sum of at most \(t\) tenth powers of integers. Zero summands may be used to pad an expression.

**Complete prime-power classification.** For powers of \(2\), the sequence at exponents \(1,2,3\) is \(1,3,7\) and is permanently \(8\) from exponent \(4\) onward. For powers of \(5\), the value is \(2\) at exponent \(1\), and \(12\) at all larger exponents.

For every odd prime \(p\ne5\), \(\gamma(10,p)=2\), except for the following exceptions (grouped by value):

- \(\gamma(10,p)=10\) for \(p=11\), and \(\gamma(10,p)=5\) for \(p=31\).
- \(\gamma(10,p)=4\) for \(p\in\{41,61\}\).
- \(\gamma(10,p)=3\) for \(p\in\{71,101,131,151,181,191,211,241,251,271,281,311,331,401,421,431,461,491,641,911\}\).

For every odd prime \(p\ne5\) and every exponent \(a\ge2\), the **baseline** is
\[
\gamma(10,p^a)=\begin{cases}2,&p\equiv1\pmod4,\\3,&p\equiv3\pmod4.\end{cases}
\]
Exactly the following exceptions override the baseline:

- Value \(11\) for \(p=11\), and value \(5\) for \(p=31\).
- Value \(4\) for \(p\in\{41,61,71,131,311,431,491,911\}\).
- Value \(3\) for \(p\in\{101,181,241,281,401,421,461,641\}\) (these eight primes ordinarily have baseline \(2\)).

All exceptional primes, the two exact values, and the shortest nontrivial zero-sum lengths appear in `prime_exceptions.csv`. For every integer \(m>1\), the Chinese remainder theorem yields
\[
\gamma(10,m)=\max_{p^a\parallel m}\gamma(10,p^a).
\]
Consequently \(\sup_{m\ge1}\gamma(10,m)=12\). The global \(12\) follows already from older general bounds and special cases; the genuinely refined assertion here is the complete local classification with its finite exceptional-prime spectrum.

## Assumptions and scope

All primes are ordinary rational primes; \(a\) ranges over all integers \(a\ge1\). The integer bases are unrestricted, and the modulus may be any positive integer. Throughout, \(H_p=\{u^{10}:u\in\mathbb F_p^\times\}\) and \(tH_p\) is the set of sums of exactly \(t\) elements of \(H_p\), while \(\{0\}\cup H_p\) includes the zero tenth power. Define \(z_p\) as the smallest \(t\ge2\) such that \(0\in tH_p\). For \(m=1\), the stipulated least positive value is \(1\).

## Proof

**1. Prime-to-ten lifting and its exact converse.** Assume \(p\) is odd and \(p\ne5\). Let \(g_p\) be the least number of summands covering \(\mathbb F_p\). Every representation of a nonzero residue modulo \(p\) uses at least one nonzero base. A representation of zero with at least one nonzero base exists with exactly \(z_p\) summands, and none shorter does (the zero-padding terms are irrelevant). Thus every residue has a representation with a nonzero base using at most \(\max(g_p,z_p)\) terms. Since \(p\nmid10\), changing this nonzero base by a multiple of \(p^j\) changes its tenth power modulo \(p^{j+1}\) by every prescribed multiple of \(p^j\). Ordinary Hensel lifting therefore gives
\[
\gamma(10,p^a)\le\max(g_p,z_p)\qquad(a\ge2).
\]
Reduction modulo \(p\) gives the reverse bound \(\gamma(10,p^a)\ge g_p\). In addition, any representation of \(p\) modulo \(p^2\) must include a base coprime to \(p\): otherwise all tenth powers vanish modulo \(p^2\). Reduction of such a representation gives a nontrivial zero-sum modulo \(p\), forcing at least \(z_p\) summands. Hence, for **all** \(a\ge2\),
\[
\boxed{\gamma(10,p^a)=\max(g_p,z_p).}
\]

**2. Uniform control for large primes.** Let \(p\ge6000\) be prime. For each \(c\in\mathbb F_p^\times\), the smooth plane Fermat curve \(X^{10}+Y^{10}=cZ^{10}\) has genus \((10-1)(10-2)/2=36\). The Hasse–Weil bound gives at least \(p+1-72\sqrt p\) rational projective points. At most \(10\) have \(Z=0\), and at most \(10\) have each of \(X=0\) and \(Y=0\). Thus there are at least \(p-29-72\sqrt p>0\) affine points with both coordinates nonzero. For the last inequality, \(\sqrt p\ge\sqrt{6000}>77\) implies \(72\sqrt p<(72/77)p\), hence \(p-29-72\sqrt p>(5/77)p-29>0\).

It follows that **every nonzero element** of \(\mathbb F_p\) is the sum of two nonzero tenth powers. The tenth-power subgroup is proper because \(\gcd(10,p-1)\ge2\), so \(g_p=2\). For zero, a two-term nontrivial representation exists precisely when \(-1\in H_p\), which is equivalent (by cyclicity of \(\mathbb F_p^\times\)) to \(p\equiv1\pmod4\). Otherwise \(-1=u^{10}+v^{10}\) for units \(u,v\) from the preceding conclusion, so \(0=1+u^{10}+v^{10}\) and \(z_p=3\). This gives the claimed baseline for **every** \(p\ge6000\), with no finite-sample extrapolation.

**3. Exact finite classification.** For the \(781\) odd primes \(p<6000\) other than \(5\), the standalone `verify.py` uses exact integer residue masks. It generates \(H_p\), repeatedly forms the sumsets \(t(\{0\}\cup H_p)\) to determine \(g_p\), and separately forms \(tH_p\) to determine \(z_p\). All residues are enumerated; no probabilistic primality tests, floating-point tolerances, or truncated unverified branches are used. The complete table of primes differing from the generic prime/baseline values is `prime_exceptions.csv`. Its \(24\) rows yield exactly the \(24\) first-power exceptions and \(18\) higher-power exceptions stated above. Recomputing and comparing the entire CSV is part of the verifier; it also independently tests selected actual squares of primes.

**4. Primes dividing the exponent.** For \(p=2\), the tenth powers of odd residues modulo \(2^a\) for \(a\ge3\) are exactly the residues congruent to \(1\pmod8\): the odd squares form this subgroup, and raising a square to the fifth power is a permutation of it. An arbitrary target modulo \(2^a\) is therefore a sum of at most \(8\) tenth powers by selecting its residue count modulo \(8\) and adjusting one odd summand. Modulo \(16\), exactly eight are required to represent the residue \(8\): tenth powers are \(0,1,9\), and a sum of at most seven such residues cannot equal \(8\pmod{16}\). Direct residue enumeration gives \(\gamma(10,2)=1\), \(\gamma(10,4)=3\), and \(\gamma(10,8)=7\).

For \(p=5\), tenth powers modulo \(25\) are exactly \(0,1,-1\). Every residue has a representative between \(-12\) and \(12\), hence is represented by at most \(12\) such summands; the residues \(12\) and \(13\) need all \(12\). Each residue also has a representation with a unit base (for zero use \(1+(-1)\)). Since \(5\) divides the exponent \(10\) exactly once, a unit base can be varied by \(5^{a-1}\) to lift a representation modulo \(5^a\), \(a\ge2\), to any prescribed residue modulo \(5^{a+1}\). The linear coefficient is \(2u^9\) after division by \(5^a\), a unit modulo \(5\), and all higher binomial terms vanish at this precision. Thus the bound \(12\) holds at every higher power. Direct computation modulo \(5\) gives \(2\).

**5. Composite moduli.** If \(m=\prod p_i^{a_i}\), padding representations to the maximum local length and applying the Chinese remainder theorem to each variable gives the global maximum formula. Conversely, reducing a representation modulo each prime power yields the matching lower bound. This completes the proof.

## Verification

Run `python3 verify.py` in the same directory as `prime_exceptions.csv`. The code is standalone Python standard library. It must reproduce the full exception CSV byte-for-byte, scan all \(781\) relevant primes below \(6000\), check powers of \(2\) through exponent \(10\), powers of \(5\) through exponent \(5\), and directly evaluate \(11\) illustrative odd-prime-square moduli. Expected output is included in `verification_output.txt`. No finite check substitutes for the stated Hasse–Weil and Hensel arguments.

## Relationship to prior work

Arias, Borja, and Anaya (2023) formulate these modular Waring numbers and display global values for exponents \(2\) through \(9\); their Table 3 does not determine the tenth-power local prime-power spectrum. Alnaser and Cochrane (2008) provide general bounds, an exact \(2\)-adic theorem by Subocz, and the special \(5\)-adic extremal identity covering \(\gamma(10,5^a)=12\). Cipra, Cochrane, and Pinner (2007) prove general prime-field bounds and formulas for some very small power-residue subgroups. These earlier results **already imply the global bound** \(\gamma(10)=12\), but do not give the present complete, sharply exceptional local classification. The two-step structure of the prime-to-ten argument also explains when the first prime-power layer has strictly larger Waring number than the underlying prime field.

## Limitations

The table is specific to exponent \(10\). The large-prime argument invokes the established Hasse–Weil estimate for smooth curves; the finite verifier implements only its exact arithmetic consequence at the cutoff, not a proof of Hasse–Weil itself. A historically published equivalent complete prime-power table may exist outside the inspected literature, particularly in the older work of Small (1977), which was not available for full-text inspection. The global bound \(12\) is not claimed as independently new. Independent external validation has not been performed.

## References

1. F. Arias, J. Borja, and S. Anaya, *Counting Integers Representable as Sums of k-th Powers Modulo n*, Journal of Integer Sequences **26** (2023), Article 23.8.1, publicly published August 28, 2023; primary MSC2020 11A07. https://cs.uwaterloo.ca/journals/JIS/VOL26/Borja/borja4.pdf
2. A. Alnaser and T. Cochrane, *Waring's number mod m*, Journal of Number Theory **128** (2008), 2582–2590. https://www.math.ksu.edu/~cochrane/research/waringmodm.pdf
3. J. A. Cipra, T. Cochrane, and C. Pinner, *Heilbronn's conjecture on Waring's number (mod p)*, Journal of Number Theory **125** (2007), 289–297. https://www.math.ksu.edu/~cochrane/research/heilbronn.pdf
4. C. Small, *Waring's problem mod n*, American Mathematical Monthly **84** (1977), 12–25 (bibliographic reference; full text not inspected).
