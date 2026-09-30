# Independent Audit — 2026/09/20/lucas-carmichael-primitive-three-prime-uniqueness--fd644204c2f1

- Audit date: 2026-09-30 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `b77fc1610f04ccada10899af36c6de2e882866b0`
- Disposition: **PASSED**

## Correctness

**PASS** — The Diophantine classification is correct. From gcd(p+1,q+1,r+1)=2, writing p=2a-1, q=2b-1, r=2c-1 gives gcd(a,b,c)=1; the Lucas-Carmichael divisibilities force pairwise coprimality. Hence lcm(p+1,q+1,r+1)=2abc and T=(n+1)/(2abc) is an integer below 4, so T is 1, 2, or 3. The resulting equation c((4-T)ab-2a-2b+1)=2ab-a-b excludes T=1 and T=2 in the record's lambda notation except the lambda=1 branch, where c>b forces a<=4. The a=2 and a=4 cases are impossible and a=3 leaves only (a,b,c)=(3,7,16) after pairwise-coprimality and ordering constraints. Direct independent enumeration of the full Diophantine equation for 2<=a<100 and a<b<300 found exactly this solution. The converse 2015=5*13*31 is immediate.

## Originality

**PASS** — Tamilvanan--Muthukrishnan Theorem 4.2 proves only the general representation (2hr_1-1)(2hr_2-1)(2hr_3-1) with pairwise-coprime r_i; its inspected theorem text does not classify h=1. OEIS A006972 lists 2015 and records a broader normalized-gcd conjectural observation, but not the audited uniqueness theorem. Exact and synonymous searches for gcd(p+1,q+1,r+1)=2 and 2015 did not reveal a prior proof. The result is elementary enough that older problem-literature priority remains a real but limited risk.

## Scientific value

**PASS** — The theorem gives a complete infinite-range classification of the primitive three-prime case rather than a computation under a cutoff. It sharpens the recent structural decomposition by resolving its minimal common-gcd branch exactly. The scope is narrow, but the statement is clean and nontrivial.

## Sources

- **A new characterization for the Lucas-Carmichael Integers and sums of base-p digits** — Sridhar Tamilvanan; Subramani Muthukrishnan. https://arxiv.org/abs/2311.08012 — Theorem 4.2 gives the three-prime normalized-gcd decomposition with pairwise-coprime factors, but not uniqueness of the h=1 case.
- **There are infinitely many elliptic Carmichael numbers** — Thomas Wright. https://doi.org/10.1112/blms.12185 — Establishes infinitude of Lucas-Carmichael numbers; background rather than the primitive three-prime classification.
- **OEIS A006972: Lucas-Carmichael numbers** — OEIS contributors. https://oeis.org/A006972 — Sequence data include 2015 and a normalized-gcd comment, but no uniqueness theorem matching the audited statement.

## Limitations

- Only the exactly-three-prime-factor case and minimal shifted-factor gcd are classified.
- The theorem does not classify h>1 or Lucas-Carmichael numbers with four or more prime factors.
- Because the proof is elementary, differently indexed older problem literature remains a residual originality risk.

## Independent checks

```json
{
  "proof_reconstructed": true,
  "diophantine_enumeration_a_lt_100_b_lt_300_unique": true,
  "tamilvanan_theorem_4_2_text_checked": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation or separate dispatcher report was performed. Open-access and preprint sources were checked first; no decisive comparison remained inaccessible, so Oxford Download was not required.
