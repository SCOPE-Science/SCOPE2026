# An unbounded fractional-affordability gap for Pareto-efficient core committees

## Finding

For each integer \(k\geq1\), there is an approval election with exactly \(k+1\) candidates and \(k+1\) voters and a size-\(k\) committee \(W\) that is both Hare-core-stable and Pareto-efficient, but whose **exact maximum fractional affordability load**, under the core+ assignment relaxation of Becker, Greger and Peters [1], is
\[
\mathcal B(W)=\frac{k^2}{2(k+1)}.
\]
Consequently, this committee satisfies core+ exactly when \(k\leq2\), and for every \(k\geq3\) it fails core+ despite satisfying the ordinary core and Pareto efficiency. The load is unbounded and grows as \(k/2\) with an additive asymptotic correction of \(-1/2\). This is a quantitative separation for a restricted family, **not** a claim that ordinary core and core+ were previously known to coincide or that this is the first separation for unrestricted elections.

## Assumptions and scope

There are \(k\) incumbent candidates \(w_1,\ldots,w_k\) and one unelected challenger \(a\). The designated committee is \(W=\{w_1,\ldots,w_k\}\). For each \(1\leq i\leq k\), voter \(i\) approves exactly \(\{w_i,a\}\). One additional voter \(g\) approves exactly \(W\). Utilities are approval cardinalities \(u_i(T)=|A_i\cap T|\), candidate sets \(T\) are arbitrary subsets of the \(k+1\) candidates, and the Hare quota is \(q=(k+1)/k\).

Ordinary core means that there are no nonempty voter coalitions \(S\) and proposals \(T\) with \(|S|\geq q|T|\) and \(u_i(T)>u_i(W)\) for every member of \(S\). Pareto efficiency means no size-\(k\) committee weakly improves every voter's utility while strictly improving at least one.

For the core+ fractional relaxation [1, Section 3], take \(x_{ic},y_i,z_c\in[0,1]\), where \(x_{ic}\) exists only for approved voter-candidate pairs. The assignment constraints are
\[
\sum_{c\in A_i}x_{ic}=(u_i(W)+1)y_i,\qquad x_{ic}\leq z_c,\qquad x_{iw}\leq y_i\quad(w\in W\cap A_i).
\]
Write \(Y=\sum_i y_i\) and \(Z=\sum_c z_c\). For feasible assignments with \(Y>0\), the above equations imply \(Z>0\). Define their normalized affordability load \(\mathcal L=Y/(qZ)\), **before** imposing the core+ affordability inequality. Define \(\mathcal B(W)\) as the supremum of \(\mathcal L\) over these feasible assignments. By definition, \(W\) fails core+ precisely when a feasible assignment attains \(\mathcal L\geq1\). The value of \(\mathcal B(W)\) is finite and attained in this family.

## Proof

**1. Ordinary core.** Every incumbent-only guardian voter \(g\) already approves all \(k\) winners, so cannot be strictly improved by any candidate set. A blocking coalition therefore can contain only a subset \(S\) of the first \(k\) voters. Write \(|S|=s\geq1\). Each such voter has incumbent utility one and approves only \(w_i\) and \(a\). For strictly improved utility two, the proposal must contain \(a\) and every \(w_i\) with \(i\in S\). Thus \(|T|\geq s+1\), but the affordability condition would require
\[
s\geq q|T|\geq\frac{k+1}{k}(s+1)>s,
\]
a contradiction. Therefore \(W\) is Hare-core-stable for all \(k\geq1\).

**2. Pareto efficiency.** The guardian obtains utility \(k\) at \(W\), the maximum number of candidates this voter approves. Any size-\(k\) committee offering this guardian at least utility \(k\) must include all \(k\) incumbents, hence must equal \(W\). There is no weak Pareto improvement that is strict for anyone.

**3. Exact fractional upper bound.** For the guardian, the assignment identity is \(\sum_{j=1}^{k}x_{g,w_j}=(k+1)y_g\), while each winning assignment obeys \(x_{g,w_j}\leq y_g\). Hence \((k+1)y_g\leq ky_g\), which forces \(y_g=0\). For each ordinary voter, the assignment identity and candidate-weight bound give
\[
2y_i=x_{i,w_i}+x_{i,a}\leq z_{w_i}+z_a.
\]
Summing gives
\[
2Y\leq\sum_{i=1}^{k}z_{w_i}+kz_a\leq k\left(\sum_{i=1}^{k}z_{w_i}+z_a\right)=kZ.
\]
The last inequality holds for every integer \(k\geq1\) because all candidate weights are nonnegative. Consequently every fractional proposal has
\[
\mathcal L=\frac{Y}{qZ}\leq\frac{k}{2q}=\frac{k^2}{2(k+1)}.
\]

