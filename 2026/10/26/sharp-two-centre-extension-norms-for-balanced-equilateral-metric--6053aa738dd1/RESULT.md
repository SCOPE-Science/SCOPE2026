# Sharp two-centre extension norms for balanced equilateral metric frames

## Finding

Let \(m\geq2\) be an integer and let \(X=A\sqcup B\) be a metric space consisting of two labelled blocks of \(m\) vertices each, with distance \(1\) between any two distinct vertices of \(X\). Add distinct points \(p,q\) with distances as specified below, obtaining the metric space \(Y\). The least norm of a real-linear, constant-preserving Lipschitz extension operator from \(X\) to \(Y\) is

\[
\boxed{\Lambda_m(r,s,t)=\max\left\{1,\ \frac{2m-1}{m(r+s)},\ \frac{m-1}{mr},\ \frac{2m-1}{2mr+t}\right\}.}
\]

The same sharp factor works for Lipschitz extensions of **all** maps from \(X\) to an arbitrary real Banach space, where an extension may depend nonlinearly on the given map. Equivalently, it is the relative projection constant \(\lambda(\mathcal F(X),\mathcal F(Y))\) for the canonical inclusion of real Lipschitz-free spaces. A single explicit, positive, symmetry-equivariant linear operator attains all three minima.

The four entries in the maximum represent, respectively, the fixed-source constraint, one-centre mass balance, saturation of an entire near block, and the interaction between the two added points. In particular, the final term is a genuinely simultaneous obstruction, not a one-point bound.

**Illustration.** For \(m=2\), \(r=1/2\), \(s=3/4\), and \(t=1/4\), each single added point separately has sharp universal extension factor \(6/5\), but the simultaneous factor is \(4/3\). The interaction disappears once \(t\geq1/2\). More generally, when \(r=1/2\), \(s=3/4\), the interaction threshold equals \(m/4\) for \(m=2,3\) and \(m/[2(m-1)]\) for \(m\geq4\); the second static obstruction becomes dominant starting at \(m=4\).

## Assumptions and scope

All metrics and Banach spaces are real. Choose \(m\in\{2,3,\ldots\}\) and real parameters

\[
\frac12\leq r\leq s\leq r+1,\qquad
0<t,\qquad s-r\leq t\leq r+s.
\]

For all \(a\in A\), \(b\in B\), set

\[
 d(p,a)=d(q,b)=r,\qquad
 d(p,b)=d(q,a)=s,\qquad d(p,q)=t.
\]

All distinct source vertices have mutual distance \(1\). These inequalities on the parameters are **exactly** those that make \(Y\) a metric with the specified positive distances: source pairs in the near block require \(2r\geq1\); all source pairs require \(s-r\leq1\); the triangles containing both added points require \(s-r\leq t\leq r+s\). Equalities are permitted, except \(t=0\).

For a scalar map \(f\), its Lipschitz seminorm is \(\sup_{x\ne y}|f(x)-f(y)|/d(x,y)\). An extension operator is real-linear on the quotient by constant functions and is the identity on values at \(X\). The universal Banach-valued extension factor is the least \(C\geq1\) such that every real-Banach-valued Lipschitz map on \(X\) admits an extension to \(Y\) with seminorm at most \(C\) times that of the input.

## Proof

**1. Reduction without a sign or positivity assumption.** A scalar extension operator on \(\operatorname{Lip}(X)/\mathbb R\) can be represented at \(p\) and \(q\) by affine coefficient vectors on the source, whose entries sum to \(1\). This remains true for any operator with signed coefficients. Averaging an arbitrary operator over permutations of the vertices of \(A\), permutations of the vertices of \(B\), and the involution exchanging \(A\leftrightarrow B\) together with \(p\leftrightarrow q\), preserves extension identities and does not increase the Lipschitz operator norm. For the averaged operator, there are real numbers \(a,b\) with

\[
 ma+mb=1,\quad
 Tf(p)=a\sum_{A}f+b\sum_{B}f,\quad
 Tf(q)=b\sum_{A}f+a\sum_{B}f.
\]

No bound, sign, or positivity condition has been imposed on \(a,b\).

