# Sylvester-type arithmetic in the fixed-homology Seifert tower
## Finding
Let
\[
Y_0=M\!\left(0;b,\frac{a_1}{b_1},\ldots,\frac{a_n}{b_n}\right)
\]
be a stage of the homology-preserving Seifert-fibered iteration used by Boyer--Gordon--Hu--McCoy in the proof of their Theorem 1.13. Write
\[
H=|H_1(Y_0)|,\qquad P_0=\prod_{i=1}^n b_i.
\]
At stage \(k\), let \(P_k\) be the product of all exceptional-fiber orders then present, and apply the source operation by adjoining the Seifert coefficient
\[
-\frac{H^2}{P_kH+1}.
\]
Let \(d_{k+1}=P_kH+1\) be the new exceptional-fiber order and put \(Q_k=HP_k\). Then, for every \(k\ge0\),
\[
H_1(Y_k)\cong H_1(Y_0),\qquad Q_{k+1}=Q_k(Q_k+1),
\]
and
\[
d_{k+1}=1+Q_0\prod_{j=1}^{k}d_j.
\]
In particular, \(d_1,d_2,\ldots\) are pairwise coprime, every \(d_j\) is coprime to \(HP_0\), and
\[
d_{k+1}>Q_0^{2^k}.
\]
Thus the fixed-first-homology tower in the source has a forced Sylvester-type arithmetic: every newly introduced cone order is new modulo all previous ones, and the orders grow at least doubly exponentially in the number of iterations.

## Assumptions and scope
The statement concerns exactly the iterative Seifert-fibered operation printed in Boyer--Gordon--Hu--McCoy, Section 5, in which a rational homology sphere
\[
Y=M\!\left(0;b,\frac{a_1}{b_1},\ldots,\frac{a_n}{b_n}\right)
\]
with \(H=|H_1(Y)|\) is replaced by the manifold obtained by adjoining the coefficient
\[
-\frac{H^2}{(b_1\cdots b_n)H+1}.
\]
The source proves that this operation preserves the first homology group and explicitly iterates it in the proof of Theorem 1.13. The arithmetic conclusion here does not claim that every Seifert presentation with fixed first homology has this form; it is a structural statement about this particular source construction.

The fraction is already reduced: if a prime divides both \(H\) and \(P_kH+1\), it divides \(1\), hence
\[
\gcd(H^2,P_kH+1)=1.
\]
Therefore \(P_kH+1\) is indeed the new exceptional-fiber order.

## Proof
The source proves at each step that
\[
H_1(Y_{k+1})\cong H_1(Y_k).
\]
Induction therefore gives \(H_1(Y_k)\cong H_1(Y_0)\) for all \(k\), so the integer \(H\) remains fixed throughout the iteration.

By definition of the operation,
\[
d_{k+1}=P_kH+1=Q_k+1.
\]
Since adjoining this exceptional fiber multiplies the product of exceptional-fiber orders by \(d_{k+1}\),
\[
P_{k+1}=P_kd_{k+1}.
\]
Multiplying by \(H\) gives the exact recurrence
\[
Q_{k+1}=HP_{k+1}=HP_k(P_kH+1)=Q_k(Q_k+1).
\]
Iterating the product identity yields
\[
P_k=P_0\prod_{j=1}^{k}d_j,
\]
so
\[
Q_k=Q_0\prod_{j=1}^{k}d_j
\]
and hence
\[
d_{k+1}=Q_k+1=1+Q_0\prod_{j=1}^{k}d_j.
\]

Now fix \(1\le i<j\). At stage \(j-1\), the integer \(Q_{j-1}=HP_{j-1}\) is divisible by \(d_i\). Therefore
\[
d_j=Q_{j-1}+1\equiv1\pmod{d_i},
\]
which proves \(\gcd(d_i,d_j)=1\). The same argument with any divisor of \(Q_0=HP_0\) gives
\[
d_j\equiv1\pmod{q}
\]
for every prime \(q\mid Q_0\); thus \(\gcd(d_j,HP_0)=1\).

Finally,
\[
Q_{k+1}=Q_k^2+Q_k>Q_k^2.
\]
Induction gives \(Q_k\ge Q_0^{2^k}\), with strict inequality once \(k\ge1\). Since \(d_{k+1}=Q_k+1\),
\[
d_{k+1}>Q_0^{2^k}
\]
for every \(k\ge0\).

## Verification
The proof uses only the exact one-step formula and homology-preservation statement printed in the source. No finite experiment is used to infer an infinite claim. The critical checks are: the appended coefficient is reduced; the product \(P_k\) really gains the factor \(d_{k+1}\); the first homology order stays equal to \(H\); and every earlier \(d_i\) divides \(Q_{j-1}\) before \(d_j=Q_{j-1}+1\) is formed.

The growth statement is a lower bound, not an asymptotic equality. The result does not classify all Seifert towers with fixed first homology and does not strengthen the source's foliation-existence theorem itself.

## Relationship to prior work
Boyer--Gordon--Hu--McCoy introduce the homology-preserving surgery step and use it to obtain an infinite sequence of Seifert fibered rational homology spheres with prescribed first homology. Their text proves preservation of \(H_1\), persistence of the Euler-class obstruction, and eventual existence of co-orientable taut foliations, but it does not state the induced recurrence
\[
Q_{k+1}=Q_k(Q_k+1),
\]
the product formula for the successive exceptional orders, their pairwise coprimality, or the doubly-exponential lower bound.

The recurrence is reminiscent of classical Sylvester-type product-plus-one sequences. The point here is not novelty of the elementary number-theoretic identity in isolation, but its exact occurrence in this recent topological construction: it quantitatively describes how the singular-fiber data are forced to separate while the first homology group is held fixed.

Targeted searches in the published-findings index and the broader web literature found no statement attaching this recurrence and pairwise-coprime exceptional-order law to the Boyer--Gordon--Hu--McCoy tower. The closest returned records concerned unrelated fixed-homology or recurrence phenomena.

## Limitations
This is a structural refinement of one explicit construction, not a classification of Seifert manifolds with fixed first homology. The argument does not determine whether different choices outside the printed iteration can produce slower-growing exceptional orders. Pairwise coprimality is proved only for the newly introduced orders and their coprimality with the original product \(HP_0\); no assertion is made that the original exceptional orders \(b_i\) are pairwise coprime among themselves.

The source paper first appeared publicly as arXiv:2509.20135 on 2025-09-24; the exact iterative step used here is present in its later public version v3. The primary MSC classifications on the arXiv record are 57M25, 57M50, and 57M99.

## References
1. Steven Boyer, Cameron McA. Gordon, Ying Hu, and Duncan McCoy, *On 3-manifolds admitting co-orientable taut foliations, but none with vanishing Euler class*, arXiv:2509.20135v3. In Section 5, the proof of Theorem 1.13 gives the homology-preserving operation used here.
2. arXiv record for arXiv:2509.20135, submission history and MSC metadata; first public submission 2025-09-24.
