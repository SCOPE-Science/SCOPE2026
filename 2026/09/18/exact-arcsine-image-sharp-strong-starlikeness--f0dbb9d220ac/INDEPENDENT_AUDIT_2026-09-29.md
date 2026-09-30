# Independent audit — Exact normalized-arcsine image and sharp strong-starlikeness

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/18/exact-arcsine-image-sharp-strong-starlikeness--f0dbb9d220ac`
**Audited tree:** `7350c419ba81979a07c651d113379891a35bee6f`

## Disposition

**PASSED.** The record survives independent review on correctness, originality, and scientific value without a substantive research-file change.

## Correctness

The exact image formula is correct: writing z=sin(u+iv) on the principal inverse-sine strip gives |z|^2=sin^2 u+sinh^2 v, and the affine normalization w=1+2(u+iv)/pi yields exactly the submitted inequality. The convexity test, Catalan-area integral, sharp sector |arg w|<pi/4, and the canonical Ma--Minda extremal establishing sharp strong-starlikeness order 1/2 all check independently.

### Independent checks

- Re-derived the exact image in both directions from the principal-strip identity |sin(u+iv)|^2=sin^2(u)+sinh^2(v).
- Checked 1+z phi''/phi'=1/(1-z^2) and Re(1/(1-z^2))>1/2 on the unit disk.
- Independently evaluated the area integral I(1)=int_0^{pi/2} asinh(sin t) dt=G and hence area=16G/pi^2; numerical evaluation gives 1.4849074908430888.
- Checked the sharp sector by Y(x)/x->1 at the cusp and verified that the canonical solution of z f'/f=phi belongs to the class.
- Independently inspected the full companion convex preprint arXiv:2607.27293; it uses leaf-shaped terminology but does not supply the submitted exact geometric package.

## Originality

PASS to the best of current searchable knowledge. The motivating starlike preprint arXiv:2609.20288 states the full-strip image that the record corrects. The closest companion convex preprint arXiv:2607.27293 was independently inspected in full text during this audit: it calls the target leaf-shaped, but no exact sinh/sine boundary, Catalan-area formula, sharp pi/4 sector, or strong-starlikeness consequence was found. The inverse-sine identities themselves are classical and are not treated as novel.

### Literature checked

- https://arxiv.org/abs/2609.20288 — Panja–Banerjee–Majumder, the motivating starlike Ma--Minda paper; its geometric identification is the strip statement corrected by this record.
- https://arxiv.org/abs/2607.27293 — Panja–Banerjee–Banerjee–Majumder, companion convex class; full text independently inspected in this audit and no matching exact image/sector/area theorem was found.
- https://dlmf.nist.gov/4.15 — Classical inverse-trigonometric identities; used only as background, not as an originality claim.

## Scientific value

Replacing the defining target from an unbounded strip to its exact bounded geometry changes the immediate geometric information for the newly studied class and yields a sharp class-wide strong-starlikeness theorem; the exact area and height supply additional invariant checks. This is a substantive correction/refinement rather than a cosmetic rewrite.

## Limitations

- The novelty claim is source-specific; the sine/arcsine conformal identities and Catalan constant are classical.
- This audit does not revalidate the motivating papers' coefficient or Hankel-determinant estimates.
- Both motivating preprints are recent, so unindexed contemporaneous overlap remains a residual priority risk.

## Publication guard

This audit is scoped to the exact source-tree SHA above. The guarded change-set adds this independent-audit evidence pair and updates only the independent-audit channel in `VERIFICATION.md`; Lean and expert-attestation channels are preserved unchanged.
