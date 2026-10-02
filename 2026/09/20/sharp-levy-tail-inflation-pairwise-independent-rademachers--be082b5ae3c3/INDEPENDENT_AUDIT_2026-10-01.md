# Independent scientific audit — SCOPE-20260920-be082b5ae3c3

Audited at: 2026-10-01T21:06:11.107600Z

Disposition: **passed**

## Correctness — PASS

Pairwise independence and centering give \(\mathbb E S_n^2=n\). For odd \(n\), the complement of \(|S_n|\ge2\) has \(S_n^2=1\), while the tail has \(S_n^2\le n^2\), so its probability is at least \(1/(n+1)\) and the ratio is at most \(n+1\). For \(n=2^m-1\), the nonzero characters of \(\mathbb F_2^m\) are pairwise independent Rademachers. In the prescribed six-character prefix, avoiding level two would force three character products to equal \(-1\), although their three indexing vectors sum to zero, a contradiction. The complete character sum is \(n\) at the zero seed and \(-1\) otherwise, so the terminal tail has probability exactly \(1/(n+1)\). Thus equality holds for every \(m\ge4\).

### Correctness sources

- assigned RESULT.md
- assigned artifacts/verify.py
- Révész-Wschebor 1964 full paper
- Lê Vǎn Thành 2023

### Correctness risks

- The exhaustive artifact checks only \(4\le m\le9\); the proof, not the enumeration, establishes all \(m\ge4\).

## Originality — PASS

The finite-field character family and failures of classical maximal inequalities under pairwise independence are prior art, but the inspected Walsh paper studies natural/lacunary partial sums and the 2023 weak-law paper develops maximal weak laws without the Kolmogorov inequality. Neither gives the exact threshold-two maximal-to-terminal ratio or the six-character forcing prefix. Resultary found no earlier published SCOPE theorem with this exact factor/construction.

### Equivalent formulations

Known bad maximal behavior does not imply the exact extremal ratio with matching terminal law.

### Broader coverage

These ingredients do not force a probability-one early excursion while preserving the terminal extremizer; the six-step obstruction is the extra structural lemma.

### Exact database or table

This supports, but does not by itself prove, originality; the full-text Walsh comparison supplies the substantive check.

### Claim versus prior implication

The sharpness proof needs the new three-pair zero-sum contradiction, so the final claim is not a routine corollary of the terminal heavy-tail construction.

### Sources inspected

- On the statistical properties of the Walsh functions — https://real.mtak.hu/189835/1/cut_MATKUTINT_1964_3_pp543_-_554.pdf. NOT_COVERING: It states Walsh functions are pairwise independent and studies bounded natural sums/lacunary subsequences, not the sharp threshold-two Levy ratio.
- On weak laws of large numbers for maximal partial sums of pairwise independent random variables — https://doi.org/10.5802/crmath.387. NOT_COVERING: It develops weak laws while avoiding Kolmogorov's maximal inequality; it does not give the finite exact ratio here.

### Checked sources

- https://real.mtak.hu/189835/1/cut_MATKUTINT_1964_3_pp543_-_554.pdf
- https://doi.org/10.5802/crmath.387
- standard finite-field character construction
- Resultary semantic search

### Residual risks

- Older orthogonal-system or Walsh literature may contain an equivalent extremal ordering under different terminology; no such statement was found in the directly relevant full text.

## Value — PASS

This is a sharp, motivated boundary result for a classical inequality under the natural weakening from mutual to pairwise independence. It gives both the universal optimal order and an explicit infinite sharp family, exposing a linear rather than constant inflation mechanism.

### Value sources

- classical Levy inequality
- Révész-Wschebor 1964
- Lê Vǎn Thành 2023

### Value risks

- The theorem optimizes only threshold two and a sharp subsequence of lengths; arbitrary thresholds and lengths remain open.

## Limitations

- Sharp attainment is proved for \(n=2^m-1\), \(m\ge4\), not every odd length.
- Only threshold two is classified exactly.
- No higher-wise-independence or general-marginal extension is claimed.
- Originality remains best-of-knowledge against older Walsh terminology.
