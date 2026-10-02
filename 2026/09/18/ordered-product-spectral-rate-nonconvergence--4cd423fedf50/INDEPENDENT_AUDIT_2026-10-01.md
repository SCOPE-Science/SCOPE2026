---
audit_date: 2026-10-01
status: passed
---

# Scientific audit

## Final claim

A smooth deterministic period-four Jacobian cocycle with a simple top Lyapunov exponent can have ordered-product spectral rate \(h_{2k}=a\) and \(h_{2k+1}=(a+b)/2\), so a Lyapunov gap alone does not force the spectral-radius diagnostic in arXiv:2609.18017v1 to converge. For periodic cocycles, a nonzero endpoint pairing supplies a sufficient residue-class convergence condition, and the example also shows finite-horizon spectral radius is moving-frame dependent.

## Correctness — PASS

For the polynomial map in the package, the period-four orbit has block Jacobian with fiber steps \(J_n=Q^{n+1}DQ^{-n}\). Multiplication telescopes exactly to \(P_n^{(L)}=Q^{n+L}D^LQ^{-n}\). Singular values are therefore \(e^{aL}\) and \(e^{bL}\), giving simple top exponent \(a\). For even \(L\), \(Q^L=\pm I\) and the spectral rate is \(a\); for odd \(L\), \(Q^LD^L\) has eigenvalue modulus \(e^{(a+b)L/2}\). The periodic residue-class formula \(P_n^{(kp+r)}=A_{n,r}M_n^k\) gives the stated nonzero left-right endpoint pairing criterion by the dominant rank-one term. Under a moving orthogonal frame, endpoint frames act on opposite sides rather than by similarity, so spectral radius need not be invariant. The inspected numerical artifact reproduces the exact parity identities for \(a=2,b=1\).

**Checked sources.** Assigned RESULT.md and verification artifact at source tree 8c8b9c00b51ced1da9f8c3a57eeddd19523f0c50; Sornette, Saiprasad and Troude, arXiv:2609.18017v1; Aoun and Sert, arXiv:1908.07469; N. Martínez Ramos, arXiv:2507.19624 / IMRN 2026

**Residual risks.** The exact general-source wording was checked through the source abstract and the frozen cited formula/claim in the assigned package; a later source revision could amend the convergence statement.

## Originality — PASS

General nonconvergence of normalized spectral radius is known, so that broad phenomenon is explicitly excluded from the originality claim. Searches found no earlier source-specific smooth deterministic period-four counterexample with the exact parity law, endpoint-transversality diagnosis, and moving-frame interpretation directed at the 2026 ordered-product diagnostic.

### Equivalent formulations

Those prior results show the broad issue, but they do not state the same smooth deterministic tangent-map example or the exact endpoint-pairing criterion.

### Broader coverage

No general theorem found mechanically yields this explicit smooth period-four source-specific correction; conversely the broad counterexamples do not supply the exact parity construction.

### Exact database or table

No standard numerical table is relevant; the exact-corpus comparison establishes that the nearby explicit constructions found are later.

### Claim versus prior implication

The prior results motivate the correction but do not subsume its exact construction and source-specific mechanism.

**Checked sources.** https://arxiv.org/abs/2609.18017; https://arxiv.org/abs/1908.07469; https://arxiv.org/abs/2507.19624; published-result searches dated through 2026-10-01

**Residual risks.** The source preprint is very recent and may revise its theoretical statement. Broad spectral-radius nonconvergence is prior mathematics and is not part of the novelty claim.

## Scientific value — PASS

The result supplies a concrete smooth counterexample to a currently used asymptotic interpretation, separates spectral-radius growth from Oseledets singular-direction growth, and identifies an exact endpoint-pairing mechanism that explains when periodic residue classes recover the Lyapunov exponent. That is a motivated correction with reusable structural content.

**Residual risks.** The correction does not invalidate the source's empirical observations on its specific Hénon and Ikeda data.

## Limitations

- The result corrects a general asymptotic interpretation of the source diagnostic, not the source's reported finite-horizon numerical values.
- The endpoint transversality condition is sufficient for periodic cocycles; it is not claimed to characterize arbitrary aperiodic cocycles.

## Disposition

PASSED. Acceptance requires all three scientific axes to pass.
