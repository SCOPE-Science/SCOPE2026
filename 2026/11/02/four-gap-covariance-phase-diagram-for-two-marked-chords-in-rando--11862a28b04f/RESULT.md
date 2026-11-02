# Four-gap covariance phase diagram for two marked chords in random matchings

## Finding

Fix two disjoint endpoint-pairs \(e\) and \(f\) among \(2n\) cyclically ordered points, and condition a uniformly random perfect matching to contain both prescribed chords. Let \(X\) and \(Y\) count the *remaining* chords crossing \(e\) and \(f\), respectively. Write \(a,b,c,d\) for the four intersection-cell sizes defined below, with \(a+b+c+d=2n-4\). For every integer \(n\ge4\),

\[
\boxed{\operatorname{Cov}(X,Y)=\frac{2\left[(ad-bc)^2-ad(a+d-1)-bc(b+c-1)\right]}{(2n-5)^2(2n-7)}.}
\]

This is an exact sign classification, not just an asymptotic approximation. If the two prescribed chords do not cross, their crossing degrees have nonnegative covariance; it is positive exactly when the two disjoint interior arcs contain at least two unmarked endpoints each. If the prescribed chords cross, the covariance can have either sign, even when all four intervening gaps contain endpoints. For \(n=6\), the four cell sizes \((3,1,1,3)\) give covariance \(36/245>0\), whereas \((2,2,2,2)\) give covariance \(-48/245<0\). With all four gap sizes strictly positive, \(n=6\) is the first possible positive example; when empty gaps are permitted, positive examples already exist at \(n=4\).

The sign law also has contrasting asymptotic regimes. For \((a,b,c,d)=(k,k,k,k)\), the covariance tends to \(-1/8\) as \(k\to\infty\). For \((a,b,c,d)=(3k,k,k,3k)\), it is positive and asymptotic to \(k/4\).

## Assumptions and scope

A chord diagram is a perfect matching on \(2n\) distinct, cyclically ordered endpoints. The random diagram is uniform among the matchings containing the prescribed disjoint endpoint-pairs \(e\) and \(f\). Equivalently, its \(N=2n-4\) remaining endpoints are uniformly perfectly matched. Here \(n\ge4\), so \(N\ge4\). The two marked chords may cross or not.

Choose either open complementary arc of \(e\), and let \(U\) be its unmarked endpoints. Independently choose either open complementary arc of \(f\), and call its unmarked endpoints \(V\). With \(W\) the set of all unmarked endpoints, define

\[
a=|U\cap V|,\qquad b=|U\setminus V|,\qquad c=|V\setminus U|,\qquad d=|W\setminus(U\cup V)|.
\]

All four parameters are nonnegative integers and sum to \(N\). Different choices of complementary arcs only permute the cells and preserve the displayed covariance. A random residual chord crosses a marked chord if and only if its endpoints lie on opposite sides of the corresponding partition. Adding the deterministic crossing indicator between \(e\) and \(f\) to both full graph degrees does not change their covariance, so the theorem also describes the covariance of their degrees in the entire intersection graph.

## Proof

**1. Exact matching-indicator moments.** Put \(M=N-1=2n-5\). For any distinct unmarked vertices \(u,v\), let \(I_{uv}\) indicate that the residual matching pairs them. Then \(\mathbb E I_{uv}=1/M\). For two *different* pairs with four distinct endpoints, \(\mathbb E[I_{uv}I_{xy}]=1/[M(M-2)]\); for pairs sharing exactly one endpoint the product is zero. These follow by matching the partner of one fixed endpoint and then, where appropriate, matching another partner among the \(N-3\) available points.

Let \(\chi_{uv}\) be one if \(\{u,v\}\) straddles \(U\) and its complement; let \(\psi_{uv}\) similarly straddle \(V\). Then \(X=\sum_{u<v}\chi_{uv}I_{uv}\) and \(Y=\sum_{u<v}\psi_{uv}I_{uv}\). Write

\[
A=(a+b)(c+d),\quad B=(a+c)(b+d),\quad C=ad+bc.
\]

Here \(A\) and \(B\) count potential pairs crossing the respective marked chords, while \(C\) counts potential pairs crossing both. Thus \(\mathbb EX=A/M\) and \(\mathbb EY=B/M\).

**2. Account for overlapping potential pairs.** Let \(d_U(v)\) be the number of vertices on the opposite side of \(U\) from \(v\), and define \(d_V(v)\) analogously. Direct cell counting gives

\[
Q:=\sum_{v\in W}d_U(v)d_V(v)
=a(c+d)(b+d)+b(c+d)(a+c)+c(a+b)(b+d)+d(a+b)(a+c).
\]

The ordered sum over a potential \(U\)-straddling pair and a potential \(V\)-straddling pair that *share at least one endpoint* is \(Q-C\). Indeed, summing over their shared vertex counts an identical pair twice, while it should be counted once. Consequently the number of ordered **disjoint** eligible pair-pairs is \(AB-Q+C\), and the matching-indicator moments give

\[
\mathbb E[XY]=\frac{C}{M}+\frac{AB-Q+C}{M(M-2)}.
\]

