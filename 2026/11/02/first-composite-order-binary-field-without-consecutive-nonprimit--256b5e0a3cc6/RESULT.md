# First composite-order binary field without consecutive nonprimitive elements

## Finding

Let \(\mathbb F_q\) be a field of even order, and call a nonzero element **nonprimitive** when its multiplicative order is strictly less than \(q-1\). A *consecutive nonprimitive pair* is a pair \((x,x+1)\) of nonprimitive elements. Write \(A_q\) for the nonprimitive set.

**Theorem.** In \(\mathbb F_{2048}\), the nonprimitive set consists of exactly \(111\) elements and is disjoint from its additive translate:
\[
2048-1=23\cdot89,\qquad A_{2048}=\mu_{23}\cup\mu_{89},\qquad
|A_{2048}|=111,\qquad A_{2048}\cap(A_{2048}+1)=\varnothing,
\]
where \(\mu_e=\{x:x^e=1\}\) is taken inside \(\mathbb F_{2048}\). This is the **smallest even field whose multiplicative group has composite order but which has no consecutive nonprimitive pair**.

Consequently, writing \(\theta_q=\varphi(q-1)/(q-1)\), we have
\[
\theta_{2048}=\frac{1936}{2047}.
\]
For any real constant \(c\) such that \(\theta_q<c\) guarantees a consecutive nonprimitive pair in every even finite field other than \(\mathbb F_4,\mathbb F_8\), one necessarily has \(c\le1936/2047\). This is an obstruction to improving a general sufficient density threshold, not an assertion that this upper bound is attainable.

## Assumptions and scope

All polynomial certificates below are over \(\mathbb F_2[T]\). In this characteristic, \(x+1=x-1\). Elements of multiplicative order \(1\), including \(1\) itself, count as nonprimitive; \(0\) is excluded. The field \(\mathbb F_{2048}\) exists uniquely up to isomorphism. The theorem concerns exact nonexistence at this field size and the least-composite-order boundary, not all finite fields with larger \(\theta_q\).

## Proof

**1. Reduce nonprimitivity to two subgroups.** The multiplicative group of a finite field is cyclic. Since \(2047=23\cdot89\), with both factors prime, an element has order less than \(2047\) exactly when its order divides \(23\) or \(89\). Thus \(A_{2048}=\mu_{23}\cup\mu_{89}\). Both subgroups exist, have sizes \(23\) and \(89\), and intersect in \(\mu_1=\{1\}\). Therefore \(|A_{2048}|=23+89-1=111\).

**2. Prove translated subgroup disjointness by exact polynomial identities.** Define \(F_r(T)=T^r+1\), \(G_s(T)=(T+1)^s+1\), for \(r,s\in\{23,89\}\). Given a nonnegative integer \(c\), define its bit polynomial \(\mathcal P(c)=\sum_{j\ge0}(\lfloor c/2^j\rfloor\bmod2)T^j\in\mathbb F_2[T]\). The following four pairs of hexadecimal integers provide explicit Bézout certificates:

| \((r,s)\) | \(U_{r,s}\) | \(V_{r,s}\) |
| --- | --- | --- |
| \((23,23)\) | `0xfeff` | `0x8101` |
| \((23,89)\) | `0x16d4b3de4c40fc98972d82d` | `0x6df116` |
| \((89,23)\) | `0x6d89f3` | `0x16c591d9c33949f6cda888b` |
| \((89,89)\) | `0x355f8a2bfd500aa0202023` | `0x264c993ebd7af5f264c991` |

For each row, direct multiplication in \(\mathbb F_2[T]\) gives the **polynomial identity**
\[
\mathcal P(U_{r,s})F_r(T)+\mathcal P(V_{r,s})G_s(T)=1.
\]
These four finite identities are exact, not sampled evaluations; `check_np2048.py` independently checks their complete coefficients using carryless integer polynomial multiplication. If \(x\in\mu_r\) and \(x+1\in\mu_s\), evaluating the corresponding identity at \(T=x\) gives \(0=1\), impossible. Taking the union over all four choices proves \(A_{2048}\cap(A_{2048}+1)=\varnothing\).

