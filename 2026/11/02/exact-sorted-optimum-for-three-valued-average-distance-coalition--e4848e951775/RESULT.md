# Exact sorted optimum for three-valued average-distance coalitions

## Finding

Let \(x<y<z\) be real-valued types represented by \(a,b,c\ge1\) agents respectively. Partition all \(n=a+b+c\) agents into **at most two nonempty coalitions**. The cost of a member of a coalition \(S\) of size at least two is the mean absolute type difference to the other members of \(S\), and a singleton has cost zero (happy in isolation). Social cost is the sum of individual costs. Set \(u=y-x>0\) and \(v=z-y>0\). Then the exact minimum social cost is

\[
\boxed{\operatorname{OPT}_2(a,b,c;u,v)=\min\left\{\frac{2ab}{a+b-1}u,\ \frac{2bc}{b+c-1}v\right\}.}
\]

The minimum is attained by a **sorted** partition placing either all \(a+b\) agents of types \(x,y\) opposite the \(c\) agents of type \(z\), or the \(a\) agents of type \(x\) opposite all \(b+c\) agents of types \(y,z\). This remains true with arbitrarily many repeated agents at each type. Ties between these two partitions occur exactly when the two displayed quantities are equal. No uniqueness claim for all optimum partitions is made.

## Assumptions and scope

There are exactly three distinct real-valued types with positive integer multiplicities \(a,b,c\); agents are distinguishable, but only their types enter cost. Either one or two nonempty coalitions may be formed. For \(|S|\ge2\),

\[
\operatorname{SC}(S)=\frac{2}{|S|-1}\sum_{\{i,j\}\subseteq S}|v_i-v_j|,
\qquad \operatorname{SC}(\{i\})=0.
\]

The singleton rule is the happy-in-isolation convention; no statement is made here for singleton-prohibiting conventions or fixed coalition cardinalities. In particular, the two groups are not required to have prescribed sizes. The conclusion is not asserted for four or more distinct types.

## Proof

Write \(A=a b/(a+b-1)\), \(B=b c/(b+c-1)\), and introduce strictly positive weights

\[
w_1=\frac1A=\frac{a+b-1}{ab},\qquad
w_2=\frac1B=\frac{b+c-1}{bc}.
\]

For a coalition having \(p\) low, \(q\) middle, and \(r\) high agents, its contribution to one half of social cost is

\[
F(p,q,r;u,v)=\frac{p(q+r)u+r(p+q)v}{p+q+r-1}
\]

when its cardinality is at least two, and zero when its cardinality is one. The two candidate sorted partitions have costs \(2Au\) and \(2Bv\), respectively. To establish optimality, it suffices to show, for every admissible partition, that the sum \(X\) of coefficients of \(u\) in the half-cost and the sum \(Y\) of coefficients of \(v\) satisfy

\[
\boxed{w_1X+w_2Y\ge1.}\tag{1}
\]

Indeed, \(uX+vY=(w_1X)(Au)+(w_2Y)(Bv)\ge\min\{Au,Bv\}\), since both weights are nonnegative and their sum is at least one. Multiplying by two gives the required lower bound.

We first treat partitions into two groups of cardinalities \(m\) and \(n-m\), both at least two. Let the first group contain \((p,q,r)\) agents of the three types, with \(p+q+r=m\), and the second the complementary counts. Relax \(p,q,r\) to the real box \([0,a]\times[0,b]\times[0,c]\) intersected with the plane \(p+q+r=m\). In terms of \(d_1=p\) and \(d_2=p+q\), the left side of (1), apart from a positive constant factor, is

\[
\frac{w_1}{2}\alpha_a(d_1)+\frac{w_2}{2}\alpha_{a+b}(d_2),
\]

where, for \(i\in\{a,a+b\}\),

\[
\alpha_i(d)=\frac{2d(m-d)}{m-1}+
\frac{2(i-d)(n-m-i+d)}{n-m-1}.
\]

Each \(\alpha_i\) is a concave quadratic in \(d\), so their positive weighted sum is concave on the feasible polygon. Its minimum therefore occurs at a vertex. Every vertex of this two-dimensional box slice has at least two of \(p,q,r\) at a boundary (zero or its full type multiplicity). Thus it is enough to verify (1) for allocations in which **at most one type is split** between the coalitions. The resulting vertex inequality also applies to every integer allocation because the relaxed feasible set contains it.

For this check, set \(h_d(t)=dt/(d+t-1)\) when the denominator is positive, and \(h_1(0)=0\). For every integer \(d\ge1\), the function \(h_d\) is nonnegative and concave on \([0,\infty)\): when \(d>1\) this follows by differentiation, and when \(d=1\) the function equals zero at zero and one at every positive argument. We also need the elementary inequality

\[
\frac{ac(w_1+w_2)}{a+c-1}\ge1,\tag{2}
\]

because the numerator minus the denominator, after multiplication out, is

\[
ac(w_1+w_2)-(a+c-1)=1+\frac{2ac-a-c}{b}\ge1.
\]

Here \(2ac-a-c\ge0\) for all positive integers \(a,c\).

