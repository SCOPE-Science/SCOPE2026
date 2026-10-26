# An exact odd-order stratum of the signed three-stamp problem

## Finding
For any integer \(h\ge1\), let \(hA\) be the set of sums of **exactly** \(h\) elements of an integer set \(A\), with repetition permitted. Define \(n_h^{\flat}(2)\) to be the largest \(N\ge0\) for which there exists a set \(A\) of exactly three distinct integers, containing at least one negative integer, with \([0,N]\subseteq hA\).

**Theorem.** For every even integer \(t\ge2\), put \(h=6t-3\). Then
\[
\boxed{n_h^{\flat}(2)=9t^2-3.}
\]
The sharp bound is attained by the explicitly given signed set
\[
A_t=\{-t,t,2t+1\}.
\]
Equivalently, for every integer \(k\ge0\) and \(h=12k+9\),
\[
\boxed{n_h^{\flat}(2)=\frac{h^2+6h+1}{4}-1.}
\]
The first nonnegative integer missing after the covered interval of this particular set is \(9t^2-2\).

## Assumptions and scope
The integers in the basis need not be positive, but the set must contain **three distinct elements** and at least one negative element. In a sum of order \(h\), exactly \(h\) summands are used, including repetitions. All interval endpoints are inclusive. The parameter \(t\) is even and at least \(2\), so \(h\) runs through \(9,21,33,45,\ldots\). Other residue classes of odd \(h\), and bases with four or more elements, are not classified.

## Proof
**1. Uniform upper bound from the prior strictness theorem.** Theorem 1.1 and Theorem 4.1 of van Doorn, Monticone and Nathanson (2026) establish for every odd \(h\ge3\)
\[
n_h^{\flat}(2)<n_h(2)=\frac{h^2+6h+1}{4}.
\]
For \(h=6t-3\), the classical extremum on the right is \(9t^2-2\). Since the signed extremum is an integer,
\[
n_h^{\flat}(2)\le9t^2-3.
\]
The remainder proves this sharp bound is attained and does not assume any other unpublished result.

**2. The progression decomposition.** Fix even \(t\ge2\) and put \(h=6t-3\). In a sum of exactly \(h\) elements of \(A_t\), let \(z\) be the number of copies of \(2t+1\), and \(r\) the number of copies of \(-t\). The other \(h-z-r\) copies are \(t\). Consequently
\[
(-t)r+t(h-z-r)+(2t+1)z=ht+(t+1)z-2tr,
\]
where \(z,r\) are integers with \(0\le z\le h\) and \(0\le r\le h-z\). For each fixed \(z\), this is the complete step-\(2t\) arithmetic progression from
\[
L(z)=-ht+(3t+1)z\quad\text{to}\quad U(z)=ht+(t+1)z.
\]
Because \(t\) is even, \(\gcd(t+1,2t)=1\). Thus, as \(z_0\) runs from \(0\) through \(2t-1\), the progressions for \(z=z_0\) represent each residue class modulo \(2t\) exactly once. The values \(z=z_0+2tj\), for integral \(j\), share that residue class.

**3. Initial coverage and the first two blocks.** Let \(z_0\in\{0,\ldots,2t-1\}\), set \(z_1=z_0+2t\), and note \(z_1\le4t-1\le h\). Because \(L(z)\) increases with \(z\),
\[
L(z_0)\le L(2t-1)=2t-1,\qquad U(z_0)\ge ht>0.
\]
It follows that the first progression covers the least nonnegative integer in its residue class and every later integer of the same residue up to \(U(z_0)\). Direct subtraction gives
\[
L(z+2t)-U(z)=2t(z+3t+1-h).
\]
For \(z=z_0\), the bound \(z_0\le2t-1\le3t-3=h-3t\) holds for every \(t\ge2\); hence \(L(z_1)\le U(z_0)+2t\). The first two progressions form one unbroken residue-class progression ending at
\[
U(z_1)=8t^2-t+(t+1)z_0.
\]

**4. Reaching the sharp endpoint.** There are two cases. If \(z_0\le t-3\), then \(z_2=z_0+4t\le h\) and the same subtraction, now with \(z=z_1\le3t-3\), shows \(L(z_2)\le U(z_1)+2t\). The joined progression reaches
\[
U(z_2)\ge ht+4t(t+1)=10t^2+t>9t^2-3.
\]
If instead \(z_0\ge t-2\), then already
\[
U(z_1)\ge8t^2-t+(t+1)(t-2)=9t^2-2t-2.
\]
The next integer of that residue class after \(U(z_1)\) is at least \(U(z_1)+2t\ge9t^2-2\), so no integer of the residue class below or equal to \(9t^2-3\) is missed. These cases cover every \(z_0\); since all residues occur, \([0,9t^2-3]\subseteq hA_t\).

For completeness, the missing endpoint is explicit: choose \(z_0=t-2\). Its second progression ends at \(U(z_1)=9t^2-2t-2\), while the next allowed progression in that residue starts at \(L(z_0+4t)=9t^2+2t-2\) (and might not even have an admissible \(z\) for small \(t\)). Thus \(9t^2-2\) is absent from \(hA_t\). Combining the construction with Step 1 proves the theorem. \(\square\)

## Verification
The supplied standalone script `verify.py` uses only exact standard-library integer arithmetic. It independently generates all sums for the construction at 30 even parameter values \(t=2,4,\ldots,60\), checking that the first missing nonnegative integer is exactly \(9t^2-2\). It separately enumerates every potential globally optimal three-element signed basis under the finite-candidate restrictions of the motivating paper for \(h=9,21,33\), and finds the claimed maxima and explicit extremizers. It prints `CERTIFICATE_OK`. These computations check small instances; the preceding progression argument proves the unbounded parameter range.

## Relationship to prior work
The paper by van Doorn, Monticone and Nathanson (arXiv:2610.19470v1, first posted 2026-10-14) gives the sharp ordinary three-stamp extremum and proves strict inequality for signed bases whenever \(h\) is odd (Theorems 1.1 and 4.1). It explicitly leaves the exact odd-order signed optimum open. The construction and exact infinite congruence class \(h\equiv9\pmod{12}\) above are not stated or implied by those upper-bound theorems. Nathanson's earlier 2026 paper (arXiv:2605.26425v1, Problem 5) motivates how negative elements affect coverage but does not determine these odd-order values. Other exact signed-stamp findings in a disjoint class \(h\equiv11\pmod{12}\) concern different parameters and do not imply this equality. Targeted literature searches did not identify prior covering results; implicit or uncatalogued equivalent work remains a risk.

## Limitations
This exact result only treats odd orders \(h\equiv9\pmod{12}\), with \(h\ge9\); it does not assert a formula for all odd orders. The unrestricted additive-h-basis problem for three stamps remains open in other strata. The verifier checks finitely many cases and is not a substitute for the proof. No independent external mathematical validation has been performed.

## References
1. W. van Doorn, P. Monticone and M. B. Nathanson, *Positivity and negativity for \(h\)-bases for \(n\)*, arXiv:2610.19470v1 (2026), particularly Theorems 1.1 and 4.1.
2. M. B. Nathanson, *Problems in additive number theory, VII: The structure of additive \(h\)-bases for \(n\)*, arXiv:2605.26425v1 (2026), Problem 5.
