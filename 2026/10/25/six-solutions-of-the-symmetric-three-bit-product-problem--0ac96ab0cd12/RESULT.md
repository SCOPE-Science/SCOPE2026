# Six solutions of the symmetric three-bit product problem

## Finding

Let \(s_2(n)\) denote the number of one-bits in the standard binary expansion of the positive integer \(n\). Every pair of positive odd integers \((a,b)\) satisfying
\[
s_2(a)=s_2(b)=s_2(ab)=3
\]
is, up to interchanging the factors, one of precisely these six pairs:

| \(a\) | \(b\) | \(ab\) | Binary expansion of \(ab\) |
|---:|---:|---:|---|
| 7 | 7 | 49 | `110001` |
| 7 | 19 | 133 | `10000101` |
| 7 | 37 | 259 | `100000011` |
| 11 | 35 | 385 | `110000001` |
| 13 | 21 | 273 | `100010001` |
| 21 | 49 | 1029 | `10000000101` |

In particular there are six unordered pairs and eleven ordered pairs, with one diagonal pair.

## Assumptions and scope

Factors are positive, odd integers, with \(a\le b\) used solely to remove the ordering symmetry. No bound on either factor or product is assumed in the statement. The theorem uses the published Kaneko--Stoll product bound for binary digit weights, and an exact exhaustive arithmetic computation for the remaining finite range; it does not reprove the published bound.

## Proof

**Global reduction.** Kaneko and Stoll, Theorem 2.2 of *Products of integers with few nonzero digits*, prove: for odd positive integers with \(s_2(a)=\ell\ge2\), \(s_2(b)=m\ge2\), \(\max\{\ell,m\}\ge3\) and \(s_2(ab)=3\), one has
\[
ab<2^{-13+4\ell m}.
\]
Taking \(\ell=m=3\) yields the strict, unconditional bound \(ab<2^{23}\). Since the factors are positive, each factor also lies below \(2^{23}\).

**Complete parametrization.** Every odd positive integer below \(2^{23}\) with precisely three one-bits has a unique expression
\[
1+2^i+2^j,\qquad 1\le i<j\le22.
\]
There are \(\sum_{j=2}^{22}(j-1)=231\) such integers. Therefore every prospective solution is among the unordered pairs from this explicit list, after discarding products at least \(2^{23}\). The program `verify.py` implements exactly this parametrization with integer-only operations, examines all \(3672\) pairs remaining after the strict product cutoff, and selects those products whose binary one-bit counts equal three. It returns precisely the six pairs displayed above. Every computation compares exact unbounded integers; no floating-point approximation is involved.

**Separate exhaustion of the product side.** An alternative search, also in `verify.py`, parametrizes the three-one-bit *product* instead of either factor. There are again exactly \(231\) eligible odd products below \(2^{23}\). For each it examines every odd candidate divisor \(a\) from \(7\) through \(\lfloor\sqrt n\rfloor\); whenever \(a\mid n\), it checks whether both \(a\) and \(n/a\) have exactly three one-bits. This enumeration recovers the same six pairs, and any solution must be found because its lesser factor divides its product and does not exceed its square root.

The published global bound makes these finite enumerations exhaustive for arbitrarily large integers. Each listed pair directly satisfies all the digit-weight conditions. This establishes both necessity and sufficiency.

## Verification

Run `python3 verify.py` with Python 3.8 or newer. The script asserts all six factor/product triples, computes the \(231\) candidate three-bit factors, counts the \(3672\) candidate pairs passing the product cutoff, and independently enumerates three-bit products and their possible divisors. Both algorithms must return the identical six-element set. The actual checked output and limitations appear in `VERIFICATION.md`.

## Relationship to prior work

Kaneko and Stoll [1] formulate the multiplicative binary digit-count problem for arbitrary fixed weights and establish the required finiteness bound for output weight three. Their result does not enumerate the solutions for the symmetric weight triple \((3,3,3)\). Earlier results on sparse squares, discussed in their introduction, cover the diagonal \((7,7)\) instance but do not give the five off-diagonal solutions or prove the list exhaustive. A published classification of the asymmetric triple \((3,2,3)\) concerns one factor of weight two and therefore does not imply the present six-pair classification. The finite census here is a new exact classification under the established global bound, rather than a strengthening of that bound.

## Limitations

The proof depends on the externally proved Kaneko--Stoll bound; the supplied code certifies only the finite range made sufficient by that bound. The result applies specifically to positive *odd* factors and exactly three one-bits in each factor and their product. It does not address other weight patterns, signed factors, or higher bases. Priority over unindexed or implicit antecedents has not been independently established.

## References

[1] H. Kaneko and T. Stoll, *Products of integers with few nonzero digits*, arXiv:2112.03077v1 (first posted 2021-12-06), Theorem 2.2 and its proof in Section 4. https://arxiv.org/html/2112.03077v1

[2] H. Kaneko and T. Stoll, *Products of integers with few nonzero digits*, *Uniform Distribution Theory* **17** (2022), 11–28, DOI 10.2478/udt-2022-0006. https://doi.org/10.2478/udt-2022-0006
