# Self-review

## Correctness — PASS

The object is the level-\(i\) avoidance density for a fixed finite nonempty set of forbidden primes. Its depth recursion gives the uniquely minimal depth-\(i\) witness \(M_i\). For large \(i\), the next witness in the same depth class is at least \(2M_i\); a witness using another permitted prime has base at least \(s>r\). The proven Euler products have strictly positive limiting factors and tails controlled by sums of \(p^{-M_i}\). The unique valuation event \(v_r(n)=M_i\) yields the leading constant. Exact recurrence and truncated Euler-factor tests passed for finite cases, but no finite experiment is used to prove the asymptotic. The conclusion does not interchange natural-density and depth limits without establishing them.

## Originality — PASS, qualified

The nearest 2026 work proves finite-level density products; the 2014 work proves complete prime-tower density for one forbidden prime. Both are attributed. The new assertion is the *sharp leading asymptotic in the truncation depth* for every finite forbidden prime set, including an explicit positive Euler-product coefficient. The 2023 paper's total-height distribution and tower upper bounds omit prime-label constraints, and the 2025 paper's single-tree enumerations similarly do not imply the coefficient. The OEIS catalog lists the singleton complete-avoidance sequence, not the level-error asymptotic. Priority uncertainty from unindexed or implicit derivations remains.

## Mathematical value — PASS

The exact tower scale and positive leading constant quantify how quickly the finite-level arithmetic density captures the complete recursive-mosaic condition; the distinction is natural because the 2026 fixed-level results and 2014 complete-level results do not quantify the depth gap. The uniquely minimal witness explains the asymptotic structurally, and the result applies uniformly in level for every fixed finite forbidden-prime set, not to an arbitrary finite slice.

## Closest literature and limits

- Dao–Kasian–Mirabi, arXiv:2606.22842, Theorem 7.3: finite-level Euler products, not sharp level-limit correction.
- Devlin–Gnang, arXiv:1204.5251v2, Theorem 1/Proposition 2: full-tower density for single primes, not depth error.
- De Koninck–Verreault, arXiv:2308.09149, Section 6: total-height bounds, which do not resolve labeled forbidden-prime depth events.
- Conti–Contucci–Iudelevich, arXiv:2512.01376, Theorem 2.3: single unlabeled tree-shape asymptotics, not avoidance of specified prime labels.

The theorem is asymptotic as depth increases with the forbidden set fixed. The coefficient need not admit an elementary closed form. Independent audit is still necessary.

Self-review: passed. Independent audit: not yet performed.
