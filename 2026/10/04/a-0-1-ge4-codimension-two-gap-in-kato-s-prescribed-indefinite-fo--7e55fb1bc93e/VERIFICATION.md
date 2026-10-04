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

The proof is symbolic; no finite experiment is used as evidence for the infinite statement.

The primary full text was checked at the four local cases in the proof of Theorem 1.1. In the \(z_i=1\), even case the indefinite-fold image has no normal crossing. In the \(z_i=1\), odd case the construction invokes Lemma 2.1 once, whose middle singular fiber is the type-\(\mathrm{II}^2\) chain shown by comparing Figures 1 and 2. In the \(z_i\ne1\), even case the source explicitly states four type-\(\mathrm{II}^2\) fibers; in the odd case it explicitly states five.

The gluing paragraph was checked separately. The \(W_i\)-maps are joined along boundary Morse functions, then attached to a product-induced map and a natural projection. These pieces do not add a new two-indefinite-point singular fiber. Hence the total is the sum of the local contributions:
\[
0,\ 1,\ 4,\ 5.
\]

Writing
\[
r(b)=\left|\{i:z_i\ne1\}\right|,
\qquad
o(b)=\left|\{i:m_i\text{ odd}\}\right|
\]
gives
\[
\left|\mathrm{II}^2(f_b)\right|=4r(b)+o(b).
\]

The \(0/1/\ge4\) gap follows because a cost at most \(3\) forces \(r(b)=0\); the compressed-word condition then forces a single syllable. The parity check uses
\[
(-1)^{o(b)}=\operatorname{sgn}(\pi_b)=(-1)^{n-c(\widehat b)}.
\]

The verification does not establish any minimality statement over all stable maps, and no such statement is claimed.