**3. Prove the first-occurrence assertion.** Consider any smaller even finite field \(\mathbb F_{2^m}\) with composite multiplicative group order \(2^m-1\). We have \(2\le m<11\). For prime \(m\in\{2,3,5,7\}\), the numbers \(2^m-1=3,7,31,127\), respectively, are prime. Hence any \(m<11\) with composite \(2^m-1\) must itself be composite. Select a proper divisor \(d\) with \(1<d<m\); then \(\mathbb F_{2^d}\) is a proper subfield. For any \(x\in\mathbb F_{2^d}\setminus\{0,1\}\), both \(x\) and \(x+1\) are nonzero and have multiplicative order at most \(2^d-1<2^m-1\). They form a consecutive nonprimitive pair. The obstruction at \(m=11\) is therefore the first with composite multiplicative group order.

**4. Obtain the threshold obstruction.** Euler's function gives \(\varphi(2047)=(23-1)(89-1)=1936\). If \(c>1936/2047\), then \(q=2048\) satisfies \(\theta_q<c\) but has no consecutive nonprimitive pair; it is neither \(q=4\) nor \(q=8\). Thus a sufficient threshold of the indicated form cannot exceed \(1936/2047\).

## Verification

Run `python3 check_np2048.py` using Python's standard library only. It checks each displayed Bézout identity coefficient by coefficient, polynomial coprimality, the irreducibility of \(T^{11}+T^2+1\), a primitive generator in the resulting field, and a separate exhaustive check of all \(2047\) nonzero elements. The expected output is:

```
VERIFY_OK bezout=4 irreducible_degree=11 primitive_generator=yes nonprimitive=111 exhaustive_elements=2047 ordered_NP_pairs=0
```

The polynomial identities alone certify the critical nonexistence result over every extension of \(\mathbb F_2\); the complete enumeration provides an independent finite-field cross-check. All limiting-threshold consequences are logical implications, not extrapolations of enumeration.

## Relationship to prior work

Cohen, *Consecutive non-square non-primitive pairs in a finite field* (arXiv:2604.21429; first public April 23, 2026), asks in Question 7.1 for conditions guaranteeing a consecutive nonprimitive pair in characteristic two. The paper itself proves results for odd-order fields and later acknowledges work addressing its question. Sharma and Basnet, *On Consecutive Non-primitive Elements over Finite Fields* (arXiv:2608.27318; first public August 27, 2026), prove that \(\theta_q<8/9\) guarantees such a pair in even fields apart from \(q=4,8\), and classify several smaller fields. Their result does not imply a pair at \(q=2048\) because \(1936/2047>8/9\), and their displayed classifications do not give this no-pair certificate. The present contribution is a first composite-order **nonexistence** boundary and the associated upper obstruction on a universal sufficient density threshold, not a reproof or sharpening of their lower sufficient threshold.

The factorization \(2^{11}-1=23\cdot89\) and its role as the first composite Mersenne number with prime exponent are classical background, not claimed to be new. Relevant published-record and prior-claim searches did not show a covering theorem, but priority is not guaranteed by absence from these sources.

## Limitations

This is an exact finite boundary, not a classification of all pairless binary fields or an optimal universal threshold. It does not show whether a sufficient bound strictly between \(8/9\) and \(1936/2047\) holds. No external independent audit has been performed. Earlier source files may contain unindexed computations or equivalent cyclotomic-number tables; any such material could affect priority.

## References

1. S. D. Cohen, *Consecutive non-square non-primitive pairs in a finite field*, arXiv:2604.21429, first posted 2026-04-23; relevant Question 7.1 and discussion of later results. https://arxiv.org/abs/2604.21429
2. B. Sharma and D. K. Basnet, *On Consecutive Non-primitive Elements over Finite Fields*, arXiv:2608.27318, first posted 2026-08-27; Theorem 1.1, Sections 2–3, Tables 1–3. https://arxiv.org/abs/2608.27318
3. M. Waldschmidt, *Finite Fields*, Section 5.11.1 (background on \(2^{11}-1=23\cdot89\) and the binary Golay code). https://webusers.imj-prg.fr/~michel.waldschmidt/articles/FiniteFields.pdf
