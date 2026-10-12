# A sharp entropy-resistance phase for Bernoulli laws on the five-cycle

## Finding

Let \(G=\mathbb Z/5\mathbb Z\) with addition modulo five, and let \(X_p\) have probabilities \(\Pr(X_p=0)=p\) and \(\Pr(X_p=1)=1-p\), where \(0<p<1\). A symmetrizer is an independent \(G\)-valued random variable \(Y\) for which \(X_p+Y\) and \(-X_p-Y\) have the same law. Write \(H\) for discrete Shannon entropy with natural logarithms and \(t=\min(p,1-p)\). Put
\[
 h(t)=-t\log t-(1-t)\log(1-t),\qquad
 r(t)=\frac{1-2t}{3-5t},\qquad s(t)=\frac{1-t}{3-5t},
\]
where \(0<t\le 1/2\), and use \(0\log0=0\). Then the *attained global minimum over all independent symmetrizers* is
\[
 \boxed{\inf_Y H(Y)=\min\{h(t),\ -2r(t)\log r(t)-s(t)\log s(t)\}.}
\]
There is a unique \(t_\star\in(0,1/2)\) at which the two branches agree, with \(t_\star\approx0.4607513816494958726\). For \(0<t<t_\star\), the unique minimizer is the reflected Bernoulli symmetrizer; for \(t_\star<t\le1/2\), it is a sparse three-point symmetrizer (a point mass at \(t=1/2\)); at \(t=t_\star\), exactly these two distinct laws minimize. In particular, all independent symmetrizers satisfy \(H(Y)\ge H(X_p)\) exactly when \(t\le t_\star\), whereas strict entropy reduction is possible exactly when \(t>t_\star\).

For \(0<p\le1/2\), in coordinate order \(0,1,2,3,4\), the reflected Bernoulli law is \((p,0,0,0,1-p)\) and the sparse competitor is \((0,r(p),s(p),0,r(p))\). For \(1/2<p<1\), apply the involution \(Y\mapsto-1-Y\) to the corresponding minimizers at \(1-p\). These statements include every entropy-minimizing law, not merely the minimum value.

## Assumptions and scope

All variables are defined on the finite additive group \(G\), not on the real line. Symmetry means invariance under inversion about the identity element, not symmetry about an arbitrarily chosen center. The symmetrizer may have any probability law on all five group elements and must be independent of \(X_p\). The two-point input has the fixed support \(\{0,1\}\); automorphisms and translations reduce the equivalent versions with a generating difference to this case. The result includes all \(p\in(0,1)\), including the balanced input \(p=1/2\).

## Proof

By replacing \(X_p\) by \(1-X_p\), and a symmetrizer \(Y\) by \(-1-Y\), it suffices to take \(0<p\le1/2\). Set \(q=1-p\) and \(y_i=\Pr(Y=i)\) for indices modulo five. The sum \(Z=X_p+Y\) has \(\Pr(Z=i)=p y_i+q y_{i-1}\). Consequently inversion symmetry is equivalent to the following three independent affine equations:
\[
 \sum_{i=0}^{4}y_i=1,\quad q y_0+p y_1-q y_3-p y_4=0,\quad
 q y_1+(2p-1)y_2-p y_3=0.
\]
Together with \(y_i\ge0\), these define a nonempty compact convex polytope. The constraint matrix has rank three, so every vertex has at most three positive coordinates. Entropy is strictly concave on the probability simplex; therefore every global entropy minimizer is a vertex.

For \(0<p<1/2\), examining the ten possible three-column supports yields *exactly four distinct vertices*, displayed as probability vectors in order \(0,1,2,3,4\):
\[
\begin{aligned}
 A&=(p,0,0,0,q),\\
 B&=\left(\frac{1-2p}{2-3p},\frac{pq}{2-3p},0,\frac{q^2}{2-3p},0\right),\\
 C&=(0,q/2,1/2,p/2,0),\\
 D&=\left(0,\frac{1-2p}{3-5p},\frac{q}{3-5p},0,\frac{1-2p}{3-5p}\right).
\end{aligned}
\]
Here is an exhaustive sign certificate for the discarded support triples. For \(\{0,1,2\}\), the first nonzero coordinate is \(p(2p-1)/(5p^2-6p+2)<0\). For \(\{0,2,3\}\), coordinates at 0 and 2 are \((2p-1)/(5p-2)\) and \(p/(5p-2)\), of opposite signs whenever the determinant is nonzero. For \(\{1,3,4\}\), coordinates at 1 and 4 are \(p^2/(3p-1)\) and \((2p-1)/(3p-1)\), also of opposite signs. For \(\{2,3,4\}\), the coordinate at 3 equals \(p(2p-1)/(5p^2-4p+1)<0\). The triples \(\{0,1,4\}\), \(\{0,2,4\}\), and \(\{0,3,4\}\) all give \(A\), while \(\{0,1,3\}\), \(\{1,2,3\}\), and \(\{1,2,4\}\) give \(B,C,D\). When a listed determinant vanishes at \(p=1/3\) or \(p=2/5\), its columns cannot span an additional three-positive-coordinate vertex; the independent-column triples above still exhaust the possibilities. The inequalities follow because \(5p^2-6p+2\) and \(5p^2-4p+1\) are positive for all real \(p\).

