# Independent audit — 2026-10-01

## Final claim

For every \(0<c\le1/8\), the two quartic-profile maps \(M_c^-\) and \(M_c^+\) are smooth symmetric homogeneous strictly monotone means lying respectively below and above the arithmetic mean off the diagonal, while each is neither convex nor concave; hence both implications in Raïssouli--Sándor Problem 4(ii) are false.

## Correctness — PASS

For \(0<c\le1/8\), the profile \(q_c(t)=ct^2(2-t^2)\) is positive off the diagonal and satisfies \(q_c(t)<|t|\), placing \(M_c^-\) and \(M_c^+\) strictly between the inputs. The coordinate derivative formula together with \(|q_c'|\le1/(3\sqrt3)\) yields a uniform positive lower bound, so both maps are strictly monotone. Independent symbolic differentiation gives \(\phi_+''(x)=-16c(x^2-4x+1)/(x+1)^5\) and \(\phi_-''(x)=16c(x^2-4x+1)/(x+1)^5\); the numerator changes sign at \(2+\sqrt3\), so each mean is neither convex nor concave. The construction therefore answers both directions of the source problem negatively.

Checked sources:
- M. Raïssouli and J. Sándor, Sub-super-stabilizability of certain bivariate means via mean-convexity, J. Inequalities Appl. 2016:273, complete open full text inspected.
- M. Raïssouli and A. Rezgui, Characterization of homogeneous symmetric monotone bivariate means, J. Inequalities Appl. 2016:217, related characterization source.
- Resultary semantic search for Problem 4(ii), strict monotone means, and order-versus-curvature counterexamples.
- Independent symbolic differentiation of the two one-variable sections.

Residual risks:
- None.

## Originality — PASS

Best-of-knowledge originality passes. The complete 2016 source explicitly poses Problem 4(ii) in exactly the strict symmetric homogeneous monotone setting. Resultary searches returned the assigned finding as the only exact solution; the related 2016 characterization paper supplies a broad parametrization framework but no inspected statement that implies these order-curvature counterexamples.

### Equivalent formulations

Searches:
- Resultary semantic search: Raissouli Sandor Problem 4(ii) monotone mean convex concave counterexample
- Exact primary Problem 4(ii) text in the 2016 source

Evidence:
- The source asks whether every such mean below \(A\) is strictly concave and every such mean above \(A\) strictly convex.
- The assigned finding is the exact published-record hit.

Reasoning: Equivalent formulations include counterexamples to order-relative-to-arithmetic-mean forcing curvature and profile functions whose sign is fixed while their second derivative changes sign.

### Broader coverage

Searches:
- Raïssouli--Sándor 2016 full text
- Raïssouli--Rezgui 2016 characterization paper

Evidence:
- The source provides examples motivating the conjecture and explicitly leaves Problem 4(ii) open.
- The characterization work is broader on representing strict means but does not itself force curvature from order.

Reasoning: No broader inspected theorem covers the counterexamples.

### Exact database or table

Searches:
- Resultary exact-topic search
- Searches for quartic-profile mean counterexamples

Evidence:
- No earlier exact family or database entry was located.

Reasoning: This is a constructive analytic counterexample, not a numerical table claim.

### Claim versus prior implication

Searches:
- Primary open problem versus audited family

Evidence:
- The source contains no counterexample and explicitly asks for proof or disproof.
- The audited family satisfies every listed hypothesis and violates each proposed conclusion.

Reasoning: The final theorem directly resolves the stated open implication rather than being a special case of a stronger known theorem.

### Source inspections

- **Sub-super-stabilizability of certain bivariate means via mean-convexity** — The problem is genuinely posed there and the audited counterexample family is not in the source. Material read: Complete open full text, including Sections 2--5 and the exact wording of Problem 4(ii). Method: Primary full-text inspection. Evidence: Problem 4(ii) asks precisely whether strict monotone symmetric homogeneous means below \(A\) must be concave and those above \(A\) convex.

Checked sources:
- M. Raïssouli and J. Sándor, Sub-super-stabilizability of certain bivariate means via mean-convexity, J. Inequalities Appl. 2016:273, complete open full text inspected.
- M. Raïssouli and A. Rezgui, Characterization of homogeneous symmetric monotone bivariate means, J. Inequalities Appl. 2016:217, related characterization source.
- Resultary semantic search for Problem 4(ii), strict monotone means, and order-versus-curvature counterexamples.
- Independent symbolic differentiation of the two one-variable sections.

Residual risks:
- Terminology-equivalent prior counterexamples outside the indexed mean-inequality literature remain a best-of-knowledge risk.

## Scientific value — PASS

The finding resolves both halves of an explicit published open problem with smooth one-parameter counterexample families and exposes the structural reason the conjecture fails: pointwise order is governed by the profile value while curvature is governed by its second derivative. This is a motivated analytic boundary result.

Checked sources:
- M. Raïssouli and J. Sándor, Sub-super-stabilizability of certain bivariate means via mean-convexity, J. Inequalities Appl. 2016:273, complete open full text inspected.
- M. Raïssouli and A. Rezgui, Characterization of homogeneous symmetric monotone bivariate means, J. Inequalities Appl. 2016:217, related characterization source.
- Resultary semantic search for Problem 4(ii), strict monotone means, and order-versus-curvature counterexamples.
- Independent symbolic differentiation of the two one-variable sections.

Residual risks:
- Terminology-equivalent prior counterexamples outside the indexed mean-inequality literature remain a best-of-knowledge risk.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
