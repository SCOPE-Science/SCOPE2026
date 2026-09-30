# Independent Audit — 2026/09/21/admirable-two-prime-support-converse--69b8ac762f3d

- Audit date: 2026-09-30 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `bb7ac21c315cdfd6e7b1447aea77302036d62648`
- Disposition: **PASSED**

## Correctness

**PASS** — The converse classification checks. Writing M=2^(a+1)-1 and G_b=1+p+...+p^(b-1), the excess E=M G_b-p^b must equal twice one proper divisor. Parity forces b odd. For b=1, splitting the possible divisor into 2^s and 2^s p yields exactly the binary-deviation, isolated n=40, and even-perfect-divisor branches; the order of 2 modulo 2^h+1 is indeed 2h. For odd b>=3, the cases u=v_p(M)=0, 1<=u<b, and u>=b give respectively a size contradiction, the unique b=3 Mersenne-cube branch, and an LTE/geometric-sum contradiction. An independent exact-rational enumeration over 1<=a<=12, odd primes p<1000, and 1<=b<=7 found 29 admirable triples and zero disagreements with the theorem.

## Originality

**PASS** — Firoozbakht-Hasler supply the individual sufficient construction mechanisms but not the two-prime-support converse. The original 1960 Sachs paper was obtained through authorized institutional access after open-access attempts and checked in full (three pages); it introduces admirable numbers, examples, and elementary conjectures but contains no such classification. Current OEIS material likewise records constructions/data rather than the converse. Targeted formula searches found no antecedent. The theorem is therefore a genuine converse synthesis on the stated support slice.

## Scientific value

**PASS** — The theorem turns several known sufficient constructions into an exhaustive classification: the odd-prime exponent is forced to be 1 or 3, all odd exponents at least 5 are excluded, and b=3 is exactly the Mersenne-cube family. This is a clean rigidity result for a natural arithmetic subfamily, while leaving larger prime support and two-odd-prime support open.

## Sources

- **Variations on Euclid's Formula for Perfect Numbers** — Farideh Firoozbakht; M. F. Hasler. https://cs.uwaterloo.ca/journals/JIS/VOL13/Hasler/hasler2.pdf — Open full text checked; contains the sufficient binary-deviation, Mersenne-cube, and perfect-divisor constructions.
- **Admirable Numbers and Compatible Pairs** — J. M. Sachs. https://www.jstor.org/stable/41184328 — Authorized full text checked, pages 293-295; it introduces the notion and elementary examples/generalizations, not the audited converse.
- **OEIS A111592: Admirable numbers** — OEIS Foundation. https://oeis.org/A111592 — Current data/construction reference; no equivalent two-prime-support converse was located.

## Limitations

- The classification is restricted to n=2^a p^b with one odd prime p.
- It does not classify admirable integers supported on two odd primes or on at least three primes.
- The term 'admirable' has had broader pedagogical sign conventions historically; the theorem uses the explicit one-subtracted-divisor definition stated in the record.

## Independent checks

```json
{
  "proof_case_split_reconstructed": true,
  "order_mod_2h_plus_1_argument_checked": true,
  "lte_high_valuation_branch_checked": true,
  "independent_enumeration_box": {
    "a_max": 12,
    "p_lt": 1000,
    "b_max": 7
  },
  "independent_enumeration_hits": 29,
  "independent_enumeration_mismatches": 0,
  "sachs_full_text_checked": true,
  "oxford_used": true,
  "oxford_job_id": "75667b6a5fe54dae6aa4d5071454cc13",
  "oxford_status": "complete",
  "oxford_pages_checked": "1-3 of 3"
}
```

GitHub was used only as read-only evidence and no repository mutation or separate dispatcher report was performed. The assigned source tree was unchanged between the inventory commit and the source-tree-check commit. Open-access/preprint sources were checked before authorized institutional retrieval. Inaccessible material is explicitly identified and is not claimed read.
