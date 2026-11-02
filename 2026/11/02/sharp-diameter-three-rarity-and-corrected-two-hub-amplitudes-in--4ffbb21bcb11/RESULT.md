# Sharp diameter-three rarity and corrected two-hub amplitudes in isotropic redirection trees

## Finding
Start from one edge, and when the tree has \(n\) vertices choose a uniformly random vertex and then a uniformly random neighbour of that vertex; attach a new leaf to the neighbour. Let \(T_n\) be the resulting tree and let \(J_n\) be its number of vertices of degree at least two. Then
\[
\lim_{n\to\infty}n\Pr(J_n=2)=3,\qquad
\lim_{n\to\infty}n\Pr(\operatorname{diam}(T_n)\le3)=5.
\]
More precisely, every two-internal-vertex realization has two adjacent hubs. Mark the unique hub that **first became the second internal vertex**, and let \(B_n\) be its number of leaf neighbours, defined on \(J_n=2\). For every fixed positive integer \(b\),
\[
\lim_{n\to\infty}n\Pr(J_n=2,B_n=b)=\frac4{b(b+2)}.
\]
The limiting conditional probability mass function of \(B_n\) given \(J_n=2\) is therefore \(4/[3b(b+2)]\). The two-internal-vertex event accounts for three fifths of the rare diameter-at-most-three event; stars account for two fifths.

This explicitly differs from the coefficient \(D_2=2\) and the formula \(U_b=4(b+1)/(b+2)!\) presented in Section 4.3 of Krapivsky and Redner (2017) for two-hub configurations. Its displayed exact two-hub recurrence contains a factor \(b-1\) that is absent from its continuum equation (22); retaining that factor yields the amplitudes above. This is a mathematical comparison of published equations, not a claim that the earlier work lacked the model or its two-hub recurrence.

## Assumptions and scope
All trees are finite simple undirected labelled trees. The process begins with the edge joining vertices \(1,2\); at each size \(n\ge2\), draw \(V_n\) uniformly from existing vertices, draw \(W_n\) uniformly from its neighbours conditional on \(V_n\), then join vertex \(n+1\) to \(W_n\). Probabilities include every possible history of the growth process. All limits are along the full integer sequence \(n\to\infty\), and the assertion for each fixed \(b\) is not an assertion uniform in \(b\) growing with \(n\).

For \(n\ge4\), a tree has diameter at most three if and only if it has at most two nonleaf vertices, which must be adjacent if two exist. The event \(J_n=1\) consists of stars, whereas \(J_n=2\) consists of proper double stars. Let \(q_n(b)=\Pr(J_n=2,B_n=b)\), interpreted as zero outside \(1\le b\le n-3\). The original central hub is the unique nonleaf until the first departure from a star; after that first departure, the identity of the newly internal hub is permanent whenever \(J_n=2\) persists.

## Proof
**1. Star masses and the exact two-hub recurrence.** For a star with \(n\ge3\) vertices, attachment to its centre occurs with probability \((n-1)/n\), because a sampled leaf necessarily redirects to the centre. Thus the star mass satisfies \(s_{n+1}=(n-1)s_n/n\), with \(s_3=1\), giving \(s_n=2/(n-1)\).

On the double-star event, let the old hub have \(a=n-2-b\) leaves and the marked second hub have \(b\) leaves. To remain a double star and attach to the old hub, the sampled vertex must be one of its \(a\) leaves or be the second hub followed by the edge to the old hub. This occurs with probability \((a+1/(b+1))/n\). Similarly, attachment to the second hub has probability \((b+1/(a+1))/n\), which increments \(b\) by one. Attaching to any other vertex makes a third nonleaf and can never return to \(J=2\), since degrees never decrease. The only entry from a star occurs when its centre is sampled and one of its leaves is chosen, with probability \(1/n\); the new second hub then has one leaf. Hence, for \(n\ge3\),
\[
q_{n+1}(b)=\frac{n-2-b+(b+1)^{-1}}n q_n(b)
 +\frac{b-1+(n-b)^{-1}}n q_n(b-1)
 +\frac{2\mathbf1_{\{b=1\}}}{n(n-1)},\qquad q_3(b)=0.
\]
This is an **exact**, finite-size recursion, including both boundaries.

**2. Fixed-\(b\) limits.** Put \(u_{n,b}=nq_n(b)\) and \(\beta_b=b+1-1/(b+1)>0\). When \(b\) is fixed, the recurrence becomes
\[
u_{n+1,b}=\left(1-\frac{\beta_b}{n}+O_b(n^{-2})\right)u_{n,b}
+\frac{(b-1)u_{n,b-1}+2\mathbf1_{\{b=1\}}}{n}+O_b(n^{-2})u_{n,b-1}.
\]
For \(b=1\), the predecessor term is absent; the standard stable-recursion lemma states that if \(z_{n+1}=(1-\beta/n+O(n^{-2}))z_n+\gamma/n+o(n^{-1})\), with \(\beta>0\), then \(z_n\to\gamma/\beta\). This follows by comparing to a constant plus/minus arbitrary \(\varepsilon\), then iterating the contracted error (the product of \(1-\beta/(2n)\) tends to zero). Inducting on \(b\) both bounds \(u_{n,b}\) and gives
\[
 c_1=\frac2{\beta_1}=\frac43,\qquad
 c_b=\frac{b-1}{\beta_b}c_{b-1}\quad (b\ge2).
\]
Because \((b-1)/\beta_b=(b-1)(b+1)/(b(b+2))\), induction yields \(c_b=4/[b(b+2)]\).

