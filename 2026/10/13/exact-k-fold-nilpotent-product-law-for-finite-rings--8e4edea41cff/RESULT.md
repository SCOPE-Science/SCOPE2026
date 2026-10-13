# Exact \(k\)-fold nilpotent-product law for finite rings

## Finding

For a finite associative ring \(R\) with identity, let \(J=J(R)\), and let its semisimple quotient have the Artin–Wedderburn decomposition
\[
R/J\cong\prod_{i=1}^{t}M_{n_i}(\mathbb F_{q_i}),
\]
where \(n_i\ge1\) and each \(q_i\) is a prime power. For every integer \(k\ge1\), sample \(a_1,\ldots,a_k\) independently and uniformly from \(R\). Then
\[
\boxed{\Pr(a_1a_2\cdots a_k\text{ is nilpotent})
=\prod_{i=1}^{t}\left[1-\left(1-q_i^{-n_i}\right)^k\right].}
\]
The empty product is interpreted as \(1\), covering the zero ring. In particular, for every \(n\ge1\) and prime power \(q\),
\[
\Pr\bigl(A_1\cdots A_k\text{ nilpotent in }M_n(\mathbb F_q)\bigr)
=1-(1-q^{-n})^k.
\]
This coincides with the probability that a product of \(k\) uniform elements of the field \(\mathbb F_{q^n}\) equals zero. The entire sequence of nilpotent-product probabilities is unchanged by replacing each simple matrix factor \(M_{n_i}(\mathbb F_{q_i})\) by the field \(\mathbb F_{q_i^{n_i}}\), or by changing the nilpotent Jacobson radical without changing the semisimple quotient.

## Assumptions and scope

All rings here are finite, associative, and unital; the zero ring is allowed. "Nilpotent" means that a positive power of the element is zero, not that the individual random factors are nilpotent. The integers \(k\) range over all \(k\ge1\); the factors are independent and uniform. No commutativity assumption is imposed. If \(R\ne0\), then \(t\ge1\), \(q_i\ge2\), and \(n_i\ge1\). No assertion is made for nonunital rings, infinite rings, or nonuniform factor distributions.

## Proof

**1. One uniform factor following an arbitrary fixed matrix.** Let \(V\) be an \(n\)-dimensional vector space over \(\mathbb F_q\). Fix \(A:V\to V\) of rank \(r\), with image \(U\). Let \(B:V\to V\) be uniformly random. The restriction \((AB)|_U:U\to U\) is uniform on \(\operatorname{End}_{\mathbb F_q}(U)\): on a fixed basis of \(U\), the images under \(B\) are independent uniform elements of \(V\), and applying the surjection \(A:V\twoheadrightarrow U\) gives independent uniform elements of \(U\). Also, \(AB(V)\subseteq U\), so \(AB\) is nilpotent exactly when \((AB)|_U\) is nilpotent. Indeed, if the restriction has zero \(m\)-th power for some positive \(m\), then \((AB)^{m+1}=0\); conversely, nilpotency of \(AB\) implies nilpotency of its restriction. The classical finite-field nilpotent enumeration (Fine–Herstein; see Leinster, Theorem 5) gives exactly \(q^{r^2-r}\) nilpotent endomorphisms out of \(q^{r^2}\) endomorphisms of \(U\), including the dimension-zero convention. Thus
\[
\Pr(AB\text{ nilpotent}\mid A)=q^{-r}=\frac{|\ker A|}{q^n}.
\]
For clarity about this input lemma: Leinster constructs a bijection \(\operatorname{Nil}(U)\times U\cong\operatorname{End}(U)\) by combining the nilpotent cyclic chain of a distinguished vector, choices of complementary subspaces, and the Fitting nilpotent/automorphism decomposition. Taking cardinalities proves the enumerative identity; this is an infinite-family theorem, not an extrapolation from finite checks.

**2. Arbitrarily many uniform matrix factors.** Let \(A_1,\ldots,A_k\) be independently uniform, and put \(T=A_1\cdots A_{k-1}\), with \(T=I\) for \(k=1\). By Step 1 and conditioning on \(T\),
\[
\Pr(A_1\cdots A_k\text{ nilpotent})
=\mathbb E\,q^{-\operatorname{rank}(T)}
=q^{-n}\mathbb E|\ker T|.
\]
For \(v\ne0\), the random vector \(Tv\) is nonzero precisely when \(k-1\) independent uniform endomorphisms successively map a nonzero vector to a nonzero vector. For any fixed nonzero \(w\), a uniform endomorphism sends \(w\) uniformly into \(V\), so each conditional survival probability is \(1-q^{-n}\). Hence
\[
\Pr(Tv=0)=1-(1-q^{-n})^{k-1}\qquad(v\ne0).
\]
Linearity of expectation, summing the indicators \(1_{\{Tv=0\}}\) over all \(q^n\) vectors, gives
\[
\mathbb E|\ker T|=1+(q^n-1)\left[1-(1-q^{-n})^{k-1}\right].
\]
Dividing by \(q^n\) and simplifying yields \(1-(1-q^{-n})^k\) exactly. This argument applies to all \(n\ge1\), all prime powers \(q\), and all positive \(k\), with no rank-distribution assumptions.

