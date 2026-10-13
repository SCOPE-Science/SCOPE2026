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

The verifier checks the Birkhoff-dual equality classification independently of the product proof. It enumerates every labelled partial order on at most five points by assigning each unordered pair one of the three states “incomparable”, “forward”, or “backward” and filtering by transitivity.

For every resulting poset \(P\), it enumerates every upset. An upset is complemented in \(\operatorname{Up}(P)\) exactly when its set complement is also an upset, so the script computes
\[
\frac{|\mathrm{EM}(\operatorname{Up}(P))|}{|\operatorname{Up}(P)|}
\]
as an exact rational number. It then checks that this ratio is \(2/3\) exactly when the comparability graph of \(P\) has one component of size two and all other components are singletons.

The exhaustive labelled-poset totals for sizes \(1,2,3,4,5\) are
\[
1,3,19,219,4231,
\]
and the corresponding equality-case counts are
\[
0,2,6,12,20.
\]
For \(n\ge2\), the latter equal \(n(n-1)\), exactly the number of ways to choose and orient the unique two-element chain component.

Replay:

```text
python3 verify_excluded_middle_equality.py
```

Expected final line:

```text
VERIFY_OK 8956 exact assertions
```

The script also checks for each poset that the number of complemented upsets is \(2^c\), where \(c\) is the number of comparability components. Independent audit has not been performed.
