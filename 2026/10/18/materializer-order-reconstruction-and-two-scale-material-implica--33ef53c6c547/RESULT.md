# Materializer order reconstruction and two-scale material-implication loss in Boolean--chain Heyting algebras

## Finding

For integers \(n,k\geq1\), let \(H_{n,k}\) be the Heyting algebra obtained by adjoining \(k\) new elements \(t_1<\cdots<t_k\) above the Boolean algebra \(\mathcal B_n=\mathcal P([n])\). Write \(T=t_k\), \(b=2^n\), and \(N=b+k\). For \(a\in H_{n,k}\) define its **materializer** by
\[
\mathcal M(a)=\{c\in H_{n,k}:a\to c=\neg a\vee c\}.
\]
The complete materializer family is
\[
\begin{aligned}
\mathcal M(\varnothing)&=H_{n,k},\\
\mathcal M(A)&=\{B\subseteq[n]: A\not\subseteq B\}\cup\{T\}, &&\varnothing\ne A\subseteq[n],\\
\mathcal M(t_i)&=\mathcal B_n\cup\{t_1,\ldots,t_{i-1}\}\cup\{T\},&&1\le i\le k.
\end{aligned}
\]
The assignment \(a\mapsto\mathcal M(a)\), restricted to \(H_{n,k}\setminus\{\varnothing\}\), is an order isomorphism onto the set of distinct materializers ordered by inclusion; the only collision for all antecedents is \(\mathcal M(\varnothing)=\mathcal M(T)\).

The full size-distribution polynomial is
\[
\sum_{a\in H_{n,k}}z^{|\mathcal M(a)|}
=z^N+\sum_{r=1}^n\binom nr z^{b+1-2^{n-r}}+\sum_{i=1}^k z^{b+i}.
\]
Consequently, for independent uniform \(a,c\in H_{n,k}\), the exact degree of satisfaction of material implication is
\[
\Pr(a\to c=\neg a\vee c)
=1-\frac{3^n-2^n+(2^n-1)(k-1)+\binom{k}{2}}{(2^n+k)^2}.
\]
As \(n\to\infty\), if \(k=o(2^n)\), its failure probability is asymptotic to \((3/4)^n+k/2^n\), exhibiting a crossover at \(k\asymp(3/2)^n\). If \(k/2^n\to\lambda\in[0,\infty)\), the satisfaction probability tends to \(\frac12+\frac1{2(1+\lambda)^2}\); if \(k/2^n\to\infty\), it tends to \(1/2\).

## Assumptions and scope

The Boolean part \(\mathcal B_n\) has its usual inclusion order, bottom \(\varnothing\), and largest old element \([n]\). Every old element is below every newly adjoined \(t_i\), which form a strict chain. Meet and join extend the Boolean operations by this order; the finite distributive lattice has its uniquely determined Heyting residual \(a\to c=\max\{d:d\wedge a\le c\}\). The top \(T\) is not the old Boolean top \([n]\). All assertions hold for every integer \(n,k\ge1\), and the asymptotic assertions allow arbitrary integer-valued sequences \(k=k_n\ge1\).

## Proof

**Residual and negation.** The Heyting residual is defined by its adjunction. In particular \(a\to c=T\) exactly when \(a\le c\). For \(A,B\in\mathcal B_n\) with \(A\not\subseteq B\), no new element \(t_i\) can satisfy \(t_i\wedge A\le B\), since \(t_i\wedge A=A\). Therefore the maximal admissible element is the Boolean residual \(([n]\setminus A)\cup B\). For nonempty \(A\in\mathcal B_n\), this also implies \(\neg A=[n]\setminus A\), while \(\neg\varnothing=T\). For \(a=t_i\), the meet with any \(d\le t_i\) equals \(d\); hence \(t_i\to c=c\) if \(c<t_i\) and \(t_i\to c=T\) if \(c\ge t_i\). Thus \(\neg t_i=\varnothing\).

**Materializer membership.** For nonempty old \(A\), any old \(B\) with \(A\not\subseteq B\) satisfies \(A\to B=([n]\setminus A)\cup B=\neg A\vee B\). If \(A\subseteq B\), then \(A\to B=T\) while \(\neg A\vee B\) remains old, so the equality fails. Among new targets \(t_i\), the equality holds exactly for \(i=k\): the residual is \(T\), whereas the material expression is \(t_i\). If the antecedent is \(t_i\), then \(\neg t_i=\varnothing\); equality holds for all \(c<t_i\) and for \(c=T\), but fails for \(t_i\le c<T\). Finally, the antecedent \(\varnothing\) gives residual \(T\) and material expression \(T\) for every target. These are precisely the three displayed materializer formulas.