**3. Passage from a matrix algebra to any finite unital ring.** The Jacobson radical \(J\) of a finite ring is a nilpotent two-sided ideal: choose \(s\ge1\) with \(J^s=0\). For any \(x\in R\), its image \(\bar x\in R/J\) is nilpotent if and only if \(x\) is nilpotent. The forward implication follows because \(\bar x^m=0\) implies \(x^m\in J\), and consequently \(x^{ms}=0\); the reverse implication follows from the quotient homomorphism. Therefore the event that a product is nilpotent depends only on the images of its factors in \(R/J\). The quotient map has equal-sized fibers, so independent uniform elements of \(R\) project to independent uniform elements of \(R/J\). Direct products turn the event into independent componentwise events; their probabilities multiply. By the Wedderburn structure theorem, \(R/J\) is a product of full matrix algebras over finite fields. Applying Step 2 componentwise proves the asserted formula.

## Verification

The standalone standard-library program `verify.py` independently enumerates complete finite multiplication distributions, rather than relying on random sampling. It verifies \(n=2,q=2\) for \(k=1,2,3,4\), \(n=2,q=3\) for \(k=1,2,3\), and \(n=3,q=2\) for \(k=1,2,3\). It also checks \(k\le4\) in the upper-triangular binary \(2\times2\) ring and \(\mathbb Z/4\mathbb Z\), and \(k\le3\) in \(\mathbb F_2\times M_2(\mathbb F_2)\), for \(21\) exact comparisons in total. Run `python3 verify.py` using Python 3 and no external packages. The expected final line is `EXACT_CHECKS=21 VERIFY_OK`. Exhaustive finite examples are corroboration of the proof, not substitutes for the universal argument.

## Relationship to prior work

Dolžan, *The multiplication probability of a finite ring* (arXiv:2504.12886, first submitted 2025-04-17), determines the pointwise distribution of a **two-factor** matrix product and studies quotient bounds. Its Theorem 3.2 is a strictly more detailed description of two uniform factors, but it does not state an arbitrary-length nilpotent-product law, the elementary fixed-image conditional reduction, or the Jacobson-radical invariance of the nilpotent event. In particular, the \(k=2\) matrix case can be recovered by summing Dolžan's formula over nilpotent target matrices; the new content is not a claim of a new two-factor convolution table.

Sarma and Subedi, *The probability that the product of k elements in a finite ring is zero* (arXiv:2506.10392, 2025), treats **zero products**, chiefly in finite commutative rings; its field formula includes the \(n=1\) special case of the present result, which is not claimed as new. Leinster, *The probability that an operator is nilpotent* (arXiv:1912.12562), establishes the classical single-factor nilpotent count used in Step 1. For contextual comparison, Sarma and Subedi's later *Nilpotent Product Probability of Finite Rings* (arXiv:2610.07892, first submitted 2026-10-06) considers **two factors**, derives commutative-ring classifications, and does not state the \(k\)-factor noncommutative formula. The last paper postdates the 2026-10-04 literature window for the present motivating source.

## Limitations

No result is asserted for dependent factors, arbitrary nonuniform distributions, infinite or nonunital rings, or exact distribution among distinct nilpotency indices. The formula determines only the probability of nilpotency, not the full distribution of product matrices. The classical nilpotent enumeration and finite-ring structure theorem are cited mathematical inputs, each with well-established proofs. The motivating primary source has primary MSC2020 16P10. This statement has not undergone independent audit; older literature on random matrix semigroups could contain an equivalent probabilistic formulation despite the comparisons recorded here.

## References

- D. Dolžan, *The multiplication probability of a finite ring*, arXiv:2504.12886v1 (2025-04-17), https://arxiv.org/abs/2504.12886. Primary MSC2020 16P10.
- D. Sarma and T. Subedi, *The probability that the product of k elements in a finite ring is zero*, arXiv:2506.10392v1 (2025-06-12), https://arxiv.org/abs/2506.10392.
- T. Leinster, *The probability that an operator is nilpotent*, arXiv:1912.12562, https://arxiv.org/abs/1912.12562, Theorem 5; see also N. J. Fine and I. N. Herstein, *The probability that a matrix be nilpotent*, Illinois J. Math. 2 (1958), 499–504.
- D. Sarma and T. Subedi, *Nilpotent Product Probability of Finite Rings*, arXiv:2610.07892v1 (2026-10-06), https://arxiv.org/abs/2610.07892. Included only as a later comparison, not as the dating or primary classification source.
