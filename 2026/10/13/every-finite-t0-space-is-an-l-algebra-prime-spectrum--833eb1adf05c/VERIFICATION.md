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

The standalone `verify.py` exhausts every labeled poset on \(n\le5\) points. For each poset it adjoins one new greatest element and independently checks:

1. the three defining \(L\)-algebra identities for every tuple of elements;
2. that the candidate ideals are the nonempty upper sets;
3. prime ideals by the lattice condition \(I\cap J\subseteq P\Rightarrow I\subseteq P\) or \(J\subseteq P\);
4. equality of the computed prime set with \(\{\Omega\setminus\downarrow t:t\in T\}\);
5. the identity \(\phi^{-1}(U_I)=I\cap T\) for every ideal \(I\); and
6. equality of the pulled-back spectrum topology with the complete upper-set topology of the original poset.

As an independent census check, the enumerator reproduces the labeled-poset counts
\[
1,1,3,19,219,4231
\]
through five points. Its recorded output is

```text
n=0 labeled_posets=1
n=1 labeled_posets=1
n=2 labeled_posets=3
n=3 labeled_posets=19
n=4 labeled_posets=219
n=5 labeled_posets=4231
VERIFY_OK 1115466 exact assertions; 4474 labeled posets checked
```

The finite computation is a replay certificate, not the general proof. Independent audit has not been performed.
