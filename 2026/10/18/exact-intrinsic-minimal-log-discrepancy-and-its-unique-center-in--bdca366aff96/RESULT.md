# Exact intrinsic minimal log discrepancy and its unique center in a sharp-volume toric family

## Finding

For every integer \(n\ge2\) and \(h\ge3\), define integers
\[
u_1=h,\qquad u_{j+1}=u_j(1+u_j),\qquad q_j=1+u_j,\qquad L=\prod_{j=1}^nq_j,
\]
and \(a_j=L/q_j\). Let \(X_{n,h}=\mathbb P(1,a_1,\ldots,a_n)\) over \(\mathbb C\), as in Bie–Du–Yu's sharp anticanonical-volume construction. Write \(S\) for the coordinate divisor of weight one and \(p_1=[0:1:0:\cdots:0]\) for the point corresponding to its largest nonunit weight \(a_1\).

The **intrinsic** (boundary-free) global minimal log discrepancy is exactly
\[
\boxed{\operatorname{mld}(X_{n,h},0)=\frac1h+\frac{h-1}{h a_1}},
\qquad a_1=\prod_{j=2}^n(1+u_j).
\]
Every divisorial valuation realizing the global minimum is centered at \(p_1\), and at least one such valuation exists. Thus \(p_1\) is the unique center where the global minimum is realized; this does not assert uniqueness of the valuation. In contrast, the marked pair \((X_{n,h},(1-1/h)S)\) has minimal log discrepancy \(1/h\), as established in prior work.

As an intrinsic normalization of the sharpness construction, for fixed \(n\ge2\),
\[
\lim_{h\to\infty}\operatorname{vol}(-K_{X_{n,h}})\,\operatorname{mld}(X_{n,h},0)^{\,2^n-n-1}=1.
\]

## Assumptions and scope

All varieties are over \(\mathbb C\). The integer quantifiers are \(n\ge2\) and \(h\ge3\). The global minimal log discrepancy means the infimum of log discrepancies of divisorial valuations over the entire variety, including invariant divisors on the variety. The chosen weights define a well-formed \(\mathbb Q\)-factorial weighted projective variety: the \(q_j\) are pairwise coprime; the \(a_j\) are integers and strictly decrease; and \(\gcd(a_1,\ldots,a_n)=1\). The parameter \(h\) is integral, and the asserted exact formula is not a claim about arbitrary Fano varieties.

## Proof

**1. Elementary weights and Cartier control.** The recurrence yields pairwise coprime \(q_j\), and the telescoping identity \(\sum_j1/q_j=1/h-1/u_{n+1}\). Because \(u_{n+1}=hL\), for \(Q=1+\sum_ja_j\) we obtain
\[
hQ=L+h-1.
\]
The divisor \(S\) is the weight-one coordinate divisor, so \(K_X\sim-QS\) as a Weil divisor class. Put \(B=(1-1/h)S\). Hence
\[
h(K_X+B)\sim-LS.
\]
The divisor \(LS\) is Cartier because each weight divides \(L\). Each toric ray discrepancy of the pair \((X,B)\) is positive (equal to \(1/h\) for \(S\) and to \(1\) for the other invariant prime divisors). The positive piecewise-linear toric discrepancy function shows the pair is klt on a toric log resolution, hence klt. Every divisorial log discrepancy of the pair belongs to \((1/h)\mathbb Z\), since \(h(K_X+B)\) is Cartier. Thus, for every divisorial valuation \(v\),
\[
A_{X,B}(v)\ge1/h.
\]
This reconstructs, using the toric discrepancy function, the lower bound needed from the marked construction; it does not assume a claimed result about the unmarked variety.

**2. Lower bound for every center.** For any divisorial valuation \(v\),
\[
A_X(v)=A_{X,B}(v)+(1-1/h)v(S).
\]
On the affine chart \(U_j=\{x_j\ne0\}\) for \(1\le j\le n\), the rational function \(x_0^{a_j}/x_j\) has principal divisor \(a_jS\); hence \(a_jS\) is Cartier on \(U_j\). If the center of \(v\) lies in \(S\cap U_j\), then \(v(S)>0\) and \(a_jv(S)\) is a positive integer, giving \(v(S)\ge1/a_j\). Since \(a_1>a_2>\cdots>a_n\), every valuation centered on \(S\) satisfies
\[
A_X(v)\ge1/h+(h-1)/(h a_1).
\]
If its center lies outside \(S\), the chart \(x_0\ne0\) identifies \(X\setminus S\) with the smooth affine space \(\mathbb A^n\); every divisorial log discrepancy there is at least \(1\), strictly above the proposed bound because \(a_1>1\).

