# Sharp alphabet threshold for correlations of three-letter factors in de Bruijn cycles

## Finding
Let \(q\ge3\). Sample uniformly from the cyclic de Bruijn sequences of order two on a labelled \(q\)-letter alphabet \(\Sigma\), up to cyclic rotation. Choose \(b\in\Sigma\) and four letters \(a,d,c,e\in\Sigma\setminus\{b\}\) with \(a\ne d\) and \(c\ne e\). Let \(X_{abc}\) and \(X_{dbe}\) be the indicators that the indicated cyclic length-three factors occur.

Write \(x=\mathbf1_{a=c}\), \(y=\mathbf1_{d=e}\), \(u=\mathbf1_{d=c}\), \(v=\mathbf1_{a=e}\). The covariance is completely determined by the equality pattern between the ordered pairs \((a,d)\) and \((c,e)\):

\[
\operatorname{Cov}(X_{abc},X_{dbe})=\begin{cases}
\dfrac{1}{q^2(q-1)}, &x+y+u+v=0,\\[3pt]
\dfrac{q-3}{q^2(q-1)(q-2)},&x+y+u+v=1,\\[3pt]
\dfrac{q^2-5q+5}{q^2(q-1)^2(q-2)},&x=y=1,\\[3pt]
\dfrac{q-5}{q^2(q-1)(q-2)},&u=v=1.
\end{cases}
\]

These four cases are exhaustive and mutually exclusive. The zero-match class is feasible only for \(q\ge5\), and the one-match class only for \(q\ge4\). Thus *all* such distinct local factor indicators are pairwise nonnegatively correlated exactly when \(q\ge5\), and *all* are strictly positively correlated exactly when \(q\ge6\). For \(q=5\), covariance vanishes precisely for the crossed equality \(a=e,\ d=c\). For \(q=4\), precisely this crossed class has negative covariance; for \(q=3\), both feasible two-match classes have negative covariance. For each fixed central letter, the exceptional crossed class contains exactly \((q-1)(q-2)\) ordered pairs of factor indicators; hence there are \(q(q-1)(q-2)\) such ordered pairs when the central letter varies.

## Assumptions and scope
A cyclic de Bruijn sequence of order two contains each ordered pair from \(\Sigma^2\) exactly once as a cyclic contiguous factor. Each particular triple \(abc\) can consequently appear at most once, because its initial pair \(ab\) occurs once. The random ensemble consists of all such cyclic sequences, each with equal probability. The specified two triples are distinct and their four underlying directed edges are pairwise distinct by the stated restrictions. Alphabet labels are fixed; no quotient by permutations of the alphabet is taken. Covariance uses the Bernoulli indicators defined above. All restrictions on \(q\) and on equality patterns are essential.

## Proof
**1. Eulerian encoding and counting.** Consider the directed graph \(G\) on vertex set \(\Sigma\), with one labelled directed edge \((s,t)\) for each ordered pair \((s,t)\in\Sigma^2\), including loops. Each de Bruijn cycle corresponds bijectively to a cyclic Euler tour using all these edges exactly once. The directed BEST theorem counts cyclic tours of an Eulerian directed multigraph \(H\) with individually distinguished edges as \(\tau_r(H)\prod_z(\deg_H^+(z)-1)!\), where \(\tau_r(H)\) is the number of spanning in-arborescences rooted at any fixed \(r\) (zero if the tour does not exist). For \(G\), the directed Laplacian is \(qI-J\), so the directed Matrix-Tree theorem gives \(\tau_b(G)=q^{q-2}\). Thus the number of cycles is \(q^{q-2}((q-1)!)^q\).

**2. Two nonoverlapping prescribed turns.** The event \(X_{abc}=X_{dbe}=1\) prescribes the two consecutive edge pairs \((a,b)\to(b,c)\) and \((d,b)\to(b,e)\). Their four edges are distinct, so these two disjoint two-edge paths can be replaced by separate shortcut edges \((a,c)\) and \((d,e)\), giving a balanced multigraph \(H\). Expanding or contracting the distinguished shortcuts bijects cyclic Euler tours in \(H\) with the prescribed tours of \(G\). All outdegrees of \(H\) equal \(q\), except the outdegree of \(b\), which is \(q-2\). Consequently,
\[
\mathbb P(X_{abc}=X_{dbe}=1)=\frac{\tau_b(H)}{\tau_b(G)(q-1)(q-2)}.
\tag{1}
\]
This identity also handles disconnected \(H\), because its arborescence count is then zero.

