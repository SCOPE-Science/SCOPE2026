# Grounded undecided mass and parity-resolved stable limits in sparse one-attacker frameworks

## Finding
Fix \(0<p<1\) and put \(a=1-p\). On \(n\ge1\) labelled arguments choose, independently for each target \(v\), either no attacker (probability \(p\)), or one attacker selected uniformly from all \(n\) arguments (total probability \(a\)); self-attacks are permitted. Let \(U_n\) be the number of arguments labelled undecided by Dung's grounded semantics, and let \(C_{n,o}\), \(C_{n,e}\) be the numbers of odd- and even-length directed-cycle components. Write \(Z_n\) for the number of stable extensions.

The following exact finite-size distribution holds for every integer \(0\le k<n\):
\[
\Pr(U_n=k)=\binom nk\left(\frac an\right)^k k^k\,p\left(p+\frac{a(n-k)}n\right)^{n-k-1},\quad \Pr(U_n=n)=a^n,
\]
where \(0^0=1\). In particular \(\Pr(U_n=0)=\Pr(Z_n=1)=p\) **exactly at every size**.

Let \(T(s)\) be the unique probability generating function satisfying \(T(s)=s\exp(a(T(s)-1))\), \(0\le s\le1\). Then the entire integer-valued vector \((U_n,C_{n,o},C_{n,e})\) converges in distribution, and its joint limiting probability generating function is
\[
\boxed{\lim_{n\to\infty}\mathbb E[s^{U_n}x^{C_{n,o}}y^{C_{n,e}}]
=p\exp\bigl(x\operatorname{arctanh}(aT(s))\bigr)
\bigl(1-a^2T(s)^2\bigr)^{-y/2}}
\]
for \(s,x,y\in[0,1]\), with \(0^0:=1\). In particular, the limiting odd/even cycle counts are independent Poisson variables of means \(\lambda_o=\operatorname{arctanh}(a)\) and \(\lambda_e=-\tfrac12\log(1-a^2)\), and \(Z_n=0\) whenever \(C_{n,o}>0\), otherwise \(Z_n=2^{C_{n,e}}\). Thus
\[
\lim_{n\to\infty}\Pr(Z_n=0)=1-\sqrt{\frac{p}{2-p}},\qquad
\lim_{n\to\infty}\Pr(Z_n=2^j)=p\frac{\lambda_e^j}{j!}\quad(j=0,1,2,\ldots).
\]
The second set of events is disjoint from \(Z_n=0\). The limiting grounded-undecided count has mean \(a/p^2\).

## Assumptions and scope
The attacker choices above are independent *by target*. This is a partial functional digraph pointing from a vertex to its selected attacker, with a missing pointer at an unattacked vertex. An argumentation attack arrow is the reverse of this pointer. Directed cycles have the same lengths in either orientation. Grounded semantics is the least fixed point of Dung's characteristic operator; its three-valued labelling uses IN, OUT and UNDEC. A stable extension is a conflict-free set attacking every argument outside it. All expectations are over this exact finite random ensemble, not over a uniform set of attack relations with variable indegree. The parameter \(p\) stays strictly between zero and one as \(n\) grows; the endpoints and parameter scalings with \(n\) are not asserted.

## Proof
**Deterministic semantics.** Every component of the partial pointer graph ends either at an unattacked argument (a missing pointer) or at a directed cycle. From a missing pointer the grounded labelling alternates IN and OUT, with no undecided vertices. In a cycle component no vertex can be labelled IN at the first grounded iteration and induction leaves every member and every in-tree descendant UNDEC. Hence \(U_n\) is exactly the total size of the union of components containing a directed cycle. Stable extensions, which require complementary IN/OUT labels along every pointer edge, exist uniquely on each rooted tree component; an odd cycle precludes them, whereas an even cycle yields two choices and determines its attachments. Therefore \(Z_n=\mathbf1_{\{C_{n,o}=0\}}2^{C_{n,e}}\).