**Order reconstruction.** For nonempty old \(A,A'\), complementing their Boolean principal upper sets gives \(\mathcal M(A)\subseteq\mathcal M(A')\) exactly when \(A\subseteq A'\). The formulas give \(\mathcal M(t_i)\subseteq\mathcal M(t_j)\) exactly when \(i\le j\). Every old nonempty materializer is a proper subset of every new-level materializer, because it omits the old target \(A\), while all new-level materializers contain every old target. In the opposite direction no new-level materializer can be included in an old one. This proves an order isomorphism on the nonzero part. The only repeated materializer is the full set, attained at \(\varnothing\) and \(T\).

**Rank polynomial and exact failure count.** If \(|A|=r\ge1\), then exactly \(2^{n-r}\) Boolean targets contain \(A\); also the \(k-1\) new non-top targets fail, so \(|\mathcal M(A)|=b+1-2^{n-r}\). For \(t_i\), exactly \(k-i\) targets fail, so \(|\mathcal M(t_i)|=b+i\). There are \(\binom nr\) old antecedents of cardinality \(r\), and the bottom materializer has size \(N\); this proves the rank polynomial. Summing failure counts over all antecedents yields
\[
\sum_{r=1}^n\binom nr2^{n-r}+(b-1)(k-1)+\sum_{i=1}^k(k-i)
=3^n-2^n+(b-1)(k-1)+\binom{k}{2},
\]
where the first identity is the binomial theorem. Divide by \(N^2\).

**Two-scale asymptotics.** Put \(\delta_{n,k}=1-\Pr(a\to c=\neg a\vee c)\). If \(k=o(b)\), the exact numerator divided by \(b^2\) differs from \((3/4)^n+k/b\) by a quantity that is \(o((3/4)^n+k/b)\): the terms of order \(1/b\) are negligible compared to \((3/4)^n\), and the quadratic term of order \((k/b)^2\) is negligible compared to \(k/b\). This proves the asserted asymptotic equivalent; equality of its two leading terms occurs at \(k\asymp(3/2)^n\). When \(k/b\to\lambda<\infty\), divide numerator and denominator by \(b^2\) and use \(3^n/4^n\to0\), obtaining failure limit \((\lambda+\lambda^2/2)/(1+\lambda)^2\). Its complement simplifies to the displayed satisfaction limit. For \(k/b\to\infty\), division by \(k^2\) gives failure limit \(1/2\).

## Verification

Run `python verify.py` with a standard Python 3 interpreter. It computes the Heyting residual using the defining meet-adjunction on all \(H_{n,k}\) with \(1\le n,k\le5\), independently constructs each materializer, and checks every membership formula, the inclusion-order reconstruction, rank multiplicities, and the exact failure count. It also tests the residual adjunction for every triple in each finite case. The recorded output is `VERIFY_OK exhaustive_parameter_pairs=25 evaluated_input_pairs=8955`. These finite checks corroborate but do not replace the general proof.

For example, \(H_{2,3}\) has seven elements and fourteen failing ordered pairs, giving satisfaction degree \(5/7\). Its materializer-size polynomial is \(2z^7+z^6+z^5+z^4+2z^3\).

## Relationship to prior work

Bumpus and Kocsis introduced the materializer \(\mathcal M_H(a)\) and recorded basic closure and uniqueness properties. Their arXiv preprint first appeared on 2021-10-21; the revised paper's Sections 3.13--3.15 exhibit the one-new-top family \(H_{n,1}\) to show absence of a finite satisfiability gap for material implication, using an inequality instead of an exact count. The same paper's Section 2.18 uses repeated top adjunction for other, one-variable equations. Thus the materializer definition, the family with one new top, and the no-gap conclusion are prior results, **not** independent contributions here.

The present result identifies every materializer, recovers their inclusion order, gives the entire size spectrum and exact two-variable satisfiability degree for arbitrary positive chain length, and resolves the two separate asymptotic crossover scales. The formulas refine, rather than contradict, the earlier lower bound. The available related mathematical records contained results on other implication operations and team semantics but did not imply the antecedent-specific materializer-order theorem.

## Limitations

The theorem is restricted to Boolean algebras with a chain of new top elements, not arbitrary finite Heyting algebras. Its order-reconstruction statement is not asserted for a general Heyting algebra. The asymptotic statements assume \(n\to\infty\); no assertion of a sharp probabilistic threshold on random Heyting algebras is made. Prior results might contain these formulas implicitly under another terminology; independent literature priority and external proof audit remain unverified.

## References

1. Benjamin Merlin Bumpus and Zoltan A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, arXiv:2110.11515 (first posted 2021-10-21; version 3, 2024-01-04), Sections 1.11, 2.18, and 3.13--3.16. https://arxiv.org/abs/2110.11515
2. Benjamin Merlin Bumpus and Zoltan A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, *Journal of Symbolic Logic* (online 2024-01-09), DOI:10.1017/jsl.2024.2. https://doi.org/10.1017/jsl.2024.2
