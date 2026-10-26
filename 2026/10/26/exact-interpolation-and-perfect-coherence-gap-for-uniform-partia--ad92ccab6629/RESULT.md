# Exact interpolation and perfect-coherence gap for uniform partial-conjunction bounds

## Finding
Let \(I\) be a labeled set of \(n\) hypotheses, with integers \(1\le r\le k\le n\). Set \(d_0(S)=r\) for every \(k\)-element subset \(S\subseteq I\), and \(d_0(S)=0\) for all other subsets. Define interpolation
\[
(Td)(S)=\max_{U\subseteq I}\{d(U)-|U\setminus S|+d(S\setminus U)\},
\]
and let \(d_\infty\) be its eventual fixed point, obtained by repeated updates. Define the perfectly coherent envelope
\[
D(S)=\min_{J\subseteq I:\ |J\cap E|\ge r\ \text{for every }E\subseteq I,\ |E|=k}|J\cap S|.
\]
For every \(S\subseteq I\), put \(s=|S|=qk+t\), with \(q\ge0\) and \(0\le t<k\). Then **both operations have exact closed forms**:
\[
\boxed{d_\infty(S)=qr+\max\{0,t-(k-r)\}},\qquad
\boxed{D(S)=\max\{0,s-(k-r)\}}.
\]
In particular, when \(r<k\) and \(n=2k-r\), the full set has \(d_\infty(I)=r\) while \(D(I)=k\). Thus the improvement factor \(k/r\) is attainable and unbounded over allowed \(k,r\). For fixed \(k,r<k\) and increasing \(n\), the ratio \(D(I)/d_\infty(I)\) tends to \(k/r\), while the absolute difference grows linearly with \(n\).

## Assumptions and scope
The universe is finite and the initial lower bound has exactly the stated **complete uniform support**: each \(k\)-subset is certified to contain at least \(r\) false null hypotheses, with no initial positive bound recorded for any other cardinality. Here \(d_0\), \(T\), \(d_\infty\), and \(D\) are deterministic set functions conditional on that bound pattern being observed. Validity as a statistical confidence statement is preserved whenever the initial bounds hold simultaneously; the theorem concerns the exact combinatorial closure, not power or calibration of a particular test. For example, one may reject the global null that *some* \(k\)-subset contains fewer than \(r\) false hypotheses by a level-\(\alpha\) partial-conjunction test, and issue all \(k\)-subset bounds together only on rejection. This produces a simultaneous \(1-\alpha\) true-discovery guarantee. No independence of individual hypothesis tests is required for the deterministic formula.

## Proof
**1. Fixed-point upper bound.** For \(s\ge0\) define
\[
F(s)=\max_{m\in\mathbb Z_{\ge0}}\left[mr-(mk-s)_+\right],\qquad (x)_+=\max(x,0).
\]
Writing \(s=qk+t\), any \(m\le q\) gives at most \(qr\), attained at \(m=q\). For \(m\ge q+1\), the displayed expression equals \(s-m(k-r)\) and is largest at \(m=q+1\). Thus \(F(s)=qr+\max(0,t-(k-r))\), including \(r=k\). In particular \(F(0)=0\), \(F(s)\ge0\), and \(F(k)=r\).

Each function \(s\mapsto mr-(mk-s)_+\) is nondecreasing and \(1\)-Lipschitz, so their pointwise maximum \(F\) is too. Also \(F\) is superadditive: for any nonnegative \(a,b\) and integers \(m_1,m_2\ge0\),
\[
(m_1k-a)_++(m_2k-b)_+\ge ((m_1+m_2)k-a-b)_+,
\]
whence \(F(a)+F(b)\le F(a+b)\), by taking the two suprema and the candidate \(m_1+m_2\). For arbitrary \(U,S\subseteq I\), put \(a=|U\cap S|\), \(b=|U\setminus S|\) and \(c=|S\setminus U|\). The Lipschitz and superadditive properties give
\[
F(|U|)-|U\setminus S|+F(|S\setminus U|)
=F(a+b)-b+F(c)\le F(a)+F(c)\le F(|S|).
\]
Taking \(U=\varnothing\) achieves equality, proving that the set function \(S\mapsto F(|S|)\) is a fixed point of \(T\). It majorizes \(d_0\), so monotonicity of \(T\) gives \(d_\infty(S)\le F(|S|)\).

**2. Attainment by repeated interpolation.** Let \(f=d_\infty\). By construction, \(f\ge d_0\), \(Tf=f\), and \(f(\varnothing)=0\). The interpolation identity implies three elementary rules: \(f(A\cup B)\ge f(A)\); \(f(B\setminus A)\ge f(B)-|A\cap B|\); and consequently
\[
f(A\cup B)\ge f(A)+f(B)-|A\cap B|.
\]
(The first takes \(U=A\), \(S=A\cup B\); the second takes \(U=B\), \(S=B\setminus A\); combine the first interpolation step with the second for \(B\setminus A\).) If \(s<k\), extend \(S\) to a \(k\)-set \(E\) and obtain \(f(S)\ge f(E)-(k-s)\ge r-(k-s)\), while \(f(S)\ge0\). This equals \(F(s)\).

