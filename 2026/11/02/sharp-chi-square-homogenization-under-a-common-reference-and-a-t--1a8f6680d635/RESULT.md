# Sharp chi-square homogenization under a common reference and a two-experiment divergence budget

## Finding

Let \(P_1,P_2\) be probability laws absolutely continuous with respect to a **common** reference probability law \(Q\), with finite Pearson chi-square divergences. Put \(\overline P=(P_1+P_2)/2\) and, whenever the denominator is positive, define
\[
R=\frac{\chi^2(\overline P^{\otimes 2}\Vert Q^{\otimes 2})}{\chi^2(P_1\otimes P_2\Vert Q^{\otimes 2})}.
\]
For every real budget \(T>0\), the **exact**, attained supremum of \(R\) over all such triples \((P_1,P_2,Q)\), on arbitrary measurable spaces, with \(\chi^2(P_1\Vert Q)+\chi^2(P_2\Vert Q)\le T\), is
\[
\boxed{C(T)=\begin{cases}1,&0<T\le2,\\\dfrac{\frac12(T+2t_T)+\frac1{16}(T+2t_T)^2}{T+t_T^2},&T>2,\end{cases}\qquad t_T=\frac{\sqrt{T(T+16)}-T}{4}.}
\]
In particular \(C(T)>1\) exactly for \(T>2\), with critical onset \(C(2+\delta)=1+\delta^2/36+O(\delta^3)\) as \(\delta\downarrow0\). Thus two heterogeneous experiments with a shared reference cannot increase chi-square divergence under homogenization when their total original marginal chi-square budget is at most \(2\); above this threshold amplification is possible and the exact worst-case amplification is given above.

For \(0<T\le2\), equality \(R=C(T)\) holds exactly when \(P_1=P_2\ne Q\). For \(T>2\), equality requires the full budget and positively collinear, unequal likelihood-score functions; more precisely, after possibly interchanging indices, their \(L^2(Q)\) norms \(a>b>0\) satisfy \(a^2+b^2=T\), \(ab=t_T\) and \(\mathrm dP_i/\mathrm dQ=1+a_i h\) for one mean-zero, unit-variance function \(h\), with \((a_1,a_2)=(a,b)\). Every equality pattern can be realized on a **binary observation alphabet**, with both likelihoods strictly positive.

## Assumptions and scope

Pearson divergence is \(\chi^2(P\Vert Q)=\int (\mathrm dP/\mathrm dQ-1)^2\,\mathrm dQ\), assumed finite. Only two product factors are considered; both baseline measures are the same \(Q\). The constraint \(T>0\) is on the **sum** of the two marginal chi-square divergences, not on the product divergence. We exclude the degenerate denominator-zero case \(P_1=P_2=Q\) from the ratio; the corresponding divergence inequality remains true as \(0\le0\). The theorem holds for arbitrary real \(T\), not only integer budgets, and arbitrary common measurable spaces.

## Proof

Write \(u_i=\mathrm dP_i/\mathrm dQ-1\in L^2(Q)\), so \(\mathbb E_Q u_i=0\). Let \(a=\|u_1\|_2\), \(b=\|u_2\|_2\), \(s=a^2+b^2\), \(t=ab\), and, when \(t>0\), \(c=\langle u_1,u_2\rangle/(ab)\in[-1,1]\). When \(t=0\), set \(c=1\) purely for the formulas. Product likelihoods and independent mean-one factors give the exact identities
\[
D_{\mathrm{original}}=\chi^2(P_1\otimes P_2\Vert Q^{\otimes2})=s+t^2,
\qquad
D_{\mathrm{hom}}=\left(1+\frac{s+2tc}{4}\right)^2-1.
\]
Here \(s>0\), \(0\le t\le s/2\), and \(c\le1\). For fixed \((s,t)\), the latter expression is largest at \(c=1\), with equality if the nonzero score vectors are positively proportional. Thus
\[
R\le r(s,t):=\frac{(s+2t)/2+(s+2t)^2/16}{s+t^2}.
\]
The exact **geometric deficit** is
\[
D_{\mathrm{hom}}-D_{\mathrm{original}}
=\frac{(s-2t)(s+6t-8)}{16}
-\frac{t(1-c)[4+s+t(1+c)]}{4}.
\]
This identity follows by expanding the two product moments and factoring the difference at \(c=1\). Since \(s-2t=(a-b)^2\ge0\), if \(s\le2\), then \(s+6t-8\le4s-8\le0\): amplification is impossible, and equality requires \(a=b>0\) and \(c=1\), equivalently \(P_1=P_2\ne Q\).

