# Scientific review

## Correctness — PASS

The theorem concerns every dyadic length \(2^k\), for \(k\ge0\), and the all-length asymptotic exponent. The four-state substitution is shown to agree with the digit definition, including the convention \(b(0)=1\). At each dyadic scale, the identities \(A_k=B_k+C_k\) coordinatewise and \(D_k=0^{2^k}\) are proved inductively. Every factor is a suffix/prefix of aligned blocks, and each is bounded by a rotation of \(A_k\), so the initial dyadic prefix maximizes ones. Fibonacci counts, zero-factor availability, and the intermediate-value property of sliding one-counts give all Parikh vectors. Monotonicity extends the exponent to every length. The included finite test passed, but the infinite argument does not rely on extrapolation.

## Originality — PASS, subject to stated risks

Merta's 2018 Baum–Sweet study supplies recurrences, zero runs and Fibonacci-related information, without the required maximum over *every shifted* dyadic window. Cicalese–Lipták–Rossi give the general relationship between binary abelian complexity and extremal counts, but do not evaluate this invariant for the Baum–Sweet word. The block-domination proof supplies an extra upper bound not implied by knowing the Fibonacci count in the initial prefix. Targeted terminology, known tables, and published-result comparisons did not identify a stronger or equivalent statement. Unindexed equivalent work remains possible; search absence does not prove novelty.

## Value — PASS

A natural combinatorics-on-words invariant receives an exact formula at every intrinsic substitution scale, plus a sharp growth exponent at *all* lengths. The structural insight is the extremality of the Baum–Sweet dyadic initial factor under arbitrary shifts, not merely a Fibonacci recomputation. No nondyadic exact expression, whole-word prefix-normality, or independent validation is claimed.

## Closest literature and limitations

- Ł. Merta, *Composition inverses of the variations of the Baum–Sweet sequence*, arXiv:1803.00292v1, 2018.
- F. Cicalese, Z. Lipták, M. Rossi, *On Infinite Prefix Normal Words*, arXiv:1811.06273v1, 2018.

The proof is symbolic; the packaged verifier supplies finite corroboration only. The scope excludes an exact abelian-complexity formula for nondyadic lengths. Priority uncertainty from unindexed equivalent work persists.

Self-review: passed. Independent audit: not yet performed.
