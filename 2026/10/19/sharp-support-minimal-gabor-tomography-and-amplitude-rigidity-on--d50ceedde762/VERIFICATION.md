---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The group characters of Weyl conjugation are distinct, so the v-squared orthogonal Weyl matrices diagonalize the frame. The Hilbert–Schmidt norm squared of a Weyl matrix is v; summing v-squared equal squared trace magnitudes gives eigenvalue v|A_g|², including zero eigenvalues, with maximum v. Invertibility requires every nonzero difference, and counting ordered pairs at the stated support budget forces precisely a perfect difference set. The unique term for each nonzero shift gives v p_x p_y, repeated v times; shift zero gives v times the squared Fourier magnitudes of the weights. This proves rank and phase independence. The minimum is at most the mean over the ordered distinct-pair products times v, which is v(1−sum p_x²)/[k(k−1)]. Equality requires all positive pair products equal, hence constant weights for k≥3. Character orthogonality for the constant weights gives 1 and (k−1)/k² at zero shift in squared-ambiguity units, and 1/k² at every other shift. In the near-vertex family (1−(k−1)e,e,…,e), at least two small sites exist; the least squared ambiguity is e² for small e since all zero-shift Fourier moduli are ≥1−2(k−1)e. The deficit divided by the squared distance from flat weights tends to v/[k(k−1)], even along invertible windows. The condition ratio is that of the operator frame, not that of the lifting map itself. Independent finite replay: in Z_7 on {0,1,3}, form P from each of the 49 shifts and modulations and evaluate sum_P Tr(PW)P on each Weyl matrix W. Flat weights gave levels 7,14/9,7/9 with multiplicities 1,6,42 and maximum residual about 1e−14; weights (0.5,0.3,0.2) gave full rank and minimum 0.42, below the bound 0.723333…. The numerical check is not an all-groups proof. Bundled verify.py and VERIFICATION.md were inspected, not executed.

## originality

PASS

The spectral reduction and the flat Singer construction are not distinct discoveries. The mirrored Singer record gives the same optimum, optimizer classification and flat spectrum in singular-value units, and its minimax proof works for any perfect support after the Weyl formula; a convention change does not establish novelty. The distinct content supported here is the sharp global squared-amplitude deficit at the support floor, including sharpness over strictly positive, still-invertible windows. The weighted spectrum/rank are explicit consequences of the known spectral reduction and unique differences, not a separate novelty basis. No inspected source establishes the sharp stability statement or supplies it as an existing bound with matching sharpness.

## value

PASS

At the absolute sparsity floor, an experimenter choosing amplitudes needs to know how optima degrade, not just whether generic perturbations preserve rank. The best global coefficient relates measurable spectral loss to squared distance from the optimum over the whole admissible class, and proves how concentrated yet complete windows limit any stronger such global estimate. This is useful beyond the known flat construction and qualitative equality classification; no unrestricted-support or nonlinear phase-retrieval optimality is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
