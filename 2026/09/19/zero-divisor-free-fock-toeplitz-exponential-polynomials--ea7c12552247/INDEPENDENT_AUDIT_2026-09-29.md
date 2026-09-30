# Independent Audit — 2026/09/19/zero-divisor-free-fock-toeplitz-exponential-polynomials--ea7c12552247

- Audit date: 2026-09-29 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `ea89f10d8738a650f1e6401b00d0dd2240b28102`
- Disposition: **PASSED**

## Correctness

**PASS** — For q(z)=p(z)e^{a.z}, the Fock reproducing formula gives T_q as holomorphic multiplication and T_conj(q)=p#(partial) tau_conj(a) on the exponential-polynomial domain. Hence every generator is a finite differential-difference operator. Writing U_(a,b)=E_a tau_b gives the stated Weyl-algebra automorphism and nonzero scalar 2-cocycle. The frequencies occurring in any product generate a finitely generated torsion-free abelian group, so a translation-invariant total order exists. The unique maximal support coefficient in a product is nonzero because the Weyl algebra is a domain, proving the formal crossed product is a domain. Faithfulness is correctly established by acting on e^{lambda.z}: linear independence of finite exponential-polynomials first in z and then in lambda kills every normal-form coefficient. A nonzero pluriharmonic symbol cannot induce the zero operator because its Berezin transform is its Gaussian convolution, which equals the harmonic function itself. Finally, differentiating A e^{lambda.z} at lambda=0 shows that a nonzero finite differential-difference operator must be detected by some polynomial. No bounded-operator assumption is silently used: the theorem is explicitly on the common invariant dense domain E_n.

## Originality

**PASS** — Qin's September 2026 paper constructs zero products for much broader Fock symbols and explicitly leaves the pluriharmonic exponential-type case open. Cichon's older work treats exponential-polynomial Toeplitz symbols in connection with adjoints, and Bauer-Choe-Koo study commuting pluriharmonic Toeplitz operators; targeted searches found no domain/no-zero-divisors theorem for the finite-frequency crossed-product class. The Weyl algebra's domain property and exponential-polynomial linear independence are classical; novelty is the faithful Toeplitz realization and its finite-product zero-divisor consequence for this natural subclass of Qin's open problem.

## Scientific value

**PASS** — The theorem gives a substantial positive region inside a zero-product problem that otherwise has strong counterexamples, works in every complex dimension and for arbitrary finite product length, and identifies finite frequency as an algebraically rigid boundary. It also proves polynomial detection, which makes the nonvanishing assertion testable on the natural core domain.

## Sources

- **Zero-product problem for Toeplitz operators on the Fock space** — Jie Qin. https://arxiv.org/abs/2609.20555 — Primary 2026 source; constructs broad zero divisors and leaves the pluriharmonic exponential-type question open.
- **Generalization of the Newman-Shapiro isometry theorem and Toeplitz operators. II** — Dariusz Cichoń. https://doi.org/10.4064/sm150-2-6 — Prior exponential-polynomial Fock Toeplitz/adjoint background, not the audited crossed-product domain theorem.
- **Commuting Toeplitz operators with pluriharmonic symbols on the Fock space** — Wolfram Bauer; Boo Rim Choe; Hyungwoon Koo. https://doi.org/10.1016/j.jfa.2015.03.003 — Prior pluriharmonic Toeplitz commutation theory; no matching finite-frequency zero-divisor-free algebra statement was located.

## Limitations

- Only finite sums of polynomial amplitudes times linear exponentials are covered; the full exponential-type question remains open.
- The generally unbounded generators are treated on the common invariant dense domain E_n, not asserted bounded on all Fock space.
- No quantitative degree bound is given for the polynomial witness.
- The algebraic ingredients are classical; originality rests on this Toeplitz realization and source-specific zero-product consequence.

## Independent checks

```json
{
  "toeplitz_action_formula_reconstructed": true,
  "crossed_product_leading_support_argument_checked": true,
  "normal_form_faithfulness_checked": true,
  "berezin_harmonic_nonzero_argument_checked": true,
  "polynomial_witness_argument_checked": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Open-access/preprint sources were checked before institutional retrieval. Any inaccessible comparison is explicitly identified above rather than claimed read.
