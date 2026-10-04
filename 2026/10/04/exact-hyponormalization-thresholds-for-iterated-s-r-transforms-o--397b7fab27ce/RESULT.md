# Exact hyponormalization thresholds for iterated \(S_r\)-transforms of quaternionic weighted shifts
## Finding
Let \(w=(w_n)_{n\ge0}\) be a bounded sequence of positive real numbers and let \(T_w\) be the unilateral weighted shift on the right quaternionic Hilbert space \(\ell^2(\mathbb H)\),
\[
T_w e_n=e_{n+1}w_n.
\]
For any sequence \(r_0,r_1,\ldots>0\), define \(T^{(0)}=T_w\) and recursively
\[
T^{(k+1)}=S_{r_k}(T^{(k)}),\qquad S_r(A)=V|A|^rV
\]
when \(A=V|A|\) is the polar decomposition. Put \(R_0=1\) and \(R_k=\prod_{j=0}^{k-1}r_j\) for \(k\ge1\). Then, for every \(k,n\ge0\),
\[
T^{(k)}e_n=e_{n+2^k}w_{n+2^k-1}^{R_k}.
\]
For every \(p>0\), the iterate \(T^{(k)}\) is \(p\)-hyponormal if and only if
\[
w_m\le w_{m+2^k}\qquad\text{for every }m\ge2^k-1.
\]
Hence the set of indices \(k\) for which the iterate is \(p\)-hyponormal is independent of \(p\) and of the entire positive exponent schedule \((r_j)\). It is either empty or a tail \(\{k\ge q\}\). Every finite threshold \(q\in\mathbb N_0\) is realizable by a bounded positive weight sequence, and the empty case is realizable as well.

## Assumptions and scope
The weights are positive real scalars, so they are central in \(\mathbb H\); this removes left-right scalar-order issues and makes every iterate injective. No monotonicity is assumed. The transform is iterated with arbitrary positive exponents, not necessarily a constant exponent. The conclusion concerns \(p\)-hyponormality of these weighted shifts and does not assert subnormality or normality.

## Proof
Let \(Ue_n=e_{n+1}\). For \(T_w\), the polar decomposition is \(T_w=U|T_w|\) with \(|T_w|e_n=w_ne_n\). We prove the formula for \(T^{(k)}\) by induction. It is immediate for \(k=0\). Suppose
\[
T^{(k)}e_n=e_{n+d}w_{n+d-1}^{R_k},\qquad d=2^k.
\]
Because all displayed weights are positive, the polar partial isometry of \(T^{(k)}\) is \(U^d\), and
\[
|T^{(k)}|e_n=w_{n+d-1}^{R_k}e_n.
\]
Therefore
\[
S_{r_k}(T^{(k)})e_n
=U^d|T^{(k)}|^{r_k}U^de_n
=e_{n+2d}w_{n+2d-1}^{R_kr_k},
\]
which is the asserted formula at \(k+1\).

Now consider any positive \(d\)-step weighted shift \(We_n=e_{n+d}c_n\). Directly,
\[
W^*We_n=c_n^2e_n,
\]
while \(WW^*e_n=0\) for \(n<d\) and \(WW^*e_n=c_{n-d}^2e_n\) for \(n\ge d\). Hence, for any \(p>0\),
\[
(W^*W)^p\ge(WW^*)^p
\]
if and only if \(c_m\le c_{m+d}\) for every \(m\ge0\). Applying this with \(d=2^k\) and \(c_n=w_{n+d-1}^{R_k}\), and using \(R_k>0\), gives exactly
\[
w_m\le w_{m+2^k}\quad(m\ge2^k-1).
\]

If this condition holds for \(d=2^k\), then for every \(m\ge2d-1\),
\[
w_m\le w_{m+d}\le w_{m+2d},
\]
so it holds for \(2d=2^{k+1}\). Thus the successful iteration indices form a tail whenever nonempty.

To realize threshold \(q=0\), take any bounded positive nondecreasing sequence, for example \(w_n=2-(n+1)^{-1}\). For \(q\ge1\), put \(d=2^{q-1}\), take \(w_{d-1}=2\), and take \(w_n=1\) for every \(n\ne d-1\). The criterion fails at level \(q-1\) using \(m=d-1\), but it holds at level \(q\) because every weight with index at least \(2d-1\) equals \(1\). The tail implication then shows that \(q\) is the first successful level. Finally, \(w_n=1+(n+1)^{-1}\) is strictly decreasing, so the criterion fails at every level and the successful set is empty.

## Verification
The proof is symbolic. The induction checks the polar decomposition at every iterate, including the index shift \(2^k-1\) and exponent product \(R_k\). The \(p\)-hyponormal criterion was recomputed from the two diagonal operators \(W^*W\) and \(WW^*\), so no finite experiment is used to infer the infinite statement. The realizability examples were checked directly against the same criterion.

## Relationship to prior work
Fashandi's 2026 paper introduces the quaternionic application considered here and, for one transform, computes
\[
S_r(T_w)e_n=e_{n+2}w_{n+1}^r
\]
for a positive real weighted shift; its Example 13 uses an increasing sequence to obtain hyponormality for every \(r>0\). The paper contains no iterated-transform statement. The original complex transform paper of Patel, Tanahashi and Uchiyama treats \(S(T)=U|T|^{1/2}U\), proves one-step hyponormality results, and includes weighted-shift examples, but the inspected text does not give the dyadic iterate formula or classify the first hyponormal iterate. The present result turns the one-step computation into an exact dynamical classification for arbitrary positive exponent schedules.

## Limitations
The classification is for unilateral shifts with strictly positive real weights on \(\ell^2(\mathbb H)\). It does not address quaternion-valued noncentral weights, zeros in the weight sequence, bilateral shifts, or general operators. The closest older transform literature is substantial; although targeted searches and the inspected primary texts did not reveal this exact iterate-threshold theorem, an equivalent observation under different terminology remains a residual originality risk.

## References
1. M. Fashandi, *A Quaternionic Hansen--Pedersen Inequality and its Application to \(S_r\)-Transforms*, arXiv:2609.32623v1, 2026.
2. S. M. Patel, K. Tanahashi, A. Uchiyama, *A Note on an Operator Transform \(S(T)\)*, Scientiae Mathematicae Japonicae Online, 2005, 433--447.
3. S. Menkad, S. Zid, *Some relationships between an operator and its transform \(S_r(T)\)*, Advances in Operator Theory 9 (2024), article 18, DOI 10.1007/s43036-024-00317-w.
