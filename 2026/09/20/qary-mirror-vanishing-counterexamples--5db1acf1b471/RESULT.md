# Sharp dimension-two counterexamples to q-ary mirror vanishing

## Statement

Let \(q\ge 3\) be a prime power, let \(d\ge 2\), and let \(t\ge 1\). There exists a q-ary linear code
\[
C\text{ with parameters }[2d+1,2,d]_q
\]
such that
\[
A_{d+1}=A_{d+2}=\cdots=A_{d+t}=0
\quad\text{and}\quad
A_{2d+1}>0
\]
if and only if
\[
 d\le (q-1)(d-t),
\]
equivalently
\[
 t\le d-\left\lceil\frac{d}{q-1}\right\rceil.
\]

Every such code satisfies the dimension hypothesis
\[
 k\ge n-2d+1
\]
with equality. Hence, whenever the displayed inequality holds, it is a counterexample to the direct q-ary analogue of the binary mirror-vanishing implication
\[
A_{d+1}=\cdots=A_{d+t}=0
\Longrightarrow
A_{2d+1}=\cdots=A_{2d+t}=0.
\]
Since \(n=2d+1\), the first mirrored weight \(2d+1\) is the only nonvacuous one in this extremal dimension-two family.

In particular:

- for every fixed \(q\ge3\), one may take
  \[
  t=d-\left\lceil\frac{d}{q-1}\right\rceil,
  \]
  so the local gap can have asymptotic relative length \((q-2)/(q-1)\);
- for \(q=3\), there are counterexamples with \(t=\lfloor d/2\rfloor\);
- if \(q\ge d+1\), there are counterexamples with the maximal possible gap
  \[
  A_{d+1}=\cdots=A_{2d-1}=0
  \]
  while \(A_{2d+1}>0\).

## Context

A recent binary result proves that if a binary linear \([n,k,d]\) code satisfies \(k\ge n-2d+1\) and has a local gap \(A_{d+1}=\cdots=A_{d+t}=0\), then it also has the mirror gap \(A_{2d+1}=\cdots=A_{2d+t}=0\). Its proof uses the binary-only disjoint-support decomposition of nonminimal codewords. The same paper explains that the proof does not extend to larger alphabets and states that a q-ary analogue would require additional conditions, but the example discussed there does not satisfy the local-gap hypothesis. The theorem above gives an explicit infinite family that satisfies the full binary hypotheses and violates the first mirrored conclusion, and it gives the sharp gap-length threshold for this dimension-two extremal family.

## Proof

Use the standard geometric representation of a full-length q-ary \([n,2]\) linear code by a spanning multiset of points on the projective line
\[
\operatorname{PG}(1,q),
\]
which has \(q+1\) points. Let \(m(P)\) be the multiplicity of a projective point \(P\). A nonzero codeword, up to nonzero scalar multiplication, corresponds to a projective hyperplane. On \(\operatorname{PG}(1,q)\), a hyperplane is a single point, and the corresponding codeword has weight
\[
 n-m(P).
\]
Thus each projective point contributes \(q-1\) nonzero codewords of weight \(n-m(P)\).

### Necessity

Suppose a q-ary \([2d+1,2,d]\) code satisfies
\[
A_{d+1}=\cdots=A_{d+t}=0
\quad\text{and}\quad
A_{2d+1}>0.
\]
The existence of a full-weight codeword implies that the generator matrix has no zero column, so the projective-multiset model has total multiplicity exactly
\[
\sum_P m(P)=2d+1.
\]

Because the minimum distance is \(d\), the maximum projective-point multiplicity is
\[
\max_P m(P)=(2d+1)-d=d+1.
\]
There can be only one point of multiplicity \(d+1\), since two such points would already have total multiplicity \(2d+2\). Also, \(A_{2d+1}>0\) means that at least one projective point has multiplicity zero.

The forbidden weights \(d+1,\ldots,d+t\) correspond exactly to forbidden multiplicities
\[
(2d+1)-(d+j)=d+1-j,
\qquad 1\le j\le t,
\]
that is,
\[
d+1-t,\ldots,d.
\]
Therefore every projective point other than the unique point of multiplicity \(d+1\) has multiplicity at most \(d-t\), except that at least one such point has multiplicity zero.

After removing the unique point of multiplicity \(d+1\) and one empty point, at most \(q-1\) projective points remain. Their multiplicities sum to
\[
(2d+1)-(d+1)=d,
\]
and each is at most \(d-t\). Hence
\[
d\le(q-1)(d-t).
\]
This proves necessity.

