# Self-review

**Correctness — PASS.** The proof partitions all initial pairs by \(\gcd(a,b,m)\), reduces to primitive pairs modulo each divisor, and uses the invertible companion map. The rank identity \(U^{z(d)}=cI\) and the unit property of \(c\) show each primitive first-hit index from \(0\) through \(z(d)-1\) has exactly \(\varphi(d)\) disjoint witnesses. This checks normalization at \(t=0\), the zero pair, composite moduli, and \(m=1\). Exact finite replay independently confirms \(90\) complete moduli but is not an infinite proof.

**Originality — PASS, with residual risk.** The exact total \(\sum_{d\mid m}\varphi(d)z(d)\) already appears as an OEIS conjecture (2017) and identity (2021), and is explicitly treated as known prior coverage. The **new assessed claim** is the full waiting-time histogram, uniform gcd-stratum splitting, and exact waiting-time moment. Material passages of Avila–Khovanova and Renault, the OEIS entries, and targeted equivalent-formulation searches were compared by mathematical implication, not just title. No directly covering time-refined result was located. General recurrence-dynamics literature could imply it implicitly and remains a real risk.

**Mathematical value — PASS.** The 2001 zero-forcing question and the 2013 count sequence motivate a first-passage law. The distribution supplies new exact timing information that the published total cannot determine: a monotone staircase with explicit jumps at divisor ranks, all gcd-conditioned masses, and an exact conditional mean. It completely settles the natural first-hitting-time problem for this family rather than an arbitrary parameter slice.

**Limitations.** The method uses rank-of-apparition data and does not compute those ranks from prime factorization alone; other linear recurrences, exact dynamical division processes, and historical equivalence outside inspected material remain open. Finite replay is corroboration only.

Self-review: passed. Independent audit: not yet performed.
