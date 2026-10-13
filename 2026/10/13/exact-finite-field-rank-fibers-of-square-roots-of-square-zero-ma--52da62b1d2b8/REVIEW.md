# Scientific review

**Correctness (PASS).** For a fixed nilpotent target with \(N^2=0\), every root satisfies \(X^4=0\). Squaring Jordan blocks of size at most four forces the two integer constraints \(2a+b=r\) and \(b+2c+d=m\). Nilpotent similarity classes and centralizer orders are valid over every finite field, including characteristic two. Uniformity of the square map on each conjugacy class gives the exact centralizer ratio for each root type. All possible ranks and the empty-fiber boundary follow from integer constraints, not just experiments. The independently implemented direct matrix enumerations test all target ranks in the cases specified in VERIFICATION.md.

**Originality (PASS, with residual risk).** Borwein–Richmond and Öztürk already establish square-root feasibility and Jordan partition behavior, and classic centralizer formulas count nilpotent conjugacy classes. These ingredients are explicitly credited. The final claim instead provides exact individual square-root *fiber multiplicities indexed by the root rank* for all finite fields, dimensions, and square-zero target ranks. Inspected primary full texts do not give the same rank-refined finite-field fiber formula. This is a targeted literature finding, not a proof of absolute historical priority; an equivalent enumeration may exist.

**Value (PASS).** The square map is a canonical polynomial map on a finite matrix algebra, and its nonuniform fibers at a fixed nilpotent target are natural arithmetic invariants. The formula is not merely a feasibility test: it determines every fiber cardinality by root rank and a sharp gap-free rank support for infinitely many dimensions and finite fields. The fixed-target enumeration distinguishes the number of *actual roots* from the known number of possible Jordan types. The proof exposes why the contributions are integers and how nilpotent conjugacy-class sizes combine.

**Independent validation:** None. Exhaustive small cases and symbolic calculations support, but do not replace, the universal group-action argument. Some historical literature may use equivalent notation.

Self-review: passed. Independent audit: not yet performed.
