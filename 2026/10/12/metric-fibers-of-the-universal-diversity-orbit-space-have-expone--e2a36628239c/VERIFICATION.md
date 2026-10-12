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

The bundled `verify.py` uses only Python's standard library and exact rational arithmetic.

For each \(2\le n\le8\), it constructs the explicit interior point
\[
\delta_0(A)=0\quad(|A|\le1),\qquad
\delta_0(A)=1+\frac{|A|}{4n}\quad(|A|\ge2),
\]
enumerates every nontrivial monotonicity and overlapping-subadditivity inequality, and checks strictly positive slack. From each inequality's exact coefficient \(\ell_1\)-norm it computes a positive rational radius for a full \(\ell_\infty\) coordinate box around \(\delta_0\). This is a finite certificate that all \(2^n-n-1\) diversity coordinates vary independently near \(\delta_0\). The script then checks that fixing all \(\binom n2\) pair coordinates leaves exactly \(2^n-n-1-\binom n2\) higher-set coordinates.

As an independent low-arity test, the script enumerates all integer metric triples with edge lengths from 1 through 6 and all tested half-integer values of the triple coordinate. It evaluates the original diversity axiom directly, not the monotonicity/subadditivity reformulation, and checks equivalence with
\[
\max(d_{12},d_{13},d_{23})\le t\le
\min(d_{12}+d_{13},d_{12}+d_{23},d_{13}+d_{23}).
\]

It also checks the full-diversity hidden-dimension sequence and its contrast with the \(L_1\) cut-coordinate count through \(n=12\). Running

```text
python verify.py
```

returns

```text
full_hidden_n2_to_n10 [(2, 0), (3, 1), (4, 5), (5, 16), (6, 42), (7, 99), (8, 219), (9, 466), (10, 968)]
VERIFY_OK 171758 exact assertions
```
