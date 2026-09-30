# Independent Audit — 2026/09/21/four-way-interaction-sparre-andersen-persistence--a412ed2dcdb6

- Audit date: 2026-09-30 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `16c1ac7b878ee22f1c563c5865bfed3860562088`
- Disposition: **PASSED**

## Correctness

**PASS** — The Walsh-Fourier law is exact: fair 3-wise independence kills every nonconstant coefficient except the fourth-order product, so P(e)=2^-4(1+theta prod e), with |theta|<=1. Consequently every proper subset is iid and the full law is exchangeable. The persistence enumeration is correct under b<2a. In the positive-parity class the four sign patterns beginning with + contribute 1, 1/2, 3/8, and 0, giving 15/64; in the negative-parity class they contribute 1,1,1/2,0, giving 5/16. Their affine mixture is (35-5 theta)/128 and theta=0 gives 35/128. Independent exact rational enumeration verified all one-, two-, and three-sign marginals of both parity classes and the endpoint probabilities.

## Originality

**PASS** — Parity-conditioned and k-wise-independent random walks are established techniques, and Sparre Andersen's dependent fluctuation theory is broad. The closest modern universality result checked assumes exchangeability together with global sign-invariance; the audited parity-tilted laws deliberately violate that global condition while matching every proper-subset law. The located limited-independence papers establish anomalous path behavior but not this exact four-step affine response. Originality is therefore supported for the precise (35-5 theta)/128 formula and the pair of continuous exchangeable models indistinguishable on every proper subset, not for the parity gadget itself.

## Scientific value

**PASS** — The theorem isolates exactly one hidden fourth-order statistic that changes persistence while all lower-order marginals remain iid. It gives a sharp finite-horizon boundary showing why proper-subset information cannot replace global sign-invariance in a modern Sparre-Andersen extension. Its finite-horizon scope and amplitude restriction are stated clearly.

## Sources

- **An application of Sparre Andersen's fluctuation theorem for exchangeable and sign-invariant random variables** — Q. Berger; L. Béthencourt. https://arxiv.org/abs/2304.09031 — Modern universality theorem whose assumptions include global sign-invariance.
- **Random walks with k-wise independent increments** — I. Benjamini; G. Kozma; D. Romik. https://doi.org/10.1214/ECP.v11-1201 — Prior limited-independence random-walk constructions using parity/product mechanisms.
- **Extremal persistence probabilities of exchangeable sign-invariant random variables** — D. Iľkovič; J. Yan. https://arxiv.org/abs/2609.05586 — Recent persistence work inside the exchangeable sign-invariant class, distinct from the audited non-sign-invariant parity tilt.

## Limitations

- This is a four-step theorem, not an asymptotic persistence result.
- The distribution-free constants use the sufficient amplitude condition b<2a.
- The result does not classify arbitrary 3-wise independent real-valued increment laws.
- Older dependent-fluctuation literature is broad, leaving residual risk of an equivalent finite observation under different terminology.

## Independent checks

```json
{
  "walsh_law_reconstructed": true,
  "proper_subset_marginals_exactly_checked": true,
  "positive_parity_persistence": "15/64",
  "negative_parity_persistence": "5/16",
  "iid_midpoint": "35/128",
  "separation": "5/64",
  "source_tree_unchanged": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned record tree was unchanged from the inventory snapshot through the checked commit. GitHub was used only as read-only evidence. Open-access and preprint sources were checked first, and no decisive comparison required institutional retrieval. No GitHub write or separate dispatcher report was performed.
