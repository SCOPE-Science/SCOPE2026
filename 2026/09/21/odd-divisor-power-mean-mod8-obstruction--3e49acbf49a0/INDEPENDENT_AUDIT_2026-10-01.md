# Independent scientific audit — SCOPE-20260921-3e49acbf49a0

Audited at: 2026-10-01T23:13:29.436856Z

Disposition: **passed**

## Correctness — PASS

The local identity for \(F_N(1+8h)\) follows by binomial expansion in \(\mathbf Q_2\): the constant and linear terms give \(1+4h(N-1)\) modulo eight and every higher term has 2-adic valuation at least three. Multiplicativity then reduces the theorem to parity of the prime exponents and the supplementary law for \((2/n)\). The even-power corollary follows because every even power of an odd 2-adic unit is one modulo eight. The bounded script was inspected and is corroborative only.

### Correctness sources

- assigned RESULT.md
- assigned artifacts/verify_sigma_r_mod8.py
- OEIS A140480/A003601

### Correctness risks

- The theorem is restricted to odd \(n\); even RMS numbers require different 2-adic analysis.
- The finite check through 200000 is not used as proof.

## Originality — PASS

OEIS A140480 records T. D. Noe's 2008 empirical observation that the displayed odd RMS terms appear to be \(+1\) or \(-1\) modulo eight, and A003601 records the generalized divisor-power-mean terminology. The inspected arithmetic-number literature concerns the first divisor mean. Resultary returned the assigned theorem as the only direct published result among the close hits. No inspected source supplies the proved all-odd-\(n\), all-even-\(r\) 2-adic formula.

### Equivalent formulations

The empirical RMS pattern is prior art, but the theorem is a proof and a uniform generalization, not an equivalent restatement.

### Broader coverage

Neither inspected source gives the even-power 2-adic residue classification, so no broader implication was found.

### Exact database or table

The tabulation establishes examples and prior motivation, not the infinite congruence theorem.

### Claim versus prior implication

The final theorem is not mechanically implied by the empirical sequence data or the r=1 arithmetic-number results.

### Sources inspected

- RMS numbers — https://oeis.org/A140480. PRIOR_EMPIRICAL_PATTERN: The modulo-eight pattern is explicitly empirical prior art; no proof is stated there.
- On arithmetic numbers — https://arxiv.org/abs/1206.1823. NOT_COVERING: It treats the ordinary arithmetic mean of divisors rather than the assigned even-power 2-adic formula.

### Checked sources

- OEIS A140480
- OEIS A224988
- OEIS A003601
- arXiv:1206.1823
- Resultary semantic search

### Residual risks

- Informal sequence discussions or poorly indexed notes could contain a proof of the old RMS observation, but no concrete covering source emerged.

## Value — PASS

The result supplies a proof of a long-recorded residue phenomenon and strengthens it to an exact natural 2-adic invariant for every odd integer and every even divisor-power mean. This is a motivated structural congruence, not merely a finite sequence check.

### Value sources

- OEIS A140480
- OEIS A003601

### Value risks

- For exponents divisible by four the congruence is always one and yields no restriction on \(n\).

## Limitations

- The residue obstruction is for odd \(n\).
- For \(r\equiv0\pmod4\) the mean is always one modulo eight, so no residue restriction on \(n\) follows.
- Originality is best-of-knowledge against incompletely indexed informal sequence discussion.
