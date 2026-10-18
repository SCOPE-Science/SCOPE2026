# A universal even-parity bias in random parking outcomes

## Finding

For every integer \(n\geq1\), choose a classical parking function uniformly from the \((n+1)^{n-1}\) preference lists of length \(n\), and let \(\Pi_n\) be the permutation recording the final car labels from left to right. Define the integer signed imbalance
\[
D_n=\#\{\text{preferences with even }\Pi_n\}-\#\{\text{preferences with odd }\Pi_n\}.
\]
Then **\(D_n>0\) for every \(n\geq1\)**. Equivalently,
\[
\boxed{\Pr(\Pi_n\text{ even})=\frac12+\frac{D_n}{2(n+1)^{n-1}}>\frac12.}
\]

The following exact recurrence computes the imbalance without enumerating parking functions or permutations. Put \(D_0=1\). For integers \(m\geq0\) and \(0\leq k\leq m\), set
\[
G_{m,k}=\begin{cases}
0,&m\text{ even and }k\text{ odd},\\
\binom{\lfloor m/2\rfloor}{\lfloor k/2\rfloor},&\text{otherwise}.
\end{cases}
\]
For every \(n\geq1\),
\[
\boxed{D_n=\sum_{k=0}^{n-1}(k+1)(-1)^{n-1-k}G_{n-1,k}D_kD_{n-1-k}.}
\]
This is an \(O(n^2)\)-arithmetic recurrence for the sequence up to any chosen size (with precomputed binomial coefficients).

More structurally, the formal exponential series
\[
E(z)=\sum_{m\geq0}\frac{D_{2m}}{m!}z^m,\qquad
O(z)=\sum_{m\geq0}\frac{D_{2m+1}}{m!}z^m
\]
satisfy
\[
\boxed{O(z)=\frac{d}{dz}\bigl(zE(z)^2\bigr),\qquad
E'(z)=E(z)^3+8zE(z)^2E'(z)+4z^2E(z)^2E''(z).}
\]
The second identity has a **coefficientwise-positive** inductive interpretation, proving the strict parity inequality at every size without relying on numerical experiments.

The first signed imbalances are \(D_1=1\), \(D_2=1\), \(D_3=4\), \(D_4=11\), \(D_5=72\), \(D_6=335\), \(D_7=2944\), and \(D_8=19449\). In particular, \(\Pr(\Pi_4\text{ even})=68/125\) and \(\Pr(\Pi_5\text{ even})=19/36\).

## Assumptions and scope

There are \(n\) cars labeled \(1,\ldots,n\) arriving in increasing order and \(n\) parking places labeled \(1,\ldots,n\) from left to right. Car \(i\) has preference \(a_i\in\{1,\ldots,n\}\), parks in the least vacant place greater than or equal to \(a_i\), and fails if none exists. A parking function is a preference vector \((a_1,\ldots,a_n)\) for which no car fails; all such vectors are equally likely. The permutation \(\Pi_n(j)\) is the label of the car parked in place \(j\). Its sign equals the sign of the inverse permutation listing the positions occupied by cars in arrival order. The empty case \(D_0=1\) is a recurrence convention. The power series are **formal**; no analytic radius of convergence or asymptotic parity-rate claim is asserted.

## Proof

**1. Split at the final vacancy.** Just before car \(n\) arrives there is exactly one vacant place, say \(k+1\), with \(k\) filled places on the left and \(r=n-1-k\) on the right. No earlier car can cross the vacant place: an attempt from the left would park there first. Thus, after extracting the subsequences of car labels assigned to the two sides, their preferences (translated on the right) are independent classical parking functions of sizes \(k\) and \(r\). Conversely, any such two lists and any order-preserving interleaving of their arrival subsequences yields a valid partial parking trajectory leaving the designated place vacant.

