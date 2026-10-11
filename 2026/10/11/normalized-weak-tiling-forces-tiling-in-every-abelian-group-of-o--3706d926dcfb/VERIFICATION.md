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

Run `python3 verify_order16.py` in the same directory. The entire proof checker is included in this package, uses the Python standard library only, and does not import any saved computation or external data. Its final lines read:

```
VERIFIED: every normalized weak tile in every abelian group of order 16 tiles.
NORMALIZED_SUBSETS_CHECKED= 163840
```

The enumeration loops over every one of the \(2^{15}\) origin-containing nonempty subsets of each group, without a heuristic stopping threshold. For each, it constructs the exact group table and the difference support \(A-A\), checks all legal translate blocks, enumerates possible exact tiling partners, and performs fraction-free integer Gaussian elimination on every remaining incidence system. There are no floating-point constants, tolerances, random searches, or external scientific code dependencies in the certificate.

For a concrete nontrivial obstruction in \(\mathbb Z_{16}\), take
\[
A=\{0,1,2,9\},\quad
T_A=\{3,4,5,6,10,11,12,13\}.
\]
The complement of \(A\), in increasing order, is
\[
X=(3,4,5,6,7,8,10,11,12,13,14,15).
\]
Assign integer weights
\[
w=(0,1,-1,-1,2,-1,2,-2,0,1,0,0).
\]
Then \(\sum_{x\in X}w(x)=1\) but \(\sum_{a\in A}w(a+t)=0\) for every allowed \(t\in T_A\), contradicting a weak tiling, even one with signed weights supported on the legal shifts.

An additional exact symbolic-rank cross-check compared the same integer elimination method to rational ranks on \(800\) deterministic random rectangular matrices. This independent software check does not replace the self-contained exhaustive group verifier.

The claim does not address other group orders, uniqueness of weak tiling weights, or a general structural theorem without finite enumeration.
