# Sharp mean–mode constants for monotone log-concave laws on at most five atoms
## Finding
Let \(X\) be a nondegenerate integer-valued random variable with a monotone log-concave probability mass function \(p\) and contiguous support of cardinality \(N\in\{2,3,4,5\}\). Define
\[
\mu=\mathbb E X,\qquad M=\max_k p(k),\qquad R(X)=\frac{\max\{p(\lfloor\mu\rfloor),p(\lceil\mu\rceil)\}}{M}.
\]
Then the exact support-size constants are
\[
\min R(X)=1\quad(N=2,3),
\]
\[
\min R(X)=r_4\quad(N=4),\qquad r_4^2(1+2r_4)=1,
\]
and
\[
\min R(X)=r_5\quad(N=5),\qquad r_5^2(1+2r_5+3r_5^2)=1,
\]
where in each case \(r_N\) denotes the unique root in \((0,1)\). Numerically,
\[
r_4=0.6572981061383759\ldots,\qquad r_5=0.5677373609406795\ldots.
\]
For \(N=4\) and \(N=5\), equality holds exactly, up to integer translation and reflection, for the truncated geometric mass vector
\[
(1,r_N,r_N^2,\ldots,r_N^{N-1})
\]
after normalization.

## Assumptions and scope
Log-concavity means \(p(k)^2\ge p(k-1)p(k+1)\) at each interior support point, with no internal zeros. Monotonicity means the positive masses are nonincreasing or nondecreasing across their support. Translation and reflection preserve all hypotheses and preserve \(R(X)\), so it is enough to analyze a nonincreasing mass function on \(\{0,1,\ldots,N-1\}\).

The result is deliberately finite-support. It sharpens the general bound \(R(X)\ge e^{-1}\) known for arbitrary discrete log-concave laws, but only for monotone laws with at most five support points. No claim is made for support size six or larger; at six points a decreasing law can already have mean strictly larger than \(2\), so a second interior mean cell enters the optimization.

## Proof
Assume first that the masses decrease. For \(N\le5\), monotonicity gives
\[
\mu\le\frac{N-1}2.
\]
Indeed, pairing the masses symmetrically about \((N-1)/2\) shows that every upper-side mass is no larger than its reflected lower-side mass. Equality holds only for the uniform law.

For \(N=2\), this puts \(\mu<1\), so \(\lfloor\mu\rfloor=0\) and the mode itself occurs among the two mean-adjacent lattice points. Thus \(R(X)=1\). For \(N=3\), one has \(\mu\le1\). If \(\mu<1\), again \(p(0)=M\) is sampled by \(R\); if \(\mu=1\), monotonicity forces the three masses to be equal, so again \(R(X)=1\).

Now let \(N=4\). Write the positive mass ratios as
\[
a=\frac{p(1)}{p(0)},\qquad b=\frac{p(2)}{p(1)},\qquad c=\frac{p(3)}{p(2)}.
\]
Monotone log-concavity is exactly
\[
1\ge a\ge b\ge c>0.
\]
If \(\mu<1\), then \(R(X)=1\). If \(\mu\ge1\), then \(\mu\le3/2\), so the larger of the two masses adjacent to the mean is \(p(1)\), and hence \(R(X)=a\). Up to normalization the masses are \((1,a,ab,abc)\), and \(\mu\ge1\) is equivalent to
\[
ab(1+2c)\ge1.
\]
Because \(b,c\le a\),
\[
1\le ab(1+2c)\le a^2(1+2a).
\]
The function \(a\mapsto a^2(1+2a)\) is strictly increasing on \((0,1)\), so \(a\ge r_4\), where \(r_4\) is the unique root of \(r_4^2(1+2r_4)=1\). Equality throughout forces \(a=b=c=r_4\), and then the mean is exactly \(1\). Conversely that truncated geometric vector realizes equality.

