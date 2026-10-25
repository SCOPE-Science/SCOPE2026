# Exact nonwandering arity filtration in a one-fixed-point symbolic homeomorphism

## Finding
Let \(Y\) and \(g:Y\to Y\) be the compact quotient homeomorphism constructed by Đorić in *A note on the non-wandering dynamics in the \(n\)-fold symmetric products* (arXiv:2610.23058v1). For every nonempty finite set \(A\subset Y\), the smallest symmetric-product order \(\nu(A)\) for which \(A\) is nonwandering under the induced map is given exactly below. In particular, there is a complete classification of the nonwandering set of \(F_n(g)\) for **every** positive integer \(n\), whereas the motivating paper explicitly classifies \(F_2(g)\).

Let \(p\) be the unique fixed point, \(\{x_r:r\in\mathbb Z\}\) and \(\{y_s:s\in\mathbb Z\}\) the two families of step configurations, and \(\mathcal I\) the family of finite-block configurations. For a finite nonempty \(A\), put
\[
a=|A\cap\{x_r\}|,\quad b=|A\cap\{y_s\}|,\quad c=|A\cap\mathcal I|.
\]
If \(p\notin A\), then
\[
\nu(A)=\begin{cases}2\max(a,b),&a,b\ge1\text{ and }c=0,\\
\infty,&\text{otherwise}.
\end{cases}
\]
If \(p\in A\), then
\[
\boxed{\nu(A)=2c+2\max(a,b)+\mathbf1_{\{c=0,\ a=b\}}.}
\]
For every integer \(n\ge1\), the exact equivalence is
\[
 A\in\operatorname{NW}(F_n(g))\quad\Longleftrightarrow\quad n\ge\nu(A),
\]
where the left side is interpreted as false if \(|A|>n\). For example, any collection of \(c\ge1\) distinct finite-block points together with \(p\) first becomes nonwandering at order exactly \(2c\); a collection of \(a\ge1\) upward steps and \(b\ge1\) downward steps, without \(p\), first becomes nonwandering at order \(2\max(a,b)\).

## Assumptions and scope
Consider the two-sided binary subshift \(X\subset\{0,1\}^{\mathbb Z}\) consisting of configurations with at most one \(01\) transition and at most one \(10\) transition. It consists of the two constants \(\mathbf0,\mathbf1\), upward steps \(x_r\) (zero for indices less than \(r\), one thereafter), downward steps \(y_s\) (one below \(s\), zero thereafter), one-block configurations \(z_{r,m}\) (ones on \([r,r+m)\), zero outside), and zero-block configurations \(w_{r,m}\) (zeros on \([r,r+m)\), one outside), with \(r\in\mathbb Z,m\ge1\). The left shift is \(\sigma(u)_j=u_{j+1}\). Identify precisely the two constants to obtain \(Y\), with quotient \(q:X\to Y\) and \(g(q(u))=q(\sigma(u))\). Write the same symbols for the nonconstant images, set \(p=q(\mathbf0)=q(\mathbf1)\), and set \(\mathcal I=\{z_{r,m},w_{r,m}\}\). Every member of \(\mathcal I\) is an isolated point of \(Y\).

The symmetric product \(F_n(Y)\) is the space of nonempty subsets of at most \(n\) points, with the Hausdorff topology and induced homeomorphism \(F_n(g)(A)=g(A)\). Nonwandering uses the standard condition that every neighborhood returns to intersect itself at some positive time. No smoothness, differentiability, metric normalization, or unproved genericity assumption is involved.

## Proof
**1. All long-time one-particle endpoint possibilities.** Suppose \(N_j\to\infty\), \(u_j\to u\), and \(g^{N_j}(u_j)\to v\). If \(u\ne p\) is a finite block, it is isolated, so eventually \(u_j=u\) and \(v=p\). If \(u=x_r\), the transition \(01\) at \(r\) must occur in every sufficiently close lift. Any nonfixed limit \(v\) at time \(N_j\) requires a second transition at a position tending to \(+\infty\) in the original coordinates. Since every configuration has at most one transition of each orientation, that distant transition must be \(10\), and the only possible nonfixed limit is a downward step \(y_s\). Thus \(x_r\) may lead only to \(p\) or to some \(y_s\). Symmetrically, \(y_s\) may lead only to \(p\) or to some \(x_r\). A point near \(p\) may lead to any point of \(Y\). These are the only possible directed endpoint pairs:
\[
 p\to v\ (v\in Y),\quad x_r\to p,\quad y_s\to p,\quad z_{r,m}\to p,\quad w_{r,m}\to p,\quad x_r\to y_s,\quad y_s\to x_r.
\]
Each listed pair actually occurs for arbitrarily large common times. Use \(x_r\) or \(y_s\) for a step-to-\(p\) pair, a fixed finite block for a finite-block-to-\(p\) pair, and the fixed point for \(p\to p\). For \(x_r\to y_s\), take the one-block configuration with ones on \([r,N+s)\); for \(y_s\to x_r\), take zeros on \([s,N+r)\). For \(p\to v\), translate a representative of \(v\) to the right by \(N\). The initial point converges to \(p\), and its \(N\)-iterate is \(v\). For a step endpoint, these constructions may be chosen distinct when multiple edges share the same step vertex by varying the other (distant) transition.