Subtracting \(AB/M^2\) yields

\[
\operatorname{Cov}(X,Y)
=\frac{M(M-1)C-MQ+2AB}{M^2(M-2)}.
\]

**3. Factorization.** Expanding the explicit expressions for \(A,B,C,Q\) and collecting terms gives the identity

\[
M(M-1)C-MQ+2AB
=2\left[ad(a-1)(d-1)+bc(b-1)(c-1)-2abcd\right]
\]

\[
=2\left[(ad-bc)^2-ad(a+d-1)-bc(b+c-1)\right].
\]

Substitution of \(M=2n-5\) proves the exact covariance formula for every allowed composition and every placement of the marked chords.

**4. The geometric sign boundary.** If the marked chords are noncrossing, choose their two interior arcs so that they do not overlap. They contain \(s\) and \(t\) unmarked points, respectively. Then \((a,b,c,d)=(0,s,t,N-s-t)\) and the factorization becomes

\[
\operatorname{Cov}(X,Y)=\frac{2st(s-1)(t-1)}{(2n-5)^2(2n-7)}\ge0,
\]

strictly positive precisely when \(s,t\ge2\). If they cross, their four open gap lengths (in suitable cyclic order) realize the four cell sizes. The covariance is positive, zero or negative precisely as \((ad-bc)^2\) is greater than, equal to or less than \(ad(a+d-1)+bc(b+c-1)\). For four **positive** gap sizes, at \(n=4\) there is only \((1,1,1,1)\), giving a negative value. At \(n=5\), the multiset of four positive sizes summing to six is either \((3,1,1,1)\) or \((2,2,1,1)\); both arrangements of the two 2's in the latter case give negative numerators. At \(n=6\) the positive example \((3,1,1,3)\) exists, establishing sharpness under the strictly-positive-gap condition.

When empty gaps are allowed, \((0,2,2,0)\) is an admissible crossing-chord layout already at \(n=4\), with covariance \(8/9>0\). Thus the all-positive-gap condition in the first-positive statement is necessary.

**5. Asymptotic contrast.** In the balanced case \((a,b,c,d)=(k,k,k,k)\), the covariance equals

\[
-\frac{4k^2(2k-1)}{(4k-1)^2(4k-3)}\longrightarrow-\frac18.
\]

For \((a,b,c,d)=(3k,k,k,3k)\), it equals

\[
\frac{4k^2(32k^2-28k+5)}{(8k-1)^2(8k-3)}\sim\frac{k}{4}>0.
\]

Both families have four nonempty gaps, showing a persistent structural distinction and different covariance scales.

## Verification

Run the standalone Python 3 checker with `python verify_two_marked_chords.py`. It requires only the Python standard library. It enumerates **every** four-gap composition and all three pairings of the four prescribed endpoints for \(n=4,5,6,7\), and then enumerates every matching of the remaining endpoints for each case. It checks all first moments, both signs of the crossing-degree covariance, and the rational closed form without floating-point arithmetic: 1,710 marked layouts and 866,880 layout–residual-matching combinations. A separate exact-arithmetic implementation of the pair-indicator moment identity compares the algebraic and factored formulas on 19,149 four-cell compositions through 28 residual endpoints. These finite computations verify the finite cases only; the all-size result rests on the preceding proof.

## Relationship to prior work

Acan (2015) studies the crossing degree of a **single** chord in the same uniform chord-diagram model, including its distributional limit and moments conditional on one chord's span. Flajolet and Noy (2000) compute global crossing-count moments and limit laws. Paguyo (2021; revised 2023) gives rates for the total-crossing central limit theorem. These do not state an exact joint covariance **conditional on two prescribed chords and their four arc gaps**, nor the positive/negative sign phase diagram above. The pair-indicator probabilities are elementary and can be extracted from classical perfect-matching counting; the contribution assessed here is the four-cell factorization, complete geometric sign law, sharp four-positive-gap boundary, and contrasting asymptotic regimes. No claim of exhaustive historical novelty is made.

## Limitations

The theorem concerns uniform **perfect matchings conditioned on the existence of two disjoint prescribed chords**, not unconditioned pairs selected uniformly from the finished intersection graph. It assumes \(n\ge4\); the smaller residual matching is deterministic and the displayed denominator is not applicable. Covariance signs do not establish stochastic or likelihood-ratio ordering of the joint law. The literature comparison does not exclude equivalent formulas implicitly contained in broader matching-moment identities or older inaccessible sources. Independent validation has not been performed.

## References

1. H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1, January 7, 2015, https://arxiv.org/abs/1501.01489 . The preprint states primary MSC 60C05; Section 2 treats one-chord degree statistics.
2. P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA Research Report 3914, March 2000, https://algo.inria.fr/flajolet/Publications/FlNo00.pdf . Its Section 2 treats the global crossing count.
3. J. E. Paguyo, *Convergence Rates of Limit Theorems in Random Chord Diagrams*, arXiv:2104.01134, first posted April 2, 2021, https://arxiv.org/abs/2104.01134 . Its Section 2 treats total-crossing normal approximation.