For \(N=5\), put
\[
a=\frac{p(1)}{p(0)},\quad b=\frac{p(2)}{p(1)},\quad c=\frac{p(3)}{p(2)},\quad d=\frac{p(4)}{p(3)}.
\]
Then \(1\ge a\ge b\ge c\ge d>0\), and \(\mu\le2\), with equality only for the uniform law. If \(\mu<1\), then \(R(X)=1\). If \(1\le\mu<2\), the larger adjacent mass is \(p(1)\), hence \(R(X)=a\); the uniform case \(\mu=2\) has \(R(X)=1\). For masses proportional to \((1,a,ab,abc,abcd)\), the condition \(\mu\ge1\) is
\[
ab(1+2c+3cd)\ge1.
\]
Using \(b,c,d\le a\),
\[
1\le ab(1+2c+3cd)\le a^2(1+2a+3a^2).
\]
Again the right-hand side is strictly increasing on \((0,1)\), so \(a\ge r_5\), where \(r_5^2(1+2r_5+3r_5^2)=1\). Equality forces \(a=b=c=d=r_5\), and the defining equation then makes the mean exactly \(1\). The corresponding normalized truncated geometric vector therefore attains the bound.

Finally, a nondecreasing law is reflected to a nonincreasing one. Reflection preserves log-concavity and the ratio \(R(X)\), and carries the equality vectors to their reversals. This proves the stated classification.

## Verification
The proof is algebraic and covers every admissible law, including all boundary cases. The standalone script `verify.py` independently checks the defining roots, verifies that both equality distributions have mean exactly \(1\), and exhausts a fine rational ratio grid as a diagnostic. The grid is not used as a proof.

For the equality laws the computed constants are
\[
r_4=0.6572981061383759908\ldots,\qquad r_5=0.5677373609406794914\ldots.
\]
The support-size cutoff is structural: for decreasing laws on at most five atoms, \(\mu\le2\), so only the first nontrivial mean cell needs optimization; with six atoms, \(\mu\) may lie above \(2\).

## Relationship to prior work
Melbourne and Palafox-Castillo prove the general discrete log-concave mean-versus-mode estimate
\[
\max\{p(\lfloor\mathbb EX\rfloor),p(\lceil\mathbb EX\rceil)\}\ge e^{-1}\max_k p(k),
\]
and note sharpness through geometric laws with large integer mean (arXiv:2111.06997v1, Corollary 2.8). Their statement does not give support-cardinality refinements or finite-support equality cases.

Marsiglietti and Melbourne characterize log-affine extreme points for convex optimization over half-space slices of finite log-concave probability simplices (arXiv:2004.12005v4). That framework explains why geometric profiles are natural extremizers, but the inspected paper does not state the mean-adjacent/mode ratio constants above; the present proof resolves the moving floor/ceiling location directly through adjacent mass ratios.

Bobkov, Marsiglietti and Melbourne study concentration and Rényi entropy inequalities for discrete log-concave distributions (arXiv:2007.11030v1; DOI:10.1017/S096354832100016X). The journal metadata lists primary MSC 60E15. Aravinda's degree-of-freedom work gives sharp min-entropy--variance inequalities with geometric extremizers (arXiv:2212.09115v1), but not the finite-support mean-adjacent ratio classification.

## Limitations
The theorem assumes monotonicity in addition to log-concavity and treats support cardinalities only through five. It does not determine the optimal constants for six or more support points, where additional mean cells can be active. The originality comparison cannot exclude an older equivalent elementary calculation hidden under different mean-mode terminology; the strongest closely related sources inspected do not contain the stated constants or equality classification.

## References
1. S. G. Bobkov, A. Marsiglietti, J. Melbourne, *Concentration functions and entropy bounds for discrete log-concave distributions*, arXiv:2007.11030v1, DOI:10.1017/S096354832100016X.
2. J. Melbourne, G. Palafox-Castillo, *A discrete complement of Lyapunov's inequality and its information theoretic consequences*, arXiv:2111.06997v1.
3. A. Marsiglietti, J. Melbourne, *Geometric and Functional Inequalities for Log-concave Probability Sequences*, arXiv:2004.12005v4, DOI:10.1007/s00454-023-00528-7.
4. H. Aravinda, *Entropy-variance inequalities for discrete log-concave random variables via degree of freedom*, arXiv:2212.09115v1.
