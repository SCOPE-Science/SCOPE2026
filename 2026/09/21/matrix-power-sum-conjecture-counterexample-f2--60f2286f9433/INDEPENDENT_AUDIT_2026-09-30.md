# Independent audit — 2026-09-30

**Record:** `2026/09/21/matrix-power-sum-conjecture-counterexample-f2--60f2286f9433`  
**Audited source tree:** `e9f6b14709f13a65caec57f3404537bcf34d600b`  
**Disposition:** passed

## Correctness — PASS

PASS. Centrality of t makes the coefficient of t^a in sum_{A,B}(tA+B)^N exactly the multidegree word sum T_{a,N-a}. I independently reimplemented the exhaustive dynamic-programming recurrence over all 256 ordered pairs of 2x2 matrices over F_2 and separately aggregated (tA+B)^23 by polynomial-matrix exponentiation. The first nonzero positive bidegrees occur at total degree 23; the a-support is exactly {5,6,7,9,10,11,12,13,14,16,17,18}; every corresponding value is I_2, including T_{5,18}; and the aggregate polynomial is exactly t^5(t+1)^5(t^2+t+1)(t^3+t+1)(t^3+t^2+1) I_2. The original paper's Conjecture 3, inspected in the accessible author/arXiv version, asserts vanishing for p=d=2, r>1 and every multidegree, so this is a direct counterexample. The record correctly limits minimality to r=2 and does not claim to refute Conjectures 1 or 2.

## Originality — PASS

PASS. The full accessible Fortuny--Grau--Oller-Marcén--Rúa manuscript was inspected and states Conjecture 3 in the form contradicted here. Targeted searches for corrections, counterexamples, the multidegree (5,18), and degree-23 matrix word sums did not locate a prior published counterexample or the same polynomial identity. Later adjacent matrix-power literature found in search does not advertise this failure. Because negative search cannot prove priority, a poorly indexed antecedent remains possible, but the direct comparison to the conjecture source strongly supports originality.

## Scientific value — PASS

PASS. A small exact counterexample to an explicit published conjecture has clear scientific value, especially because the conjecture was used as a conditional ingredient in the source paper's broader program. The exact first-failure degree and full degree-23 support make the result diagnostically useful rather than merely exhibiting one opaque computational exception. The finite verification is transparent and independently reproducible.

## Independent checks

- Reimplemented matrix multiplication and the shuffle recurrence over all 16^2 ordered matrix pairs.
- Independently computed the polynomial matrix sum by binary exponentiation over F_2[t].
- Compared the resulting coefficient support and factorization with the filed artifact.
- Inspected the accessible original paper/preprint for the exact scope of Conjecture 3 and the distinction from Conjectures 1 and 2.

## Literature evidence

- https://arxiv.org/abs/1505.08132 — Fortuny, Grau, Oller-Marcén and Rúa, accessible original preprint containing Conjecture 3.
- https://doi.org/10.1142/S0218196717500278 — Published version of the matrix power-sum paper whose Conjecture 3 is refuted.
- https://www.unioviedo.es/grau/ARTICULOS%20PUBLICADOS/articulo54.pdf — Author-hosted full-text copy used as an additional lawful accessible source.

## Limitations

- The result refutes Conjecture 3 only, not Conjecture 1 or Conjecture 2 of the source paper.
- The degree-23 minimality statement is only for r=2 with two noncommuting letters.
- The counterexample and minimality are established by exact finite enumeration rather than a closed-form classification of all multidegrees.

No GitHub write was performed by the audit chat. The guarded publication plan stages only this audit evidence and the independent-audit verification channel.