The last car can park in place \(k+1\) with exactly \(k+1\) preferences, namely the places from \(1\) through \(k+1\). Relative order within each side contributes signed weights \(D_k\) and \(D_r\). The last car contributes \(r\) inversions against the cars occupying places to its right. A right-side car appearing earlier than a left-side car contributes one further inversion. Therefore the total signed weight for the selected vacancy is
\[
(k+1)(-1)^rD_kD_r\,G_{n-1,k},
\]
where \(G_{m,k}\) is the signed sum over all binary interleavings of \(k\) left and \(m-k\) right entries, with sign \((-1)^{\#\text{ right-before-left pairs}}\).

**2. Evaluate the signed shuffle.** Pair successive positions of a binary interleaving: \((1,2),(3,4),\ldots\). If some pair has different labels, swap the entries of its **first** mixed pair. This is a fixed-point-free involution, and it changes the inversion parity by exactly one. Hence only interleavings constant on each pair survive. When \(m=2h\), they exist precisely for even \(k=2j\) and number \(\binom hj\). When \(m=2h+1\), the last unpaired position is determined by the parity of \(k\), and the number is \(\binom h{\lfloor k/2\rfloor}\). The remaining interleavings all have even inversion parity because inversions between doubletons occur in multiples of four (and any pair involving the trailing singleton contributes an even number). This proves the displayed formula for \(G_{m,k}\), and summing the vacancy contributions proves the recurrence for \(D_n\).

**3. Separate parity in the recurrence.** Write \(A_m=D_{2m}\) and \(B_m=D_{2m+1}\). For odd size, only even values of \(k\) survive, giving
\[
B_m=\sum_{j=0}^{m}(2j+1)\binom mj A_jA_{m-j}.
\]
For even size,
\[
A_{m+1}=\sum_{j=0}^{m}\binom mj\left((2j+2)B_jA_{m-j}-(2j+1)A_jB_{m-j}\right).
\]
Taking formal exponential generating series turns these into
\[
O=E^2+2zEE',\qquad E'=EO+2z(EO'-E'O).
\]
Substituting the first equation into the second yields the two boxed formal differential identities.

**4. Prove strict positivity for all sizes.** Write \(E(z)=\sum_{m\geq0}c_mz^m\), where \(c_m=D_{2m}/m!\). The initial coefficient is \(c_0=1\). In the coefficient of \(z^m\) in
\[
E'=E^3+8zE^2E'+4z^2E^2E'',
\]
the left side is \((m+1)c_{m+1}\), while every term on the right uses only \(c_0,\ldots,c_m\), with nonnegative numerical multipliers. If these coefficients are positive, then the coefficient from \(E^3\) alone is strictly positive. Induction gives \(c_m>0\) for all \(m\), hence \(A_m>0\). Finally, \(O=(zE^2)'\) has strictly positive coefficients, so \(B_m>0\) for all \(m\). This proves \(D_n>0\) for every \(n\geq0\). The previously established classical count \((n+1)^{n-1}\) then gives the stated even-parity probability.

## Verification

Run `python3 verify.py` in a directory containing the provided standalone script; no packages beyond Python's standard library are required. The script compares (i) direct binary-interleaving sign sums with the closed signed-shuffle coefficient, (ii) the signed last-vacancy recurrence with the formal differential recurrence through \(n=24\), (iii) an independent occupied-subset dynamic program through \(n=13\), and (iv) direct exhaustive preference-list parking simulations through \(n=6\). The observed run completed 131 assertions successfully. Computations support the derivation but are not invoked to prove its validity for all \(n\).

## Relationship to prior work

Pinsky [1] gives the **complete** probability mass function on induced outcome permutations, including the multiplicity of every particular permutation. Thus the parity probability was already determined implicitly as a factorial-size signed sum of his weights. The contribution here is not the individual-permutation law: it is the universal strict **sign inequality**, the exact polynomial-arithmetic recurrence, and its positive formal differential mechanism. In particular, a complete mass function does not itself display or prove a signed cancellation inequality without further argument.

Stanley and Yin [2] study several joint parking-function statistics, including descents of the inverse outcome, not the sign of that permutation. Celano and collaborators [3] develop inversion generating functions of the **preference word**, which is a different statistic: at size four the signed preference-word count is \(5\), while the signed outcome count in this result is \(11\). These are not equated here. The possibility of a previously published equivalent sign-reversing involution or formal differential identity remains a historical-priority risk.

## Limitations

No explicit elementary closed form for \(D_n\), sharp large-size decay rate of the normalized parity bias, limit law for inversions, or independent historical-priority certification is asserted. The last-vacancy recurrence and formal differential identities determine exact values and show strict positivity, but their scope is limited to ordinary one-way classical parking with all preference lists equally likely. The conclusion need not hold for different parking protocols, car arrival orders conditioned on preferences, or other weighted parking laws.

## References

[1] R. G. Pinsky, *The distribution on permutations induced by a random parking function*, arXiv:2404.11529, first posted 2024-04-17. https://arxiv.org/abs/2404.11529

[2] R. P. Stanley and M. Yin, *Some enumerative properties of parking functions*, arXiv:2306.08681, first posted 2023-06-14. https://arxiv.org/abs/2306.08681

[3] K. Celano, J. Elder, K. P. Hadaway, P. E. Harris, A. Priestley, and G. Udell, *Inversions in parking functions*, arXiv:2508.11587, first posted 2025-08-15. https://arxiv.org/abs/2508.11587
