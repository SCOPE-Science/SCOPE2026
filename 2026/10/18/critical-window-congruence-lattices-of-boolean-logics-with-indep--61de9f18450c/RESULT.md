# Critical-window congruence lattices of Boolean logics with independent De Morgan negations

## Finding
For a Boolean algebra on \(n\) atoms equipped with independently sampled De Morgan negations, the entire congruence lattice undergoes a structural critical transition near \(\log n\) operators. At that scale the nontrivial proper congruences are, with probability tending to one, exactly those supported on the points with **zero total incoming degree** in the corresponding directed graph.

Let \(r=r_n\in\mathbb N\), \(r-\log n=O(1)\). Write \(Z_n\) for the zero-indegree points and \(\lambda_n=n(1-1/n)^{nr}\). Then
\[
\Pr\big(\operatorname{Con}(A_{n,r})\cong\mathcal P(Z_n)\oplus\mathbf1\big)\longrightarrow1,
\]
where \(\oplus\mathbf1\) means **adjoin a new greatest element**, and the isomorphism identifies actual congruences with subsets of \(Z_n\) plus the universal congruence. Moreover
\[
 d_{\mathrm{TV}}\big(\mathcal L(|Z_n|),\operatorname{Pois}(\lambda_n)\big)\to0,
 \qquad \Pr(A_{n,r}\text{ is simple})=e^{-\lambda_n}+o(1).
\]
If \(r-\log n\to c\in\mathbb R\), the dimension has limiting Poisson mean \(e^{-c}\). If instead \(r=\lfloor\log n\rfloor\), the subsequential simplicity limits are precisely \([e^{-e},e^{-1}]\). The lattice statement is stronger than this numerical corollary.

## Assumptions and scope
Fix \(n\ge2\) and the Boolean algebra \(B_n=(\mathcal P([n]),\cap,\cup,\varnothing,[n])\). A *De Morgan negation* here means a unary **dual lattice homomorphism**, reversing finite unions/intersections and exchanging top/bottom; no involution axiom is imposed. Every such map has a unique form
\[
N_j(X)=[n]\setminus\tau_j^{-1}(X), \qquad \tau_j:[n]\to[n].
\]
Choose each \(\tau_j\) independently and uniformly among \(n^n\) maps. Loops and duplicate directed edges \(u\to\tau_j(u)\) are allowed. No fixed-outdegree claim is made: the operator count \(r=r_n\) diverges on the logarithmic scale.

For \(S\subseteq[n]\), define the Boolean lattice congruence \(\theta_S\) by
\[
 X\equiv Y\pmod{\theta_S}\iff X\mathbin\triangle Y\subseteq S.
\]
Every Boolean lattice congruence is uniquely of this form. Call \(S\) *closed* if no edge enters it from its complement. Let \(Z_n=\{v:\forall u,j\;\tau_j(u)\ne v\}\). Congruence order is inclusion of support sets. The finite case \(S=[n]\) always gives the universal congruence.

## Proof
**Step 1: deterministic congruence–graph correspondence.** A Boolean congruence \(\theta_S\) respects every \(N_j\) precisely when \(\tau_j^{-1}(S)\subseteq S\). Indeed, Boolean symmetric differences obey
\[
N_j(X)\mathbin\triangle N_j(Y)=\tau_j^{-1}(X\mathbin\triangle Y).
\]
The forward condition is necessary by taking \(X\mathbin\triangle Y=S\), and sufficient by inclusion. Thus the congruence supports are exactly the subsets with no incoming edge from outside. Every \(S\subseteq Z_n\) is closed, and \([n]\) is closed.

**Step 2: exclude every other proper closed set.** Put \(m=|S|\), \(1\le m<n\). The \(r(n-m)\) edges issuing outside \(S\) avoid \(S\) with probability \((1-m/n)^{r(n-m)}\). Conditional on this event, if \(S\not\subseteq Z_n\), an edge from a point inside \(S\) must end inside \(S\). These internal edges are independent of the external edges, and the union bound yields
\[
\Pr(S\text{ closed},\ S\not\subseteq Z_n)
\le (1-m/n)^{r(n-m)}\min\{1,rm^2/n\}.
\tag{1}
\]
Summing over \(\binom nm\) choices of \(S\), use \(r=\log n+O(1)\) and split the range. For any fixed \(K\), at \(1\le m\le K\), the factor \(rm^2/n\to0\), while \(\binom nm(1-m/n)^{r(n-m)}\) is bounded. For \(K<m\le n/(\log n)^2\),
\[
\binom nm(1-m/n)^{r(n-m)}
\le\frac{(ne^{-r}e^{rm/n})^m}{m!}\le\frac{C^m}{m!}
\]
for an absolute \(C\) depending only on the bound on \(|r-\log n|\). This tail vanishes uniformly as \(K\to\infty\). For \(n/(\log n)^2<m\le n/2\), the same expression is at most
\[
\left(\frac{en e^{-r/2}}m\right)^m
\le\left(O((\log n)^2/\sqrt n)\right)^m,
\]
whose sum tends to zero. Finally, if \(n/2<m<n\), write \(k=n-m\). The expected number of closed \(m\)-sets is at most
\[
\binom nk(k/n)^{rk}\le\big(e(k/n)^{r-1}\big)^k
\le\big(e2^{-(r-1)}\big)^k;
\]
its sum over \(1\le k<n/2\) also tends to zero. By (1), with probability \(1-o(1)\) there is no proper closed \(S\) outside \(\mathcal P(Z_n)\). Along with Step 1, this proves the full congruence lattice statement (including its order).