**3. No mass escapes to diverging \(b\).** Fix \(\alpha=1/8\) and define \(F_n=\sum_b b^\alpha q_n(b)\). Conditional on a double star with \(a+b=n-2\), write \(p_A=[a+(b+1)^{-1}]/n\) and \(p_B=[b+(a+1)^{-1}]/n\). The one-step expectation of \(b^\alpha\), counting killed trajectories as zero, is \(p_Ab^\alpha+p_B(b+1)^\alpha\). Since \((b+1)^\alpha-b^\alpha\le\alpha b^{\alpha-1}\), the multiplicative loss is at least
\[
\frac1n\left(2-\frac1{b+1}-\frac1{a+1}-\alpha\left[1+\frac1{b(a+1)}\right]\right).
\]
For all \(n\ge12\) and positive \(a,b\) with \(a+b=n-2\), the parenthesis is at least \(35/32>17/16\). Indeed, if \(a\ge3\), use \(1/(a+1)\le1/4\), \(1/(b+1)\le1/2\), and \(1/[b(a+1)]\le1/4\); otherwise \(a\le2\) forces \(b\ge8\), giving an even stronger bound. Births from stars add \(2/[n(n-1)]\) to \(F_{n+1}\), so
\[
F_{n+1}\le\left(1-\frac{17}{16n}\right)F_n+\frac2{n(n-1)}\qquad(n\ge12).
\]
The elementary bound \(F_{12}\le 9^{1/8}<64/12\) and induction give \(F_n\le64/n\) for all \(n\ge12\). Therefore for any cutoff \(K\ge1\),
\[
 \sup_{n\ge12} n\sum_{b>K}q_n(b)\le \frac{64}{K^{1/8}}.
\]
This proves tightness of the rescaled measures \(nq_n(\cdot)\), and hence allows interchange of the fixed-\(b\) limits and the sum:
\[
\lim_n n\Pr(J_n=2)=\sum_{b=1}^{\infty}\frac4{b(b+2)}
=2\sum_{b=1}^{\infty}\left(\frac1b-\frac1{b+2}\right)=3.
\]
Finally \(n\Pr(J_n=1)=2n/(n-1)\to2\), and for \(n\ge4\) the events \(J_n=1\) and \(J_n=2\) partition diameter at most three. Summing gives \(5\). Normalizing the fixed-\(b\) masses by their total \(3\) proves the conditional limit.

## Verification
`checker.py` uses exact rational probabilities and independently enumerates the labelled growth histories for \(3\le n\le8\). It reconstructs attachment probabilities by summing over sampled vertices and their neighbours, verifies star probabilities, computes the number of nonleaves and the marked hub from each full labelled tree, and compares the results against the closed finite-state recursion. It makes 29 exact checks or asymptotic probes, and reports success. A separate floating-point recursion for \(n=5000\) gives approximately \(n\Pr(\operatorname{diam}\le3)=5.006849\) and checks the first seven amplitudes. All infinite assertions are established by the proof above; finite verification does not prove the asymptotic theorem.

## Relationship to prior work
Krapivsky and Redner (2017, Section 4, equations (11), (22)–(24) and Section 5.2) already developed the two-hub recurrence and proposed the fixed-small-hub amplitude \(4(b+1)/(b+2)!\), with summed amplitude \(2\). In equation (11), however, the coefficient multiplying the predecessor \(H_{b-1,n}\) tends to \((b-1)/n\). That nonconstant multiplier is missing from the right-hand side of their continuum equation (22). Keeping it leads to the different recurrence and constants established here, agreeing with their values at \(b=1,2\) but differing already at \(b=3\). In particular their \(U_3=2/15\) contrasts with \(4/15\) here; their total \(2\) contrasts with \(3\). The exact two-hub recurrence, star probability, and qualitative rarity are not newly claimed.

Addario-Berry et al. (2024), the motivating paper, rigorously treats the same random-friend-tree model, with primary MSC 60C05, and studies its diameter. Cannings and Jordan (2013) provide related foundations of random-walk attachment. The present claim isolates the sharp finite-diameter constant and a probability-conserving, marked-secondary-hub limit.

## Limitations
The result is specific to one-step undirected complete redirection starting from one edge. It does not describe typical tree diameters, all component counts, or the distribution of double-star hub sizes when both grow with \(n\). The known finite-state recursion is used, not claimed as new. The published discrepancy is established by comparison of explicit formulas but does not establish the absence of any alternative publication giving the corrected coefficients. No independent mathematical review has been performed.

## References
1. P. L. Krapivsky and S. Redner, “Emergent Network Modularity” (2017), arXiv:1706.01514, in particular Sections 2, 4 and 5.2; full text: https://sites.santafe.edu/~redner/pubs/pdf/enm.pdf.
2. L. Addario-Berry, S. Briend, L. Devroye, S. Donderwinkel, C. Kerriou and G. Lugosi, “Random friend trees” (first posted 2024-03-29), arXiv:2403.20185.
3. C. Cannings and J. Jordan, “Random walk attachment graphs” (2013), arXiv:1303.1052.
