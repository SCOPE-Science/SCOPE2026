# A cycle-cancellation sieve for nilpotent centralizers in symmetric inverse monoids

## Finding

Let \(\mathcal I_n\) be the symmetric inverse monoid of partial injective transformations of a labeled \(n\)-point set, including the empty transformation. Let \(\alpha\in\mathcal I_n\) be nilpotent, so its directed functional graph is a disjoint union of chains. Write \(\lambda=(\lambda_1,\ldots,\lambda_c)\) for their positive numbers of **vertices**, with \(\sum_i\lambda_i=n\). Define the rank polynomials

\[
C_\lambda(t)=\sum_{\substack{\beta\in\mathcal I_n\\\alpha\beta=\beta\alpha}}t^{\operatorname{rank}\beta},\qquad
N_\lambda(t)=\sum_{\substack{\beta\in\mathcal I_n\\\alpha\beta=\beta\alpha\\\beta\text{ nilpotent}}}t^{\operatorname{rank}\beta}.
\]

For positive integers \(a,b\), set \(W_{a,b}(t)=t+t^2+\cdots+t^{\min(a,b)}\). Then \(C_\lambda(t)\) is the weighted partial-permutation (rook) polynomial

\[
C_\lambda(t)=\sum_{k=0}^{c}\ \sum_{\substack{I,J\subseteq[c]\\|I|=|J|=k}}\ \sum_{\sigma:I\overset{\sim}{\longrightarrow}J}\ \prod_{i\in I}W_{\lambda_i,\lambda_{\sigma(i)}}(t).
\tag{1}
\]

