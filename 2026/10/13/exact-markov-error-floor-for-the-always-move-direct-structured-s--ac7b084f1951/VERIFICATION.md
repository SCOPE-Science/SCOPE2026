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

The source formula was specialized symbolically to \(f(w)=w^2/2\). The directional score reduces to \(w\xi+h/2\), so the common \(h/2\) term cannot affect candidate ranking. This proves the transition law directly for every \(h>0\).

The included `verify_markov.py` uses exact rational arithmetic to check, for multiple integer candidate counts \(q\ge2\), the detailed-balance equations, normalization of the proposed invariant distribution, and the identity
\[
\sum_{{n\in\mathbb Z}} n^2\pi_n=\frac1{{2(1-2^{1-q})^2}}.
\]
It also exhaustively enumerates short \(q=1\) Rademacher walks and verifies \(\mathbb E[N_t^2]=t\). Replaying the embedded file should print `VERIFY_OK`.

The exact script does not certify the infinite-horizon results. Pathwise nonconvergence is proved from the fixed increment magnitude, the \(q=1\) limsup uses the classical unboundedness of simple symmetric random walk, and the \(q\ge2\) time-average statement uses the countable-state positive-recurrent Markov-chain ergodic theorem. Because the chain has period two, no pointwise convergence to the invariant distribution is claimed from the stated start.
