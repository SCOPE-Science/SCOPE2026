# Radial Bregman boundary-cluster dichotomy and the dimension-one exception

## Finding

A complete boundary-limit classification holds for strictly convex radial distance generators that remain finite on the closed Euclidean ball. In dimension one every approach from the interior gives vanishing Bregman distance. In dimension at least two, **finite limiting radial slope** is precisely the threshold for the same property. If the radial slope instead diverges, then at each boundary point the divergence admits **every prescribed finite nonnegative limit and also infinity** along different interior approaches.

In particular, any essentially smooth strictly convex radial kernel with finite values on the closed ball necessarily fails the boundary-continuity requirement of the Bregman-with-zone assumption in dimension at least two; the one-dimensional kernel satisfies it. This classifies the radial situation, rather than only producing a failure example for one function.

## Assumptions and scope

Let \(R>0\) and \(n\ge1\), and equip \(\mathbb R^n\) with the Euclidean norm. Let \(h:[0,R]\to\mathbb R\) be finite, continuous, and strictly convex, with \(h\in C^1([0,R))\) and \(h'(0)=0\). Convexity then gives \(h'(r)\ge0\) and makes \(h'\) nondecreasing. Define

\[
\Phi(z)=\begin{cases}h(\|z\|),&\|z\|\le R,\\+\infty,&\|z\|>R.\end{cases}
\]

The strict convexity and nondecreasing radial profile ensure that \(\Phi\) is proper, closed, and strictly convex; it is continuously differentiable on the open ball, with \(\nabla\Phi(y)=h'(\|y\|)y/\|y\|\) away from the origin, and gradient zero at the origin. For a point \(x\) in the closed ball and \(y\) in the open ball, set

\[
D_\Phi(x,y)=\Phi(x)-\Phi(y)-\langle\nabla\Phi(y),x-y\rangle.
\]

Fix a boundary point \(x\) with \(\|x\|=R\). Its **boundary cluster set** consists of extended real numbers \(a\in[0,\infty]\) for which there exists an interior sequence \(y_j\to x\) with \(D_\Phi(x,y_j)\to a\); the symbol \(\infty\) means divergence to positive infinity. The radial slope limit \(L=\lim_{r\uparrow R}h'(r)\) exists in \([0,\infty]\) by monotonicity.

The Bregman-with-zone requirement here means (i) \(D_\Phi(x,y_j)\to0\) whenever an interior sequence \(y_j\to x\) approaches any point \(x\) of the closed domain, and (ii) each map \(y\mapsto D_\Phi(x,y)\) has bounded sublevel sets when \(x\) is on the boundary. It is not the separate notion of consistency of Bregman projection algorithms.

## Proof

**Step 1 (the radial–angular identity).** Take \(x=Re_1\), \(y=rv\), where \(0<r<R\) and \(\|v\|=1\). Put \(c=\langle e_1,v\rangle\). Direct substitution into the definition gives

\[
D_\Phi(Re_1,rv)=A(r)+Rh'(r)(1-c),\qquad
A(r):=h(R)-h(r)-h'(r)(R-r).
\]

The supporting-line inequality for convex \(h\) yields \(A(r)\ge0\). Since \(h'(r)\ge0\), also

\[
0\le A(r)\le h(R)-h(r)\longrightarrow0\quad(r\uparrow R).
\]

This identity and inequality apply equally after rotating coordinates to any chosen boundary point.

**Step 2 (one dimension).** If \(n=1\), any interior \(y_j\to R\) eventually lies on the positive ray. Thus \(c=1\) and \(D_\Phi(R,y_j)=A(|y_j|)\to0\). At \(-R\), use the negative ray instead. At interior points continuity of \(\Phi\) and \(\nabla\Phi\) gives \(D_\Phi(x,y_j)\to0\). This holds whether or not \(L\) is finite.

**Step 3 (any dimension when \(L<\infty\)).** Since \(0\le h'(r)\le L\), the gradient is bounded by \(L\) everywhere in the open ball. If \(y_j\to x\) with \(x\) anywhere in the closed ball, continuity of \(\Phi\) and

\[
|\langle\nabla\Phi(y_j),x-y_j\rangle|\le L\|x-y_j\|\longrightarrow0
\]

show that \(D_\Phi(x,y_j)\to0\).

**Step 4 (higher-dimensional steepness: every finite limit).** Suppose \(n\ge2\) and \(L=\infty\). Fix arbitrary \(a\ge0\) and any radii \(r_j\uparrow R\), passing to sufficiently large indices so that \(h'(r_j)>0\) and \(0\le a/(Rh'(r_j))\le2\). Because two orthogonal unit vectors exist, select a unit \(v_j\) with

\[
\langle e_1,v_j\rangle=1-\frac{a}{Rh'(r_j)}.
\]

Then \(r_jv_j\to Re_1\) and the identity in Step 1 yields **exactly**

\[
D_\Phi(Re_1,r_jv_j)=A(r_j)+a\longrightarrow a.
\]

Thus every finite nonnegative number is a boundary cluster value, including zero.

**Step 5 (higher-dimensional steepness: infinite limit).** With the same radii, choose instead

\[
\langle e_1,v_j\rangle=1-\frac1{\sqrt{h'(r_j)}}.
\]

For sufficiently large \(j\) this is a legitimate cosine and tends to one. Consequently \(r_jv_j\to Re_1\), but

\[
D_\Phi(Re_1,r_jv_j)=A(r_j)+R\sqrt{h'(r_j)}\longrightarrow\infty.
\]

By convexity no Bregman distance is negative. Therefore the cluster set is **exactly** \([0,\infty]\), not merely a set containing a divergent path. Rotation covers every boundary point.

**Step 6 (the zone-condition iff statement).** Steps 2–5 establish boundary continuity exactly when \(n=1\) or \(L<\infty\). Interior continuity always holds. The sublevel sets in requirement (ii) are automatically bounded because the variable \(y\) ranges over a bounded open ball. Finally, essential smoothness of this differentiable radial kernel at the ball boundary is equivalent to \(\|\nabla\Phi(y)\|=h'(\|y\|)\to\infty\), namely \(L=\infty\). Combined with strict convexity, this is the Legendre case. It satisfies the zone conditions exactly when \(n=1\). \(\square\)

## Verification

The critical algebraic identity comes from \(\langle\nabla\Phi(rv),Re_1-rv\rangle=h'(r)(Rc-r)\). The range of allowable angular cosines is \([-1,1]\); both prescribed cosine sequences eventually lie in that interval and tend to one. The radial supporting-line error obeys the explicit two-sided bound above and hence tends to zero, regardless of how fast \(h'(r)\) diverges.

As a check on a concrete nonpolynomial kernel, take \(R=1\) and \(h(r)=-\sqrt{1-r^2}\), which has \(h'(r)=r/\sqrt{1-r^2}\). Then

\[
A(r)=\frac{1-r}{\sqrt{1-r^2}}\longrightarrow0.
\]

For any given finite \(a\ge0\), the cosine \(1-a/h'(r)\) gives the **exact** identity \(D_\Phi(e_1,rv)=A(r)+a\). This analytically reproduces the source's divergent Hellinger-type example while demonstrating all finite angular boundary limits. No finite numerical experiment is used as a proof of the universal classification.

## Relationship to prior work

Ou, Latafat, and Themelis (arXiv:2508.01353, earliest submission 2 August 2025) formulate the two Bregman-with-zone requirements in Assumption 2.4. Their Example 2.5 proves that a **specific** finite Hellinger-type radial kernel satisfies the requirements in one dimension but fails for dimensions at least two. Their Section 5.6 also studies radial kernels with nonclosed effective domains. Those statements do not supply the radial-slope iff criterion, the full classification over every finite continuous strictly convex radial profile, or the exact entire extended boundary cluster set. The proof here recovers their example as a strict special case.

Solodov and Svaiter (2000), Definition 2.1, provide the original zone requirements, and their Section 2 develops convergence-consistency consequences under the assumption; the inspected definition and results do not classify the above radial kernels. Bauschke and Borwein (1997), especially Sections 5–6, study Bregman/Legendre functions including one-dimensional Hellinger examples, products, and a different nonradial two-dimensional failure example; no result in the inspected sections asserts the radial universal iff or boundary cluster-set result. The classification is not obtained by claiming that a failed literature search proves novelty.

## Limitations

This theorem concerns **finite-valued continuous kernels on the closed Euclidean ball**, not log barriers that take \(+\infty\) on the sphere, nor all convex bodies, nonradial mirrors, or infinite-dimensional spaces. It concerns a **sufficient analytical Bregman-with-zone hypothesis**, not whether the adaptive optimization algorithms themselves converge without that hypothesis. The ordinary definitions of a Bregman distance and of a Legendre function are standard; the claimed contribution is the sharp radial boundary classification and its complete attainable-limit set. No independent external validation has been performed. Search coverage cannot rule out unindexed earlier statements or stronger equivalences.

## References

1. H. Ou, P. Latafat, and A. Themelis, *Linesearch-free adaptive Bregman proximal gradient for convex minimization under local relative smoothness*, arXiv:2508.01353v2, Assumption 2.4, Example 2.5, Theorem 2.7, and Section 5.6. https://arxiv.org/pdf/2508.01353 (first public submission 2025-08-02: https://arxiv.org/abs/2508.01353).
2. M. V. Solodov and B. F. Svaiter, *An inexact hybrid generalized proximal point algorithm and some new results on the theory of Bregman functions*, Mathematics of Operations Research 25 (2000), 214–230, especially Definition 2.1 and Theorem 2.4. https://pages.cs.wisc.edu/~solodov/solsva00Bregman.pdf .
3. H. H. Bauschke and J. M. Borwein, *Legendre functions and the method of random Bregman projections*, Journal of Convex Analysis 4 (1997), 27–67, especially Sections 5–6. https://cmps-people.ok.ubc.ca/bauschke/Research/07.pdf .