**2. Four unrestricted lower bounds.** Let \(C\) be the norm of this averaged operator. Because the source distance is \(1\), every source function taking only values \(0\) and \(1\) is \(1\)-Lipschitz. Fix \(a_0\in A\), \(b_0\in B\). Using a function equal to \(0\) at \(a_0\) and to \(1\) at every other source point, then the analogous function with its sole zero at \(b_0\), gives

\[
 rC\geq1-a,\qquad sC\geq1-b.
\]

Adding, and using \(a+b=1/m\), gives \(C\geq(2m-1)/[m(r+s)]\).

Instead use the source function equal to \(1\) on \(A\setminus\{a_0\}\) and \(0\) elsewhere. Its extension difference between \(p\) and \(a_0\) is \((m-1)a\), so \(rC\geq(m-1)a\). Combining this with \(rC\geq1-a\) yields \(C\geq(m-1)/(mr)\).

Finally, use the source indicator of \(A\). The extension difference between \(p\) and \(q\) is \(m(a-b)=2ma-1\), so \(tC\geq2ma-1\). Combining with \(a\geq1-rC\) yields

\[
 (2mr+t)C\geq2m-1.
\]

Also \(C\geq1\) because source distances are unchanged. These deductions hold for **all signed affine coefficients**; therefore the displayed four-term maximum is a lower bound for the norm of every scalar extension operator, whether equivariant or not.

**3. Matching positive operator for the complete parameter domain.** Write \(C_*\) for that maximum and define

\[
 a_*=\max\left\{\frac1{2m},\ 1-rC_*\right\},
 \qquad b_*=\frac1m-a_*.
\]

First \(C_*\geq(m-1)/(mr)\) implies \(a_*\leq1/m\). Consequently \(0\leq b_*\leq a_*\), and the coefficients at each new point are nonnegative and sum to one.

The remaining inequalities required by the metric are

\[
 1-a_*\leq rC_*,\qquad
 1-b_*\leq sC_*,\qquad
 m(a_*-b_*)\leq tC_*.
\]

The first is immediate by construction. To prove the second, note that \(a_*\leq sC_*-1+1/m\): for the branch \(a_*=1-rC_*\) this is exactly the bound \(C_*\geq(2m-1)/[m(r+s)]\); for the branch \(a_*=1/(2m)\), use the same bound and \(s\geq r\), which imply \(sC_*\geq1-1/(2m)\). To prove the third, note that \(a_*\leq(1+tC_*)/(2m)\): it is automatic for the branch \(a_*=1/(2m)\), while for \(a_*=1-rC_*\) it is equivalent to \(C_*\geq(2m-1)/(2mr+t)\).

Define, for every real Banach space \(E\), the extension of \(f:X\to E\) by

\[
 (Tf)(p)=a_*\sum_{A}f+b_*\sum_{B}f,
 \qquad (Tf)(q)=b_*\sum_{A}f+a_*\sum_{B}f.
\]

It is positive affine interpolation. For \(a_0\in A\), \(\|(Tf)(p)-f(a_0)\|\leq(1-a_*)\operatorname{Lip}(f)\), and for \(b_0\in B\) the corresponding bound is \((1-b_*)\operatorname{Lip}(f)\); analogous estimates hold at \(q\). For the new pair,

\[
 (Tf)(p)-(Tf)(q)
 =m(a_*-b_*)\left(\frac1m\sum_{A}f-\frac1m\sum_{B}f\right).
\]

The difference between the two averages is at most \(\operatorname{Lip}(f)\), since all cross-block source distances equal \(1\). Thus all new source and new-pair Lipschitz quotients are at most \(C_*\operatorname{Lip}(f)\). This yields the upper bound for every real Banach target.

