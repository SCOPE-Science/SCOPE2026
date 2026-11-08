# A double-exponential Poisson window for nested possibility on random two-agent S5 frames

## Finding

Let \(R_n\) and \(S_n\) be independent uniform equivalence relations on \([n]\), each chosen uniformly among all \(B_n\) labelled set partitions. Independently mark each vertex by a proposition \(p\) with probability \(p_n\). Put \(r_n e^{r_n}=n\), with \(r_n>0\), and suppose
\[
 p_n r_n-\log r_n\longrightarrow c\in\mathbb R.
\]
For each \(j\ge1\), let \(Z_{n,j}\) count \(R_n\)-classes of size \(j\) on which \(\Diamond_{R_n}\Diamond_{S_n}p\) is false, and let \(Z_n=\sum_{j\ge1}Z_{n,j}\). Then for every fixed \(J\ge1\),
\[
 (Z_{n,1},\ldots,Z_{n,J})\ \xrightarrow{\mathrm d}\
 (P_1,\ldots,P_J),\qquad
 P_j\ \text{independent},\quad P_j\sim\operatorname{Poisson}(e^{-cj}/j!).
\]
Moreover,
\[
 Z_n\xrightarrow{\mathrm d}\operatorname{Poisson}(\exp(e^{-c})-1).
\]
Thus the probability that \(\Diamond_{R_n}\Diamond_{S_n}p\) holds at **every** world converges to
\[
 \boxed{\exp(1-\exp(e^{-c}))}.
\]
All claims concern the specified random finite two-agent \(\mathsf{S5}\) models; they do not assert the same limit for arbitrary equivalence frames or nonindependent valuations.

## Assumptions and scope

An equivalence relation is identified with its partition into nonempty classes. For any relation \(T\), the modal formula \(\Diamond_T\psi\) is true at world \(x\) if some \(T\)-related world satisfies \(\psi\). The Boolean atomic valuation of \(p\) is sampled once and reused in both nested modalities. The two equivalence relations and this valuation are mutually independent. The parameters \(p_n\in[0,1]\) for all sufficiently large \(n\); the convergence hypothesis forces \(p_n\to0\). Fixing \(c\in\mathbb R\) imposes the critical scale \(p_n\sim\log\log n/\log n\).

Define \(F_n\subseteq[n]\) as the union of those \(S_n\)-classes containing no marked vertex and \(T_n=|F_n|\). An \(R_n\)-class \(C\) contributes to \(Z_{n,j}\) exactly if \(|C|=j\) and \(C\subseteq F_n\). For every integer \(k\ge0\), conditional on any fixed \(F_n\) of size \(m\), the following finite identity is exact:
\[
 \mathbb E[(Z_n)_k\mid F_n]
 =\frac{k!}{B_n}\sum_{s=k}^{m}\binom ms\left\{\begin{matrix}s\\k\end{matrix}\right\}B_{n-s},
\]
where \((z)_k=z(z-1)\cdots(z-k+1)\), \((z)_0=1\), and the braces are Stirling numbers of the second kind (including the standard \(s=k=0\) convention). The identity also holds when \(F_n\) is random, by conditioning.

## Proof

**Step 1: the uniform-partition urn representation.** Write \(B_n\) for the number of partitions of \([n]\). Stam's exact construction first draws a positive integer \(M\) with
\[
 \Pr(M=t)=\frac{t^n}{e\,t!\,B_n}\qquad(t\ge1),
\]
then independently puts each vertex into one of the \(M\) uniformly chosen labelled urns and deletes empty urns. For each fixed partition with \(h\) blocks the total probability of producing it equals
\[
 \frac1{eB_n}\sum_{t\ge h}\frac{(t)_h}{t!}=\frac1{B_n},
\]
so the resulting partition is uniform. For \(r_n e^{r_n}=n\), the classical moment estimates for this urn variable give
\[
 M=\frac{n}{r_n}+O_{\Pr}\!\left(\frac{\sqrt n}{r_n}\right),
 \qquad \frac nM-r_n\xrightarrow{\Pr}0,
 \qquad M e^{-n/M}\xrightarrow{\Pr}1.
\]
The estimates follow, for example, from the mean and variance in Chern--Diaconis--Kane--Rhoades (2015), Section 2, with their saddle point defined using \(n+1\) instead of \(n\), an asymptotically negligible difference.

