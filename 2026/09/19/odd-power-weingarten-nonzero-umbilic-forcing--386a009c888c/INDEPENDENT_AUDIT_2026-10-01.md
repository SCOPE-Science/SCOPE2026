---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For every odd integer \(p\ge3\), any compact \(C^3\) immersed surface satisfying the unordered monomial Weingarten relation \((\kappa_1-c\kappa_2^p)(\kappa_2-c\kappa_1^p)=0\) has \(c>0\), nonnegative Gaussian curvature, and at least one nonzero umbilic of curvature \(c^{-1/(p-1)}\) in every connected component of its positive-curvature set.

## Correctness — PASS

After scaling to \(c=1\), the positive-curvature spectrum is \(\{t,t^p\}\). The farthest-point Hessian argument gives \(c>0\), and oddness makes \(K\ge0\). Recomputing Codazzi gives \(\omega(e_1)=e_2(t)/(t(1-t^{p-1}))\) and \(\omega(e_2)=p t^{p-2}e_1(t)/(1-t^{p-1})\). Cheng's full cubic proof was inspected, including the distributional Gauss identity and Proposition 4.3. Replacing \(3t\) by \(p t^{p-2}\) changes the cutoff bound by the factor \(\delta^{p-3}\): the \(t>1\) branch contradicts Stokes and the \(0<t<1\) branch forces the cutoff curvature integral both to zero and to \(\int_UK>0\). The rescaling then gives the displayed umbilic curvature.

**Checked sources.** assigned RESULT.md at the frozen tree; Cheng, arXiv:2609.19188v1, full PDF Proposition 4.3 and surrounding lemmas; Kühnel--Steller 2005

**Residual risks.** The global connection-form argument assumes the source regularity needed for a continuous principal connection and the weak Gauss equation; these hypotheses are satisfied at \(C^3\).

## Originality — PASS

Cheng proves exactly the cubic endpoint \(p=3\). Searches for higher odd monomial Weingarten relations, generalized Hopf surfaces, and classical umbilic theorems found constructions and stronger-rigidity results under different hypotheses, but no arbitrary-immersion componentwise forcing theorem for every odd \(p\ge5\).

### Equivalent formulations

The relevant equivalent formulation is a componentwise nonzero-umbilic theorem for the unordered monomial curvature relation; no such higher-odd statement was located.

### Broader coverage

Those theorems do not dominate the audited componentwise statement under the same \(C^3\) hypotheses.

### Exact database or table

The database/table check is inapplicable because the claim is analytic and quantified over arbitrary compact immersions.

### Claim versus prior implication

The higher-power conclusion is not a formal special case of the cubic theorem; it needs the recomputed structure equations and cutoff estimate.

**Source inspections.**
- Umbilic slopes and cubic Weingarten surfaces: Full 25-page PDF, especially Section 4, Lemma 4.2 and Proposition 4.3 on pages 11--12. Assessment: Proves the \(p=3\) endpoint only; its formulas expose the generalization mechanism but do not state it.
- On closed Weingarten surfaces: Abstract and bibliographic theorem context. Assessment: Supplies higher-power examples, not the componentwise forcing theorem for arbitrary \(C^3\) immersions.

**Checked sources.** https://arxiv.org/abs/2609.19188; https://doi.org/10.1007/s00605-005-0313-4; https://doi.org/10.2307/2372698; published-results semantic search

**Residual risks.** The 1959 Voss paper was not inspected in full. Very recent parallel work around the Cheng preprint may not yet be indexed.

## Value — PASS

The theorem extends a key global geometric mechanism from the cubic case to every higher odd monomial at no extra regularity, and identifies \(p=3\) as the sharp scale-invariant cutoff endpoint. Because higher odd-power closed examples are known, the result constrains a nonvacuous natural class rather than an artificial slice.

**Checked sources.** Cheng 2026 cubic classification; Kühnel--Steller 2005 higher-power examples

**Residual risks.** It does not classify the \(p\ge5\) surfaces or give a universal numerical count beyond one umbilic per positive-curvature component.

## Limitations

- This is an umbilic-existence theorem, not a global classification for \(p\ge5\).
- Even exponents are not covered, and the proof retains \(C^3\) regularity.
- Historical coverage under older analytic Weingarten terminology remains a residual risk.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
