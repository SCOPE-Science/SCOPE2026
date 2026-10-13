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

The proof has two independent components.

First, Lemma 3.3 of arXiv:2609.39370 gives the normal form of a strict element: a matching edge \(e_i\) is collapsed to an independent image vertex \(v_i\). For an idempotent, every image vertex must be in the domain and fixed. Because domain edges are disjoint and image vertices are distinct, this is equivalent to \(v_i\in e_i\) for every \(i\). Conversely, that endpoint condition visibly fixes every image point.

Second, on \(P_n\) this becomes a tiling by monomers and oriented dominoes. The selected endpoints fail independence in exactly one local configuration: an \(R\)-domino immediately followed by an \(L\)-domino. The weighted transfer recurrence is therefore
\[
I_n(y)=I_{n-1}(y)+2yI_{n-2}(y)-y^2I_{n-4}(y),
\]
with
\[
I_0(y)=1,\quad I_1(y)=1,\quad I_2(y)=1+2y,\quad I_3(y)=1+4y.
\]
This yields
\[
\sum_{n\ge0}I_n(y)x^n=\frac{1}{1-x-2yx^2+y^2x^4}.
\]
Expanding the right-hand side geometrically and extracting \(x^ny^k\) gives the stated factorial sum exactly.

The bundled `check_idempotents.py` does not assume the tiling model when checking small paths. It enumerates all partial maps on \(P_n\) for \(1\le n\le6\), tests vertex-fiber strictness and edge-preimage continuity from the definitions, and then tests idempotency. It independently obtains totals
\[
1,3,5,10,19,36.
\]
It separately checks the closed rank formula and recurrence through \(n=14\) and ends with `CHECK_OK`.

The finite checks do not prove the infinite formulas; the symbolic argument above does. No closed enumeration for cycles or arbitrary graphs is asserted.
