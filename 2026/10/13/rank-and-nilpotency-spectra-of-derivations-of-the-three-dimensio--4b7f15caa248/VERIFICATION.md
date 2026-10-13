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

The standalone `verify.py` reconstructs the claimed derivation matrices and checks the formulas independently of the symbolic simplifications in the proof.

For each of \(q=2,3,5,7\), it enumerates all \(q^6\) parameter choices
\[
(a,b,c,d,u,v)
\]
and computes the rank and nilpotency index of
\[
\begin{pmatrix}
a&c&0\\
b&d&0\\
u&v&a+d
\end{pmatrix}.
\]
The observed rank and nilpotency-index histograms agree with the closed formulas.

For \(q=2\) and \(q=3\), the verifier additionally enumerates every one of the \(q^9\) linear maps on the underlying three-dimensional vector space, tests the derivation identity on all basis pairs, and confirms that exactly \(q^6\) maps are derivations with the same rank histogram. This independently checks that no derivations are missing from the six-parameter normal form.

The non-prime field \(\mathbb F_4\) is implemented directly as \(\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\). Exhaustive enumeration of all \(4^6\) derivations gives rank counts
\[
1,75,1908,2112
\]
and nilpotency-index counts
\[
1,75,180,
\]
exactly as predicted.

Representative replay output ends with:

```text
prime parameter 2 {0: 1, 1: 9, 2: 46, 3: 8} {1: 1, 2: 9, 3: 6}
prime parameter 3 {0: 1, 1: 32, 2: 426, 3: 270} {1: 1, 2: 32, 3: 48}
prime parameter 5 {0: 1, 1: 144, 2: 5980, 3: 9500} {1: 1, 2: 144, 3: 480}
prime parameter 7 {0: 1, 1: 384, 2: 32886, 3: 84378} {1: 1, 2: 384, 3: 2016}
all linear maps 2 derivations 64 ranks {0: 1, 1: 9, 2: 46, 3: 8}
all linear maps 3 derivations 729 ranks {0: 1, 1: 32, 2: 426, 3: 270}
GF4 parameter {0: 1, 1: 75, 2: 1908, 3: 2112} {1: 1, 2: 75, 3: 180}
VERIFY_OK
```

The finite checks do not prove the arbitrary-prime-power theorem; the proof in `RESULT.md` supplies that general argument.