### Sufficiency

Assume
\[
d\le(q-1)(d-t).
\]
Choose two distinguished points \(P_\star,P_0\in\operatorname{PG}(1,q)\). Set
\[
m(P_\star)=d+1,
\qquad
m(P_0)=0.
\]
There are \(q-1\) other projective points. Because \(d\le(q-1)(d-t)\), choose nonnegative integers on those points summing to \(d\), each at most \(d-t\). This defines a projective multiset of total size \(2d+1\). Since \(t\ge1\), the remaining multiplicity \(d\) cannot all lie on one point under the cap \(d-t<d\), so the multiset spans \(\operatorname{PG}(1,q)\) and defines a dimension-two code.

The point \(P_\star\) yields weight
\[
(2d+1)-(d+1)=d,
\]
so the minimum distance is at most \(d\). Every other projective point has multiplicity at most \(d-t<d+1\), so all other nonzero weights are strictly larger than \(d\); hence the minimum distance is exactly \(d\).

For every other point \(P\), either \(m(P)=0\), giving the full weight \(2d+1\), or
\[
1\le m(P)\le d-t,
\]
which gives
\[
\operatorname{wt}=2d+1-m(P)\ge d+t+1.
\]
Therefore
\[
A_{d+1}=\cdots=A_{d+t}=0,
\]
while the distinguished empty point gives
\[
A_{2d+1}>0.
\]
This proves sufficiency.

Finally,
\[
 n-2d+1=(2d+1)-2d+1=2=k,
\]
so these counterexamples meet the binary theorem's dimension inequality with equality.

## Smallest example

For \(q=3,d=2,t=1\), take projective multiplicities on the four points of \(\operatorname{PG}(1,3)\)
\[
(3,1,1,0).
\]
The resulting ternary \([5,2,2]\) code has nonzero weights
\[
2,4,5,
\]
with multiplicities
\[
A_2=2,\qquad A_4=4,\qquad A_5=2.
\]
Thus \(A_3=0\) but \(A_5>0\), even though
\[
2=n-2d+1.
\]
One generator matrix is
\[
G=
\begin{pmatrix}
1&0&0&1&0\\
0&1&2&2&1
\end{pmatrix},
\]
whose projective-column multiplicities are \((1,3,1,0)\), a permutation of the pattern above.

## Verification

`artifacts/verify_projective_line.py` constructs the family over the prime fields \(q=3,5,7,11,13\) for 280 feasible parameter triples and directly enumerates every codeword. It also exhaustively enumerates projective-point multiplicity vectors for 42 small \((q,d,t)\) cases and checks the sharp iff threshold. The recorded output is in `artifacts/verification.txt`.

The computational check is only a finite sanity check. The theorem for all prime powers follows from the projective-line counting argument above.

## Originality boundary

The geometric correspondence between linear codes and multisets of projective points is classical and is not claimed as new. Nor is the binary mirror-vanishing theorem. The claim here is the sharp dimension-two q-ary obstruction: the exact condition
\[
t\le d-\left\lceil\frac d{q-1}\right\rceil
\]
for a \([2d+1,2,d]_q\) code to simultaneously have the local gap \(d+1,\ldots,d+t\) and a full-weight codeword, thereby violating the first mirror position under equality in the binary theorem's dimension hypothesis.

Targeted searches for the recent mirror-vanishing paper, q-ary mirror bands, the parameter family \([2d+1,2,d]_q\), dimension-two weight distributions, and projective-line multiplicity formulations did not locate this statement. Because the proof is short once the projective-line model is used, folklore or near-simultaneous priority risk remains material.

## Limitations

The theorem classifies only this extremal dimension-two family with \(n=2d+1\) and a full-weight violating codeword. It does not classify all q-ary codes that may satisfy or fail other possible mirror principles, nor does it identify additional hypotheses under which a q-ary mirror theorem could be restored. It is a structural counterexample and sharp boundary result, not a decoding or construction-efficiency result.

## References

1. X. He, “A Mirror Vanishing Band for Weight Distributions of Binary Linear Codes,” arXiv:2609.20344, 2026. https://arxiv.org/abs/2609.20344
2. S. Kurz et al., geometric point-of-view discussion for linear codes in “On strongly walk regular graphs, triple sum sets and their codes,” Designs, Codes and Cryptography, 2023. https://link.springer.com/article/10.1007/s10623-022-01118-z
3. A. Ashikhmin and A. Barg, “Minimal vectors in linear codes,” IEEE Transactions on Information Theory 44(5), 2010–2017, 1998.
