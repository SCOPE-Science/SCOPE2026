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

The proof depends on two exact published statements.

Ore's squarefree characterization, as quoted in the inspected arithmetic-number
source, gives
\[
n\text{ squarefree and non-arithmetic}
\iff
n=2m,\quad
p\mid m\Rightarrow p\equiv1\pmod4.
\]

Prabhu's Theorem 1.3 gives, for fixed \(k\ge2\), modulus \(4\), and the
all-\(1\) residue tuple,
\[
\#\{m\le X:\mu^2(m)=1,\ \omega(m)=k,\ p\mid m\Rightarrow p\equiv1\pmod4\}
\sim
\frac1{2^k}
\frac{X(\log\log X)^{k-1}}{(k-1)!\log X}.
\]
The \(k=1\) endpoint is the prime number theorem in arithmetic progressions.

Substitution \(k=r-1\) and \(X=x/2\) gives the claimed exceptional main term.
Landau's squarefree \(r\)-prime theorem gives the denominator for the relative
proportion.

The packaged checker independently enumerates finite squarefree integers,
computes divisor means from their prime factorizations, verifies the exact
squarefree criterion, and reports finite ratios to the predicted main terms.
Those computations are corroborative and are not used as an infinite proof.