**Step 3: Poisson dimension and simplicity.** All \(nr\) targets are independent uniform points. For every fixed positive integer \(m\), the falling-factorial moment of \(W_n=|Z_n|\) equals
\[
 \mathbb E (W_n)_m=(n)_m(1-m/n)^{nr}.
\]
If \(r-\log n\to c\), this tends to \(e^{-cm}\), the factorial moments of \(\operatorname{Pois}(e^{-c})\). Tightness plus the standard factorial-moment characterization gives weak convergence and, since the variables are integer valued, total-variation convergence. More generally, \(\lambda_n\) remains in a compact positive interval when \(r-\log n=O(1)\). Every subsequence has a further one on which \(\lambda_n\to\lambda\) and the same argument applies; hence the distance from \(\operatorname{Pois}(\lambda_n)\) tends to zero without assuming a limit for \(r-\log n\). A lattice \(\mathcal P(Z_n)\oplus\mathbf1\) has exactly two elements if and only if \(Z_n=\varnothing\). Therefore \(\Pr(A_{n,r}\text{ simple})=e^{-\lambda_n}+o(1)\).

For \(r=\lfloor\log n\rfloor\), \(\lambda_n=\exp(\{\log n\})+o(1)\). The fractional parts of \(\log n\) have every value of \([0,1]\) as a subsequential limit: between consecutive exponential scales, the intervals \([e^{k+a},e^{k+b}]\) contain integers for all large \(k\) and any \(0\le a<b\le1\). Continuity of \(x\mapsto e^{-e^x}\) yields the asserted full interval of subsequential limits.

## Verification
A standalone Python 3 standard-library verifier, `artifacts/verify.py`, independently checks the Boolean-algebra congruence condition by actual operation tables for all tuples of maps with \(n\in\{2,3\}\), \(r\in\{1,2\}\), and compares with the forbidden-incoming-edge characterization. It also verifies the exact occupancy factorial-moment identity by exhaustive maps for small \(n,r\), and prints finite samples of the structural lattice event. The unrestricted asymptotic result rests on the proof above, not finite enumeration or simulation.

## Relationship to prior work
Guričan and Ghumashyan (first published online 2023-01-04; primary MSC 03G25) study finite algebra congruences and strong endomorphism kernel properties and review their context in Ockham algebras; the present finding instead concerns a random family of multiple negations and its full congruence-lattice law. Davey and Haviar (2024, Section 2.3 and Lemma 2.5) give Ockham-algebra definitions and deterministic congruence theory; such foundations are not claimed as new here. Cai and Devroye, arXiv:1504.06238 (Section 4, Theorem 6), prove that an independent random \(r\)-out directed multigraph is whp strongly connected when \(r-\log n\to+\infty\) and not strongly connected when \(r-\log n\to-\infty\); their Lemma 13 also calculates the expected number of non-leaf (closed) sets. The present assertion is the **constant-width critical-window full inclusion-poset law**, not the already-known coarse 0–1 strong-connectivity transition or the elementary formula for the expected number of closed sets. A strong-connectivity critical-window formula by itself would also not establish the Boolean-plus-top congruence structure.

## Limitations
This result applies only to independent uniformly chosen maps, Boolean reducts and the scale \(r=\log n+O(1)\), and does not assert uniform integrable convergence of congruence counts or their expectations: rare large congruence lattices may affect unbounded moments. No extension to a fixed number of negations or to non-Boolean Ockham algebras is claimed. A logically equivalent older statement in random directed graph or multi-operator congruence literature remains a publication-priority risk. The review here is not independent validation.

## References
- J. Guričan and H. Ghumashyan, “Strong endomorphism kernel property for finite Brouwerian semilattices and relative Stone algebras”, *Mathematica Bohemica* 149 (2024), 13–25; first published online 2023-01-04. DOI: `10.21136/MB.2023.0050-22`. Primary MSC 2020: 03G25.
- B. A. Davey and M. Haviar, “Factor principal congruences and Boolean products in filtral varieties”, *Algebra Universalis*, published online 2024-03-05, DOI: `10.1007/s00012-024-00846-8`; particularly Section 2.3 and Lemma 2.5.
- X. S. Cai and L. Devroye, “The graph structure of a deterministic automaton chosen at random: full version”, arXiv:1504.06238, Section 4, Theorem 6 and Lemma 13, first posted 2015; graph limit results only cited as antecedents.