**3. Matching valuation.** The weighted affine chart \(U_1\) at \(p_1\) is the cyclic quotient of \(\mathbb A^n\) by \(\mu_{a_1}\) with weights \((1,a_2,\ldots,a_n)\). Since \(0<a_j<a_1\) for \(j\ge2\), the generator defines a primitive interior toric lattice vector
\[
\frac1{a_1}(1,a_2,\ldots,a_n),
\]
whose divisorial log discrepancy for the boundary-free quotient equals its coordinate sum,
\[
A_X(v_1)=\frac{1+\sum_{j=2}^na_j}{a_1}=\frac{Q-a_1}{a_1}
=\frac1h+\frac{h-1}{ha_1}.
\]
It realizes the lower bound. Here \(\mu_{a_1}\) acts faithfully because one weight is one, and the toric vector is primitive for the same reason.

**4. Center uniqueness.** If the center of a valuation attaining this value lies in \(S\) and also in some \(U_j\) with \(j\ge2\), then the strict inequality \(a_j<a_1\) gives the strictly stronger lower bound \(1/h+(h-1)/(ha_j)\), a contradiction. Centers outside \(S\) were excluded above. The only remaining point is \(p_1\), which is already a center of the constructed toric valuation.

**5. Volume normalization.** The originating paper proves \(\operatorname{vol}(-K_{X_{n,h}})\sim h^{2^n-n-1}\) for fixed \(n\) as \(h\to\infty\). Since \(a_1\to\infty\), the proved exact formula gives \(h\operatorname{mld}(X_{n,h},0)=1+(h-1)/a_1\to1\), proving the displayed limit. This final asymptotic uses the previously established volume statement rather than a new volume estimate.

## Verification

The accompanying standalone `verify.py` computes the weights with exact integers, verifies the telescoping/weight identities, and enumerates the cyclic-quotient age spectra on every coordinate chart for the cases \(n=2\), \(3\le h\le17\), and \(n=3\), \(3\le h\le7\). All tested minima equal the formula and occur on the largest-weight chart at group element one. The verifier reports `VERIFY_OK` when successful. These finite tests are corroboration only: the unrestricted quantifiers follow from the proof above.

## Relationship to prior work

Bie, Du, and Yu (2026, arXiv:2610.10537v1, Proposition 9.1) construct these weighted projective Fano varieties and prove the marked pair is \(1/h\)-log canonical, giving an unmarked \(1/h\)-lower bound and the sharp anticanonical-volume asymptotic. They do **not** give the exact unmarked global minimal log discrepancy or identify its unique minimizing center. Ambro (2014, arXiv:1411.2770v1, Example 5.3) gives the underlying recursive toric construction and the marked-pair minimal log discrepancy; his Section 5 supplies general toric minimum formulas, which are acknowledged as foundational tools. The new statement is the exact boundary-free singularity threshold and its locus, extracted uniformly across both parameters.

## Limitations

The exact formula concerns the global divisorial minimal log discrepancy, not local log discrepancies at every point, a classification of all valuations achieving the minimum, or all \(\epsilon\)-lc Fano varieties. The proof uses basic toric quotient descriptions and the toric klt criterion. The originating papers supply the construction and volume asymptotic, so those parts are not claimed as new. An unindexed or implicit earlier computation of the same unmarked minimum remains a literature risk.

## References

1. P. Bie, P. Du, Z. Yu, *Sharp polynomial upper bounds for anticanonical volumes*, arXiv:2610.10537v1 (first posted 7 October 2026), Proposition 9.1 and Section 9.
2. F. Ambro, *Variation of log canonical thresholds in linear systems*, arXiv:1411.2770v1 (2014), Section 5, especially Example 5.3 and toric minimal log-discrepancy formulas.
3. Standard toric cyclic quotient age formula and discrepancy description, as recalled in Ambro (2014), Section 5.