**Middle type split.** If all low types lie in the first group and all high types in the second, let \(t\in[0,b]\) middle agents join the low group. Then the left side of (1) equals

\[
w_1h_a(t)+w_2h_c(b-t).
\]

This expression is concave in \(t\). At each endpoint it equals one; hence it is at least one throughout. If the low and high types instead lie in the *same* group and \(t\) middle agents join them, the other group is homogeneous and the expression is

\[
\frac{a(t+c)w_1+c(a+t)w_2}{a+c+t-1}.
\]

Its numerator minus its denominator equals

\[
\bigl(ac(w_1+w_2)-a-c+1\bigr)+t(aw_1+cw_2-1)\ge0,
\]

by (2) and \(aw_1\ge1\), \(cw_2\ge1\).

**Low type split.** By interchanging coalition names, there are only two placements of the unsplit middle and high types. If middle and high lie together, let \(t\in[0,a]\) low agents join them while the other low agents form a homogeneous group. The left side of (1) is

\[
\frac{t(b+c)w_1+c(t+b)w_2}{t+b+c-1}\ge1.
\]

Subtracting the denominator from the numerator gives \(t((b+c)w_1+cw_2-1)\ge0\), using \(cw_2\ge1\). If middle and high lie in different groups, let \(t\) low agents join middle and \(a-t\) join high. The expression becomes

\[
w_1h_b(t)+(w_1+w_2)h_c(a-t).
\]

It is concave in \(t\in[0,a]\), and its endpoint values are one and \(ac(w_1+w_2)/(a+c-1)\ge1\). Thus (1) holds. The **high-type-split** cases follow by reflecting the type order and exchanging \((a,w_1,u)\) with \((c,w_2,v)\).

If a group is a singleton, its type is necessarily homogeneous. The complementary group falls into one of the unsplit-type cases above, whose inequalities did not assume the complementary homogeneous group had size at least two. Therefore (1) also holds for all partitions with a singleton (where its own cost is defined to be zero).

Finally, for the grand coalition, its normalized half-cost is

\[
\frac{a(b+c)w_1+c(a+b)w_2}{a+b+c-1}.
\]

This is the preceding middle-type-together expression at \(t=b\); it too is at least one. Thus no partition into at most two coalitions can beat either sorted split. Both sorted splits are feasible, completing the proof.

## Verification

The accompanying `check.py` independently evaluates exact rational pair-distance coefficients for every allocation of the three type multiplicities \(1\le a,b,c\le7\), including singleton groups. It checks inequality (1), the closed formula for five positive gap pairs, and the grand-coalition bound. The completed package was extracted and the program run successfully, producing

`VERIFY_OK exact_count_profiles=343 exact_two_group_partitions=42189 gap_pairs=5 singleton_allowed=True`

The computational domain is finite; the preceding symbolic concavity and endpoint proof, not the enumeration, establishes the result for all positive integer multiplicities and all real type gaps.

## Relationship to prior work

Merlin de la Haye, Pascal Lenzner, Farehe Soheil, and Marcus Wunderlich, *Metric Hedonic Games on the Line*, arXiv:2602.05888 (first public version February 5, 2026; revision February 16, 2026), introduce this average-cost hedonic model and pose Conjecture 3.11: with two freely sized coalitions, a social optimum is sorted. Their Appendix C (Equation 12) gives the concave coefficient decomposition used in the proof above and establishes several partial structural properties; the present statement supplies an explicit optimum formula for the distinct three-type subfamily. Their nine-agent unsorted optimum concerns fixed coalition sizes (the swap model), so it does not imply a counterexample for freely chosen coalition sizes. Their cut-off and maximum-cost models are also distinct.

Classical one-dimensional clustering results for unnormalized sum-of-pair distances and centroid-based quadratic objectives do not directly imply a claim for the per-coalition factor \(1/(|S|-1)\), whose dependence on each chosen coalition's size is critical here.

## Limitations

The theorem does not establish the general sorted-optimum conjecture for four or more distinct types. Its formula allows singleton coalitions at zero cost; if singleton groups are forbidden or have infinite cost, the feasible set changes. Neither a uniqueness classification of optimizers nor a classification under externally prescribed coalition sizes is claimed. An equivalent unindexed prior theorem about normalized pairwise-distance clustering cannot be ruled out solely by literature searches. Independent review remains outstanding.

## References

1. M. de la Haye, P. Lenzner, F. Soheil, M. Wunderlich, *Metric Hedonic Games on the Line*, arXiv:2602.05888, v1 February 5, 2026, v2 February 16, 2026. https://arxiv.org/abs/2602.05888 ; full text https://arxiv.org/html/2602.05888v2 . Relevant material: Definition of Average and HIS, Section 3.2 and Conjecture 3.11, Appendix C Equations 11–12 and Lemma 2.4 comparison.
2. Y. Bartal, M. Charikar, D. Raz, *Approximating min-sum k-clustering in metric spaces*, STOC 2001, DOI:10.1145/380752.380754 (unnormalized min-sum clustering, a different objective).
