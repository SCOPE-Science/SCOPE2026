# Independent Audit — Exact tenth-power stable obstruction set via a numerical semigroup

Audit date: 2026-09-29 (UTC)
Record path: `2026/09/17/exact-tenth-power-obstruction-semigroup--a3858d8ef09c`
Audited tree: `41be28cfca1d0a19dcaf05040f5e3e735b15742a`

## Disposition

**PASSED** — All three audit axes pass, subject to the explicit qualifications below.

## Correctness

**PASS**. The numerical-semigroup proof checks exactly. Stable offsets are the positive gaps of Gamma_10=<m^10-1:m>=2>. Fermat modulo 11 and the Frobenius number of T=<93,5368> reduce every generator to Gamma_10=<1023,59048,C> with C=11^10-1. Because C belongs to T and C=-1 mod 11, the unique decomposition N=rC+11z (0<=r<=10) satisfies N in Gamma_10 iff z in T. Sylvester’s formulas then give F(T)=493763 and g(T)=246882, hence F(Gamma_10)=259379677393 and g(Gamma_10)=129689838697; independent exact arithmetic reproduced these values and 2g-1=F. The residue-wise complement map correctly transports symmetry, including the negative-z and z>F(T) boundary cases.

## Originality

**PASS**. Benfield–Lippard determine the stable obstruction sets only through exponent 9 and for k=10 state a lower bound |B^10|>=129687123005 together with the relevant even-exponent symmetry conjectures. The exact three-generator collapse and exact invariants were not located in targeted searches. The previously inaccessible Zenkin 1995 paper was obtained through authorized Oxford access for this audit; it develops the generalized Waring invariant-set framework but contains no exponent-10 semigroup reduction or these constants. This removes the record’s principal stated literature uncertainty.

## Scientific value

**PASS**. The theorem replaces a published lower bound near 1.3e11 with an exact description of the entire stable obstruction set, exact Frobenius number and genus, and verifies the exponent-10 symmetry cases by a conceptual three-generator reduction. That is a substantive exact advance rather than a large brute-force enumeration.

## Literature evidence

- https://arxiv.org/abs/2404.08193 — Brennan Benfield and Oliver Lippard, Integers that are not the sum of positive powers. The paper treats k<=9 exactly and records only a lower bound for |B^10| plus conjectures at exponent 10.
- https://doi.org/10.1007/BF02304770 — A. A. Zenkin, The Generalized Waring Problem: A New Property of Positive Integers (1995). Full five-page text obtained via authorized Oxford access; no exponent-10 exact semigroup result appears.

## Independent checks

- Recomputed F(<93,5368>)=493763 and genus 246882 and verified C=25937424600=93*278893056+5368*69.
- Recomputed a_10=259379677393, b_10=129689838697, b_10-129687123005=2715692, and a_10=2b_10-1.
- Inspected the full Zenkin 1995 paper through authorized institutional access rather than inferring its contents from metadata.

## Limitations

- The result does not determine the stabilization index g(1,10) and does not resolve the even-exponent conjectures beyond k=10.
- Zenkin 1995 was read through authorized Oxford access and is no longer an unresolved literature gap for this audit.

GitHub was used only as read-only evidence. The repository tree matched the assigned tree exactly.
