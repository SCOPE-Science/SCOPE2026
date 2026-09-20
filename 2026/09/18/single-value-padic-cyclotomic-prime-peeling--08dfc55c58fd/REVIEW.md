# Review

## Scientific claim

The record proves an exact local recursion for recovering the ordered distinct prime divisors of a cyclotomic index from one evaluation \(\Phi_n(x)\), provided a prime \(\ell\mid x\) allows the Möbius sign of the radical to be read locally. The next unrecovered prime is the normalized valuation of a residual obtained by canceling only divisor factors supported on already recovered primes.

The strongest concrete corollaries are that one value \(\Phi_n(3)\) or \(\Phi_n(4)\) suffices for every \(n>1\), while one binary value \(\Phi_n(2)\) suffices for every nonsquarefree \(n>1\).

## Correctness

**PASS.**

The proof reduces \(\Phi_n(x)\) to the squarefree radical:
\[
\Phi_n(x)=\Phi_r(x^a),\qquad r=\operatorname{rad}(n),\ a=n/r.
\]
The lowest nonconstant term
\[
\Phi_r(Y)=1-\mu(r)Y+O(Y^2)
\]
gives the local radical valuation and, under the stated parity hypothesis, the sign \(\mu(r)\).

After the factors indexed by divisors of the product of already recovered primes are canceled, the smallest divisor still present in the Möbius product is exactly the next unrecovered prime \(q\). Its term has coefficient \(\pm1\), and every remaining term has strictly higher \(\ell\)-adic order. This yields the exact valuation \(awq\). Denominators introduced by negative exponents are \(\ell\)-adic units because every \(1-x^{ad}\equiv1\pmod\ell\).

The recursion uses only already recovered primes because for squarefree \(r\) and \(d\mid r\),
\[
\mu(r/d)=\mu(r)\mu(d).
\]
The stop condition is exact: the product of recovered primes reaches \(r=n/a\).

A finite exact-arithmetic regression check agrees with the theorem throughout the stated test range.

## Originality

**PASS, to the best of our knowledge.**

The full relevant statements of Shunia, arXiv:2609.18480v1, were inspected. Its Theorem 3.1 gives the local radical valuation. Theorem 3.4 gives the binary least-prime/squarefreeness extractor, and Corollary 3.5 strips squarefree indices by iteration. The paper also has a separate Archimedean peeling mechanism. It does not state the normalized residual \(p\)-adic recursion proved here, nor the general single-value corollaries at bases such as \(3\) and \(4\), nor the complete binary peeling of nonsquarefree radicals by successive residual valuations.

Pomerance--Rubinstein-Salzedo, arXiv:1903.01962 / Experimental Mathematics 31 (2022), was inspected at its Möbius product, radical-reduction, and first-gap results. Those are background ingredients and do not state the local recursion.

Searches included exact and synonymous formulations involving cyclotomic \(p\)-adic peeling, normalized residual valuations, least-prime extraction from Möbius products, one-value recovery of the prime support of an index, and valuation formulas involving \(\operatorname{rad}(n)\). No stronger or equivalent published theorem was located.

No inaccessible source was identified whose title, abstract, or available metadata specifically indicates this same local recursion. The principal residual originality risk is that the motivating preprint is extremely recent, so contemporaneous work may not yet be indexed.

## Value

**PASS.**

The result turns a one-step local radical extractor into an exact prime-by-prime local decoder. It is structurally different from the unnormalized binary plus-valuation: in the nonsquarefree regime where that valuation collapses to \(1\), the residual valuations recover the entire radical. It also provides a base-independent mechanism and clean all-index specializations at \(x=3\) and \(x=4\).

The theorem is elementary once the correct normalization is identified, but it is not merely a numerical specialization: it supplies a reusable recursion, an exact local analogue of Archimedean factor peeling, and a qualitatively stronger interpretation of what a single cyclotomic value encodes.

## Limitations

The index \(n\) and base \(x\) are inputs. The result does not reconstruct an unknown unlabeled index from \(C\) alone and is not claimed to be an efficient factoring algorithm.

The binary sign step does not cover squarefree indices at \(x=2\); this is stated explicitly. Other methods in the motivating paper handle that regime.

The computational artifact supports but does not replace the proof. No formal proof-assistant verification or independent validation is asserted.

**Same-model review: passed. Independent audit: not yet performed.**