To optimize at a general budget, set \(\alpha=t/s\in[0,1/2]\). Then
\[
r(s,\alpha s)=\frac{(1+2\alpha)/2+s(1+2\alpha)^2/16}{1+s\alpha^2},
\quad
\frac{\partial}{\partial s}r(s,\alpha s)=\frac{(1+2\alpha)(1-2\alpha)(1+4\alpha)}{16(1+s\alpha^2)^2}\ge0.
\]
For \(\alpha<1/2\), this derivative is strictly positive, while \(\alpha=1/2\) gives \(r=1\). Hence the supremum under \(s\le T\) is obtained by maximizing \(r(T,t)\) for \(0\le t\le T/2\). Direct differentiation yields
\[
\frac{\partial}{\partial t}r(T,t)=
\frac{(T+4)(2T-Tt-2t^2)}{8(T+t^2)^2},
\]
so the unconstrained positive maximizer is the unique root \(t_T=(\sqrt{T(T+16)}-T)/4\). It belongs to \([0,T/2]\) exactly for \(T\ge2\). If \(0<T\le2\), the maximum is at \(t=T/2\) and equals \(1\). If \(T>2\), the unique constrained maximizer is \(t=t_T<T/2\) and its ratio is the displayed \(C(T)>1\). The factorized deficit gives strict positivity, and Taylor expansion at \(T=2\) gives the stated \(\delta^2/36\) onset. Equality conditions follow from the strict derivative and Cauchy–Schwarz equality.

It remains to prove attainability on two atoms. Given desired \(a,b\ge0\), choose any integer \(m>\max\{a,b\}\), set \(Q(1)=1/(1+m^2)\), \(Q(0)=m^2/(1+m^2)\), and let \(h(1)=m\), \(h(0)=-1/m\). Then \(\mathbb E_Qh=0\), \(\mathbb E_Qh^2=1\), and \(1+ah\), \(1+bh\) are strictly positive \(Q\)-densities. Taking \(\mathrm dP_1/\mathrm dQ=1+ah\), \(\mathrm dP_2/\mathrm dQ=1+bh\) makes \(c=1\) and realizes every stated maximizing configuration. When \(T>2\), the positive \(a>b\) satisfying \(a^2+b^2=T\), \(ab=t_T\) exist because \(0<t_T<T/2\), and the common-sign construction completes the proof.

## Verification

The accompanying `verify.py` is standalone Python 3 and checks the rational two-atom construction directly, with independent tensor-sum evaluation rather than reusing the closed product formula. It also checks the exact algebraic deficit and a sample of budget monotonicity and critical-onset values. Run `python3 verify.py`; expected output is provided as `verification_output.txt`. These finite tests are cross-checks of formulas, not substitutes for the universal Hilbert-space argument and calculus proof.

## Relationship to prior work

Kontorovich, *A local-to-global principle for \(f\)-divergence homogenization* (arXiv:2610.31164v1, first publicly posted 2026-10-22), Theorem 2.1 and Section 7.4, shows that no **unrestricted** uniform homogenization constant exists for chi-square divergence and supplies a binary two-observation counterexample with **unequal** reference laws. That negative result does not give a sharp constrained comparison with a **common** reference and a fixed total chi-square budget. The present exact budget threshold, the complete worst-case constant, and its binary extremizer are additional constrained statements; the well-known chi-square product identity is explicitly used as a starting point rather than claimed as new. General results on divergence tensorization and data processing provide background but do not by themselves identify this phase boundary or the optimizing likelihood configuration.

## Limitations

The result is restricted to two experiments and a common baseline measure; it is not a universal chi-square homogenization inequality for arbitrary unequal reference laws or arbitrary numbers of factors. The ratio is undefined when both original experiments equal the reference, although the divergence inequality remains trivial. The result concerns Pearson chi-square divergence, not total variation, KL, or all \(f\)-divergences. No independent audit of the mathematical proof or exhaustive historical-priority search has been performed; the possibility of an implicit classical sharp two-factor inequality remains a residual originality risk.

## References

1. Aryeh Kontorovich, *A local-to-global principle for \(f\)-divergence homogenization*, arXiv:2610.31164v1, 2026-10-22, https://arxiv.org/html/2610.31164v1. In particular, Sections 2, 5 and 7.4.
2. A. Kontorovich, *A homogenization principle for total variation*, arXiv:2604.03882, 2026, https://arxiv.org/abs/2604.03882 (related, different divergence).
3. C. Cressie and T. R. C. Read, *Multinomial goodness-of-fit tests*, J. R. Statist. Soc. B 46 (1984), 440–464 (classical divergence family; no priority claim for the result above).