**Step 2: the effective unmarked set has a deterministic urn-scale size.** Realize \(S_n\) with an independent urn variable \(M_S\). For a vertex \(v\), let \(I_v\) indicate that the \(S_n\)-urn containing \(v\) has no marked vertex. Conditional on \(M_S=M\), with \(q_n=1-p_n\), direct independence of markings and urn assignments gives
\[
 \mathbb E[I_v\mid M]=q_n(1-p_n/M)^{n-1},
\]
while for distinct \(u,v\),
\[
 \mathbb E[I_uI_v\mid M]
 =q_n^2\left[\frac1M(1-p_n/M)^{n-2}
   +\left(1-\frac1M\right)(1-2p_n/M)^{n-2}\right].
\]
Since \(p_n r_n-\log r_n\to c\), \(p_n\to0\), and \(n/M_S-r_n\to0\) in probability, these imply
\[
 \frac{n}{M_S}\mathbb E[I_v\mid M_S]\xrightarrow{\Pr}d:=e^{-c}.
\]
On urn counts satisfying \(n/M_S=r_n+o(1)\), the displayed pair expression shows \(\operatorname{Cov}(I_u,I_v\mid M_S)=O(1/n)\) and the conditional variance of \(T_n/M_S\) is \(O(r_n^2/n)=o(1)\). Hence conditional Chebyshev and the concentration of \(M_S\) yield
\[
 \boxed{\ T_n/M_S\xrightarrow{\Pr}d\ }.
\]
In particular, \(T_n r_n/n\xrightarrow{\Pr}d\). This step preserves the dependence between vertices that occupy the same \(S_n\)-class; it does not treat the effective unmarked indicators as independent.

**Step 3: total number of bad classes.** Independently realize \(R_n\) through Stam's construction with \(M_R\) urns. Conditional on \(T_n=m\) and \(M_R=M\), a bad \(R_n\)-class is exactly a nonempty urn receiving only vertices from \(F_n\). For every fixed integer \(k\ge0\), selecting ordered distinct urns and applying inclusion--exclusion to require each selected urn to receive at least one of the \(m\) eligible vertices gives the exact identity
\[
 \mathbb E[(Z_n)_k\mid T_n=m,M_R=M]
 =(M)_k\left(1-\frac{k}{M}\right)^{n-m}
 \sum_{i=0}^{k}(-1)^i\binom ki\left(1-\frac{i}{M}\right)^m.
\]
On every deterministic sequence of conditionings with \(n/M_R-r_n\to0\) and \(m/M_R\to d\), the inclusion--exclusion sum tends to \((1-e^{-d})^k\), whereas the prefactor tends to \(e^{kd}\), because \(M_R e^{-n/M_R}\to1\). Thus the conditional factorial moment tends to \((e^d-1)^k\) for every fixed \(k\). The factorial-moment characterization of the Poisson law proves the corresponding conditional weak limit. As the required conditioning regime has probability tending to one, bounded-test-function convergence yields the unconditional limit \(Z_n\Rightarrow\operatorname{Poisson}(e^d-1)\).

**Step 4: size-resolved independence.** Fix distinct positive integers \(j_1,\ldots,j_t\), with multiplicities \(k_1,\ldots,k_t\), and put \(k=\sum_\ell k_\ell\), \(s=\sum_\ell j_\ell k_\ell\). Given \(m=T_n\) and \(M=M_R\), choosing ordered urns with specified numbers of eligible vertices and zero ineligible vertices gives the exact mixed factorial moment
\[
 \mathbb E\!\left[\prod_{\ell=1}^{t}(Z_{n,j_\ell})_{k_\ell}\ \middle|\ m,M\right]
 =\frac{(M)_k(m)_s}{M^s\prod_{\ell=1}^t(j_\ell!)^{k_\ell}}
   \left(1-\frac{k}{M}\right)^{n-s}.
\]
It tends to \(\prod_\ell (d^{j_\ell}/j_\ell!)^{k_\ell}\), because \(m/M\to d\) and \(M e^{-n/M}\to1\). Joint factorial moments therefore give independent Poisson limits of means \(d^j/j!=e^{-cj}/j!\) for every fixed finite list of sizes.

