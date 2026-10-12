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

The verification separates the source-backed modal step from the finite combinatorics.

1. **Modal-to-set-system reduction.** Goldblatt--Hodkinson's frame characterization says that failure of \(U_n\) yields a world \(x\) with \(n+1\) successors \(y_i\) whose future sets are pairwise inclusion-incomparable. Transitivity gives \(R(y_i)\subseteq R(x)\); achronality rules out \(y_iRy_j\), hence each \(R(y_i)\) is contained in \(Z=R(x)\setminus\{y_0,\ldots,y_n\}\).

2. **Exact lower bound.** The \(n+1\) sets \(R(y_i)\) form an antichain in \(\mathcal P(Z)\). Sperner's theorem gives
   \[
   n+1\le\binom{|Z|}{\lfloor |Z|/2\rfloor},
   \]
   hence \(|Z|\ge q_n\) and the frame has at least \(n+2+q_n\) worlds.

3. **Exact construction.** Choosing \(n+1\) distinct central-layer subsets of a \(q_n\)-element set and making them the future sets of \(n+1\) successors of one root gives an irreflexive transitive rooted frame with exactly \(n+2+q_n\) worlds that fails \(U_n\).

4. **Computational replay.** The bundled script constructs this frame for every \(1\le n\le500\), checks its relation and achronality exactly, verifies the threshold dimension, and separately verifies both central-binomial threshold inequalities for every \(1\le n\le10000\). It reports:

`VERIFY_OK 20520 exact assertions`

The replay also returns the first twenty exact minima:

`[5, 7, 9, 10, 11, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29]`

No independent audit has been performed.
