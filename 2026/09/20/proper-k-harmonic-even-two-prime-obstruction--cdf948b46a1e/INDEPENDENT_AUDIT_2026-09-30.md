# Independent audit — 2026-09-30 UTC

Record: `2026/09/20/proper-k-harmonic-even-two-prime-obstruction--cdf948b46a1e`  
Assigned source tree: `126ed974824586984325c63f8140b45b6d1b6615`  
Audited current source tree: `126ed974824586984325c63f8140b45b6d1b6615`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `23778ecb6e9e3d936b17705166525e57baa894c0`  
Disposition: **passed**

## Correctness

**independently_supported**. The Zsigmondy argument is correct. Writing m=a+1, c=b+1, A=(2^(km)-1)/(2^k-1), B=(p^(kc)-1)/(p^k-1), k-harmonicity forces AB | 2^(ak)p^(bk)mc. A primitive prime s of p^(kc)-1 exists because p is odd and kc>=4; it divides B, has ord_s(p)=kc and therefore s>=kc+1>c. Since s is neither 2 nor p, divisibility forces s|m, hence m>=kc+1>c. Except for the sole relevant Zsigmondy exception km=6, a primitive prime r of 2^(km)-1 divides A and satisfies r>=km+1>m>c, so the same divisibility forces r=p and m|p-1. Then s|m gives p≡1 mod s, contradicting ord_s(p)=kc. When km=6, the only pairs (k,m)=(2,3),(3,2) already contradict m>=kc+1 for c>=2. No finite computation is used in the proof.

## Originality

**qualified_with_inaccessible_primary_source**. Cohen and Deng introduced k-harmonic numbers in 1998, and the accessible standard handbook summary records only weaker necessary congruence conditions for a hypothetical proper k-harmonic number 2^a p^b. Targeted searches under k-harmonic/power-harmonic, two-prime support and primitive-divisor terminology did not locate the complete nonexistence theorem. The 1998 primary article itself could not be obtained as lawful open full text, and an authorized institutional retrieval attempt returned no verified PDF. It is therefore not claimed as read and remains the decisive residual prior-art risk. Originality is supported only subject to that explicit limitation.

## Scientific value

**meaningful_uniform_structural_elimination**. The theorem removes the entire even two-prime-support search space for every k>=2, replacing previously recorded congruence restrictions by complete nonexistence. Since no proper k-harmonic number with k>=2 is known in the checked literature, this is a useful unconditional structural reduction for future searches.

## Independent checks

- Re-derived both primitive-prime order arguments and all Zsigmondy exceptional cases.
- Checked gcd(psi(C_{p^a}),p^a)=1 from psi(C_{p^a})=(p^(2a+1)+1)/(p+1)≡1 mod p.
- Verified that the handbook summary attributes only the weaker two-prime congruence restrictions to Cohen-Deng.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/20/proper-k-harmonic-even-two-prime-obstruction--cdf948b46a1e
- https://www.researchgate.net/publication/266699253_On_a_generalisation_of_Ore%27s_harmonic_numbers
- https://cjhb.site/Files.php/Books/%28Uncategorized%29/Handbook/Sandor-Crstici2004_Book_HandbookOfNumberTheoryII.pdf
- https://doi.org/10.1007/BF01692444
## Literature access note

Bibliographic and secondary-source searches located citations and a detailed handbook summary but no lawful readable full article. Authorized institutional retrieval was attempted after the open-access search and returned no verified PDF. The article is **not** claimed to have been read in full.

## Limitations

- Odd proper k-harmonic numbers with exactly two prime factors are not excluded.
- Even candidates with at least three distinct prime factors are not addressed.
- The complete Cohen-Deng 1998 primary paper was not accessible and is not claimed to have been read; an equivalent argument there remains a residual originality risk.
