# Rational periodic limits in three-layer counting modal logic

## Finding

Let \(T_n\) be the complete rooted \(n\)-ary tree of height three, with each propositional letter independently true at each vertex with probability \(1/2\). Satisfaction is evaluated at its root. The syntax is the counting modal logic \(K^{\#}\): formulas are Boolean combinations of integer linear comparisons involving counts \(\#\psi\) of immediate successors satisfying \(\psi\). No congruence or modulo operator is used.

**Periodic-profile universality.** For every fixed integer \(m\ge2\) and every rational vector \((c_0,\ldots,c_{m-1})\in(\mathbb Q\cap[0,1])^m\), an effectively constructible \(K^{\#}\)-formula \(\Psi\) of modal depth at most three satisfies

\[
\lim_{k\to\infty}\Pr(T_{mk+r},\mathrm{root}\models\Psi)=c_r
\qquad(r=0,\ldots,m-1).
\]

More precisely, the construction contains a depth-three *residue detector* \(D_{m,r}\) with probability identically zero unless \(n\equiv r\pmod m\), whereas along the indicated residue class its failure probability has a strictly positive stretched-exponential rate:

\[
\Pr(T_n,\mathrm{root}\not\models D_{m,r})
=\exp\bigl(-\alpha_m\sqrt n+o(\sqrt n)\bigr)
\quad(n\equiv r\pmod m),
\]

where the constant \(\alpha_m>0\), independent of \(r\), is given explicitly below. Thus every prescribed binary periodic pattern, and more generally every rational-valued periodic limiting profile, is obtained using only independent fair propositional letters and linear counting comparisons.

## Assumptions and scope

Here \(m\), the rational targets, and the formula are fixed as \(n\) tends to infinity. Every non-leaf has exactly \(n\) children; labels of distinct letters and vertices are mutually independent fair bits. The integer \(n\) is not itself a constant appearing in the formula; the term \(\#\top\) evaluates to \(n\) at any non-leaf, where \(\top\) is a propositional tautology. Equality is the conjunction of two permitted linear inequalities.

For \(m\) distinct letters \(p_1,\ldots,p_m\), put

\[
B_m=\bigwedge_{j=2}^m\bigl(\#p_1-\#p_j\ge1\bigr),
\qquad
H_{m,r}=\bigl(m\#B_m-\#\top+r=0\bigr),
\qquad
D_{m,r}=\bigl(\#H_{m,r}\ge1\bigr).
\]

Their modal depths are one, two, and three, respectively. A separate finite collection of letters \(q_i\), independent of all \(p_i\), is used only for rational-valued output gates at the root.

## Proof

**1. Exact plurality probability and its tie correction.** At any node with \(n\) children, the variables \(X_i=\#p_i\), for \(1\le i\le m\), are independent \(\operatorname{Bin}(n,1/2)\) random variables. The event \(B_m\) is that \(X_1\) is the unique maximum, and its probability \(u_m(n)\) is exactly

\[
u_m(n)=2^{-mn}\sum_{t=0}^n\binom nt
  \left(\sum_{j=0}^{t-1}\binom nj\right)^{m-1}.
\]

Write \(\varphi(z)=(2\pi)^{-1/2}e^{-z^2/2}\) and \(\Phi(z)=\int_{-\infty}^z\varphi(y)\,dy\), and define

\[
I_m=\int_{-\infty}^{\infty}\varphi(z)^2\Phi(z)^{m-2}\,dz,
\qquad \delta_m=(m-1)I_m>0.
\]

Symmetry gives \(m u_m(n)=\Pr(\text{the maximum of the }X_i\text{ is unique})\). The probability of a fixed pair tying at the maximum with every other count strictly below it is

\[
\sum_{t=0}^n \Pr(X_1=t)^2\Pr(X_1<t)^{m-2}
=\frac{2I_m}{\sqrt n}+o(n^{-1/2}),
\]

by the binomial local central limit theorem and a Gaussian Riemann sum. Three-way ties have probability \(O(n^{-1})\), so their contribution is negligible after multiplying by \(\sqrt n\). Summing over unordered pairs therefore yields

\[
u_m(n)=\frac1m-\frac{\delta_m}{\sqrt n}+o(n^{-1/2}).
\]

**2. A rare exact-equality event that knows the residue.** At a parent of \(n\) independent subtrees, let \(Y_n=\#B_m\). The probability just calculated is the same for each subtree and their labels are disjoint, hence \(Y_n\sim\operatorname{Bin}(n,u_m(n))\). The formula \(H_{m,r}\) is precisely the event \(mY_n=n-r\). It is impossible unless \(n\equiv r\pmod m\). On the correct residue class, put \(t_n=(n-r)/m\). Then

\[
t_n-nu_m(n)=\delta_m\sqrt n+o(\sqrt n),
\qquad \frac{nu_m(n)(1-u_m(n))}{n}\longrightarrow
\sigma_m^2=\frac{m-1}{m^2}>0.
\]

The triangular-array binomial local central limit estimate gives

\[
\Pr(H_{m,r})=\Pr(Y_n=t_n)
=\frac{\alpha_m+o(1)}{\sqrt n},
\quad
\alpha_m=\frac{m}{\sqrt{2\pi(m-1)}}
\exp\!\left(-\frac{m^2\delta_m^2}{2(m-1)}\right)>0.
\]

This leading constant is the same for all fixed residues \(r\).

**3. Rare-event amplification.** At the root, the \(n\) children have disjoint descendant-label sets. Consequently the events \(H_{m,r}\) at these children are independent, each with probability \(e_{n,r}=\Pr(H_{m,r})\). Their exact distribution gives

\[
\Pr(D_{m,r})=1-(1-e_{n,r})^n,
\qquad
e_{n,r}=
\begin{cases}
\binom{n}{(n-r)/m}u_m(n)^{(n-r)/m}
(1-u_m(n))^{n-(n-r)/m},&n\ge r,\ n\equiv r\pmod m,\\
0,&\text{otherwise.}
\end{cases}
\]

Off the residue class, \(D_{m,r}\) is false with certainty. On the residue class, \(n e_{n,r}=\alpha_m\sqrt n+o(\sqrt n)\); moreover \(n e_{n,r}^2=O(1)\), so

\[
\log\Pr(\neg D_{m,r})=n\log(1-e_{n,r})
=-\alpha_m\sqrt n+o(\sqrt n).
\]

This proves the detector's asserted rate.

**4. Rational output probabilities without biased letters.** To realize a rational \(a/b\), with \(0<a<b\), use distinct fresh letters \(q_1,\ldots,q_b\) and the depth-one formula

\[
G_{a,b}=\bigvee_{i=1}^{a}\bigwedge_{\substack{1\le j\le b\\ j\ne i}}
\bigl(\#q_i-\#q_j\ge1\bigr).
\]

It says that one of the first \(a\) binomial counts is the unique largest of the \(b\) exchangeable counts. Its probability is exactly \(a u_b(n)\), tending to \(a/b\). For targets zero and one, define the gate to be \(\bot\) and \(\top\), respectively. Every such gate is independent of every \(D_{m,r}\), since the former uses only \(q\)-letters and the latter only \(p\)-letters.

**5. Assemble an arbitrary periodic profile.** Choose a rational gate \(G_r\) for each target \(c_r\), and set

\[
\Psi=\bigvee_{r=0}^{m-1}(D_{m,r}\wedge G_r).
\]

At any given \(n\), at most the term with \(r=n\bmod m\) can hold. Accordingly its exact probability is

\[
\Pr(\Psi)=\left[1-(1-e_{n,r})^n\right]\Pr(G_r),
\qquad r=n\bmod m.
\]

The first factor tends to one on that residue, the second to \(c_r\). This completes the construction for every fixed \(m\) and every rational profile.

## Verification

The standalone `checker.py` directly enumerates labelled local assignments and tests the exact probabilities of \(B_m\), \(H_{m,r}\), \(D_{m,r}\), and the rational gates for bounded parameter choices. It also checks large-binomial numerical convergence for \(m=2,3\). The finite tests cover 5,276 plurality assignments, 266,508 middle-level assignments, 65,536 complete root assignments, 656 gate assignments, and two numerical asymptotic parameter tests. All tests completed successfully. These computations are checks of definitions and finite identities, not a proof of the infinite statements; the proof above supplies the asymptotics.

For example, \(m=3\) and target profile \((0,1,1/2)\) yield a single depth-three formula whose satisfaction probabilities converge respectively to \(0,1,1/2\) along \(n\equiv0,1,2\pmod3\). For \(m=2\), the detector rate is \(\alpha_2=\sqrt{2/\pi}\exp(-1/(2\pi))\).

## Relationship to prior work

Ghosh and Schwarzentruber (2026) define the same counting-modal syntax and random full-branching tree proportions. Their Section 6.1 gives an oscillating parity example and Sections 6.2–6.3 study a modified limit and density of achievable limiting values. The present claim concerns ordinary, unmodified probabilities and realizes *every finite modulus and every rational-valued residue profile*, with a quantitative detector law; this statement does not follow from the paper's single parity witness or its density assertion alone. Benedikt, Lu, Motik and Tan (2024) investigate expressive and decision-theoretic properties of related Presburger-counting graph logics; that is a distinct problem from the ordinary branching-limit probability profile studied here. General literature on logics with explicit modulo quantifiers uses stronger syntax: no such quantifier occurs in this construction.

## Limitations

The tree is complete, directed away from the root, of fixed height three, with fair independent labels. The modulus, number of proposition letters and formula are fixed before sending the branching parameter to infinity. This is a realization theorem, not a classification of limits of all counting-modal formulas, a decision procedure for convergence, or a claim about arbitrary random graphs. The explicit detector rate is asymptotic along its designated residue only. Earlier unpublished or specialized equivalent constructions may exist; the priority assessment is limited to the inspected literature.

## References

1. Avijeet Ghosh and François Schwarzentruber, *On Counting Graphs for Modal Logic with Counting*, arXiv:2610.26187v1, first public October 19, 2026; specifically Sections 3 and 6. https://arxiv.org/abs/2610.26187
2. Michael Benedikt, Chia-Hsuan Lu, Boris Motik, and Tony Tan, *Decidability of Graph Neural Networks via Logical Characterizations*, ICALP 2024, DOI: 10.4230/LIPIcs.ICALP.2024.127 (background on counting-logic expressivity).
