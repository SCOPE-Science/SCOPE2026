# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

**Disposition:** PASSED

## Correctness — PASS

The proof reconstructs the DNP estimate from the exact FLM intersection machinery. FLM Lemma 7.15 gives \(c(\mathrm{Dist},\mathrm{NoPlus})^2\le t(t-1)/(N-t+1)\), and the proof of their Theorem 7.7 supplies the factor-4 union-bound losses. Independently, \(I-\Pi_{\mathrm{NoPlus}}\preceq\sum_j |+\rangle\langle+|_j\) gives the \(t\mu_+\) term. For a local exact 2-design the two-copy equality projector twirls to \((2/(d+1))\Pi_{\mathrm{sym}}\); independence over \(n\) sites gives \((2/(d+1))^n\), and a pair union bound gives the displayed collision estimate. A tensor product of local 1-designs is a global 1-design. These steps establish the stated bound for \(2\le t\le N/2\).

## Originality — PASS

The final contribution is the lifting principle 'ordinary distinctness plus one-copy plus-state flatness implies DNP concentration' and its product-local-design/local-Clifford corollary. The motivating paper explicitly leaves the local-Clifford DNP question open, while FLM proves DNP concentration for global unitary 2-designs. No published SCOPE/resultary hit or primary source inspected states the product-local corollary or general lifting inequality.

The structured originality comparison, source inspections, checked sources, and residual risks are recorded in `INDEPENDENT_AUDIT_2026-10-01.json`.

## Scientific value — PASS

This resolves an explicit open question for a natural depth-one quantum ensemble and extracts a reusable sufficient condition that applies beyond global 2-designs. It is a motivated structural lemma with a concrete cryptographic application, not an arbitrary parameter slice.

## Limitations

- The result is for parallel forward-query states and does not by itself prove PRU security after removing the binary phase layer.
- The exact constants are not claimed optimal.
- The motivating papers are recent, so near-simultaneous priority remains a residual risk.
