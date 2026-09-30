# Independent Audit — 2026/09/19/full-gap-divisibility-binary-linear-codes--e02f7c6a431d

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `d003398725ba62f0f1f79a92c0cd416c5d9de2c6`
- Disposition: **PASSED**

## Correctness

**PASS** — The argument follows exactly from the Ashikhmin-Barg minimal-vector properties. Under the full gap through M=n-k+1, every minimal codeword must have weight d because every minimal support has size at most M. In a binary code each nonminimal word decomposes into two nonzero proper subwords with disjoint supports; induction on weight therefore decomposes every codeword into pairwise support-disjoint minimum words, forcing d-divisibility. For two minimum words x,y, wt(x+y)=2d-2s is a positive multiple of d in [d,2d], so the intersection size is 0 or d/2. When d is odd, all minimum supports are disjoint; since minimal vectors span the code, there are exactly k independent minimum words and the code is a direct sum of k length-d repetitions plus zero coordinates. The full-gap condition applied to a weight-2d word then forces k=2,z=0, while for k≥3 the inequality fails because (k-2)d+z-k+1>0 for odd d>1. No hidden step requires the newer mirror theorem.

## Originality

**PASS** — He’s September 2026 note uses the same classical disjoint-support lemma to produce a local mirror vanishing band near 2d, but does not state the global d-divisibility consequence of a gap extending all the way to the universal minimal-support ceiling. Chubenko-Kurz study codes that are themselves minimal and divisible, a different class; their work does not supply the implication that an arbitrary binary code whose minimal codewords all have one weight must be divisible. Targeted searches for the exact 'all minimal codewords have common weight' implication and the odd-distance full-gap classification found no covering theorem. The proof is short once the classical lemma is noticed, so folklore risk is material, but the specific global closure and rigidity statement remains distinct from the located literature.

## Scientific value

**PASS** — The result identifies the endpoint at which a local weight-gap hypothesis becomes a global arithmetic structure theorem, and the odd-distance corollary sharply rules out such gaps in dimension at least three. It is useful as a clean structural complement to the recent mirror-band theorem and may simplify exclusion arguments for binary weight distributions. Scientific value is moderate rather than broad because the hypothesis is strong and the recursive decomposition is binary-specific.

## Sources

- A Mirror Vanishing Band for Weight Distributions of Binary Linear Codes (Xianmang He): https://arxiv.org/abs/2609.20344 — Immediate motivating source; proves a local mirror vanishing band using the binary disjoint-support decomposition of nonminimal words.
- Minimal Vectors in Linear Codes (Alexei Ashikhmin; Alexander Barg): https://doi.org/10.1109/18.705584 — Classical source for the minimal-support ceiling, spanning by minimal vectors, and binary disjoint-support decomposition used in the proof.
- Divisible Minimal Codes (Sascha Kurz; Vladislav Chubenko): https://arxiv.org/abs/2312.00885 — Background on codes that are both minimal and divisible; distinct from the audited implication for arbitrary codes with equal-weight minimal vectors.

## Limitations

- The full gap through n-k+1 is much stronger than the short initial band in He's theorem.
- The disjoint-support recursion is binary-specific.
- No complete classification is obtained for even minimum distance.
- Because the proof is a short consequence of a 1998 lemma, undocumented folklore remains a meaningful originality risk.

## Independent checks

```json
{
  "proof_reconstructed_from_classical_lemma": true,
  "odd_distance_inequality_checked": true,
  "source_tree_unchanged": true
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Open-access/preprint sources were checked first. The scientific conclusions above are independent of the record's same-model review.
