# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The claimed theorem is the \(k=7\) instance of Chu's Conjecture 5 for
\[
n=2^{\alpha-1}p^{\beta-1},\qquad p<3\cdot2^{\alpha-1}-1.
\]
The proof uses only Chu's general preliminary divisibility conditions and
Lemmas 8--10, plus a new elementary treatment of the \(\beta=4\) case and an
exact finite check after explicit analytic bounds.

The principal correctness risks were checked adversarially:

1. **The exceptional Lemma-10 branch \(p=k\).** For \(k=7\), unlike Chu's
   \(k=5\) proof, this branch cannot simply be ignored because \(7\equiv3\bmod4\).
   The proof isolates \(p=7\). Using \(\alpha\le v+3\) and
   \(\nu_7(S_\alpha)=2+\nu_7(\alpha)\) when \(3\mid\alpha\), it shows that only
   \(v=1,\alpha=3,\beta=2\) survives, giving the valid even perfect number 28.

2. **The \(\beta=4\) obstruction.** Chu's Lemma 7 is specific to \(k=5\), so
   importing it would be invalid. The present proof replaces it. Exact
   2-adic valuation of \(\sigma_7(p^3)\) gives
   \(p=t2^{\alpha-2}-1\), \(1\le t\le5\). Factoring
   \(x^7-1=(x-1)(x^6+\cdots+1)\) and reducing \(tx\equiv4\bmod p\) reduces the
   second factor to five explicit constants. Their prime factors leave no
   admissible prime after separately handling \(p=7,127\).

3. **Division by \(127\).** The cases \(p=127\) are treated separately wherever
   reducing \(S_\alpha=(2^{7\alpha}-1)/127\) could otherwise lose a
   \(p\)-adic factor. LTE gives valuation zero in the relevant \(\beta=4\) and
   \(v=1\) cases.

4. **Exhaustiveness of the finite reduction.** For \(p\equiv3\bmod4\),
   Chu's Lemma 9 bounds \(v\le4\). Lemma 10 gives
   \(\alpha\le\lambda+v\), the common inequality
   \[
   (2^\lambda-1)^{\beta-1}\le\sum_{i=0}^6 2^{i(\lambda+v)},
   \]
   and, together with the original size hypothesis,
   \(q<3\cdot2^{v-1}\) for \(p+1=2^\lambda q\).
   The remaining ranges are therefore genuinely finite, not a truncated
   search. The exact verifier checks all retained primes and all allowed
   \(\alpha\).

5. **Finite arithmetic.** The verifier finds 8, 62, and 33 admissible tuples in
   the three residual families \((v,\beta)=(2,12),(3,8),(4,16)\). The maximum
   values of \(\nu_p(S_\alpha)\) are respectively 1, 1, and 2, below the
   required 11, 7, and 15. A separate direct scan over a broad initial box
   finds only the expected \(\beta=2\) even-perfect cases and excludes 8128.

The backward implication and the \(\beta=2\) classification are exactly Chu's
Theorem 3, whose proof applies to every prime \(k>2\) with \(2^k-1\) prime.

## Originality

**PASS, to the best of our knowledge.**

Chu's 2021 Journal of Integer Sequences paper explicitly proves the full
\(\beta>1\) statement only for \(k=5\), then states Conjecture 5 for general
Mersenne exponents and says the \(k=5\) method does not directly apply to other
values of \(k\). Since \(2^7-1=127\) is prime, \(k=7\) is the next unresolved
instance suggested by that paper.

Current-status searches through 20 September 2026 used the exact paper title
and author, the wording of Conjecture 5, `sigma_7`, "seventh powers of divisors",
the form \(2^{\alpha-1}p^{\beta-1}\), and broader divisor-function/perfect-number
terminology. The Journal of Integer Sequences landing page and the accessible
full paper were inspected. Searches also covered recent web-indexed literature
and arXiv-facing results. No later theorem proving the \(k=7\) instance, nor a
stronger theorem that implies it, was located.

The closest earlier lineage inspected is:
- X.-W. Jiang, *On even perfect numbers* (2018), whose accessible abstract
  states the full \(k=3\) result;
- H. V. Chu (2021), which extends the \(\beta=2\) theorem to general relevant
  \(k\), proves the full exponent theorem for \(k=5\), and explicitly leaves
  the general case conjectural;
- Cai--Chen--Zhang (2015), an earlier predecessor cited by Chu.

The full text of Jiang (2018) was not inspected. Its abstract and Chu's
description identify its central claim as \(k=3\), so it is a low residual
priority risk rather than evidence of coverage. No inaccessible source with a
title or abstract suggesting a \(k=7\) proof was identified. Unindexed or
poorly indexed literature remains a residual originality risk.

## Value

**PASS.**

This resolves a named, explicit conjectural instance left open in a 2021
number-theory paper, rather than supplying a numerical example or a routine
parameter increment. The \(k=7\) case is structurally different from the
published \(k=5\) proof because the exceptional branch \(p=k\) is now compatible
with \(p\equiv3\bmod4\), and because Chu's special \(\beta=4\) lemma no longer
applies. The replacement \(\beta=4\) argument and the bounded
\((v,\beta,\lambda,q,\alpha)\) reduction are reusable for attempts at higher
Mersenne exponents.

The theorem also cleanly advances Conjecture 5 from the known \(k=3,5\)
landscape to the next Mersenne exponent \(k=7\), while explicitly leaving the
higher cases open.

## Limitations

Only the \(k=7\) case is proved; no claim is made for \(k=13,17,19,\ldots\).
The final bounded elimination is computer-assisted but exact and reproducible.
The full text of Jiang (2018) was not inspected. No formal proof-assistant
verification or independent audit has been performed.
