# Finite-Blocklength Jigsaw Ledger for the Li–He–Tang Marker–Codeword–Marker VT Family (n=32, N=1024)

## Record statement

At segment length n=32 and total blocklength N=1024 over the binary segmented
single-deletion channel (32 segments, at most one deletion per segment, segment
boundaries unknown to the receiver), the Li–He–Tang marker+codeword+marker VT
family — per segment `s = b·v·a` with `v` in `VT_0(26;25)` minus `0^25`,
`b = v_1` (R1), `a` in `{A0=000010, A1=111101}` with `a^(i)=A1 iff b^(i+1)=0`
(R2, `a^(32)=A0` fixed) — with the explicit deletion-only jigsaw decoder
achieves 20 information bits per segment (640 bits over N=1024, rate
0.625 ≥ 0.60) at deterministic zero block error (hence block error ≤ 1e-3),
proving R*(1024,1e-3) ≥ 0.60. The family codebook holds at most 1290556^32
words, so no block-by-block decoder for the same family exceeds rate
log2(1290556)/32 ≈ 0.6343613 < 0.68, the stated envelope.

## Context

Segmented edit channels (at most one edit per segment, unknown boundaries)
were introduced by Liu–Mitzenmacher and developed by Abroshan et al.
(arXiv:1701.06341), who built zero-error segment-by-segment codes from VT
subsets with prefix/suffix conditions and proved rate bounds of the form
R ≥ 1 − log2(b+1)/b − κ/b with a matching general upper bound. The recent
Li–He–Tang "Marker+Codeword+Marker" structure (IEEE doc. 11206538) proposes a
coupled `b+v+a` construction with redundancy log2(n−6)+7 and a jigsaw decoder
that resynchronizes by markers. The admitted TARGET asked for the concrete
finite-blocklength ledger of this named family at n=32, N=1024 around rate
0.60 with a 0.68 block-by-block envelope. This record resolves that ledger.

## Definitions

- Channel: binary segmented single-deletion channel, N=1024 = 32×32, each
  32-bit segment suffers 0 or 1 deletions; boundaries unknown.
- Family: per segment `s^(i) = b^(i)·v^(i)·a^(i)`; `v^(i)` is a 25-bit
  `VT_0(26;25)` codeword (checksum Σ i·v_i ≡ 0 mod 26) excluding `0^25`;
  `b^(i)=v^(i)_1`; `a^(i) ∈ {000010,111101}` with R2 coupling above.
- Decoder: for each non-final segment at position `pos`, if the 6-bit window
  `y[pos+26:pos+32]` is a marker declare no deletion (value
  `y[pos+1:pos+26]`, advance 32); else declare one deletion (value
  `vt_decode_del(y[pos+1:pos+25])`, advance 31). Final segment by remaining
  length (32/31). `vt_decode_del` is the standard linear-time VT
  checksum-deficiency inversion (D ≤ R → deleted 0; else deleted 1 via
  monotone `f(p)=p+#{ones ≥ p}`).
- Rates: explicit subcode 2^20 words/segment → 640/1024 = 0.625; full-family
  rate log2(1290555)/32 ≈ 0.63436; unconstrained VT ceiling
  log2(1290556)/32 ≈ 0.6343613.

## Result

R*(1024,1e-3) ≥ 0.60 is achieved with zero error (error exactly 0 over all
33^32 admissible deletion patterns), and the family-scoped envelope 0.68
holds since 0.6343613 < 0.68 with margin ≈ 0.0456. The achievability margin
is 0.025 (≈ 25.6 bits of slack); both inequalities use exact integer counts
and are robust to rounding.

## Proof / evidence

1. VT census (exact DP over Σ i·v_i mod 26, k=25): residue-0 coset has
   1290556 words; usable alphabet minus `0^25` has 1290555 ≥ 2^20=1048576.
   Redundancy 32−log2(1290555) ≈ 11.70 bits matches LHT log2(26)+7.
   Independently re-verified by forward DP (sum 2^25) and by
   checksum(1^25)=325≡13≢0 confirming only `0^25` is removed.