**4. Universal lower bound and the projection formulation.** Equip \(X\) with a basepoint and let \(f(x)=\delta_X(x)\in\mathcal F(X)\) denote its canonical isometric embedding into the finite-dimensional real Lipschitz-free space. Any Banach-valued extension \(F:Y\to\mathcal F(X)\) of \(f\) with Lipschitz constant \(C\) linearizes, by the universal property, to a projection \(\mathcal F(Y)\to\mathcal F(X)\) of norm at most \(C\). Its adjoint gives a scalar linear Lipschitz extension of norm at most \(C\). Part 2 therefore forces \(C\geq C_*\), even if \(F\) is a nonlinear function of the input map. Conversely the positive formulas in part 3 extend every Banach-valued map with factor \(C_*\). Duality also shows that every scalar extension operator corresponds to a projection with the same norm. Hence all three constants equal \(C_*\).

**5. Phase structure.** The first two nontrivial terms compete according to the exact threshold \(s/r=m/(m-1)\): the mass-balance bound dominates for lower ratios, and near-block saturation dominates for higher ratios. The interaction term overtakes mass balance precisely when \(t<m(s-r)\), and overtakes the near-block term precisely when \(t<mr/(m-1)\). These inequalities describe the transitions when the baseline \(1\) is not already dominant; equalities give ties.

## Verification

The supplied standalone Python file `two_centre_certificate.py` uses only the standard library and exact `fractions.Fraction` arithmetic. It constructs the claimed optimal coefficients at admissible rational parameters, checks all source-to-new and new-to-new molecule norms, and enumerates every Boolean extreme source Lipschitz potential in the finite tested cases. It also rechecks the four analytical obstructions exactly at the selected optimum. Run `python3 two_centre_certificate.py` from the extracted package. The observed output was `PAIRED_CENTRE_CERTIFICATE_OK configurations=118 exact_potential_pair_checks=766160`.

An independent floating-point full-operator linear-programming comparison, which optimized signed coefficients after the mathematically justified block-symmetry reduction, matched the formula within numerical precision on 960 compatible parameter configurations with \(2\leq m\leq5\). This diagnostic is supplementary; the infinite-parameter proof is the algebraic argument above. The exact checker does not constitute an independent audit.

## Relationship to prior work

Basso's *Lipschitz extensions to finitely many points* (first made public 20 July 2017; arXiv:1707.06593) develops general upper bounds depending on the number of new points, rather than the precise relative projection norm of this two-centre, two-block construction. Basso's *Absolute Lipschitz extendability and linear projection constants* (arXiv:2104.14238, 2021), especially Theorem 1.2, equation (1.6), and Section 5, establishes a general bridge between Banach-valued Lipschitz extension and relative projection constants and discusses linear-programming methods; it does not give this four-term closed formula. Cúth and Doucha's *Projections in Lipschitz-free spaces induced by group actions* (arXiv:2104.11519, 2021), especially Theorem 4.5 and Corollary 4.6, studies complemented orbit-quotient free spaces, a different projection range; it does not compute the present relative projection constant.

The one-point equilateral radius-sorting formula recovers the first two nontrivial terms as the one-centre obstruction. It contains no inter-centre distance and cannot determine the last term. The example at the beginning exhibits a strict additional two-point cost. Related results on clustered-metric fluctuation projections and equilateral-metric facet enumeration concern different targets or invariants and do not imply this claim. No covering published formula was identified in the scoped searches; this is not a proof of uniqueness of the discovery.

## Limitations

The theorem concerns real Banach targets, a source of exactly \(2m\) equilateral vertices split into equal marked groups, exactly two added points with opposite two-level radius patterns, and the explicitly specified admissible metric domain. It does not classify unequal block sizes, arbitrary initial metrics, three or more added points, or nonlinear quasi-Banach targets. Full independence of originality and correctness has not been established; specialized or unindexed finite-metric projection calculations may exist. Finite verification is not a replacement for the all-parameter proof.

## References

1. G. Basso, *Lipschitz extensions to finitely many points*, arXiv:1707.06593 (first submission 2017-07-20), especially Theorem 1.1 and Section 4.
2. G. Basso, *Absolute Lipschitz extendability and linear projection constants*, arXiv:2104.14238 (first submission 2021-04-29), especially Theorem 1.2, equation (1.6), and Section 5.
3. M. Cúth and M. Doucha, *Projections in Lipschitz-free spaces induced by group actions*, arXiv:2104.11519 (first submission 2021-04-23), especially Theorem 4.5 and Corollary 4.6.