**2. Finite arrows forced by nonwandering.** The only periodic point of \(g\) is \(p\), hence the only periodic point of every \(F_n(g)\) is \(\{p\}\). For any other nonwandering \(A\), choose finite point sets \(A_j\to A\) with \(g^{N_j}(A_j)\to A\) and \(N_j\to\infty\). A bounded return-time subsequence would instead make \(A\) periodic, so these times can be taken unbounded. After fixing \(|A_j|\le n\) and passing to a subsequence, enumerate their members and take limits of each member and its image. This produces at most \(n\) arrows, all of the types in Step 1, whose sets of sources and targets each cover all vertices of \(A\).

If \(A\) contains \(c\) isolated finite-block points, every one requires a separate outgoing arrow to \(p\) and a separate incoming arrow from \(p\); thus \(p\in A\) and at least \(2c\) arrows are forced. Independently, let \(E_1\) consist of arrows departing an upward step or arriving at a downward step, and let \(E_2\) consist of arrows departing a downward step or arriving at an upward step. Step 1 makes these classes disjoint from each other and from the \(2c\) finite-block arrows. Each class must have at least \(\max(a,b)\) members: it must cover at least \(a\) sources/targets of one orientation and at least \(b\) targets/sources of the other. Hence \(n\ge 2c+2\max(a,b)\). If \(p\notin A\), any finite block or a collection of steps of only one orientation is impossible, since its required outgoing/target arrows do not exist in \(A\). If \(p\in A,c=0,a=b\), equality in the bound would force every member of \(E_1\) to be upward-to-downward and every member of \(E_2\) to be downward-to-upward; no arrow could touch \(p\), contradicting the required source and target coverage of \(p\). Therefore one additional arrow is necessary, including when \(a=b=0\).

**3. Sharpness with simultaneous orbit witnesses.** A finite arrow multiset can be realized at one common sequence of times \(N\to\infty\) by the explicit binary configurations in Step 1. At every sufficiently large \(N\), all representatives can be made distinct before and after shifting. In particular, arrows from a fixed step to several differently indexed opposite steps use different far transition positions; arrows from \(p\) to different targets use distinct right translations. Hence the resulting finite sets converge to \(A\) at both times, proving nonwandering.

When \(p\notin A,c=0,a,b\ge1\), use \(\max(a,b)\) upward-to-downward arrows and \(\max(a,b)\) downward-to-upward arrows, distributing endpoints to cover every step of each type. Every ordered step pair is available, so this requires exactly \(2\max(a,b)\) distinct arrows. When \(p\in A\), first use the two arrows \(p\leftrightarrow v\) for each of the \(c\) finite-block vertices. Match \(\min(a,b)\) upward and downward steps in opposite directed pairs. For every unmatched step, add its two arrows to and from \(p\). This uses \(2c+2\max(a,b)\) arrows and covers \(p\) unless there are no unmatched steps and \(c=0\); in that sole case add \(p\to p\). The lower bounds of Step 2 are attained in all cases. Because \(F_n(Y)\subset F_{n+1}(Y)\) is a closed invariant subspace, realization at the minimum order implies realization at all greater orders. This proves the formula.

## Verification
The standalone `verify.py` constructs the finite directed endpoint relation and independently finds minimal edge counts via an exact dynamic program over in/out-coverage bitmasks. It compares the result with the formula for all \(a,b,c\in\{0,1,2\}\) and either choice of whether \(p\) is present, excluding the empty set. It then constructs explicit simultaneous binary-configuration witnesses at a large common shift time and checks their local source and target words. The script prints `VERIFY_OK` when all assertions pass. These finite checks verify implementation details; the universal assertion is proved by Steps 1–3, not by enumeration.

## Relationship to prior work
Đorić, arXiv:2610.23058v1 (16 October 2026), constructs this exact quotient homeomorphism and proves the \(n=2\) nonwandering-set description (Proposition 7): pairs \(\{p,v\}\) and opposite-step pairs \(\{x_r,y_s\}\). The present threshold specializes exactly to that result at \(n=2\), while determining membership and the minimal order for **every finite set** at all higher symmetric-product levels. The earlier 2012 work of Gómez-Rueda, Illanes and Méndez studies transfer of dynamical properties on symmetric products of continua; its abstract does not provide the stated explicit countable-quotient filtration. Related polynomial-entropy results of Đorić and collaborators measure a different invariant and do not imply this nonwandering-set classification.

## Limitations
This is a complete classification for the specified, explicitly constructed countable compact quotient system, not a general classification for arbitrary subshifts or continuum homeomorphisms. It makes no assertion about the chain-recurrent set of any induced system and does not compute polynomial entropy. Finite-window tests are not a proof of all-time nonwandering. Priority may be affected by general results under alternative terminology; the primary new-paper comparison was made using its full open text, while the 2012 article's full text could not be inspected and its abstract-level comparison leaves residual historical risk. Independent validation has not been performed.

## References
1. M. Đorić, *A note on the non-wandering dynamics in the n-fold symmetric products*, arXiv:2610.23058v1, first publicly posted 16 October 2026, https://arxiv.org/html/2610.23058v1.
2. J. L. Gómez-Rueda, A. Illanes and H. Méndez, *Dynamic properties for the induced maps in the symmetric products*, Chaos, Solitons & Fractals 45 (2012), 1180–1187, https://doi.org/10.1016/j.chaos.2012.05.003.
3. M. Đorić, J. Katić and B. Lasković, *On Polynomial Entropy Of Induced Maps On Symmetric Products*, Acta Math. Hungar. 171 (2023), 334–347, https://doi.org/10.1007/s10474-023-01386-8.
4. M. Đorić, *Polynomial entropy on the n-fold symmetric product and its suspension*, arXiv:2507.10126 (2025), https://arxiv.org/abs/2507.10126.