2. Codec: lexicographic rank/unrank via suffix-count table; roundtrip checked
   on edge ranks {1,2,2^19,2^20} + 2000 random ranks.
3. VT inversion: standard D/R/f(p) algebra; uniqueness of the admissible
   preimage checked by exhaustive preimage enumeration on 3000 random
   (codeword, deletion) pairs plus all 25 deletions of 556 codewords.
4. Jigsaw sync (Lemma 1): window non-forgery proved by exhaustion — d≤26:
   `a[1:]+nextbit` ∈ {000100,000101,111010,111011}, never a marker (4 combos);
   d∈27..31: `(a minus one bit)+nextbit` never a marker (20 combos);
   d=32: `a[0:5]+nextbit` forges only if next bit equals the deleted last
   marker bit, which the R2 coupling (`A1 iff next b=0`; A1 ends in 1, A0
   ends in 0; first surviving bit of next segment always equals its `b`
   since `b=v_1`) makes impossible for non-final segments. Verified by 1089
   adjacent-pair exhaustive tests with zero window/truth mismatches.
5. Value recovery (Lemma 2): every deletion-branch candidate is a genuine
   single-deletion trace of the true `v` (d=1: `v` minus first bit; d=2..26:
   `v` minus one bit; d=27..32: `v` minus last bit), so VT decoding is exact;
   confirmed trace fractions 200/200 across all deletion positions.
6. End-to-end: 6346 blocks / 203072 segments with exact message equality and
   full-consumption (`pos==M`) assertions, zero failures (1000 random blocks,
   3168 single-segment sweep blocks, 2178 paired-segment grid blocks);
   plus independent corner patterns (all-clean, all-31, d=1/d=32 everywhere).
7. Ledger arithmetic: 32·20/1024=0.625≥0.60; log2(1290555)/32≈0.63436;
   log2(1290556)/32≈0.6343613<0.68.

## Limitations

Deletion-only scope (insertion/substitution branches of the full LHT insdel
machinery not re-verified); the 0.68 statement is a family codebook-counting
envelope, not a channel converse (segmented-deletion capacity at b=32 is
≈0.80+); rate 0.625 uses an integer-bit 2^20 subcode leaving ~20% of the
1290555-word alphabet unused (family supports ≈0.63436 with non-integer-bit
mapping); exposition slips corrected here — the DRAFT's "all other cosets
1290555" omits the second maximal coset (residue 13, also 1290556; total
26·1290555+2=2^25), immaterial to the ledger, and Lemma 2's "NOT a trace"
aside is over-cautious since all candidates are genuine traces.

## Reproducibility

`output/artifacts/ledger.py` (stdlib + numpy, fixed seeds 1141/7/21/3/11/…):
`python3 output/artifacts/ledger.py` reproduces `ledger_results.json`
(ledger + verification counts) and prints ALL CHECKS PASSED. Independent
checks above used the same file plus small driver scripts for window
exhaustion, preimage uniqueness, and adjacent-pair grids.

## References

- Abroshan–Venkataramanan–Guillén i Fàbregas, "Coding for Segmented Edit
  Channels", arXiv:1701.06341v4 (2018): channel model, VT background,
  prefix/suffix VT subsets, rate bounds, Table I.
- Li–He–Tang, "Marker+Codeword+Marker: A Coding Structure for Segmented
  Single-Insdel/-Edit Channels" (IEEE Xplore staging doc. 11206538; workspace
  `mcm_paper.gz` v7): MCM structure b+v+a, markers A0/A1, R1/R2,
  log2(n−6)+7 redundancy, jigsaw/appendix analysis.
- Error Correction Zoo, "Varshamov-Tenengolts (VT) code" (vt_single_deletion):
  definition, single-deletion/insertion correction, log(n+1) redundancy.
- Wang–Duman–Aktas, "Capacity Bounds and Concatenated Codes over Segmented
  Deletion Channels" (IEEE TCOMM 2013, 10.1109/tcomm.2012.010213.110836).
- Jiao et al., "On Prefixed Varshamov-Tenengolts Codes for Segmented Edit
  Channels" (IEEE TCOMM 2022, 10.1109/tcomm.2022.3146285).
