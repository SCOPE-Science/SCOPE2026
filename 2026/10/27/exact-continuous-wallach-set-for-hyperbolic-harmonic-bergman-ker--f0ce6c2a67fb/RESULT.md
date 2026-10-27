# Exact continuous Wallach set for hyperbolic-harmonic Bergman kernels on the real four-ball

## Finding
Let \(I_m(s)\) be the meromorphically continued Peter–Weyl coefficients of the normalized weighted hyperbolic-harmonic Bergman norm on the real four-dimensional unit ball, with \(m\) ranging over all nonnegative integers and \(s\) real. Then the **entire continuous positive-coefficient Wallach set** is
\[
\boxed{\mathcal W_c^{(4)}=[-2,\infty)\,\cup\,(-4,-3).}
\]
In particular, the nonclassical interval \((-4,-3)\) consists entirely of positive-definite reproducing kernels, separated by \((-3,-2)\) from the component containing the usual weighted Bergman spaces. The endpoints \(-4\) and \(-3\) are poles, not continuous-Wallach parameters. This classification is distinct from the residue-based discrete Wallach set.

## Assumptions and scope
Work on the open unit ball \(B^4\subset\mathbb R^4\) with the Möbius-invariant hyperbolic Laplacian. For every integer \(m\geq0\), let \(\mathcal H^m\) be the degree-\(m\) spherical harmonics on \(S^3\), with normalized surface \(L^2\) norm. The degree-\(m\) hyperbolic-harmonic extension is \(r^m S_m(r^2)Y_m(\zeta)\), where
\[
 S_m(t)=\frac{m+2-mt}{2}.
\]
For \(s>-1\), the normalized radial squared-norm coefficient is
\[
 I_m(s)=\frac{\Gamma(s+3)}{\Gamma(s+1)}\int_0^1t^{m+1}(1-t)^s S_m(t)^2\,dt.
\]
The term \(I_0(s)\) is identically \(1\). Each coefficient has its unique meromorphic continuation. Define \(\mathcal W_c^{(4)}=\{s\in\mathbb R:0<I_m(s)<\infty\text{ for every integer }m\ge0\}\); a pole cannot enter this set by a residue prescription.

## Proof
For each integer \(m\ge1\), expand \(S_m(t)^2=((m+2)^2-2m(m+2)t+m^2t^2)/4\). Using the beta integral for \(s>-1\), combining the three terms over a common gamma denominator, and then continuing meromorphically gives the identity
\[
 \boxed{I_m(s)=\frac{\Gamma(m+3)\Gamma(s+3)}{4\Gamma(m+s+5)}\Big[m(s+2)(s+5)+2(s+3)(s+4)\Big].}\tag{1}
\]
This also follows by terminating the even-dimensional hypergeometric representation at its second summand; the novel issue here is the complete *simultaneous positivity* over all degrees and all real parameters.

If \(s\ge-2\), all gamma factors and the bracket in (1) are positive, including \(s=-2\) where \(I_m(-2)=1\). If \(-4<s<-3\), then \(\Gamma(s+3)<0\) and \(\Gamma(m+s+5)>0\); both \((s+2)(s+5)\) and \((s+3)(s+4)\) are negative. The bracket is strictly negative for every \(m\ge1\), so \(I_m(s)>0\) for all degrees.

Conversely, if \(-3<s<-2\) or \(-5<s<-4\), the gamma quotient in (1) is positive for every integer \(m\ge1\), while \((s+2)(s+5)<0\). The bracket becomes negative for all sufficiently large \(m\). Therefore those two open intervals are excluded. For each noninteger \(s<-5\), the degree-one coefficient simplifies to
\[
 I_1(s)=\frac{3(3s^2+21s+34)}{2(s+3)(s+4)(s+5)}<0.
\]
Indeed the denominator is negative and the numerator is positive for \(s<-5\). At every integer \(s=-k\) with \(k\ge3\), choose \(m=k+3\). Then \(\Gamma(m+s+5)=\Gamma(8)\) is finite, \(\Gamma(s+3)\) has a pole, and the bracket in (1) is nonzero: it equals \(-2m\) for \(k=3,4\), equals \(4\) for \(k=5\), and is positive for \(k\ge6\). Such parameters are excluded as genuine poles. These cases exhaust the real line and prove the classification.

For completeness, positivity of the angular coefficients supplies genuine positive-definite reproducing kernels on both components. For fixed admissible \(s\), (1) implies that \(I_m(s)^{-1}\) grows at most polynomially; for \(s\neq-2\) its large-degree growth is \(O(m^{s+1})\). The dimension of \(\mathcal H^m\) is \((m+1)^2\), while \(S_m(t)=O(m)\) uniformly for \(0\le t\le1\). Thus the spherical addition-kernel expansion converges normally for pairs of points in compact subsets of \(B^4\), because their radial factors decay geometrically. Positive coefficients yield the reproducing-kernel Hilbert completion; negative coefficients would violate positive definiteness on the corresponding spherical harmonic sector.

## Verification
The accompanying standalone `verify.py` independently compares 144 exact rational beta moments to (1), checks 144 evaluations of the terminating hypergeometric representation against (1) at positive and negative nonintegral parameters, and samples both admissible and excluded sign regimes. It also tests the exact \(s=-2\) identity for 40 degrees. The universal statement is proved by the preceding sign analysis, not by the finite checker. Run `python verify.py` with Python, SymPy and mpmath installed.

## Relationship to prior work
Blaschke, Engliš and Youssfi introduced the hyperbolic-harmonic Wallach problem and explicitly asked for the continuous set in their concluding Question 1. Their work supplies the Peter–Weyl radial decomposition and analytic continuation framework. Moravík's June 2026 paper proves a general hypergeometric coefficient representation in even dimensions (Proposition 3.2) and studies **discrete** Wallach sets and degree asymptotics. In dimension four, his formula terminates and is algebraically equivalent to (1). Neither inspected paper states or proves the exact continuous set \([-2,\infty)\cup(-4,-3)\). The closed coefficient expression itself is a specialization of prior general formulas and is not presented as a new independent theorem. The contribution is the complete simultaneous sign classification, with exact endpoints and exclusion witnesses for every remaining parameter.

## Limitations
This is a real-dimension-four classification only. It does not determine continuous Wallach sets in other dimensions, the discrete residue spaces, or Möbius invariance of every newly positive norm. The comparison is limited to the inspected primary texts and searchable claims; absence of a matching result is not proof of worldwide priority. Independent scientific audit has not been performed.

## References
1. Matěj Moravík, *Analytic continuation of weighted H-harmonic Bergman spaces*, arXiv:2606.19810, first public 2026-06-18, especially Proposition 3.2, Theorem 4.1, Proposition 5.1. https://arxiv.org/abs/2606.19810
2. Petr Blaschke, Miroslav Engliš, El-Hassan Youssfi, *A Moebius invariant space of H-harmonic functions on the ball*, arXiv:2404.07384, first public 2024-04-10, especially equations (3)–(5) and Concluding Remarks, Question 1. https://arxiv.org/abs/2404.07384