**Exact finite distribution.** Designate a \(k\)-subset \(S\) as precisely the union of cyclic components. Every vertex of \(S\) must select an attacker in \(S\); there are \(k^k\) such maps, of total weight \((a/n)^k k^k\). For the remaining \(m=n-k>0\) vertices, their pointers must form a forest directed toward missing pointers, never toward \(S\). Give each missing pointer weight \(p\) and each directed pointer to another member of the complement weight \(b=a/n\). The weighted rooted-forest identity is
\[
\sum_{\text{rooted forests on }[m]}p^{\#\text{roots}}b^{\#\text{edges}}
=p(p+mb)^{m-1}.
\]
For completeness, add a sink vertex \(0\). The directed matrix-tree theorem gives the determinant of the \(m\times m\) reduced Laplacian \((p+mb)I_m-bJ_m\), whose eigenvalues are \(p\) once and \(p+mb\) with multiplicity \(m-1\). Choosing \(S\) proves the displayed law. If \(k=n\), every vertex selects an attacker, giving probability \(a^n\). Taking \(k=0\) gives \(p(p+a)^{n-1}=p\); precisely these acyclic frameworks have one stable extension.

**Joint limit: sparse unicyclic components.** For any fixed rooted-directed unicyclic component shape \(H\) of size \(h\), let \(N_n(H)\) count its components. Directly choose its distinct labels and require no outside vertex to choose a pointer into its vertex set. Then
\[
\mathbb E N_n(H)=\frac{(n)_h}{|\operatorname{Aut}(H)|}
\left(\frac an\right)^h\left(1-\frac{ah}{n}\right)^{n-h}
\longrightarrow\frac{a^h e^{-ah}}{|\operatorname{Aut}(H)|}.
\]
For finitely many specified shapes, the identical disjoint-component calculation for factorial moments yields independent Poisson limits with these means. A size truncation is legitimate: for any vertex, a cyclic ancestry must at some stage follow a non-missing pointer to an earlier vertex. A union bound over its first \(r\) pointer choices yields
\(\Pr(v\text{ lies in a cyclic component})\le n^{-1}\sum_{r\ge1}r a^r=a/(np^2)\).
Consequently \(\sup_n\mathbb E U_n\le a/p^2\), and the mass in components larger than any fixed cutoff vanishes uniformly as the cutoff increases. This proves convergence of the full integer-valued vector from its finite-shape Poisson limits.

**Compute the limiting generating function.** The labelled EGF of in-trees is \(R(z)=z\exp(R(z))\). Each vertex in a unicyclic component contributes the factor \(a e^{-a}s\) after the Poisson-limit isolation probability, so put \(R(ae^{-a}s)=aT(s)\); here the equation for \(T\) follows by substitution. A directed cycle of length \(j\) with an independent in-tree attached at each cycle vertex contributes \((aT(s))^j/j\) to the logarithm of the component EGF. Mark odd and even cycles with \(x\) and \(y\) respectively. Independent Poisson components and the zero-component normalization \(\exp[-\sum_{j\ge1}a^j/j]=1-a=p\) give
\[
\exp\left(-\sum_{j\ge1}\frac{a^j}{j}+x\sum_{j\text{ odd}}\frac{(aT(s))^j}{j}+y\sum_{j\text{ even}}\frac{(aT(s))^j}{j}\right)
=p\exp(x\operatorname{arctanh}(aT(s)))(1-a^2T(s)^2)^{-y/2}.
\]
The component-shape expansion is absolutely convergent because \(a<1\); the previous tightness argument justifies passage from finitely many shapes and bounded generating functions. At \(s=1\), \(T(1)=1\). Marking odd cycles by \(x=0\) gives the claimed probabilities for stable extensions. Finally \(T'(1)=1/p\), so differentiating the unconditional limiting pgf \(p/(1-aT(s))\) yields mean \(a/p^2\). The statement concerning the limiting mean refers to the limiting law obtained from the generating function; no assertion about convergence of finite-size means is needed.

## Verification
The standalone `checker.py` enumerates every targetwise attacker assignment for \(1\le n\le5\) at \(p=2/5\) using exact rational weights (respectively \(2,9,64,625,7776\) assignments). For each it obtains the cyclic basin directly from pointer trajectories; independently enumerates stable subsets and compares their number with the parity-cycle formula; and compares every \(\Pr(U_n=k)\) with the closed expression using exact fractions. It also checks the \(n\)-independent identity \(\Pr(U_n=0)=\Pr(Z_n=1)=2/5\). These finite checks are not the proof of the limit.

## Relationship to prior work
Dung (1995) supplies the semantics. Xu and Luo (2026, first posted October 8) study the computational complexity of grounded and preferred semantics for computably finitary frameworks, not this probabilistic model. Finch (2022) studies complete uniform random mappings, for which no missing pointers occur, and does not state the parity-resolved limit under the fixed positive missing-pointer probability. Hansen and Jaworski (2006) study general random mapping component statistics; standard cycle-index and Poisson-assembly methods are deliberately reused here. Berg and Mutafchiev (1990) studied Lagrangian size distributions for a single-attracting-centre random mapping. Its detailed relationship to the finite undecided-size marginal is not fully resolved from accessible material, and independent priority is *not claimed* for the standard forest identity or the isolated size-marginal calculation. The proposed contribution is the explicit *joint* grounded-undecided-mass and parity-labelled stable-multiplicity law for the specified argumentation model. Prior one-attacker stable-extension classifications already determine \(Z_n\) from the cycle parity of a fixed graph; the joint random law is a different assertion.

## Limitations
This is restricted to one or zero independently chosen attacker per vertex with a fixed \(p\in(0,1)\), including self-attack. It does not cover correlated attacks, multiple attackers, or the critical regime \(p\to0\). Earlier probabilistic mapping papers could contain equivalent joint cycle-size and parity formulas under different terminology. An old attracting-centre paper was available only at abstract level, so that possible priority overlap remains a substantive residual risk. No external independent audit has been performed.

## References
1. P. M. Dung, "On the acceptability of arguments and its fundamental role in nonmonotonic reasoning, logic programming and n-person games", *Artificial Intelligence* **77** (1995), 321–357, DOI:10.1016/0004-3702(94)00041-X.
2. J. Xu and J. Luo, "Complexity of Grounded Semantics and Preferred Semantics in Finitary Argumentation Frameworks", arXiv:2610.12008 (first public October 8, 2026), https://arxiv.org/html/2610.12008v1.
3. S. Finch, "Components and Cycles of Random Mappings", arXiv:2205.05579 (2022), https://arxiv.org/html/2205.05579v1.
4. J. C. Hansen and J. Jaworski, "A new random mapping model", arXiv:math/0603529 (2006), https://arxiv.org/abs/math/0603529.
5. S. Berg and L. Mutafchiev, "Random mappings with an attracting center: Lagrangian distributions and a regression function", *Journal of Applied Probability* **27** (1990), 622–636, DOI:10.2307/3214546 (full text not inspected).
6. J. K. Fichte et al., "Diversity of Extensions in Abstract Argumentation", arXiv:2605.13332 (2026).