Every coordinate of \(B\) and \(C\) is at most \(q\): for \(C\), this is immediate from \(q\ge1/2\); for \(B\), use \(pq\le q(2-3p)\), \(q^2\le q(2-3p)\), and \(1-2p<q(2-3p)\). Thus \((q,p,0,0,0)\) majorizes \(B\) and \(C\). Both have three strictly positive coordinates, so strict Schur concavity gives \(H(B)>H(A)=h(p)\) and \(H(C)>H(A)\). Only \(A\) and \(D\) can minimize entropy.

To compare them, let \(\varepsilon=1-2p\in(0,1)\). The coordinates of \(D\) are \(r=2\varepsilon/(1+5\varepsilon)\), \(s=(1+\varepsilon)/(1+5\varepsilon)=1-2r\), and \(r\). Differentiating its entropy with respect to \(\varepsilon\) gives
\[
 \frac{d}{d\varepsilon}H(D)=\frac{4}{(1+5\varepsilon)^2}\log\frac{s}{r}>0,
\]
whereas \(h((1-\varepsilon)/2)\) strictly decreases with \(\varepsilon\). The difference \(H(D)-h(p)\) therefore strictly decreases with \(p\). It tends to \(\log3\) as \(p\downarrow0\) and to \(-\log2\) as \(p\uparrow1/2\), so it vanishes at one and only one \(p=t_\star\). This proves the phase formula and the uniqueness assertions for \(p<1/2\), because strict concavity excludes any nontrivial mixture of minimizing vertices. At \(p=1/2\), the law \(D=(0,0,1,0,0)\) is a deterministic symmetrizer, and the only deterministic symmetrizer is the point mass at 2: the symmetric pair \(\{j,j+1\}\) must satisfy \(2j+1=0\pmod5\). Hence the entropy minimum and its optimizer remain uniquely determined at the boundary. Reflection handles \(p>1/2\).

## Verification

The accompanying `verify.py` re-derives the symmetry equations and enumerates all nonsingular three-column supports with exact rational Gaussian determinants for eleven rational parameter values, including the exceptional minors at \(p=1/3\) and \(p=2/5\). It checks exact nonnegativity, normalization, symmetry, the four-vertex classification, and two majorization inequalities; numerical logarithms provide an independent approximate phase-bracket check. Executing `python3 verify.py` prints `CHECKS_PASS 189`. These finite tests corroborate the displayed symbolic enumeration; the analytic sign certificate and strict monotonicity prove the statements for all real \(p\) in scope.

## Relationship to prior work

Madiman and Pollard, *Entropic Symmetrization Resistance* (arXiv:2607.29020, first posted 31 July 2026), introduced the finite-group formulation and report classifications for the groups of orders three and four. The five-element group is the first larger cyclic prime case, and the formula here classifies the full two-point generating-support family with an exact entropy phase transition. The paper's general necessary boundary-of-simplex condition does not decide which two-point laws are resistant. Pollard's 2023 dissertation developed the real-line symmetrizer polytope and Bernoulli entropy inequality; that real-line conclusion cannot simply be transported through reduction modulo five, as the strict entropy-reduction phase above demonstrates. Li's 2026 results for geometric and exponential real-valued variables concern different laws and ambient groups. Full text of arXiv:2607.29020 was not inspected in this comparison; the paper's publicly available abstract expressly identifies its complete finite-group classifications only for orders three and four, but an unrecognized stronger implication in the unavailable text remains a priority risk.

## Limitations

This is a complete minimum-entropy classification for a two-point law with generating support difference on the five-cycle, not a characterization of all input distributions on that group, nor a theorem on arbitrary cyclic orders or other entropy functionals. Natural logarithms are used; changing the logarithm base multiplies all entropies by the same positive constant and leaves the phase unchanged. Approximate digits of \(t_\star\) are not an interval certificate; existence and uniqueness are analytic. No independent external verification has been performed.

## References

1. M. Madiman and E. Pollard, *Entropic Symmetrization Resistance*, arXiv:2607.29020 (public version 31 July 2026), https://arxiv.org/abs/2607.29020.
2. E. Pollard, *A Study of Some Entropy Inequalities*, University of Delaware doctoral dissertation (2023), https://udspace.udel.edu/items/9b85671a-9f4b-43c6-930d-2cc82fb23e02.
3. J. Li, *How Much Randomness Is Needed to Symmetrize a Random Variable?*, arXiv:2607.17576 (20 July 2026), https://arxiv.org/abs/2607.17576.