If \(s\ge k\), partition \(qk\) of the \(s=qk+t\) elements of \(S\) into \(q\) disjoint \(k\)-sets. Their union has \(f\)-value at least \(qr\) by the preceding union rule. If \(t>k-r\), select one more \(k\)-set inside \(S\), consisting of all \(t\) unused elements and \(k-t\) elements from the already covered union. Such a choice exists because \(q\ge1\). The union inequality increases the certified value by at least \(r-(k-t)=t-(k-r)\). Hence \(f(S)\ge F(s)\), and equality follows from Step 1.

**3. Perfect coherence.** Let \(J\) be feasible in the minimization defining \(D\) and \(Z=I\setminus J\). All \(k\)-sets contain at least \(r\) elements of \(J\) if and only if \(|Z|\le k-r\). The forward implication holds because \(|Z|\ge k-r+1\), together with \(n\ge k\), permits choosing a \(k\)-set containing at least \(k-r+1\) elements of \(Z\); the converse follows directly. Thus \(D(S)=\min_{|Z|\le k-r}|S\setminus Z|=\max(0,|S|-(k-r))\), achieved by choosing as much of \(Z\) inside \(S\) as possible.

**4. Sharp gap.** With \(n=2k-r\), \(k>r\), the decomposition \(n=k+(k-r)\) gives \(d_\infty(I)=r\), while \(D(I)=k\). For fixed \(k,r\), the explicit formulas yield \(d_\infty(I)=(r/k)n+O(1)\) and \(D(I)=n+O(1)\). Taking \(r=1\) and arbitrarily large \(k\) gives an unbounded exact multiplicative advantage.

## Verification
The complete elementary argument above applies to every allowable \(n,k,r,S\); enumeration is not the proof. The accompanying standalone `verify.py` uses integer arithmetic and directly iterates \(T\) on all subsets, independently enumerates every feasible model \(J\), and checks both formulas for **all** \(1\le n\le7\), \(1\le r\le k\le n\), and \(S\subseteq I\). The executable reports **5,630 individual subset comparisons passed**. Run `python3 verify.py` from the directory containing that file.

## Relationship to prior work
Tran, Leung, and Hemerik [1] define repeated interpolation and perfect coherence, demonstrate a single \(n=3,k=2,r=1\) strict gap (their Example 3.1 and Appendix A), prove equality when the support-incidence matrix is totally unimodular (Theorem 3), and identify the closed-testing representation (Theorem 5). The special \(3,2,1\) instance is **already published**; the new assertion is the all-parameter pointwise classification and arbitrarily large exact gap. The complete uniform incidence family is neither nested nor forest-structured in general, and Theorem 3 is only an equality criterion, not a covering characterization. Blanchard, Neuvial, and Roquain [2] develop optimal post-hoc bounds and computational properties for reference families; Goeman, Hemerik, and Solari [3] establish the general admissibility of closed testing. Those general frameworks underpin the definitions but, in the inspected relevant portions, do not give the pair of formulas for all \(n,k,r,S\). The maximization formula for \(D\) is a direct specialization of known general principles; the novel structural comparison is the exact behavior of **iterated** interpolation and its gap over the entire complete-uniform family.

## Limitations
This is a deterministic finite-set theorem. The family contains *all* \(k\)-subsets with the **same** lower bound; arbitrary uneven bounds or missing subsets are not classified. The results do not quantify test power or computational cost of producing the starting constraints, and no claim is made that the basic interpolation or maximization operators are new. An implicit formulation in older integer-covering or closed-testing literature cannot be categorically excluded; no independent scientific audit has been performed.

## References
[1] N. Tran, D. Leung, and J. Hemerik, "Interpolation and coherence in multiple testing," arXiv:2610.18205v1 (2026), Sections 2–3 and Appendices A–D. https://arxiv.org/abs/2610.18205
[2] G. Blanchard, P. Neuvial, and E. Roquain, "Post hoc confidence bounds on false positives using reference families," Annals of Statistics 48 (2020), 1281–1303; earlier arXiv:1703.02307, especially Section 2 and Proposition 2.5. https://arxiv.org/abs/1703.02307
[3] J. Goeman, J. Hemerik, and A. Solari, "Only closed testing procedures are admissible for controlling false discovery proportions," Annals of Statistics 49 (2021), 1218–1238. https://doi.org/10.1214/20-AOS1999