The new nilpotent sieve substantially simplifies exclusion of directed cycles. Let \(H\) be the set of distinct parts of \(\lambda\), and let \(m_h=\#\{i:\lambda_i=h\}\). For \(T\subseteq H\), write \(\lambda\setminus T\) for the list obtained by deleting **one** part equal to each \(h\in T\). Then

\[
\boxed{
N_\lambda(t)=\sum_{T\subseteq H}(-1)^{|T|}
\left(\prod_{h\in T}m_h t^h\right)C_{\lambda\setminus T}(t).
}
\tag{2}
\]

This formula holds for every nilpotent partial bijection in every finite degree, including isolated vertices as chains of size one; the empty-list conventions are \(C_\varnothing(t)=N_\varnothing(t)=1\).

An especially transparent consequence concerns \(c\) chains of a common vertex-length \(L\). Put \(w_L(t)=t+\cdots+t^L\). Then the exponential generating functions in the **number of chains** are

\[
\boxed{
\begin{aligned}
\sum_{c\ge0}C_{(L^c)}(t)\frac{z^c}{c!}
 &=\frac{\exp\!\left(z/(1-w_L(t)z)\right)}{1-w_L(t)z},\\
\sum_{c\ge0}N_{(L^c)}(t)\frac{z^c}{c!}
 &=\frac{1-t^Lz}{1-w_L(t)z}\exp\!\left(\frac{z}{1-w_L(t)z}\right).
\end{aligned}}
\tag{3}
\]

Consequently the number of **nonnilpotent** centralizing partial bijections of a specified rank obeys the exact rank-shift identity

\[
\boxed{[t^r]\big(C_{(L^c)}(t)-N_{(L^c)}(t)\big)
=c\,[t^{r-L}]C_{(L^{c-1})}(t),}
\tag{4}
\]

where coefficients with negative degree vanish. This is valid for all positive integers \(c,L\); the previously studied case \(L=1\) is included only as a consistency boundary. At \(t=1\), the total centralizer size is

\[
C_{(L^c)}(1)=\sum_{k=0}^c\binom ck^2 k! L^k,
\]

and the nilpotent count equals \(C_{(L^c)}(1)-c\,C_{(L^{c-1})}(1)\).

## Assumptions and scope

Composition of partial maps uses ordinary functional composition (either consistently chosen left-to-right or right-to-left); commutation is independent of that convention. The rank is the cardinality of a partial map's domain. Nilpotent means that some positive power is the empty map, equivalently that the directed functional graph has no cycles. A chain of vertex-length \(L\) has \(L-1\) directed edges; singleton chains are retained. The coefficients of all displayed series are formal integers, not analytic convergence statements. A distinct-part set \(H\) is used in (2), whereas each multiplicity \(m_h\) counts labeled chains of its length. Statements concern labeled partial bijections, not similarity or conjugacy orbits.

## Proof

**Commuting-chain normal form.** Write chain \(i\) as \(x_{i,0}\mapsto x_{i,1}\mapsto\cdots\mapsto x_{i,\lambda_i-1}\), with the last map undefined. Suppose \(\alpha\beta=\beta\alpha\). If \(x_{i,j}\) is in the domain of \(\beta\), then so are all preceding \(x_{i,a}\) with \(a<j\): commutation at each predecessor forces this. Thus the domain of \(\beta\) on chain \(i\) is either empty or an initial segment of some vertex-length \(s\ge1\). Its successive images under \(\beta\) lie in one target chain in consecutive order, and its final image must be terminal; otherwise commutation would force the next source point to be in the domain. Hence the image is exactly the terminal segment of some target chain \(j\), of the same length \(s\le\min(\lambda_i,\lambda_j)\). Conversely any such choice satisfies commutation. As terminal segments in a given target chain overlap, injectivity permits at most one source chain per target chain. We therefore obtain a unique partial injection \(i\mapsto j\) on the set of chain labels and, for each chosen edge, a length \(s\) from \(1\) through \(\min(\lambda_i,\lambda_j)\). The contribution to \(\operatorname{rank}\beta\) is \(s\). This proves (1).

**Which chain-label cycles cause nonnilpotence?** The chain-label partial injection is a disjoint union of directed paths and directed cycles. An edge \(i\to j\) of selected prefix length \(s\) sends the position \(a\) (counting from zero) to position \(a+\lambda_j-s\) in target chain \(j\), whenever defined. Each such increment is nonnegative. Along a directed cycle of chain labels, the net increment is zero only when every edge has \(s=\lambda_j\). Because also \(s\le\lambda_i\), traversing the cycle forces all lengths \(\lambda_i\) on that cycle to be equal and every selected length to be the full common length. Such a cycle yields genuine cycles of \(\beta\) on the underlying vertices. All other chain-label cycles increase position strictly on at least one edge, so iteration must eventually become undefined. Directed paths necessarily terminate. Thus \(\beta\) is nilpotent exactly when it has **no fully aligned equal-length chain-label cycle**.

**Signed cycle cancellation.** Apply inclusion-exclusion to the finite collection of possible fully aligned directed cycles (including loops). A chosen family of pairwise vertex-disjoint cycles occupies a subset \(S\) of chain labels, carries rank weight \(t^{\sum_{i\in S}\lambda_i}\), and leaves a completely arbitrary commuting partial injection on the complementary chains, counted by \(C_{\lambda\setminus S}(t)\). All selected cycles must preserve chain length. For a fixed selected subset of \(s\) labels of the same length, the sum over permutations of those labels, with sign \((-1)^{\text{number of cycles}}\), equals

\[
\sum_{\pi\in S_s}(-1)^{\#\mathrm{cycles}(\pi)}
=(-1)(0)(1)\cdots(s-2),
\]

which is \(1\) for \(s=0\), \(-1\) for \(s=1\), and zero for every \(s\ge2\). The product over distinct chain lengths therefore vanishes unless at most one label of each length is selected. Selecting one from a length class of size \(m_h\) gives precisely the factor \(m_h\). The surviving terms give (2) without any assumption that the chain lengths are equal.

**Uniform chains.** For \(\lambda=(L^c)\), every edge of the chain-label partial injection has independent weight \(w_L(t)\). A directed path component on \(k\ge1\) labeled chain indices contributes \(w_L(t)^{k-1}\) and has \(k!\) possible linear orders. A directed cycle component on \(k\ge1\) indices has \((k-1)!\) cyclic orders and weight \(w_L(t)^k\) if unrestricted, or \(w_L(t)^k-t^{Lk}\) when nilpotent partial maps alone are admitted. The exponential formula for sets of directed paths and directed cycles therefore gives the two equalities in (3), since

\[
\exp\left(\sum_{k\ge1}\frac{\big(w_L(t)^k-t^{Lk}\big)z^k}{k}\right)
=\frac{1-t^Lz}{1-w_L(t)z}.
\]

Multiplying the full centralizer generating function by \(1-t^Lz\) proves (4). Alternatively, (4) follows immediately from (2), because the distinct-length set for uniform chains contains only \(L\). Specializing the full centralizer rook polynomial at \(t=1\) gives the stated finite sum.

## Verification

The accompanying standalone Python programs use only the standard library. `general_verify.py` independently enumerates every partial injection, composes actual point maps, and classifies nilpotence by absence of directed cycles. For **every partition of each size \(1\) through \(6\)** it compares every rank coefficient with both the weighted matching recurrence and the signed cancellation formula. For partitions of sizes \(7\) through \(11\) with at most five parts, it independently compares the signed cancellation formula with an enumeration of decorated chain-label matchings. The separate `verify.py` derives the uniform bivariate exponential generating function by rational polynomial arithmetic and checks it against direct point-map enumeration and an independent matching enumerator for selected cases up to six vertices; it checks additional uniform pairs algebraically. All these checks completed successfully. They corroborate the proof; finite experiments are not evidence for infinitely many partitions by themselves.

## Relationship to prior work

Konieczny's 2012 characterization (Theorem 3.4, particularly its chain clause) gives a general structural criterion for partial bijections commuting with a given partial bijection. That result is the structural foundation for (1), and the present result does not claim a new characterization of *which* individual partial maps commute. Gomes and Howie (1987) characterize nilpotent partial bijections as unions of chains. Laradji and Umar (2004) enumerate nilpotent partial transformations and partial injections without conditioning on commutation with a specified nilpotent element. Those unconditional counts include the \(L=1\) boundary but do not specify the multitype rank-refined signed cycle sieve (2) or the uniform rank-shift identity (4). The independent contribution assessed here is the counting and cancellation theorem for the intersection of these two conditions, with the natural rank grading. A later paper by Konieczny (2020) studies the Green-relation structure of finite centralizers; its full text was not obtained, leaving a material priority risk. Searches found no exact prior statement of (2) or (4), but search failure alone cannot establish priority.

## Limitations

The result applies only when the fixed transformation \(\alpha\) is nilpotent; cycles in the fixed map are not covered. It counts labeled partial bijections, not isomorphism classes or their multiplication table, and does not classify centralizer Green's relations. For nonuniform chain lengths the sum (2) is an exact finite formula, not necessarily a closed product. An equivalent formula could be implicit in earlier literature, especially in more recent centralizer work not available for full-text comparison. Independent mathematical validation has not been performed.

## References

1. J. Konieczny, *Centralisers in the Infinite Symmetric Inverse Semigroup*, Bulletin of the Australian Mathematical Society 87 (2013), 462–479; first available online 28 September 2012. DOI: 10.1017/S0004972712000779. Full paper: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/154EF2A9346132686853C8D32F78737F/S0004972712000779a.pdf/centralisers_in_the_infinite_symmetric_inverse_semigroup.pdf.
2. G. M. S. Gomes and J. M. Howie, *Nilpotents in Finite Symmetric Inverse Semigroups*, Proceedings of the Edinburgh Mathematical Society 30 (1987), 383–395. DOI: 10.1017/S0013091500026778. Full paper: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F9FD0F5C89C4C7A773997A82CF5BC168/S0013091500026778a.pdf/nilpotents_in_finite_symmetric_inverse_semigroups.pdf.
3. A. Laradji and A. Umar, *On the Number of Nilpotents in the Partial Symmetric Semigroup*, Communications in Algebra 32 (2004), 3017–3023. DOI: 10.1081/AGB-120038637. Publisher listing: https://www.tandfonline.com/doi/abs/10.1081/AGB-120038637.
4. J. Konieczny, *The Structure of Centralizers in the Finite Symmetric Inverse Semigroup*, Communications in Algebra 48 (2020), 5181–5194. DOI: 10.1080/00927872.2020.1782926. Publisher listing: https://www.tandfonline.com/doi/abs/10.1080/00927872.2020.1782926.