**Step 5: logical equivalence and finite formula.** The truth of \(\Diamond_{S_n}p\) at a world is constant on its \(S_n\)-class and false exactly on \(F_n\). Consequently \(\Diamond_{R_n}\Diamond_{S_n}p\) is false precisely on \(R_n\)-classes included in \(F_n\). The global formula holds if and only if \(Z_n=0\), whose probability converges to \(\exp(-(e^d-1))=\exp(1-\exp(e^{-c}))\).

For the finite factorial identity in the statement, an ordered \(k\)-tuple of bad \(R_n\)-blocks having union of size \(s\) is chosen in \(\binom ms k!\left\{\begin{smallmatrix}s\\k\end{smallmatrix}\right\}\) ways; the remaining \(n-s\) vertices admit exactly \(B_{n-s}\) partitions. Division by \(B_n\) proves the identity independently of the urn construction.

## Verification

Run `python3 checker.py` using only the Python standard library. The checker reconstructs Bell and Stirling numbers, enumerates all partitions on up to five labelled vertices, and verifies the exact conditional factorial-moment identity for every possible cardinality of \(F_n\). It also enumerates all pairs of partitions and all Boolean valuations on up to four vertices to check the precise equivalence between the number of bad blocks and global satisfaction of the nested modal formula. It prints `NESTED_S5_EXACT_CHECKS_OK 3873` on success. The finite checker does not establish the asymptotic Poisson convergence; the urn and moment arguments above supply that proof.

## Relationship to prior work

Zantedeschi (2026) develops modal exchangeability and de Finetti representations on \(\mathsf{S5}\) and \(\mathsf{S4}\) frames. The inspected paper addresses symmetry-constrained distributions on valuations of countable frames, not independently uniform finite equivalence relations and the universal truth of a nested two-agent possibility formula.

Stam's urn representation and the concentration estimates used above are prior results, as presented in Chern, Diaconis, Kane, and Rhoades (2015). Arratia and Tavaré (1994) give broad independent-process approximations for component counts of random assemblies, including one set partition. Their inspected assembly and partition arguments provide important background, but do not directly state the interacting two-partition, shared-valuation critical window or its double-exponential limit. No originality is claimed for Bell-number asymptotics, Stirling-number identities, or general Poisson factorial-moment methods.

## Limitations

The result requires two independent **uniform** labelled partitions and independent vertex markings with the stated critical scaling. It concerns the global satisfaction of one nested formula, not a complete random-modal zero-one law, arbitrary frame distributions, non-exchangeable valuations, or growing modal depth. No explicit rate of convergence or extension to more agents is proved. Convergence can be slow because \(p_n\) decays like \(\log\log n/\log n\). Earlier probabilistic combinatorics might contain an equivalent formulation not identified by the consulted sources; independent audit has not been performed.

## References

1. D. Zantedeschi, *Modal Exchangeability: Centered Symmetry and the Credal Architecture of Kripke Frames*, arXiv:2603.27547 (first public version, March 29, 2026). https://arxiv.org/html/2603.27547v2
2. B. Chern, P. Diaconis, D. M. Kane, and R. C. Rhoades, *Central Limit Theorems for Some Set Partition Statistics*, Advances in Applied Mathematics **70** (2015), 92--105, Section 2; arXiv:1502.00938. https://arxiv.org/abs/1502.00938
3. R. Arratia and S. Tavaré, *Independent Process Approximations for Random Combinatorial Structures*, Advances in Mathematics **104** (1994), 90--154; arXiv:1308.3279. https://arxiv.org/html/1308.3279v1
