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

The universal proof was checked symbolically at the level of its two critical spectral constructions.

For \(k<N\), the full sequence Gram matrix is \(B^{\otimes k}\) with \(B=(1-s)I+sJ\). The injective Gram matrix is a principal submatrix, so its smallest eigenvalue is at least \((1-s)^k\). A nonzero alternating tensor on any \(k+1\) labels is supported only on injective tuples and lies in \((\mathbf1^\perp)^{\otimes k}\), giving an exact eigenvector with eigenvalue \((1-s)^k\).

For \(k=N\), the Gram matrix expands as a positive linear combination of restriction-equivalence matrices \(A_T\). All terms with \(|T|=N-1\) or \(|T|=N\) equal the identity, giving the claimed lower bound. The permutation sign vector is killed by every \(A_T\) with \(|T|\le N-2\), because the remaining completions pair by a transposition, and therefore attains that bound.

The packaged script `artifacts/verify.py` uses exact rational arithmetic at \(s=2/5\). It directly checks the alternating-tensor eigenvector equation for every \(3\le N\le6\), \(2\le k<N\), and the sign-vector eigenvector equation for every \(3\le N\le6\). These computations are finite corroboration only; the proof above supplies the all-parameter argument.

The result does not verify or claim the minimum-error part of the motivating conjecture.
