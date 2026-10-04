# Lattice-segment factors preserve Ehrhart \(h^*\)-log-concavity
## Finding
Let \(P\) be a \(d\)-dimensional lattice polytope with \(h_P^*(t)=\sum_{i=0}^{s}h_i t^i\) log-concave with no internal zeros, and let \(m\ge1\) be an integer. Put \(h_i=0\) outside \(0\le i\le s\). Then the Ehrhart \(h^*\)-polynomial of \(P\times[0,m]\) has coefficients \[g_i=(1+mi)h_i+\bigl(m(d+2-i)-1\bigr)h_{i-1}\qquad(0\le i\le d+1),\] and \((g_i)\) is log-concave with no internal zeros. Consequently, if \(B=\prod_{j=1}^{k}[0,m_j]\) is any lattice box, then log-concavity of \(h_P^*\) implies log-concavity of \(h_{P\times B}^*\).

This gives an affirmative answer to the Cartesian-product log-concavity question when one factor is a lattice segment, and by iteration when one factor is an arbitrary axis-aligned lattice box.

## Assumptions and scope
A lattice polytope is taken with respect to the standard integer lattice. For a \(d\)-dimensional lattice polytope \(P\), write
\[\sum_{n\ge0} |nP\cap\mathbb Z^N|t^n=\frac{h_P^*(t)}{(1-t)^{d+1}}.\]
The coefficient sequence of a polynomial with nonnegative coefficients is called log-concave here when it has no internal zeros and satisfies \(a_i^2\ge a_{i-1}a_{i+1}\) throughout its positive support. No real-rootedness, IDP, spanning, or triangulation hypothesis is assumed.

## Proof
Write \(F(t)=h_P^*(t)/(1-t)^{d+1}\). The segment \([0,m]\) has \(|n[0,m]\cap\mathbb Z|=mn+1\), hence
\[\sum_{n\ge0} |n(P\times[0,m])\cap\mathbb Z|t^n=m tF'(t)+F(t).\]
Putting this over the denominator \((1-t)^{d+2}\) gives the numerator
\[(1-t)h_P^*(t)+mt(1-t)(h_P^*)'(t)+m(d+1)t h_P^*(t).\]
Therefore, with \(h_i=0\) outside \(0\le i\le s\),
\[g_i=(1+mi)h_i+\bigl(m(d+2-i)-1\bigr)h_{i-1}.\]
For \(0\le i\le d+1\), both weights are nonnegative.

It remains to prove log-concavity. If \(s=0\), the resulting numerator has degree at most one and there is nothing to prove. Assume \(s\ge1\). For an index \(1\le i\le s\), set \(x=h_{i-1}>0\) and \(y=h_i>0\), and define
\[A_j=1+mj,\qquad B_j=m(d+2-j)-1,\qquad C_j=A_jy+B_jx.\]
Log-concavity of \((h_i)\) gives
\[h_{i-2}\le \frac{x^2}y,\qquad h_{i+1}\le \frac{y^2}x,\]
where the first or second term is interpreted as zero at the ends of the support. Consequently,
\[g_{i-1}\le \frac{x}{y}C_{i-1},\qquad g_{i+1}\le \frac{y}{x}C_{i+1}.\]
Since \(C_j\) is affine in \(j\) with increment \(m(y-x)\),
\[C_i^2-C_{i-1}C_{i+1}=m^2(y-x)^2\ge0.\]
Because \(g_i=C_i\), it follows that
\[g_i^2\ge C_{i-1}C_{i+1}\ge g_{i-1}g_{i+1}.\]
These are all nontrivial log-concavity inequalities of the output sequence. Its positive support is consecutive: the input has consecutive positive support, all displayed weights are nonnegative, and after the last possible term every coefficient is zero. Thus \(h_{P\times[0,m]}^*\) is log-concave with no internal zeros.

Applying the segment statement successively to the factors \([0,m_1],\ldots,[0,m_k]\) proves the box-product assertion.

## Verification
The accompanying `verify.py` independently reconstructs the numerator transform from Ehrhart-series coefficients for many exact integer test vectors, checks the affine identity
\[C_i^2-C_{i-1}C_{i+1}=m^2(y-x)^2,\]
and tests log-concavity preservation on a collection of exact log-concave sequences and repeated box factors. These finite checks are consistency tests only; the universal proof is the argument above.

## Relationship to prior work
Ferroni and Higashitani formulate the general question whether Cartesian products preserve log-concavity of Ehrhart \(h^*\)-polynomials (Question 3.4(a)). They also recall Wagner's stronger-input theorem: Cartesian products preserve \(h^*\)-real-rootedness. Liu, Tao, and Xin explicitly restate the log-concavity problem in their 2026 study of joins and Cartesian products. Brändén, Ferroni, and Jochemko prove preservation of ultra log-concavity under the corresponding Hadamard-product operation, again under a stronger hypothesis than ordinary log-concavity. None of these statements yields the segment-factor result from ordinary log-concavity alone.

The present result supplies a direct coefficient transform and proves that a lattice segment, and hence any lattice box, is a preserving factor for ordinary \(h^*\)-log-concavity.

## Limitations
The argument uses the linear Ehrhart polynomial \(mn+1\) of a lattice segment. It does not settle the Cartesian-product question for a general second factor, does not upgrade log-concavity to real-rootedness, and does not claim strict log-concavity. The result concerns Cartesian products, not joins.

## References
1. F. Liu, S. Tao, and G. Xin, “Ehrhart Theory of the Join of Two Lattice Polytopes,” arXiv:2606.18794v1 (2026). Primary MSC 52B20.
2. L. Ferroni and A. Higashitani, “Examples and counterexamples in Ehrhart theory,” arXiv:2307.10852v4; EMS Surveys in Mathematical Sciences, DOI 10.4171/EMSS/86.
3. P. Brändén, L. Ferroni, and K. Jochemko, “Preservation of inequalities under Hadamard products,” arXiv:2408.12386.
4. D. G. Wagner, “Total positivity of Hadamard products,” Journal of Mathematical Analysis and Applications 163 (1992), 459–483.
