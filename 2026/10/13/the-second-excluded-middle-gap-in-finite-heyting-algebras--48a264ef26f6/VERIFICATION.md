---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The verifier checks the second-gap theorem through finite Birkhoff duality, independently of the factor-decomposition proof. It enumerates every labelled partial order on at most five points by assigning each unordered pair one of the three states “incomparable”, “forward”, or “backward” and filtering by transitivity.

For every poset \(P\), the script enumerates every upset and every complemented upset, so it computes
\[
\frac{|\mathrm{EM}(\operatorname{Up}(P))|}{|\operatorname{Up}(P)|}
\]
as an exact rational number. It checks that complemented upsets are exactly the \(2^c\) unions of comparability components, where \(c\) is the number of components. It then verifies:

1. ratio \(2/3\) occurs exactly for one two-element chain plus isolated points;
2. after removing that family, every non-Boolean ratio is at most \(1/2\);
3. ratio \(1/2\) occurs exactly for one three-element chain plus isolated points.

The exhaustive labelled-poset totals for sizes \(1,2,3,4,5\) are
\[
1,3,19,219,4231,
\]
and the corresponding \(1/2\) equality-case counts are
\[
0,0,6,24,60.
\]
For \(n\ge3\), the latter are \(n(n-1)(n-2)\), exactly the number of ways to choose three vertices and linearly order them as the unique nontrivial component.

Replay:

```text
python3 verify_second_excluded_middle_gap.py
```

Expected final line:

```text
VERIFY_OK 17907 exact assertions
```

Independent audit has not been performed.