**4. Attainment and threshold.** Set \(z_a=1\) and \(z_{w_i}=0\) for all incumbents. Set \(y_i=1/2\) and \(x_{i,a}=1\) for each \(1\leq i\leq k\), with all other voter weights and assignment weights zero. These are within the interval \([0,1]\). The assignment identities hold because \(2y_i=1=x_{i,a}\); all winner-assignment bounds hold because winner assignments are zero. The resulting \(Y=k/2\), \(Z=1\) attain the upper bound. Core+ fails iff
\[
\frac{k}{2}\geq\frac{k+1}{k}\quad\Longleftrightarrow\quad k^2-2k-2\geq0.
\]
For positive integer \(k\), this holds exactly for \(k\geq3\). The smallest member of this **particular family** with separation has three seats, four voters and four candidates, and exact load \(9/8\). The identity
\[
\frac{k^2}{2(k+1)}=\frac{k-1}{2}+\frac{1}{2(k+1)}
\]
shows divergence with \(k\). These arguments prove every assertion.

## Verification

Execute `python verify.py` using a Python 3 standard-library environment. It exhaustively checks all voter-coalition/proposal pairs and all possible size-\(k\) committees for \(1\leq k\leq7\), totaling \(86{,}367\) integral pairs, and verifies the exact fractional witness with rational arithmetic for all \(1\leq k\leq100\). No finite computation is used to infer the infinite-size theorem; Steps 1–4 above are the proof for all positive integers. The program verifies the witness and integer examples independently of the displayed formula; the symbolic inequality in Step 3 is verified by direct mathematical reasoning, not an external certificate.

## Relationship to prior work

Becker, Greger and Peters [1] introduce core+ by relaxing integer coalition and assignment variables and prove that a core+ committee exists for every approval election. The present result concerns a **specified ordinary-core committee**, not existence, and gives an exact, unbounded numerical disparity between integral and fractional objections while retaining Pareto efficiency. Its proof uses precisely the assignment inequalities in [1, Section 3], not a different fractional-coalition model.

Brill and Peters' earlier two-voter core/EJR+ separation is recounted explicitly by Teh [2, Example 5.2]. Thus strict separation by itself, including a simpler two-voter case, is prior knowledge. The contribution claimed here is the exact size-dependent, unbounded affordability load in a Pareto-efficient incumbent-and-challenger family, and the three-seat transition **within this family**. Teh [2] concerns FJR+, EJR+ and the sub-core, with different fractional tests; it does not state this quantified core+ load. Peters [3] develops core-stability and approximate-core methodology without the newer core+ assignment formulation.

## Limitations

This is an exact classification of one natural approval-profile family, not a universal tight bound for all Pareto-efficient core committees. The fractional load is a ratio of the proposed coalition and candidate weights under the *particular* core+ assignment relaxation; it is not a claim about real coalitions actually improving, and it is not a ratio of voter welfare. The existing literature already establishes that core stability need not imply stronger representation axioms; this work does not reclaim that fact. An unrecognized general bound for related priceability or strengthened-representation relaxations might subsume the quantified construction; historical priority should be checked independently before publication.

## References

1. P. Becker, M. Greger, and D. Peters, *Existence of the Core in Approval-Based Committee Elections*, arXiv:2609.11912v1 (first public 2026-09-10), especially Sections 2–3, 6–8. https://arxiv.org/html/2609.11912v1
2. N. Teh, *Strengthening Full Justified Representation: Efficient Verification and Computation*, arXiv:2608.11500v1 (2026-08-11), especially Section 5.2 and Example 5.2. https://arxiv.org/html/2608.11500v1
3. D. Peters, *The Core of Approval-Based Committee Elections with Few Seats*, arXiv:2501.18304 (first public 2025-01-30), Sections 1–2. https://arxiv.org/abs/2501.18304
