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

The analytic verification has four steps.

1. For \(K=[a,b]\), differentiate or directly compare cross ratios to verify that
\[
\psi_K(x)=\frac12\log\!\left(\frac{x-a}{b-x}\right)
\]
is strictly increasing and satisfies \(d_K^H(x,y)=|\psi_K(x)-\psi_K(y)|\).

2. For a convexified \(\alpha\)-separated sequence in \(G=[c,d]\), the previous convex hull is an interval. Its image under \(\psi_K\) is the interval between the previous extreme coordinates. Each new point therefore increases the occupied coordinate span by at least \(\alpha\). This proves
\[
N-1\le \frac{D_H(G,K)}{\alpha}.
\]
Equally spaced monotone coordinates give equality at the integer floor.

3. Substituting \(K^\circ=[1/a,1/b]\) and \(G^\circ=[1/c,1/d]\) into the interval Hilbert cross ratio and clearing \(abcd\) gives exactly the same diameter quotient. Hence all four packing numbers in the finding have the same exact value.

4. Arya–Mount Lemma 4.3 gives
\[
\widehat M_{\mathrm{diag},H}(\eta)
\le M_H(\eta/4)\widehat M_H(\eta/2).
\]
In one dimension \(M_H=\widehat M_H\), and monotonicity yields the claimed square at \(\eta/4\).

The included `verify.py` replays exact rational cross-ratio cancellations on fixed examples and numerical checks of the coordinate isometry. It is a finite sanity check only. No exhaustive search, timeout, or numerical log is used to justify the universal theorem.