**3. A two-by-two tree determinant.** Delete row and column \(b\) from the Laplacian of \(G\). The resulting \((q-1)\)-square matrix is \(A=qI-J\), with inverse \(A^{-1}=(I+J)/q\). Let \(\mathbf e_z\) denote the coordinate vector at \(z\ne b\). In the rooted Laplacian, each shortcut replacement subtracts the rank-one matrix \(\mathbf e_{a_i}\mathbf e_{c_i}^{\mathsf T}\), where \((a_1,a_2)=(a,d)\) and \((c_1,c_2)=(c,e)\). Therefore the determinant lemma gives
\[
\frac{\tau_b(H)}{\tau_b(G)}=\det\left(I_2-\frac1q
\begin{pmatrix}1+x&1+u\\1+v&1+y\end{pmatrix}\right).
\tag{2}
\]
Equation (1) now yields
\[
J:=\mathbb P(X_{abc}=X_{dbe}=1)=
\frac{q^2-q(2+x+y)+x+y+xy-u-v-uv}{q^2(q-1)(q-2)}.
\tag{3}
\]
Applying the identical single-shortcut argument to one triple gives
\[
\mathbb P(X_{abc}=1)=\frac{q-1-x}{q(q-1)},\qquad
\mathbb P(X_{dbe}=1)=\frac{q-1-y}{q(q-1)}.
\tag{4}
\]

**4. Equality-pattern exhaustion and sign.** Because \(a\ne d\) and \(c\ne e\), any equality between an input and output letter is part of an injective partial matching. The only possibilities are no equality, one equality (in any of four positions), a full direct matching \(a=c,\ d=e\), or a full crossed matching \(a=e,\ d=c\). Insert each in \(J-\mathbb P(X_{abc}=1)\mathbb P(X_{dbe}=1)\), using (3)--(4). Direct cancellation gives exactly the four displayed covariance expressions. Their feasibility thresholds follow by counting available letters outside \(\{b\}\). The numerator \(q^2-5q+5\) is negative at \(q=3\) and strictly positive for every integer \(q\ge4\). The crossed numerator \(q-5\) is negative for \(q=3,4\), zero at \(q=5\), and positive thereafter. The other two expressions are positive whenever the corresponding class is feasible. This proves the sharp threshold and all equality and negativity cases. The count of crossed ordered pairs for each \(b\) is the number of ordered choices of distinct \(a,d\) from \(\Sigma\setminus\{b\}\), namely \((q-1)(q-2)\). \(\square\)

## Verification
The standalone `verify.py` performs two computations independent of the symbolic covariance simplification. First, it enumerates every local edge-successor matching of the order-two complete directed de Bruijn graph for \(q=3\) and \(q=4\), retains exactly those inducing one Euler cycle, and counts each prescribed pair of triples; it checks respectively \(24\) and \(20736\) cycles. Second, it physically contracts the four specified edges and computes a rooted Laplacian determinant with integer Bareiss elimination for every admissible ordered motif pair at \(q=3,4,5,6\), comparing exact rational probabilities. It checks the covariance case formulas and sign distributions. The recorded stdout appears in `verification_output.txt`. Run `python3 verify.py` with Python 3 standard library only. These exhaustive small cases verify the calculation but are not used to infer the infinite theorem.

## Relationship to prior work
Sawada and Gabrić, *Las Vegas Algorithms to Generate Universal Cycles and de Bruijn Sequences Uniformly at Random* (arXiv:2510.16545, first posted 2025-10-18), establishes the uniform ensemble and arborescence sampling context, not this covariance sign threshold. Rødland, *Exact Distribution of Word Counts in Shuffled Sequences* (2006), especially Theorem 1 and Theorem 3, gives general formulae for joint counts of prescribed patterns under fixed shorter-word compositions. Its general path-contraction theorem **already implies the raw joint probability** (3), and that formula or the underlying BEST/Matrix-Tree technique is not presented here as original. Cowan (1991) gives a general expectation formula for individual fixed-composition patterns and likewise supplies background for the marginals. The contribution assessed here is the simultaneous, complete *sign classification and sharp alphabet cutoff* for all pairs of distinct nonloop triples sharing their middle letter, including exact exceptional and independence cases. No directly stated all-alphabet sign law was found in the inspected primary results; a differently formulated implication in other literature remains possible.

## Limitations
Only order-two de Bruijn cycles, two factors with the same central letter and four pairwise distinct component edges, and covariance of occurrence indicators are addressed. Pairs involving the central-letter loop, triples with different middle letters, higher-order cycles, and higher joint cumulants are not classified. The general pointwise count identity is classical; the novelty assessment is solely of its nontrivial uniform sign consequences. No independent scientific audit or external validation has been performed.

## References
1. J. Sawada and D. Gabrić, *Las Vegas Algorithms to Generate Universal Cycles and de Bruijn Sequences Uniformly at Random*, arXiv:2510.16545 (first public version 2025-10-18), https://arxiv.org/abs/2510.16545.
2. E. A. Rødland, *Exact Distribution of Word Counts in Shuffled Sequences*, Advances in Applied Probability 38 (2006), 116–133, DOI: 10.1239/aap/1143936143, https://doi.org/10.1239/aap/1143936143.
3. R. Cowan, *Expected Frequencies of DNA Patterns Using Whittle's Formula*, Journal of Applied Probability 28 (1991), 886–892, https://www.maths.usyd.edu.au/u/richardc/Whittleformula.pdf.
4. N. G. de Bruijn, T. van Aardenne-Ehrenfest, C. A. B. Smith, W. T. Tutte, BEST theorem and directed Matrix-Tree theorem (standard counting results).
