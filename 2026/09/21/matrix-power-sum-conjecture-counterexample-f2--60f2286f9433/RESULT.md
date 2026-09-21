# A degree-23 counterexample to a matrix power-sum conjecture over \(\mathbf F_2\)

## Statement

For \(a,b\ge 0\), let \(\Omega_{a,b}\) be the set of words in two noncommuting letters \(x,y\) having exactly \(a\) occurrences of \(x\) and \(b\) occurrences of \(y\), and define
\[
T_{a,b}:=\sum_{w\in\Omega_{a,b}}\ \sum_{A,B\in M_2(\mathbf F_2)} w(A,B).
\]

Then
\[
\boxed{T_{5,18}=I_2.}
\]
In particular, Conjecture 3 of Fortuny--Grau--Oller-Marcén--Rúa, *On power sums of matrices over a finite commutative ring*, is false.

More precisely, in \(M_2(\mathbf F_2[t])\),
\[
\boxed{
\sum_{A,B\in M_2(\mathbf F_2)}(tA+B)^{23}
=
t^5(t+1)^5(t^2+t+1)(t^3+t+1)(t^3+t^2+1)\,I_2.
}
\]
Consequently the nonzero degree-\(23\) word sums \(T_{a,23-a}\) occur exactly for
\[
a\in\{5,6,7,9,10,11,12,13,14,16,17,18\},
\]
and every one of them equals \(I_2\).

An exact exhaustive check also gives
\[
T_{a,b}=0
\qquad
(a,b\ge1,\ a+b\le22),
\]
so total degree \(23\) is the first failure of Conjecture 3 in the case \(r=2\).

## Why this is the conjectured quantity

Because \(t\) is central,
\[
(tA+B)^N
=
\sum_{a+b=N} t^a
\sum_{w\in\Omega_{a,b}}w(A,B).
\]
After summing over all \(A,B\in M_2(\mathbf F_2)\), the coefficient of \(t^a\) is exactly \(T_{a,N-a}\). Thus the displayed polynomial identity gives \(T_{5,18}=I_2\neq0\).

Fortuny--Grau--Oller-Marcén--Rúa formulate Conjecture 3 for \(p=d=2\), \(r>1\), asserting that the corresponding sum vanishes for every multidegree. The choice \(r=2\) and multidegree \((5,18)\) is therefore a direct counterexample.

## Exact verification

The artifact `artifacts/verify.py` uses only exact arithmetic over \(\mathbf F_2\) and contains two checks.

First, for each of the \(16^2=256\) ordered pairs \((A,B)\), it computes
\[
P_{a,b}(A,B)=\sum_{w\in\Omega_{a,b}}w(A,B)
\]
from
\[
P_{0,0}=I_2,\qquad
P_{a,b}=P_{a-1,b}A+P_{a,b-1}B.
\]
Summing these values over all pairs proves the stated first-failure degree and the twelve nonzero degree-\(23\) multidegrees.

Second, independently of that shuffle table, it represents polynomials over \(\mathbf F_2\) as coefficient bitsets and computes
\[
\sum_{A,B}(tA+B)^{23}
\]
by polynomial-matrix binary exponentiation. It verifies that the result is diagonal with both diagonal entries equal to
\[
t^5(t+1)^5(t^2+t+1)(t^3+t+1)(t^3+t^2+1)
\]
and zero off diagonal.

The verification is finite and exhaustive; it does not use sampling or floating-point arithmetic.

## Relation to the original paper

The 2017 paper proves several vanishing results for matrix power sums and then states Conjectures 2 and 3 as the remaining computationally supported ingredients for a general formula. Its Proposition 13 and the subsequently stated general theorem are explicitly conditional on those conjectures.

The counterexample above invalidates Conjecture 3 and therefore that proposed proof route. It does **not** by itself disprove the paper's Conjecture 1 about the final value of
\[
S_k^d(R)=\sum_{M\in M_d(R)}M^k
\]
for arbitrary finite commutative rings: cancellation among different multidegrees after substituting a ring basis may still occur.

## Limitations

- The result refutes Conjecture 3, not Conjecture 1 or Conjecture 2.
- The minimality statement is only for \(r=2\): total degree \(23\) is the first nonzero \(T_{a,b}\) with both coordinates positive.
- The polynomial identity and minimality are established by transparent exact finite enumeration rather than a closed-form classification of all multidegrees.
- Originality is to the best of our knowledge. Targeted searches through the present found the original conjecture and later papers that cite or concern adjacent matrix-power questions, but no published correction, counterexample, or equivalent degree-\(23\) identity. A differently phrased or poorly indexed antecedent remains possible.

## References

1. P. Fortuny, J. M. Grau, A. M. Oller-Marcén, I. F. Rúa, “On power sums of matrices over a finite commutative ring,” *International Journal of Algebra and Computation* **27** (2017), no. 5, 547–560. DOI: https://doi.org/10.1142/S0218196717500278
2. Author manuscript / arXiv version: https://arxiv.org/abs/1505.08132
