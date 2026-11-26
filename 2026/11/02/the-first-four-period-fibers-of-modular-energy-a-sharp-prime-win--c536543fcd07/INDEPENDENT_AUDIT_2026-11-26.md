# Independent mathematical audit

## correctness

PASS

For energy at most 4, every omitted prime p costs at least floor(m/p) across its multiples. In the valuation step, the prime itself already divides n whenever p²≤m: this holds for 2 and 3 by m≥18 and for p≥5 by floor(m/p)≥p. Thus a first omitted power p^a has a≥2 and each of its multiples costs at least p^(a-1), giving total at least 5 by the case bounds in the proof. For p≤m/4, four positive multiples cannot all have remainder 1 because n is even. In (m/4,m/3] the residues at p,2p,3p would have to equal the same u∈{1,2} (adding p≥5 exceeds the budget), which would require u to be divisible by both 2 and 3. In (m/3,m/2] an active prime contributes u+u, so u=2; in (m/2,m] it contributes any single residue from 0 through 4. All these primes have exponent one, and the CRT both realizes each budget assignment in exactly one full-period class and excludes any other assignments. The independent upper-window costs give the negative-binomial expansion through degree four; the middle window contributes exactly s_m to coefficient four. At m=17 the upper primes 11,13,17 already give ten energy-three classes and the distinct class 2L_17/3 has remainder 3 only at k=9. A separate direct full-period replay gave (1,3,6,11,19) at m=17 and (1,3,6,10,16) at m=18, both with L_m=12252240.

## originality

PASS

The supported distinct content is the exact fixed-cutoff period histogram through energy four, including the middle-prime correction and sharp threshold. The remainder-sum object and its whole-period moments are not new. The strongest accessible comparators concern moments, extremal information, or distributional questions, not statements implying the coefficients.

## value

PASS

The exact low tail answers a natural distributional question left open by global moment formulas. It identifies where the prime-only law first acquires a middle-window contribution and where an exceptional prime power invalidates the proposed uniform range. The resulting low-degree polynomial is an exact reusable benchmark for broader modular-energy distributions, not simply a calculation at one small m.

The dated certificate retains the supplied scientific assessment, sources and limitations.
